from copy import deepcopy
from dataclasses import replace
from datetime import UTC, datetime, timedelta
from hashlib import sha256
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

import numpy as np
import pytest

from aquasentinel.geometry import extract_hab_anomaly_geometry
from aquasentinel.persistence import compute_hab_persistence
from aquasentinel.temporal.baseline import temporal_product_id
from aquasentinel.temporal.models import ReferencePeriod, utc


@pytest.fixture(scope="session")
def upstream():
    # Reuse upstream synthetic fixtures unchanged, never accepted handoffs or caches.
    path = Path(__file__).parents[1] / "geometry" / "conftest.py"
    spec = spec_from_file_location("as106_synthetic_geometry", path)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    template = module.synthetic_template.__wrapped__()
    factory = module.make_parent.__wrapped__(template)
    return module, factory, template[1]


def reidentify(parent):
    parameters = deepcopy(parent.processing_parameters)
    identity = parameters["identity"]
    identity["target_acquired_at"] = utc(parent.target_acquired_at).isoformat()
    identity["target_product_id"] = parent.target_product_id
    identity["reference_product_ids"] = list(parent.reference_product_ids)
    identity["reference_acquired_at"] = [utc(t).isoformat() for t in parent.reference_acquired_at]
    identity["reference_period"] = parent.reference_period.to_dict()
    identity["compatibility"][0]["product_id"] = parent.target_product_id
    identity["compatibility"][0]["observation"]["acquired_at"] = identity["target_acquired_at"]
    for d, product_id, time in zip(
        identity["compatibility"][1:], parent.reference_product_ids, parent.reference_acquired_at
    ):
        d["product_id"] = product_id
        d["observation"]["acquired_at"] = utc(time).isoformat()
    product_id = temporal_product_id(identity)
    result = replace(
        parent, product_id=product_id, processing_parameters=parameters,
        provenance=replace(parent.provenance, product_id=product_id,
                           source_ids=(parent.target_product_id, *parent.reference_product_ids),
                           parameters=deepcopy(parameters)),
    )
    result.validate()
    return result


@pytest.fixture
def make_sequence(upstream):
    _module, factory, _ = upstream

    def make(states=((True, True), (True, True)), *, times=None, shape=(2, 3)):
        scenes, witnesses = [], {}
        for i, (p, c) in enumerate(states):
            p = np.broadcast_to(p, shape).copy()
            c = np.broadcast_to(c, shape).copy()
            assert not np.any(c & ~p), "Synthetic parents must satisfy C contained in P"
            names = factory().feature_order
            supports = {n: p.copy() for n in names}
            ranks = {n: np.where(c & (n in {"ndci_like", "green_red_ratio"}), 0.95, 0.5)
                     for n in names}
            parent = factory(shape=shape, supports=supports, ranks=ranks)
            time = times[i] if times else datetime(2023, 4, 1, tzinfo=UTC) + timedelta(days=i)
            parent = replace(
                parent, target_acquired_at=time,
                target_product_id="spectral:" + sha256(time.isoformat().encode()).hexdigest(),
                reference_period=ReferencePeriod(datetime(2023, 3, 1, tzinfo=UTC),
                                                 datetime(2023, 4, 1, tzinfo=UTC)),
            )
            parent = reidentify(parent)
            scene = extract_hab_anomaly_geometry(parent)
            assert np.array_equal(scene.candidate_analysis_support_mask, p)
            assert np.array_equal(scene.candidate_mask, c)
            scenes.append(scene)
            witnesses[parent.product_id] = parent
        return scenes, witnesses

    return make


@pytest.fixture
def sequence(make_sequence):
    return make_sequence()


@pytest.fixture
def compute():
    def run(sequence):
        scenes, parents = sequence
        return compute_hab_persistence(
            scenes, temporal_parents=parents, target_geometry_product_id=scenes[-1].product_id
        )
    return run
