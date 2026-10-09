from copy import deepcopy
from dataclasses import replace
from datetime import UTC, datetime, timedelta, timezone
from statistics import median

import numpy as np
import pytest

from aquasentinel.features.spectral import FEATURE_ORDER

from .conftest import refresh


@pytest.mark.parametrize(
    "history,target",
    [
        ([1, 2, 3, 4, 5], 6),
        ([1, 2, 4, 8], -3),
        ([-10, -4, -2, -1, 10], -7),
        ([1, 2, 3, 4, 10000], 9),
    ],
)
def test_independent_scalar_median_mad_signed_results(make_collection, run, history, target):
    scenes, registry, _ = make_collection(history, target_value=target)
    result = run(scenes, registry, minimum_observations=3)
    centre = median(history)
    scale = 1.4826 * median([abs(x - centre) for x in history])
    for name in FEATURE_ORDER:
        feature = result.results[name]
        np.testing.assert_array_equal(feature.baseline_centre, centre)
        np.testing.assert_array_equal(feature.baseline_scale, scale)
        np.testing.assert_array_equal(feature.deviation, target - centre)
        np.testing.assert_allclose(
            feature.robust_standardized_anomaly, (target - centre) / scale, rtol=1e-7
        )
        assert feature.baseline_centre.dtype == feature.baseline_scale.dtype == np.float64
        assert feature.deviation.dtype == np.float64
        assert feature.robust_standardized_anomaly.dtype == np.float32
        assert feature.baseline_observation_count.dtype == np.uint32


@pytest.mark.parametrize(
    "history,target,expected",
    [
        ([1, 2, 3, 4, 5], -1, 0),
        ([1, 2, 3, 4, 5], 10, 1),
        ([1, 2, 2, 4, 5], 2, 0.4),
        ([2, 2, 2, 2, 2], 2, 0.5),
        ([1, 2, 3, 4, 5], 3, 0.5),
    ],
)
def test_exact_midrank(make_collection, run, history, target, expected):
    scenes, registry, _ = make_collection(history, target_value=target)
    result = run(scenes, registry).results["ndci_like"]
    np.testing.assert_allclose(result.empirical_rank, expected)
    assert result.rank_valid_mask.all()
    assert np.all((result.empirical_rank >= 0) & (result.empirical_rank <= 1))


@pytest.mark.parametrize("target", [2, 10, -1])
def test_zero_mad_preserves_baseline_deviation_rank_not_anomaly(make_collection, run, target):
    scenes, registry, _ = make_collection([2] * 5, target_value=target)
    feature = run(scenes, registry).results["ndci_like"]
    assert feature.baseline_valid_mask.all() and feature.rank_valid_mask.all()
    assert not feature.anomaly_valid_mask.any()
    assert np.isnan(feature.robust_standardized_anomaly).all()
    np.testing.assert_array_equal(feature.baseline_scale, 0)
    np.testing.assert_array_equal(feature.deviation, target - 2)
    assert feature.diagnostics.zero_MAD_count == 6


@pytest.mark.parametrize("target,overflow", [(6e-40, False), (1.0, True)])
def test_tiny_positive_scale_no_floor_and_float32_overflow(make_collection, run, target, overflow):
    history = [1e-40, 2e-40, 3e-40, 4e-40, 5e-40]
    scenes, registry, _ = make_collection(history, target_value=target)
    feature = run(scenes, registry).results["ndci_like"]
    assert (feature.baseline_scale > 0).all()
    assert (feature.baseline_scale < 1e-39).all()
    assert feature.anomaly_valid_mask.all() != overflow
    assert feature.diagnostics.anomaly_numeric_rejection_count == (6 if overflow else 0)
    assert feature.rank_valid_mask.all()
    if overflow:
        assert np.isnan(feature.robust_standardized_anomaly).all()


def test_feature_specific_date_varying_support(make_collection, run):
    scenes, registry, _ = make_collection()
    reference = deepcopy(scenes[0])
    reference.feature_valid_masks["ndci_like"][0, 0] = False
    reference = refresh(reference)
    scenes[0] = reference
    registry.derived_products[reference.product_id] = reference.provenance
    result = run(scenes, registry)
    assert result.results["ndci_like"].baseline_observation_count[0, 0] == 4
    assert not result.results["ndci_like"].baseline_valid_mask[0, 0]
    assert result.results["mci_like"].baseline_observation_count[0, 0] == 5
    assert result.results["mci_like"].baseline_valid_mask[0, 0]
    assert result.results["ndci_like"].baseline_valid_mask[1, 1]


@pytest.mark.parametrize("reference_count", [0, 1, 2, 4])
def test_sparse_global_history_is_valid_empty(make_collection, run, reference_count):
    scenes, registry, _ = make_collection(list(range(reference_count)))
    result = run(scenes, registry)
    for feature in result.results.values():
        np.testing.assert_array_equal(feature.baseline_observation_count, reference_count)
        assert feature.diagnostics.insufficient_history_count == 6
        assert not feature.baseline_valid_mask.any()
        assert np.isnan(feature.baseline_centre).all()
        assert feature.statistics.centre.minimum is None
        assert feature.statistics.centre.fraction_of_target_feature_support == 0


@pytest.mark.parametrize("empty_target", [True, False])
def test_empty_target_or_no_historical_pixel_support(make_collection, run, empty_target):
    empty = np.zeros((2, 3), bool)
    scenes, registry, _ = make_collection(
        target_mask=empty if empty_target else None, reference_masks=[empty] * 5
    )
    result = run(scenes, registry)
    assert result.reference_product_ids == tuple(scene.product_id for scene in scenes[:-1])
    assert result.provenance.source_ids == (scenes[-1].product_id, *result.reference_product_ids)
    for feature in result.results.values():
        assert not feature.baseline_valid_mask.any()
        assert not feature.baseline_observation_count.any()
        assert feature.statistics.centre.minimum is None
        assert feature.statistics.centre.fraction_of_target_feature_support == (
            None if empty_target else 0
        )


def test_target_invalid_history_valid_never_expands_support(make_collection, run):
    mask = np.ones((2, 3), bool)
    mask[0, 0] = False
    scenes, registry, _ = make_collection(target_mask=mask)
    output = run(scenes, registry)
    for feature in output.results.values():
        for support in (
            feature.baseline_valid_mask,
            feature.anomaly_valid_mask,
            feature.rank_valid_mask,
        ):
            assert not np.any(support & ~mask)
        assert feature.baseline_observation_count[0, 0] == 0
        for array in (
            feature.baseline_centre,
            feature.baseline_scale,
            feature.deviation,
            feature.robust_standardized_anomaly,
            feature.empirical_rank,
        ):
            assert np.isnan(array[0, 0])


@pytest.mark.parametrize("minimum", [True, False, 2, 0, -3, 5.0, "5", 2**32])
def test_invalid_minimum_rejected(collection, run, minimum):
    scenes, registry, _ = collection
    with pytest.raises(ValueError, match="minimum_observations"):
        run(scenes, registry, minimum_observations=minimum)


@pytest.mark.parametrize(
    "bounds",
    [
        {"reference_start": datetime(2023, 3, 1, tzinfo=UTC).replace(tzinfo=None)},
        {"reference_end": datetime(2023, 4, 1, tzinfo=UTC).replace(tzinfo=None)},
        {"reference_end": datetime(2023, 5, 1, tzinfo=UTC)},
        {
            "reference_start": datetime(2023, 4, 2, tzinfo=UTC),
            "reference_end": datetime(2023, 4, 1, tzinfo=UTC),
        },
        {"reference_start": "2023-03-01"},
    ],
)
def test_invalid_reference_bounds(collection, run, bounds):
    scenes, registry, _ = collection
    with pytest.raises(ValueError):
        run(scenes, registry, **bounds)


def test_half_open_period_target_exclusion_and_equivalent_utc(collection, run):
    scenes, registry, _ = collection
    end = scenes[3].acquired_at
    result = run(scenes, registry, minimum_observations=3, reference_end=end)
    assert result.reference_product_ids == tuple(scene.product_id for scene in scenes[:3])
    assert scenes[-1].product_id not in result.reference_product_ids
    assert all((r.baseline_observation_count == 3).all() for r in result.results.values())
    shifted = run(
        scenes,
        registry,
        minimum_observations=3,
        reference_start=datetime(2023, 3, 1, 4, tzinfo=timezone(timedelta(hours=4))),
        reference_end=end.astimezone(timezone(timedelta(hours=4))),
    )
    assert shifted.product_id == result.product_id
    explicit = run(scenes, registry, reference_end=scenes[-1].acquired_at)
    assert explicit.product_id == run(scenes, registry).product_id


@pytest.mark.parametrize("case", ["missing", "duplicate", "same_time", "malformed"])
def test_invalid_temporal_collection(collection, run, case):
    scenes, registry, _ = collection
    target_id = scenes[-1].product_id
    if case == "missing":
        scenes = scenes[:-1]
    elif case == "duplicate":
        scenes = [*scenes, scenes[0]]
    elif case == "same_time":
        scenes = [*scenes, replace(scenes[0], product_id="spectral:" + "f" * 64)]
    else:
        scenes = [*scenes, object()]
    with pytest.raises((ValueError, TypeError)):
        run(scenes, registry, target_product_id=target_id)
