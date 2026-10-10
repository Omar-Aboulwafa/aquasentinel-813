from copy import deepcopy
from dataclasses import FrozenInstanceError, replace
from datetime import timedelta

import pytest

from aquasentinel.risk.policy import HABRiskPolicy

from .conftest import rehash_risk, validate


def test_frozen_models_and_independent_metadata(inputs, compute):
    result = compute(inputs)
    for obj, field, value in [(result, "product_id", "bad"),
                              (result.regions[0], "risk_score", 0.),
                              (result.regions[0].drivers[0], "component_value", 0.),
                              (result.site_summary, "risk_band", "Normal")]:
        with pytest.raises(FrozenInstanceError):
            setattr(obj, field, value)
    assert result.processing_parameters is not result.provenance.parameters
    copy = replace(result)
    copy.processing_parameters["identity"]["policy"].clear()
    copy.provenance.parameters.clear()
    validate(result, inputs)
    assert result.policy is not HABRiskPolicy()


def tamper(result, attack):
    r = result.regions[0]
    d = r.drivers[0]
    if attack.startswith("driver:"):
        field = attack.split(":")[1]
        changes = {
            "component_value": 41., "configured_weight": .36, "canonical_weight": .36,
            "effective_weight": .6, "contribution_points": 999., "availability": "unavailable",
            "unavailable_reason": "invented", "evidence_numerator": 13,
            "evidence_denominator": 31, "definition_id": "other",
            "source_product_ids": ("pc:shortcut",), "family_counts": (),
        }
        d = replace(d, **{field: changes[field]})
        return replace(result, regions=(replace(r, drivers=(d, *r.drivers[1:])),))
    if attack.startswith("region:"):
        field = attack.split(":")[1]
        changes = {"pixel_count": 7, "component_label": 2, "area_m2": 1., "region_id": "bad",
                   "risk_score": 75., "risk_band": "High", "component_coverage": .9,
                   "evidence_completeness": .9, "interpretation_flags": (),
                   "assessment_status": "confirmed", "monitoring_recommendation": "Shutdown",
                   "limitations": (), "family_counts": (), "explanation_order": ()}
        return replace(result, regions=(replace(r, **{field: changes[field]}),))
    if attack.startswith("factor:"):
        field = attack.split(":")[1]
        changed = replace(r.completeness_factors, **{field: 999 if "count" in field else .9})
        return replace(result, regions=(replace(r, completeness_factors=changed),))
    if attack.startswith("site:"):
        field = attack.split(":")[1]
        changes = {"selected_region": "bad", "selected_component_label": 999, "risk_score": 0.,
                   "risk_band": "Normal", "drivers": (), "limitations": (),
                   "assessment_status": "confirmed", "monitoring_recommendation": "Shutdown",
                   "evidence_completeness": 1., "component_coverage": 1.}
        return replace(result, site_summary=replace(result.site_summary, **{field: changes[field]}))
    if attack == "statistics":
        return replace(result, statistics=replace(result.statistics, region_count=2))
    if attack == "diagnostics":
        return replace(result, diagnostics=replace(result.diagnostics, overlap_disclosure="independent"))
    if attack == "target_time":
        return replace(result, target_acquired_at=result.target_acquired_at + timedelta(seconds=1))
    if attack == "grid":
        return replace(result, grid=replace(result.grid, grid_id="bad"))
    if attack == "weights":
        return replace(result, policy=HABRiskPolicy(weights=dict(zip(
            (n for n, _ in result.policy.weights), (.3, .25, .15, .15, .15)))))
    if attack == "bands":
        return replace(result, policy=HABRiskPolicy(low_max=23))
    if attack == "hidden_context":
        hidden = replace(r.drivers[3], component_value=80., availability="available",
                         unavailable_reason=None, effective_weight=.15, contribution_points=12.)
        return replace(result, regions=(replace(r, drivers=(*r.drivers[:3], hidden, r.drivers[4])),))
    if attack == "hidden_exposure":
        hidden = replace(r.drivers[4], component_value=80., availability="available",
                         unavailable_reason=None, effective_weight=.15, contribution_points=12.)
        return replace(result, regions=(replace(r, drivers=(*r.drivers[:4], hidden)),))
    raise AssertionError(attack)


ATTACKS = (
    *(f"driver:{f}" for f in ("component_value", "configured_weight", "canonical_weight",
        "effective_weight", "contribution_points", "availability", "unavailable_reason",
        "evidence_numerator", "evidence_denominator", "definition_id", "source_product_ids", "family_counts")),
    *(f"region:{f}" for f in ("pixel_count", "component_label", "area_m2", "region_id", "risk_score",
        "risk_band", "component_coverage", "evidence_completeness", "interpretation_flags",
        "assessment_status", "monitoring_recommendation", "limitations", "family_counts", "explanation_order")),
    *(f"factor:{f}" for f in ("family_available_count", "red_edge_available_count",
        "prior_supported_candidate_count", "family_availability", "candidate_history_coverage")),
    *(f"site:{f}" for f in ("selected_region", "selected_component_label", "risk_score", "risk_band",
        "drivers", "limitations", "assessment_status", "monitoring_recommendation",
        "evidence_completeness", "component_coverage")),
    "statistics", "diagnostics", "target_time", "grid", "weights", "bands",
    "hidden_context", "hidden_exposure",
)


@pytest.mark.parametrize("attack", ATTACKS)
@pytest.mark.parametrize("rehash", [False, True], ids=["stale", "attacker-rehashed"])
def test_semantic_tampering_rejected_even_if_attacker_rehashes(inputs, compute, attack, rehash):
    altered = tamper(compute(inputs), attack)
    if rehash:
        altered = rehash_risk(altered)
    with pytest.raises((ValueError, TypeError)):
        validate(altered, inputs)


@pytest.mark.parametrize("field,value", [("risk_score", True), ("pixel_count", True),
                                       ("risk_score", float("nan")), ("risk_score", float("inf"))])
def test_numeric_type_and_nonfinite_output_rejected(inputs, compute, field, value):
    result = compute(inputs)
    result = replace(result, regions=(replace(result.regions[0], **{field: value}),))
    with pytest.raises((ValueError, TypeError)):
        validate(result, inputs)


@pytest.mark.parametrize("field", ["regions", "drivers", "family_counts", "source_ids"])
def test_canonical_tuples_not_replaced_with_lists(inputs, compute, field):
    result = compute(inputs)
    if field == "regions":
        result = replace(result, regions=list(result.regions))
    elif field == "source_ids":
        result = replace(result, provenance=replace(result.provenance, source_ids=list(result.provenance.source_ids)))
    else:
        r = result.regions[0]
        result = replace(result, regions=(replace(r, **{field: list(getattr(r, field))}),))
    with pytest.raises((ValueError, TypeError)):
        validate(result, inputs)


@pytest.mark.parametrize("field,value", [("product_type", "other"), ("processing_version", "other"),
    ("source_ids", ("pc:shortcut",)), ("source_ids", ("temporal:shortcut",)),
    ("product_id", "hab_risk:wrong")])
def test_provenance_shortcuts_and_metadata_rejected(inputs, compute, field, value):
    result = compute(inputs)
    result = replace(result, provenance=replace(result.provenance, **{field: value}))
    with pytest.raises(ValueError):
        validate(result, inputs)


def test_altered_recommendation_policy_even_with_consistent_local_id(inputs, compute):
    from aquasentinel.risk.scoring import risk_product_id

    result = compute(inputs)
    parameters = deepcopy(result.processing_parameters)
    parameters["identity"]["policy"]["recommendations"]["High"] = "Shutdown"
    product_id = risk_product_id(parameters["identity"])
    result = replace(result, product_id=product_id, processing_parameters=parameters,
                     provenance=replace(result.provenance, product_id=product_id, parameters=parameters))
    with pytest.raises(ValueError):
        validate(result, inputs)


@pytest.mark.parametrize("url", [
    "https://example.test/data.tif?sv=synthetic&se=2099-01-01&sp=r&sig=SYNTHETIC_SAS_SECRET",
    "https://user:SYNTHETIC_PASSWORD@example.test/path", "https://example.test/path#secret",
])
def test_credential_urls_rejected_without_echo(inputs, compute, url):
    from aquasentinel.risk.scoring import _encoded

    with pytest.raises(ValueError) as exc:
        _encoded({"nested": [url]})
    assert "SYNTHETIC" not in str(exc.value) and url not in str(exc.value)
    result = compute(inputs)
    result.processing_parameters["extra"] = url
    with pytest.raises(ValueError) as exc:
        validate(result, inputs)
    assert "SYNTHETIC" not in str(exc.value) and url not in str(exc.value)
