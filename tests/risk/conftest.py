from copy import deepcopy
from dataclasses import replace
from datetime import UTC, datetime, timedelta
from hashlib import sha256
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

import numpy as np
import pytest

from aquasentinel.geometry import extract_hab_anomaly_geometry
from aquasentinel.geometry.hab import FAMILY_MEMBERS, FAMILY_ORDER
from aquasentinel.persistence import compute_hab_persistence
from aquasentinel.risk import HABRiskPolicy, compute_hab_risk
from aquasentinel.temporal.models import ReferencePeriod


@pytest.fixture(scope="session")
def synthetic_upstream():
    # Existing synthetic factories only; this is not a sealed handoff/cache reader.
    path = Path(__file__).parents[1] / "persistence" / "conftest.py"
    spec = spec_from_file_location("as107_synthetic_upstream", path)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module, module.upstream.__wrapped__()


@pytest.fixture
def make_inputs(synthetic_upstream):
    module, (_, factory, _) = synthetic_upstream

    def make(specs=None, *, states=((True, True), (True, True)), shape=(2, 3)):
        if specs is None:
            specs = [{"support": p, "candidate": c} for p, c in states]
        geometries, witnesses = [], {}
        for i, spec in enumerate(specs):
            support = spec.get("support", True)
            candidate = np.broadcast_to(spec.get("candidate", True), shape)
            available = spec.get("available", {})
            evidence = spec.get("evidence", {})
            supports, ranks = {}, {}
            for f, names in FAMILY_MEMBERS.items():
                a = np.broadcast_to(available.get(f, support), shape).copy()
                v = np.broadcast_to(evidence.get(f, candidate if f in (FAMILY_ORDER[0], FAMILY_ORDER[3])
                                                  else False), shape)
                for n in names:
                    supports[n] = a.copy()
                    ranks[n] = np.where(v, 0.95, 0.5)
            parent = factory(shape=shape, supports=supports, ranks=ranks)
            time = datetime(2023, 4, 1, tzinfo=UTC) + timedelta(days=i)
            parent = replace(parent, target_acquired_at=time,
                             target_product_id="spectral:" + sha256(time.isoformat().encode()).hexdigest(),
                             reference_period=ReferencePeriod(datetime(2023, 3, 1, tzinfo=UTC),
                                                              datetime(2023, 4, 1, tzinfo=UTC)))
            parent = module.reidentify(parent)
            geometry = extract_hab_anomaly_geometry(parent)
            geometries.append(geometry)
            witnesses[parent.product_id] = parent
        persistence = compute_hab_persistence(geometries, temporal_parents=witnesses,
                                              target_geometry_product_id=geometries[-1].product_id)
        return geometries[-1], persistence, geometries, witnesses
    return make


@pytest.fixture
def inputs(make_inputs):
    return make_inputs()


@pytest.fixture
def compute():
    def run(inputs, policy=None):
        target, persistence, sequence, witnesses = inputs
        return compute_hab_risk(target, persistence, geometry_scenes=sequence,
                                temporal_parents=witnesses, policy=policy or HABRiskPolicy())
    return run


def validate(result, inputs, policy=None):
    g, p, seq, witnesses = inputs
    result.validate(g, p, geometry_scenes=seq, temporal_parents=witnesses,
                    policy=policy or HABRiskPolicy())


def rehash_risk(result):
    """Attacker updates every local output hash/identity copy, without authoritative regeneration."""
    from aquasentinel.risk.scoring import output_content_fingerprint, risk_product_id

    parameters = deepcopy(result.processing_parameters)
    parameters["identity"]["policy"] = result.policy.to_dict()
    parameters["identity"]["input_content_fingerprint"] = result.input_content_fingerprint
    out = output_content_fingerprint(result)
    parameters["output_content_fingerprint"] = out
    product_id = risk_product_id(parameters["identity"])
    return replace(result, processing_parameters=parameters, output_content_fingerprint=out,
                   product_id=product_id, provenance=replace(result.provenance,
                       product_id=product_id, parameters=deepcopy(parameters)))
