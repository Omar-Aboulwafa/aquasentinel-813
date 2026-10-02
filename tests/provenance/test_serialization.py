import json
from datetime import UTC, datetime

import pytest

from aquasentinel.provenance import (
    DerivedProductRecord,
    SourceRecord,
    derived_product_to_dict,
    source_record_to_dict,
    write_derived_product_record,
    write_source_record,
)


def test_source_record_serialization() -> None:
    record = SourceRecord(
        source_id="s2-demo-001",
        platform="Sentinel-2",
        product_id="S2_DEMO_PRODUCT",
        acquired_at=datetime(
            2023,
            4,
            15,
            6,
            30,
            tzinfo=UTC,
        ),
        catalog="demo-stac",
        collection="sentinel-2-l2a",
        source_url="https://example.test/item",
        license_name="public-demo",
    )

    payload = source_record_to_dict(record)

    assert payload["schema_version"] == "1.0"
    assert payload["record_type"] == "source_observation"
    assert payload["platform"] == "Sentinel-2"
    assert payload["acquired_at"] == "2023-04-15T06:30:00Z"


def test_derived_product_serialization() -> None:
    record = DerivedProductRecord(
        product_id="hab-risk-demo-001",
        product_type="hab_risk_map",
        created_at=datetime(
            2026,
            10,
            2,
            10,
            0,
            tzinfo=UTC,
        ),
        processing_version="0.1.0",
        source_ids=("s2-demo-001",),
        parameters={
            "max_cloud_cover_percent": 30,
            "method": "temporal_anomaly",
        },
    )

    payload = derived_product_to_dict(record)

    assert payload["record_type"] == "derived_product"
    assert payload["source_ids"] == ["s2-demo-001"]
    assert payload["parameters"]["method"] == "temporal_anomaly"


def test_write_source_record(tmp_path) -> None:
    record = SourceRecord(
        source_id="s1-demo-001",
        platform="Sentinel-1",
        product_id="S1_DEMO_PRODUCT",
        acquired_at=datetime(
            2026,
            5,
            8,
            9,
            0,
            tzinfo=UTC,
        ),
        catalog="demo-stac",
    )

    output = tmp_path / "source.json"
    write_source_record(record, output)

    payload = json.loads(output.read_text(encoding="utf-8"))

    assert payload["source_id"] == "s1-demo-001"
    assert payload["platform"] == "Sentinel-1"


def test_write_derived_product_record(tmp_path) -> None:
    record = DerivedProductRecord(
        product_id="oil-risk-demo-001",
        product_type="oil_slick_candidate_map",
        created_at=datetime.now(UTC),
        processing_version="0.1.0",
        source_ids=("s1-demo-001",),
        parameters={"threshold": -18.5},
    )

    output = tmp_path / "derived.json"
    write_derived_product_record(record, output)

    payload = json.loads(output.read_text(encoding="utf-8"))

    assert payload["product_id"] == "oil-risk-demo-001"
    assert payload["processing_version"] == "0.1.0"


def test_rejects_non_json_serializable_parameters() -> None:
    record = DerivedProductRecord(
        product_id="invalid-demo",
        product_type="test",
        created_at=datetime.now(UTC),
        processing_version="0.1.0",
        source_ids=("source-1",),
        parameters={"invalid": {1, 2, 3}},
    )

    with pytest.raises(
        TypeError,
        match="must be JSON serializable",
    ):
        derived_product_to_dict(record)