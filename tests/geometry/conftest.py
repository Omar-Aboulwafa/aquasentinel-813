from copy import deepcopy
from dataclasses import asdict, replace
from datetime import UTC, datetime
from hashlib import sha256
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

import numpy as np
import pytest
from rasterio import Affine

from aquasentinel.features.spectral import FEATURE_ORDER
from aquasentinel.preprocessing.models import AnalysisGrid
from aquasentinel.temporal import compute_temporal_anomaly
from aquasentinel.temporal.baseline import temporal_product_id
from aquasentinel.temporal.models import (
    output_fingerprint,
    result_diagnostics,
    result_statistics,
)


def grid_for(shape, resolution=20):
    height, width = shape
    return AnalysisGrid(
        "EPSG:32640",
        Affine(resolution, 0, 200000, 0, -resolution, 2800000),
        width,
        height,
        float(resolution),
        (200000, 2800000 - resolution * height, 200000 + resolution * width, 2800000),
        f"synthetic-{height}-{width}-{resolution}",
    )


def refresh_parent(parent):
    """Keep synthetic changes internally valid without bypassing AS-104 validation."""
    results = {}
    for name, r in parent.results.items():
        z = np.full(parent.grid.shape, np.nan, np.float32)
        positive = r.baseline_valid_mask & (r.baseline_scale > 0)
        with np.errstate(over="ignore", invalid="ignore", divide="ignore"):
            values = r.deviation[positive] / r.baseline_scale[positive]
            cast = values.astype(np.float32)
        mask = np.zeros(parent.grid.shape, bool)
        mask[positive] = np.isfinite(values) & np.isfinite(cast)
        z[positive] = cast
        z[~mask] = np.nan
        r = replace(r, anomaly_valid_mask=mask, robust_standardized_anomaly=z)
        results[name] = replace(
            r, statistics=result_statistics(r), diagnostics=result_diagnostics(r, 5)
        )
    parameters = deepcopy(parent.processing_parameters)
    parameters["identity"]["grid"] = parent.grid.to_dict()
    parameters["identity"]["target_water_mask_digest"] = sha256(
        parent.valid_water_mask.astype(np.uint8).tobytes(order="C")
    ).hexdigest()
    parameters["statistics"] = {n: asdict(r.statistics) for n, r in results.items()}
    parameters["diagnostics"] = {n: asdict(r.diagnostics) for n, r in results.items()}
    parameters["output_content_fingerprint"] = output_fingerprint(results, parent.valid_water_mask)
    product_id = temporal_product_id(parameters["identity"])
    parent = replace(
        parent,
        results=results,
        processing_parameters=parameters,
        product_id=product_id,
        provenance=replace(
            parent.provenance, product_id=product_id, parameters=deepcopy(parameters)
        ),
    )
    parent.validate()
    return parent


@pytest.fixture(scope="session")
def synthetic_template():
    # Reuse the existing upstream synthetic factory read-only. No EO handoff/cache is loaded.
    path = Path(__file__).parents[1] / "temporal" / "conftest.py"
    spec = spec_from_file_location("as105_upstream_synthetic_fixtures", path)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    scenes, registry, _ = module.make_collection.__wrapped__()()
    parent = compute_temporal_anomaly(
        scenes,
        target_product_id=scenes[-1].product_id,
        reference_start=datetime(2023, 3, 1, tzinfo=UTC),
        minimum_observations=5,
        registry=registry,
    )
    return parent, registry


@pytest.fixture
def make_parent(synthetic_template):
    def make(
        *,
        shape=(3, 4),
        qualifying=("ndci_like", "green_red_ratio"),
        supports=None,
        water=None,
        deviations=None,
        ranks=None,
        scale=1,
        resolution=20,
    ):
        template, _ = synthetic_template
        water = np.ones(shape, bool) if water is None else np.asarray(water, bool).copy()
        parent = replace(
            deepcopy(template), grid=grid_for(shape, resolution), valid_water_mask=water
        )
        results = {}
        for name in FEATURE_ORDER:
            support = water.copy() if supports is None else np.asarray(supports[name], bool).copy()
            centre = np.full(shape, np.nan, np.float64)
            scales, deviation = centre.copy(), centre.copy()
            rank = np.full(shape, np.nan, np.float32)
            centre[support], scales[support] = 1, scale
            deviation[support] = (
                1 if deviations is None else np.broadcast_to(deviations[name], shape)[support]
            )
            rank[support] = (
                (np.float32(0.90) if name in qualifying else np.float32(0.5))
                if ranks is None
                else np.broadcast_to(ranks[name], shape)[support]
            )
            results[name] = replace(
                parent.results[name],
                target_valid_mask=water.copy(),
                baseline_observation_count=np.where(support, 5, 0).astype(np.uint32),
                baseline_valid_mask=support.copy(),
                rank_valid_mask=support,
                baseline_centre=centre,
                baseline_scale=scales,
                deviation=deviation,
                empirical_rank=rank,
            )
        return refresh_parent(replace(parent, results=results))

    return make


@pytest.fixture
def make_five_history_parent():
    """Use unchanged AS-104 calculation on synthetic histories; never read the handoff."""
    path = Path(__file__).parents[1] / "temporal" / "conftest.py"
    spec = spec_from_file_location("as105_five_history_synthetic_fixtures", path)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    factory = module.make_collection.__wrapped__()

    def make(history, target):
        scenes, registry, _ = factory(values=history, target_value=target)
        parent = compute_temporal_anomaly(
            scenes,
            target_product_id=scenes[-1].product_id,
            reference_start=datetime(2023, 3, 1, tzinfo=UTC),
            minimum_observations=5,
            registry=registry,
        )
        parent.validate()
        return parent

    return make


@pytest.fixture
def parent(make_parent):
    return make_parent()
