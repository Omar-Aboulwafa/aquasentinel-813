"""Decision 052 policy and pure binary64 arithmetic; no provider interface."""

from __future__ import annotations

import math
from collections.abc import Mapping
from dataclasses import dataclass, field
from itertools import pairwise
from numbers import Real
from typing import Any

COMPONENT_ORDER = (
    "spectral_anomaly", "chlorophyll_red_edge_signal", "persistence",
    "environmental_context", "intake_exposure",
)
DEFAULT_WEIGHTS = tuple(zip(COMPONENT_ORDER, (0.35, 0.20, 0.15, 0.15, 0.15)))
MANDATORY_COMPONENTS = COMPONENT_ORDER[:2]
ASSESSMENT_STATUS = "provisional_observational_screening"
LIMITED_COMPLETENESS_THRESHOLD = 0.50
RECOMMENDATIONS = (
    ("Normal", "Continue scheduled observation"),
    ("Watch", "Review on the next valid acquisition"),
    ("Elevated", "Prioritize targeted review and field verification"),
    ("High", "High-priority field verification and increased monitoring"),
)
UNSCORED_RECOMMENDATION = "Request evidence review / additional valid observations"
NO_CANDIDATES_MESSAGE = "No candidates under the frozen policy in evaluable observations."


def _number(value: Any, name: str, *, minimum: float, maximum: float) -> float:
    if isinstance(value, bool) or not isinstance(value, Real):
        raise TypeError(f"{name} must be a real non-boolean number.")
    try:
        value = float(value)
    except (OverflowError, ValueError):
        raise ValueError(f"{name} must be finite and in range.") from None
    if not math.isfinite(value) or not minimum <= value <= maximum:
        raise ValueError(f"{name} must be finite and in range.")
    return value


def _weights(values: Mapping | tuple) -> tuple[tuple[str, float], ...]:
    if isinstance(values, Mapping):
        pairs = tuple(values.items())
    elif type(values) is tuple:
        pairs = values
    else:
        raise ValueError("Weights require a mapping or canonical tuple.")
    if (
        len(pairs) != len(COMPONENT_ORDER)
        or any(type(p) is not tuple or len(p) != 2 for p in pairs)
        or any(type(p[0]) is not str for p in pairs)
        or {p[0] for p in pairs} != set(COMPONENT_ORDER)
    ):
        raise ValueError("Exactly the five recognized component weights are required.")
    supplied = dict(pairs)
    ordered = tuple((n, _number(supplied[n], "Weight", minimum=0, maximum=math.inf))
                    for n in COMPONENT_ORDER)
    try:
        total = math.fsum(v for _, v in ordered)
    except OverflowError:
        raise ValueError("Configured weight total must be finite.") from None
    if not math.isfinite(total) or total <= 0 or abs(total - 1.0) > 1e-9:
        raise ValueError("Configured weights must sum to one within 1e-9.")
    if any(supplied[n] <= 0 for n in MANDATORY_COMPONENTS):
        raise ValueError("Mandatory spectral/red-edge weights must be positive.")
    return ordered


@dataclass(frozen=True, slots=True)
class HABRiskPolicy:
    """Strict risk boundary; raw configuration is copied without changing its loader."""

    weights: tuple[tuple[str, float], ...] | Mapping[str, float] = DEFAULT_WEIGHTS
    low_max: int = 24
    watch_max: int = 49
    elevated_max: int = 74
    high_max: int = 100
    mandatory_components: tuple[str, ...] = field(default=MANDATORY_COMPONENTS, init=False)
    assessment_status: str = field(default=ASSESSMENT_STATUS, init=False)
    limited_evidence_completeness_threshold: float = field(
        default=LIMITED_COMPLETENESS_THRESHOLD, init=False
    )

    def __post_init__(self) -> None:
        object.__setattr__(self, "weights", _weights(self.weights))
        self.validate()

    def validate(self) -> None:
        if type(self.weights) is not tuple or self.weights != _weights(self.weights):
            raise ValueError("Policy weights must retain canonical storage order.")
        bands = (self.low_max, self.watch_max, self.elevated_max, self.high_max)
        if (any(type(v) is not int or v < 0 for v in bands)
                or any(a >= b for a, b in pairwise(bands)) or self.high_max != 100):
            raise ValueError("Bands require increasing nonnegative integer maxima ending at 100.")
        if (self.mandatory_components != MANDATORY_COMPONENTS
                or type(self.mandatory_components) is not tuple
                or self.assessment_status != ASSESSMENT_STATUS
                or type(self.limited_evidence_completeness_threshold) is not float
                or self.limited_evidence_completeness_threshold != LIMITED_COMPLETENESS_THRESHOLD):
            raise ValueError("Fixed Decision 052 qualification/mandatory/completeness policy changed.")

    @property
    def canonical_weights(self) -> tuple[tuple[str, float], ...]:
        self.validate()
        total = math.fsum(v for _, v in self.weights)
        return tuple((n, q / total) for n, q in self.weights)

    def to_dict(self) -> dict[str, Any]:
        self.validate()
        return {
            "decision": "052", "version": "as107-v1",
            "component_order": list(COMPONENT_ORDER),
            "raw_weights": dict(self.weights), "canonical_weights": dict(self.canonical_weights),
            "mandatory_components": list(self.mandatory_components),
            "assessment_status": self.assessment_status,
            "limited_evidence_completeness_threshold": self.limited_evidence_completeness_threshold,
            "bands": dict(zip(("low_max", "watch_max", "elevated_max", "high_max"),
                              (self.low_max, self.watch_max, self.elevated_max, self.high_max))),
            "band_semantics": "unrounded binary64; maxima+1 cuts; no epsilon/snapping",
            "definitions": {
                "spectral_anomaly": "100*sum(v_all)/sum(a_all); family-pixel evidence breadth",
                "chlorophyll_red_edge_signal": "100*sum(v_F1_F3)/sum(a_F1_F3); red-edge family evidence breadth",
                "persistence": "100*C/B; B=0 unavailable/no_prior_valid_candidate_history",
                "environmental_context": "unavailable/not_implemented; no source",
                "intake_exposure": "unavailable/not_implemented; no source",
            },
            "missing": "None; no zero/neutral/imputation; renormalize available canonical weights",
            "risk": "100*fsum(w_i*(x_i/100) canonical available order)/fsum(available w_i)",
            "coverage": "available configured weight/all configured weight; canonical K",
            "completeness": "min(coverage,sum(a)/(5*A),sum(a_F1_F3)/(3*A),B/A)",
            "completeness_flags": "<1 incomplete_evidence; <0.50 limited_evidence_completeness",
            "overlap": "F1-F3 in spectral and red-edge; correlated, deliberate emphasis",
            "regions": "authoritative AS-105; retain all; one pixel single_pixel_region",
            "site_selection": "descending raw score, descending completeness, ascending label",
            "driver_storage": list(COMPONENT_ORDER),
            "driver_explanation": "descending available contribution; canonical ties; unavailable last",
            "driver_contribution": "effective_weight=w_i/K; points=effective_weight*x_i",
            "recommendations": dict(RECOMMENDATIONS),
            "unscored_recommendation": UNSCORED_RECOMMENDATION,
            "no_regions": {"status": "no_candidate_regions", "message": NO_CANDIDATES_MESSAGE},
            "numeric": "finite binary64; exact counts; fsum; no clipping/NaN/bool numerics",
            "serialization": "sorted keys; fixed lists; UTC; exact float hex; null unavailable",
        }


def risk_band(score: float, policy: HABRiskPolicy) -> str:
    policy.validate()
    value = _number(score, "Risk score", minimum=0, maximum=100)
    for name, cut in zip((n for n, _ in RECOMMENDATIONS),
                         (policy.low_max + 1, policy.watch_max + 1, policy.elevated_max + 1)):
        if value < cut:
            return name
    return "High"


def _score_components(
    values: Mapping[str, float | None], policy: HABRiskPolicy,
) -> tuple[float | None, float, tuple[float, ...]]:
    """Pure arithmetic kernel, including synthetic future components; no provider hook."""
    policy.validate()
    if not isinstance(values, Mapping) or set(values) != set(COMPONENT_ORDER):
        raise ValueError("Arithmetic requires exactly the five component names.")
    checked = tuple(None if values[n] is None else _number(
        values[n], "Component value", minimum=0, maximum=100
    ) for n in COMPONENT_ORDER)
    weights = tuple(w for _, w in policy.canonical_weights)
    coverage = math.fsum(w for w, v in zip(weights, checked) if v is not None)
    effective = tuple(w / coverage if v is not None and coverage else 0.0
                      for w, v in zip(weights, checked))
    if coverage == 0 or any(values[n] is None for n in MANDATORY_COMPONENTS):
        return None, coverage, effective
    score = 100.0 * math.fsum(w * (v / 100.0) for w, v in zip(weights, checked)
                              if v is not None) / coverage
    return _number(score, "Risk score", minimum=0, maximum=100), coverage, effective


def _completeness_flags(value: float) -> tuple[str, ...]:
    value = _number(value, "Evidence completeness", minimum=0, maximum=1)
    return tuple(name for cut, name in (
        (1.0, "incomplete_evidence"), (LIMITED_COMPLETENESS_THRESHOLD, "limited_evidence_completeness")
    ) if value < cut)
