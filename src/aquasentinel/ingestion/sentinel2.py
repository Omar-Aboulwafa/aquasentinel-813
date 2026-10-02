"""Discover and normalize Sentinel-2 candidate scenes without fetching imagery."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC, datetime, time
from hashlib import sha256
from math import isfinite
from typing import Any
from urllib.parse import quote, urljoin, urlsplit

from aquasentinel.catalog.stac import CatalogMetadataError, search_catalog
from aquasentinel.config import AOIFeature, STACConfig
from aquasentinel.provenance import SourceRecord
from aquasentinel.runtime import RuntimeContext


class InvalidSearchInputError(ValueError):
    """Configured AOI, dates, or cloud threshold cannot be used for this search."""


class MissingItemMetadataError(CatalogMetadataError):
    """An item is missing a required field; no default observation is invented."""


class MalformedItemMetadataError(CatalogMetadataError):
    """An item's supplied metadata is invalid or internally inconsistent."""


@dataclass(frozen=True)
class AssetReference:
    key: str
    href: str
    media_type: str | None
    roles: tuple[str, ...]


@dataclass(frozen=True)
class Sentinel2Candidate:
    item_id: str
    acquired_at: datetime
    platform: str
    collection: str
    cloud_cover_percent: float
    catalog: str
    source_url: str | None
    license_name: str | None
    assets: tuple[AssetReference, ...]

    def to_source_record(self) -> SourceRecord:
        # The complete endpoint digest qualifies IDs even for configurable providers.
        provider_id = sha256(self.catalog.rstrip("/").encode("utf-8")).hexdigest()
        source_id = (
            f"stac:{provider_id}:{quote(self.collection, safe='')}:{quote(self.item_id, safe='')}"
        )
        record = SourceRecord(
            source_id=source_id,
            platform=self.platform,
            product_id=self.item_id,
            acquired_at=self.acquired_at,
            catalog=self.catalog,
            collection=self.collection,
            source_url=self.source_url,
            license_name=self.license_name,
        )
        record.validate()
        return record


def _required_text(value: Any, field: str, item_id: str) -> str:
    if value is None:
        raise MissingItemMetadataError(f"Item {item_id!r} is missing {field}.")
    if not isinstance(value, str) or not value.strip() or value != value.strip():
        raise MalformedItemMetadataError(f"Item {item_id!r} has invalid {field}.")
    return value


def _optional_text(value: Any, field: str, item_id: str) -> str | None:
    return None if value is None else _required_text(value, field, item_id)


def normalize_item(
    item: dict[str, Any],
    settings: STACConfig,
    *,
    collection_license: str | None = None,
) -> Sentinel2Candidate:
    """Fail explicitly on unusable metadata rather than silently skipping items."""
    if not isinstance(item, dict) or item.get("type") != "Feature":
        raise MalformedItemMetadataError("STAC item must be a Feature object.")
    item_id = _required_text(item.get("id"), "id", "<unknown>")
    collection = _required_text(item.get("collection"), "collection", item_id)
    if collection != settings.collection:
        raise MalformedItemMetadataError(f"Item {item_id!r} belongs to an unexpected collection.")
    properties = item.get("properties")
    if properties is None:
        raise MissingItemMetadataError(f"Item {item_id!r} is missing properties.")
    if not isinstance(properties, dict):
        raise MalformedItemMetadataError(f"Item {item_id!r} properties must be an object.")

    timestamp = _required_text(properties.get("datetime"), "datetime", item_id)
    try:
        acquired_at = datetime.fromisoformat(timestamp)
    except ValueError as exc:
        raise MalformedItemMetadataError(f"Item {item_id!r} has invalid datetime.") from exc
    if acquired_at.utcoffset() is None:
        raise MalformedItemMetadataError(f"Item {item_id!r} datetime must be timezone-aware.")
    acquired_at = acquired_at.astimezone(UTC)
    platform = _required_text(properties.get("platform"), "platform", item_id)

    cloud_cover = properties.get("eo:cloud_cover")
    if cloud_cover is None:
        raise MissingItemMetadataError(f"Item {item_id!r} is missing eo:cloud_cover.")
    if (
        isinstance(cloud_cover, bool)
        or not isinstance(cloud_cover, (int, float))
        or not isfinite(cloud_cover)
        or not 0 <= cloud_cover <= 100
    ):
        raise MalformedItemMetadataError(f"Item {item_id!r} has invalid eo:cloud_cover.")

    links = item.get("links", [])
    if not isinstance(links, list) or any(not isinstance(link, dict) for link in links):
        raise MalformedItemMetadataError(f"Item {item_id!r} links must be a list of objects.")
    self_urls = {
        urljoin(settings.endpoint, _required_text(link.get("href"), "self href", item_id))
        for link in links
        if link.get("rel") == "self"
    }
    if len(self_urls) > 1:
        raise MalformedItemMetadataError(f"Item {item_id!r} has conflicting self links.")
    source_url = next(iter(self_urls), None)

    raw_assets = item.get("assets")
    if raw_assets is None or raw_assets == {}:
        raise MissingItemMetadataError(f"Item {item_id!r} is missing assets (asset references).")
    if not isinstance(raw_assets, dict):
        raise MalformedItemMetadataError(f"Item {item_id!r} assets must be an object.")
    assets = []
    for key, asset in raw_assets.items():
        _required_text(key, "asset key", item_id)
        if not isinstance(asset, dict):
            raise MalformedItemMetadataError(f"Item {item_id!r} asset {key!r} must be an object.")
        href = _required_text(asset.get("href"), f"asset {key} href", item_id)
        if not urlsplit(href).scheme:
            if source_url is None:
                raise MalformedItemMetadataError(
                    f"Item {item_id!r} has relative asset href without a self URL."
                )
            href = urljoin(source_url, href)
        roles = asset.get("roles", [])
        if not isinstance(roles, list):
            raise MalformedItemMetadataError(f"Item {item_id!r} asset roles must be a list.")
        assets.append(
            AssetReference(
                key=key,
                href=href,
                media_type=_optional_text(asset.get("type"), "asset type", item_id),
                roles=tuple(
                    sorted({_required_text(role, "asset role", item_id) for role in roles})
                ),
            )
        )

    license_name = _optional_text(properties.get("license"), "license", item_id)
    if license_name is None:
        license_name = _optional_text(collection_license, "collection license", item_id)
    candidate = Sentinel2Candidate(
        item_id=item_id,
        acquired_at=acquired_at,
        platform=platform,
        collection=collection,
        cloud_cover_percent=float(cloud_cover),
        catalog=settings.endpoint,
        source_url=source_url,
        license_name=license_name,
        assets=tuple(sorted(assets, key=lambda asset: asset.key)),
    )
    candidate.to_source_record()
    return candidate


def _polygon_geometry(aoi: AOIFeature) -> dict[str, Any]:
    if aoi.geometry_type != "Polygon":
        raise InvalidSearchInputError("Primary validation AOI must be a Polygon.")
    rings = aoi.coordinates
    if not isinstance(rings, list) or not rings:
        raise InvalidSearchInputError("AOI Polygon must contain linear rings.")
    for ring in rings:
        if not isinstance(ring, list) or len(ring) < 4 or ring[0] != ring[-1]:
            raise InvalidSearchInputError("AOI Polygon rings must be closed with >= 4 positions.")
        for position in ring:
            if not isinstance(position, list) or len(position) < 2:
                raise InvalidSearchInputError("AOI positions require longitude and latitude.")
            for value, bound in zip(position[:2], (180, 90)):
                if (
                    isinstance(value, bool)
                    or not isinstance(value, (int, float))
                    or not isfinite(value)
                    or not -bound <= value <= bound
                ):
                    raise InvalidSearchInputError("AOI coordinates must be finite WGS84 positions.")
    return {"type": "Polygon", "coordinates": rings}


def search_sentinel2(context: RuntimeContext) -> tuple[Sentinel2Candidate, ...]:
    """Return all metadata candidates, sorted by UTC acquisition time and item ID."""
    try:
        context.config.validate()
        geometry = _polygon_geometry(context.primary_validation_aoi)
        analysis = context.config.analysis
        if (
            isinstance(analysis.max_cloud_cover_percent, bool)
            or not isinstance(analysis.max_cloud_cover_percent, (int, float))
        ):
            raise InvalidSearchInputError("Cloud threshold must be a number, not a boolean.")
        start = datetime.combine(analysis.start_date, time.min, tzinfo=UTC)
        end = datetime.combine(analysis.end_date, time.max, tzinfo=UTC)
    except (TypeError, ValueError) as exc:
        raise InvalidSearchInputError(str(exc)) from exc

    interval = (
        f"{start.isoformat().replace('+00:00', 'Z')}/{end.isoformat().replace('+00:00', 'Z')}"
    )
    result = search_catalog(
        context.config.catalog,
        intersects=geometry,
        datetime_interval=interval,
        max_cloud_cover_percent=analysis.max_cloud_cover_percent,
    )
    by_id: dict[str, Sentinel2Candidate] = {}
    for item in result.items:
        candidate = normalize_item(
            item, context.config.catalog, collection_license=result.license_name
        )
        previous = by_id.get(candidate.item_id)
        if previous is not None and previous != candidate:
            raise MalformedItemMetadataError(
                f"Conflicting duplicate metadata for item {candidate.item_id!r}."
            )
        by_id[candidate.item_id] = candidate

    # Recheck returned values: a catalog ignoring filters cannot widen the dataset.
    return tuple(
        sorted(
            (
                candidate
                for candidate in by_id.values()
                if start <= candidate.acquired_at <= end
                and candidate.cloud_cover_percent <= analysis.max_cloud_cover_percent
            ),
            key=lambda candidate: (candidate.acquired_at, candidate.item_id),
        )
    )
