import math
from dataclasses import FrozenInstanceError

import pytest

from aquasentinel.risk import HABRiskPolicy
from aquasentinel.risk.policy import (
    COMPONENT_ORDER,
    DEFAULT_WEIGHTS,
    _completeness_flags,
    _score_components,
    risk_band,
)


def components(**changes):
    return {**dict(zip(COMPONENT_ORDER, (40.0, 60.0, 20.0, None, None))), **changes}


def test_policy_strict_canonical_copy_integer_and_float_weights():
    raw = dict(reversed(DEFAULT_WEIGHTS))
    p = HABRiskPolicy(weights=raw)
    raw.clear()
    assert p.weights == DEFAULT_WEIGHTS
    assert tuple(p.to_dict()["raw_weights"]) == COMPONENT_ORDER
    assert math.fsum(v for _, v in p.canonical_weights) == 1
    integer = dict(zip(COMPONENT_ORDER, (0.5, 0.5, 0, 0, 0)))
    assert HABRiskPolicy(weights=integer).weights[2][1] == 0.0
    with pytest.raises(FrozenInstanceError):
        p.low_max = 1


@pytest.mark.parametrize("bad", [True, False, "0.35", None, math.nan, math.inf, -math.inf, -0.1, 0])
def test_invalid_required_weight(bad):
    weights = dict(DEFAULT_WEIGHTS)
    weights[COMPONENT_ORDER[0]] = bad
    with pytest.raises((ValueError, TypeError)):
        HABRiskPolicy(weights=weights)


@pytest.mark.parametrize("change", ["missing", "extra", "duplicate", "zero_total", "bad_total", "overflow"])
def test_weight_structure_total_rejected(change):
    weights = dict(DEFAULT_WEIGHTS)
    if change == "missing":
        weights.pop(COMPONENT_ORDER[-1])
    elif change == "extra":
        weights["other"] = 0
    elif change == "duplicate":
        weights = (*DEFAULT_WEIGHTS[:-1], DEFAULT_WEIGHTS[0])
    elif change == "zero_total":
        weights = dict.fromkeys(COMPONENT_ORDER, 0)
    elif change == "bad_total":
        weights[COMPONENT_ORDER[-1]] = 0.2
    else:
        weights = dict.fromkeys(COMPONENT_ORDER, 1e308)
    with pytest.raises((ValueError, TypeError)):
        HABRiskPolicy(weights=weights)


def test_positive_mandatory_weights_even_when_total_valid():
    for name in COMPONENT_ORDER[:2]:
        weights = dict(DEFAULT_WEIGHTS)
        weights[COMPONENT_ORDER[-1]] += weights[name]
        weights[name] = 0
        with pytest.raises(ValueError, match="Mandatory"):
            HABRiskPolicy(weights=weights)


def test_existing_sum_tolerance_and_raw_normalized_metadata():
    weights = dict(DEFAULT_WEIGHTS)
    weights[COMPONENT_ORDER[-1]] += 5e-10
    p = HABRiskPolicy(weights=weights)
    assert dict(p.weights) == weights
    total = math.fsum(weights.values())
    assert p.canonical_weights == tuple((n, weights[n] / total) for n in COMPONENT_ORDER)
    weights[COMPONENT_ORDER[-1]] += 2e-9
    with pytest.raises(ValueError):
        HABRiskPolicy(weights=weights)


@pytest.mark.parametrize("field", ["low_max", "watch_max", "elevated_max", "high_max"])
@pytest.mark.parametrize("bad", [True, -1, 2.5, "24", None])
def test_invalid_band_types_ranges(field, bad):
    with pytest.raises(ValueError):
        HABRiskPolicy(**{field: bad})


@pytest.mark.parametrize("bands", [(24, 24, 74, 100), (50, 49, 74, 100), (24, 49, 100, 100),
                                  (24, 49, 74, 99)])
def test_nonincreasing_or_non100_bands(bands):
    with pytest.raises(ValueError):
        HABRiskPolicy(**dict(zip(("low_max", "watch_max", "elevated_max", "high_max"), bands)))


@pytest.mark.parametrize("score,band", [(0, "Normal"), (24, "Normal"), (25, "Watch"),
    (49, "Watch"), (50, "Elevated"), (74, "Elevated"), (75, "High"), (100, "High")])
def test_exact_band_boundaries(score, band):
    assert risk_band(score, HABRiskPolicy()) == band


@pytest.mark.parametrize("cut,below,above", [(25., "Normal", "Watch"),
                                           (50., "Watch", "Elevated"), (75., "Elevated", "High")])
def test_nextafter_neighbours_and_display_rounding(cut, below, above):
    p = HABRiskPolicy()
    lower, higher = math.nextafter(cut, -math.inf), math.nextafter(cut, math.inf)
    assert round(lower, 2) == round(higher, 2) == cut
    assert risk_band(lower, p) == below
    assert risk_band(cut, p) == risk_band(higher, p) == above


@pytest.mark.parametrize("score", [True, False, -1, 101, math.nan, math.inf, -math.inf, "50"])
def test_invalid_score_rejected(score):
    with pytest.raises((ValueError, TypeError)):
        risk_band(score, HABRiskPolicy())


def test_custom_integer_maxima_derive_continuous_cuts():
    p = HABRiskPolicy(low_max=9, watch_max=19, elevated_max=29)
    assert risk_band(math.nextafter(10., 0.), p) == "Normal"
    assert risk_band(10., p) == "Watch"
    assert risk_band(20., p) == "Elevated"
    assert risk_band(30., p) == "High"


@pytest.mark.parametrize("missing", COMPONENT_ORDER[:2])
def test_missing_mandatory_no_fallback(missing):
    score, coverage, _ = _score_components(components(**{missing: None}), HABRiskPolicy())
    assert score is None
    assert coverage > 0


def test_zero_score_and_zero_coverage_kernel_only():
    # No impossible zero-evidence AS-105 candidate is fabricated for this boundary.
    score, coverage, _ = _score_components(dict.fromkeys(COMPONENT_ORDER, 0.0), HABRiskPolicy())
    assert score == 0.0 and coverage == 1
    assert _score_components(dict.fromkeys(COMPONENT_ORDER), HABRiskPolicy()) == (None, 0.0, (0.,)*5)


def test_all_five_synthetic_arithmetic_only():
    values = dict(zip(COMPONENT_ORDER, (10., 20., 30., 40., 50.)))
    score, coverage, effective = _score_components(values, HABRiskPolicy())
    assert score == 100*math.fsum(w*(values[n]/100) for n, w in DEFAULT_WEIGHTS)
    assert coverage == 1 and effective == tuple(w for _, w in DEFAULT_WEIGHTS)


@pytest.mark.parametrize("name", COMPONENT_ORDER)
@pytest.mark.parametrize("bad", [True, "10", math.nan, math.inf, -1., 101.])
def test_invalid_component_rejected_before_arithmetic(name, bad):
    with pytest.raises((ValueError, TypeError)):
        _score_components(components(**{name: bad}), HABRiskPolicy())


@pytest.mark.parametrize("value,flags", [(1., ()), (.5, ("incomplete_evidence",)),
    (math.nextafter(.5, 0.), ("incomplete_evidence", "limited_evidence_completeness")),
    (0., ("incomplete_evidence", "limited_evidence_completeness"))])
def test_flag_boundaries(value, flags):
    assert _completeness_flags(value) == flags
