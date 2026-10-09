from copy import deepcopy
from dataclasses import asdict, replace
from datetime import UTC, datetime

import numpy as np
import pytest

from aquasentinel.preprocessing.cache import canonical_json
from aquasentinel.temporal.baseline import _input_fingerprint, _snapshot

from .conftest import refresh, rewrite_parent


def _with_platforms(scene, registry, observation_platform, source_platform):
    """Build self-consistent upstream identities without changing platform spelling."""
    parent = registry.get_derived_product(scene.parent_product_id)
    source_id = parent.source_ids[0]
    registry.sources[source_id] = replace(
        registry.get_source(source_id), platform=source_platform
    )

    def change(identity):
        identity["pc_source"]["platform"] = source_platform
        identity["observation_match"]["platform"] = observation_platform

    return rewrite_parent(scene, registry, change)


@pytest.mark.parametrize(
    ("observation_platform", "source_platform"),
    [
        ("sentinel-2b", "Sentinel-2B"),
        ("Sentinel-2A", "sentinel-2a"),
        ("sentinel-2b", "sentinel-2b"),
    ],
)
def test_platform_consistency_guard_accepts_case_only(
    collection, monkeypatch, observation_platform, source_platform
):
    from aquasentinel.temporal import baseline

    scenes, registry, _ = collection
    scene = _with_platforms(scenes[-1], registry, observation_platform, source_platform)
    before_scene, before_registry = deepcopy(scene), deepcopy(registry)
    descriptors = []
    # Isolate the consistency guard: the later, unchanged descriptor schema requires
    # lowercase ObservationIdentity.platform. The reverse-case example tests only
    # this equality predicate, not permission to supply a mixed-case observation.
    monkeypatch.setattr(baseline, "validate_descriptors", descriptors.extend)
    descriptor = baseline._descriptor(scene, registry)
    assert descriptors == [descriptor]
    assert descriptor["observation"]["platform"] == observation_platform
    assert registry == before_registry
    assert scene.product_id == before_scene.product_id
    assert scene.parent_product_id == before_scene.parent_product_id
    assert scene.processing_parameters == before_scene.processing_parameters
    assert scene.provenance == before_scene.provenance


@pytest.mark.parametrize("platform", ["sentinel-2a", "sentinel-2b"])
def test_real_platform_case_pattern_preserves_identity_lineage_and_inputs(
    make_collection, run, platform
):
    from aquasentinel.temporal.baseline import temporal_product_id

    scenes, registry, _ = make_collection(platform=platform)
    source_platform = "Sentinel-2" + platform[-1].upper()
    scenes = [_with_platforms(s, registry, platform, source_platform) for s in scenes]
    before_scenes, before_registry = deepcopy(scenes), deepcopy(registry)
    fingerprints = [_input_fingerprint(_snapshot(s, None), s.grid.shape) for s in scenes]
    result = run(scenes, registry)
    assert_equal(result, run(scenes, registry))
    assert registry == before_registry
    assert result.provenance.source_ids == (
        scenes[-1].product_id, *(s.product_id for s in scenes[:-1])
    )
    assert result.product_id == temporal_product_id(result.processing_parameters["identity"])
    for scene, before, fingerprint in zip(scenes, before_scenes, fingerprints):
        assert scene.product_id == before.product_id
        assert scene.parent_product_id == before.parent_product_id
        assert scene.processing_parameters == before.processing_parameters
        assert scene.provenance == before.provenance
        assert _input_fingerprint(_snapshot(scene, None), scene.grid.shape) == fingerprint
        for name in scene.feature_order:
            np.testing.assert_array_equal(scene.features[name], before.features[name])
            np.testing.assert_array_equal(
                scene.feature_valid_masks[name], before.feature_valid_masks[name]
            )
        np.testing.assert_array_equal(scene.valid_water_mask, before.valid_water_mask)
        parent = registry.get_derived_product(scene.parent_product_id)
        identity = parent.parameters["identity"]
        source = registry.get_source(parent.source_ids[0])
        assert source.platform == identity["pc_source"]["platform"] == source_platform
        assert identity["observation_match"]["platform"] == platform
    assert all(
        d["observation"]["platform"] == platform
        for d in result.processing_parameters["identity"]["compatibility"]
    )


@pytest.mark.parametrize(
    "observation_platform",
    [
        "sentinel-2a", "sentinel2b", "sentinel_2b", "sentinel-3b", "s2b",
        "Sentinel-2B-extra", "prefix-Sentinel-2B", " sentinel-2b", "sentinel-2b ",
    ],
)
def test_platform_consistency_guard_rejects_non_case_differences(
    collection, run, observation_platform
):
    scenes, registry, _ = collection
    scenes[-1] = _with_platforms(
        scenes[-1], registry, observation_platform, "Sentinel-2B"
    )
    with pytest.raises(ValueError, match="upstream"):
        run(scenes, registry)


@pytest.mark.parametrize("mismatch", ["observation", "source"])
def test_case_equivalent_platform_does_not_allow_acquisition_mismatch(collection, run, mismatch):
    scenes, registry, _ = collection
    scene = _with_platforms(scenes[-1], registry, "sentinel-2b", "Sentinel-2B")
    timestamp = datetime(2023, 4, 29, 6, 46, 29, 24000, tzinfo=UTC)
    parent = registry.get_derived_product(scene.parent_product_id)
    source_id = parent.source_ids[0]
    if mismatch == "source":
        registry.sources[source_id] = replace(
            registry.get_source(source_id), acquired_at=timestamp
        )

    def change(identity):
        identity["observation_match" if mismatch == "observation" else "pc_source"][
            "acquired_at"
        ] = timestamp.isoformat().replace("+00:00", "Z")

    scenes[-1] = rewrite_parent(scene, registry, change)
    with pytest.raises(ValueError, match="upstream"):
        run(scenes, registry)


@pytest.mark.parametrize("invalid_platform", [None, 42, True, {"platform": "sentinel-2b"}])
def test_platform_consistency_guard_does_not_coerce_non_strings(collection, run, invalid_platform):
    scenes, registry, _ = collection
    scenes[-1] = _with_platforms(scenes[-1], registry, invalid_platform, "Sentinel-2B")
    with pytest.raises(ValueError, match="upstream"):
        run(scenes, registry)


def assert_equal(first, second):
    assert first.product_id == second.product_id
    assert first.provenance.source_ids == second.provenance.source_ids
    assert first.processing_parameters == second.processing_parameters
    for name in first.feature_order:
        a, b = first.results[name], second.results[name]
        for field in asdict(a):
            x, y = getattr(a, field), getattr(b, field)
            if isinstance(x, np.ndarray):
                np.testing.assert_array_equal(x, y)
            else:
                assert x == y


def test_repeat_permutation_layout_and_creation_time_independence(collection, run):
    scenes, registry, _ = collection
    first = run(scenes, registry)
    assert_equal(first, run(scenes, registry))
    assert_equal(
        first, run(list(reversed(scenes)), registry, target_product_id=scenes[-1].product_id)
    )
    changed = deepcopy(scenes)
    for scene in changed:
        for mapping in (scene.features, scene.feature_valid_masks):
            for key in mapping:
                mapping[key] = np.asfortranarray(mapping[key])
    assert_equal(first, run(changed, registry))
    changed[-1] = replace(
        changed[-1],
        provenance=replace(changed[-1].provenance, created_at=datetime(2030, 1, 1, tzinfo=UTC)),
    )
    assert_equal(first, run(changed, registry))
    changed_output = replace(
        first, provenance=replace(first.provenance, created_at=datetime(2030, 1, 1, tzinfo=UTC))
    )
    changed_output.validate()
    assert changed_output.product_id == first.product_id


def test_selection_reuses_validated_collection_for_single_pass_input(collection, run):
    from aquasentinel.temporal import compute_temporal_anomaly

    scenes, registry, _ = collection
    original = run(scenes, registry)
    result = compute_temporal_anomaly(
        iter(scenes),
        target_product_id=scenes[-1].product_id,
        reference_start=datetime(2023, 3, 1, tzinfo=UTC),
        minimum_observations=5,
        registry=registry,
    )
    assert_equal(original, result)


@pytest.mark.parametrize(
    "role", ["target_value", "target_support", "reference_value", "reference_support"]
)
def test_consumed_content_changes_identity(collection, run, role):
    scenes, registry, _ = collection
    original = run(scenes, registry)
    index = -1 if role.startswith("target") else 2
    changed = deepcopy(scenes[index])
    if role.endswith("value"):
        changed.features["ndci_like"][0, 0] += 20
    else:
        changed.feature_valid_masks["ndci_like"][0, 0] = False
    changed = refresh(changed)
    scenes[index] = changed
    registry.derived_products[changed.product_id] = changed.provenance
    new = run(scenes, registry)
    assert new.product_id != original.product_id
    if role == "reference_value":
        assert (
            new.results["ndci_like"].baseline_centre[0, 0]
            != (original.results["ndci_like"].baseline_centre[0, 0])
        )
    if role.endswith("support"):
        assert not new.results["ndci_like"].baseline_valid_mask[0, 0]


@pytest.mark.parametrize("change_support", [False, True])
def test_reference_outside_target_feature_support_ignored(make_collection, run, change_support):
    scenes, registry, _ = make_collection()
    target = deepcopy(scenes[-1])
    target.feature_valid_masks["ndci_like"][0, 0] = False
    target = refresh(target)
    scenes[-1] = target
    registry.derived_products[target.product_id] = target.provenance
    original = run(scenes, registry)
    reference = deepcopy(scenes[0])
    if change_support:
        reference.feature_valid_masks["ndci_like"][0, 0] = False
    else:
        reference.features["ndci_like"][0, 0] = 1000
    reference = refresh(reference)
    scenes[0] = reference
    registry.derived_products[reference.product_id] = reference.provenance
    assert reference.product_id in original.reference_product_ids
    assert_equal(original, run(scenes, registry))


@pytest.mark.parametrize("future", [False, True])
def test_unselected_scene_mutation_never_changes_product(collection, run, future):
    scenes, registry, _ = collection
    target_id = scenes[-1].product_id
    if future:
        candidate = deepcopy(scenes[0])
        new_time = datetime(2023, 5, 1, tzinfo=UTC)
        # This excluded scene is independently model-valid; upstream resolution is not needed.
        parameters = deepcopy(candidate.processing_parameters)
        parameters["identity"]["acquired_at"] = new_time.isoformat()
        from aquasentinel.features.spectral import feature_product_id

        product_id = feature_product_id(parameters["identity"])
        candidate = replace(
            candidate,
            acquired_at=new_time,
            product_id=product_id,
            processing_parameters=parameters,
            provenance=replace(candidate.provenance, product_id=product_id, parameters=parameters),
        )
        pool = [*scenes, candidate]
        original = run(scenes, registry)
        kwargs = {}
    else:
        pool = scenes
        candidate = scenes[0]
        kwargs = {"reference_start": scenes[1].acquired_at, "minimum_observations": 3}
        original = run(pool, registry, **kwargs)
    assert_equal(original, run(pool, registry, target_product_id=target_id, **kwargs))
    changed = deepcopy(candidate)
    changed.features["ndci_like"][:] = -20
    changed = refresh(changed)
    pool[pool.index(candidate)] = changed
    assert_equal(original, run(pool, registry, target_product_id=target_id, **kwargs))
    assert changed.product_id not in original.provenance.source_ids


def test_target_water_mask_and_invalid_nan_payload_fingerprint(make_collection, run):
    water = np.ones((2, 3), bool)
    water[0, 0] = False
    scenes, registry, _ = make_collection(target_mask=water)
    original = run(scenes, registry)
    changed = deepcopy(scenes[-1])
    for array in changed.features.values():
        array.view(np.uint32)[0, 0] = 0x7FC00042
    assert_equal(original, run([*scenes[:-1], changed], registry))
    snapshot = _snapshot(changed, None)
    old = _input_fingerprint(snapshot, changed.grid.shape)
    # The full original water mask is semantic input even when feature masks are unchanged.
    snapshot.water[0, 0] = True
    assert _input_fingerprint(snapshot, changed.grid.shape) != old


def test_exact_multi_parent_lineage_and_read_only_registry(collection, run):
    scenes, registry, parents = collection
    before = deepcopy(registry)
    result = run(scenes, registry)
    assert registry == before
    expected_parents = (scenes[-1].product_id, *(scene.product_id for scene in scenes[:-1]))
    assert result.provenance.source_ids == expected_parents
    registry.add_derived_product(result.provenance)
    expected = []
    for index in [-1, *range(len(scenes) - 1)]:
        expected.extend(
            [
                parents[index].source_id,
                parents[index].provenance.product_id,
                scenes[index].product_id,
            ]
        )
    assert registry.get_lineage(result.product_id) == (*expected, result.product_id)
    assert all("cdse:" not in value for value in registry.get_lineage(result.product_id))


@pytest.mark.parametrize(
    "corruption",
    [
        "missing_feature",
        "missing_optical",
        "missing_source",
        "pc_shortcut",
        "optical_shortcut",
        "observation",
    ],
)
def test_upstream_missing_and_shortcut_rejected(collection, run, corruption):
    scenes, registry, parents = collection
    scene, parent = scenes[0], parents[0]
    if corruption == "missing_feature":
        del registry.derived_products[scene.product_id]
    elif corruption == "missing_optical":
        del registry.derived_products[parent.provenance.product_id]
    elif corruption == "missing_source":
        del registry.sources[parent.source_id]
    elif corruption in {"pc_shortcut", "optical_shortcut"}:
        registry.derived_products[scene.product_id] = replace(
            scene.provenance,
            source_ids=(parent.source_id,)
            if corruption == "pc_shortcut"
            else (scenes[-1].parent_product_id,),
        )
    else:
        scenes[0] = rewrite_parent(
            scene,
            registry,
            lambda identity: identity["observation_match"].update(platform="sentinel-2a"),
        )
    with pytest.raises(ValueError, match="upstream"):
        run(scenes, registry)


@pytest.mark.parametrize(
    "field", ["tile", "orbit", "baseline", "version", "resampling", "support", "decoding", "aoi"]
)
def test_rehashed_processing_contract_mismatch_rejected(collection, run, field):
    scenes, registry, _ = collection

    def change(identity):
        if field == "tile":
            identity["observation_match"]["mgrs_tile"] = "40RBP"
        elif field == "orbit":
            identity["observation_match"]["relative_orbit"] = 21
        elif field == "baseline":
            identity["pc_processing_baseline"] = "05.10"
            identity["decoding"]["processing_baseline"] = "05.10"
        elif field == "version":
            identity["processing_version"] = "as102-v2"
        elif field == "resampling":
            identity["resampling"]["reflectance"] = "nearest"
        elif field == "support":
            identity["interpolation_support_policy"] = "relaxed"
        elif field == "decoding":
            identity["decoding"]["offsets"]["B02"] = 0
        else:
            identity["aoi_geometry_digest"] = "b" * 64

    scenes[0] = rewrite_parent(scenes[0], registry, change)
    with pytest.raises(ValueError, match="incompatible"):
        run(scenes, registry)


def test_mixed_sentinel_platforms_and_generation_times_allowed(collection, run):
    scenes, registry, _ = collection
    source = registry.get_source("pc:0")
    registry.sources["pc:0"] = replace(source, platform="sentinel-2a")

    def change(identity):
        identity["pc_source"]["platform"] = "sentinel-2a"
        identity["observation_match"]["platform"] = "sentinel-2a"
        identity["pc_generation_time"] = "2024-01-01T00:00:00Z"

    scenes[0] = rewrite_parent(scenes[0], registry, change)
    assert run(scenes, registry).results["ndci_like"].anomaly_valid_mask.all()


def test_no_io_and_input_immutability(collection, run, monkeypatch):
    import builtins
    import socket
    import urllib.request
    from pathlib import Path

    import rasterio

    scenes, registry, _ = collection
    before = deepcopy(scenes)
    registry_before = canonical_json(
        {k: v.parameters for k, v in registry.derived_products.items()}
    )

    def forbidden(*args, **kwargs):
        pytest.fail("AS-104 attempted retrieval or disk IO")

    for module, name in [
        ("aquasentinel.catalog.stac", "search_catalog"),
        ("aquasentinel.ingestion.planetary_computer", "sign_asset"),
        ("aquasentinel.ingestion.planetary_computer", "read_bytes"),
        ("aquasentinel.preprocessing.alignment", "read_native_asset"),
        ("aquasentinel.preprocessing.cache", "write_cache"),
    ]:
        monkeypatch.setattr(module + "." + name, forbidden)
    for owner, name in [
        (builtins, "open"),
        (Path, "open"),
        (Path, "write_bytes"),
        (Path, "write_text"),
        (socket, "create_connection"),
        (urllib.request, "urlopen"),
        (rasterio, "open"),
        (np, "save"),
        (np, "savez"),
        (np, "savez_compressed"),
    ]:
        monkeypatch.setattr(owner, name, forbidden)
    result = run(scenes, registry)
    assert result.results["ndci_like"].anomaly_valid_mask.all()
    for old, scene in zip(before, scenes):
        for name in scene.feature_order:
            np.testing.assert_array_equal(old.features[name], scene.features[name])
            np.testing.assert_array_equal(
                old.feature_valid_masks[name], scene.feature_valid_masks[name]
            )
        np.testing.assert_array_equal(old.valid_water_mask, scene.valid_water_mask)
        assert old.processing_parameters == scene.processing_parameters
        assert old.provenance == scene.provenance
    assert registry_before == canonical_json(
        {k: v.parameters for k, v in registry.derived_products.items()}
    )
