"""Strict cross-provider observation matching and native asset resolution."""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from datetime import UTC, datetime, timedelta
from typing import Any
from urllib.parse import urlsplit

from aquasentinel.catalog.stac import search_catalog
from aquasentinel.config import OpticalConfig, STACConfig
from aquasentinel.ingestion.planetary_computer import AssetAccessError, validate_asset_href
from aquasentinel.ingestion.sentinel2 import AssetReference, Sentinel2Candidate, normalize_item
from aquasentinel.provenance.models import SourceRecord

BANDS = ("B02", "B03", "B04", "B05", "B06", "B07", "B08", "B8A", "B11")
REQUIRED_ASSETS = (*BANDS, "SCL", "product-metadata")
NATIVE_RESOLUTION = {
    key: (10 if key in {"B02", "B03", "B04", "B08"} else 20) for key in (*BANDS, "SCL")
}
CDSE_ID = re.compile(
    r"S2([AB])_MSIL2A_(\d{8}T\d{6})_N(\d{4})_R(\d{3})_T(\d{2}[C-HJ-NP-X][A-HJ-NP-Z]{2})_(\d{8}T\d{6})"
)
PC_ID = re.compile(
    r"S2([AB])_MSIL2A_(\d{8}T\d{6})_R(\d{3})_T(\d{2}[C-HJ-NP-X][A-HJ-NP-Z]{2})_(\d{8}T\d{6})"
)


class ObservationMatchError(ValueError):
    """Missing, conflicting or ambiguous observation identity."""


@dataclass(frozen=True)
class ObservationIdentity:
    acquired_at: datetime
    platform: str
    tile: str
    relative_orbit: int

    def to_dict(self) -> dict[str, Any]:
        return {
            "acquired_at": self.acquired_at.isoformat(),
            "platform": self.platform,
            "mgrs_tile": self.tile,
            "relative_orbit": self.relative_orbit,
        }


@dataclass(frozen=True)
class ResolvedOpticalSource:
    source: SourceRecord
    discovery_source: SourceRecord
    identity: ObservationIdentity
    processing_baseline: str
    generation_time: str
    discovery_processing: dict[str, Any]
    assets: tuple[AssetReference, ...]
    provider_metadata: dict[str, Any]
    native_grids: dict[str, dict[str, Any]] = field(default_factory=dict)
    decoding_metadata: dict[str, Any] = field(default_factory=dict)

    def asset(self, key: str) -> AssetReference:
        return next(asset for asset in self.assets if asset.key == key)


def _date(text: str) -> datetime:
    try:
        return datetime.strptime(text, "%Y%m%dT%H%M%S").replace(tzinfo=UTC)
    except ValueError:
        raise ObservationMatchError("Product ID has an invalid date.") from None


def _platform(text: str) -> str:
    normalized = text.lower().replace("_", "-")
    if normalized not in {"sentinel-2a", "sentinel-2b"}:
        raise ObservationMatchError("Unsupported Sentinel-2 platform.")
    return normalized


def discovery_identity(candidate: Sentinel2Candidate) -> tuple[ObservationIdentity, dict[str, Any]]:
    match = CDSE_ID.fullmatch(candidate.item_id)
    if not match:
        raise ObservationMatchError("CDSE product ID cannot be safely parsed.")
    satellite, acquired, baseline, orbit, tile, generation = match.groups()
    platform = _platform(candidate.platform)
    if (
        platform != f"sentinel-2{satellite.lower()}"
        or candidate.acquired_at.replace(microsecond=0) != _date(acquired)
        or candidate.acquired_at.tzinfo is None
    ):
        raise ObservationMatchError("CDSE metadata conflicts with its product ID.")
    if not 1 <= int(tile[:2]) <= 60:
        raise ObservationMatchError("Invalid MGRS UTM zone.")
    orbit_number = int(orbit)
    if not 1 <= orbit_number <= 143:
        raise ObservationMatchError("Invalid relative orbit.")
    return ObservationIdentity(candidate.acquired_at, platform, tile, orbit_number), {
        "processing_baseline": f"{baseline[:2]}.{baseline[2:]}",
        "generation_time": _date(generation).isoformat(),
    }


def _pc_identity(item: dict[str, Any]) -> tuple[ObservationIdentity, str, str]:
    try:
        props = item["properties"]
        match = PC_ID.fullmatch(item["id"])
        if not match:
            raise ValueError
        satellite, acquired, orbit, tile, generation = match.groups()
        timestamp = datetime.fromisoformat(props["datetime"]).astimezone(UTC)
        if datetime.fromisoformat(props["datetime"]).tzinfo is None:
            raise ValueError
        platform = _platform(props["platform"])
        metadata_tile = props["s2:mgrs_tile"]
        if any(
            key in props for key in ("s2:utm_zone", "s2:latitude_band", "s2:grid_square")
        ) and metadata_tile != (
            f"{int(props['s2:utm_zone']):02d}{props['s2:latitude_band']}{props['s2:grid_square']}"
        ):
            raise ValueError
        metadata_orbit = props["sat:relative_orbit"]
        baseline = props["s2:processing_baseline"]
        generated = props["s2:generation_time"]
        generation_date = datetime.fromisoformat(generated)
        if (
            platform != f"sentinel-2{satellite.lower()}"
            or tile != metadata_tile
            or not 1 <= int(tile[:2]) <= 60
            or type(metadata_orbit) is not int
            or metadata_orbit != int(orbit)
            or not 1 <= int(orbit) <= 143
            or timestamp.replace(microsecond=0) != _date(acquired)
            or generation_date.tzinfo is None
            or generation_date.astimezone(UTC).replace(microsecond=0) != _date(generation)
            or not isinstance(baseline, str)
            or not re.fullmatch(r"\d{2}\.\d{2}", baseline)
        ):
            raise ValueError
        if "s2:product_uri" in props:
            uri_match = CDSE_ID.fullmatch(props["s2:product_uri"].removesuffix(".SAFE"))
            if not uri_match:
                raise ValueError
            uri_satellite, uri_acquired, uri_baseline, uri_orbit, uri_tile, uri_generation = (
                uri_match.groups()
            )
            if (uri_satellite, uri_acquired, uri_orbit, uri_tile, uri_generation) != (
                satellite,
                acquired,
                orbit,
                tile,
                generation,
            ) or baseline != f"{uri_baseline[:2]}.{uri_baseline[2:]}":
                raise ValueError
        return ObservationIdentity(timestamp, platform, tile, int(orbit)), baseline, generated
    except (KeyError, TypeError, ValueError, AttributeError):
        raise ObservationMatchError(
            "PC observation metadata is missing or conflicts with product ID."
        ) from None


def match_and_resolve(
    candidate: Sentinel2Candidate,
    items: tuple[dict[str, Any], ...],
    settings: OpticalConfig,
    *,
    license_name: str | None = None,
) -> ResolvedOpticalSource:
    settings.validate()
    expected, discovery_processing = discovery_identity(candidate)
    matches = []
    for item in items:
        identity, baseline, generated = _pc_identity(item)
        if identity == expected:
            matches.append((item, identity, baseline, generated))
    if len(matches) != 1:
        raise ObservationMatchError(
            f"Expected exactly one PC observation match; found {len(matches)}."
        )
    item, identity, baseline, generated = matches[0]
    raw_assets = item.get("assets", {})
    if not isinstance(raw_assets, dict):
        raise ObservationMatchError("PC assets must be an object.")
    selected = {}
    for key in REQUIRED_ASSETS:
        asset = raw_assets.get(key)
        if not isinstance(asset, dict):
            raise ObservationMatchError(f"Required PC asset {key} is missing.")
        try:
            validate_asset_href(asset.get("href"), settings)
        except AssetAccessError:
            valid_href = False
        else:
            valid_href = True
        if not valid_href:
            raise ObservationMatchError(
                f"Required PC asset {key} lacks a valid stable unsigned HTTPS reference."
            ) from None
        media = asset.get("type", "")
        if not isinstance(media, str):
            raise ObservationMatchError(f"PC asset {key} lacks a media type.")
        if (key == "product-metadata" and "xml" not in media) or (
            key != "product-metadata" and ("tiff" not in media or "cloud-optimized" not in media)
        ):
            raise ObservationMatchError(
                f"PC asset {key} is not the expected native XML/COG format."
            )
        selected[key] = asset
    # Normalize only selected unsigned assets; previews or irrelevant keys are not pixel sources.
    minimal = {**item, "assets": selected}
    normalized = normalize_item(
        minimal,
        STACConfig(settings.endpoint, settings.collection, settings.timeout_seconds),
        collection_license=license_name,
    )
    for record in (normalized.to_source_record(), candidate.to_source_record()):
        if record.source_url is not None:
            parsed = urlsplit(record.source_url)
            if parsed.query or parsed.fragment or parsed.username is not None:
                raise ObservationMatchError(
                    "Stable source reference must not contain signing credentials."
                )
    return ResolvedOpticalSource(
        normalized.to_source_record(),
        candidate.to_source_record(),
        identity,
        baseline,
        generated,
        discovery_processing,
        tuple(normalized.assets),
        {
            key: value
            for key, value in item["properties"].items()
            if key
            in {
                "s2:product_uri",
                "s2:granule_id",
                "s2:datatake_id",
                "s2:datastrip_id",
                "proj:epsg",
                "s2:product_type",
                "sat:orbit_state",
            }
        },
    )


def resolve_optical_source(
    candidate: Sentinel2Candidate, geometry: dict[str, Any], settings: OpticalConfig
) -> ResolvedOpticalSource:
    expected, _ = discovery_identity(candidate)
    start, end = (
        expected.acquired_at - timedelta(seconds=1),
        expected.acquired_at + timedelta(seconds=1),
    )
    result = search_catalog(
        STACConfig(settings.endpoint, settings.collection, settings.timeout_seconds),
        intersects=geometry,
        datetime_interval=f"{start.isoformat()}/{end.isoformat()}",
        max_cloud_cover_percent=100,
    )
    return match_and_resolve(candidate, result.items, settings, license_name=result.license_name)
