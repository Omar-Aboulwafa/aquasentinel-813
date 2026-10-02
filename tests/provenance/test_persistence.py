from datetime import UTC, datetime

from aquasentinel.provenance import (
    DerivedProductRecord,
    ProvenanceRegistry,
    SourceRecord,
    load_registry,
    save_registry,
)


def test_registry_round_trip(tmp_path) -> None:
    registry = ProvenanceRegistry()

    source = SourceRecord(
        source_id="s2-demo-001",
        platform="Sentinel-2",
        product_id="S2_PRODUCT_001",
        acquired_at=datetime(
            2023,
            4,
            15,
            6,
            30,
            tzinfo=UTC,
        ),
        catalog="test-stac",
    )

    registry.add_source(source)

    spectral_layer = DerivedProductRecord(
        product_id="spectral-layer-001",
        product_type="spectral_anomaly_layer",
        created_at=datetime.now(UTC),
        processing_version="0.1.0",
        source_ids=(source.source_id,),
        parameters={"method": "temporal_anomaly"},
    )

    registry.add_derived_product(spectral_layer)

    risk_map = DerivedProductRecord(
        product_id="hab-risk-map-001",
        product_type="hab_risk_map",
        created_at=datetime.now(UTC),
        processing_version="0.1.0",
        source_ids=(spectral_layer.product_id,),
        parameters={"threshold": 0.75},
    )

    registry.add_derived_product(risk_map)

    path = tmp_path / "manifest.json"
    save_registry(registry, path)

    restored = load_registry(path)

    assert restored.get_source("s2-demo-001") == source
    assert (
        restored.get_derived_product("hab-risk-map-001").product_type
        == "hab_risk_map"
    )
    assert restored.get_lineage("hab-risk-map-001") == (
        "s2-demo-001",
        "spectral-layer-001",
        "hab-risk-map-001",
    )