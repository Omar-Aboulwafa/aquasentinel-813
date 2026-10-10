"""Typed, auditable candidate geometry with parent-aware integrity validation."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any

import numpy as np
from numpy.typing import NDArray

from aquasentinel.preprocessing.models import AnalysisGrid
from aquasentinel.provenance import DerivedProductRecord
from aquasentinel.temporal.models import TemporalFeatureScene


@dataclass(frozen=True)
class DescriptiveSummary:
    count: int
    minimum: float | None
    median: float | None
    maximum: float | None


@dataclass(frozen=True)
class RegionFeatureSummary:
    deviation: DescriptiveSummary
    empirical_rank: DescriptiveSummary


@dataclass(frozen=True)
class HABAnomalyRegion:
    region_id: str
    component_label: int
    first_pixel_row: int
    first_pixel_col: int
    geometry: dict[str, Any]
    pixel_count: int
    area_m2: float
    area_km2: float
    bbox_projected: tuple[float, float, float, float]
    participating_families: tuple[str, ...]
    family_evidence_pixel_counts: dict[str, int]
    maximum_family_votes: int
    median_family_votes: float
    feature_summaries: dict[str, RegionFeatureSummary]


@dataclass(frozen=True)
class FeatureEvidenceDiagnostics:
    eligible_count: int
    positive_deviation_count: int
    threshold_rank_count: int
    evidence_count: int
    evidence_fraction_of_feature_support: float | None


@dataclass(frozen=True)
class FamilyEvidenceDiagnostics:
    available_count: int
    evidence_count: int
    evidence_fraction_of_family_support: float | None


@dataclass(frozen=True)
class GeometryDiagnostics:
    features: dict[str, FeatureEvidenceDiagnostics]
    families: dict[str, FamilyEvidenceDiagnostics]


@dataclass(frozen=True)
class GeometryStatistics:
    candidate_analysis_support_count: int
    candidate_pixel_count: int
    candidate_fraction_of_policy_support: float | None
    pixel_area_m2: float
    total_candidate_area_m2: float
    total_candidate_area_km2: float
    region_count: int
    one_pixel_region_count: int
    largest_region_pixels: int | None
    median_region_pixels: float | None
    largest_region_area_m2: float | None
    median_region_area_m2: float | None
    region_size_histogram: dict[str, int]
    family_vote_histogram_on_policy_support: dict[str, int]
    family_vote_histogram_on_candidates: dict[str, int]


@dataclass(frozen=True)
class HABAnomalyGeometryScene:
    grid: AnalysisGrid
    parent_temporal_product_id: str
    target_acquired_at: datetime
    feature_support_masks: dict[str, NDArray[np.bool_]]
    feature_evidence_masks: dict[str, NDArray[np.bool_]]
    family_available_masks: dict[str, NDArray[np.bool_]]
    family_evidence_masks: dict[str, NDArray[np.bool_]]
    candidate_analysis_support_mask: NDArray[np.bool_]
    available_family_count: NDArray[np.uint8]
    family_vote_count: NDArray[np.uint8]
    candidate_mask: NDArray[np.bool_]
    component_labels: NDArray[np.int32]
    regions: tuple[HABAnomalyRegion, ...]
    statistics: GeometryStatistics
    diagnostics: GeometryDiagnostics
    processing_parameters: dict[str, Any]
    product_id: str
    provenance: DerivedProductRecord

    def validate(self, parent: TemporalFeatureScene) -> None:
        """Regenerate all scientific content and lineage from the immediate parent."""
        from aquasentinel.geometry.hab import validate_scene

        validate_scene(self, parent)
