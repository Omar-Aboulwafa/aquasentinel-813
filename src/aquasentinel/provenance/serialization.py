from __future__ import annotations

import json
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from aquasentinel.provenance.models import (
    DerivedProductRecord,
    SourceRecord,
)

PROVENANCE_SCHEMA_VERSION = "1.0"


def _utc_isoformat(value: datetime) -> str:
    if value.tzinfo is None:
        raise ValueError("Datetime must be timezone-aware.")

    return (
        value.astimezone(UTC)
        .isoformat()
        .replace("+00:00", "Z")
    )


def source_record_to_dict(record: SourceRecord) -> dict[str, Any]:
    record.validate()

    return {
        "schema_version": PROVENANCE_SCHEMA_VERSION,
        "record_type": "source_observation",
        "source_id": record.source_id,
        "platform": record.platform,
        "product_id": record.product_id,
        "acquired_at": _utc_isoformat(record.acquired_at),
        "catalog": record.catalog,
        "collection": record.collection,
        "source_url": record.source_url,
        "license_name": record.license_name,
    }


def derived_product_to_dict(
    record: DerivedProductRecord,
) -> dict[str, Any]:
    record.validate()

    payload = {
        "schema_version": PROVENANCE_SCHEMA_VERSION,
        "record_type": "derived_product",
        "product_id": record.product_id,
        "product_type": record.product_type,
        "created_at": _utc_isoformat(record.created_at),
        "processing_version": record.processing_version,
        "source_ids": list(record.source_ids),
        "parameters": record.parameters,
    }

    try:
        json.dumps(payload)
    except TypeError as exc:
        raise TypeError(
            "Derived product parameters must be JSON serializable."
        ) from exc

    return payload


def write_provenance_json(
    payload: dict[str, Any],
    path: str | Path,
) -> Path:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    text = json.dumps(
        payload,
        indent=2,
        ensure_ascii=False,
        sort_keys=True,
    )

    path.write_text(
        text + "\n",
        encoding="utf-8",
    )

    return path


def write_source_record(
    record: SourceRecord,
    path: str | Path,
) -> Path:
    return write_provenance_json(
        source_record_to_dict(record),
        path,
    )


def write_derived_product_record(
    record: DerivedProductRecord,
    path: str | Path,
) -> Path:
    return write_provenance_json(
        derived_product_to_dict(record),
        path,
    )

def source_record_from_dict(payload: dict[str, Any]) -> SourceRecord:
    if payload.get("record_type") != "source_observation":
        raise ValueError("Payload is not a source_observation record.")

    acquired_at = datetime.fromisoformat(
        str(payload["acquired_at"])
    )

    record = SourceRecord(
        source_id=str(payload["source_id"]),
        platform=str(payload["platform"]),
        product_id=str(payload["product_id"]),
        acquired_at=acquired_at,
        catalog=str(payload["catalog"]),
        collection=payload.get("collection"),
        source_url=payload.get("source_url"),
        license_name=payload.get("license_name"),
    )

    record.validate()
    return record


def derived_product_from_dict(
    payload: dict[str, Any],
) -> DerivedProductRecord:
    if payload.get("record_type") != "derived_product":
        raise ValueError("Payload is not a derived_product record.")

    created_at = datetime.fromisoformat(
        str(payload["created_at"])
    )

    record = DerivedProductRecord(
        product_id=str(payload["product_id"]),
        product_type=str(payload["product_type"]),
        created_at=created_at,
        processing_version=str(payload["processing_version"]),
        source_ids=tuple(payload["source_ids"]),
        parameters=dict(payload["parameters"]),
    )

    record.validate()
    return record