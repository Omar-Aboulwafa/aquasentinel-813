from __future__ import annotations

import json
from pathlib import Path

from aquasentinel.provenance.registry import ProvenanceRegistry
from aquasentinel.provenance.serialization import (
    PROVENANCE_SCHEMA_VERSION,
    derived_product_from_dict,
    derived_product_to_dict,
    source_record_from_dict,
    source_record_to_dict,
)


def save_registry(
    registry: ProvenanceRegistry,
    path: str | Path,
) -> Path:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    payload = {
        "schema_version": PROVENANCE_SCHEMA_VERSION,
        "record_type": "provenance_registry",
        "sources": [
            source_record_to_dict(record)
            for record in registry.sources.values()
        ],
        "derived_products": [
            derived_product_to_dict(record)
            for record in registry.derived_products.values()
        ],
    }

    path.write_text(
        json.dumps(
            payload,
            indent=2,
            ensure_ascii=False,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )

    return path


def load_registry(
    path: str | Path,
) -> ProvenanceRegistry:
    path = Path(path)

    if not path.exists():
        raise FileNotFoundError(
            f"Provenance registry file not found: {path}"
        )

    payload = json.loads(path.read_text(encoding="utf-8"))

    if payload.get("record_type") != "provenance_registry":
        raise ValueError("Payload is not a provenance_registry.")

    registry = ProvenanceRegistry()

    for source_payload in payload.get("sources", []):
        registry.add_source(
            source_record_from_dict(source_payload)
        )

    pending_products = [
        derived_product_from_dict(item)
        for item in payload.get("derived_products", [])
    ]

    while pending_products:
        remaining = []
        progress = False

        for product in pending_products:
            try:
                registry.add_derived_product(product)
                progress = True
            except ValueError as exc:
                if "unknown source IDs" not in str(exc):
                    raise
                remaining.append(product)

        if not progress:
            unresolved = ", ".join(
                product.product_id
                for product in remaining
            )
            raise ValueError(
                "Could not resolve provenance dependencies for: "
                f"{unresolved}"
            )

        pending_products = remaining

    return registry