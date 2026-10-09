from copy import deepcopy
from dataclasses import replace
from datetime import UTC, datetime, timedelta
from hashlib import sha256

import numpy as np
import pytest
from rasterio import Affine

from aquasentinel.features import extract_spectral_features
from aquasentinel.features.models import FeatureDiagnostics, feature_statistics
from aquasentinel.ingestion.sentinel2_assets import (
    BANDS,
    ObservationIdentity,
    ResolvedOpticalSource,
)
from aquasentinel.preprocessing.cache import cache_identity
from aquasentinel.preprocessing.masks import scene_statistics
from aquasentinel.preprocessing.models import AnalysisGrid, PreprocessedOpticalScene
from aquasentinel.provenance import DerivedProductRecord, ProvenanceRegistry, SourceRecord
from aquasentinel.provenance.serialization import source_record_to_dict
from aquasentinel.temporal import compute_temporal_anomaly


def refresh(scene):
    """Model-consistent feature snapshots, including intentional mutable-content tests."""
    count = int(scene.valid_water_mask.sum())
    stats, diagnostics = {}, {}
    for name in scene.feature_order:
        mask, values = scene.feature_valid_masks[name], scene.features[name]
        values[~mask] = np.nan
        stats[name] = feature_statistics(values, mask, count)
        diagnostics[name] = FeatureDiagnostics(
            count,
            0,
            0,
            0,
            count - int(mask.sum()),
            int((mask & ((values < -1) | (values > 1))).sum()) if name == "ndci_like" else None,
        )
    parameters = deepcopy(scene.processing_parameters)
    from dataclasses import asdict

    parameters["statistics"] = {k: asdict(v) for k, v in stats.items()}
    parameters["diagnostics"] = {k: asdict(v) for k, v in diagnostics.items()}
    parameters["identity"]["parent_water_mask_digest"] = sha256(
        scene.valid_water_mask.astype(np.uint8).tobytes(order="C")
    ).hexdigest()
    # Preserve product ID when only feature values change, as the existing model does.
    from aquasentinel.features.spectral import feature_product_id

    product_id = feature_product_id(parameters["identity"])
    result = replace(
        scene,
        statistics=stats,
        diagnostics=diagnostics,
        processing_parameters=parameters,
        product_id=product_id,
        provenance=replace(scene.provenance, product_id=product_id, parameters=parameters),
    )
    result.validate()
    return result


def rewrite_parent(scene, registry, change):
    """Rehash a structured upstream change, rather than failing an unrelated ID check."""
    from aquasentinel.features.spectral import feature_product_id

    scene = deepcopy(scene)
    parent = registry.get_derived_product(scene.parent_product_id)
    parameters = deepcopy(parent.parameters)
    change(parameters["identity"])
    parent_id = "optical:" + cache_identity(parameters["identity"])
    parent = replace(
        parent,
        product_id=parent_id,
        parameters=parameters,
        processing_version=parameters["identity"]["processing_version"],
    )
    registry.derived_products[parent_id] = parent
    feature_parameters = deepcopy(scene.processing_parameters)
    feature_parameters["identity"]["parent_product_id"] = parent_id
    feature_parameters["identity"]["parent_processing_version"] = parent.processing_version
    feature_id = feature_product_id(feature_parameters["identity"])
    scene = replace(
        scene,
        parent_product_id=parent_id,
        product_id=feature_id,
        processing_parameters=feature_parameters,
        provenance=replace(
            scene.provenance,
            product_id=feature_id,
            source_ids=(parent_id,),
            parameters=feature_parameters,
        ),
    )
    scene.validate()
    registry.derived_products[feature_id] = scene.provenance
    return scene


@pytest.fixture
def make_collection():
    def make(
        values=(1, 2, 3, 4, 5),
        *,
        target_value=6,
        target_mask=None,
        reference_masks=None,
        platform="sentinel-2b",
    ):
        registry = ProvenanceRegistry()
        scenes, parents = [], []
        shape = (2, 3)
        grid = AnalysisGrid(
            "EPSG:32640",
            Affine(20, 0, 200000, 0, -20, 2800000),
            3,
            2,
            20.0,
            (200000, 2799960, 200060, 2800000),
            "test-grid",
        )
        for index, value in enumerate([*values, target_value]):
            is_target = index == len(values)
            acquired = (
                datetime(2023, 4, 28, 6, 46, 29, 24000, tzinfo=UTC)
                if is_target
                else datetime(2023, 3, 1, 6, tzinfo=UTC) + timedelta(days=index)
            )
            mask = (
                target_mask
                if is_target
                else (reference_masks[index] if reference_masks is not None else None)
            )
            water = np.ones(shape, bool) if mask is None else np.asarray(mask, bool).copy()
            pc = SourceRecord(
                f"pc:{index}",
                platform,
                f"actual-product-{index}",
                acquired,
                "https://planetarycomputer.microsoft.com/api/stac/v1/",
                "sentinel-2-l2a",
            )
            cdse = replace(pc, source_id=f"cdse:{index}", catalog="https://stac.example/")
            decoding = {
                "processing_baseline": "05.09",
                "quantification": 10000.0,
                "offsets": {b: -1000.0 for b in BANDS},
                "band_ids": {b: str(i) for i, b in enumerate(BANDS)},
            }
            observation = ObservationIdentity(acquired, platform, "40RBN", 20)
            identity = {
                "processing_version": "as102-v1",
                "pc_source": source_record_to_dict(pc),
                "observation_match": observation.to_dict(),
                "target_grid": grid.to_dict(),
                "pc_processing_baseline": "05.09",
                "pc_generation_time": acquired.isoformat(),
                "aoi_geometry_digest": "a" * 64,
                "bands": list(BANDS),
                "resampling": {"reflectance": "bilinear", "categorical": "nearest"},
                "mask_policy": {"water_scl": 6},
                "interpolation_support_policy": "all-contributor water support",
                "decoding": decoding,
            }
            parameters = {"identity": identity, "source_grids": {}}
            cache_id = cache_identity(identity)
            provenance = DerivedProductRecord(
                "optical:" + cache_id,
                "preprocessed_optical_scene",
                datetime(2026, 10, 8, tzinfo=UTC),
                "as102-v1",
                (pc.source_id,),
                parameters,
            )
            resolved = ResolvedOpticalSource(
                pc,
                cdse,
                observation,
                "05.09",
                acquired.isoformat(),
                {},
                (),
                {},
                decoding_metadata=decoding,
            )
            ones = np.ones(shape, bool)
            parent = PreprocessedOpticalScene(
                resolved,
                grid,
                {b: np.full(shape, 0.05, np.float32) for b in BANDS},
                np.full(shape, 6, np.uint8),
                ones,
                ones.copy(),
                water.copy(),
                water,
                ones.copy(),
                scene_statistics(ones, ones, water, water),
                parameters,
                cache_id,
                provenance,
            )
            scene = extract_spectral_features(parent)
            for array in scene.features.values():
                array[water] = value
            scene = refresh(scene)
            registry.add_source(pc)
            registry.add_derived_product(parent.provenance)
            registry.add_derived_product(scene.provenance)
            scenes.append(scene)
            parents.append(parent)
        return scenes, registry, parents

    return make


@pytest.fixture
def collection(make_collection):
    return make_collection()


@pytest.fixture
def run():
    def compute(scenes, registry, **kwargs):
        return compute_temporal_anomaly(
            scenes,
            target_product_id=(
                kwargs.pop("target_product_id")
                if "target_product_id" in kwargs
                else scenes[-1].product_id
            ),
            reference_start=kwargs.pop("reference_start", datetime(2023, 3, 1, tzinfo=UTC)),
            minimum_observations=kwargs.pop("minimum_observations", 5),
            registry=registry,
            **kwargs,
        )

    return compute
