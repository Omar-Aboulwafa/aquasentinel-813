import json
from dataclasses import replace
from hashlib import sha256

import numpy as np
import pytest
from rasterio import Affine

from aquasentinel.ingestion.sentinel2_assets import BANDS, NATIVE_RESOLUTION
from aquasentinel.preprocessing import optical
from aquasentinel.preprocessing.alignment import NativeRasterWindow, analysis_grid
from aquasentinel.preprocessing.cache import (
    CacheCorruptionError,
    cache_identity,
    canonical_json,
    load_cache,
    write_cache,
)
from aquasentinel.provenance.serialization import derived_product_to_dict
from aquasentinel.runtime import build_runtime_context


@pytest.fixture
def pipeline(monkeypatch, tmp_path, resolved, product_xml):
    context = build_runtime_context()
    context = replace(context, config=replace(context.config, cache_dir=tmp_path / "cache"))
    geometry = {"type": "Polygon", "coordinates": context.primary_validation_aoi.coordinates}
    grid = analysis_grid(geometry, context.config.optical)
    calls = {"resolve": 0, "sign": 0, "xml": 0, "raster": []}

    def resolve(*args):
        calls["resolve"] += 1
        return resolved

    def sign(*args):
        calls["sign"] += 1
        return "https://sentinel2l2a01.blob.core.windows.net/test.xml?temporary=only-memory"

    def xml(*args, **kwargs):
        calls["xml"] += 1
        return product_xml

    def raster(asset, *args):
        calls["raster"].append(asset.key)
        res = NATIVE_RESOLUTION[asset.key]
        scale = round(grid.resolution / res)
        shape = (grid.height * scale + 8, grid.width * scale + 8)
        data = np.full(
            shape, 6 if asset.key == "SCL" else 1500, np.uint8 if asset.key == "SCL" else np.uint16
        )
        transform = Affine(res, 0, grid.bounds[0] - 4 * res, 0, -res, grid.bounds[3] + 4 * res)
        header = {
            "crs": grid.crs,
            "transform": list(transform)[:6],
            "width": 10980,
            "height": 10980,
            "window": [100, 100, shape[1], shape[0]],
            "nodata": 0,
            "native_resolution": res,
            "dtype": str(data.dtype),
            "driver": "GTiff",
        }
        return NativeRasterWindow(data, grid.crs, transform, 0, header)

    monkeypatch.setattr(optical, "resolve_optical_source", resolve)
    monkeypatch.setattr(optical, "sign_asset", sign)
    monkeypatch.setattr(optical, "read_bytes", xml)
    monkeypatch.setattr(optical, "read_native_asset", raster)
    return context, calls


def test_full_pipeline_actual_pixel_provenance_and_shapes(pipeline, cdse_candidate):
    context, calls = pipeline
    scene = optical.preprocess_optical_scene(context, cdse_candidate)
    scene.validate()
    assert scene.grid.shape == (228, 310)
    assert scene.band_order == BANDS
    assert all(
        b.dtype == np.float32 and b.shape == scene.grid.shape for b in scene.reflectance.values()
    )
    assert scene.scl.dtype == np.uint8
    assert scene.provenance.source_ids == (scene.source_id,)
    assert cdse_candidate.to_source_record().source_id not in scene.provenance.source_ids
    assert (
        scene.processing_parameters["identity"]["discovery_source"]["source_id"]
        == cdse_candidate.to_source_record().source_id
    )
    assert scene.statistics.valid_water_count == scene.statistics.aoi_pixel_count
    assert scene.statistics.water_retained_fraction == 1
    assert calls["raster"] == ["SCL", *BANDS]
    for band in scene.reflectance.values():
        np.testing.assert_allclose(band[scene.valid_water_mask], 0.05)
    payload = derived_product_to_dict(scene.provenance)
    serialized = canonical_json(payload)
    assert b"only-memory" not in serialized and b"?temporary" not in serialized
    assert len(scene.cache_id) == 64
    assert scene.provenance.product_id == "optical:" + scene.cache_id


def test_known_cache_hit_no_catalog_signing_xml_or_raster(pipeline, cdse_candidate, monkeypatch):
    context, calls = pipeline
    original = optical.preprocess_optical_scene(context, cdse_candidate)
    before = json.loads(json.dumps(calls))

    def forbidden(*args, **kwargs):
        pytest.fail("Cache hit must not perform catalog/signing/XML/raster work")

    for name in ("resolve_optical_source", "sign_asset", "read_bytes", "read_native_asset"):
        monkeypatch.setattr(optical, name, forbidden)
    monkeypatch.setattr("rasterio.open", forbidden)
    cached = optical.preprocess_optical_scene(context, known_cache_id=original.cache_id)
    assert calls == before
    assert cached.statistics == original.statistics
    assert cached.provenance == original.provenance
    assert cached.resolved_source == original.resolved_source
    for band in BANDS:
        np.testing.assert_array_equal(cached.reflectance[band], original.reflectance[band])
    for name in (
        "scl",
        "aoi_mask",
        "valid_data_mask",
        "water_mask",
        "valid_water_mask",
        "interpolation_support_mask",
    ):
        np.testing.assert_array_equal(getattr(cached, name), getattr(original, name))
    manifest = context.config.cache_dir / "as102" / original.cache_id / "manifest.json"
    assert b"only-memory" not in manifest.read_bytes()


def test_key_determinism_sensitive_to_decoding_grid_mask(pipeline, cdse_candidate):
    context, _ = pipeline
    scene = optical.preprocess_optical_scene(context, cdse_candidate)
    identity = scene.processing_parameters["identity"]
    assert cache_identity(identity) == cache_identity(dict(reversed(list(identity.items()))))
    for field in ("processing_version", "bands", "decoding", "target_grid", "mask_policy"):
        changed = {**identity, field: "changed"}
        assert cache_identity(changed) != scene.cache_id


@pytest.mark.parametrize("corruption", ["bytes", "grid", "statistics", "json", "source"])
def test_corrupted_cache_rejected(pipeline, cdse_candidate, corruption):
    context, _ = pipeline
    scene = optical.preprocess_optical_scene(context, cdse_candidate)
    directory = context.config.cache_dir / "as102" / scene.cache_id
    manifest = directory / "manifest.json"
    if corruption == "bytes":
        with (directory / "arrays.npz").open("ab") as stream:
            stream.write(b"corruption")
    elif corruption == "json":
        manifest.write_text("broken")
    else:
        payload = json.loads(manifest.read_text())
        if corruption == "grid":
            payload["grid"]["width"] += 1
        if corruption == "statistics":
            payload["statistics"]["valid_water_count"] += 1
        if corruption == "source":
            payload["resolved_source"]["source"]["product_id"] = "not-the-source"
        manifest.write_text(json.dumps(payload))
    with pytest.raises(CacheCorruptionError):
        load_cache(context.config.cache_dir, scene.cache_id)


def test_zero_water_scene_valid_without_relaxation(pipeline, cdse_candidate, monkeypatch):
    context, _ = pipeline
    original = optical.read_native_asset

    def nonwater(asset, *args):
        native = original(asset, *args)
        if asset.key == "SCL":
            native.data[:] = 5
        return native

    monkeypatch.setattr(optical, "read_native_asset", nonwater)
    scene = optical.preprocess_optical_scene(context, cdse_candidate)
    assert scene.statistics.valid_water_count == 0
    assert scene.statistics.candidate_water_count == 0
    assert scene.statistics.valid_data_count > 0
    assert scene.statistics.water_retained_fraction is None
    scene.validate()


def test_invalid_cloud_contributors_excluded_before_bilinear(pipeline, cdse_candidate, monkeypatch):
    context, _ = pipeline
    original = optical.read_native_asset

    def contaminated(asset, *args):
        native = original(asset, *args)
        if asset.key == "SCL":
            native.data[40:50, 40:50] = 9
        else:
            native.data[:] = 1500
            factor = round(20 / NATIVE_RESOLUTION[asset.key])
            # The 20 m SCL origin has a larger halo; shift native coordinates accordingly.
            start = (40 - 4) * factor + 4
            end = (50 - 4) * factor + 4
            native.data[start:end, start:end] = 60000
        return native

    monkeypatch.setattr(optical, "read_native_asset", contaminated)
    scene = optical.preprocess_optical_scene(context, cdse_candidate)
    for values in scene.reflectance.values():
        np.testing.assert_allclose(values[scene.valid_water_mask], 0.05)
    assert scene.statistics.valid_water_count < scene.statistics.candidate_water_count


def test_atomic_cache_failure_keeps_final_path_absent(
    pipeline, cdse_candidate, monkeypatch, tmp_path
):
    context, _ = pipeline
    scene = optical.preprocess_optical_scene(context, cdse_candidate)

    def failed(*a, **k):
        raise OSError("disk failure")

    monkeypatch.setattr(np, "savez_compressed", failed)
    root = tmp_path / "failure"
    with pytest.raises(OSError):
        write_cache(scene, root)
    assert not (root / "as102" / scene.cache_id).exists()
    assert list((root / "as102").iterdir()) == []


def test_cache_wrong_configured_grid_rejected(pipeline, cdse_candidate):
    context, _ = pipeline
    scene = optical.preprocess_optical_scene(context, cdse_candidate)
    changed = replace(
        context,
        config=replace(
            context.config, optical=replace(context.config.optical, target_resolution=10)
        ),
    )
    with pytest.raises(ValueError, match="AOI/grid"):
        optical.preprocess_optical_scene(changed, known_cache_id=scene.cache_id)


def test_one_band_nodata_rejects_all_band_water_support(pipeline, cdse_candidate, monkeypatch):
    context, _ = pipeline
    original = optical.read_native_asset

    def contaminated(asset, *args):
        native = original(asset, *args)
        if asset.key == "B11":
            native.data[40:50, 40:50] = 0
        return native

    monkeypatch.setattr(optical, "read_native_asset", contaminated)
    scene = optical.preprocess_optical_scene(context, cdse_candidate)
    assert scene.statistics.candidate_water_count == scene.statistics.aoi_pixel_count
    assert scene.statistics.valid_water_count < scene.statistics.candidate_water_count
    counts = scene.processing_parameters["water_support_counts_by_band"]
    assert counts["B11"] < counts["B02"]
    # This fixture uses aligned 20 m B11/target pixel grids with a four-pixel
    # native halo: native [40:50, 40:50] maps to target [36:46, 36:46].
    # Target [40, 40] is therefore inside the injected nodata block.
    assert not scene.valid_water_mask[40, 40]
    for values in scene.reflectance.values():
        assert np.isfinite(values[scene.valid_water_mask]).all()


@pytest.mark.parametrize(
    "path,value",
    [
        (("resolved_source", "discovery_source", "product_id"), "altered-product"),
        (("resolved_source", "identity", "relative_orbit"), 21),
        (("resolved_source", "processing_baseline"), "05.10"),
        (("resolved_source", "generation_time"), "2023-04-29T12:23:11Z"),
        (("resolved_source", "discovery_processing"), {"altered": True}),
        (("resolved_source", "provider_metadata"), {"altered": True}),
        (("resolved_source", "assets", 0, "href"),
         "https://sentinel2l2a01.blob.core.windows.net/altered.tif"),
        (("resolved_source", "decoding_metadata"), {"altered": True}),
        (("resolved_source", "native_grids"), {"altered": True}),
        (("provenance", "source_ids"), ["altered-source"]),
        (("provenance", "processing_version"), "altered-version"),
        (("provenance", "product_type"), "altered-type"),
        (("provenance", "product_id"), "altered-id"),
        (("provenance", "parameters", "altered"), True),
    ],
)
def test_metadata_tampering_rejected_with_valid_arrays_checksum(
    pipeline, cdse_candidate, path, value
):
    context, _ = pipeline
    scene = optical.preprocess_optical_scene(context, cdse_candidate)
    directory = context.config.cache_dir / "as102" / scene.cache_id
    manifest = directory / "manifest.json"
    payload = json.loads(manifest.read_text())
    checksum = sha256((directory / "arrays.npz").read_bytes()).hexdigest()
    target = payload
    for key in path[:-1]:
        target = target[key]
    target[path[-1]] = value
    manifest.write_text(json.dumps(payload))
    assert payload["files"]["arrays.npz"] == checksum
    assert sha256((directory / "arrays.npz").read_bytes()).hexdigest() == checksum
    with pytest.raises(CacheCorruptionError, match="failed checksum, identity or grid"):
        load_cache(context.config.cache_dir, scene.cache_id)


def test_cache_provenance_created_at_is_not_identity(pipeline, cdse_candidate):
    context, _ = pipeline
    scene = optical.preprocess_optical_scene(context, cdse_candidate)
    manifest = context.config.cache_dir / "as102" / scene.cache_id / "manifest.json"
    payload = json.loads(manifest.read_text())
    payload["provenance"]["created_at"] = "2026-10-08T12:00:00Z"
    manifest.write_text(json.dumps(payload))
    cached = load_cache(context.config.cache_dir, scene.cache_id)
    assert cached.cache_id == scene.cache_id
    assert cached.provenance.created_at.isoformat() == "2026-10-08T12:00:00+00:00"
