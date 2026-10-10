import math
from dataclasses import replace

import numpy as np
import pytest

from aquasentinel.geometry.hab import FAMILY_ORDER
from aquasentinel.risk import HABRiskPolicy
from aquasentinel.risk.policy import ASSESSMENT_STATUS, COMPONENT_ORDER, NO_CANDIDATES_MESSAGE
from aquasentinel.risk.scoring import _explanation_order, _site_summary

from .conftest import validate


def test_three_components_exact_counts_score_and_driver_reconstruction(inputs, compute):
    result = compute(inputs)
    validate(result, inputs)
    r = result.regions[0]
    assert tuple(d.canonical_name for d in r.drivers) == COMPONENT_ORDER
    assert r.family_counts == tuple((n, 6, 6 if i in (0, 3) else 0) for i, n in enumerate(FAMILY_ORDER))
    assert [d.component_value for d in r.drivers] == [40., 100/3, 100., None, None]
    assert [d.evidence_denominator for d in r.drivers] == [30, 18, 6, None, None]
    weights = tuple(w for _, w in HABRiskPolicy().canonical_weights)
    expected = 100*math.fsum(w*(v/100) for w, v in zip(weights[:3], (40., 100/3, 100.)))/math.fsum(weights[:3])
    assert r.risk_score == expected
    assert r.component_coverage == .7
    assert r.evidence_completeness == .7
    assert r.completeness_factors.family_opportunity_count == 30
    assert r.completeness_factors.red_edge_opportunity_count == 18
    assert r.completeness_factors.prior_supported_candidate_count == 6
    reconstructed = 100*math.fsum(d.canonical_weight*(d.component_value/100) for d in r.drivers
                                 if d.availability == "available")/r.component_coverage
    assert reconstructed == r.risk_score
    for d in r.drivers:
        if d.component_value is not None:
            assert d.effective_weight == d.canonical_weight/r.component_coverage
            assert d.contribution_points == d.effective_weight*d.component_value
        else:
            assert d.unavailable_reason == "not_implemented"
            assert d.source_product_ids == ()
            assert d.effective_weight == 0 and d.contribution_points is None
    assert math.fsum(d.contribution_points for d in r.drivers if d.contribution_points is not None) == pytest.approx(r.risk_score)
    assert r.assessment_status == result.site_summary.assessment_status == ASSESSMENT_STATUS
    assert "correlated" in result.diagnostics.overlap_disclosure
    assert "correlated_red_edge_emphasis" in r.limitations


def test_no_prior_history_unknown_not_zero(make_inputs, compute):
    inputs = make_inputs(states=((True, True),))
    r = compute(inputs).regions[0]
    d = r.drivers[2]
    assert d.component_value is None and d.availability == "unavailable"
    assert d.unavailable_reason == "no_prior_valid_candidate_history"
    assert d.evidence_denominator == 0
    assert r.component_coverage == .55 and r.evidence_completeness == 0
    assert r.completeness_factors.candidate_history_coverage == 0
    assert r.risk_score is not None
    assert r.interpretation_flags == ("incomplete_evidence", "limited_evidence_completeness")


def test_partial_history_uses_c_over_b_and_b_over_a(make_inputs, compute):
    p = np.array([[1, 1, 1], [0, 0, 0]], bool)
    c = np.array([[1, 1, 0], [0, 0, 0]], bool)
    inputs = make_inputs(states=((p, c), (True, True)))
    r = compute(inputs).regions[0]
    assert r.persistence_evidence.target_pixel_count == 6
    assert r.persistence_evidence.persistence_evaluable_target_candidate_count == 3
    assert r.persistence_evidence.recurrent_candidate_count == 2
    assert r.drivers[2].component_value == 100*2/3
    assert r.completeness_factors.candidate_history_coverage == .5
    assert r.evidence_completeness == .5
    assert r.interpretation_flags == ("incomplete_evidence",)


def test_regional_availability_from_masks_not_global_diagnostics(make_inputs, compute):
    shape = (1, 3)
    # One connected 3-pixel region, with F2 available only at its first pixel.
    available = {FAMILY_ORDER[1]: np.array([[1, 0, 0]], bool)}
    inputs = make_inputs([{"available": available}], shape=shape)
    r = compute(inputs).regions[0]
    assert r.family_counts[1] == (FAMILY_ORDER[1], 1, 0)
    assert r.drivers[0].evidence_denominator == 13
    assert r.drivers[1].evidence_denominator == 7
    assert r.drivers[0].component_value == 100*6/13
    assert r.drivers[1].component_value == 100*3/7
    assert r.completeness_factors.family_availability == 13/15
    assert r.completeness_factors.red_edge_availability == 7/9


@pytest.mark.parametrize("evaluable", [True, False])
def test_zero_regions_none_not_normal(make_inputs, compute, evaluable):
    inputs = make_inputs(states=((evaluable, False),))
    result = compute(inputs)
    validate(result, inputs)
    s = result.site_summary
    assert result.regions == () and s.status == "no_candidate_regions"
    assert s.selected_region is s.risk_score is s.risk_band is s.evidence_completeness is None
    assert s.message == NO_CANDIDATES_MESSAGE
    assert s.policy_support_count == (6 if evaluable else 0)
    assert result.diagnostics.evaluable_observation is evaluable


def test_single_pixel_retained(make_inputs, compute):
    c = np.array([[1, 0, 0], [0, 0, 0]], bool)
    inputs = make_inputs(states=((True, c),))
    result = compute(inputs)
    r = result.regions[0]
    assert r.region_id == inputs[0].regions[0].region_id
    assert r.pixel_count == 1 and r.area_m2 == 400
    assert r.bbox_projected == inputs[0].regions[0].bbox_projected
    assert "single_pixel_region" in r.limitations
    assert result.statistics.single_pixel_region_count == 1


def test_multiple_regions_maximum_all_evidence_copied(make_inputs, compute):
    shape = (1, 5)
    candidates = np.array([[1, 1, 0, 1, 1]], bool)
    extra = np.array([[0, 0, 0, 1, 1]], bool)
    evidence = {f: extra for f in (FAMILY_ORDER[1], FAMILY_ORDER[2], FAMILY_ORDER[4])}
    inputs = make_inputs([{"candidate": candidates, "evidence": evidence}], shape=shape)
    result = compute(inputs)
    assert len(result.regions) == 2
    selected = result.regions[1]
    assert result.site_summary.selected_region == selected.region_id
    for field in ("risk_score", "risk_band", "evidence_completeness", "component_coverage",
                  "completeness_factors", "drivers", "monitoring_recommendation", "limitations",
                  "assessment_status", "explanation_order", "interpretation_flags"):
        assert getattr(result.site_summary, field) == getattr(selected, field)


def test_site_ties_completeness_then_label(inputs, compute):
    original = compute(inputs).regions[0]
    # Pure selector synthetic records; not fabricated upstream candidate parents.
    r1 = replace(original, region_id="r1", component_label=1, evidence_completeness=.1)
    r2 = replace(original, region_id="r2", component_label=2, evidence_completeness=.5)
    assert _site_summary((r1, r2), inputs[0].target_acquired_at, 6).selected_region == "r2"
    r1 = replace(r1, evidence_completeness=.5)
    assert _site_summary((r2, r1), inputs[0].target_acquired_at, 6).selected_region == "r1"


def test_driver_ties_canonical_missing_last(inputs, compute):
    drivers = compute(inputs).regions[0].drivers
    tied = tuple(replace(d, contribution_points=10. if d.component_value is not None else None)
                 for d in drivers)
    assert _explanation_order(tied) == COMPONENT_ORDER


def test_high_with_low_completeness_no_downgrade(make_inputs, compute):
    evidence = dict.fromkeys(FAMILY_ORDER, True)
    inputs = make_inputs([{"evidence": evidence}])
    r = compute(inputs).regions[0]
    assert r.risk_score == 100. and r.risk_band == "High"
    assert r.evidence_completeness == 0
    assert r.monitoring_recommendation == "High-priority field verification and increased monitoring"
    assert "limited_evidence_completeness" in r.interpretation_flags
