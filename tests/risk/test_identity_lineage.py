import builtins
import inspect
import io
import socket
import urllib.request
from copy import deepcopy
from dataclasses import replace
from datetime import timedelta
from pathlib import Path

import numpy as np
import pytest

from aquasentinel.geometry import extract_hab_anomaly_geometry
from aquasentinel.geometry.hab import FAMILY_ORDER
from aquasentinel.geometry.models import HABAnomalyGeometryScene
from aquasentinel.persistence import compute_hab_persistence
from aquasentinel.persistence.models import HABPersistenceScene
from aquasentinel.preprocessing.cache import canonical_json
from aquasentinel.risk import HABRiskPolicy, compute_hab_risk
from aquasentinel.risk.policy import COMPONENT_ORDER, DEFAULT_WEIGHTS
from aquasentinel.risk.scoring import (
    _build,
    _encoded,
    input_content_fingerprint,
    output_content_fingerprint,
    risk_product_id,
)

from .conftest import validate


def test_creation_time_excluded_from_identity_and_output(inputs, compute):
    first = compute(inputs)
    later = _build(inputs[0], inputs[1], HABRiskPolicy(), first.provenance.created_at + timedelta(days=10))
    assert first.provenance.created_at != later.provenance.created_at
    assert first.product_id == later.product_id
    assert first.input_content_fingerprint == later.input_content_fingerprint
    assert first.output_content_fingerprint == later.output_content_fingerprint
    assert first.processing_parameters == later.processing_parameters
    validate(later, inputs)


def test_deterministic_repeat_reordered_maps_sequence_and_generator(inputs, compute):
    first = compute(inputs)
    g, p, seq, witnesses = inputs
    changed = (g, p, (s for s in reversed(seq)), dict(reversed(tuple(witnesses.items()))))
    repeated = compute(changed, HABRiskPolicy(weights=dict(reversed(DEFAULT_WEIGHTS))))
    assert repeated.product_id == first.product_id
    assert repeated.input_content_fingerprint == first.input_content_fingerprint
    assert repeated.output_content_fingerprint == first.output_content_fingerprint
    assert repeated.regions == first.regions
    assert repeated.site_summary == first.site_summary
    validate(repeated, inputs)


@pytest.mark.parametrize("field", ["candidate_analysis_support_mask", "candidate_mask", "component_labels",
    "family_available_masks", "family_evidence_masks", "regions", "prior_valid_observation_count",
    "persistence_evaluable_mask", "current_streak_count", "recurrent_candidate_mask",
    "previous_valid_observation_gap_us", "current_streak_span_us", "persistence_regions"])
def test_consumed_evidence_changes_input_fingerprint(inputs, field):
    g, p, _, _ = deepcopy(inputs)
    expected = input_content_fingerprint(g, p)
    if field in ("family_available_masks", "family_evidence_masks"):
        getattr(g, field)[FAMILY_ORDER[0]][0, 0] ^= True
    elif field == "regions":
        object.__setattr__(g, "regions", (replace(g.regions[0], area_m2=1.),))
    elif field == "persistence_regions":
        object.__setattr__(p, "regions", (replace(p.regions[0], maximum_streak_count=9),))
    else:
        obj = g if field in ("candidate_analysis_support_mask", "candidate_mask", "component_labels") else p
        a = getattr(obj, field)
        a[0, 0] = not a[0, 0] if a.dtype == bool else a[0, 0]+1
    assert input_content_fingerprint(g, p) != expected


def test_unconsumed_feature_rank_deviation_and_outside_candidate_family_values(inputs):
    g, p, _, _ = deepcopy(inputs)
    before = input_content_fingerprint(g, p)
    g.regions[0].feature_summaries.clear()
    g.feature_support_masks.clear()
    g.feature_evidence_masks.clear()
    assert input_content_fingerprint(g, p) == before


def test_family_and_history_values_outside_candidates_are_not_consumed(make_inputs):
    candidate = np.array([[1, 0, 0], [0, 0, 0]], bool)
    g, p, _, _ = make_inputs(states=((True, candidate), (True, candidate)))
    before = input_content_fingerprint(g, p)
    g.family_available_masks[FAMILY_ORDER[0]][0, 2] ^= True
    g.family_evidence_masks[FAMILY_ORDER[0]][0, 2] ^= True
    p.current_streak_count[0, 2] += 1
    assert input_content_fingerprint(g, p) == before


def test_valid_family_change_same_score_different_identity(make_inputs, compute):
    original = make_inputs()
    changed = make_inputs([{}, {"evidence": {
        FAMILY_ORDER[0]: False, FAMILY_ORDER[1]: True,
    }}])
    first, second = compute(original), compute(changed)
    validate(first, original)
    validate(second, changed)
    assert first.regions[0].risk_score == second.regions[0].risk_score
    assert first.input_content_fingerprint != second.input_content_fingerprint
    assert first.product_id != second.product_id


def test_consumed_bit_changes_fingerprint_even_when_pooled_score_unchanged(inputs, compute):
    result = compute(inputs)
    g, p, _, _ = deepcopy(inputs)
    # Exchange which red-edge family contributes one pixel, preserving every pooled count.
    g.family_evidence_masks[FAMILY_ORDER[0]][0, 0] = False
    g.family_evidence_masks[FAMILY_ORDER[1]][0, 0] = True
    assert sum(int(v.sum()) for v in g.family_evidence_masks.values()) == 12
    assert input_content_fingerprint(g, p) != result.input_content_fingerprint
    # Whole-parent validation still rejects this invalid rehashed shortcut; it is
    # only a fingerprint-boundary check, not an upstream acceptance claim.


def test_output_identity_formats_and_exact_serialization(inputs, compute):
    r = compute(inputs)
    assert r.product_id.startswith("hab_risk:")
    assert r.provenance.product_type == "hab_risk" and r.provenance.processing_version == "as107-v1"
    assert r.processing_parameters["identity"]["input_fingerprint_format"] == "as107-input-v1"
    assert r.processing_parameters["output_fingerprint_format"] == "as107-output-v1"
    assert risk_product_id(r.processing_parameters["identity"]) == r.product_id
    assert output_content_fingerprint(r) == r.output_content_fingerprint
    assert _encoded({"a": 1., "b": None}) == _encoded({"b": None, "a": 1.})
    assert b"0x1.0000000000000p+0" in _encoded({"a": 1.})
    assert b"null" in _encoded({"b": None})
    assert _encoded(0.) != _encoded(-0.)


@pytest.mark.parametrize("change", ["weights", "bands", "parent_id"])
def test_valid_identity_policy_or_parent_changes_digest(inputs, compute, change):
    r = compute(inputs)
    identity = deepcopy(r.processing_parameters["identity"])
    if change == "weights":
        identity["policy"] = HABRiskPolicy(weights=dict(zip(COMPONENT_ORDER, (.3, .25, .15, .15, .15)))).to_dict()
    elif change == "bands":
        identity["policy"] = HABRiskPolicy(low_max=23).to_dict()
    else:
        identity["source_product_ids"] = ("hab_geometry:other", inputs[1].product_id)
    assert risk_product_id(identity) != r.product_id


def test_full_parent_validation_called(inputs, compute, monkeypatch):
    calls = []
    original_g, original_p = HABAnomalyGeometryScene.validate, HABPersistenceScene.validate

    def geometry(g, parent):
        calls.append(("g", g.product_id))
        return original_g(g, parent)

    def persistence(p, scenes, *, temporal_parents):
        calls.append(("p", p.product_id))
        return original_p(p, scenes, temporal_parents=temporal_parents)

    monkeypatch.setattr(HABAnomalyGeometryScene, "validate", geometry)
    monkeypatch.setattr(HABPersistenceScene, "validate", persistence)
    result = compute(inputs)
    assert ("p", inputs[1].product_id) in calls
    assert all(("g", g.product_id) in calls for g in inputs[2])
    assert calls.count(("g", inputs[0].product_id)) >= 2
    calls.clear()
    validate(result, inputs)
    assert ("p", inputs[1].product_id) in calls
    assert all(("g", g.product_id) in calls for g in inputs[2])


@pytest.mark.parametrize("kind", ["missing", "wrong_type", "wrong_key", "explicit_other_target", "future_sequence"])
def test_incompatible_or_missing_witnesses_targets_rejected(inputs, compute, kind):
    g, p, seq, witnesses = deepcopy(inputs)
    if kind == "missing":
        witnesses.clear()
    elif kind == "wrong_type":
        witnesses[g.parent_temporal_product_id] = object()
    elif kind == "wrong_key":
        witnesses[g.parent_temporal_product_id] = next(v for k, v in witnesses.items()
                                                      if k != g.parent_temporal_product_id)
    elif kind == "explicit_other_target":
        g = seq[0]
    else:
        p = replace(p, target_geometry_product_id=seq[0].product_id)
    with pytest.raises((ValueError, TypeError)):
        compute((g, p, seq, witnesses))


PARENT_ATTACKS = (
    "family_available", "family_evidence", "candidate", "labels", "region_count",
    "A", "B", "C", "history_fraction", "recurrence_fraction", "streak", "span", "gap",
    "target_id", "target_time", "grid",
)


@pytest.mark.parametrize("attack", PARENT_ATTACKS)
@pytest.mark.parametrize("rehash", [False, True], ids=["stale", "attacker-rehashed-parent"])
def test_parent_tampering_rejected(inputs, compute, attack, rehash):
    from aquasentinel.geometry.hab import output_content_fingerprint as g_hash
    from aquasentinel.persistence.recurrence import output_content_fingerprint as p_hash

    g, p, seq, witnesses = deepcopy(inputs)
    if attack.startswith("family_"):
        getattr(g, f"{attack}_masks")[FAMILY_ORDER[0]][0, 0] ^= True
    elif attack == "candidate":
        g.candidate_mask[0, 0] = False
    elif attack == "labels":
        g.component_labels[0, 0] = 99
    elif attack == "region_count":
        object.__setattr__(g, "regions", (replace(g.regions[0], pixel_count=7),))
    elif attack in ("A", "B", "C", "history_fraction", "recurrence_fraction"):
        field = {"A": "target_pixel_count", "B": "persistence_evaluable_target_candidate_count",
                 "C": "recurrent_candidate_count", "history_fraction": "candidate_history_coverage",
                 "recurrence_fraction": "recurrence_fraction"}[attack]
        value = 7 if attack in ("A", "B", "C") else .2
        object.__setattr__(p, "regions", (replace(p.regions[0], **{field: value}),))
    elif attack in ("streak", "span", "gap"):
        field = {"streak": "current_streak_count", "span": "current_streak_span_us",
                 "gap": "previous_valid_observation_gap_us"}[attack]
        getattr(p, field)[0, 0] += 1
    elif attack == "target_id":
        object.__setattr__(p, "target_geometry_product_id", "hab_geometry:other")
    elif attack == "target_time":
        object.__setattr__(p, "target_acquired_at", p.target_acquired_at + timedelta(seconds=1))
    else:
        object.__setattr__(p, "grid", replace(p.grid, grid_id="bad"))
    if rehash:
        g.processing_parameters["output_content_fingerprint"] = g_hash(vars(g))
        g.provenance.parameters.clear()
        g.provenance.parameters.update(deepcopy(g.processing_parameters))
        p.processing_parameters["output_content_fingerprint"] = p_hash(vars(p))
        p.provenance.parameters.clear()
        p.provenance.parameters.update(deepcopy(p.processing_parameters))
    with pytest.raises((ValueError, TypeError)):
        compute((g, p, seq, witnesses))


def test_exact_immediate_and_recursive_registry_lineage(synthetic_upstream):
    _, (_, factory, original) = synthetic_upstream
    t = factory()
    g = extract_hab_anomaly_geometry(t)
    witnesses = {t.product_id: t}
    p = compute_hab_persistence([g], temporal_parents=witnesses, target_geometry_product_id=g.product_id)
    registry = deepcopy(original)
    for record in (t.provenance, g.provenance, p.provenance):
        registry.add_derived_product(record)
    before = deepcopy(registry)
    r = compute_hab_risk(g, p, geometry_scenes=[g], temporal_parents=witnesses, policy=HABRiskPolicy())
    validate(r, (g, p, [g], witnesses))
    assert registry == before
    assert r.provenance.source_ids == (g.product_id, p.product_id)
    registry.add_derived_product(r.provenance)
    lineage = registry.get_lineage(r.product_id)
    assert lineage[-4:] == (t.product_id, g.product_id, p.product_id, r.product_id)
    for spectral_id in t.provenance.source_ids:
        spectral = registry.get_derived_product(spectral_id)
        optical = registry.get_derived_product(spectral.source_ids[0])
        pc = registry.get_source(optical.source_ids[0])
        assert lineage.index(pc.source_id) < lineage.index(optical.product_id) < lineage.index(spectral_id)
        assert lineage.index(spectral_id) < lineage.index(t.product_id)


def test_parent_immutability_and_nonaliasing(inputs, compute):
    _g, p, seq, witnesses = inputs
    nodes = [*seq, p, *witnesses.values()]
    arrays = []
    for node in nodes:
        for value in vars(node).values():
            if isinstance(value, np.ndarray):
                arrays.append(value)
            elif isinstance(value, dict):
                arrays.extend(v for v in value.values() if isinstance(v, np.ndarray))
    for t in witnesses.values():
        for feature in t.results.values():
            arrays.extend(v for v in vars(feature).values() if isinstance(v, np.ndarray))
    snapshots = [(a.shape, a.dtype.str, a.tobytes()) for a in arrays]
    metadata = [canonical_json(n.processing_parameters) for n in nodes]
    provenance = [deepcopy(n.provenance) for n in nodes]
    result = compute(inputs)
    validate(result, inputs)
    assert snapshots == [(a.shape, a.dtype.str, a.tobytes()) for a in arrays]
    assert metadata == [canonical_json(n.processing_parameters) for n in nodes]
    assert provenance == [n.provenance for n in nodes]
    assert result.regions[0].persistence_evidence is not p.regions[0]
    result.processing_parameters["identity"]["policy"].clear()
    result.provenance.parameters.clear()
    assert metadata == [canonical_json(n.processing_parameters) for n in nodes]


def test_no_io_network_cache_registry_or_public_upstream_extraction(inputs, compute, monkeypatch):
    import aquasentinel.geometry.hab as geometry
    import aquasentinel.persistence.recurrence as persistence
    from aquasentinel.features import spectral
    from aquasentinel.preprocessing import cache, optical
    from aquasentinel.provenance.registry import ProvenanceRegistry
    from aquasentinel.temporal import baseline

    def forbidden(*args, **kwargs):
        pytest.fail("AS-107 attempted an external side effect or upstream extraction")

    # Fixtures and imports complete first; internal parent regeneration remains required.
    for obj, name in [(builtins, "open"), (io, "open"), (Path, "open"),
        (socket, "socket"), (socket, "create_connection"), (urllib.request, "urlopen"),
        (np, "load"), (np, "save"), (np, "savez_compressed"),
        (cache, "load_cache"), (cache, "write_cache"),
        (geometry, "extract_hab_anomaly_geometry"), (persistence, "compute_hab_persistence"),
        (spectral, "extract_spectral_features"), (optical, "preprocess_optical_scene"),
        (baseline, "compute_temporal_anomaly"), (ProvenanceRegistry, "add_derived_product"),
        (ProvenanceRegistry, "add_source")]:
        monkeypatch.setattr(obj, name, forbidden)
    result = compute(inputs)
    validate(result, inputs)


def test_public_signature_no_hidden_provider_hooks(inputs):
    assert tuple(inspect.signature(compute_hab_risk).parameters) == (
        "geometry_scene", "persistence_scene", "geometry_scenes", "temporal_parents", "policy")
    g, p, seq, witnesses = inputs
    for name in COMPONENT_ORDER[3:]:
        with pytest.raises(TypeError):
            compute_hab_risk(g, p, geometry_scenes=seq, temporal_parents=witnesses,
                             policy=HABRiskPolicy(), **{name: 80.})
