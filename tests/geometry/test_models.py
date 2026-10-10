from copy import deepcopy
from dataclasses import asdict, replace
from datetime import UTC, datetime

import numpy as np
import pytest

from aquasentinel.geometry import extract_hab_anomaly_geometry
from aquasentinel.geometry.hab import geometry_product_id, output_content_fingerprint


@pytest.mark.parametrize(
    "field",
    [
        "feature_support_masks",
        "feature_evidence_masks",
        "family_available_masks",
        "family_evidence_masks",
        "candidate_analysis_support_mask",
        "available_family_count",
        "family_vote_count",
        "candidate_mask",
        "component_labels",
    ],
)
def test_tampered_arrays_fail_parent_aware_validation(parent, field):
    scene = deepcopy(extract_hab_anomaly_geometry(parent))
    value = getattr(scene, field)
    array = next(iter(value.values())) if isinstance(value, dict) else value
    array[0, 0] = not array[0, 0] if array.dtype == bool else array[0, 0] + 1
    # Even recomputing the output hash cannot hide scientific disagreement.
    scene.processing_parameters["output_content_fingerprint"] = output_content_fingerprint(
        vars(scene)
    )
    scene = replace(
        scene,
        provenance=replace(scene.provenance, parameters=deepcopy(scene.processing_parameters)),
    )
    with pytest.raises(ValueError):
        scene.validate(parent)


@pytest.mark.parametrize("field", ["shape", "dtype", "keys", "order"])
def test_mask_contract_is_explicit(parent, field):
    scene = deepcopy(extract_hab_anomaly_geometry(parent))
    masks = scene.feature_evidence_masks
    first = next(iter(masks))
    if field == "shape":
        masks[first] = masks[first][:-1]
    elif field == "dtype":
        masks[first] = masks[first].astype(np.uint8)
    elif field == "keys":
        masks["extra"] = masks[first].copy()
    else:
        scene = replace(scene, feature_evidence_masks=dict(reversed(list(masks.items()))))
    with pytest.raises(ValueError):
        scene.validate(parent)


@pytest.mark.parametrize(
    "change",
    [
        "geometry",
        "pixel_count",
        "area_m2",
        "area_km2",
        "bbox_projected",
        "region_id",
        "component_label",
        "first_pixel_row",
        "first_pixel_col",
        "participating_families",
        "family_evidence_pixel_counts",
        "maximum_family_votes",
        "median_family_votes",
        "summaries",
    ],
)
def test_tampered_region_geometry_and_measurements(parent, change):
    scene = deepcopy(extract_hab_anomaly_geometry(parent))
    r = scene.regions[0]
    if change == "geometry":
        r.geometry["coordinates"][0][0] = (0.0, 0.0)
    elif change == "summaries":
        n = next(iter(r.feature_summaries))
        r.feature_summaries[n] = replace(
            r.feature_summaries[n], deviation=replace(r.feature_summaries[n].deviation, median=99.0)
        )
    else:
        value = {
            "pixel_count": 99,
            "area_m2": 999.0,
            "area_km2": 0.999,
            "bbox_projected": (0.0, 0.0, 1.0, 1.0),
            "region_id": "wrong",
            "component_label": 2,
            "first_pixel_row": 2,
            "first_pixel_col": 2,
            "participating_families": (),
            "family_evidence_pixel_counts": {},
            "maximum_family_votes": 5,
            "median_family_votes": 5.0,
        }[change]
        r = replace(r, **{change: value})
    scene = replace(scene, regions=(r,))
    with pytest.raises(ValueError):
        scene.validate(parent)


@pytest.mark.parametrize(
    "field", ["statistics", "diagnostics", "grid", "parent", "time", "id", "output_hash"]
)
def test_tampered_scene_metadata(parent, field):
    scene = deepcopy(extract_hab_anomaly_geometry(parent))
    if field == "statistics":
        scene = replace(scene, statistics=replace(scene.statistics, candidate_pixel_count=99))
    elif field == "diagnostics":
        first = next(iter(scene.diagnostics.features))
        scene.diagnostics.features[first] = replace(
            scene.diagnostics.features[first], evidence_count=99
        )
    elif field == "grid":
        scene = replace(scene, grid=replace(scene.grid, grid_id="wrong"))
    elif field == "parent":
        scene = replace(scene, parent_temporal_product_id="temporal:wrong")
    elif field == "time":
        scene = replace(scene, target_acquired_at=datetime(2024, 1, 1, tzinfo=UTC))
    elif field == "id":
        scene = replace(scene, product_id="hab_geometry:wrong")
    else:
        scene.processing_parameters["output_content_fingerprint"] = "0" * 64
    with pytest.raises(ValueError):
        scene.validate(parent)


@pytest.mark.parametrize(
    "change", ["mapping", "threshold", "connectivity", "filter", "denominator"]
)
def test_rehashed_altered_policy_is_not_valid_v1(parent, change):
    scene = deepcopy(extract_hab_anomaly_geometry(parent))
    old_id = scene.product_id
    policy = scene.processing_parameters["identity"]["policy"]
    if change == "mapping":
        policy["family_members"]["red_edge_b5_vs_red"] = ["ndci_like"]
    elif change == "threshold":
        policy["rank_threshold"]["nominal"] = 0.8
    elif change == "connectivity":
        policy["region_connectivity"] = 4
    elif change == "filter":
        policy["spatial_filtering"] = "remove single pixels"
    else:
        policy["denominator"] = "all AOI pixels"
    new_id = geometry_product_id(scene.processing_parameters["identity"])
    assert new_id != old_id
    scene = replace(
        scene,
        product_id=new_id,
        regions=tuple(
            replace(r, region_id=f"{new_id}:region:{r.component_label}") for r in scene.regions
        ),
        provenance=replace(
            scene.provenance, product_id=new_id, parameters=deepcopy(scene.processing_parameters)
        ),
    )
    with pytest.raises(ValueError):
        scene.validate(parent)


@pytest.mark.parametrize(
    "field,value",
    [
        ("product_type", "wrong"),
        ("processing_version", "as105-v2"),
        ("product_id", "wrong"),
        ("source_ids", ("pc:5",)),
        ("source_ids", ("optical:wrong",)),
        ("source_ids", ("spectral:wrong",)),
        ("source_ids", ()),
        ("created_at", datetime(2026, 10, 9, tzinfo=UTC).replace(tzinfo=None)),
        ("parameters", {}),
    ],
)
def test_provenance_shortcuts_or_tampering_rejected(parent, field, value):
    scene = extract_hab_anomaly_geometry(parent)
    scene = replace(scene, provenance=replace(scene.provenance, **{field: value}))
    with pytest.raises(ValueError):
        scene.validate(parent)


def test_parent_validation_is_not_bypassed(parent):
    broken = deepcopy(parent)
    broken.results["ndci_like"].empirical_rank[0, 0] = 1.1
    with pytest.raises(ValueError):
        extract_hab_anomaly_geometry(broken)
    with pytest.raises(TypeError):
        extract_hab_anomaly_geometry(object())


@pytest.mark.parametrize("bad_rank", [-0.1, 1.1, float("inf"), float("nan")])
def test_parent_rank_range_and_finiteness_enforced(parent, bad_rank):
    broken = deepcopy(parent)
    broken.results["ndci_like"].empirical_rank[0, 0] = bad_rank
    with pytest.raises(ValueError):
        extract_hab_anomaly_geometry(broken)


def test_wrong_parent_version_rejected(parent):
    broken = replace(parent, provenance=replace(parent.provenance, processing_version="as104-v2"))
    with pytest.raises(ValueError):
        extract_hab_anomaly_geometry(broken)


def test_output_fingerprint_covers_summaries_and_geometry(parent):
    scene = extract_hab_anomaly_geometry(parent)
    before = output_content_fingerprint(vars(scene))
    mutated = deepcopy(scene)
    mutated.regions[0].geometry["coordinates"][0][0] = (0.0, 0.0)
    assert output_content_fingerprint(vars(mutated)) != before
    mutated = replace(
        scene, regions=tuple(replace(r, region_id="noncircular") for r in scene.regions)
    )
    assert output_content_fingerprint(vars(mutated)) == before
    assert scene.processing_parameters["statistics"] == asdict(scene.statistics)
