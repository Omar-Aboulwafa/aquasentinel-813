from copy import deepcopy
from dataclasses import replace

import numpy as np
import pytest
from rasterio import Affine

from aquasentinel.temporal.baseline import temporal_product_id

from .conftest import rewrite_parent


@pytest.mark.parametrize(
    "corruption",
    [
        "shape",
        "dtype",
        "mask_dtype",
        "mask_shape",
        "expand",
        "count_dtype",
        "count_value",
        "below_minimum",
        "valid_nan",
        "invalid_finite",
        "negative_scale",
        "rank_range",
        "rank_mask",
        "zero_anomaly",
        "anomaly_value",
        "statistics",
        "diagnostics",
        "order",
        "water",
        "product_id",
        "provenance_type",
        "provenance_version",
        "pc_shortcut",
        "optical_shortcut",
        "parent_order",
        "parameters",
        "json_nan",
        "naive_time",
        "reference_time",
        "algorithm",
        "fingerprint",
    ],
)
def test_typed_output_rejects_corruption(collection, run, corruption):
    scenes, registry, _ = collection
    result = deepcopy(run(scenes, registry))
    name = "ndci_like"
    feature = result.results[name]
    if corruption == "shape":
        feature = replace(feature, baseline_centre=feature.baseline_centre[:1])
    elif corruption == "dtype":
        feature = replace(feature, baseline_centre=feature.baseline_centre.astype(np.float32))
    elif corruption == "mask_dtype":
        feature = replace(feature, anomaly_valid_mask=feature.anomaly_valid_mask.astype(np.uint8))
    elif corruption == "mask_shape":
        feature = replace(feature, rank_valid_mask=feature.rank_valid_mask[:1])
    elif corruption == "expand":
        feature.target_valid_mask[0, 0] = False
    elif corruption == "count_dtype":
        feature = replace(
            feature, baseline_observation_count=feature.baseline_observation_count.astype(np.int32)
        )
    elif corruption == "count_value":
        feature.baseline_observation_count[0, 0] = 4
    elif corruption == "below_minimum":
        feature.baseline_observation_count[0, 0] = 0
    elif corruption == "valid_nan":
        feature.baseline_centre[0, 0] = np.nan
    elif corruption == "invalid_finite":
        feature.baseline_valid_mask[0, 0] = False
    elif corruption == "negative_scale":
        feature.baseline_scale[0, 0] = -1
    elif corruption == "rank_range":
        feature.empirical_rank[0, 0] = 1.1
    elif corruption == "rank_mask":
        feature.rank_valid_mask[0, 0] = False
    elif corruption == "zero_anomaly":
        feature.baseline_scale[0, 0] = 0
    elif corruption == "anomaly_value":
        feature.robust_standardized_anomaly[0, 0] += 1
    elif corruption == "statistics":
        feature = replace(
            feature,
            statistics=replace(
                feature.statistics, centre=replace(feature.statistics.centre, minimum=999)
            ),
        )
    elif corruption == "diagnostics":
        feature = replace(feature, diagnostics=replace(feature.diagnostics, valid_anomaly_count=0))
    elif corruption == "order":
        result = replace(result, feature_order=tuple(reversed(result.feature_order)))
    elif corruption == "water":
        result.valid_water_mask[0, 0] = False
    elif corruption == "product_id":
        result = replace(result, product_id="temporal:" + "f" * 64)
    elif corruption in {"provenance_type", "provenance_version"}:
        result = replace(
            result,
            provenance=replace(
                result.provenance,
                **(
                    {"product_type": "hab"}
                    if corruption == "provenance_type"
                    else {"processing_version": "as104-v2"}
                ),
            ),
        )
    elif corruption in {"pc_shortcut", "optical_shortcut", "parent_order"}:
        source_ids = (
            ("pc:0",)
            if corruption == "pc_shortcut"
            else (
                (scenes[0].parent_product_id,)
                if corruption == "optical_shortcut"
                else tuple(reversed(result.provenance.source_ids))
            )
        )
        result = replace(result, provenance=replace(result.provenance, source_ids=source_ids))
    elif corruption == "parameters":
        result = replace(result, provenance=replace(result.provenance, parameters={}))
    elif corruption == "json_nan":
        result.processing_parameters["bad"] = float("nan")
    elif corruption == "naive_time":
        result = replace(result, target_acquired_at=result.target_acquired_at.replace(tzinfo=None))
    elif corruption == "reference_time":
        result = replace(
            result,
            reference_acquired_at=(result.target_acquired_at, *result.reference_acquired_at[1:]),
        )
    elif corruption == "algorithm":
        result.processing_parameters["identity"]["algorithm"]["MAD_factor"] = 1.0
    else:
        result.processing_parameters["identity"]["input_fingerprints"]["target"] = "invalid"
    result.results[name] = feature
    with pytest.raises((ValueError, KeyError)):
        result.validate()


@pytest.mark.parametrize(
    "key,value",
    [
        ("minimum_observations", True),
        ("formulas", {}),
        ("feature_order", []),
        ("processing_version", "as104-v2"),
        ("algorithm", {}),
    ],
)
def test_rehashed_output_identity_cannot_override_frozen_contract(collection, run, key, value):
    scenes, registry, _ = collection
    result = deepcopy(run(scenes, registry))
    result.processing_parameters["identity"][key] = value
    product_id = temporal_product_id(result.processing_parameters["identity"])
    result = replace(
        result, product_id=product_id, provenance=replace(result.provenance, product_id=product_id)
    )
    with pytest.raises(ValueError):
        result.validate()


@pytest.mark.parametrize("field", ["shift", "crs", "shape", "grid_id"])
def test_selected_grid_mismatch(collection, run, field):
    scenes, registry, _ = collection
    scene = deepcopy(scenes[0])
    grid = scene.grid
    changes = {
        "shift": {"transform": Affine(20, 0, 200020, 0, -20, 2800000)},
        "crs": {"crs": "EPSG:32641"},
        "shape": {"width": 4},
        "grid_id": {"grid_id": "other"},
    }
    scene = replace(scene, grid=replace(grid, **changes[field]))
    scenes[0] = scene
    with pytest.raises(ValueError):
        run(scenes, registry)


@pytest.mark.parametrize(
    "key,value",
    [("processing_version", "as103-v2"), ("formulas", {}), ("input_support_policy", "relaxed")],
)
def test_as103_contract_mismatch_rejected(collection, run, key, value):
    scenes, registry, _ = collection
    scenes[0].processing_parameters["identity"][key] = value
    with pytest.raises(ValueError):
        run(scenes, registry)


def test_distinct_reprocessing_products_same_acquisition_rejected(collection, run):
    scenes, registry, _ = collection
    extra = rewrite_parent(
        scenes[0],
        registry,
        lambda identity: identity.update(pc_generation_time="2024-01-01T00:00:00Z"),
    )
    assert extra.product_id != scenes[0].product_id
    with pytest.raises(ValueError, match="Duplicate"):
        run([extra, *scenes], registry)
