import numpy as np
import pytest

from aquasentinel.geometry import extract_hab_anomaly_geometry, spatial
from aquasentinel.geometry.spatial import connected_components


def test_diagonal_eight_connectivity():
    labels, seeds = connected_components(np.eye(4, dtype=bool))
    assert seeds == ((0, 0),)
    assert np.array_equal(labels, np.eye(4, dtype=np.int32))


def test_separated_single_pixels_row_major_and_no_filtering(make_parent):
    mask = np.zeros((5, 7), bool)
    mask[0, 6] = mask[2, 2] = mask[4, 0] = True
    scene = extract_hab_anomaly_geometry(make_parent(shape=mask.shape, water=mask))
    assert [(r.first_pixel_row, r.first_pixel_col) for r in scene.regions] == [
        (0, 6),
        (2, 2),
        (4, 0),
    ]
    assert [scene.component_labels[r, c] for r, c in [(0, 6), (2, 2), (4, 0)]] == [1, 2, 3]
    assert [r.pixel_count for r in scene.regions] == [1, 1, 1]
    assert scene.statistics.one_pixel_region_count == 3
    assert scene.statistics.region_size_histogram["1"] == 3


def test_exact_label_pixel_counts():
    mask = np.zeros((5, 8), bool)
    mask[:2, :3] = True
    mask[3:, 6:] = True
    labels, seeds = connected_components(mask)
    assert seeds == ((0, 0), (3, 6))
    assert [int((labels == label).sum()) for label in (1, 2)] == [6, 4]
    assert np.array_equal(labels > 0, mask)
    assert labels.dtype == np.int32


def test_label_overflow_is_explicit(monkeypatch):
    monkeypatch.setattr(spatial, "LABEL_LIMIT", 1)
    with pytest.raises(ValueError, match="int32"):
        connected_components(np.array([[True, False, True]], bool))


@pytest.mark.parametrize("mask", [np.zeros((2, 2), np.uint8), np.zeros(3, bool)])
def test_component_input_contract(mask):
    with pytest.raises(ValueError):
        connected_components(mask)
