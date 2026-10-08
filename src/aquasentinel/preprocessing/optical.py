"""AS-102 orchestration: metadata first, bounded native pixels, masks, lineage, cache."""

from __future__ import annotations

import platform
from dataclasses import asdict, replace
from datetime import UTC, datetime

import numpy as np
import rasterio

from aquasentinel.ingestion.planetary_computer import read_bytes, sign_asset
from aquasentinel.ingestion.sentinel2 import Sentinel2Candidate, _polygon_geometry
from aquasentinel.ingestion.sentinel2_assets import BANDS, resolve_optical_source
from aquasentinel.preprocessing.alignment import (
    analysis_grid,
    aoi_grid_mask,
    read_native_asset,
    scl_on_native,
    warp_array,
)
from aquasentinel.preprocessing.cache import cache_identity, load_cache, write_cache
from aquasentinel.preprocessing.masks import (
    INVALID_SCL,
    SUPPORT_POLICY,
    VALID_SCL,
    interpolation_support,
    scene_statistics,
    scl_masks,
)
from aquasentinel.preprocessing.metadata import (
    MAX_XML_BYTES,
    decode_reflectance,
    parse_product_metadata,
)
from aquasentinel.preprocessing.models import PreprocessedOpticalScene, geometry_digest
from aquasentinel.provenance.models import DerivedProductRecord
from aquasentinel.provenance.serialization import derived_product_to_dict, source_record_to_dict
from aquasentinel.runtime import RuntimeContext

PROCESSING_VERSION = "as102-v1"


def preprocess_optical_scene(
    context: RuntimeContext,
    candidate: Sentinel2Candidate | None = None,
    *,
    known_cache_id: str | None = None,
) -> PreprocessedOpticalScene:
    if known_cache_id is not None:
        scene = load_cache(context.config.cache_dir, known_cache_id)
        geometry = _polygon_geometry(context.primary_validation_aoi)
        grid = analysis_grid(geometry, context.config.optical)
        if (
            grid != scene.grid
            or geometry_digest(geometry)
            != (scene.processing_parameters["identity"]["aoi_geometry_digest"])
        ):
            raise ValueError("Known cache does not match configured AOI/grid.")
        if (
            candidate is not None
            and candidate.to_source_record() != scene.resolved_source.discovery_source
        ):
            raise ValueError("Known cache does not match supplied discovery candidate.")
        return scene
    if candidate is None:
        raise ValueError("A discovery candidate or known cache ID is required.")
    context.config.validate()
    settings = context.config.optical
    geometry = _polygon_geometry(context.primary_validation_aoi)
    grid = analysis_grid(geometry, settings)
    resolved = resolve_optical_source(candidate, geometry, settings)
    signed = sign_asset(resolved.asset("product-metadata").href, settings)
    try:
        body = read_bytes(
            signed,
            timeout=settings.timeout_seconds,
            max_bytes=MAX_XML_BYTES,
        )
    finally:
        signed = None
    decoding = parse_product_metadata(body, resolved.processing_baseline)
    identity = {
        "processing_version": PROCESSING_VERSION,
        "pc_source": source_record_to_dict(resolved.source),
        "discovery_source": source_record_to_dict(resolved.discovery_source),
        "observation_match": resolved.identity.to_dict(),
        "pc_processing_baseline": resolved.processing_baseline,
        "pc_generation_time": resolved.generation_time,
        "pc_provider_metadata": resolved.provider_metadata,
        "discovery_processing": resolved.discovery_processing,
        "assets": [{**asdict(a), "roles": list(a.roles)} for a in resolved.assets],
        "decoding": decoding.to_dict(),
        "aoi_geometry_digest": geometry_digest(geometry),
        "target_grid": grid.to_dict(),
        "bands": list(BANDS),
        "resampling": {"reflectance": "bilinear", "categorical": "nearest"},
        "mask_policy": {
            "invalid_scl": list(INVALID_SCL),
            "valid_scl": list(VALID_SCL),
            "water_scl": 6,
            "unknown": "invalid",
            "aoi": "pixel-centre",
        },
        "interpolation_support_policy": SUPPORT_POLICY,
        "software_versions": {
            "python": platform.python_version(),
            "numpy": np.__version__,
            "rasterio": rasterio.__version__,
            "gdal": rasterio.__gdal_version__,
        },
    }
    cache_id = cache_identity(identity)
    destination = context.config.cache_dir / "as102" / cache_id
    if destination.exists():
        return load_cache(context.config.cache_dir, cache_id)
    native_scl = read_native_asset(resolved.asset("SCL"), grid, settings)
    scl = warp_array(native_scl.data, native_scl, grid, categorical=True, nodata=native_scl.nodata)
    aoi = aoi_grid_mask(geometry, grid)
    valid_data, water = scl_masks(scl, aoi)
    support = np.ones(grid.shape, dtype=bool)
    reflectance, source_grids, support_counts = {}, {"SCL": native_scl.header}, {}
    for band in BANDS:
        native = read_native_asset(resolved.asset(band), grid, settings)
        native_quality = scl_on_native(native_scl, native)
        decoded = decode_reflectance(native.data, native.nodata, band, decoding)
        source_valid = np.isin(native_quality, VALID_SCL) & np.isfinite(decoded)
        decoded[~source_valid] = np.nan
        reflectance[band] = warp_array(decoded, native, grid, nodata=np.nan)
        band_support = interpolation_support(source_valid & (native_quality == 6), native, grid)
        support &= band_support
        support_counts[band] = int(np.count_nonzero(water & band_support))
        source_grids[band] = native.header
        valid_data &= np.isfinite(reflectance[band])
    support &= aoi
    valid_water = valid_data & water & support
    statistics = scene_statistics(aoi, valid_data, water, valid_water)
    parameters = {
        "identity": identity,
        "source_grids": source_grids,
        "statistics": asdict(statistics),
        "water_support_counts_by_band": support_counts,
        "candidate_water_excluded": statistics.candidate_water_count - statistics.valid_water_count,
        "decoding_formula": "(DN + band_offset) / BOA_QUANTIFICATION_VALUE",
        "scientific_limit": "L2A BOA surface reflectance is not aquatic Rrs or HAB evidence.",
    }
    provenance = DerivedProductRecord(
        f"optical:{cache_id}",
        "preprocessed_optical_scene",
        datetime.now(UTC),
        PROCESSING_VERSION,
        (resolved.source.source_id,),
        parameters,
    )
    derived_product_to_dict(provenance)
    resolved = replace(resolved, native_grids=source_grids, decoding_metadata=decoding.to_dict())
    scene = PreprocessedOpticalScene(
        resolved,
        grid,
        reflectance,
        scl,
        aoi,
        valid_data,
        water,
        valid_water,
        support,
        statistics,
        parameters,
        cache_id,
        provenance,
    )
    scene.validate()
    write_cache(scene, context.config.cache_dir)
    return scene
