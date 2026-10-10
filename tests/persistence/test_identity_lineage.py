import builtins
import inspect
import io
import socket
import urllib.request
from copy import deepcopy
from dataclasses import replace
from datetime import UTC, datetime, timedelta, timezone

import numpy as np
import pytest

from aquasentinel.geometry import extract_hab_anomaly_geometry
from aquasentinel.geometry.models import HABAnomalyGeometryScene
from aquasentinel.persistence import compute_hab_persistence
from aquasentinel.persistence.recurrence import ARRAY_DTYPES, input_content_fingerprint
from aquasentinel.preprocessing.cache import canonical_json


def test_deterministic_repeat_and_caller_permutation(sequence, compute):
    a = compute(sequence)
    b = compute_hab_persistence(
        list(reversed(sequence[0])), temporal_parents=sequence[1],
        target_geometry_product_id=sequence[0][-1].product_id,
    )
    assert a.product_id == b.product_id
    assert a.processing_parameters == b.processing_parameters
    for field in ARRAY_DTYPES:
        assert np.array_equal(getattr(a, field), getattr(b, field))
    assert a.provenance.source_ids == tuple(s.product_id for s in sequence[0])


def test_created_at_does_not_change_identity(sequence, compute):
    a = compute(sequence)
    later = replace(a, provenance=replace(a.provenance, created_at=datetime(2030, 1, 1, tzinfo=UTC)))
    later.validate(sequence[0], temporal_parents=sequence[1])
    assert later.product_id == a.product_id
    assert later.processing_parameters == a.processing_parameters


def test_input_timezone_representation_invariant(sequence, compute):
    scenes, parents = sequence
    changed = [replace(s, target_acquired_at=s.target_acquired_at.astimezone(
        timezone(timedelta(hours=4)))) for s in scenes]
    a, b = compute(sequence), compute((changed, parents))
    assert a.product_id == b.product_id
    assert all(t.tzinfo == UTC for t in b.acquired_at)


@pytest.mark.parametrize("field,target,index", [
    ("candidate_analysis_support_mask", True, (0, 0)),
    ("candidate_mask", True, (0, 0)),
    ("candidate_analysis_support_mask", False, (0, 0)),
    ("candidate_mask", False, (0, 0)),
    ("component_labels", True, (0, 0)),
])
def test_consumed_content_changes_fingerprint_at_boundary(sequence, field, target, index):
    before = input_content_fingerprint(sequence[0])
    changed = deepcopy(sequence[0])
    array = getattr(changed[-1] if target else changed[0], field)
    array[index] = not array[index] if array.dtype == bool else array[index] + 1
    assert input_content_fingerprint(changed) != before
    # Deliberately malformed snapshots are only used at hashing boundary, never accepted by API.


def test_target_region_identity_mapping_consumed(sequence):
    before = input_content_fingerprint(sequence[0])
    changed = deepcopy(sequence[0])
    changed[-1] = replace(changed[-1], regions=(replace(changed[-1].regions[0], region_id="other"),))
    assert input_content_fingerprint(changed) != before


@pytest.mark.parametrize("kind", ["P_outside_target_P", "C_outside_target_C", "C_without_prior_P",
                                  "prior_labels", "votes", "region_description"])
def test_unconsumed_prior_inputs_do_not_change_consumed_fingerprint(make_sequence, kind):
    target_p = np.array([[True, True, False], [True, True, True]])
    target_c = np.array([[True, False, False], [True, True, True]])
    prior_p = np.ones((2, 3), bool)
    prior_p[0, 0] = False
    prior_c = prior_p.copy()
    scenes, _ = make_sequence([(prior_p, prior_c), (target_p, target_c)])
    changed = deepcopy(scenes)
    prior = changed[0]
    if kind == "P_outside_target_P":
        prior.candidate_analysis_support_mask[0, 2] = False
    elif kind == "C_outside_target_C":
        prior.candidate_mask[0, 1] = False
    elif kind == "C_without_prior_P":
        prior.candidate_mask[0, 0] = True
    elif kind == "prior_labels":
        prior.component_labels[:] = 999
    elif kind == "votes":
        prior.family_vote_count[:] = 0
    else:
        prior.regions[0].family_evidence_pixel_counts.clear()
    assert input_content_fingerprint(changed) == input_content_fingerprint(scenes)


@pytest.mark.parametrize("layout", ["C", "F"])
def test_memory_layout_does_not_change_product(sequence, compute, layout):
    changed = deepcopy(sequence)
    for s in changed[0]:
        for field, value in vars(s).items():
            if isinstance(value, np.ndarray):
                object.__setattr__(s, field, np.array(value, order=layout))
    assert compute(changed).product_id == compute(sequence).product_id


def test_endian_boundary_canonicalization_preserves_whole_parent_dtype_rule(sequence):
    changed = deepcopy(sequence[0])
    for s in changed:
        object.__setattr__(s, "component_labels", s.component_labels.astype(">i4"))
    assert input_content_fingerprint(changed) == input_content_fingerprint(sequence[0])
    with pytest.raises(ValueError):
        compute_hab_persistence(changed, temporal_parents=sequence[1],
                                target_geometry_product_id=changed[-1].product_id)


def test_changed_legitimate_prior_id_changes_product_with_same_consumed_science(
    sequence, compute, upstream
):
    scenes, parents = deepcopy(sequence)
    prior = scenes[0]
    temporal = deepcopy(parents.pop(prior.parent_temporal_product_id))
    # Deviation 1 -> 2 retains the same support/votes/candidate pixels, but changes valid AS-105 ID.
    for r in temporal.results.values():
        r.deviation[r.baseline_valid_mask] *= 2
    from .conftest import reidentify

    from_module = upstream[0]
    temporal = reidentify(from_module.refresh_parent(temporal))
    scenes[0] = extract_hab_anomaly_geometry(temporal)
    parents[temporal.product_id] = temporal
    assert scenes[0].product_id != prior.product_id
    assert input_content_fingerprint(scenes) == input_content_fingerprint(sequence[0])
    assert compute((scenes, parents)).product_id != compute(sequence).product_id


def test_all_parent_validators_invoked(sequence, compute, monkeypatch):
    called = []
    original = HABAnomalyGeometryScene.validate

    def recording(scene, parent):
        called.append((scene.product_id, parent.product_id))
        original(scene, parent)

    monkeypatch.setattr(HABAnomalyGeometryScene, "validate", recording)
    result = compute(sequence)
    assert called == [(s.product_id, s.parent_temporal_product_id) for s in sequence[0]]
    called.clear()
    result.validate(sequence[0], temporal_parents=sequence[1])
    assert len(called) == len(sequence[0])


def test_exact_recursive_lineage_registry_compatibility(upstream):
    _, factory, original = upstream
    parent = factory()
    geometry = extract_hab_anomaly_geometry(parent)
    registry = deepcopy(original)
    registry.add_derived_product(parent.provenance)
    registry.add_derived_product(geometry.provenance)
    before = deepcopy(registry)
    result = compute_hab_persistence([geometry], temporal_parents={parent.product_id: parent},
                                     target_geometry_product_id=geometry.product_id)
    assert registry == before
    assert result.provenance.source_ids == (geometry.product_id,)
    registry.add_derived_product(result.provenance)
    lineage = registry.get_lineage(result.product_id)
    assert lineage[-3:] == (parent.product_id, geometry.product_id, result.product_id)
    for spectral_id in parent.provenance.source_ids:
        spectral = registry.get_derived_product(spectral_id)
        optical = registry.get_derived_product(spectral.source_ids[0])
        pc = registry.get_source(optical.source_ids[0])
        assert pc.source_id.startswith("pc:")
        assert lineage.index(pc.source_id) < lineage.index(optical.product_id)
        assert lineage.index(optical.product_id) < lineage.index(spectral_id)
        assert lineage.index(spectral_id) < lineage.index(parent.product_id)


def test_parent_immutability_and_output_nonaliasing(sequence, compute):
    scenes, witnesses = sequence
    parent_arrays = []
    for s in scenes:
        for value in vars(s).values():
            if isinstance(value, np.ndarray):
                parent_arrays.append(value)
            elif isinstance(value, dict):
                parent_arrays.extend(v for v in value.values() if isinstance(v, np.ndarray))
    for parent in witnesses.values():
        parent_arrays.append(parent.valid_water_mask)
        for r in parent.results.values():
            parent_arrays.extend(v for v in vars(r).values() if isinstance(v, np.ndarray))
    snapshots = [(a.dtype.str, a.shape, a.tobytes()) for a in parent_arrays]
    metadata = [canonical_json(s.processing_parameters) for s in [*scenes, *witnesses.values()]]
    provenance = [deepcopy(s.provenance) for s in [*scenes, *witnesses.values()]]
    result = compute(sequence)
    result.validate(scenes, temporal_parents=witnesses)
    assert snapshots == [(a.dtype.str, a.shape, a.tobytes()) for a in parent_arrays]
    assert metadata == [canonical_json(s.processing_parameters) for s in [*scenes, *witnesses.values()]]
    assert provenance == [s.provenance for s in [*scenes, *witnesses.values()]]
    outputs = [getattr(result, f) for f in ARRAY_DTYPES]
    assert all(not np.shares_memory(a, b) for a in parent_arrays for b in outputs)
    result.target_candidate_mask[:] = False
    result.processing_parameters["identity"]["common_temporal_comparison_contract"].clear()
    assert snapshots == [(a.dtype.str, a.shape, a.tobytes()) for a in parent_arrays]
    assert metadata == [canonical_json(s.processing_parameters) for s in [*scenes, *witnesses.values()]]


def test_api_no_io_network_cache_registry_mutation_or_upstream_extraction(sequence, compute, monkeypatch):
    from pathlib import Path

    import aquasentinel.geometry.hab as geometry
    from aquasentinel.features import spectral
    from aquasentinel.preprocessing import cache, optical
    from aquasentinel.temporal import baseline

    def forbidden(*args, **kwargs):
        pytest.fail("Persistence API attempted IO/network/cache or upstream extraction")

    # Fixtures/imports finish before guards. AS-105 _build regeneration remains allowed.
    for obj, name in [(builtins, "open"), (io, "open"), (Path, "open"),
                      (socket, "socket"), (socket, "create_connection"),
                      (urllib.request, "urlopen"), (np, "load"), (np, "save"),
                      (np, "savez_compressed"), (cache, "load_cache"), (cache, "write_cache"),
                      (geometry, "extract_hab_anomaly_geometry"),
                      (spectral, "extract_spectral_features"),
                      (optical, "preprocess_optical_scene"), (baseline, "compute_temporal_anomaly")]:
        monkeypatch.setattr(obj, name, forbidden)
    result = compute(sequence)
    result.validate(sequence[0], temporal_parents=sequence[1])


def test_public_signature_is_frozen():
    assert tuple(inspect.signature(compute_hab_persistence).parameters) == (
        "geometry_scenes", "temporal_parents", "target_geometry_product_id")
