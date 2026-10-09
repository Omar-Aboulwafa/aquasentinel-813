"""Pure causal median/MAD comparisons and target-specific semantic identity."""

from __future__ import annotations

import platform
import re
from collections.abc import Iterable
from copy import deepcopy
from dataclasses import asdict, dataclass
from datetime import UTC, datetime
from hashlib import sha256
from typing import Any

import numpy as np

from aquasentinel.features.models import SpectralFeatureScene
from aquasentinel.features.spectral import FEATURE_ORDER, FORMULA_DEFINITIONS
from aquasentinel.preprocessing.cache import canonical_json
from aquasentinel.provenance import DerivedProductRecord, ProvenanceRegistry
from aquasentinel.provenance.serialization import source_record_to_dict
from aquasentinel.temporal.models import (
    ReferencePeriod,
    TemporalDiagnostics,
    TemporalFeatureResult,
    TemporalFeatureScene,
    TemporalStatistics,
    output_fingerprint,
    summarize,
    utc,
    validate_minimum,
)

PROCESSING_VERSION = "as104-v1"
MAD_FACTOR = 1.4826


def algorithm_policy() -> dict[str, Any]:
    return {
        "temporal": "start <= reference < end <= target; strictly prior; target excluded",
        "centre": "median; mean of two middle values for even history",
        "MAD": "median(abs(history - centre))",
        "MAD_factor": MAD_FACTOR,
        "deviation": "target - centre",
        "anomaly": "deviation / scale where scale > 0",
        "zero_scale": "baseline/deviation/rank valid; standardized anomaly masked NaN",
        "positive_scale": "direct float64 division; finite float32 result required",
        "rank": "(count(history < target) + 0.5*count(history == target))/n; exact ties",
        "support": "per-feature valid history at target feature-valid pixels only",
        "count_outside_target": 0,
        "arithmetic_dtype": "float64",
        "output_dtypes": {
            "centre": "float64",
            "scale": "float64",
            "deviation": "float64",
            "anomaly": "float32",
            "rank": "float32",
            "count": "uint32",
            "mask": "bool",
        },
        "statistics": "declared support; float64 linear percentiles [5,50,95]; None if empty",
        "summary_denominator": "target feature-valid pixel count",
        "clip": False,
    }


def temporal_product_id(identity: dict[str, Any]) -> str:
    return "temporal:" + sha256(canonical_json(identity)).hexdigest()


def _descriptor(scene: SpectralFeatureScene, registry: ProvenanceRegistry) -> dict[str, Any]:
    """Resolve structured upstream metadata without fetching or changing the registry."""
    try:
        registered = registry.get_derived_product(scene.product_id)
        registered.validate()
        if (
            registered.product_id != scene.product_id
            or registered.product_type != scene.provenance.product_type
            or registered.processing_version != scene.provenance.processing_version
            or registered.source_ids != (scene.parent_product_id,)
            or canonical_json(registered.parameters) != canonical_json(scene.processing_parameters)
        ):
            raise ValueError
        parent = registry.get_derived_product(scene.parent_product_id)
        parent.validate()
        identity = parent.parameters["identity"]
        if (
            parent.product_id != scene.parent_product_id
            or parent.product_type != "preprocessed_optical_scene"
            or parent.processing_version != identity["processing_version"]
            or parent.processing_version
            != scene.processing_parameters["identity"]["parent_processing_version"]
            or parent.product_id != "optical:" + sha256(canonical_json(identity)).hexdigest()
            or len(parent.source_ids) != 1
            or canonical_json(identity["target_grid"]) != canonical_json(scene.grid.to_dict())
        ):
            raise ValueError
        source = registry.get_source(parent.source_ids[0])
        source.validate()
        if canonical_json(source_record_to_dict(source)) != canonical_json(identity["pc_source"]):
            raise ValueError
        observation = deepcopy(identity["observation_match"])
        observation["acquired_at"] = utc(
            datetime.fromisoformat(observation["acquired_at"])
        ).isoformat()
        if (
            observation["acquired_at"] != utc(scene.acquired_at).isoformat()
            or utc(source.acquired_at) != utc(scene.acquired_at)
            or observation["platform"].casefold() != source.platform.casefold()
        ):
            raise ValueError
        descriptor = {
            "product_id": scene.product_id,
            "parent_product_id": parent.product_id,
            "pc_source_id": source.source_id,
            "pc_product_id": source.product_id,
            "observation": observation,
            "pc_processing_baseline": identity["pc_processing_baseline"],
            "pc_generation_time": utc(
                datetime.fromisoformat(identity["pc_generation_time"])
            ).isoformat(),
            "contract": {
                "as103_version": registered.processing_version,
                "as102_version": parent.processing_version,
                "catalog": source.catalog,
                "collection": source.collection,
                **{
                    key: deepcopy(identity[key])
                    for key in (
                        "aoi_geometry_digest",
                        "bands",
                        "resampling",
                        "mask_policy",
                        "interpolation_support_policy",
                        "decoding",
                    )
                },
            },
        }
        validate_descriptors([descriptor])
        return descriptor
    except (KeyError, TypeError, AttributeError, ValueError):
        raise ValueError(
            "Selected scene has unresolved or inconsistent upstream provenance."
        ) from None


def validate_descriptors(descriptors: list[dict[str, Any]]) -> None:
    if not descriptors:
        raise ValueError("Target compatibility metadata is required.")
    keys = set()
    common = None
    for descriptor in descriptors:
        observation, contract = descriptor["observation"], descriptor["contract"]
        time = utc(datetime.fromisoformat(observation["acquired_at"]))
        tile, orbit, satellite = (
            observation["mgrs_tile"],
            observation["relative_orbit"],
            observation["platform"],
        )
        baseline = descriptor["pc_processing_baseline"]
        decoding = contract["decoding"]
        if (
            not re.fullmatch(r"spectral:[a-f0-9]{64}", descriptor["product_id"])
            or not re.fullmatch(r"optical:[a-f0-9]{64}", descriptor["parent_product_id"])
            or satellite not in {"sentinel-2a", "sentinel-2b"}
            or not re.fullmatch(r"\d{2}[C-HJ-NP-X][A-HJ-NP-Z]{2}", tile)
            or not 1 <= int(tile[:2]) <= 60
            or type(orbit) is not int
            or not 1 <= orbit <= 143
            or not re.fullmatch(r"\d{2}\.\d{2}", baseline)
            or decoding["processing_baseline"] != baseline
            or not isinstance(decoding["quantification"], (int, float))
            or isinstance(decoding["quantification"], bool)
            or not np.isfinite(decoding["quantification"])
            or decoding["quantification"] <= 0
            or contract["as103_version"] != "as103-v1"
            or not contract["as102_version"].strip()
            or not descriptor["pc_source_id"].strip()
            or not descriptor["pc_product_id"].strip()
        ):
            raise ValueError("Malformed temporal observation/processing compatibility metadata.")
        utc(datetime.fromisoformat(descriptor["pc_generation_time"]))
        for band in ("B02", "B03", "B04", "B05", "B06"):
            if not np.isfinite(decoding["offsets"][band]) or not decoding["band_ids"][band]:
                raise ValueError("Incomplete BOA decoding contract.")
        key = (time, satellite, tile, orbit)
        if key in keys:
            raise ValueError("Multiple processing products represent the same observation.")
        keys.add(key)
        comparable = canonical_json(
            {"contract": contract, "tile": tile, "orbit": orbit, "pc_processing_baseline": baseline}
        )
        if common is not None and common != comparable:
            raise ValueError("Selected scenes have incompatible processing/tile/orbit contracts.")
        common = comparable


@dataclass(frozen=True)
class _Snapshot:
    masks: dict[str, np.ndarray]
    values: dict[str, np.ndarray]
    water: np.ndarray | None


def _snapshot(scene: SpectralFeatureScene, target_masks: dict[str, np.ndarray] | None) -> _Snapshot:
    if target_masks is None:
        masks = {name: scene.feature_valid_masks[name].copy() for name in FEATURE_ORDER}
        values = {name: scene.features[name][masks[name]].copy() for name in FEATURE_ORDER}
        return _Snapshot(masks, values, scene.valid_water_mask.copy())
    masks, values = {}, {}
    for name in FEATURE_ORDER:
        # Only target-supported locations participate, including reference validity there.
        masks[name] = scene.feature_valid_masks[name][target_masks[name]].copy()
        values[name] = scene.features[name][target_masks[name]][masks[name]].copy()
    return _Snapshot(masks, values, None)


def _input_fingerprint(snapshot: _Snapshot, shape: tuple[int, int]) -> str:
    digest = sha256()

    def segment(header: dict[str, Any], payload: bytes) -> None:
        encoded = canonical_json({**header, "byte_count": len(payload)})
        digest.update(len(encoded).to_bytes(8, "big"))
        digest.update(encoded)
        digest.update(payload)

    segment(
        {
            "format": "as104-input-v1",
            "shape": list(shape),
            "feature_order": list(FEATURE_ORDER),
            "role": "target" if snapshot.water is not None else "reference",
            "order": "C",
        },
        b"",
    )
    if snapshot.water is not None:
        segment(
            {"mask": "valid_water", "dtype": "uint8", "count": snapshot.water.size},
            snapshot.water.astype(np.uint8).tobytes(order="C"),
        )
    for name in FEATURE_ORDER:
        mask, values = snapshot.masks[name], snapshot.values[name]
        if not np.isfinite(values).all():
            raise ValueError("Consumed temporal feature values must be finite.")
        segment(
            {
                "feature": name,
                "mask_shape": list(mask.shape),
                "dtype": "uint8",
                "count": int(mask.size),
            },
            mask.astype(np.uint8).tobytes(order="C"),
        )
        segment(
            {"feature": name, "dtype": "<f4", "count": int(values.size)},
            np.asarray(values, dtype="<f4").tobytes(order="C"),
        )
    return digest.hexdigest()


def _reduce_feature(
    name: str, target: _Snapshot, references: list[_Snapshot], minimum: int
) -> TemporalFeatureResult:
    mask = target.masks[name]
    pixels = int(mask.sum())
    history = np.full((len(references), pixels), np.nan, np.float64)
    for row, reference in enumerate(references):
        history[row, reference.masks[name]] = reference.values[name]
    counts = np.isfinite(history).sum(axis=0).astype(np.uint32)
    eligible = counts >= minimum
    centre, scale, deviation = (np.full(pixels, np.nan, np.float64) for _ in range(3))
    rank = np.full(pixels, np.nan, np.float32)
    if eligible.any():
        selected = history[:, eligible]
        centre[eligible] = np.nanmedian(selected, axis=0)
        scale[eligible] = MAD_FACTOR * np.nanmedian(np.abs(selected - centre[eligible]), axis=0)
        values = target.values[name][eligible].astype(np.float64)
        deviation[eligible] = values - centre[eligible]
        rank[eligible] = (
            ((selected < values).sum(axis=0) + 0.5 * (selected == values).sum(axis=0))
            / counts[eligible]
        ).astype(np.float32)
    baseline = eligible & np.isfinite(centre) & np.isfinite(scale) & np.isfinite(deviation)
    for array in (centre, scale, deviation, rank):
        array[~baseline] = np.nan
    positive = baseline & (scale > 0)
    anomaly = np.full(pixels, np.nan, np.float32)
    with np.errstate(over="ignore", invalid="ignore", divide="ignore"):
        standardized = deviation[positive] / scale[positive]
        anomaly[positive] = standardized.astype(np.float32)
    anomaly_valid = positive & np.isfinite(anomaly)
    anomaly[~anomaly_valid] = np.nan

    def raster(values: np.ndarray, *, outside: float | bool) -> np.ndarray:
        result = np.full(mask.shape, outside, dtype=values.dtype)
        result[mask] = values
        return result

    zero = baseline & (scale == 0)
    statistics = TemporalStatistics(
        summarize(counts, np.ones(pixels, bool), pixels),
        summarize(centre, baseline, pixels),
        summarize(scale, baseline, pixels),
        summarize(deviation, baseline, pixels),
        summarize(anomaly, anomaly_valid, pixels),
        summarize(rank, baseline, pixels),
    )
    diagnostics = TemporalDiagnostics(
        pixels,
        int((~eligible).sum()),
        int((eligible & ~baseline).sum()),
        int(baseline.sum()),
        int(zero.sum()),
        int((positive & ~anomaly_valid).sum()),
        int(anomaly_valid.sum()),
        int(baseline.sum()),
        int((baseline & (deviation > 0)).sum()),
        int((baseline & (deviation == 0)).sum()),
        int((baseline & (deviation < 0)).sum()),
    )
    return TemporalFeatureResult(
        mask.copy(),
        raster(counts, outside=0),
        raster(baseline, outside=False),
        raster(centre, outside=np.nan),
        raster(scale, outside=np.nan),
        raster(deviation, outside=np.nan),
        raster(anomaly_valid, outside=False),
        raster(anomaly, outside=np.nan),
        raster(baseline.copy(), outside=False),
        raster(rank, outside=np.nan),
        statistics,
        diagnostics,
    )


def compute_temporal_anomaly(
    scenes: Iterable[SpectralFeatureScene],
    *,
    target_product_id: str,
    reference_start: datetime,
    reference_end: datetime | None = None,
    minimum_observations: int,
    registry: ProvenanceRegistry,
) -> TemporalFeatureScene:
    """Select strictly-prior history; compare each feature without IO or registry mutation."""
    validate_minimum(minimum_observations)
    start = utc(reference_start)
    by_id, seen_times = {}, set()
    for scene in scenes:
        if not isinstance(scene, SpectralFeatureScene):
            raise TypeError("Temporal inputs must be AS-103 SpectralFeatureScene objects.")
        scene.validate()
        time = utc(scene.acquired_at)
        if scene.product_id in by_id or time in seen_times:
            raise ValueError("Duplicate product ID or normalized acquisition time.")
        by_id[scene.product_id] = scene
        seen_times.add(time)
    if target_product_id not in by_id:
        raise ValueError("Target product is missing from the temporal collection.")
    target = by_id[target_product_id]
    target_time = utc(target.acquired_at)
    end = target_time if reference_end is None else utc(reference_end)
    if not start < end <= target_time:
        raise ValueError("Reference bounds must satisfy start < end <= target acquisition.")
    references = sorted(
        (
            scene
            for scene in by_id.values()
            if scene.product_id != target_product_id and start <= utc(scene.acquired_at) < end
        ),
        key=lambda scene: (utc(scene.acquired_at), scene.product_id),
    )
    if len(references) > np.iinfo(np.uint32).max:
        raise ValueError("Reference collection exceeds uint32 observation-count capacity.")
    selected = [target, *references]
    if any(scene.grid != target.grid for scene in selected):
        raise ValueError("Selected scenes must have identical AnalysisGrid values.")
    descriptors = [_descriptor(scene, registry) for scene in selected]
    validate_descriptors(descriptors)
    snapshot = _snapshot(target, None)
    snapshots = [_snapshot(scene, snapshot.masks) for scene in references]
    identity = {
        "processing_version": PROCESSING_VERSION,
        "target_product_id": target.product_id,
        "target_acquired_at": target_time.isoformat(),
        "reference_product_ids": [scene.product_id for scene in references],
        "reference_acquired_at": [utc(scene.acquired_at).isoformat() for scene in references],
        "reference_period": ReferencePeriod(start, end).to_dict(),
        "minimum_observations": minimum_observations,
        "grid": target.grid.to_dict(),
        "feature_order": list(FEATURE_ORDER),
        "formulas": deepcopy(FORMULA_DEFINITIONS),
        "compatibility": descriptors,
        "algorithm": algorithm_policy(),
        "input_fingerprints": {
            "format": "as104-input-v1",
            "target": _input_fingerprint(snapshot, target.grid.shape),
            "references": [_input_fingerprint(s, target.grid.shape) for s in snapshots],
        },
        "target_water_mask_digest": sha256(
            snapshot.water.astype(np.uint8).tobytes(order="C")
        ).hexdigest(),
        "software_versions": {"python": platform.python_version(), "numpy": np.__version__},
    }
    results = {
        name: _reduce_feature(name, snapshot, snapshots, minimum_observations)
        for name in FEATURE_ORDER
    }
    parameters = {
        "identity": identity,
        "statistics": {k: asdict(v.statistics) for k, v in results.items()},
        "diagnostics": {k: asdict(v.diagnostics) for k, v in results.items()},
        "output_content_fingerprint": output_fingerprint(results, snapshot.water),
        "scientific_limit": "Candidate temporal BOA signals only; not HAB or operational evidence.",
    }
    product_id = temporal_product_id(identity)
    parents = (target.product_id, *(scene.product_id for scene in references))
    provenance = DerivedProductRecord(
        product_id,
        "temporal_feature_scene",
        datetime.now(UTC),
        PROCESSING_VERSION,
        parents,
        parameters,
    )
    result = TemporalFeatureScene(
        target.grid,
        target.product_id,
        target_time,
        parents[1:],
        tuple(utc(scene.acquired_at) for scene in references),
        FEATURE_ORDER,
        snapshot.water,
        results,
        ReferencePeriod(start, end),
        parameters,
        product_id,
        provenance,
    )
    result.validate()
    return result
