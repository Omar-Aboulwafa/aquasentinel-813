"""Immutable typed observational screening results; no probability/confidence field."""

from __future__ import annotations

from collections.abc import Iterable, Mapping
from copy import deepcopy
from dataclasses import dataclass, replace
from datetime import datetime
from typing import Any

from aquasentinel.geometry.models import HABAnomalyGeometryScene
from aquasentinel.persistence.models import HABPersistenceScene, PersistenceRegionSummary
from aquasentinel.preprocessing.models import AnalysisGrid
from aquasentinel.provenance import DerivedProductRecord
from aquasentinel.risk.policy import HABRiskPolicy
from aquasentinel.temporal.models import TemporalFeatureScene


@dataclass(frozen=True, slots=True)
class RiskDriver:
    canonical_name: str
    component_value: float | None
    configured_weight: float
    canonical_weight: float
    effective_weight: float
    contribution_points: float | None
    availability: str
    unavailable_reason: str | None
    evidence_numerator: int | None
    evidence_denominator: int | None
    family_counts: tuple[tuple[str, int, int], ...]
    definition_id: str
    source_product_ids: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class EvidenceCompletenessFactors:
    component_coverage: float
    available_configured_weight: float
    total_configured_weight: float
    family_availability: float
    family_available_count: int
    family_opportunity_count: int
    red_edge_availability: float
    red_edge_available_count: int
    red_edge_opportunity_count: int
    candidate_history_coverage: float
    prior_supported_candidate_count: int
    target_candidate_count: int


@dataclass(frozen=True, slots=True)
class HABRegionRisk:
    region_id: str
    component_label: int
    pixel_count: int
    area_m2: float
    area_km2: float
    bbox_projected: tuple[float, float, float, float]
    first_pixel_row: int
    first_pixel_col: int
    participating_families: tuple[str, ...]
    family_counts: tuple[tuple[str, int, int], ...]
    persistence_evidence: PersistenceRegionSummary
    drivers: tuple[RiskDriver, ...]
    explanation_order: tuple[str, ...]
    risk_score: float | None
    risk_band: str | None
    component_coverage: float
    evidence_completeness: float
    completeness_factors: EvidenceCompletenessFactors
    interpretation_flags: tuple[str, ...]
    assessment_status: str
    monitoring_recommendation: str
    limitations: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class HABSiteRiskSummary:
    # None means no empty-support status. Qualification is assessment_status.
    # No additional scientific/site-status policy string is introduced.
    status: str | None
    selected_region: str | None
    selected_component_label: int | None
    risk_score: float | None
    risk_band: str | None
    evidence_completeness: float | None
    component_coverage: float | None
    completeness_factors: EvidenceCompletenessFactors | None
    drivers: tuple[RiskDriver, ...]
    explanation_order: tuple[str, ...]
    interpretation_flags: tuple[str, ...]
    assessment_status: str
    monitoring_recommendation: str
    limitations: tuple[str, ...]
    message: str | None
    target_acquired_at: datetime
    policy_support_count: int


@dataclass(frozen=True, slots=True)
class HABRiskStatistics:
    region_count: int
    scored_region_count: int
    single_pixel_region_count: int
    target_policy_support_count: int
    target_candidate_count: int


@dataclass(frozen=True, slots=True)
class HABRiskDiagnostics:
    missing_components: tuple[str, ...]
    persistence_unavailable_region_labels: tuple[int, ...]
    overlap_disclosure: str
    scientific_limit: str
    evaluable_observation: bool


@dataclass(frozen=True, slots=True)
class HABRiskScene:
    grid: AnalysisGrid
    target_acquired_at: datetime
    target_geometry_product_id: str
    persistence_product_id: str
    policy: HABRiskPolicy
    regions: tuple[HABRegionRisk, ...]
    site_summary: HABSiteRiskSummary
    statistics: HABRiskStatistics
    diagnostics: HABRiskDiagnostics
    input_content_fingerprint: str
    output_content_fingerprint: str
    processing_parameters: dict[str, Any]
    product_id: str
    provenance: DerivedProductRecord

    def __post_init__(self) -> None:
        # Match repository metadata conventions: independent mutable dictionaries,
        # while all scientific scalar/sequence records are frozen canonical tuples.
        object.__setattr__(self, "processing_parameters", deepcopy(self.processing_parameters))
        object.__setattr__(self, "provenance", replace(
            self.provenance, parameters=deepcopy(self.provenance.parameters)
        ))

    def validate(
        self, geometry_scene: HABAnomalyGeometryScene, persistence_scene: HABPersistenceScene,
        *, geometry_scenes: Iterable[HABAnomalyGeometryScene],
        temporal_parents: Mapping[str, TemporalFeatureScene], policy: HABRiskPolicy,
    ) -> None:
        """Regenerate from authoritative typed parents and the supplied frozen policy."""
        from aquasentinel.risk.scoring import validate_scene

        validate_scene(self, geometry_scene, persistence_scene, geometry_scenes=geometry_scenes,
                       temporal_parents=temporal_parents, policy=policy)
