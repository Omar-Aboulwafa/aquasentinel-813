"""Typed observation-recurrence evidence; no biological or risk interpretation."""

from __future__ import annotations

from collections.abc import Iterable, Mapping
from dataclasses import dataclass
from datetime import datetime
from typing import Any

import numpy as np
from numpy.typing import NDArray

from aquasentinel.geometry.models import HABAnomalyGeometryScene
from aquasentinel.preprocessing.models import AnalysisGrid
from aquasentinel.provenance import DerivedProductRecord
from aquasentinel.temporal.models import TemporalFeatureScene


@dataclass(frozen=True)
class ExactMicroseconds:
    """Exact integer or half-microsecond median; never a truncated duration."""

    numerator_microseconds: int
    denominator: int


@dataclass(frozen=True)
class PriorRegionEvidence:
    geometry_product_id: str
    acquired_at: datetime
    supported_target_region_pixel_count: int
    candidate_overlap_pixel_count: int
    candidate_overlap_fraction_of_supported: float | None


@dataclass(frozen=True)
class PersistenceRegionSummary:
    region_id: str
    component_label: int
    target_pixel_count: int
    persistence_evaluable_target_candidate_count: int
    candidate_history_coverage: float | None
    recurrent_candidate_count: int
    recurrence_fraction: float | None
    maximum_streak_count: int | None
    median_streak_count: float | None
    maximum_current_streak_span_us: int | None
    median_current_streak_span_us: ExactMicroseconds | None
    prior_observations: tuple[PriorRegionEvidence, ...]


@dataclass(frozen=True)
class PersistenceStatistics:
    target_policy_support_count: int
    persistence_evaluable_pixel_count: int
    target_candidate_count: int
    persistence_evaluable_target_candidate_count: int
    recurrent_candidate_count: int
    target_candidates_without_prior_history: int
    candidate_history_coverage: float | None
    recurrence_fraction: float | None
    streak_histogram_on_target_candidates: dict[str, int]


@dataclass(frozen=True)
class HABPersistenceScene:
    grid: AnalysisGrid
    parent_geometry_product_ids: tuple[str, ...]
    acquired_at: tuple[datetime, ...]
    target_geometry_product_id: str
    target_acquired_at: datetime
    target_candidate_analysis_support_mask: NDArray[np.bool_]
    target_candidate_mask: NDArray[np.bool_]
    target_component_labels: NDArray[np.int32]
    prior_valid_observation_count: NDArray[np.uint32]
    persistence_evaluable_mask: NDArray[np.bool_]
    current_streak_count: NDArray[np.uint32]
    recurrent_candidate_mask: NDArray[np.bool_]
    previous_valid_observation_gap_us: NDArray[np.int64]
    current_streak_span_us: NDArray[np.int64]
    regions: tuple[PersistenceRegionSummary, ...]
    statistics: PersistenceStatistics
    processing_parameters: dict[str, Any]
    product_id: str
    provenance: DerivedProductRecord

    def validate(
        self,
        geometry_scenes: Iterable[HABAnomalyGeometryScene],
        *,
        temporal_parents: Mapping[str, TemporalFeatureScene],
    ) -> None:
        """Regenerate science from fully validated immediate parents, not stored hashes."""
        from aquasentinel.persistence.recurrence import validate_scene

        validate_scene(self, geometry_scenes, temporal_parents=temporal_parents)
