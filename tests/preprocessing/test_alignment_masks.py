from dataclasses import replace

import numpy as np
import pytest
import rasterio
from rasterio import Affine
from rasterio.warp import transform_bounds

from aquasentinel.config import OpticalConfig
from aquasentinel.preprocessing.alignment import (
    NativeRasterWindow,
    analysis_grid,
    aoi_grid_mask,
    bounded_window,
    read_native_asset,
    warp_array,
)
from aquasentinel.preprocessing.masks import interpolation_support, scene_statistics, scl_masks
from aquasentinel.preprocessing.models import AnalysisGrid
from aquasentinel.runtime import build_runtime_context


def small_grid(res=20):
    return AnalysisGrid(
        "EPSG:32640",
        Affine(res, 0, 200000, 0, -res, 2800000),
        10,
        10,
        res,
        (200000, 2800000 - 10 * res, 200000 + 10 * res, 2800000),
        "test-grid",
    )


def test_current_aoi_grid_deterministic():
    context = build_runtime_context()
    geometry = {"type": "Polygon", "coordinates": context.primary_validation_aoi.coordinates}
    grid = analysis_grid(geometry, context.config.optical)
    assert grid == analysis_grid(geometry, OpticalConfig())
    assert grid.bounds == (249020, 2702860, 255220, 2707420)
    assert grid.shape == (228, 310)
    assert list(grid.transform)[:6] == [20, 0, 249020, 0, -20, 2707420]
    mask = aoi_grid_mask(geometry, grid)
    assert mask.dtype == bool
    assert 0 < mask.sum() < 228 * 310


def test_cross_crs_reflectance_and_categorical_alignment():
    grid = small_grid()
    left, _bottom, _right, top = transform_bounds(
        grid.crs, "EPSG:32639", *grid.bounds, densify_pts=21
    )
    transform = Affine(10, 0, left - 100, 0, -10, top + 100)
    source = NativeRasterWindow(
        np.full((60, 60), 6, dtype=np.uint8), "EPSG:32639", transform, 0, {}
    )
    out = warp_array(source.data, source, grid, categorical=True, nodata=0)
    values = warp_array(np.full((60, 60), 0.123, np.float32), source, grid, nodata=np.nan)
    assert out.shape == values.shape == grid.shape
    assert np.all(out == 6)
    np.testing.assert_allclose(values, 0.123)
    assert np.all(interpolation_support(np.ones((60, 60), bool), source, grid))


@pytest.mark.parametrize("contaminant", [0, 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 255])
def test_invalid_or_land_support_rejected(contaminant):
    grid = small_grid()
    source = NativeRasterWindow(
        np.full((28, 28), 6, np.uint8), grid.crs, Affine(10, 0, 199960, 0, -10, 2800040), 0, {}
    )
    good = np.ones(source.data.shape, bool)
    # One bad native contributor near the centre of a target water pixel.
    good[14, 14] = contaminant == 6
    support = interpolation_support(good, source, grid)
    assert not support[5, 5]
    assert support[1, 1]


def test_nodata_support_and_conservative_window_edge():
    grid = small_grid()
    source = NativeRasterWindow(np.ones((10, 10), np.uint16), grid.crs, grid.transform, 0, {})
    good = np.ones((10, 10), bool)
    good[5, 5] = False
    support = interpolation_support(good, source, grid)
    assert not support[5, 5] and not support[4, 5]
    assert not support[0, :].any() and not support[-1, :].any()
    assert support[2, 2]


def test_scl_policy_every_class_and_unknown():
    scl = np.array([list(range(12)) + [255]], np.uint8)
    valid, water = scl_masks(scl, np.ones(scl.shape, bool))
    assert np.flatnonzero(valid).tolist() == [4, 5, 6]
    assert np.flatnonzero(water).tolist() == [6]
    assert not valid[0, 2]  # Provider class 2: dark-area pixels, conservatively excluded.


def test_fraction_denominators_and_zero_water():
    aoi = np.ones((2, 2), bool)
    data = np.array([[True, True], [False, False]])
    water = np.array([[True, False], [True, False]])
    valid = np.array([[True, False], [False, False]])
    stats = scene_statistics(aoi, data, water, valid)
    assert stats.aoi_pixel_count == 4 and stats.valid_data_count == 2
    assert stats.valid_water_fraction_of_aoi == 0.25
    assert stats.water_retained_fraction == 0.5
    zero = scene_statistics(aoi, data, np.zeros((2, 2), bool), np.zeros((2, 2), bool))
    assert zero.valid_water_count == 0 and zero.water_retained_fraction is None
    none_retained = scene_statistics(aoi, data, water, np.zeros((2, 2), bool))
    assert none_retained.valid_water_fraction_of_aoi == 0
    assert none_retained.water_retained_fraction == 0


def test_local_native_header_window_read(monkeypatch, tmp_path, resolved):
    grid = small_grid()
    path = tmp_path / "native.tif"
    with rasterio.open(
        path,
        "w",
        driver="GTiff",
        width=200,
        height=200,
        count=1,
        dtype="uint16",
        crs=grid.crs,
        transform=Affine(10, 0, 199500, 0, -10, 2800500),
        nodata=0,
    ) as ds:
        ds.write(np.full((200, 200), 1500, np.uint16), 1)
    monkeypatch.setattr("aquasentinel.preprocessing.alignment.sign_asset", lambda *a: str(path))
    result = read_native_asset(resolved.asset("B02"), grid, OpticalConfig())
    assert result.data.shape == (28, 28)
    assert result.header["native_resolution"] == 10
    assert result.header["window"] == [46, 46, 28, 28]
    assert np.all(result.data == 1500)
    with rasterio.open(path) as ds, pytest.raises(ValueError, match="Full-scene"):
        bounded_window(ds, replace(grid, bounds=(199500, 2798500, 201500, 2800500)))


def test_raster_failure_does_not_leak_signed_url(monkeypatch, resolved):
    from aquasentinel.ingestion.planetary_computer import AssetAccessError

    secret = "https://sentinel2l2a01.blob.core.windows.net/test.tif?temporary=never-print"
    monkeypatch.setattr("aquasentinel.preprocessing.alignment.sign_asset", lambda *a: secret)

    def failed(*a, **k):
        raise rasterio.errors.RasterioIOError(secret)

    monkeypatch.setattr(rasterio, "open", failed)
    with pytest.raises(AssetAccessError) as error:
        read_native_asset(resolved.asset("B02"), small_grid(), OpticalConfig())
    assert "never-print" not in str(error.value)
    assert error.value.__suppress_context__
    assert error.value.__context__ is None


def test_bilinear_gradient_and_nearest_classification():
    grid = small_grid()
    source = NativeRasterWindow(
        np.ones((28, 28), np.uint16), grid.crs, Affine(10, 0, 199960, 0, -10, 2800040), 0, {}
    )
    rows, columns = np.indices((28, 28))
    gradient = (rows + 2 * columns).astype(np.float32)
    result = warp_array(gradient, source, grid, nodata=np.nan)
    # Interior 20 m target centres lie halfway between native 10 m centres.
    assert result[5, 5] == pytest.approx(43.5)
    categories = (columns % 2 + 4).astype(np.uint8)
    nearest = warp_array(categories, source, grid, categorical=True, nodata=0)
    assert set(np.unique(nearest)) <= {4, 5}


@pytest.mark.parametrize("fail", [False, True])
@pytest.mark.parametrize("previously_disabled", [False, True])
def test_signed_read_suppresses_family_and_restores_state(
    monkeypatch, resolved, caplog, tmp_path, fail, previously_disabled
):
    import logging

    from aquasentinel.ingestion.planetary_computer import AssetAccessError

    grid = small_grid()
    path = tmp_path / "native.tif"
    real_open = rasterio.open
    with real_open(path, "w", driver="GTiff", width=200, height=200, count=1,
                   dtype="uint16", crs=grid.crs,
                   transform=Affine(10, 0, 199500, 0, -10, 2800500), nodata=0) as ds:
        ds.write(np.full((200, 200), 1500, np.uint16), 1)
    signed = ("https://sentinel2l2a01.blob.core.windows.net/test.tif?"
              "sv=2023-11-03&se=fake-expiry&sp=r&sig=fake-secret")
    parent = logging.getLogger("rasterio")
    child = logging.getLogger("rasterio._base")
    monkeypatch.setattr(parent, "disabled", previously_disabled)
    before = (parent.disabled, parent.handlers, parent.propagate, parent.level, child.disabled)
    monkeypatch.setattr("aquasentinel.preprocessing.alignment.sign_asset", lambda *a: signed)

    def opened(*args, **kwargs):
        assert parent.disabled and child.disabled
        parent.warning("%s", signed)
        child.warning("sig=fake-secret")
        # A fresh child with its own explicit level still cannot propagate past the parent.
        late = logging.getLogger(f"rasterio.review_late_{fail}_{previously_disabled}")
        with monkeypatch.context() as scoped:
            scoped.setattr(late, "level", logging.DEBUG)
            late.warning("%s", signed)
        if fail:
            raise rasterio.errors.RasterioIOError(signed)
        return real_open(path)

    monkeypatch.setattr(rasterio, "open", opened)
    caplog.clear()
    with caplog.at_level(logging.WARNING):
        if fail:
            with pytest.raises(AssetAccessError) as error:
                read_native_asset(resolved.asset("B02"), grid, OpticalConfig())
            assert "fake-secret" not in str(error.value)
            assert error.value.__context__ is None
        else:
            assert read_native_asset(resolved.asset("B02"), grid, OpticalConfig()).data.shape == (28, 28)
    assert (parent.disabled, parent.handlers, parent.propagate, parent.level, child.disabled) == before
    assert signed not in caplog.text
    assert "fake-secret" not in caplog.text
    assert "fake-expiry" not in caplog.text
    assert not [r for r in caplog.records if r.name.startswith("rasterio")]
