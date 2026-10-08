"""One deterministically snapped grid per AOI; bounded native reads only."""

from __future__ import annotations

import logging
import math
from dataclasses import dataclass
from hashlib import sha256

import numpy as np
import rasterio
from rasterio import Affine
from rasterio.features import bounds, geometry_mask
from rasterio.warp import Resampling, reproject, transform_bounds, transform_geom
from rasterio.windows import Window, from_bounds

from aquasentinel.config import OpticalConfig
from aquasentinel.ingestion.planetary_computer import AssetAccessError, sign_asset
from aquasentinel.ingestion.sentinel2 import AssetReference
from aquasentinel.ingestion.sentinel2_assets import NATIVE_RESOLUTION
from aquasentinel.preprocessing.models import AnalysisGrid


@dataclass(frozen=True)
class NativeRasterWindow:
    data: np.ndarray
    crs: str
    transform: Affine
    nodata: int | float
    header: dict


def analysis_grid(geometry, settings: OpticalConfig) -> AnalysisGrid:
    settings.validate()
    projected = transform_bounds(
        "EPSG:4326", settings.target_crs, *bounds(geometry), densify_pts=21
    )
    resolution = float(settings.target_resolution)
    left, bottom = (math.floor(v / resolution) * resolution for v in projected[:2])
    right, top = (math.ceil(v / resolution) * resolution for v in projected[2:])
    width, height = round((right - left) / resolution), round((top - bottom) / resolution)
    if not 0 < width * height <= 10_000_000:
        raise ValueError("AOI analysis grid is empty or exceeds the bounded P0 size.")
    transform = Affine(resolution, 0, left, 0, -resolution, top)
    identity = f"{settings.target_crs}|{resolution}|{left}|{bottom}|{right}|{top}|{width}|{height}"
    return AnalysisGrid(
        settings.target_crs,
        transform,
        width,
        height,
        resolution,
        (left, bottom, right, top),
        sha256(identity.encode()).hexdigest(),
    )


def aoi_grid_mask(geometry, grid: AnalysisGrid):
    projected = transform_geom("EPSG:4326", grid.crs, geometry)
    return geometry_mask(
        [projected], out_shape=grid.shape, transform=grid.transform, invert=True, all_touched=False
    )


def bounded_window(dataset, grid: AnalysisGrid, halo: int = 4) -> Window:
    source_bounds = transform_bounds(grid.crs, dataset.crs, *grid.bounds, densify_pts=21)
    floating = from_bounds(*source_bounds, transform=dataset.transform)
    left = max(0, math.floor(floating.col_off) - halo)
    top = max(0, math.floor(floating.row_off) - halo)
    right = min(dataset.width, math.ceil(floating.col_off + floating.width) + halo)
    bottom = min(dataset.height, math.ceil(floating.row_off + floating.height) + halo)
    if right <= left or bottom <= top:
        raise ValueError("Source raster does not overlap the AOI grid.")
    if (right - left) * (bottom - top) >= dataset.width * dataset.height:
        raise ValueError("Full-scene reads are forbidden; use a smaller AOI.")
    return Window(left, top, right - left, bottom - top)


def read_native_asset(
    asset: AssetReference, grid: AnalysisGrid, settings: OpticalConfig
) -> NativeRasterWindow:
    signed = sign_asset(asset.href, settings)
    # Silence the family at its parent boundary, including children created during open.
    # Existing children may have their own handlers, so disable those for the scope too.
    logger = logging.getLogger("rasterio")
    previous_handlers, previous_propagate = logger.handlers, logger.propagate
    raster_loggers = [logger, *(
        value for name, value in list(logging.Logger.manager.loggerDict.items())
        if name.startswith("rasterio.") and isinstance(value, logging.Logger)
    )]
    previous_disabled = [(child, child.disabled) for child in raster_loggers]
    logger.handlers = []
    logger.propagate = False
    for child, _ in previous_disabled:
        child.disabled = True
    try:
        with (
            rasterio.Env(
                GDAL_DISABLE_READDIR_ON_OPEN="EMPTY_DIR",
                GDAL_PAM_ENABLED="NO",
                CPL_VSIL_CURL_ALLOWED_EXTENSIONS=".tif",
                GDAL_HTTP_MAX_RETRY=0,
                GDAL_HTTP_TIMEOUT=str(settings.timeout_seconds),
                CPL_DEBUG=False,
            ),
            rasterio.open(signed) as ds,
        ):
            expected_dtype = "uint8" if asset.key == "SCL" else "uint16"
            expected_res = NATIVE_RESOLUTION[asset.key]
            if (
                ds.driver != "GTiff"
                or ds.count != 1
                or ds.crs is None
                or not ds.crs.is_projected
                or ds.crs.linear_units != "metre"
                or ds.width <= 0
                or ds.height <= 0
                or ds.dtypes != (expected_dtype,)
                or ds.nodata is None
                or not math.isfinite(ds.nodata)
                or ds.transform.b != 0
                or ds.transform.d != 0
                or ds.transform.a != expected_res
                or ds.transform.e != -expected_res
            ):
                raise ValueError("Unsupported native COG header/grid/nodata.")
            window = bounded_window(ds, grid)
            data = ds.read(1, window=window)
            header = {
                "driver": ds.driver,
                "crs": ds.crs.to_string(),
                "width": ds.width,
                "height": ds.height,
                "dtype": ds.dtypes[0],
                "nodata": ds.nodata,
                "transform": list(ds.transform)[:6],
                "native_resolution": expected_res,
                "window": [
                    int(window.col_off),
                    int(window.row_off),
                    int(window.width),
                    int(window.height),
                ],
            }
            return NativeRasterWindow(
                data, ds.crs.to_string(), ds.window_transform(window), ds.nodata, header
            )
    except (OSError, ValueError, TypeError, rasterio.errors.RasterioError):
        pass
    finally:
        logger.handlers = previous_handlers
        logger.propagate = previous_propagate
        for child, disabled in previous_disabled:
            child.disabled = disabled
        signed = None
    raise AssetAccessError(
        f"Bounded raster read failed for {asset.key}; diagnostics sanitized."
    ) from None


def warp_array(
    data, source: NativeRasterWindow, grid: AnalysisGrid, *, categorical=False, nodata=None
):
    output = (
        np.zeros(grid.shape, dtype=np.uint8)
        if categorical
        else np.full(grid.shape, np.nan, dtype=np.float32)
    )
    reproject(
        data,
        output,
        src_transform=source.transform,
        src_crs=source.crs,
        dst_transform=grid.transform,
        dst_crs=grid.crs,
        src_nodata=nodata,
        dst_nodata=0 if categorical else np.nan,
        resampling=Resampling.nearest if categorical else Resampling.bilinear,
        num_threads=1,
    )
    return output


def scl_on_native(scl: NativeRasterWindow, native: NativeRasterWindow) -> np.ndarray:
    result = np.zeros(native.data.shape, dtype=np.uint8)
    reproject(
        scl.data,
        result,
        src_transform=scl.transform,
        src_crs=scl.crs,
        dst_transform=native.transform,
        dst_crs=native.crs,
        src_nodata=scl.nodata,
        dst_nodata=0,
        resampling=Resampling.nearest,
        num_threads=1,
    )
    return result
