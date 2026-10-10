"""Offline regional Decision 052 scoring and regeneration-based integrity."""

from __future__ import annotations

import math
import platform
from collections.abc import Iterable, Mapping
from copy import deepcopy
from dataclasses import fields, is_dataclass
from datetime import UTC, datetime
from hashlib import sha256
from typing import Any

import numpy as np

from aquasentinel.geometry.hab import FAMILY_ORDER
from aquasentinel.geometry.models import HABAnomalyGeometryScene
from aquasentinel.persistence.models import HABPersistenceScene
from aquasentinel.preprocessing.cache import canonical_json
from aquasentinel.preprocessing.models import AnalysisGrid
from aquasentinel.provenance import DerivedProductRecord
from aquasentinel.risk.models import (
    EvidenceCompletenessFactors,
    HABRegionRisk,
    HABRiskDiagnostics,
    HABRiskScene,
    HABRiskStatistics,
    HABSiteRiskSummary,
    RiskDriver,
)
from aquasentinel.risk.policy import (
    ASSESSMENT_STATUS,
    COMPONENT_ORDER,
    NO_CANDIDATES_MESSAGE,
    RECOMMENDATIONS,
    UNSCORED_RECOMMENDATION,
    HABRiskPolicy,
    _completeness_flags,
    _score_components,
    risk_band,
)
from aquasentinel.temporal.models import TemporalFeatureScene, utc

PROCESSING_VERSION = "as107-v1"
INPUT_FORMAT = "as107-input-v1"
OUTPUT_FORMAT = "as107-output-v1"
OVERLAP_DISCLOSURE = (
    "F1-F3 contribute to both spectral and red-edge components: correlated/overlapping "
    "evidence, not independent corroboration; weights deliberately emphasize red-edge evidence."
)
SCIENTIFIC_LIMIT = (
    "Provisional observational HAB-like screening only; not confirmed HAB, species, toxins, "
    "chlorophyll concentration, biological certainty, probability, calibrated confidence, "
    "accuracy, warning lead time, water safety, shutdown advice or complete intake risk. "
    "Al Raha is a validation AOI, not a confirmed intake."
)
BASE_LIMITATIONS = (
    "provisional_observational_screening", "environmental_context_unavailable",
    "intake_exposure_unavailable", "correlated_red_edge_emphasis",
    "candidate_conditioned_screening", "heuristic_weights_not_calibrated",
    "shared_sparse_histories_not_independent_confirmation",
    "five_histories_not_statistical_sufficiency", "exact_pixel_recurrence_no_motion_tracking",
    "observation_gaps_not_continuous_biological_persistence",
    "future_AS105_policy_validation_not_run", "not_biological_or_operational_validation",
)


def _exact(value: Any) -> Any:
    """Exact typed binary64 metadata, stable URLs guarded by canonical_json afterward."""
    if is_dataclass(value) and not isinstance(value, type):
        return {"record_type": type(value).__name__, "fields": {
            f.name: _exact(getattr(value, f.name)) for f in fields(value)
        }}
    if isinstance(value, datetime):
        return {"utc": utc(value).isoformat()}
    if type(value) is float:
        if not math.isfinite(value):
            raise ValueError("Stable risk metadata requires finite binary64 values.")
        return {"binary64": value.hex()}
    if type(value) is dict:
        if any(type(k) is not str for k in value):
            raise ValueError("Risk metadata keys must be strings.")
        return {k: _exact(v) for k, v in value.items()}
    if type(value) in (tuple, list):
        # Container types matter for typed output validation; map order does not.
        return {"sequence_type": type(value).__name__, "items": [_exact(v) for v in value]}
    if value is None or type(value) in (str, int, bool):
        return value
    raise ValueError("Unsupported value in stable risk metadata.")


def _encoded(value: Any) -> bytes:
    return canonical_json(_exact(value))


def _segment(digest, header: dict, payload: bytes = b"") -> None:
    encoded = canonical_json({**header, "byte_count": len(payload)})
    digest.update(len(encoded).to_bytes(8, "big"))
    digest.update(encoded)
    digest.update(payload)


def _region_identity(region) -> dict[str, Any]:
    return {n: getattr(region, n) for n in (
        "region_id", "component_label", "pixel_count", "area_m2", "area_km2",
        "bbox_projected", "first_pixel_row", "first_pixel_col", "participating_families",
        "family_evidence_pixel_counts",
    )}


def input_content_fingerprint(
    geometry: HABAnomalyGeometryScene, persistence: HABPersistenceScene,
) -> str:
    """Consumed target support/masks/regions and recurrence explanations, not raw features."""
    digest = sha256()
    _segment(digest, {"format": INPUT_FORMAT, "grid": geometry.grid.to_dict()})
    for name, array, dtype in (
        ("policy_support", geometry.candidate_analysis_support_mask, "uint8"),
        ("candidate", geometry.candidate_mask, "uint8"),
        ("component_labels", geometry.component_labels, "<i4"),
    ):
        _segment(digest, {"field": name, "shape": array.shape, "dtype": dtype},
                 np.asarray(array, dtype=dtype).tobytes(order="C"))
    candidate = geometry.candidate_mask
    for family in FAMILY_ORDER:
        for field in ("family_available_masks", "family_evidence_masks"):
            values = getattr(geometry, field)[family][candidate]
            _segment(digest, {"field": field, "family": family, "dtype": "uint8",
                              "selection": "target candidate row-major", "shape": values.shape},
                     np.asarray(values, dtype="uint8").tobytes(order="C"))
    for field, dtype in (
        ("prior_valid_observation_count", "<u4"), ("persistence_evaluable_mask", "uint8"),
        ("current_streak_count", "<u4"), ("recurrent_candidate_mask", "uint8"),
        ("previous_valid_observation_gap_us", "<i8"), ("current_streak_span_us", "<i8"),
    ):
        values = getattr(persistence, field)[candidate]
        _segment(digest, {"field": field, "dtype": dtype,
                          "selection": "target candidate row-major", "shape": values.shape},
                 np.asarray(values, dtype=dtype).tobytes(order="C"))
    _segment(digest, {"field": "authoritative_regions"},
             _encoded(tuple(_region_identity(r) for r in geometry.regions)))
    _segment(digest, {"field": "regional_persistence_explanations"}, _encoded(persistence.regions))
    return digest.hexdigest()


def _validated_inputs(
    geometry: HABAnomalyGeometryScene, persistence: HABPersistenceScene,
    sequence: Iterable[HABAnomalyGeometryScene], witnesses: Mapping[str, TemporalFeatureScene],
    policy: HABRiskPolicy,
) -> None:
    if type(policy) is not HABRiskPolicy:
        raise TypeError("AS-107 requires a HABRiskPolicy.")
    policy.validate()
    if type(geometry) is not HABAnomalyGeometryScene or type(persistence) is not HABPersistenceScene:
        raise TypeError("AS-107 requires typed AS-105 geometry and AS-106 persistence.")
    if not isinstance(witnesses, Mapping):
        raise TypeError("Temporal witnesses must be a mapping keyed by product ID.")
    scenes = tuple(sequence)
    # Existing full parent chain; do not bypass or repair any frozen validator.
    persistence.validate(scenes, temporal_parents=witnesses)
    if (geometry.provenance.processing_version != "as105-v1"
            or persistence.provenance.processing_version != "as106-v1"):
        raise ValueError("AS-107 v1 requires frozen AS-105/AS-106 v1 contracts.")
    parent = witnesses.get(geometry.parent_temporal_product_id)
    if type(parent) is not TemporalFeatureScene:
        raise ValueError("A typed immediate temporal integrity witness is required.")
    geometry.validate(parent)
    target = next((s for s in scenes if s.product_id == persistence.target_geometry_product_id), None)
    if (target is None or geometry.product_id != persistence.target_geometry_product_id
            or geometry.grid != persistence.grid
            or utc(geometry.target_acquired_at) != utc(persistence.target_acquired_at)
            or canonical_json(geometry.processing_parameters) != canonical_json(target.processing_parameters)
            or _encoded(tuple(_region_identity(r) for r in geometry.regions))
            != _encoded(tuple(_region_identity(r) for r in target.regions))):
        raise ValueError("Explicit geometry must exactly match the persistence target.")
    for array, other in (
        (geometry.candidate_analysis_support_mask, persistence.target_candidate_analysis_support_mask),
        (geometry.candidate_mask, persistence.target_candidate_mask),
        (geometry.component_labels, persistence.target_component_labels),
    ):
        if not np.array_equal(array, other):
            raise ValueError("Target support/candidates/labels must agree exactly.")
    if tuple((r.region_id, r.component_label, r.pixel_count) for r in geometry.regions) != tuple(
        (r.region_id, r.component_label, r.target_pixel_count) for r in persistence.regions
    ):
        raise ValueError("Target regional identity/counts must agree exactly.")


def _explanation_order(drivers: tuple[RiskDriver, ...]) -> tuple[str, ...]:
    return tuple(d.canonical_name for _, d in sorted(enumerate(drivers), key=lambda item: (
        item[1].availability != "available",
        -(item[1].contribution_points or 0.0), item[0]
    )))


def _regions(
    geometry: HABAnomalyGeometryScene, persistence: HABPersistenceScene, policy: HABRiskPolicy,
) -> tuple[HABRegionRisk, ...]:
    result = []
    for region, history in zip(geometry.regions, persistence.regions):
        mask = geometry.component_labels == region.component_label
        count = int(mask.sum())
        if count <= 0 or count != region.pixel_count:
            raise ValueError("Authoritative regions must have positive consistent support.")
        family_counts = tuple((name, int((mask & geometry.family_available_masks[name]).sum()),
                               int((mask & geometry.family_evidence_masks[name]).sum()))
                              for name in FAMILY_ORDER)
        if any(not 0 <= v <= a <= count for _, a, v in family_counts):
            raise ValueError("Family evidence must be contained in regional available support.")
        a, b, c = (history.target_pixel_count, history.persistence_evaluable_target_candidate_count,
                   history.recurrent_candidate_count)
        if any(type(n) is not int for n in (a, b, c)) or not 0 <= c <= b <= a or a != count:
            raise ValueError("Regional persistence counts must satisfy 0 <= C <= B <= A.")
        numerators = (sum(v for _, _, v in family_counts),
                      sum(v for _, _, v in family_counts[:3]), c, None, None)
        denominators = (sum(n for _, n, _ in family_counts),
                        sum(n for _, n, _ in family_counts[:3]), b, None, None)
        values = dict(zip(COMPONENT_ORDER, (
            100.0 * n / d if d else None for n, d in zip(numerators, denominators)
        )))
        score, coverage, effective = _score_components(values, policy)
        # Decision 050 candidates necessarily have >=2 votes including red-edge.
        # A fully validated nonempty region cannot reach missing-mandatory scoring.
        # Reject an impossible invariant rather than invent a new site status.
        if score is None:
            raise ValueError("Validated candidate region lacks mandatory family support.")
        drivers = []
        for i, ((name, q), (_, w)) in enumerate(zip(policy.weights, policy.canonical_weights)):
            value = values[name]
            reason = ("no_prior_valid_candidate_history" if name == "persistence"
                      else "not_implemented" if i >= 3 else "no_available_family_support")
            counts = family_counts if i == 0 else family_counts[:3] if i == 1 else ()
            sources = (geometry.product_id,) if i < 2 else (
                (persistence.product_id,) if i == 2 else ()
            )
            drivers.append(RiskDriver(
                name, value, q, w, effective[i], None if value is None else effective[i] * value,
                "unavailable" if value is None else "available", reason if value is None else None,
                numerators[i], denominators[i], counts, f"as107-v1:{name}", sources,
            ))
        drivers = tuple(drivers)
        factors = EvidenceCompletenessFactors(
            coverage, math.fsum(q for n, q in policy.weights if values[n] is not None),
            math.fsum(q for _, q in policy.weights), denominators[0] / (5 * count),
            denominators[0], 5 * count, denominators[1] / (3 * count), denominators[1],
            3 * count, b / a, b, a,
        )
        completeness = min(coverage, factors.family_availability, factors.red_edge_availability,
                           factors.candidate_history_coverage)
        band = risk_band(score, policy)
        limitations = (*BASE_LIMITATIONS, *(('single_pixel_region',) if count == 1 else ()),
                       *(('no_prior_valid_candidate_history',) if b == 0 else ()))
        result.append(HABRegionRisk(
            region.region_id, region.component_label, count, region.area_m2, region.area_km2,
            tuple(region.bbox_projected), region.first_pixel_row, region.first_pixel_col,
            tuple(region.participating_families), family_counts, deepcopy(history), drivers,
            _explanation_order(drivers), score, band, coverage, completeness, factors,
            _completeness_flags(completeness), ASSESSMENT_STATUS, dict(RECOMMENDATIONS)[band],
            limitations,
        ))
    return tuple(result)


def _site_summary(
    regions: tuple[HABRegionRisk, ...], acquired_at: datetime, policy_support_count: int,
) -> HABSiteRiskSummary:
    if not regions:
        return HABSiteRiskSummary(
            "no_candidate_regions", None, None, None, None, None, None, None, (), (), (),
            ASSESSMENT_STATUS, UNSCORED_RECOMMENDATION, BASE_LIMITATIONS, NO_CANDIDATES_MESSAGE,
            acquired_at, policy_support_count,
        )
    scored = tuple(r for r in regions if r.risk_score is not None)
    if not scored:
        raise ValueError("Validated nonempty candidate regions must have mandatory support.")
    selected = min(scored, key=lambda r: (-r.risk_score, -r.evidence_completeness, r.component_label))
    return HABSiteRiskSummary(
        None, selected.region_id, selected.component_label, selected.risk_score, selected.risk_band,
        selected.evidence_completeness, selected.component_coverage, selected.completeness_factors,
        selected.drivers, selected.explanation_order, selected.interpretation_flags,
        selected.assessment_status, selected.monitoring_recommendation, selected.limitations,
        None, acquired_at, policy_support_count,
    )


def _semantic_output(value: HABRiskScene | dict) -> dict:
    names = ("grid", "target_acquired_at", "target_geometry_product_id", "persistence_product_id",
             "policy", "regions", "site_summary", "statistics", "diagnostics")
    data = {n: value[n] if type(value) is dict else getattr(value, n) for n in names}
    if type(data["grid"]) is not AnalysisGrid:
        raise TypeError("Risk grid must be a typed AnalysisGrid.")
    data["grid"] = data["grid"].to_dict()
    return data


def output_content_fingerprint(value: HABRiskScene | dict) -> str:
    digest = sha256()
    _segment(digest, {"format": OUTPUT_FORMAT}, _encoded(_semantic_output(value)))
    return digest.hexdigest()


def risk_product_id(identity: dict[str, Any]) -> str:
    return "hab_risk:" + sha256(_encoded(identity)).hexdigest()


def _build(
    geometry: HABAnomalyGeometryScene, persistence: HABPersistenceScene,
    policy: HABRiskPolicy, created_at: datetime,
) -> HABRiskScene:
    time = utc(geometry.target_acquired_at)
    parents = (geometry.product_id, persistence.product_id)
    regions = _regions(geometry, persistence, policy)
    support_count = int(geometry.candidate_analysis_support_mask.sum())
    candidate_count = int(geometry.candidate_mask.sum())
    input_hash = input_content_fingerprint(geometry, persistence)
    identity = {
        "processing_version": PROCESSING_VERSION, "source_product_ids": parents,
        "parent_contract_versions": ("as105-v1", "as106-v1", "as104-v1_witness"),
        "target_acquired_at": time.isoformat(), "grid": geometry.grid.to_dict(),
        "input_fingerprint_format": INPUT_FORMAT, "input_content_fingerprint": input_hash,
        "policy": policy.to_dict(),
        "software_versions": {"python": platform.python_version(), "numpy": np.__version__},
    }
    data = {
        "grid": geometry.grid, "target_acquired_at": time,
        "target_geometry_product_id": parents[0], "persistence_product_id": parents[1],
        "policy": deepcopy(policy), "regions": regions,
        "site_summary": _site_summary(regions, time, support_count),
        "statistics": HABRiskStatistics(len(regions), len(regions),
                                        sum(r.pixel_count == 1 for r in regions),
                                        support_count, candidate_count),
        "diagnostics": HABRiskDiagnostics(
            COMPONENT_ORDER[3:], tuple(r.component_label for r in regions
                                      if r.persistence_evidence.persistence_evaluable_target_candidate_count == 0),
            OVERLAP_DISCLOSURE, SCIENTIFIC_LIMIT, support_count > 0,
        ),
    }
    output_hash = output_content_fingerprint(data)
    product_id = risk_product_id(identity)
    parameters = {
        "identity": identity, "output_fingerprint_format": OUTPUT_FORMAT,
        "output_content_fingerprint": output_hash,
        "scientific_limit": SCIENTIFIC_LIMIT, "overlap_disclosure": OVERLAP_DISCLOSURE,
    }
    provenance = DerivedProductRecord(product_id, "hab_risk", utc(created_at), PROCESSING_VERSION,
                                      parents, deepcopy(parameters))
    return HABRiskScene(**data, input_content_fingerprint=input_hash,
                        output_content_fingerprint=output_hash, processing_parameters=parameters,
                        product_id=product_id, provenance=provenance)


def compute_hab_risk(
    geometry_scene: HABAnomalyGeometryScene, persistence_scene: HABPersistenceScene, *,
    geometry_scenes: Iterable[HABAnomalyGeometryScene],
    temporal_parents: Mapping[str, TemporalFeatureScene], policy: HABRiskPolicy,
) -> HABRiskScene:
    """Pure scoring over fully validated typed parents; no external-system effects."""
    _validated_inputs(geometry_scene, persistence_scene, geometry_scenes, temporal_parents, policy)
    return _build(geometry_scene, persistence_scene, policy, datetime.now(UTC))


def validate_scene(
    scene: HABRiskScene, geometry_scene: HABAnomalyGeometryScene,
    persistence_scene: HABPersistenceScene, *, geometry_scenes: Iterable[HABAnomalyGeometryScene],
    temporal_parents: Mapping[str, TemporalFeatureScene], policy: HABRiskPolicy,
) -> None:
    if type(scene) is not HABRiskScene:
        raise TypeError("Expected a HABRiskScene.")
    if type(scene.provenance) is not DerivedProductRecord:
        raise TypeError("Expected a typed DerivedProductRecord.")
    scene.provenance.validate()
    _validated_inputs(geometry_scene, persistence_scene, geometry_scenes, temporal_parents, policy)
    expected = _build(geometry_scene, persistence_scene, policy, scene.provenance.created_at)
    if (
        _encoded(_semantic_output(scene)) != _encoded(_semantic_output(expected))
        or scene.input_content_fingerprint != expected.input_content_fingerprint
        or scene.output_content_fingerprint != expected.output_content_fingerprint
        or scene.product_id != expected.product_id
        or _encoded(scene.processing_parameters) != _encoded(expected.processing_parameters)
        or _encoded(scene.provenance) != _encoded(expected.provenance)
    ):
        raise ValueError("Risk outputs/identity/provenance disagree with validated parents and policy.")
