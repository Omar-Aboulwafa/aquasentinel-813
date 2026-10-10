from copy import deepcopy
from dataclasses import replace
from datetime import UTC, datetime, timedelta, timezone

import numpy as np
import pytest

from aquasentinel.geometry import extract_hab_anomaly_geometry
from aquasentinel.persistence import compute_hab_persistence
from aquasentinel.persistence.recurrence import (
    ARRAY_DTYPES,
    comparison_contract,
    output_content_fingerprint,
)
from aquasentinel.temporal.models import ReferencePeriod

from .conftest import reidentify


def run(scenes, parents, target=None):
    return compute_hab_persistence(scenes, temporal_parents=parents,
                                   target_geometry_product_id=target or scenes[-1].product_id)


@pytest.mark.parametrize("kind", ["empty", "missing_target", "duplicate_id", "duplicate_time",
                                  "naive", "not_latest", "future", "bad_type", "wrong_mapping"])
def test_invalid_sequence_rejected(sequence, kind):
    scenes, parents = deepcopy(sequence)
    target = scenes[-1].product_id
    if kind == "empty":
        scenes = []
    elif kind == "missing_target":
        target = "missing"
    elif kind == "duplicate_id":
        scenes = [*scenes, scenes[0]]
    elif kind == "duplicate_time":
        scenes[0] = replace(scenes[0], target_acquired_at=scenes[-1].target_acquired_at)
    elif kind == "naive":
        scenes[0] = replace(scenes[0], target_acquired_at=datetime(2023, 4, 1, tzinfo=UTC).replace(tzinfo=None))
    elif kind in {"not_latest", "future"}:
        target = scenes[0].product_id
    elif kind == "bad_type":
        scenes[0] = object()
    else:
        parents = []
    with pytest.raises((ValueError, TypeError)):
        run(scenes, parents, target)


def test_equivalent_timezone_duplicate_rejected(sequence):
    scenes, parents = sequence
    duplicate = replace(scenes[0], product_id="different",
                        target_acquired_at=scenes[0].target_acquired_at.astimezone(
                            timezone(timedelta(hours=4))))
    with pytest.raises(ValueError, match="Duplicate"):
        run([*scenes, duplicate], parents)


@pytest.mark.parametrize("kind", ["missing", "wrong_id", "wrong_type"])
def test_temporal_witness_required(sequence, kind):
    scenes, parents = deepcopy(sequence)
    key = scenes[0].parent_temporal_product_id
    if kind == "missing":
        del parents[key]
    elif kind == "wrong_id":
        parents[key] = parents[scenes[-1].parent_temporal_product_id]
    else:
        parents[key] = object()
    with pytest.raises((ValueError, TypeError), match="witness"):
        run(scenes, parents)


@pytest.mark.parametrize("kind", ["grid", "version", "policy", "corrupt_parent", "corrupt_geometry"])
def test_upstream_validation_not_weakened(sequence, kind):
    scenes, parents = deepcopy(sequence)
    scene = scenes[0]
    if kind == "grid":
        scenes[0] = replace(scene, grid=replace(scene.grid, grid_id="different"))
    elif kind == "version":
        scenes[0] = replace(scene, provenance=replace(scene.provenance, processing_version="as105-v2"))
    elif kind == "policy":
        scene.processing_parameters["identity"]["policy"]["minimum_family_votes"] = 1
    elif kind == "corrupt_parent":
        parents[scene.parent_temporal_product_id].results["ndci_like"].empirical_rank[0, 0] = 1.1
    else:
        scene.candidate_mask[0, 0] = False
    with pytest.raises(ValueError):
        run(scenes, parents)


@pytest.mark.parametrize("field", [
    "processing_version", "feature_order", "formulas", "reference_product_ids",
    "reference_acquired_at", "reference_period", "minimum_observations", "grid", "algorithm",
    "as103_version", "as102_version", "catalog", "collection", "aoi_geometry_digest",
    "bands", "resampling", "mask_policy", "interpolation_support_policy", "decoding",
    "mgrs_tile", "relative_orbit", "pc_processing_baseline",
])
def test_comparison_contract_consumes_each_frozen_field(sequence, field):
    # Unit-test projection independently of upstream validity. Whole API never bypasses validation.
    parent = next(iter(sequence[1].values()))
    changed = deepcopy(parent)
    identity = changed.processing_parameters["identity"]
    descriptor = identity["compatibility"][0]
    if field in descriptor["contract"]:
        descriptor["contract"][field] = "different"
    elif field in {"mgrs_tile", "relative_orbit"}:
        descriptor["observation"][field] = "different"
    elif field == "pc_processing_baseline":
        descriptor[field] = "05.10"
    else:
        identity[field] = "different"
    assert comparison_contract(parent) != comparison_contract(changed)


@pytest.mark.parametrize("field", ["period", "reference_id", "reference_time", "catalog", "tile",
                                   "orbit", "baseline", "aoi", "collection", "minimum"])
def test_individually_valid_but_incompatible_temporal_contexts_fail(sequence, field):
    scenes, parents = deepcopy(sequence)
    parent = parents.pop(scenes[0].parent_temporal_product_id)
    identity = parent.processing_parameters["identity"]
    if field == "period":
        parent = replace(parent, reference_period=ReferencePeriod(
            datetime(2023, 2, 28, tzinfo=UTC), datetime(2023, 4, 1, tzinfo=UTC)))
    elif field == "reference_id":
        parent = replace(parent, reference_product_ids=("spectral:" + "1" * 64,
                                                       *parent.reference_product_ids[1:]))
    elif field == "reference_time":
        parent = replace(parent, reference_acquired_at=(parent.reference_acquired_at[0]
                         - timedelta(minutes=1), *parent.reference_acquired_at[1:]))
    elif field == "minimum":
        # Change to 4, updating redundant diagnostics to remain model-valid.
        from dataclasses import asdict

        from aquasentinel.temporal.models import result_diagnostics

        identity["minimum_observations"] = 4
        results = {n: replace(r, diagnostics=result_diagnostics(r, 4))
                   for n, r in parent.results.items()}
        parent = replace(parent, results=results)
        parent.processing_parameters["diagnostics"] = {n: asdict(r.diagnostics)
                                                       for n, r in results.items()}
    else:
        for d in identity["compatibility"]:
            if field == "catalog":
                d["contract"]["catalog"] = "https://catalog.example/stac/"
            elif field == "collection":
                d["contract"]["collection"] = "different-collection"
            elif field == "tile":
                d["observation"]["mgrs_tile"] = "40RBP"
            elif field == "orbit":
                d["observation"]["relative_orbit"] = 21
            elif field == "aoi":
                d["contract"]["aoi_geometry_digest"] = "b" * 64
            else:
                d["pc_processing_baseline"] = "05.10"
                d["contract"]["decoding"]["processing_baseline"] = "05.10"
    parent = reidentify(parent)  # Explicit proof of whole upstream model validity.
    scenes[0] = extract_hab_anomaly_geometry(parent)
    parents[parent.product_id] = parent
    with pytest.raises(ValueError, match="comparison contexts"):
        run(scenes, parents)


@pytest.mark.parametrize("field", list(ARRAY_DTYPES))
@pytest.mark.parametrize("rehash", [False, True])
def test_array_tampering_even_rehashed_is_rejected(sequence, compute, field, rehash):
    result = deepcopy(compute(sequence))
    array = getattr(result, field)
    array[0, 0] = not array[0, 0] if array.dtype == bool else array[0, 0] + 1
    if rehash:
        result.processing_parameters["output_content_fingerprint"] = output_content_fingerprint(
            vars(result))
        result = replace(result, provenance=replace(result.provenance,
                                                   parameters=deepcopy(result.processing_parameters)))
    with pytest.raises(ValueError):
        result.validate(sequence[0], temporal_parents=sequence[1])


@pytest.mark.parametrize("kind", ["dtype", "shape"])
@pytest.mark.parametrize("field", list(ARRAY_DTYPES))
def test_output_array_contracts(sequence, compute, kind, field):
    result = compute(sequence)
    array = getattr(result, field)
    invalid = array[:-1] if kind == "shape" else array.astype(np.float64)
    result = replace(result, **{field: invalid})
    with pytest.raises(ValueError):
        result.validate(sequence[0], temporal_parents=sequence[1])


@pytest.mark.parametrize("kind", ["statistics", "region", "prior_evidence", "parameters", "id",
                                  "parents", "times", "target_time", "grid"])
def test_tampered_metadata_even_with_recomputed_hash(sequence, compute, kind):
    result = deepcopy(compute(sequence))
    if kind == "statistics":
        result = replace(result, statistics=replace(result.statistics, target_candidate_count=100))
    elif kind == "region":
        result = replace(result, regions=(replace(result.regions[0], recurrence_fraction=0.5),))
    elif kind == "prior_evidence":
        r = result.regions[0]
        result = replace(result, regions=(replace(r, prior_observations=(replace(
            r.prior_observations[0], candidate_overlap_pixel_count=0),)),))
    elif kind == "parameters":
        result.processing_parameters["identity"]["policy"]["recurrence_minimum_streak"] = 1
    elif kind == "id":
        result = replace(result, product_id="wrong")
    elif kind == "parents":
        result = replace(result, parent_geometry_product_ids=tuple(reversed(
            result.parent_geometry_product_ids)))
    elif kind == "times":
        result = replace(result, acquired_at=tuple(reversed(result.acquired_at)))
    elif kind == "target_time":
        result = replace(result, target_acquired_at=result.target_acquired_at + timedelta(seconds=1))
    else:
        result = replace(result, grid=replace(result.grid, grid_id="different"))
    result.processing_parameters["output_content_fingerprint"] = output_content_fingerprint(vars(result))
    result = replace(result, provenance=replace(result.provenance,
                                               parameters=deepcopy(result.processing_parameters)))
    with pytest.raises(ValueError):
        result.validate(sequence[0], temporal_parents=sequence[1])


@pytest.mark.parametrize("field,value", [
    ("source_ids", ("pc:shortcut",)), ("source_ids", ("temporal:shortcut",)),
    ("source_ids", ()), ("product_type", "wrong"), ("processing_version", "as106-v2"),
    ("product_id", "wrong"), ("parameters", {}), ("created_at", datetime(2026, 10, 10, tzinfo=UTC).replace(tzinfo=None)),
])
def test_provenance_tampering_rejected(sequence, compute, field, value):
    result = compute(sequence)
    result = replace(result, provenance=replace(result.provenance, **{field: value}))
    with pytest.raises(ValueError):
        result.validate(sequence[0], temporal_parents=sequence[1])


@pytest.mark.parametrize("field", ["regions", "prior_observations", "median"])
def test_typed_region_evidence_required(sequence, compute, field):
    from aquasentinel.persistence.models import ExactMicroseconds

    result = compute(sequence)
    r = result.regions[0]
    if field == "regions":
        result = replace(result, regions=list(result.regions))
    elif field == "prior_observations":
        result = replace(result, regions=(replace(r, prior_observations=list(r.prior_observations)),))
    else:
        # Same serialized scientific number but wrong declared dataclass type must be rejected.
        assert isinstance(r.median_current_streak_span_us, ExactMicroseconds)
        from dataclasses import make_dataclass

        other = make_dataclass("NotExactMicroseconds", ["numerator_microseconds", "denominator"])
        value = r.median_current_streak_span_us
        result = replace(result, regions=(replace(r, median_current_streak_span_us=other(
            value.numerator_microseconds, value.denominator)),))
    with pytest.raises(ValueError):
        result.validate(sequence[0], temporal_parents=sequence[1])
