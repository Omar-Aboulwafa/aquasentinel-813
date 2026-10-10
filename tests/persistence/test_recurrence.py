from datetime import UTC, datetime, timedelta

import numpy as np
import pytest

from aquasentinel.persistence.recurrence import gap_us, validate_count_capacity, validate_gap_us


@pytest.mark.parametrize("states,streak,count,q,recurrent", [
    ([(True, True)], 1, 0, False, False),
    ([(False, False), (True, True)], 1, 0, False, False),
    ([(True, True), (True, True)], 2, 1, True, True),
    ([(True, True), (False, False), (True, True)], 2, 1, True, True),
    ([(True, True), (True, False), (True, True)], 1, 2, True, False),
    ([(True, True), (True, False)], 0, 1, True, False),
    ([(True, True), (False, False)], 0, 0, False, False),
    ([(True, True)] * 3, 3, 2, True, True),
    ([(True, True)] + [(False, False)] * 3 + [(True, True)], 2, 1, True, True),
    ([(True, False), (True, True), (False, False), (True, True)], 2, 2, True, True),
])
def test_core_valid_observation_recurrence(make_sequence, compute, states, streak, count, q, recurrent):
    sequence = make_sequence(states)
    result = compute(sequence)
    assert np.all(result.current_streak_count == streak)
    assert np.all(result.prior_valid_observation_count == count)
    assert np.all(result.persistence_evaluable_mask == q)
    assert np.all(result.recurrent_candidate_mask == recurrent)
    result.validate(sequence[0], temporal_parents=sequence[1])


@pytest.mark.parametrize("prior_pixel,expected", [((1, 1), True), ((1, 0), False), ((0, 0), False)])
def test_exact_pixel_not_adjacent_diagonal_or_buffer(make_sequence, compute, prior_pixel, expected):
    prior, target = np.zeros((3, 3), bool), np.zeros((3, 3), bool)
    prior[prior_pixel] = True
    target[1, 1] = True
    result = compute(make_sequence([(True, prior), (True, target)], shape=(3, 3)))
    assert result.recurrent_candidate_mask[1, 1] == expected
    assert result.recurrent_candidate_mask.sum() == int(expected)
    assert np.array_equal(result.target_candidate_mask, target)


@pytest.mark.parametrize("states,a,b,c,coverage,fraction", [
    ([(True, False)], 0, 0, 0, None, None),
    ([(True, True)], 6, 0, 0, 0.0, None),
    ([(False, False), (True, True)], 6, 0, 0, 0.0, None),
    ([(True, False), (True, True)], 6, 6, 0, 1.0, 0.0),
    ([(True, True), (True, True)], 6, 6, 6, 1.0, 1.0),
])
def test_global_denominators_and_empty_vs_zero(make_sequence, compute, states, a, b, c,
                                               coverage, fraction):
    statistics = compute(make_sequence(states)).statistics
    assert statistics.target_candidate_count == a
    assert statistics.persistence_evaluable_target_candidate_count == b
    assert statistics.recurrent_candidate_count == c
    assert statistics.candidate_history_coverage == coverage
    assert statistics.recurrence_fraction == fraction
    assert sum(statistics.streak_histogram_on_target_candidates.values()) == a


def test_partial_support_exact_counts(make_sequence, compute):
    p = np.array([[True, True, False], [False, False, False]])
    c = np.array([[True, False, False], [False, False, False]])
    result = compute(make_sequence([(p, c), (True, True)]))
    s = result.statistics
    assert (s.target_policy_support_count, s.persistence_evaluable_pixel_count) == (6, 2)
    assert (s.target_candidate_count, s.persistence_evaluable_target_candidate_count,
            s.recurrent_candidate_count, s.target_candidates_without_prior_history) == (6, 2, 1, 4)
    assert s.candidate_history_coverage == 2 / 6
    assert s.recurrence_fraction == 1 / 2
    assert s.streak_histogram_on_target_candidates == {"1": 5, "2": 1}


def test_exact_subsecond_gap_skipped_span_and_break(make_sequence, compute):
    times = [datetime(2023, 4, 1, tzinfo=UTC) + timedelta(microseconds=v) for v in (0, 3, 7, 11)]
    result = compute(make_sequence([(True, True), (True, False), (False, False), (True, True)],
                                   times=times))
    assert np.all(result.previous_valid_observation_gap_us == 8)  # Noncandidate still supported.
    assert np.all(result.current_streak_span_us == 0)
    result = compute(make_sequence([(True, True), (False, False), (True, True), (True, True)],
                                   times=times))
    assert np.all(result.previous_valid_observation_gap_us == 4)
    assert np.all(result.current_streak_span_us == 11)
    assert np.all(result.current_streak_count == 3)


def test_long_gap_has_no_cutoff(make_sequence, compute):
    times = [datetime(2023, 4, 1, tzinfo=UTC), datetime(2030, 4, 1, tzinfo=UTC)]
    result = compute(make_sequence(times=times))
    assert result.current_streak_count[0, 0] == 2
    assert result.current_streak_span_us[0, 0] == 220924800000000
    assert result.previous_valid_observation_gap_us[0, 0] == gap_us(times[1], times[0])


def test_timing_and_count_dtype_and_sentinels(make_sequence, compute):
    p = np.array([[True, True, False], [True, True, True]])
    c = np.array([[True, False, False], [True, True, True]])
    result = compute(make_sequence([(False, False), (p, c)]))
    for name in ("prior_valid_observation_count", "current_streak_count"):
        assert getattr(result, name).dtype == np.uint32
    for name in ("persistence_evaluable_mask", "recurrent_candidate_mask"):
        assert getattr(result, name).dtype == bool
    for name in ("previous_valid_observation_gap_us", "current_streak_span_us"):
        assert getattr(result, name).dtype == np.int64
    assert np.all(result.previous_valid_observation_gap_us == -1)
    assert np.all(result.current_streak_span_us[c] == 0)
    assert np.all(result.current_streak_span_us[~c] == -1)
    assert np.all(result.current_streak_count[~p] == 0)


@pytest.mark.parametrize("value", [0, 1, int(np.iinfo(np.uint32).max)])
def test_count_legal_boundary(value):
    validate_count_capacity(value)


@pytest.mark.parametrize("value", [-1, True, 1.0, int(np.iinfo(np.uint32).max) + 1])
def test_count_overflow_or_invalid_type(value):
    with pytest.raises(ValueError):
        validate_count_capacity(value)


@pytest.mark.parametrize("value", [0, 1, int(np.iinfo(np.int64).max)])
def test_microseconds_legal_boundary(value):
    assert validate_gap_us(value) == value


@pytest.mark.parametrize("value", [-1, True, 1.0, int(np.iinfo(np.int64).max) + 1])
def test_microseconds_overflow_or_invalid_type(value):
    with pytest.raises(ValueError):
        validate_gap_us(value)


def test_utc_microsecond_arithmetic_avoids_float_epoch():
    earlier = datetime(9998, 1, 1, 0, 0, 0, 999999, tzinfo=UTC)
    later = earlier + timedelta(days=100, seconds=4, microseconds=1)
    assert gap_us(later, earlier) == 8640004000001
    with pytest.raises(ValueError):
        gap_us(earlier, later)


@pytest.mark.parametrize("seed", range(12))
def test_randomized_sequence_against_independent_scalar_contract(make_sequence, compute, seed):
    rng = np.random.default_rng(seed)
    states = []
    for _ in range(7):
        p = rng.random((2, 3)) > 0.35
        c = p & (rng.random((2, 3)) > 0.4)
        states.append((p, c))
    times = [datetime(2023, 4, 1, tzinfo=UTC) + timedelta(microseconds=int(v))
             for v in np.cumsum(rng.integers(1, 2000000, 7))]
    result = compute(make_sequence(states, times=times))
    for row, col in np.ndindex((2, 3)):
        target_p, target_c = (bool(m[row, col]) for m in states[-1])
        history = [i for i in range(6) if states[i][0][row, col]] if target_p else []
        assert result.prior_valid_observation_count[row, col] == len(history)
        assert result.persistence_evaluable_mask[row, col] == bool(history)
        streak_indices = [6] if target_c else []
        if target_c:
            for i in reversed(history):
                if not states[i][1][row, col]:
                    break
                streak_indices.append(i)
        assert result.current_streak_count[row, col] == len(streak_indices)
        assert result.recurrent_candidate_mask[row, col] == (len(streak_indices) >= 2)
        expected_gap = gap_us(times[-1], times[history[-1]]) if history else -1
        expected_span = gap_us(times[-1], times[streak_indices[-1]]) if streak_indices else -1
        assert result.previous_valid_observation_gap_us[row, col] == expected_gap
        assert result.current_streak_span_us[row, col] == expected_span
