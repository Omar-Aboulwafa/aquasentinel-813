from datetime import UTC, datetime, timedelta

import numpy as np
import pytest

from aquasentinel.persistence.models import ExactMicroseconds
from aquasentinel.persistence.recurrence import exact_median_us


def test_region_support_and_overlap_independently_reproduced(make_sequence, compute):
    p0 = np.array([[True, False, True], [False, True, False]])
    c0 = np.array([[True, False, False], [False, True, False]])
    c1 = np.array([[False, False, True], [False, True, False]])
    sequence = make_sequence([(p0, c0), (True, c1), (True, True)])
    result = compute(sequence)
    target = sequence[0][-1]
    assert len(result.regions) == len(target.regions)
    for summary, original in zip(result.regions, target.regions):
        mask = target.component_labels == original.component_label
        b = mask & result.persistence_evaluable_mask
        c = mask & result.recurrent_candidate_mask
        assert summary.region_id == original.region_id
        assert summary.component_label == original.component_label
        assert summary.target_pixel_count == int(mask.sum()) == original.pixel_count
        assert summary.persistence_evaluable_target_candidate_count == int(b.sum())
        assert summary.candidate_history_coverage == int(b.sum()) / int(mask.sum())
        assert summary.recurrent_candidate_count == int(c.sum())
        assert summary.recurrence_fraction == int(c.sum()) / int(b.sum())
        assert summary.maximum_streak_count == int(result.current_streak_count[b].max())
        assert summary.median_streak_count == np.median(result.current_streak_count[b])
        for evidence, prior in zip(summary.prior_observations, sequence[0][:-1]):
            support = mask & prior.candidate_analysis_support_mask
            overlap = support & prior.candidate_mask
            assert evidence.geometry_product_id == prior.product_id
            assert evidence.acquired_at == prior.target_acquired_at
            assert evidence.supported_target_region_pixel_count == int(support.sum())
            assert evidence.candidate_overlap_pixel_count == int(overlap.sum())
            expected = int(overlap.sum()) / int(support.sum()) if support.any() else None
            assert evidence.candidate_overlap_fraction_of_supported == expected


@pytest.mark.parametrize("prior", [(True, False), (False, False)])
def test_zero_recurrence_and_zero_history_regions_retained(make_sequence, compute, prior):
    sequence = make_sequence([prior, (True, True)])
    result = compute(sequence)
    assert len(result.regions) == len(sequence[0][-1].regions) == 1
    region = result.regions[0]
    assert region.recurrent_candidate_count == 0
    assert region.median_current_streak_span_us is None
    assert region.maximum_current_streak_span_us is None
    assert region.recurrence_fraction == (0.0 if prior[0] else None)
    assert region.median_streak_count == (1.0 if prior[0] else None)
    assert region.candidate_history_coverage == (1.0 if prior[0] else 0.0)
    assert region.prior_observations[0].candidate_overlap_fraction_of_supported == (
        0.0 if prior[0] else None)


def test_multiple_regions_keep_target_order_and_geometry(make_sequence, compute):
    mask = np.zeros((5, 5), bool)
    mask[0, 0] = mask[4, 4] = True
    sequence = make_sequence([(True, mask), (True, mask)], shape=(5, 5))
    target = sequence[0][-1]
    geometries = [r.geometry.copy() for r in target.regions]
    result = compute(sequence)
    assert [r.component_label for r in result.regions] == [1, 2]
    assert [r.region_id for r in result.regions] == [r.region_id for r in target.regions]
    assert [r.geometry for r in target.regions] == geometries
    assert all(r.target_pixel_count == r.recurrent_candidate_count == 1 for r in result.regions)


def test_half_microsecond_region_median_not_truncated(make_sequence, compute):
    times = [datetime(2023, 4, 1, tzinfo=UTC) + timedelta(microseconds=v) for v in (0, 1, 2)]
    p0 = np.array([[True, False]])
    p1 = np.array([[False, True]])
    result = compute(make_sequence([(p0, p0), (p1, p1), (True, True)], times=times, shape=(1, 2)))
    assert result.current_streak_span_us.tolist() == [[2, 1]]
    assert result.regions[0].median_current_streak_span_us == ExactMicroseconds(3, 2)
    assert result.regions[0].maximum_current_streak_span_us == 2


@pytest.mark.parametrize("values,expected", [
    ([], None), ([1], ExactMicroseconds(1, 1)), ([1, 3], ExactMicroseconds(2, 1)),
    ([1, 2], ExactMicroseconds(3, 2)), ([7, 1, 3], ExactMicroseconds(3, 1)),
    ([int(np.iinfo(np.int64).max) - 1, int(np.iinfo(np.int64).max)],
     ExactMicroseconds(2 * int(np.iinfo(np.int64).max) - 1, 2)),
])
def test_exact_median_empty_even_odd_overflow_safe(values, expected):
    assert exact_median_us(np.asarray(values, np.int64)) == expected
