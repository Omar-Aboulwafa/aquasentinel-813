from dataclasses import replace
from itertools import pairwise

import numpy as np
import pytest
from rasterio import Affine
from rasterio.features import rasterize

from aquasentinel.geometry import extract_hab_anomaly_geometry, spatial
from aquasentinel.geometry.spatial import connected_components, pixel_area, polygonize_labels

from .conftest import grid_for


def fixtures():
    single = np.array([[True]], bool)
    rectangle = np.ones((3, 4), bool)
    hole = np.ones((5, 5), bool)
    hole[1:4, 1:4] = False
    diagonal = np.eye(4, dtype=bool)
    pinched = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 0]], bool)
    border = np.zeros((6, 6), bool)
    border[0] = border[:, 0] = border[-1] = border[:, -1] = True
    return [single, rectangle, hole, diagonal, pinched, border]


@pytest.mark.parametrize(
    "mask", fixtures(), ids=["single", "rectangle", "hole", "diagonal", "pinched", "border"]
)
def test_exact_roundtrip_no_added_pixels(mask):
    labels, _ = connected_components(mask)
    grid = grid_for(mask.shape)
    geometries = polygonize_labels(labels, grid)
    rebuilt = rasterize(
        [(g, k) for k, g in geometries.items()],
        out_shape=grid.shape,
        transform=grid.transform,
        dtype="int32",
        all_touched=False,
    )
    assert np.array_equal(labels, rebuilt)
    assert np.array_equal(rebuilt > 0, mask)


def test_diagonal_one_region_multipart_no_bridge(make_parent):
    mask = np.eye(3, dtype=bool)
    s = extract_hab_anomaly_geometry(make_parent(shape=mask.shape, water=mask))
    assert len(s.regions) == 1
    assert s.regions[0].geometry["type"] == "MultiPolygon"
    assert len(s.regions[0].geometry["coordinates"]) == 3
    assert s.regions[0].pixel_count == 3


def signed_area(ring):
    return sum(a[0] * b[1] - b[0] * a[1] for a, b in pairwise(ring)) / 2


def test_hole_winding_and_projected_grid_edge_bounds():
    mask = fixtures()[2]
    labels, _ = connected_components(mask)
    grid = grid_for(mask.shape)
    geometry = polygonize_labels(labels, grid)[1]
    outer, hole = geometry["coordinates"]
    assert signed_area(outer) > 0 and signed_area(hole) < 0
    assert outer[0] == outer[-1] and hole[0] == hole[-1]
    for ring in (outer, hole):
        pixel_vertices = [(~grid.transform) @ point for point in ring]
        assert pixel_vertices[0] == min(pixel_vertices[:-1])
        assert all(all(float(v).is_integer() for v in p) for p in pixel_vertices)
    assert min(p[0] for p in outer) == grid.bounds[0]
    assert max(p[1] for p in outer) == grid.bounds[3]


def test_canonical_geometry_ignores_gdal_emission_ring_start_and_winding(monkeypatch):
    mask = np.eye(4, dtype=bool)
    labels, _ = connected_components(mask)
    grid = grid_for(mask.shape)
    expected = polygonize_labels(labels, grid)
    original = spatial.shapes

    def shuffled(*args, **kwargs):
        records = list(original(*args, **kwargs))
        for geometry, value in reversed(records):
            rings = []
            for ring in reversed(geometry["coordinates"]):
                points = list(reversed(ring[:-1]))
                points = points[1:] + points[:1]
                rings.append(points + [points[0]])
            yield {"type": "Polygon", "coordinates": rings}, value

    monkeypatch.setattr(spatial, "shapes", shuffled)
    assert polygonize_labels(labels, grid) == expected


def test_holes_and_parts_are_sorted(monkeypatch):
    mask = np.ones((7, 7), bool)
    mask[1:3, 1:3] = False
    mask[4:6, 4:6] = False
    labels, _ = connected_components(mask)
    grid = grid_for(mask.shape)
    expected = polygonize_labels(labels, grid)
    original = spatial.shapes

    def reversed_holes(*args, **kwargs):
        for geometry, value in original(*args, **kwargs):
            rings = geometry["coordinates"]
            yield {"type": "Polygon", "coordinates": [rings[0], *reversed(rings[1:])]}, value

    monkeypatch.setattr(spatial, "shapes", reversed_holes)
    assert polygonize_labels(labels, grid) == expected


@pytest.mark.parametrize("resolution", [10, 20, 30])
def test_area_is_affine_derived(make_parent, resolution):
    s = extract_hab_anomaly_geometry(make_parent(resolution=resolution))
    assert s.statistics.pixel_area_m2 == resolution**2
    assert s.regions[0].area_m2 == 12 * resolution**2
    assert s.regions[0].area_km2 == 12 * resolution**2 / 1e6
    assert s.regions[0].bbox_projected == s.grid.bounds


@pytest.mark.parametrize(
    "change",
    [
        {"crs": "EPSG:4326"},
        {"crs": "EPSG:99999999"},
        {"crs": "EPSG:2263"},
        {"resolution": 0},
        {"resolution": True},
        {"resolution": 10},
        {"width": 0},
        {"height": True},
        {"grid_id": ""},
        {"transform": tuple(Affine.identity())},
        {"bounds": (0, 0, 1, 1)},
        {"transform": Affine(20, 1, 200000, 0, -20, 2800000)},
        {"transform": Affine(20, 0, 200000, 1, -20, 2800000)},
        {"transform": Affine(20, 0, 200000, 0, -10, 2800000)},
        {"transform": Affine(0, 0, 200000, 0, 0, 2800000)},
        {"transform": Affine(20, 0, float("nan"), 0, -20, 2800000)},
    ],
)
def test_unsupported_crs_or_grid_fails(change):
    with pytest.raises(ValueError):
        pixel_area(replace(grid_for((3, 4)), **change))


@pytest.mark.parametrize("resolution", [1e-200, 1e200])
def test_nonrepresentable_pixel_area_fails(resolution):
    with pytest.raises(ValueError):
        pixel_area(grid_for((1, 1), resolution))
