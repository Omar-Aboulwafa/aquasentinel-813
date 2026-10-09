"""Typed temporal arrays, explicit support populations and validated provenance."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from datetime import UTC, datetime
from hashlib import sha256
from typing import Any

import numpy as np
from numpy.typing import NDArray

from aquasentinel.features.spectral import FEATURE_ORDER, FORMULA_DEFINITIONS
from aquasentinel.preprocessing.cache import canonical_json
from aquasentinel.preprocessing.models import AnalysisGrid
from aquasentinel.provenance import DerivedProductRecord


def utc(value: datetime) -> datetime:
    if not isinstance(value, datetime) or value.tzinfo is None or value.utcoffset() is None:
        raise ValueError("Temporal acquisition times and bounds must be timezone-aware datetimes.")
    return value.astimezone(UTC)


def validate_minimum(value: int) -> None:
    if type(value) is not int or not 3 <= value <= np.iinfo(np.uint32).max:
        raise ValueError("minimum_observations must be an integer from 3 through uint32 maximum.")


@dataclass(frozen=True)
class ReferencePeriod:
    start: datetime
    end: datetime

    def to_dict(self) -> dict[str, str]:
        return {"start": utc(self.start).isoformat(), "end": utc(self.end).isoformat()}


@dataclass(frozen=True)
class NumericSummary:
    valid_count: int
    fraction_of_target_feature_support: float | None
    minimum: float | None
    maximum: float | None
    p05: float | None
    median: float | None
    p95: float | None


def summarize(values: np.ndarray, mask: np.ndarray, target_count: int) -> NumericSummary:
    selected = values[mask].astype(np.float64)
    count = int(selected.size)
    fraction = count / target_count if target_count else None
    if not count:
        return NumericSummary(0, fraction, None, None, None, None, None)
    p05, median, p95 = np.percentile(selected, [5, 50, 95], method="linear")
    return NumericSummary(
        count,
        fraction,
        float(selected.min()),
        float(selected.max()),
        float(p05),
        float(median),
        float(p95),
    )


@dataclass(frozen=True)
class TemporalStatistics:
    observation_count: NumericSummary
    centre: NumericSummary
    scale: NumericSummary
    deviation: NumericSummary
    standardized_anomaly: NumericSummary
    empirical_rank: NumericSummary


@dataclass(frozen=True)
class TemporalDiagnostics:
    target_valid_count: int
    insufficient_history_count: int
    baseline_numeric_rejection_count: int
    baseline_eligible_count: int
    zero_MAD_count: int
    anomaly_numeric_rejection_count: int
    valid_anomaly_count: int
    valid_rank_count: int
    above_baseline_count: int
    equal_baseline_count: int
    below_baseline_count: int


@dataclass(frozen=True)
class TemporalFeatureResult:
    target_valid_mask: NDArray[np.bool_]
    baseline_observation_count: NDArray[np.uint32]
    baseline_valid_mask: NDArray[np.bool_]
    baseline_centre: NDArray[np.float64]
    baseline_scale: NDArray[np.float64]
    deviation: NDArray[np.float64]
    anomaly_valid_mask: NDArray[np.bool_]
    robust_standardized_anomaly: NDArray[np.float32]
    rank_valid_mask: NDArray[np.bool_]
    empirical_rank: NDArray[np.float32]
    statistics: TemporalStatistics
    diagnostics: TemporalDiagnostics


def result_statistics(result: TemporalFeatureResult) -> TemporalStatistics:
    count = int(result.target_valid_mask.sum())
    return TemporalStatistics(
        summarize(result.baseline_observation_count, result.target_valid_mask, count),
        summarize(result.baseline_centre, result.baseline_valid_mask, count),
        summarize(result.baseline_scale, result.baseline_valid_mask, count),
        summarize(result.deviation, result.baseline_valid_mask, count),
        summarize(result.robust_standardized_anomaly, result.anomaly_valid_mask, count),
        summarize(result.empirical_rank, result.rank_valid_mask, count),
    )


def result_diagnostics(result: TemporalFeatureResult, minimum: int) -> TemporalDiagnostics:
    target, baseline, anomaly = (
        result.target_valid_mask,
        result.baseline_valid_mask,
        result.anomaly_valid_mask,
    )
    sufficient = target & (result.baseline_observation_count >= minimum)
    zero = baseline & (result.baseline_scale == 0)
    return TemporalDiagnostics(
        int(target.sum()),
        int((target & ~sufficient).sum()),
        int((sufficient & ~baseline).sum()),
        int(baseline.sum()),
        int(zero.sum()),
        int((baseline & ~zero & ~anomaly).sum()),
        int(anomaly.sum()),
        int(result.rank_valid_mask.sum()),
        int((baseline & (result.deviation > 0)).sum()),
        int((baseline & (result.deviation == 0)).sum()),
        int((baseline & (result.deviation < 0)).sum()),
    )


def output_fingerprint(results: dict[str, TemporalFeatureResult], water: np.ndarray) -> str:
    """Integrity evidence outside product identity; canonical invalid NaNs are omitted."""
    digest = sha256()
    for name, result in results.items():
        masks = {
            "target": result.target_valid_mask,
            "baseline": result.baseline_valid_mask,
            "anomaly": result.anomaly_valid_mask,
            "rank": result.rank_valid_mask,
        }
        for key, mask in masks.items():
            digest.update(canonical_json({"feature": name, "mask": key, "shape": mask.shape}))
            digest.update(mask.astype(np.uint8).tobytes(order="C"))
        digest.update(result.baseline_observation_count.astype("<u4").tobytes(order="C"))
        for array, mask, dtype in (
            (result.baseline_centre, masks["baseline"], "<f8"),
            (result.baseline_scale, masks["baseline"], "<f8"),
            (result.deviation, masks["baseline"], "<f8"),
            (result.robust_standardized_anomaly, masks["anomaly"], "<f4"),
            (result.empirical_rank, masks["rank"], "<f4"),
        ):
            digest.update(np.asarray(array[mask], dtype=dtype).tobytes(order="C"))
    digest.update(water.astype(np.uint8).tobytes(order="C"))
    return digest.hexdigest()


@dataclass(frozen=True)
class TemporalFeatureScene:
    grid: AnalysisGrid
    target_product_id: str
    target_acquired_at: datetime
    reference_product_ids: tuple[str, ...]
    reference_acquired_at: tuple[datetime, ...]
    feature_order: tuple[str, ...]
    valid_water_mask: NDArray[np.bool_]
    results: dict[str, TemporalFeatureResult]
    reference_period: ReferencePeriod
    processing_parameters: dict[str, Any]
    product_id: str
    provenance: DerivedProductRecord

    def validate(self) -> None:
        from aquasentinel.temporal.baseline import (
            PROCESSING_VERSION,
            algorithm_policy,
            temporal_product_id,
            validate_descriptors,
        )

        parameters = self.processing_parameters
        canonical_json(parameters)
        identity = parameters["identity"]
        minimum = identity["minimum_observations"]
        validate_minimum(minimum)
        target_time = utc(self.target_acquired_at)
        start, end = utc(self.reference_period.start), utc(self.reference_period.end)
        if not start < end <= target_time:
            raise ValueError("Reference period must end no later than target acquisition.")
        parents = (self.target_product_id, *self.reference_product_ids)
        times = tuple(utc(value) for value in self.reference_acquired_at)
        if (
            len(times) != len(self.reference_product_ids)
            or len(set(parents)) != len(parents)
            or len(set(times)) != len(times)
            or any(not start <= value < end for value in times)
            or tuple(zip(times, self.reference_product_ids))
            != tuple(sorted(zip(times, self.reference_product_ids)))
        ):
            raise ValueError("Reference parents/times must be unique, causal and chronological.")
        if self.feature_order != FEATURE_ORDER or tuple(self.results) != FEATURE_ORDER:
            raise ValueError("Temporal feature order must match AS-103.")
        if self.valid_water_mask.shape != self.grid.shape or self.valid_water_mask.dtype != bool:
            raise ValueError("Target water mask shape/dtype differs from grid.")
        for result in self.results.values():
            self._validate_result(result, minimum, len(times))
        descriptors = identity["compatibility"]
        validate_descriptors(descriptors)
        if (
            identity["processing_version"] != PROCESSING_VERSION
            or identity["target_product_id"] != self.target_product_id
            or identity["target_acquired_at"] != target_time.isoformat()
            or identity["reference_product_ids"] != list(self.reference_product_ids)
            or identity["reference_acquired_at"] != [value.isoformat() for value in times]
            or identity["reference_period"] != self.reference_period.to_dict()
            or canonical_json(identity["grid"]) != canonical_json(self.grid.to_dict())
            or identity["feature_order"] != list(FEATURE_ORDER)
            or identity["formulas"] != FORMULA_DEFINITIONS
            or identity["algorithm"] != algorithm_policy()
            or self.product_id != temporal_product_id(identity)
            or identity["target_water_mask_digest"]
            != sha256(self.valid_water_mask.astype(np.uint8).tobytes(order="C")).hexdigest()
            or parameters["statistics"]
            != {k: asdict(v.statistics) for k, v in self.results.items()}
            or parameters["diagnostics"]
            != {k: asdict(v.diagnostics) for k, v in self.results.items()}
            or parameters["output_content_fingerprint"]
            != output_fingerprint(self.results, self.valid_water_mask)
        ):
            raise ValueError("Temporal scene disagrees with identity/output metadata.")
        if [d["product_id"] for d in descriptors] != list(parents) or [
            d["observation"]["acquired_at"] for d in descriptors
        ] != [target_time.isoformat(), *[value.isoformat() for value in times]]:
            raise ValueError("Temporal compatibility records disagree with immediate parents.")
        fingerprints = identity["input_fingerprints"]
        if (
            fingerprints["format"] != "as104-input-v1"
            or len(fingerprints["references"]) != len(times)
            or any(
                not isinstance(value, str)
                or len(value) != 64
                or any(c not in "0123456789abcdef" for c in value)
                for value in [fingerprints["target"], *fingerprints["references"]]
            )
        ):
            raise ValueError("Temporal input fingerprints are malformed.")
        self.provenance.validate()
        if (
            self.provenance.product_id != self.product_id
            or self.provenance.product_type != "temporal_feature_scene"
            or self.provenance.processing_version != PROCESSING_VERSION
            or self.provenance.source_ids != parents
            or canonical_json(self.provenance.parameters) != canonical_json(parameters)
        ):
            raise ValueError("Temporal provenance must reference immediate AS-103 parents only.")

    def _validate_result(
        self, result: TemporalFeatureResult, minimum: int, references: int
    ) -> None:
        target, baseline, anomaly, rank = (
            result.target_valid_mask,
            result.baseline_valid_mask,
            result.anomaly_valid_mask,
            result.rank_valid_mask,
        )
        for mask in (target, baseline, anomaly, rank):
            if mask.shape != self.grid.shape or mask.dtype != bool:
                raise ValueError("Temporal mask shape/dtype differs from grid.")
        if np.any(target & ~self.valid_water_mask) or any(
            np.any(mask & ~target) for mask in (baseline, anomaly, rank)
        ):
            raise ValueError("Temporal masks expand beyond target feature/water support.")
        counts = result.baseline_observation_count
        if (
            counts.shape != self.grid.shape
            or counts.dtype != np.uint32
            or np.any(counts[~target])
            or np.any(counts > references)
            or np.any(baseline & (counts < minimum))
            or not np.array_equal(rank, baseline)
        ):
            raise ValueError("Temporal counts or baseline/rank support are inconsistent.")
        for array, mask, dtype in (
            (result.baseline_centre, baseline, np.float64),
            (result.baseline_scale, baseline, np.float64),
            (result.deviation, baseline, np.float64),
            (result.robust_standardized_anomaly, anomaly, np.float32),
            (result.empirical_rank, rank, np.float32),
        ):
            if (
                array.shape != self.grid.shape
                or array.dtype != dtype
                or not np.isfinite(array[mask]).all()
                or not np.isnan(array[~mask]).all()
            ):
                raise ValueError("Temporal values require declared dtype, finite support and NaNs.")
        if np.any(result.baseline_scale[baseline] < 0) or np.any(
            (result.empirical_rank[rank] < 0) | (result.empirical_rank[rank] > 1)
        ):
            raise ValueError("Temporal scale/rank is outside its numerical contract.")
        expected_anomaly = np.full(self.grid.shape, np.nan, np.float32)
        positive = baseline & (result.baseline_scale > 0)
        with np.errstate(over="ignore", invalid="ignore", divide="ignore"):
            value = result.deviation[positive] / result.baseline_scale[positive]
            cast = value.astype(np.float32)
        expected_mask = np.zeros(self.grid.shape, bool)
        expected_mask[positive] = np.isfinite(value) & np.isfinite(cast)
        expected_anomaly[positive] = cast
        expected_anomaly[~expected_mask] = np.nan
        if not np.array_equal(anomaly, expected_mask) or not np.array_equal(
            result.robust_standardized_anomaly, expected_anomaly, equal_nan=True
        ):
            raise ValueError("Standardized anomaly disagrees with direct positive-scale division.")
        if result.statistics != result_statistics(result):
            raise ValueError("Temporal statistics disagree with arrays/support.")
        if result.diagnostics != result_diagnostics(result, minimum):
            raise ValueError("Temporal diagnostics disagree with arrays/support.")
        if any(type(value) is not int for value in asdict(result.diagnostics).values()):
            raise ValueError("Temporal diagnostic counts must be integers.")
