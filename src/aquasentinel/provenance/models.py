from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any


@dataclass(frozen=True)
class SourceRecord:
    source_id: str
    platform: str
    product_id: str
    acquired_at: datetime
    catalog: str
    collection: str | None = None
    source_url: str | None = None
    license_name: str | None = None

    def validate(self) -> None:
        if not self.source_id.strip():
            raise ValueError("source_id cannot be empty.")

        if not self.platform.strip():
            raise ValueError("platform cannot be empty.")

        if not self.product_id.strip():
            raise ValueError("product_id cannot be empty.")

        if not self.catalog.strip():
            raise ValueError("catalog cannot be empty.")

        if self.acquired_at.tzinfo is None:
            raise ValueError("acquired_at must be timezone-aware.")


@dataclass(frozen=True)
class DerivedProductRecord:
    product_id: str
    product_type: str
    created_at: datetime
    processing_version: str
    source_ids: tuple[str, ...]
    parameters: dict[str, Any]

    def validate(self) -> None:
        if not self.product_id.strip():
            raise ValueError("Derived product_id cannot be empty.")

        if not self.product_type.strip():
            raise ValueError("product_type cannot be empty.")

        if not self.processing_version.strip():
            raise ValueError("processing_version cannot be empty.")

        if self.created_at.tzinfo is None:
            raise ValueError("created_at must be timezone-aware.")

        if not self.source_ids:
            raise ValueError(
                "Derived product must reference at least one source record."
            )

        if any(not source_id.strip() for source_id in self.source_ids):
            raise ValueError("source_ids cannot contain empty values.")