"""STAC transport using pystac-client, with explicit response validation."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any

from pystac_client import Client
from pystac_client.stac_api_io import StacApiIO

from aquasentinel.config import STACConfig


class CatalogMetadataError(ValueError):
    """The catalog returned an invalid STAC response, not a valid empty search."""


@dataclass(frozen=True)
class CatalogResult:
    items: tuple[dict[str, Any], ...]
    license_name: str | None


class _SearchIO(StacApiIO):
    """Validate pages before the library can interpret missing features as empty."""

    def __init__(self, *, timeout: float) -> None:
        super().__init__(timeout=timeout, max_retries=0)
        self.validate_search_pages = False
        self._seen_next_links: set[str] = set()

    def read_json(self, source: Any, *args: Any, **kwargs: Any) -> dict[str, Any]:
        try:
            payload = super().read_json(source, *args, **kwargs)
        except ValueError as exc:
            raise CatalogMetadataError("Catalog response is not valid JSON.") from exc

        if not isinstance(payload, dict):
            raise CatalogMetadataError("Catalog response must be a JSON object.")
        if self.validate_search_pages:
            if payload.get("type") != "FeatureCollection":
                raise CatalogMetadataError("Search page must be a STAC FeatureCollection.")
            features = payload.get("features")
            if not isinstance(features, list):
                raise CatalogMetadataError("Search page must contain a features list.")
            links = payload.get("links", [])
            if not isinstance(links, list) or any(not isinstance(link, dict) for link in links):
                raise CatalogMetadataError("Search page links must be a list of objects.")
            next_links = [link for link in links if link.get("rel") == "next"]
            if len(next_links) > 1:
                raise CatalogMetadataError("Search page has ambiguous pagination links.")
            for link in links:
                if not isinstance(link.get("rel"), str):
                    raise CatalogMetadataError("Search page link is missing rel.")
                if link["rel"] == "next":
                    if not isinstance(link.get("href"), str) or not link["href"].strip():
                        raise CatalogMetadataError("Pagination link is missing href.")
                    if not features:
                        raise CatalogMetadataError(
                            "Empty page advertises a next page; refusing incomplete results."
                        )
                    fingerprint = json.dumps(link, sort_keys=True)
                    if fingerprint in self._seen_next_links:
                        raise CatalogMetadataError("Pagination repeats a next link.")
                    self._seen_next_links.add(fingerprint)
        return payload


def search_catalog(
    settings: STACConfig,
    *,
    intersects: dict[str, Any],
    datetime_interval: str,
    max_cloud_cover_percent: float,
) -> CatalogResult:
    """Consume all search pages. API/network errors propagate to the caller."""
    settings.validate()
    io = _SearchIO(timeout=settings.timeout_seconds)
    try:
        client = Client.open(settings.endpoint, stac_io=io, timeout=settings.timeout_seconds)
        collection = client.get_collection(settings.collection)
        license_name = collection.license
        if license_name is not None and (
            not isinstance(license_name, str) or not license_name.strip()
        ):
            raise CatalogMetadataError("Collection license must be a non-empty string.")
        search = client.search(
            collections=[settings.collection],
            intersects=intersects,
            datetime=datetime_interval,
            query={"eo:cloud_cover": {"lte": max_cloud_cover_percent}},
            max_items=None,
        )
        io.validate_search_pages = True
        items = tuple(search.items_as_dicts())
    except CatalogMetadataError:
        raise
    except (KeyError, TypeError, ValueError) as exc:
        raise CatalogMetadataError(f"Malformed catalog metadata: {exc}") from exc
    return CatalogResult(items=items, license_name=license_name)
