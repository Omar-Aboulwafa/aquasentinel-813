"""Exact CDSE-to-Planetary-Computer Sentinel-1 source resolver for AS-201."""

from __future__ import annotations

import json
import re
from math import isfinite
from typing import Any
from urllib.parse import urlsplit, urlunsplit

from aquasentinel.catalog.stac import search_catalog
from aquasentinel.config import SARConfig, STACConfig
from aquasentinel.ingestion.planetary_computer import AssetAccessError, validate_asset_href
from aquasentinel.ingestion.sentinel1_coverage import canonical_geometry
from aquasentinel.ingestion.sentinel1_policy import (
    ENVELOPE_GEOMETRY,
    FROZEN_SOURCES,
    REPRESENTATION,
    FrozenSentinel1Source,
    Sentinel1AssetReference,
    Sentinel1RetrievalError,
    Sentinel1RetrievalSet,
    Sentinel1SliceSource,
    _parse_time,
    _source_record,
    _with_fingerprint,
    assemble_retrieval,
)
from aquasentinel.provenance import SourceRecord


def _normalize_platform(value: Any) -> str:
    if not isinstance(value, str):
        raise Sentinel1RetrievalError("Sentinel-1 platform is missing or invalid.")
    platform = value.strip().lower().replace("_", "-")
    if platform not in {"sentinel-1a"}:
        raise Sentinel1RetrievalError("Frozen AS-201 sources must be Sentinel-1A.")
    return platform


def _stable_self_url(item: dict[str, Any], endpoint: str) -> str | None:
    links = item.get("links", [])
    if not isinstance(links, list) or any(not isinstance(link, dict) for link in links):
        raise Sentinel1RetrievalError("Sentinel-1 item links must be a list of objects.")
    self_links = [link.get("href") for link in links if link.get("rel") == "self"]
    if len(self_links) > 1:
        raise Sentinel1RetrievalError("Sentinel-1 item has conflicting self links.")
    if not self_links:
        return None
    href = self_links[0]
    if not isinstance(href, str) or not href.strip():
        raise Sentinel1RetrievalError("Sentinel-1 self link is invalid.")
    try:
        if not urlsplit(href).scheme:
            from urllib.parse import urljoin

            href = urljoin(endpoint, href)
        parsed = urlsplit(href)
        valid = (
            parsed.scheme == "https"
            and parsed.hostname
            and parsed.port in (None, 443)
            and not parsed.query
            and not parsed.fragment
            and parsed.username is None
            and parsed.password is None
            and not any(c.isspace() for c in href)
        )
    except ValueError:
        valid = False
    if not valid:
        raise Sentinel1RetrievalError("Stable Sentinel-1 self URL must be unsigned HTTPS.")
    return href


def _normalize_bbox(value: Any) -> tuple[float, float, float, float]:
    if not isinstance(value, list) or len(value) != 4:
        raise Sentinel1RetrievalError("Sentinel-1 item bbox must contain four numbers.")
    if any(
        isinstance(v, bool) or not isinstance(v, (int, float)) or not isfinite(v) for v in value
    ):
        raise Sentinel1RetrievalError("Sentinel-1 bbox must contain finite numbers.")
    bbox = tuple(float(v) for v in value)
    if not (-180 <= bbox[0] <= bbox[2] <= 180 and -90 <= bbox[1] <= bbox[3] <= 90):
        raise Sentinel1RetrievalError("Sentinel-1 bbox is outside valid WGS84 bounds.")
    return bbox  # type: ignore[return-value]


def _normalize_item(
    item: dict[str, Any],
    expected: FrozenSentinel1Source,
    *,
    endpoint: str,
    collection: str,
    expected_item_id: str,
    license_name: str | None,
) -> tuple[SourceRecord, dict[str, Any], tuple[float, float, float, float], dict[str, Any]]:
    if not isinstance(item, dict) or item.get("type") != "Feature":
        raise Sentinel1RetrievalError("Sentinel-1 STAC item must be a Feature.")
    if item.get("id") != expected_item_id or item.get("collection") != collection:
        raise Sentinel1RetrievalError("Sentinel-1 item identity/collection mismatch.")
    props = item.get("properties")
    if not isinstance(props, dict):
        raise Sentinel1RetrievalError("Sentinel-1 item properties must be an object.")

    start = _parse_time(props.get("start_datetime"), "start_datetime")
    end = _parse_time(props.get("end_datetime"), "end_datetime")
    if start != expected.acquisition_start or end != expected.acquisition_end or start >= end:
        raise Sentinel1RetrievalError(
            "Sentinel-1 acquisition interval conflicts with frozen source."
        )
    platform = _normalize_platform(props.get("platform"))
    if props.get("sar:instrument_mode") != "IW":
        raise Sentinel1RetrievalError("Sentinel-1 source must use IW mode.")
    pols = props.get("sar:polarizations")
    if not isinstance(pols, list) or tuple(sorted(str(p).upper() for p in pols)) != ("VH", "VV"):
        raise Sentinel1RetrievalError("Sentinel-1 source must expose dual VV/VH polarization.")
    if str(props.get("sat:orbit_state", "")).lower() != "ascending":
        raise Sentinel1RetrievalError("Sentinel-1 source must use ascending orbit direction.")
    if type(props.get("sat:relative_orbit")) is not int or props["sat:relative_orbit"] != 101:
        raise Sentinel1RetrievalError("Sentinel-1 source has wrong relative orbit.")
    absolute = props.get("sat:absolute_orbit")
    if absolute is not None and (type(absolute) is not int or absolute != expected.absolute_orbit):
        raise Sentinel1RetrievalError("Sentinel-1 source has wrong absolute orbit.")

    geometry = item.get("geometry")
    if not isinstance(geometry, dict) or geometry.get("type") not in {"Polygon", "MultiPolygon"}:
        raise Sentinel1RetrievalError("Sentinel-1 item requires Polygon/MultiPolygon geometry.")
    try:
        geometry = canonical_geometry(geometry)
    except (ValueError, TypeError):
        raise Sentinel1RetrievalError("Source footprint topology is invalid.") from None
    bbox = _normalize_bbox(item.get("bbox"))
    product = props.get("sar:product_type", props.get("s1:product_type", props.get("product:type")))
    # CDSE's exact IW high-resolution Level-1 GRD alias; retain field precedence.
    if product not in {"GRD", "GRDH", "IW_GRDH_1S"}:
        raise Sentinel1RetrievalError("Source is not GRDH-compatible Level-1 GRD.")
    native = props.get("s1:product_identifier")
    if expected_item_id == expected.pc_item_id and native != expected.native_source_product_id:
        raise Sentinel1RetrievalError("PC native source product identity mismatches.")
    if native is not None and native not in {
        expected.native_source_product_id,
        expected.cdse_item_id,
    }:
        raise Sentinel1RetrievalError("Native source product identifier mismatch.")
    for key in ("sar:pixel_spacing_range", "sar:pixel_spacing_azimuth"):
        value = props.get(key)
        if value is not None and (isinstance(value, bool) or value != 10):
            raise Sentinel1RetrievalError("Source sample spacing conflicts with raw GRDH.")
    source_url = _stable_self_url(item, endpoint)
    record = _source_record(
        endpoint=endpoint,
        collection=collection,
        item_id=expected_item_id,
        platform=platform,
        acquired_at=start,
        source_url=source_url,
        license_name=license_name,
    )
    return record, geometry, bbox, props


def _index_items(items: tuple[dict[str, Any], ...]) -> dict[str, list[dict[str, Any]]]:
    indexed: dict[str, list[dict[str, Any]]] = {}
    for item in items:
        if not isinstance(item, dict) or not isinstance(item.get("id"), str) or not item["id"]:
            raise Sentinel1RetrievalError("Catalog returned malformed Sentinel-1 item identity.")
        try:
            json.dumps(item, allow_nan=False)
        except (TypeError, ValueError):
            raise Sentinel1RetrievalError("Catalog metadata is not strict finite JSON.") from None
        indexed.setdefault(item["id"], []).append(item)
    return indexed


def classify_representation(item: dict[str, Any]) -> str:
    properties = item.get("properties", {})
    if not isinstance(properties, dict):
        return "UNKNOWN_REPRESENTATION"
    stated = properties.get("s1:representation", properties.get("representation"))
    if stated is not None:
        return (
            stated
            if stated in {"RAW_GRD_AMPLITUDE", "PROVIDER_CALIBRATED_BACKSCATTER", "RTC_GAMMA0"}
            else "UNKNOWN_REPRESENTATION"
        )
    if item.get("collection") == "sentinel-1-rtc":
        return "RTC_GAMMA0"
    if properties.get("s1:calibrated") is True:
        return "PROVIDER_CALIBRATED_BACKSCATTER"
    return (
        "RAW_GRD_AMPLITUDE"
        if item.get("collection") == "sentinel-1-grd"
        else ("UNKNOWN_REPRESENTATION")
    )


def _raw_asset(raw_assets: dict[str, Any], key: str) -> dict[str, Any] | None:
    value = raw_assets.get(key)
    return value if isinstance(value, dict) else None


def _measurement_asset(raw_assets: dict[str, Any], polarization: str) -> tuple[str, dict[str, Any]]:
    candidates: list[tuple[str, dict[str, Any]]] = []
    pattern = rf"(?:^|[-_/]){polarization.lower()}(?:[-_.]|$)"
    for key, asset in raw_assets.items():
        if not isinstance(key, str) or not isinstance(asset, dict):
            continue
        href = asset.get("href")
        try:
            path = urlsplit(href).path.lower() if isinstance(href, str) else ""
        except ValueError:
            raise Sentinel1RetrievalError("Measurement asset URL is malformed.") from None
        if "/measurement/" in path and re.search(pattern, path):
            candidates.append((key, asset))
    if len(candidates) != 1:
        raise Sentinel1RetrievalError(
            f"Expected one {polarization} measurement asset; found {len(candidates)}."
        )
    return candidates[0]


def _stable_asset(
    *, purpose: str, key: str, asset: dict[str, Any], settings: SARConfig
) -> Sentinel1AssetReference:
    href = asset.get("href")
    try:
        validate_asset_href(href, settings)
    except AssetAccessError:
        raise Sentinel1RetrievalError(
            f"{purpose} lacks an allowed stable HTTPS reference."
        ) from None
    media = asset.get("type")
    if media is not None and not isinstance(media, str):
        raise Sentinel1RetrievalError(f"{purpose} has invalid media type.")
    roles = asset.get("roles", [])
    if not isinstance(roles, list) or any(not isinstance(role, str) for role in roles):
        raise Sentinel1RetrievalError(f"{purpose} has invalid asset roles.")
    return Sentinel1AssetReference(purpose, key, href, media, tuple(sorted(set(roles))))


def _same_product_href(measurement_href: str, relative_path: str, settings: SARConfig) -> str:
    parsed = urlsplit(measurement_href)
    marker = "/measurement/"
    if marker not in parsed.path:
        raise Sentinel1RetrievalError("Measurement path does not expose a same-product root.")
    root = parsed.path.split(marker, 1)[0]
    href = urlunsplit((parsed.scheme, parsed.netloc, root + "/" + relative_path, "", ""))
    try:
        validate_asset_href(href, settings)
    except AssetAccessError:
        raise Sentinel1RetrievalError(
            "Normalized same-product asset path is not allowed."
        ) from None
    return href


def _resolved_assets(
    item: dict[str, Any], settings: SARConfig, expected: FrozenSentinel1Source
) -> tuple[Sentinel1AssetReference, ...]:
    raw_assets = item.get("assets")
    if not isinstance(raw_assets, dict):
        raise Sentinel1RetrievalError("Planetary Computer assets must be an object.")
    vv_key, vv_raw = _measurement_asset(raw_assets, "VV")
    vh_key, vh_raw = _measurement_asset(raw_assets, "VH")
    vv = _stable_asset(purpose="measurement_vv", key=vv_key, asset=vv_raw, settings=settings)
    vh = _stable_asset(purpose="measurement_vh", key=vh_key, asset=vh_raw, settings=settings)
    vv_url, vh_url = urlsplit(vv.href), urlsplit(vh.href)
    vv_root = vv_url.path.split("/measurement/", 1)[0]
    vh_root = vh_url.path.split("/measurement/", 1)[0]
    if (vv_url.scheme, vv_url.hostname, vv_url.port or 443, vv_root) != (
        vh_url.scheme,
        vh_url.hostname,
        vh_url.port or 443,
        vh_root,
    ):
        raise Sentinel1RetrievalError("VV/VH measurements do not share one product root.")

    # Both stable measurements must identify this exact native source root.
    for asset in (vv, vh):
        path = urlsplit(asset.href).path
        root = path.split("/measurement/", 1)[0]
        polarization = "vv" if asset.purpose == "measurement_vv" else "vh"
        if root.rsplit("/", 1)[-1] not in {
            expected.native_source_product_id,
            expected.native_source_product_id + ".SAFE",
        } or not path.startswith("/s1-grd/"):
            raise Sentinel1RetrievalError("Measurement path belongs to another source product.")
        if not re.search(rf"(?:^|[-_/]){polarization}(?:[-_.]|$)", path.rsplit("/", 1)[-1]):
            raise Sentinel1RetrievalError("Measurement filename has wrong polarization.")
    derived = {
        "manifest": ("normalized:manifest.safe", "manifest.safe"),
        "product_vv": ("normalized:annotation/iw-vv.xml", "annotation/iw-vv.xml"),
        "calibration_vv": (
            "normalized:annotation/calibration/calibration-iw-vv.xml",
            "annotation/calibration/calibration-iw-vv.xml",
        ),
        "noise_vv": (
            "normalized:annotation/calibration/noise-iw-vv.xml",
            "annotation/calibration/noise-iw-vv.xml",
        ),
    }
    resolved = [vv, vh]
    for purpose, (key, relative) in derived.items():
        resolved.append(
            Sentinel1AssetReference(
                purpose=purpose,
                key=key,
                href=_same_product_href(vv.href, relative, settings),
                media_type="application/xml",
            )
        )
    return tuple(resolved)


def _unavailable(
    policy: FrozenSentinel1Source,
    code: str,
    *,
    discovery_source: SourceRecord | None = None,
    source: SourceRecord | None = None,
    footprint: dict[str, Any] | None = None,
    bbox: tuple[float, float, float, float] | None = None,
) -> Sentinel1SliceSource:
    return _with_fingerprint(
        Sentinel1SliceSource(
            policy=policy,
            availability="UNAVAILABLE",
            reason=code,
            discovery_source=discovery_source,
            source=source,
            footprint=footprint,
            bbox=bbox,
            assets=(),
            provider_metadata={},
            representation=REPRESENTATION,
        )
    )


def build_retrieval_set(
    cdse_items: tuple[dict[str, Any], ...],
    pc_items: tuple[dict[str, Any], ...],
    settings: SARConfig,
    *,
    cdse_license: str | None = None,
    pc_license: str | None = None,
) -> Sentinel1RetrievalSet:
    """Resolve the exact Decision-054 set without any SAR pixel transformation."""
    settings.validate()
    cdse = _index_items(cdse_items)
    pc = _index_items(pc_items)
    slices: list[Sentinel1SliceSource] = []
    for policy in FROZEN_SOURCES:
        discoveries = cdse.get(policy.cdse_item_id, [])
        matches = [
            item
            for bucket in pc.values()
            for item in bucket
            if (
                item["id"] == policy.pc_item_id
                or (
                    isinstance(item.get("properties"), dict)
                    and item["properties"].get("s1:product_identifier")
                    == policy.native_source_product_id
                )
            )
        ]
        discovery_item = discoveries[0] if len(discoveries) == 1 else None
        pc_item = matches[0] if len(matches) == 1 else None
        if discovery_item is None:
            slices.append(
                _unavailable(
                    policy,
                    "DISCOVERY_SOURCE_MISSING" if not discoveries else "DISCOVERY_SOURCE_AMBIGUOUS",
                )
            )
            continue
        try:
            discovery_record, discovery_footprint, discovery_bbox, _ = _normalize_item(
                discovery_item,
                policy,
                endpoint=settings.discovery_endpoint,
                collection=settings.discovery_collection,
                expected_item_id=policy.cdse_item_id,
                license_name=cdse_license,
            )
        except Sentinel1RetrievalError:
            slices.append(_unavailable(policy, "DISCOVERY_IDENTITY_INVALID"))
            continue
        if pc_item is None:
            slices.append(
                _unavailable(
                    policy,
                    "PC_SOURCE_MISSING" if not matches else "PC_SOURCE_AMBIGUOUS",
                    discovery_source=discovery_record,
                    footprint=discovery_footprint,
                    bbox=discovery_bbox,
                )
            )
            continue
        try:
            source_record, geometry, bbox, props = _normalize_item(
                pc_item,
                policy,
                endpoint=settings.access_endpoint,
                collection=settings.access_collection,
                expected_item_id=policy.pc_item_id,
                license_name=pc_license,
            )
            if classify_representation(pc_item) != REPRESENTATION:
                raise Sentinel1RetrievalError("PC representation is not raw GRD amplitude.")
            assets = _resolved_assets(pc_item, settings, policy)
            provider_metadata = {
                key: props[key]
                for key in (
                    "sat:absolute_orbit",
                    "sat:relative_orbit",
                    "sat:orbit_state",
                    "sar:instrument_mode",
                    "sar:polarizations",
                    "s1:product_type",
                    "s1:resolution",
                    "s1:shape",
                    "proj:shape",
                    "s1:product_identifier",
                    "sar:product_type",
                    "sar:pixel_spacing_range",
                    "sar:pixel_spacing_azimuth",
                )
                if key in props
            }
            slices.append(
                _with_fingerprint(
                    Sentinel1SliceSource(
                        policy=policy,
                        availability="RESOLVED_NOT_ACCESSED",
                        reason=None,
                        discovery_source=discovery_record,
                        source=source_record,
                        footprint=geometry,
                        bbox=bbox,
                        assets=assets,
                        provider_metadata=provider_metadata,
                        representation=REPRESENTATION,
                    )
                )
            )
        except Sentinel1RetrievalError:
            slices.append(
                _unavailable(
                    policy,
                    "PC_IDENTITY_OR_ASSET_CONTRACT_INVALID",
                    discovery_source=discovery_record,
                    footprint=discovery_footprint,
                    bbox=discovery_bbox,
                )
            )

    return assemble_retrieval(tuple(slices))


def search_sentinel1(settings: SARConfig) -> Sentinel1RetrievalSet:
    """Search both providers with no optical/cloud query and resolve only the frozen six."""
    settings.validate()
    start = min(source.acquisition_start for source in FROZEN_SOURCES)
    end = max(source.acquisition_end for source in FROZEN_SOURCES)
    interval = (
        f"{start.isoformat().replace('+00:00', 'Z')}/{end.isoformat().replace('+00:00', 'Z')}"
    )
    # pystac-client deep-copies intersects; keep frozen policy metadata internal.
    geometry = json.loads(json.dumps(ENVELOPE_GEOMETRY, allow_nan=False))
    discovery = search_catalog(
        STACConfig(
            settings.discovery_endpoint,
            settings.discovery_collection,
            settings.timeout_seconds,
        ),
        intersects=geometry,
        datetime_interval=interval,
        query=None,
    )
    access = search_catalog(
        STACConfig(settings.access_endpoint, settings.access_collection, settings.timeout_seconds),
        intersects=geometry,
        datetime_interval=interval,
        query=None,
    )
    return build_retrieval_set(
        discovery.items,
        access.items,
        settings,
        cdse_license=discovery.license_name,
        pc_license=access.license_name,
    )
