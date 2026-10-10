from copy import deepcopy
from dataclasses import replace

import numpy as np
import pytest

from aquasentinel.features.spectral import FEATURE_ORDER
from aquasentinel.geometry import extract_hab_anomaly_geometry
from aquasentinel.geometry.hab import FAMILY_MEMBERS, FAMILY_ORDER, RANK_THRESHOLD

from .conftest import refresh_parent


@pytest.mark.parametrize(
    "history,target,expected_rank,passes",
    [
        pytest.param((1, 2, 3, 4, 6), 5, np.float32(0.8), False, id="four-below-no-ties"),
        pytest.param((1, 2, 3, 4, 5), 6, np.float32(1.0), True, id="five-below-no-ties"),
        pytest.param((1, 2, 3, 4, 5), 5, np.float32(0.9), True, id="four-below-one-tie"),
        pytest.param((1, 2, 3, 5, 5), 5, np.float32(0.8), False, id="three-below-two-ties"),
    ],
)
def test_five_history_rank_granularity(
    make_five_history_parent, history, target, expected_rank, passes
):
    parent = make_five_history_parent(history, target)
    assert parent.processing_parameters["identity"]["minimum_observations"] == 5
    assert len(parent.reference_product_ids) == 5
    for result in parent.results.values():
        assert result.rank_valid_mask.all()
        assert np.all(result.baseline_observation_count == 5)
        assert result.empirical_rank.dtype == np.float32
        assert np.all(result.empirical_rank == expected_rank)
        assert np.all(result.deviation > 0)
    scene = extract_hab_anomaly_geometry(parent)
    assert all(bool(mask.all()) is passes for mask in scene.feature_evidence_masks.values())
    assert bool(scene.candidate_mask.all()) is passes
    assert scene.candidate_analysis_support_mask.all()
    assert RANK_THRESHOLD == np.float32(0.90)


@pytest.mark.parametrize(
    "rank,passes",
    [
        (np.float32(0.90), True),
        (np.nextafter(np.float32(0.90), np.float32(-np.inf)), False),
        (np.float32(1), True),
        (np.float32(0.5), False),
    ],
)
def test_exact_float32_boundary(make_parent, rank, passes):
    ranks = {n: rank for n in FEATURE_ORDER}
    scene = extract_hab_anomaly_geometry(make_parent(ranks=ranks))
    assert bool(scene.candidate_mask.all()) is passes
    assert scene.processing_parameters["identity"]["policy"]["rank_threshold"] == {
        "nominal": 0.9,
        "nominal_decimal": "0.90",
        "dtype": "float32",
        "value": 0.8999999761581421,
        "ieee754_big_endian_hex": "3f666666",
    }


@pytest.mark.parametrize(
    "deviation,passes", [(1.0, True), (0.0, False), (-0.0, False), (-1.0, False)]
)
def test_strict_positive_direction(make_parent, deviation, passes):
    p = make_parent(deviations={n: deviation for n in FEATURE_ORDER})
    assert bool(extract_hab_anomaly_geometry(p).candidate_mask.all()) is passes


@pytest.mark.parametrize(
    "qualifying,votes,candidate",
    [
        (("ndci_like", "red_edge_red_ratio"), 1, False),
        (("ndci_like", "green_red_ratio"), 2, True),
        (("green_red_ratio", "green_blue_ratio"), 2, False),
        (("mci_like",), 1, False),
        (("mci_like", "red_edge2_red_ratio", "green_blue_ratio"), 3, True),
        (FEATURE_ORDER, 5, True),
        ((), 0, False),
    ],
)
def test_frozen_family_agreement(make_parent, qualifying, votes, candidate):
    scene = extract_hab_anomaly_geometry(make_parent(qualifying=qualifying))
    assert np.all(scene.family_vote_count == votes)
    assert bool(scene.candidate_mask.all()) is candidate
    assert FAMILY_MEMBERS[FAMILY_ORDER[0]] == ("ndci_like", "red_edge_red_ratio")


def test_zero_mad_votes_without_z(make_parent):
    p = make_parent(scale=0)
    assert not p.results["ndci_like"].anomaly_valid_mask.any()
    assert extract_hab_anomaly_geometry(p).candidate_mask.all()


def test_huge_z_alone_cannot_vote(make_parent):
    p = make_parent(qualifying=(), scale=1e-20)
    assert p.results["ndci_like"].robust_standardized_anomaly.min() > 1e10
    assert not extract_hab_anomaly_geometry(p).candidate_mask.any()


def test_invalid_rank_cannot_vote_and_support_does_not_require_six_features(make_parent):
    supports = {n: np.zeros((3, 4), bool) for n in FEATURE_ORDER}
    supports["ndci_like"][0, 0] = supports["green_red_ratio"][0, 0] = True
    p = make_parent(supports=supports)
    scene = extract_hab_anomaly_geometry(p)
    assert scene.candidate_mask.sum() == 1
    assert scene.candidate_analysis_support_mask.sum() == 1
    assert scene.statistics.candidate_fraction_of_policy_support == 1
    assert not scene.feature_evidence_masks["mci_like"].any()
    assert np.isnan(p.results["mci_like"].empirical_rank).all()


def test_denominator_uses_availability_not_votes(make_parent):
    supports = {n: np.zeros((3, 4), bool) for n in FEATURE_ORDER}
    supports["ndci_like"][0, :2] = True
    supports["green_red_ratio"][0, :2] = True
    ranks = {n: np.full((3, 4), 0.5, np.float32) for n in FEATURE_ORDER}
    ranks["ndci_like"][0, 0] = ranks["green_red_ratio"][0, 0] = RANK_THRESHOLD
    scene = extract_hab_anomaly_geometry(make_parent(supports=supports, ranks=ranks))
    assert scene.statistics.candidate_analysis_support_count == 2
    assert scene.statistics.candidate_pixel_count == 1
    assert scene.statistics.candidate_fraction_of_policy_support == 0.5
    assert scene.statistics.family_vote_histogram_on_policy_support["0"] == 1


@pytest.mark.parametrize("empty_water", [False, True])
def test_empty_policy_support(make_parent, empty_water):
    supports = {n: np.zeros((3, 4), bool) for n in FEATURE_ORDER}
    p = make_parent(supports=supports, water=np.full((3, 4), not empty_water, bool))
    s = extract_hab_anomaly_geometry(p)
    assert s.statistics.candidate_fraction_of_policy_support is None
    assert s.statistics.region_count == 0 and s.regions == ()
    assert s.statistics.median_region_pixels is None
    assert s.diagnostics.features["ndci_like"].evidence_fraction_of_feature_support is None


def test_eligible_zero_candidates_and_all_candidates(make_parent):
    none = extract_hab_anomaly_geometry(make_parent(qualifying=()))
    assert none.statistics.candidate_fraction_of_policy_support == 0.0
    all_scene = extract_hab_anomaly_geometry(make_parent(qualifying=FEATURE_ORDER))
    assert all_scene.statistics.candidate_fraction_of_policy_support == 1.0
    assert all_scene.statistics.candidate_pixel_count == 12
    assert all_scene.regions[0].maximum_family_votes == 5
    assert all_scene.statistics.family_vote_histogram_on_candidates["5"] == 12


def test_candidate_and_family_masks_cannot_expand_water(make_parent):
    water = np.eye(4, dtype=bool)
    s = extract_hab_anomaly_geometry(make_parent(shape=water.shape, water=water))
    for masks in (
        s.feature_support_masks,
        s.feature_evidence_masks,
        s.family_available_masks,
        s.family_evidence_masks,
    ):
        assert all(not (mask & ~water).any() for mask in masks.values())
    assert not (s.candidate_mask & ~s.candidate_analysis_support_mask).any()
    assert np.array_equal(s.candidate_mask, water)


def test_irrelevant_valid_parent_mutation_keeps_identity(parent):
    before = extract_hab_anomaly_geometry(parent)
    changed = deepcopy(parent)
    for r in changed.results.values():
        r.baseline_centre[r.baseline_valid_mask] = 10
        r.baseline_scale[r.baseline_valid_mask] = 0
    changed = refresh_parent(changed)
    changed = replace(
        changed,
        provenance=replace(
            changed.provenance, created_at=changed.provenance.created_at.replace(year=2025)
        ),
    )
    changed.validate()
    after = extract_hab_anomaly_geometry(changed)
    assert before.product_id == after.product_id
    assert before.processing_parameters == after.processing_parameters
    assert np.array_equal(before.candidate_mask, after.candidate_mask)


def test_region_summaries_use_feature_specific_support_and_finite_values(make_parent):
    supports = {n: np.ones((3, 4), bool) for n in FEATURE_ORDER}
    supports["mci_like"][:] = False
    supports["green_blue_ratio"][:] = False
    supports["green_blue_ratio"][0, :2] = True
    deviations = {n: np.arange(1, 13).reshape(3, 4) for n in FEATURE_ORDER}
    scene = extract_hab_anomaly_geometry(make_parent(supports=supports, deviations=deviations))
    region = scene.regions[0]
    missing = region.feature_summaries["mci_like"]
    assert missing.deviation.count == 0 and missing.deviation.median is None
    partial = region.feature_summaries["green_blue_ratio"].deviation
    assert (partial.count, partial.minimum, partial.median, partial.maximum) == (2, 1.0, 1.5, 2.0)
    assert region.family_evidence_pixel_counts["red_edge_b5_vs_red"] == 12
    assert region.feature_summaries["ndci_like"].empirical_rank.minimum == float(RANK_THRESHOLD)


@pytest.mark.parametrize("extreme", [1e308, -1e308])
def test_finite_regional_median_does_not_overflow(make_parent, extreme):
    ranks = {n: np.full((3, 4), 0.5, np.float32) for n in FEATURE_ORDER}
    ranks["mci_like"][0, :2] = ranks["green_red_ratio"][0, :2] = RANK_THRESHOLD
    deviations = {n: np.ones((3, 4), np.float64) for n in FEATURE_ORDER}
    deviations["ndci_like"][0, :2] = extreme
    parent = make_parent(ranks=ranks, deviations=deviations)
    scene = extract_hab_anomaly_geometry(parent)
    summary = scene.regions[0].feature_summaries["ndci_like"].deviation
    assert summary.count == 2 and summary.median == extreme
