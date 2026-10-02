from __future__ import annotations

from dataclasses import dataclass, field

from aquasentinel.provenance.models import (
    DerivedProductRecord,
    SourceRecord,
)


@dataclass
class ProvenanceRegistry:
    sources: dict[str, SourceRecord] = field(default_factory=dict)
    derived_products: dict[str, DerivedProductRecord] = field(
        default_factory=dict
    )

    def add_source(self, record: SourceRecord) -> None:
        record.validate()

        if record.source_id in self.sources:
            raise ValueError(
                f"Duplicate source_id: {record.source_id}"
            )

        self.sources[record.source_id] = record

    def add_derived_product(
        self,
        record: DerivedProductRecord,
    ) -> None:
        record.validate()

        if record.product_id in self.derived_products:
            raise ValueError(
                f"Duplicate derived product_id: {record.product_id}"
            )

        missing_source_ids = [
            source_id
            for source_id in record.source_ids
            if not self._record_exists(source_id)
        ]

        if missing_source_ids:
            missing = ", ".join(missing_source_ids)
            raise ValueError(
                "Derived product references unknown source IDs: "
                f"{missing}"
            )

        self.derived_products[record.product_id] = record

    def get_source(self, source_id: str) -> SourceRecord:
        try:
            return self.sources[source_id]
        except KeyError as exc:
            raise KeyError(
                f"Unknown source_id: {source_id}"
            ) from exc

    def get_derived_product(
        self,
        product_id: str,
    ) -> DerivedProductRecord:
        try:
            return self.derived_products[product_id]
        except KeyError as exc:
            raise KeyError(
                f"Unknown derived product_id: {product_id}"
            ) from exc

    def get_lineage(
        self,
        product_id: str,
    ) -> tuple[str, ...]:
        if product_id not in self.derived_products:
            raise KeyError(
                f"Unknown derived product_id: {product_id}"
            )

        visited: set[str] = set()
        lineage: list[str] = []

        def walk(record_id: str) -> None:
            if record_id in visited:
                return

            visited.add(record_id)

            if record_id in self.sources:
                lineage.append(record_id)
                return

            derived = self.derived_products.get(record_id)

            if derived is None:
                raise KeyError(
                    f"Broken provenance reference: {record_id}"
                )

            for source_id in derived.source_ids:
                walk(source_id)

            lineage.append(record_id)

        walk(product_id)

        return tuple(lineage)

    def _record_exists(self, record_id: str) -> bool:
        return (
            record_id in self.sources
            or record_id in self.derived_products
        )