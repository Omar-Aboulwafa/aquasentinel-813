"""Typed feature arrays, support, summaries and immediate-parent lineage."""

from __future__ import annotations

import re
from dataclasses import asdict, dataclass
from datetime import UTC, datetime
from hashlib import sha256
from typing import Any

import numpy as np
from numpy.typing import NDArray

from aquasentinel.preprocessing.cache import canonical_json
from aquasentinel.preprocessing.models import AnalysisGrid
from aquasentinel.provenance import DerivedProductRecord


@dataclass(frozen=True)
class FeatureStatistics:
    valid_count: int
    valid_fraction_of_parent_water: float | None
    minimum: float | None
    maximum: float | None
    p05: float | None
    median: float | None
    p95: float | None


@dataclass(frozen=True)
class FeatureDiagnostics:
    parent_valid_water_count: int
    negative_required_input_count: int
    denominator_rejection_count: int
    negative_denominator_count: int
    nonfinite_result_rejection_count: int
    out_of_nominal_range_count: int | None


def feature_statistics(
    values: np.ndarray, mask: np.ndarray, parent_count: int
) -> FeatureStatistics:
    selected = values[mask].astype(np.float64)
    count = int(selected.size)
    fraction = count / parent_count if parent_count else None
    if not count:
        return FeatureStatistics(0, fraction, None, None, None, None, None)
    p05, median, p95 = np.percentile(selected, [5, 50, 95], method="linear")
    return FeatureStatistics(
        count,
        fraction,
        float(selected.min()),
        float(selected.max()),
        float(p05),
        float(median),
        float(p95),
    )


@dataclass(frozen=True)
class SpectralFeatureScene:
    grid: AnalysisGrid
    parent_product_id: str
    acquired_at: datetime
    feature_order: tuple[str, ...]
    features: dict[str, NDArray[np.float32]]
    feature_valid_masks: dict[str, NDArray[np.bool_]]
    valid_water_mask: NDArray[np.bool_]
    statistics: dict[str, FeatureStatistics]
    diagnostics: dict[str, FeatureDiagnostics]
    processing_parameters: dict[str, Any]
    product_id: str
    provenance: DerivedProductRecord

    def validate(self) -> None:
        from aquasentinel.features.spectral import (
            FEATURE_ORDER,
            FORMULA_DEFINITIONS,
            PROCESSING_VERSION,
            STATISTICS_POLICY,
            SUPPORT_POLICY,
            feature_product_id,
            numerical_policy,
        )

        if self.feature_order != FEATURE_ORDER or any(
            tuple(mapping) != FEATURE_ORDER
            for mapping in (
                self.features,
                self.feature_valid_masks,
                self.statistics,
                self.diagnostics,
            )
        ):
            raise ValueError("Feature keys/order must match the canonical six-feature contract.")
        if self.acquired_at.tzinfo is None or self.acquired_at.utcoffset() is None:
            raise ValueError("Acquisition time must be timezone-aware.")
        if self.valid_water_mask.shape != self.grid.shape or self.valid_water_mask.dtype != bool:
            raise ValueError("Parent water mask shape/dtype differs from the analysis grid.")
        parent_count = int(np.count_nonzero(self.valid_water_mask))
        for name in FEATURE_ORDER:
            values, mask = self.features[name], self.feature_valid_masks[name]
            if values.shape != self.grid.shape or values.dtype != np.float32:
                raise ValueError("Feature shape/dtype differs from the analysis grid.")
            if mask.shape != self.grid.shape or mask.dtype != bool:
                raise ValueError("Feature mask shape/dtype differs from the analysis grid.")
            if np.any(mask & ~self.valid_water_mask):
                raise ValueError("Feature support expands beyond parent valid-water support.")
            if not np.isfinite(values[mask]).all() or not np.isnan(values[~mask]).all():
                raise ValueError("Feature values must be finite on support and NaN elsewhere.")
            if self.statistics[name] != feature_statistics(values, mask, parent_count):
                raise ValueError("Feature statistics disagree with arrays/support.")
            diagnostics = self.diagnostics[name]
            counts = asdict(diagnostics)
            if diagnostics.parent_valid_water_count != parent_count or any(
                (type(value) is not int or not 0 <= value <= parent_count)
                for key, value in counts.items()
                if key != "out_of_nominal_range_count"
            ):
                raise ValueError("Feature diagnostic counts are invalid.")
            if (
                self.statistics[name].valid_count
                + diagnostics.denominator_rejection_count
                + (diagnostics.nonfinite_result_rejection_count)
                != parent_count
            ):
                raise ValueError("Feature exclusions do not reconcile with parent water.")
            if name == "mci_like" and (
                diagnostics.denominator_rejection_count or diagnostics.negative_denominator_count
            ):
                raise ValueError("Line height has no denominator diagnostics.")
            outside = int(np.count_nonzero(mask & ((values < -1) | (values > 1))))
            expected_outside = outside if name == "ndci_like" else None
            if diagnostics.out_of_nominal_range_count != expected_outside or (
                expected_outside is not None
                and type(diagnostics.out_of_nominal_range_count) is not int
            ):
                raise ValueError("Nominal-range diagnostics disagree with feature values.")
        parameters = self.processing_parameters
        canonical_json(parameters)  # Finite JSON only; no arrays or credentialled URLs.
        identity = parameters["identity"]
        if (
            identity["parent_product_id"] != self.parent_product_id
            or not re.fullmatch(r"optical:[a-f0-9]{64}", self.parent_product_id)
            or identity["processing_version"] != PROCESSING_VERSION
            or identity["feature_order"] != list(FEATURE_ORDER)
            or identity["acquired_at"] != self.acquired_at.astimezone(UTC).isoformat()
            or canonical_json(identity["grid"]) != canonical_json(self.grid.to_dict())
            or identity["formulas"] != FORMULA_DEFINITIONS
            or identity["numerical_policy"] != numerical_policy()
            or identity["input_support_policy"] != SUPPORT_POLICY
            or identity["statistics_policy"] != STATISTICS_POLICY
            or identity["arithmetic_dtype"] != "float64"
            or identity["output_dtype"] != "float32"
            or not identity["parent_processing_version"].strip()
            or not re.fullmatch(r"[a-f0-9]{64}", identity["input_content_fingerprint"])
            or identity["parent_water_mask_digest"]
            != sha256(self.valid_water_mask.astype(np.uint8).tobytes(order="C")).hexdigest()
            or self.product_id != feature_product_id(identity)
            or parameters["statistics"] != {k: asdict(v) for k, v in self.statistics.items()}
            or parameters["diagnostics"] != {k: asdict(v) for k, v in self.diagnostics.items()}
        ):
            raise ValueError("Typed feature model disagrees with processing identity/metadata.")
        self.provenance.validate()
        if (
            self.provenance.product_id != self.product_id
            or self.provenance.product_type != "spectral_feature_scene"
            or self.provenance.processing_version != identity["processing_version"]
            or self.provenance.source_ids != (self.parent_product_id,)
            or canonical_json(self.provenance.parameters) != canonical_json(parameters)
        ):
            raise ValueError("Feature provenance must reference only its immediate AS-102 parent.")
