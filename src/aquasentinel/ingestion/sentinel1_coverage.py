"""Canonical WGS84 polygon metadata operations; never raster/pixel operations."""

from __future__ import annotations

from math import isfinite
from typing import Any

from shapely import Polygon, intersection, union_all
from shapely.geometry import shape
from shapely.geometry.polygon import orient


def _ring(values: Any) -> list[list[float]]:
    if not isinstance(values, (list, tuple)) or len(values) < 4:
        raise ValueError("Footprint ring must contain four or more positions.")
    points = []
    for pair in values:
        if (
            not isinstance(pair, (list, tuple))
            or len(pair) != 2
            or any(
                isinstance(v, bool) or not isinstance(v, (int, float)) or not isfinite(v)
                for v in pair
            )
        ):
            raise ValueError("Footprint positions must be finite longitude/latitude pairs.")
        x, y = map(float, pair)
        if not -180 <= x <= 180 or not -90 <= y <= 90:
            raise ValueError("Footprint position is outside WGS84 bounds.")
        points.append([0.0 if x == 0 else x, 0.0 if y == 0 else y])
    if points[0] != points[-1]:
        raise ValueError("Footprint ring must be closed.")
    return points


def canonical_geometry(value: Any, *, allow_empty: bool = False) -> dict[str, Any]:
    if not isinstance(value, dict) or value.get("type") not in {"Polygon", "MultiPolygon"}:
        raise ValueError("Footprint must be Polygon or MultiPolygon metadata.")
    coordinates = value.get("coordinates")
    if not isinstance(coordinates, (tuple, list)):
        raise TypeError("Footprint coordinates must be a sequence.")
    if not coordinates:
        if allow_empty:
            return {"type": "MultiPolygon", "coordinates": []}
        raise ValueError("Source footprint cannot be empty.")
    parts = [coordinates] if value["type"] == "Polygon" else coordinates
    normalized = []
    for rings in parts:
        if not isinstance(rings, (list, tuple)) or not rings:
            raise ValueError("Footprint polygon lacks exterior ring.")
        normalized.append([_ring(ring) for ring in rings])
    geom = shape({"type": "MultiPolygon", "coordinates": normalized})
    if not geom.is_valid or geom.is_empty or geom.area <= 0:
        raise ValueError("Source footprint must have valid nonempty polygon topology.")
    return _canonical_shape(geom)


def _canonical_shape(geom: Any) -> dict[str, Any]:
    if geom.is_empty:
        return {"type": "MultiPolygon", "coordinates": []}
    polygons = [geom] if isinstance(geom, Polygon) else list(geom.geoms)
    polygons = [g for g in polygons if isinstance(g, Polygon) and not g.is_empty]

    def canonical_ring(coords: Any) -> list[list[float]]:
        points = [tuple(0.0 if c == 0 else float(c) for c in p[:2]) for p in coords][:-1]
        rotations = [points[i:] + points[:i] for i in range(len(points))]
        ordered = min(rotations)
        return [list(p) for p in ordered + [ordered[0]]]

    parts = []
    for polygon in polygons:
        polygon = orient(polygon, sign=1.0)
        exterior = canonical_ring(polygon.exterior.coords)
        interiors = sorted(canonical_ring(r.coords) for r in polygon.interiors)
        parts.append([exterior, *interiors])
    parts.sort()
    return {"type": "MultiPolygon", "coordinates": parts}


def coverage(envelope: dict[str, Any], footprints: tuple[dict[str, Any], ...]) -> dict[str, Any]:
    """Intersection/union of source footprints, not scientific evaluability."""
    region = shape(envelope)
    support = intersection(region, union_all([shape(g) for g in footprints]))
    return {
        "source_support": _canonical_shape(support),
        "coverage_gaps": _canonical_shape(region.difference(support)),
        "geometry_crs": "EPSG:4326",
        "support_semantics": "METADATA_FOOTPRINT_ONLY_NOT_PIXEL_EVALUABILITY",
    }


def common_coverage(
    envelope: dict[str, Any], supports: tuple[dict[str, Any], ...]
) -> dict[str, Any]:
    result = shape(envelope)
    for support in supports:
        result = result.intersection(shape(support))
    return {
        "source_support": _canonical_shape(result),
        "coverage_gaps": _canonical_shape(shape(envelope).difference(result)),
        "geometry_crs": "EPSG:4326",
        "missing_support": "NODATA_OR_UNAVAILABLE_NEVER_ZERO_ANOMALY",
    }
