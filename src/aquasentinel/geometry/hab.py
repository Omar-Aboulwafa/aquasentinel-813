"""Frozen family-aware P0 screening policy; not a HAB, confidence or risk model."""

from __future__ import annotations

import platform
import struct
from copy import deepcopy
from dataclasses import asdict, replace
from datetime import UTC, datetime
from hashlib import sha256
from typing import Any

import numpy as np
import rasterio

from aquasentinel.features.spectral import FEATURE_ORDER, FORMULA_DEFINITIONS
from aquasentinel.geometry.models import (
    DescriptiveSummary,
    FamilyEvidenceDiagnostics,
    FeatureEvidenceDiagnostics,
    GeometryDiagnostics,
    GeometryStatistics,
    HABAnomalyGeometryScene,
    HABAnomalyRegion,
    RegionFeatureSummary,
)
from aquasentinel.geometry.spatial import (
    NEIGHBOURS,
    connected_components,
    pixel_area,
    polygonize_labels,
    projected_bbox,
)
from aquasentinel.preprocessing.cache import canonical_json
from aquasentinel.provenance import DerivedProductRecord
from aquasentinel.temporal.models import TemporalFeatureScene, utc

PROCESSING_VERSION = "as105-v1"
RANK_THRESHOLD = np.float32(0.90)
FAMILY_ORDER = (
    "red_edge_b5_vs_red",
    "red_edge_line_height",
    "red_edge_b6_vs_red",
    "visible_green_vs_red",
    "visible_green_vs_blue",
)
FAMILY_MEMBERS = {
    FAMILY_ORDER[0]: ("ndci_like", "red_edge_red_ratio"),
    FAMILY_ORDER[1]: ("mci_like",),
    FAMILY_ORDER[2]: ("red_edge2_red_ratio",),
    FAMILY_ORDER[3]: ("green_red_ratio",),
    FAMILY_ORDER[4]: ("green_blue_ratio",),
}
SCIENTIFIC_LIMIT = (
    "Predeclared P0 candidate spectral anomaly geometry only. Rank is not probability, "
    "confidence, significance or severity; policy families are not statistically independent. "
    "No HAB confirmation, concentration, species, toxins, water safety, intake risk, "
    "persistence, alert or lead-time inference. Future comparative policy validation required."
)


def algorithm_policy() -> dict[str, Any]:
    """Fresh serialization of the frozen policy, with no user tuning interface."""
    return {
        "status": "predeclared P0 heuristic; future comparative validation required",
        "feature_order": list(FEATURE_ORDER),
        "family_order": list(FAMILY_ORDER),
        "family_members": {k: list(v) for k, v in FAMILY_MEMBERS.items()},
        "feature_support": "rank_valid_mask",
        "evidence": "rank_valid_mask AND deviation > 0 AND rank >= threshold_float32",
        "rank_threshold": {
            "nominal": 0.90,
            "nominal_decimal": "0.90",
            "dtype": "float32",
            "value": float(RANK_THRESHOLD),
            "ieee754_big_endian_hex": struct.pack(">f", RANK_THRESHOLD).hex(),
        },
        "direction": "strictly positive deviation; both signed zeros excluded",
        "family_aggregation": "OR within each family; at most one vote per family",
        "minimum_family_votes": 2,
        "required_red_edge_vote": True,
        "red_edge_families": list(FAMILY_ORDER[:3]),
        "denominator": "P = available_family_count >= 2 AND any available F1/F2/F3",
        "region_connectivity": 8,
        "neighbour_order": [list(v) for v in NEIGHBOURS],
        "component_order": "first candidate pixel in row-major scan; labels 1..N; 0 background",
        "polygon_piece_connectivity": 4,
        "polygonization": "Rasterio shapes in pixel coordinates; group by existing label",
        "geometry": "exact grid edges; projected CRS; no WGS84 GeoJSON claim",
        "canonicalization": "world outer CCW/holes CW; lexicographic pixel start/holes/parts",
        "area": "pixel count * abs(a*e-b*d); projected metre north-up square grid only",
        "morphology": "none",
        "spatial_filtering": "none",
        "robust_z": "not consumed; neither gate nor stored regional summary",
        "statistics": {
            "regional": (
                "finite supported deviation/rank; float64 min/median/max; "
                "sorted middle value or overflow-safe even midpoint; missing None"
            ),
            "candidate_fraction": "count(candidate)/count(P); None for empty P",
            "feature_fraction": "feature evidence / feature rank support; None for empty support",
            "family_fraction": "family evidence / family availability; None for empty support",
            "vote_histograms": "0..5; separately on P and on candidates",
            "region_size_bins": ["1", "2-4", "5-9", "10-49", "50+"],
        },
    }


def _segment(digest, header: dict, data: bytes = b"") -> None:
    encoded = canonical_json({**header, "byte_count": len(data)})
    digest.update(len(encoded).to_bytes(8, "big"))
    digest.update(encoded)
    digest.update(data)


def input_content_fingerprint(parent: TemporalFeatureScene) -> str:
    """Canonical consumed content only; caller separately validates the whole parent."""
    digest = sha256()
    _segment(digest, {"format": "as105-input-v1", "segment": "grid", "grid": parent.grid.to_dict()})
    _segment(
        digest,
        {
            "segment": "associations",
            "feature_order": list(FEATURE_ORDER),
            "family_order": list(FAMILY_ORDER),
            "family_members": {k: list(v) for k, v in FAMILY_MEMBERS.items()},
        },
    )
    for name in FEATURE_ORDER:
        result = parent.results[name]
        support = result.rank_valid_mask
        if support.shape != parent.grid.shape or support.dtype != bool:
            raise ValueError("Consumed rank support must be a Boolean analysis-grid mask.")
        _segment(
            digest,
            {"feature": name, "field": "rank_valid_mask", "shape": support.shape, "dtype": "uint8"},
            support.astype(np.uint8).tobytes(order="C"),
        )
        for field, dtype, size in (("deviation", "<f8", 8), ("empirical_rank", "<f4", 4)):
            array = getattr(result, field)
            if (
                array.shape != support.shape
                or array.dtype.kind != "f"
                or array.dtype.itemsize != size
                or not np.isfinite(array[support]).all()
            ):
                raise ValueError("Consumed values require declared precision and finite support.")
            _segment(
                digest,
                {
                    "feature": name,
                    "field": field,
                    "dtype": dtype,
                    "selection": "rank_valid_mask in row-major order",
                },
                np.asarray(array[support], dtype=dtype).tobytes(order="C"),
            )
    return digest.hexdigest()


def geometry_product_id(identity: dict) -> str:
    return "hab_geometry:" + sha256(canonical_json(identity)).hexdigest()


def _identity(parent: TemporalFeatureScene) -> dict[str, Any]:
    return {
        "processing_version": PROCESSING_VERSION,
        "parent_temporal_product_id": parent.product_id,
        "parent_processing_version": parent.provenance.processing_version,
        "target_acquired_at": utc(parent.target_acquired_at).isoformat(),
        "grid": parent.grid.to_dict(),
        "input_fingerprint_format": "as105-input-v1",
        "input_content_fingerprint": input_content_fingerprint(parent),
        "policy": algorithm_policy(),
        "software_versions": {
            "python": platform.python_version(),
            "numpy": np.__version__,
            "rasterio": rasterio.__version__,
            "GDAL": rasterio.__gdal_version__,
        },
    }


def _summary(array: np.ndarray, mask: np.ndarray) -> DescriptiveSummary:
    values = array[mask].astype(np.float64)
    if not values.size:
        return DescriptiveSummary(0, None, None, None)
    ordered = np.sort(values)
    middle = values.size // 2
    median = float(ordered[middle])
    if values.size % 2 == 0:
        lower, upper = float(ordered[middle - 1]), median
        # Avoid overflow in a finite same-sign pair without changing ordinary
        # midpoint arithmetic or clipping/imputing any consumed observation.
        if (lower >= 0) == (upper >= 0) and max(abs(lower), abs(upper)) > (
            np.finfo(np.float64).max / 2
        ):
            median = lower / 2 + upper / 2
        else:
            median = (lower + upper) / 2
    return DescriptiveSummary(int(values.size), float(values.min()), median, float(values.max()))


def _fraction(count: int, denominator: int) -> float | None:
    return count / denominator if denominator else None


def _validate_parent(parent: TemporalFeatureScene) -> None:
    if not isinstance(parent, TemporalFeatureScene):
        raise TypeError("AS-105 requires an immediate TemporalFeatureScene parent.")
    parent.validate()
    if parent.provenance.processing_version != "as104-v1":
        raise ValueError("AS-105 v1 requires the validated AS-104 v1 contract.")
    for family, members in FAMILY_MEMBERS.items():
        if any(FORMULA_DEFINITIONS[n]["feature_family"] != family for n in members):
            raise ValueError("Policy family mapping differs from AS-103 metadata.")
    pixel_area(parent.grid)


def _derive(parent: TemporalFeatureScene) -> dict[str, Any]:
    support, evidence = {}, {}
    feature_diagnostics = {}
    for name in FEATURE_ORDER:
        result = parent.results[name]
        mask = result.rank_valid_mask.copy()
        positive = mask & (result.deviation > 0)
        high_rank = mask & (result.empirical_rank >= RANK_THRESHOLD)
        support[name] = mask
        evidence[name] = positive & high_rank
        count, voted = int(mask.sum()), int(evidence[name].sum())
        feature_diagnostics[name] = FeatureEvidenceDiagnostics(
            count, int(positive.sum()), int(high_rank.sum()), voted, _fraction(voted, count)
        )
    available, voted = {}, {}
    family_diagnostics = {}
    for family, members in FAMILY_MEMBERS.items():
        available[family] = np.logical_or.reduce([support[n] for n in members]).copy()
        voted[family] = np.logical_or.reduce([evidence[n] for n in members]).copy()
        a, v = int(available[family].sum()), int(voted[family].sum())
        family_diagnostics[family] = FamilyEvidenceDiagnostics(a, v, _fraction(v, a))
    a_count = np.sum(list(available.values()), axis=0, dtype=np.uint8)
    v_count = np.sum(list(voted.values()), axis=0, dtype=np.uint8)
    p = (a_count >= 2) & np.logical_or.reduce([available[n] for n in FAMILY_ORDER[:3]])
    candidate = (v_count >= 2) & np.logical_or.reduce([voted[n] for n in FAMILY_ORDER[:3]])
    if np.any(candidate & ~p) or np.any(candidate & ~parent.valid_water_mask):
        raise ValueError("Candidate support cannot expand beyond eligible parent water support.")
    labels, seeds = connected_components(candidate)
    geometries = polygonize_labels(labels, parent.grid)
    area = pixel_area(parent.grid)
    regions = []
    for label, (row, col) in enumerate(seeds, 1):
        region_mask = labels == label
        counts = {f: int((region_mask & voted[f]).sum()) for f in FAMILY_ORDER}
        pixels = int(region_mask.sum())
        regions.append(
            HABAnomalyRegion(
                "",
                label,
                row,
                col,
                geometries[label],
                pixels,
                pixels * area,
                pixels * area / 1_000_000,
                projected_bbox(region_mask, parent.grid),
                tuple(f for f in FAMILY_ORDER if counts[f]),
                counts,
                int(v_count[region_mask].max()),
                float(np.median(v_count[region_mask])),
                {
                    n: RegionFeatureSummary(
                        _summary(parent.results[n].deviation, region_mask & support[n]),
                        _summary(parent.results[n].empirical_rank, region_mask & support[n]),
                    )
                    for n in FEATURE_ORDER
                },
            )
        )
    sizes = np.asarray([r.pixel_count for r in regions], np.int64)
    total, eligible = int(candidate.sum()), int(p.sum())
    stats = GeometryStatistics(
        eligible,
        total,
        _fraction(total, eligible),
        area,
        total * area,
        total * area / 1_000_000,
        len(regions),
        int((sizes == 1).sum()),
        int(sizes.max()) if sizes.size else None,
        float(np.median(sizes)) if sizes.size else None,
        float(sizes.max() * area) if sizes.size else None,
        float(np.median(sizes) * area) if sizes.size else None,
        {
            "1": int((sizes == 1).sum()),
            "2-4": int(((sizes >= 2) & (sizes <= 4)).sum()),
            "5-9": int(((sizes >= 5) & (sizes <= 9)).sum()),
            "10-49": int(((sizes >= 10) & (sizes <= 49)).sum()),
            "50+": int((sizes >= 50).sum()),
        },
        {str(n): int((p & (v_count == n)).sum()) for n in range(6)},
        {str(n): int((candidate & (v_count == n)).sum()) for n in range(6)},
    )
    return {
        "feature_support_masks": support,
        "feature_evidence_masks": evidence,
        "family_available_masks": available,
        "family_evidence_masks": voted,
        "candidate_analysis_support_mask": p,
        "available_family_count": a_count,
        "family_vote_count": v_count,
        "candidate_mask": candidate,
        "component_labels": labels,
        "regions": tuple(regions),
        "statistics": stats,
        "diagnostics": GeometryDiagnostics(feature_diagnostics, family_diagnostics),
    }


def _array_items(data: dict) -> list[tuple[str, np.ndarray, str]]:
    items = []
    for field, order in (
        ("feature_support_masks", FEATURE_ORDER),
        ("feature_evidence_masks", FEATURE_ORDER),
        ("family_available_masks", FAMILY_ORDER),
        ("family_evidence_masks", FAMILY_ORDER),
    ):
        items.extend((field + ":" + n, data[field][n], "uint8") for n in order)
    items.extend(
        (n, data[n], "uint8")
        for n in (
            "candidate_analysis_support_mask",
            "available_family_count",
            "family_vote_count",
            "candidate_mask",
        )
    )
    items.append(("component_labels", data["component_labels"], "<i4"))
    return items


def output_content_fingerprint(data: dict) -> str:
    """Complete scientific output integrity, excluding product-derived region IDs."""
    digest = sha256()
    for name, array, dtype in _array_items(data):
        _segment(
            digest,
            {"format": "as105-output-v1", "field": name, "shape": array.shape, "dtype": dtype},
            np.asarray(array, dtype=dtype).tobytes(order="C"),
        )
    regions = []
    for region in data["regions"]:
        payload = asdict(region)
        payload.pop("region_id")
        regions.append(payload)
    _segment(
        digest,
        {"field": "measurements"},
        canonical_json(
            {
                "regions": regions,
                "statistics": asdict(data["statistics"]),
                "diagnostics": asdict(data["diagnostics"]),
            }
        ),
    )
    return digest.hexdigest()


def _build(parent: TemporalFeatureScene, created_at: datetime) -> HABAnomalyGeometryScene:
    identity = _identity(parent)
    product_id = geometry_product_id(identity)
    data = _derive(parent)
    data["regions"] = tuple(
        replace(r, region_id=f"{product_id}:region:{r.component_label}") for r in data["regions"]
    )
    parameters = {
        "identity": identity,
        "output_fingerprint_format": "as105-output-v1",
        "output_content_fingerprint": output_content_fingerprint(data),
        "statistics": asdict(data["statistics"]),
        "diagnostics": asdict(data["diagnostics"]),
        "scientific_limit": SCIENTIFIC_LIMIT,
    }
    provenance = DerivedProductRecord(
        product_id,
        "hab_anomaly_geometry",
        created_at,
        PROCESSING_VERSION,
        (parent.product_id,),
        deepcopy(parameters),
    )
    return HABAnomalyGeometryScene(
        parent.grid,
        parent.product_id,
        utc(parent.target_acquired_at),
        **data,
        processing_parameters=parameters,
        product_id=product_id,
        provenance=provenance,
    )


def extract_hab_anomaly_geometry(parent: TemporalFeatureScene) -> HABAnomalyGeometryScene:
    """Pure frozen-policy geometry; no IO, registry mutation or upstream computation."""
    _validate_parent(parent)
    scene = _build(parent, datetime.now(UTC))
    scene.validate(parent)
    return scene


def validate_scene(scene: HABAnomalyGeometryScene, parent: TemporalFeatureScene) -> None:
    _validate_parent(parent)
    scene.provenance.validate()
    expected = _build(parent, scene.provenance.created_at)
    data = vars(scene)
    expected_data = vars(expected)
    for field, order in (
        ("feature_support_masks", FEATURE_ORDER),
        ("feature_evidence_masks", FEATURE_ORDER),
        ("family_available_masks", FAMILY_ORDER),
        ("family_evidence_masks", FAMILY_ORDER),
    ):
        if not isinstance(data[field], dict) or tuple(data[field]) != order:
            raise ValueError("Geometry feature/family masks require canonical keys and order.")
    for name, array, _ in _array_items(data):
        if ":" in name:
            field, key = name.split(":", 1)
            other = expected_data[field][key]
        else:
            other = expected_data[name]
        if (
            not isinstance(array, np.ndarray)
            or array.dtype != other.dtype
            or not np.array_equal(array, other)
        ):
            raise ValueError("Geometry arrays disagree with regenerated support/evidence/labels.")
    if (
        scene.grid != expected.grid
        or scene.parent_temporal_product_id != expected.parent_temporal_product_id
        or utc(scene.target_acquired_at) != expected.target_acquired_at
        or type(scene.regions) is not tuple
        or any(type(r) is not HABAnomalyRegion for r in scene.regions)
        or canonical_json([asdict(r) for r in scene.regions])
        != canonical_json([asdict(r) for r in expected.regions])
        or type(scene.statistics) is not GeometryStatistics
        or type(scene.diagnostics) is not GeometryDiagnostics
        or canonical_json(asdict(scene.statistics)) != canonical_json(asdict(expected.statistics))
        or canonical_json(asdict(scene.diagnostics)) != canonical_json(asdict(expected.diagnostics))
        or canonical_json(scene.processing_parameters)
        != canonical_json(expected.processing_parameters)
        or scene.product_id != expected.product_id
        or scene.provenance.product_id != scene.product_id
        or scene.provenance.product_type != "hab_anomaly_geometry"
        or scene.provenance.processing_version != PROCESSING_VERSION
        or scene.provenance.source_ids != (parent.product_id,)
        or canonical_json(scene.provenance.parameters)
        != canonical_json(scene.processing_parameters)
    ):
        raise ValueError("Geometry scene disagrees with frozen policy, measurements or provenance.")
