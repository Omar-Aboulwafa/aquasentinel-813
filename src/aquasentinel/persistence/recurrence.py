"""Pure Decision 051 recurrence, canonical fingerprints and parent-aware integrity."""

from __future__ import annotations

import platform
from collections.abc import Iterable, Mapping
from copy import deepcopy
from dataclasses import asdict
from datetime import UTC, datetime
from hashlib import sha256
from typing import Any

import numpy as np

from aquasentinel.geometry.hab import PROCESSING_VERSION as GEOMETRY_VERSION
from aquasentinel.geometry.hab import algorithm_policy as geometry_policy
from aquasentinel.geometry.models import HABAnomalyGeometryScene
from aquasentinel.persistence.models import (
    ExactMicroseconds,
    HABPersistenceScene,
    PersistenceRegionSummary,
    PersistenceStatistics,
    PriorRegionEvidence,
)
from aquasentinel.preprocessing.cache import canonical_json
from aquasentinel.provenance import DerivedProductRecord
from aquasentinel.temporal.models import TemporalFeatureScene, utc

PROCESSING_VERSION = "as106-v1"
INPUT_FORMAT = "as106-input-v1"
OUTPUT_FORMAT = "as106-output-v1"
SCIENTIFIC_LIMIT = (
    "Observed candidate recurrence only, not continuous biological persistence, HAB confirmation, "
    "bloom duration, accuracy, risk, confidence, water safety or warning lead time. "
    "Shared reference histories are not independent confirmation."
)
ARRAY_DTYPES = {
    "target_candidate_analysis_support_mask": "uint8",
    "target_candidate_mask": "uint8",
    "target_component_labels": "<i4",
    "prior_valid_observation_count": "<u4",
    "persistence_evaluable_mask": "uint8",
    "current_streak_count": "<u4",
    "recurrent_candidate_mask": "uint8",
    "previous_valid_observation_gap_us": "<i8",
    "current_streak_span_us": "<i8",
}


def algorithm_policy() -> dict[str, Any]:
    return {
        "recurrence_minimum_streak": 2,
        "unsupported_observation": "UNKNOWN; skip without increment or break",
        "supported_noncandidate": "break current streak",
        "spatial": "exact same-grid pixel only; no motion/morphology/resampling",
        "calendar_gap_cutoff": None,
        "prior_count": "all earlier P=true at target P; zero outside target P",
        "Q": "target P AND prior_valid_observation_count >= 1",
        "A": "target candidate pixels",
        "B": "target C AND Q",
        "C": "target C AND current_streak_count >= 2",
        "candidate_history_coverage": "count(B)/count(A); None for empty A",
        "recurrence_fraction": "count(C)/count(B); None for empty B",
        "streak_histogram_denominator": "A; exact observed integer streaks in ascending order",
        "regional_streak_support": "B",
        "regional_span_support": "recurrent candidate pixels",
        "timing": "exact UTC microseconds; int64; missing -1; singleton span 0",
        "median_span": "exact numerator_microseconds / denominator (1 or 2)",
        "counts": "uint32; capacity checked before arithmetic",
        "masks": "bool",
        "target_labels": "int32; authoritative AS-105 labels/region IDs unchanged",
        "region_overlap": "target region AND prior P AND prior C; denominator prior support",
    }


def validate_count_capacity(value: int) -> None:
    """Also applied to total scene count, because a candidate streak includes target."""
    if type(value) is not int or not 0 <= value <= np.iinfo(np.uint32).max:
        raise ValueError("Observation count exceeds uint32 capacity or is not an integer.")


def validate_gap_us(value: int) -> int:
    if type(value) is not int or not 0 <= value <= np.iinfo(np.int64).max:
        raise ValueError("Observation interval exceeds int64 microsecond capacity.")
    return value


def gap_us(later: datetime, earlier: datetime) -> int:
    delta = utc(later) - utc(earlier)
    return validate_gap_us((delta.days * 86400 + delta.seconds) * 1000000 + delta.microseconds)


def comparison_contract(parent: TemporalFeatureScene) -> dict[str, Any]:
    """Structured common fields only; exclude target IDs/time/generation and pixel content.

    The caller first invokes the whole AS-105 parent-aware validator, including
    AS-104 descriptor validation. Both satellite platforms may occur in a sequence.
    """
    identity = parent.processing_parameters["identity"]
    descriptor = identity["compatibility"][0]
    return deepcopy({
        **{k: identity[k] for k in (
            "processing_version", "feature_order", "formulas", "reference_product_ids",
            "reference_acquired_at", "reference_period", "minimum_observations", "grid", "algorithm",
        )},
        "upstream_contract": descriptor["contract"],
        "mgrs_tile": descriptor["observation"]["mgrs_tile"],
        "relative_orbit": descriptor["observation"]["relative_orbit"],
        "pc_processing_baseline": descriptor["pc_processing_baseline"],
    })


def _sequence(
    geometry_scenes: Iterable[HABAnomalyGeometryScene],
    temporal_parents: Mapping[str, TemporalFeatureScene],
    target_id: str,
) -> tuple[tuple[HABAnomalyGeometryScene, ...], dict[str, Any]]:
    if not isinstance(temporal_parents, Mapping):
        raise TypeError("Temporal witnesses must be a mapping keyed by product ID.")
    if not isinstance(target_id, str) or not target_id.strip():
        raise ValueError("An explicit target geometry product ID is required.")
    scenes, ids, times = [], set(), set()
    for scene in geometry_scenes:
        validate_count_capacity(len(scenes) + 1)
        if not isinstance(scene, HABAnomalyGeometryScene):
            raise TypeError("Persistence inputs must be AS-105 HABAnomalyGeometryScene objects.")
        time = utc(scene.target_acquired_at)
        if scene.product_id in ids or time in times:
            raise ValueError("Duplicate geometry product ID or normalized acquisition timestamp.")
        ids.add(scene.product_id)
        times.add(time)
        scenes.append(scene)
    if not scenes or target_id not in ids:
        raise ValueError("A nonempty sequence containing the explicit target is required.")
    scenes.sort(key=lambda s: utc(s.target_acquired_at))
    if scenes[-1].product_id != target_id:
        raise ValueError("Target must be latest; future observations are forbidden.")
    common = None
    for scene in scenes:
        parent = temporal_parents.get(scene.parent_temporal_product_id)
        if parent is None:
            raise ValueError("A typed immediate temporal integrity witness is required.")
        if not isinstance(parent, TemporalFeatureScene):
            raise TypeError("Temporal integrity witnesses must be TemporalFeatureScene objects.")
        if parent.product_id != scene.parent_temporal_product_id:
            raise ValueError("Temporal witness product ID must match the immediate parent exactly.")
        # Owner-approved internal AS-105 regeneration: integrity, not new extraction.
        scene.validate(parent)
        if (
            scene.grid != scenes[-1].grid
            or scene.provenance.processing_version != GEOMETRY_VERSION
            or canonical_json(scene.processing_parameters["identity"]["policy"])
            != canonical_json(geometry_policy())
        ):
            raise ValueError("Persistence requires identical grids and the frozen AS-105 contract.")
        contract = comparison_contract(parent)
        if common is not None and canonical_json(common) != canonical_json(contract):
            raise ValueError("Temporal comparison contexts are incompatible across observations.")
        common = contract
    return tuple(scenes), common


def _segment(digest, header: dict, payload: bytes = b"") -> None:
    encoded = canonical_json({**header, "byte_count": len(payload)})
    digest.update(len(encoded).to_bytes(8, "big"))
    digest.update(encoded)
    digest.update(payload)


def input_content_fingerprint(scenes: Iterable[HABAnomalyGeometryScene]) -> str:
    """Canonical consumed science only; whole-parent validation belongs at the API boundary."""
    ordered = sorted(scenes, key=lambda s: utc(s.target_acquired_at))
    if not ordered:
        raise ValueError("Fingerprint requires at least a target observation.")
    target = ordered[-1]
    p, c = target.candidate_analysis_support_mask, target.candidate_mask
    digest = sha256()
    _segment(digest, {"format": INPUT_FORMAT, "grid": target.grid.to_dict()})
    for index, scene in enumerate(ordered):
        _segment(digest, {"observation": index, "acquired_at": utc(scene.target_acquired_at).isoformat()})
        is_target = scene is target
        prior_p = scene.candidate_analysis_support_mask
        selections = (
            ("P", prior_p if is_target else prior_p[p], "uint8"),
            ("C", scene.candidate_mask if is_target else scene.candidate_mask[c & prior_p], "uint8"),
        )
        for name, values, dtype in selections:
            _segment(digest, {"field": name, "dtype": dtype, "shape": values.shape},
                     np.asarray(values, dtype=dtype).tobytes(order="C"))
    _segment(digest, {"field": "target_labels", "dtype": "<i4", "shape": target.grid.shape},
             np.asarray(target.component_labels, dtype="<i4").tobytes(order="C"))
    _segment(digest, {"field": "target_region_identity"}, canonical_json([
        {"component_label": r.component_label, "region_id": r.region_id}
        for r in target.regions
    ]))
    return digest.hexdigest()


def persistence_product_id(identity: dict[str, Any]) -> str:
    return "hab_persistence:" + sha256(canonical_json(identity)).hexdigest()


def _fraction(numerator: int, denominator: int) -> float | None:
    return numerator / denominator if denominator else None


def exact_median_us(values: np.ndarray) -> ExactMicroseconds | None:
    if not values.size:
        return None
    ordered = np.sort(values.ravel())
    n = ordered.size
    if n % 2:
        return ExactMicroseconds(int(ordered[n // 2]), 1)
    total = int(ordered[n // 2 - 1]) + int(ordered[n // 2])
    return ExactMicroseconds(total // 2, 1) if total % 2 == 0 else ExactMicroseconds(total, 2)


def _derive(scenes: tuple[HABAnomalyGeometryScene, ...]) -> dict[str, Any]:
    target = scenes[-1]
    p, c, labels = (a.copy() for a in (
        target.candidate_analysis_support_mask, target.candidate_mask, target.component_labels
    ))
    shape, time = target.grid.shape, utc(target.target_acquired_at)
    prior_count = np.zeros(shape, np.uint32)
    streak = c.astype(np.uint32)
    previous_gap = np.full(shape, -1, np.int64)
    span = np.where(c, 0, -1).astype(np.int64)
    active = c.copy()
    for prior in reversed(scenes[:-1]):
        support = p & prior.candidate_analysis_support_mask
        elapsed = gap_us(time, prior.target_acquired_at)
        prior_count[support] += 1
        previous_gap[support & (previous_gap < 0)] = elapsed
        continued = active & support & prior.candidate_mask
        streak[continued] += 1
        span[continued] = elapsed
        active[support & ~prior.candidate_mask] = False
    q = p & (prior_count >= 1)
    b, recurrent = c & q, c & (streak >= 2)
    a_count, b_count, c_count = int(c.sum()), int(b.sum()), int(recurrent.sum())
    values, counts = np.unique(streak[c], return_counts=True)
    statistics = PersistenceStatistics(
        int(p.sum()), int(q.sum()), a_count, b_count, c_count, a_count - b_count,
        _fraction(b_count, a_count), _fraction(c_count, b_count),
        {str(int(v)): int(n) for v, n in zip(values, counts)},
    )
    regions = []
    for region in target.regions:
        mask = labels == region.component_label
        regional_b, regional_c = mask & b, mask & recurrent
        rb, rc = int(regional_b.sum()), int(regional_c.sum())
        records = []
        for prior in scenes[:-1]:
            supported = mask & prior.candidate_analysis_support_mask
            ns = int(supported.sum())
            no = int((supported & prior.candidate_mask).sum())
            records.append(PriorRegionEvidence(
                prior.product_id, utc(prior.target_acquired_at), ns, no, _fraction(no, ns)
            ))
        regions.append(PersistenceRegionSummary(
            region.region_id, region.component_label, region.pixel_count, rb,
            _fraction(rb, region.pixel_count), rc, _fraction(rc, rb),
            int(streak[regional_b].max()) if rb else None,
            float(np.median(streak[regional_b])) if rb else None,
            int(span[regional_c].max()) if rc else None,
            exact_median_us(span[regional_c]), tuple(records),
        ))
    return {
        "target_candidate_analysis_support_mask": p, "target_candidate_mask": c,
        "target_component_labels": labels, "prior_valid_observation_count": prior_count,
        "persistence_evaluable_mask": q, "current_streak_count": streak,
        "recurrent_candidate_mask": recurrent, "previous_valid_observation_gap_us": previous_gap,
        "current_streak_span_us": span, "regions": tuple(regions), "statistics": statistics,
    }


def _summary_payload(data: dict) -> dict:
    # Canonical JSON does not accept datetimes: normalize every record explicitly.
    regions = []
    for region in data["regions"]:
        item = asdict(region)
        for record in item["prior_observations"]:
            record["acquired_at"] = utc(record["acquired_at"]).isoformat()
        regions.append(item)
    return {"regions": regions, "statistics": asdict(data["statistics"])}


def output_content_fingerprint(data: dict) -> str:
    digest = sha256()
    _segment(digest, {"format": OUTPUT_FORMAT})
    for field, dtype in ARRAY_DTYPES.items():
        array = data[field]
        _segment(digest, {"field": field, "shape": array.shape, "dtype": dtype},
                 np.asarray(array, dtype=dtype).tobytes(order="C"))
    _segment(digest, {"field": "summaries"}, canonical_json(_summary_payload(data)))
    return digest.hexdigest()


def _build(
    scenes: tuple[HABAnomalyGeometryScene, ...], common: dict[str, Any], created_at: datetime,
) -> HABPersistenceScene:
    target = scenes[-1]
    times = tuple(utc(s.target_acquired_at) for s in scenes)
    ids = tuple(s.product_id for s in scenes)
    identity = {
        "processing_version": PROCESSING_VERSION,
        "parent_geometry_product_ids": list(ids),
        "acquired_at": [t.isoformat() for t in times],
        "target_geometry_product_id": target.product_id,
        "target_acquired_at": times[-1].isoformat(),
        "grid": target.grid.to_dict(),
        "common_temporal_comparison_contract": deepcopy(common),
        "policy": algorithm_policy(),
        "input_fingerprint_format": INPUT_FORMAT,
        "input_content_fingerprint": input_content_fingerprint(scenes),
        "software_versions": {"python": platform.python_version(), "numpy": np.__version__},
    }
    product_id = persistence_product_id(identity)
    data = _derive(scenes)
    parameters = {
        "identity": identity,
        "output_fingerprint_format": OUTPUT_FORMAT,
        "output_content_fingerprint": output_content_fingerprint(data),
        **_summary_payload(data),
        "scientific_limit": SCIENTIFIC_LIMIT,
    }
    provenance = DerivedProductRecord(
        product_id, "hab_persistence", created_at, PROCESSING_VERSION, ids, deepcopy(parameters)
    )
    return HABPersistenceScene(
        target.grid, ids, times, target.product_id, times[-1], **data,
        processing_parameters=parameters, product_id=product_id, provenance=provenance,
    )


def compute_hab_persistence(
    geometry_scenes: Iterable[HABAnomalyGeometryScene],
    *,
    temporal_parents: Mapping[str, TemporalFeatureScene],
    target_geometry_product_id: str,
) -> HABPersistenceScene:
    """Pure recurrence over validated parents; no network, cache, registry or upstream IO."""
    scenes, common = _sequence(geometry_scenes, temporal_parents, target_geometry_product_id)
    return _build(scenes, common, datetime.now(UTC))


def validate_scene(
    scene: HABPersistenceScene, geometry_scenes: Iterable[HABAnomalyGeometryScene],
    *, temporal_parents: Mapping[str, TemporalFeatureScene],
) -> None:
    if not isinstance(scene, HABPersistenceScene):
        raise TypeError("Expected a HABPersistenceScene.")
    scene.provenance.validate()
    scenes, common = _sequence(geometry_scenes, temporal_parents, scene.target_geometry_product_id)
    expected = _build(scenes, common, scene.provenance.created_at)
    for field, dtype in ARRAY_DTYPES.items():
        array, other = getattr(scene, field), getattr(expected, field)
        required = np.dtype(bool) if dtype == "uint8" else np.dtype(dtype)
        if (
            not isinstance(array, np.ndarray) or array.dtype != required
            or array.shape != other.shape or not np.array_equal(array, other)
        ):
            raise ValueError("Persistence arrays disagree with regenerated scientific evidence.")
    if (
        scene.grid != expected.grid
        or scene.parent_geometry_product_ids != expected.parent_geometry_product_ids
        or scene.acquired_at != expected.acquired_at
        or utc(scene.target_acquired_at) != expected.target_acquired_at
        or type(scene.regions) is not tuple
        or any(
            type(r) is not PersistenceRegionSummary
            or type(r.prior_observations) is not tuple
            or any(type(e) is not PriorRegionEvidence for e in r.prior_observations)
            or (r.median_current_streak_span_us is not None
                and type(r.median_current_streak_span_us) is not ExactMicroseconds)
            for r in scene.regions
        )
        or type(scene.statistics) is not PersistenceStatistics
        or canonical_json(_summary_payload(vars(scene)))
        != canonical_json(_summary_payload(vars(expected)))
        or canonical_json(scene.processing_parameters) != canonical_json(expected.processing_parameters)
        or scene.product_id != expected.product_id
        or scene.provenance.product_id != expected.product_id
        or scene.provenance.product_type != "hab_persistence"
        or scene.provenance.processing_version != PROCESSING_VERSION
        or scene.provenance.source_ids != expected.parent_geometry_product_ids
        or canonical_json(scene.provenance.parameters) != canonical_json(expected.processing_parameters)
    ):
        raise ValueError("Persistence identity, summaries or provenance disagree with validated parents.")
