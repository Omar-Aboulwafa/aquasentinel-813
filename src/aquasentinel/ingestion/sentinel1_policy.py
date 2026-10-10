"""Frozen Decision-054 Sentinel-1 identities and immutable AS-201 data types."""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass, replace
from datetime import UTC, date, datetime
from hashlib import sha256
from math import isfinite
from typing import Any
from urllib.parse import quote, urlsplit

from aquasentinel.provenance import SourceRecord

POLICY_VERSION = "as201-v1"


REPRESENTATION = "RAW_GRD_AMPLITUDE"


ENVELOPE_ID = "KHARG_P0_VALIDATION_ENVELOPE"


ENVELOPE_BBOX = (49.60, 28.60, 50.70, 29.60)


ENVELOPE_GEOMETRY: dict[str, Any] = {
    "type": "Polygon",
    "coordinates": [[
        [49.60, 28.60],
        [50.70, 28.60],
        [50.70, 29.60],
        [49.60, 29.60],
        [49.60, 28.60],
    ]],
}


ROLE_ORDER = ("REFERENCE", "DOCUMENTARY_EVENT", "LATE_FOLLOW_UP")


REQUIRED_POLARIZATIONS = ("VV", "VH")


REQUIRED_VV_ASSETS = ("measurement_vv", "manifest", "product_vv", "calibration_vv", "noise_vv")


class Sentinel1RetrievalError(ValueError):
    """Frozen-source identity, metadata, or retrieval contract was violated."""


class Sentinel1MetadataError(Sentinel1RetrievalError):
    """Header/XML metadata is invalid, contradictory, or belongs to another source."""


@dataclass(frozen=True)
class FrozenSentinel1Source:
    role: str
    slice_order: int
    cdse_item_id: str
    pc_item_id: str
    native_source_product_id: str
    acquisition_start: datetime
    acquisition_end: datetime
    absolute_orbit: int
    width: int
    height: int

    @property
    def acquisition_date(self) -> date:
        return self.acquisition_start.date()


@dataclass(frozen=True)
class Sentinel1AssetReference:
    purpose: str
    key: str
    href: str
    media_type: str | None
    roles: tuple[str, ...] = ()


@dataclass(frozen=True)
class Sentinel1HeaderSummary:
    width: int
    height: int
    bits_per_sample: int
    samples_per_pixel: int
    compression: int
    tile_width: int
    tile_height: int
    sample_format: int
    nodata: str | None
    tiepoint_count: int
    overview_count: int | None
    has_model_pixel_scale: bool
    has_model_transformation: bool


@dataclass(frozen=True)
class Sentinel1MetadataSummary:
    product_root: str
    calibration_root: str
    noise_root: str
    manifest_root: str
    thermal_noise_correction_performed: bool | None
    product_width: int
    product_height: int
    calibration_has_beta0: bool
    calibration_has_sigma0: bool
    calibration_has_gamma: bool
    calibration_has_dn: bool
    noise_has_range: bool
    noise_has_azimuth: bool


@dataclass(frozen=True)
class Sentinel1SliceSource:
    policy: FrozenSentinel1Source
    availability: str
    reason: str | None
    discovery_source: SourceRecord | None
    source: SourceRecord | None
    footprint: dict[str, Any] | None
    bbox: tuple[float, float, float, float] | None
    assets: tuple[Sentinel1AssetReference, ...]
    provider_metadata: dict[str, Any]
    representation: str
    header: Sentinel1HeaderSummary | None = None
    metadata: Sentinel1MetadataSummary | None = None
    fingerprint: str = ""

    def asset(self, purpose: str) -> Sentinel1AssetReference:
        matches = [asset for asset in self.assets if asset.purpose == purpose]
        if len(matches) != 1:
            raise Sentinel1RetrievalError(f"Expected one {purpose} asset; found {len(matches)}.")
        return matches[0]


@dataclass(frozen=True)
class Sentinel1AcquisitionGroup:
    role: str
    acquisition_date: date
    slices: tuple[Sentinel1SliceSource, ...]

    @property
    def ready(self) -> bool:
        return len(self.slices) == 2 and all(
            source.availability == "AVAILABLE" for source in self.slices
        )


@dataclass(frozen=True)
class Sentinel1RetrievalSet:
    policy_version: str
    envelope_id: str
    envelope_bbox: tuple[float, float, float, float]
    envelope_geometry: dict[str, Any]
    groups: tuple[Sentinel1AcquisitionGroup, ...]
    fingerprint: str

    @property
    def ready(self) -> bool:
        return len(self.groups) == 3 and all(group.ready for group in self.groups)

    @property
    def slices(self) -> tuple[Sentinel1SliceSource, ...]:
        return tuple(source for group in self.groups for source in group.slices)


def _dt(value: str) -> datetime:
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        raise RuntimeError("Frozen Sentinel-1 timestamp must be timezone-aware.")
    return parsed.astimezone(UTC)


FROZEN_SOURCES = (
    FrozenSentinel1Source(
        "REFERENCE", 1,
        "S1A_IW_GRDH_1SDV_20260424T144205_20260424T144230_064223_08158E_4192_COG",
        "S1A_IW_GRDH_1SDV_20260424T144205_20260424T144230_064223_08158E",
        "S1A_IW_GRDH_1SDV_20260424T144205_20260424T144230_064223_08158E_4192",
        _dt("2026-04-24T14:42:05.150515Z"), _dt("2026-04-24T14:42:30.148548Z"),
        64223, 25835, 16732,
    ),
    FrozenSentinel1Source(
        "REFERENCE", 2,
        "S1A_IW_GRDH_1SDV_20260424T144230_20260424T144255_064223_08158E_BA3A_COG",
        "S1A_IW_GRDH_1SDV_20260424T144230_20260424T144255_064223_08158E",
        "S1A_IW_GRDH_1SDV_20260424T144230_20260424T144255_064223_08158E_BA3A",
        _dt("2026-04-24T14:42:30.150042Z"), _dt("2026-04-24T14:42:55.148075Z"),
        64223, 25842, 16732,
    ),
    FrozenSentinel1Source(
        "DOCUMENTARY_EVENT", 1,
        "S1A_IW_GRDH_1SDV_20260506T144204_20260506T144229_064398_081C09_BF44_COG",
        "S1A_IW_GRDH_1SDV_20260506T144204_20260506T144229_064398_081C09",
        "S1A_IW_GRDH_1SDV_20260506T144204_20260506T144229_064398_081C09_BF44",
        _dt("2026-05-06T14:42:04.538690Z"), _dt("2026-05-06T14:42:29.536703Z"),
        64398, 25835, 16732,
    ),
    FrozenSentinel1Source(
        "DOCUMENTARY_EVENT", 2,
        "S1A_IW_GRDH_1SDV_20260506T144229_20260506T144254_064398_081C09_A43B_COG",
        "S1A_IW_GRDH_1SDV_20260506T144229_20260506T144254_064398_081C09",
        "S1A_IW_GRDH_1SDV_20260506T144229_20260506T144254_064398_081C09_A43B",
        _dt("2026-05-06T14:42:29.538209Z"), _dt("2026-05-06T14:42:54.536224Z"),
        64398, 25842, 16732,
    ),
    FrozenSentinel1Source(
        "LATE_FOLLOW_UP", 1,
        "S1A_IW_GRDH_1SDV_20260518T144204_20260518T144229_064573_082235_34DC_COG",
        "S1A_IW_GRDH_1SDV_20260518T144204_20260518T144229_064573_082235",
        "S1A_IW_GRDH_1SDV_20260518T144204_20260518T144229_064573_082235_34DC",
        _dt("2026-05-18T14:42:04.240283Z"), _dt("2026-05-18T14:42:29.238414Z"),
        64573, 25836, 16732,
    ),
    FrozenSentinel1Source(
        "LATE_FOLLOW_UP", 2,
        "S1A_IW_GRDH_1SDV_20260518T144229_20260518T144254_064573_082235_E298_COG",
        "S1A_IW_GRDH_1SDV_20260518T144229_20260518T144254_064573_082235",
        "S1A_IW_GRDH_1SDV_20260518T144229_20260518T144254_064573_082235_E298",
        _dt("2026-05-18T14:42:29.239908Z"), _dt("2026-05-18T14:42:54.239534Z"),
        64573, 25843, 16733,
    ),
)


def _stable_json(value: Any) -> bytes:
    def validate(node: Any) -> None:
        if isinstance(node, dict):
            for key, item in node.items():
                if not isinstance(key, str):
                    raise Sentinel1RetrievalError("Stable metadata keys must be strings.")
                validate(item)
        elif isinstance(node, (list, tuple)):
            for item in node:
                validate(item)
        elif isinstance(node, float) and not isfinite(node):
            raise Sentinel1RetrievalError("Stable metadata cannot contain NaN or infinity.")
        elif isinstance(node, str) and node.lower().startswith(("http://", "https://")):
            parsed = urlsplit(node)
            if parsed.query or parsed.fragment or parsed.username is not None:
                raise Sentinel1RetrievalError("Stable metadata cannot contain signed URLs.")

    validate(value)
    return json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        allow_nan=False,
    ).encode("utf-8")


def _fingerprint(value: Any) -> str:
    return sha256(_stable_json(value)).hexdigest()


def _source_record(
    *,
    endpoint: str,
    collection: str,
    item_id: str,
    platform: str,
    acquired_at: datetime,
    source_url: str | None,
    license_name: str | None,
) -> SourceRecord:
    provider_id = sha256(endpoint.rstrip("/").encode("utf-8")).hexdigest()
    record = SourceRecord(
        source_id=f"stac:{provider_id}:{quote(collection, safe='')}:{quote(item_id, safe='')}",
        platform=platform,
        product_id=item_id,
        acquired_at=acquired_at,
        catalog=endpoint,
        collection=collection,
        source_url=source_url,
        license_name=license_name,
    )
    record.validate()
    return record


def _parse_time(value: Any, field: str) -> datetime:
    if not isinstance(value, str) or not value.strip() or value != value.strip():
        raise Sentinel1RetrievalError(f"Sentinel-1 item has invalid {field}.")
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        raise Sentinel1RetrievalError(f"Sentinel-1 item has invalid {field}.") from None
    if parsed.tzinfo is None:
        raise Sentinel1RetrievalError(f"Sentinel-1 item {field} must be timezone-aware.")
    return parsed.astimezone(UTC)


def _slice_payload(source: Sentinel1SliceSource) -> dict[str, Any]:
    return {
        "policy": {
            **asdict(source.policy),
            "acquisition_start": source.policy.acquisition_start.isoformat(),
            "acquisition_end": source.policy.acquisition_end.isoformat(),
        },
        "availability": source.availability,
        "reason": source.reason,
        "discovery_source_id": (
            source.discovery_source.source_id if source.discovery_source else None
        ),
        "source_id": source.source.source_id if source.source else None,
        "footprint": source.footprint,
        "bbox": source.bbox,
        "assets": [asdict(asset) for asset in source.assets],
        "provider_metadata": source.provider_metadata,
        "representation": source.representation,
        "header": asdict(source.header) if source.header else None,
        "metadata": asdict(source.metadata) if source.metadata else None,
    }


def _with_fingerprint(source: Sentinel1SliceSource) -> Sentinel1SliceSource:
    return replace(source, fingerprint=_fingerprint(_slice_payload(source)))

