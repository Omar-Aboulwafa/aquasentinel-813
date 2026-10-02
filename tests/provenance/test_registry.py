from datetime import UTC, datetime

import pytest

from aquasentinel.provenance import (
    DerivedProductRecord,
    ProvenanceRegistry,
    SourceRecord,
)


def make_source(
    source_id: str = "s2-scene-001",
) -> SourceRecord:
    return SourceRecord(
        source_id=source_id,
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


def test_add_source() -> None:
    registry = ProvenanceRegistry()
    source = make_source()

    registry.add_source(source)

    assert registry.get_source(source.source_id) == source


def test_rejects_duplicate_source() -> None:
    registry = ProvenanceRegistry()
    source = make_source()

    registry.add_source(source)

    with pytest.raises(
        ValueError,
        match="Duplicate source_id",
    ):
        registry.add_source(source)


def test_rejects_unknown_source_reference() -> None:
    registry = ProvenanceRegistry()

    product = DerivedProductRecord(
        product_id="hab-layer-001",
        product_type="spectral_anomaly_layer",
        created_at=datetime.now(UTC),
        processing_version="0.1.0",
        source_ids=("missing-source",),
        parameters={},
    )

    with pytest.raises(
        ValueError,
        match="unknown source IDs",
    ):
        registry.add_derived_product(product)


def test_tracks_direct_lineage() -> None:
    registry = ProvenanceRegistry()
    source = make_source()

    registry.add_source(source)

    product = DerivedProductRecord(
        product_id="hab-layer-001",
        product_type="spectral_anomaly_layer",
        created_at=datetime.now(UTC),
        processing_version="0.1.0",
        source_ids=(source.source_id,),
        parameters={"method": "temporal_anomaly"},
    )

    registry.add_derived_product(product)

    assert registry.get_lineage(product.product_id) == (
        "s2-scene-001",
        "hab-layer-001",
    )


def test_tracks_multistep_lineage() -> None:
    registry = ProvenanceRegistry()
    source = make_source()

    registry.add_source(source)

    spectral_layer = DerivedProductRecord(
        product_id="spectral-layer-001",
        product_type="spectral_anomaly_layer",
        created_at=datetime.now(UTC),
        processing_version="0.1.0",
        source_ids=(source.source_id,),
        parameters={},
    )

    registry.add_derived_product(spectral_layer)

    risk_map = DerivedProductRecord(
        product_id="hab-risk-map-001",
        product_type="hab_risk_map",
        created_at=datetime.now(UTC),
        processing_version="0.1.0",
        source_ids=(spectral_layer.product_id,),
        parameters={},
    )

    registry.add_derived_product(risk_map)

    assert registry.get_lineage(risk_map.product_id) == (
        "s2-scene-001",
        "spectral-layer-001",
        "hab-risk-map-001",
    )