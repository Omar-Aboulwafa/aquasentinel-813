import builtins
import inspect
import socket
import urllib.request
from copy import deepcopy
from dataclasses import replace
from datetime import timedelta

import numpy as np
import pytest

from aquasentinel.geometry import extract_hab_anomaly_geometry
from aquasentinel.geometry.hab import input_content_fingerprint
from aquasentinel.preprocessing.cache import canonical_json

from .conftest import refresh_parent


def test_deterministic_repeat_and_created_at_excluded(parent):
    a, b = extract_hab_anomaly_geometry(parent), extract_hab_anomaly_geometry(parent)
    assert a.product_id == b.product_id
    assert a.processing_parameters == b.processing_parameters
    assert a.regions == b.regions
    assert np.array_equal(a.component_labels, b.component_labels)
    b = replace(
        b, provenance=replace(b.provenance, created_at=b.provenance.created_at + timedelta(days=1))
    )
    b.validate(parent)
    assert b.product_id == a.product_id


@pytest.mark.parametrize("field", ["deviation", "empirical_rank"])
def test_one_consumed_bit_changes_identity_without_crossing_threshold(parent, field):
    before = extract_hab_anomaly_geometry(parent)
    changed = deepcopy(parent)
    array = getattr(changed.results["ndci_like"], field)
    array[0, 0] = np.nextafter(array[0, 0], array.dtype.type(np.inf))
    changed = refresh_parent(changed)
    after = extract_hab_anomaly_geometry(changed)
    assert (
        before.processing_parameters["identity"]["input_content_fingerprint"]
        != after.processing_parameters["identity"]["input_content_fingerprint"]
    )
    assert before.product_id != after.product_id
    assert np.array_equal(before.candidate_mask, after.candidate_mask)


def test_threshold_crossing_changes_evidence(parent):
    before = extract_hab_anomaly_geometry(parent)
    changed = deepcopy(parent)
    changed.results["ndci_like"].empirical_rank[0, 0] = np.nextafter(
        np.float32(0.9), np.float32(-np.inf)
    )
    after = extract_hab_anomaly_geometry(refresh_parent(changed))
    assert before.candidate_mask[0, 0] and not after.candidate_mask[0, 0]
    assert not after.feature_evidence_masks["ndci_like"][0, 0]
    assert before.product_id != after.product_id


@pytest.mark.parametrize("layout", ["C", "F"])
def test_memory_layout_invariant(parent, layout):
    changed = deepcopy(parent)
    for r in changed.results.values():
        for array in vars(r).values():
            if isinstance(array, np.ndarray):
                assert array.dtype.isnative
        for name in ("rank_valid_mask", "deviation", "empirical_rank"):
            object.__setattr__(r, name, np.array(getattr(r, name), order=layout))
    changed.validate()
    assert (
        extract_hab_anomaly_geometry(parent).product_id
        == extract_hab_anomaly_geometry(changed).product_id
    )


def test_endian_canonicalization_at_fingerprint_boundary(parent):
    changed = deepcopy(parent)
    for r in changed.results.values():
        object.__setattr__(r, "deviation", r.deviation.astype(">f8"))
        object.__setattr__(r, "empirical_rank", r.empirical_rank.astype(">f4"))
    assert input_content_fingerprint(parent) == input_content_fingerprint(changed)
    # Whole-parent AS-104 validation retains its existing native-dtype contract.
    with pytest.raises(ValueError):
        extract_hab_anomaly_geometry(changed)


def test_unsupported_nan_payload_irrelevant(make_parent):
    water = np.ones((3, 4), bool)
    water[0, 0] = False
    parent = make_parent(water=water)
    before = extract_hab_anomaly_geometry(parent)
    changed = deepcopy(parent)
    for r in changed.results.values():
        r.deviation.view(np.uint64)[0, 0] = 0x7FF8000000000001
        r.empirical_rank.view(np.uint32)[0, 0] = 0x7FC00001
    changed.validate()
    after = extract_hab_anomaly_geometry(changed)
    assert before.product_id == after.product_id


@pytest.mark.parametrize("field", ["deviation", "empirical_rank"])
def test_nonfinite_consumed_value_rejected(parent, field):
    changed = deepcopy(parent)
    getattr(changed.results["ndci_like"], field)[0, 0] = np.nan
    with pytest.raises(ValueError):
        input_content_fingerprint(changed)
    with pytest.raises(ValueError):
        extract_hab_anomaly_geometry(changed)


def test_signed_zero_bits_preserved_in_consumed_identity(parent):
    plus = deepcopy(parent)
    plus.results["ndci_like"].deviation[0, 0] = 0.0
    minus = deepcopy(plus)
    minus.results["ndci_like"].deviation[0, 0] = -0.0
    a = extract_hab_anomaly_geometry(refresh_parent(plus))
    b = extract_hab_anomaly_geometry(refresh_parent(minus))
    assert a.product_id != b.product_id
    assert np.array_equal(a.candidate_mask, b.candidate_mask)


def test_support_mutation_changes_fingerprint_and_product(parent):
    before = extract_hab_anomaly_geometry(parent)
    changed = deepcopy(parent)
    r = changed.results["ndci_like"]
    r.rank_valid_mask[0, 0] = r.baseline_valid_mask[0, 0] = False
    r.baseline_observation_count[0, 0] = 0
    for field in ("baseline_centre", "baseline_scale", "deviation", "empirical_rank"):
        getattr(r, field)[0, 0] = np.nan
    after = extract_hab_anomaly_geometry(refresh_parent(changed))
    assert before.product_id != after.product_id
    assert (
        before.processing_parameters["identity"]["input_content_fingerprint"]
        != after.processing_parameters["identity"]["input_content_fingerprint"]
    )
    assert not after.candidate_mask[0, 0]


def test_unconsumed_history_count_and_statistics_do_not_change_identity(make_parent):
    supports = {n: np.ones((3, 4), bool) for n in make_parent().feature_order}
    for mask in supports.values():
        mask[0, 0] = False
    parent = make_parent(supports=supports)
    changed = deepcopy(parent)
    for r in changed.results.values():
        r.baseline_observation_count[0, 0] = 2
    changed = refresh_parent(changed)
    assert changed.processing_parameters["statistics"] != parent.processing_parameters["statistics"]
    a, b = extract_hab_anomaly_geometry(parent), extract_hab_anomaly_geometry(changed)
    assert a.product_id == b.product_id and a.processing_parameters == b.processing_parameters


def test_public_api_has_only_immediate_parent_parameter():
    assert tuple(inspect.signature(extract_hab_anomaly_geometry).parameters) == ("parent",)


def test_exact_recursive_lineage_and_registry_unchanged(parent, synthetic_template):
    _, original_registry = synthetic_template
    registry = deepcopy(original_registry)
    registry.add_derived_product(parent.provenance)
    before = deepcopy(registry)
    scene = extract_hab_anomaly_geometry(parent)
    assert registry == before
    assert scene.provenance.source_ids == (parent.product_id,)
    registry.add_derived_product(scene.provenance)
    lineage = registry.get_lineage(scene.product_id)
    assert lineage[-2:] == (parent.product_id, scene.product_id)
    for spectral_id in parent.provenance.source_ids:
        spectral = registry.get_derived_product(spectral_id)
        optical = registry.get_derived_product(spectral.source_ids[0])
        pc = registry.get_source(optical.source_ids[0])
        assert pc.source_id.startswith("pc:")
        assert (
            lineage.index(pc.source_id)
            < lineage.index(optical.product_id)
            < lineage.index(spectral_id)
            < lineage.index(parent.product_id)
        )


def test_parent_buffers_metadata_unchanged_and_outputs_defensive(parent):
    arrays = [
        v for r in parent.results.values() for v in vars(r).values() if isinstance(v, np.ndarray)
    ]
    arrays.append(parent.valid_water_mask)
    snapshots = [(a.dtype, a.shape, a.tobytes()) for a in arrays]
    metadata = canonical_json(parent.processing_parameters)
    scene = extract_hab_anomaly_geometry(parent)
    outputs = [v for v in vars(scene).values() if isinstance(v, np.ndarray)]
    for group in (
        scene.feature_support_masks,
        scene.feature_evidence_masks,
        scene.family_available_masks,
        scene.family_evidence_masks,
    ):
        outputs.extend(group.values())
    assert all(not np.shares_memory(a, b) for a in arrays for b in outputs)
    scene.feature_support_masks["ndci_like"][:] = False
    assert snapshots == [(a.dtype, a.shape, a.tobytes()) for a in arrays]
    assert canonical_json(parent.processing_parameters) == metadata


def test_public_api_no_network_writes_or_upstream_calculation(parent, monkeypatch):
    import aquasentinel.temporal.baseline as temporal
    from aquasentinel.features import spectral
    from aquasentinel.preprocessing import cache, optical

    def forbidden(*args, **kwargs):
        pytest.fail("AS-105 must not perform network, disk-cache or upstream processing")

    original_open = builtins.open

    def readonly_open(file, mode="r", *args, **kwargs):
        if any(flag in mode for flag in "wa+"):
            forbidden()
        return original_open(file, mode, *args, **kwargs)

    monkeypatch.setattr(socket, "create_connection", forbidden)
    monkeypatch.setattr(urllib.request, "urlopen", forbidden)
    monkeypatch.setattr(builtins, "open", readonly_open)
    monkeypatch.setattr(np, "savez_compressed", forbidden)
    monkeypatch.setattr(spectral, "extract_spectral_features", forbidden)
    monkeypatch.setattr(temporal, "compute_temporal_anomaly", forbidden)
    monkeypatch.setattr(optical, "preprocess_optical_scene", forbidden)
    monkeypatch.setattr(cache, "load_cache", forbidden)
    scene = extract_hab_anomaly_geometry(parent)
    scene.validate(parent)
