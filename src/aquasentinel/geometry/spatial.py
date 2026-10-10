"""Exact grid-cell components and boundaries; no morphology or size filtering."""

from __future__ import annotations

import re
from collections import deque
from typing import Any

import numpy as np
from rasterio import Affine
from rasterio.crs import CRS
from rasterio.errors import CRSError
from rasterio.features import rasterize, shapes

from aquasentinel.preprocessing.models import AnalysisGrid

NEIGHBOURS = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
LABEL_LIMIT = int(np.iinfo(np.int32).max)


def pixel_area(grid: AnalysisGrid) -> float:
    """Projected metre-grid area, not geodesic area or confirmed bloom extent."""
    if (
        not isinstance(grid, AnalysisGrid)
        or type(grid.width) is not int
        or type(grid.height) is not int
        or grid.width <= 0
        or grid.height <= 0
        or not isinstance(grid.crs, str)
        or not re.fullmatch(r"EPSG:[1-9][0-9]*", grid.crs)
        or not isinstance(grid.grid_id, str)
        or not grid.grid_id
        or not isinstance(grid.transform, Affine)
        or isinstance(grid.resolution, bool)
        or not isinstance(grid.resolution, (int, float))
    ):
        raise ValueError("AS-105 requires a positive, explicit EPSG metric analysis grid.")
    try:
        crs = CRS.from_user_input(grid.crs)
        a, b, c, d, e, f = tuple(grid.transform)[:6]
        area = abs(a * e - b * d)
        expected_bounds = (c, f + e * grid.height, c + a * grid.width, f)
        if (
            not crs.is_projected
            or crs.linear_units_factor[1] != 1.0
            or not np.isfinite([a, b, c, d, e, f, grid.resolution, *grid.bounds]).all()
            or b != 0
            or d != 0
            or a <= 0
            or e >= 0
            or a != -e
            or grid.resolution != a
            or tuple(grid.bounds) != expected_bounds
            or not np.isfinite(area)
            or area <= 0
        ):
            raise ValueError
    except (TypeError, ValueError, AttributeError, CRSError):
        raise ValueError(
            "AS-105 supports finite north-up square-pixel projected metre grids."
        ) from None
    return float(area)


def connected_components(candidate: np.ndarray) -> tuple[np.ndarray, tuple[tuple[int, int], ...]]:
    """Eight-neighbour flood fill; first row-major pixel determines each label."""
    if candidate.ndim != 2 or candidate.dtype != bool:
        raise ValueError("Candidate support must be a two-dimensional Boolean mask.")
    labels = np.zeros(candidate.shape, np.int32)
    seeds = []
    height, width = candidate.shape
    for row in range(height):
        for col in range(width):
            if not candidate[row, col] or labels[row, col]:
                continue
            label = len(seeds) + 1
            if label > LABEL_LIMIT:
                raise ValueError("Candidate region count exceeds int32 label capacity.")
            seeds.append((row, col))
            labels[row, col] = label
            pending = deque([(row, col)])
            while pending:
                r, c = pending.popleft()
                for dr, dc in NEIGHBOURS:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < height
                        and 0 <= nc < width
                        and candidate[nr, nc]
                        and not labels[nr, nc]
                    ):
                        labels[nr, nc] = label
                        pending.append((nr, nc))
    return labels, tuple(seeds)


def _ring(points: list, exterior: bool) -> tuple[tuple[int, int], ...]:
    """Exact integer grid vertices; world outer CCW / holes CW on north-up grids."""
    vertices = []
    for point in points:
        if len(point) != 2 or any(not np.isfinite(v) or int(v) != v for v in point):
            raise ValueError("Polygonization must return finite integer pixel-edge vertices.")
        vertices.append(tuple(int(v) for v in point))
    if len(vertices) < 5 or vertices[0] != vertices[-1]:
        raise ValueError("Pixel polygon rings must be closed with at least four edges.")
    vertices.pop()
    pairs = list(zip(vertices, vertices[1:] + vertices[:1], strict=True))
    if any((a[0] == b[0]) == (a[1] == b[1]) for a, b in pairs):
        raise ValueError("Polygon boundaries must follow nonzero axis-aligned pixel edges.")
    twice_area = sum(a[0] * b[1] - b[0] * a[1] for a, b in pairs)
    if not twice_area:
        raise ValueError("Pixel rings must have nonzero area.")
    # The north-up affine has negative determinant, reversing pixel-space winding.
    if (twice_area < 0) != exterior:
        vertices.reverse()
    minimum = min(vertices)
    rotations = [tuple(vertices[i:] + vertices[:i]) for i, p in enumerate(vertices) if p == minimum]
    ordered = min(rotations)
    return (*ordered, ordered[0])


def polygonize_labels(labels: np.ndarray, grid: AnalysisGrid) -> dict[int, dict[str, Any]]:
    """Four-neighbour pieces grouped by existing eight-connected region labels."""
    pixel_area(grid)
    if labels.shape != grid.shape or labels.dtype != np.int32 or np.any(labels < 0):
        raise ValueError("Polygon labels must be nonnegative int32 values on the analysis grid.")
    groups: dict[int, list] = {}
    if not np.any(labels):
        return {}
    for geometry, value in shapes(
        labels, mask=labels > 0, connectivity=4, transform=Affine.identity()
    ):
        if geometry["type"] != "Polygon":
            raise ValueError("Unexpected pixel polygonization geometry.")
        rings = geometry["coordinates"]
        outer = _ring(rings[0], True)
        holes = sorted(_ring(r, False) for r in rings[1:])
        groups.setdefault(int(value), []).append((outer, *holes))
    result = {}
    for label in sorted(groups):
        parts = sorted(groups[label])
        projected = [
            [[tuple(float(v) for v in grid.transform @ point) for point in ring] for ring in part]
            for part in parts
        ]
        result[label] = (
            {"type": "Polygon", "coordinates": projected[0]}
            if len(projected) == 1
            else {"type": "MultiPolygon", "coordinates": projected}
        )
    reconstructed = rasterize(
        [(g, label) for label, g in result.items()],
        out_shape=grid.shape,
        transform=grid.transform,
        fill=0,
        dtype="int32",
        all_touched=False,
        skip_invalid=False,
    )
    if not np.array_equal(reconstructed, labels):
        raise ValueError("Pixel polygons must rasterize to the exact original region labels.")
    return result


def projected_bbox(mask: np.ndarray, grid: AnalysisGrid) -> tuple[float, float, float, float]:
    rows, cols = np.nonzero(mask)
    left, top = grid.transform @ (int(cols.min()), int(rows.min()))
    right, bottom = grid.transform @ (int(cols.max()) + 1, int(rows.max()) + 1)
    return float(left), float(bottom), float(right), float(top)
