from copy import deepcopy
from dataclasses import replace
from datetime import UTC, datetime, timedelta

import numpy as np
import pytest

from aquasentinel.features import extract_spectral_features
from aquasentinel.features.spectral import (
    CONSUMED_BANDS,
    feature_product_id,
    input_content_fingerprint,
)
from aquasentinel.provenance import ProvenanceRegistry


def test_deterministic_repeat_timestamp_independent(parent):
    first, second = extract_spectral_features(parent), extract_spectral_features(parent)
    assert first.product_id == second.product_id
    assert first.statistics == second.statistics and first.diagnostics == second.diagnostics
    for name in first.feature_order:
        np.testing.assert_array_equal(first.features[name], second.features[name])
        np.testing.assert_array_equal(
            first.feature_valid_masks[name], second.feature_valid_masks[name]
        )
    changed = replace(first.provenance, created_at=datetime.now(UTC) + timedelta(days=1))
    replace(first, provenance=changed).validate()
    assert changed.product_id == first.product_id
    changed_parent = replace(
        parent,
        provenance=replace(
            parent.provenance, created_at=parent.provenance.created_at + timedelta(days=1)
        ),
    )
    assert extract_spectral_features(changed_parent).product_id == first.product_id


def test_dict_order_and_memory_layout_do_not_change_identity(parent):
    first = extract_spectral_features(parent)
    identity = first.processing_parameters["identity"]
    assert feature_product_id(dict(reversed(list(identity.items())))) == first.product_id
    reordered = replace(
        parent, processing_parameters=dict(reversed(list(parent.processing_parameters.items())))
    )
    assert extract_spectral_features(reordered).product_id == first.product_id
    bands = {k: np.asfortranarray(v) for k, v in parent.reflectance.items()}
    fingerprint = input_content_fingerprint(bands, np.asfortranarray(parent.valid_water_mask))
    assert fingerprint == identity["input_content_fingerprint"]
    # Public fingerprint accepts endian representation differences canonically.
    assert (
        input_content_fingerprint(
            {k: v.astype(">f4") for k, v in bands.items()}, parent.valid_water_mask
        )
        == fingerprint
    )


@pytest.mark.parametrize("field", ["formula", "epsilon", "wavelength", "parent", "grid", "version"])
def test_identity_records_semantic_changes(parent, field):
    result = extract_spectral_features(parent)
    identity = deepcopy(result.processing_parameters["identity"])
    if field == "formula":
        identity["formulas"]["ndci_like"]["formula"] = "changed"
    elif field == "epsilon":
        identity["numerical_policy"]["absolute_denominator_epsilon"] *= 2
    elif field == "wavelength":
        identity["formulas"]["mci_like"]["wavelengths"]["B05"] = 706.0
    elif field == "parent":
        identity["parent_product_id"] = "optical:changed"
    elif field == "grid":
        identity["grid"]["resolution"] = 10.0
    else:
        identity["processing_version"] = "as103-v2"
    assert feature_product_id(identity) != result.product_id


@pytest.mark.parametrize("band", CONSUMED_BANDS)
def test_consumed_valid_pixel_changes_product_id(parent, band):
    old = extract_spectral_features(parent).product_id
    parent.reflectance[band][0, 0] += 0.001
    assert extract_spectral_features(parent).product_id != old


@pytest.mark.parametrize("band", ["B07", "B08", "B8A", "B11"])
def test_unconsumed_band_changes_do_not_change_product_id(parent, band):
    old = extract_spectral_features(parent).product_id
    parent.reflectance[band][0, 0] += 0.001
    assert extract_spectral_features(parent).product_id == old


def test_mask_change_and_excluded_values_identity(make_optical):
    mask = np.ones((2, 6), bool)
    mask[0, 0] = False
    parent = make_optical(mask=mask)
    old = extract_spectral_features(parent).product_id
    for name in CONSUMED_BANDS:
        parent.reflectance[name][0, 0] = np.nan
    assert extract_spectral_features(parent).product_id == old
    parent.valid_water_mask[0, 1] = False
    assert extract_spectral_features(parent).product_id != old


def test_parent_product_change_changes_identity(parent):
    first = extract_spectral_features(parent)
    cache_id = "b" * 64
    changed = replace(
        parent,
        cache_id=cache_id,
        provenance=replace(parent.provenance, product_id="optical:" + cache_id),
    )
    assert extract_spectral_features(changed).product_id != first.product_id


def test_exact_immediate_parent_registry_lineage(parent):
    feature = extract_spectral_features(parent)
    registry = ProvenanceRegistry()
    registry.add_source(parent.resolved_source.source)
    with pytest.raises(ValueError, match="unknown"):
        registry.add_derived_product(feature.provenance)
    registry.add_derived_product(parent.provenance)
    registry.add_derived_product(feature.provenance)
    assert feature.provenance.source_ids == (parent.provenance.product_id,)
    assert registry.get_lineage(feature.product_id) == (
        parent.source_id,
        parent.provenance.product_id,
        feature.product_id,
    )
    assert parent.resolved_source.discovery_source.source_id not in registry.get_lineage(
        feature.product_id
    )


def test_extraction_has_no_external_or_write_calls(parent, monkeypatch):
    import builtins
    import socket
    import urllib.request
    from pathlib import Path

    import rasterio

    def forbidden(*a, **k):
        pytest.fail("Feature extraction attempted external access or disk write")

    for module, name in [
        ("aquasentinel.catalog.stac", "search_catalog"),
        ("aquasentinel.ingestion.planetary_computer", "sign_asset"),
        ("aquasentinel.ingestion.planetary_computer", "read_bytes"),
        ("aquasentinel.preprocessing.alignment", "read_native_asset"),
        ("aquasentinel.preprocessing.cache", "write_cache"),
        ("aquasentinel.preprocessing.optical", "write_cache"),
    ]:
        monkeypatch.setattr(module + "." + name, forbidden)
    for owner, name in [
        (builtins, "open"),
        (Path, "open"),
        (Path, "write_bytes"),
        (Path, "write_text"),
        (socket, "create_connection"),
        (urllib.request, "urlopen"),
        (rasterio, "open"),
        (np, "save"),
        (np, "savez"),
        (np, "savez_compressed"),
    ]:
        monkeypatch.setattr(owner, name, forbidden)
    assert extract_spectral_features(parent).statistics["mci_like"].valid_count == 12
