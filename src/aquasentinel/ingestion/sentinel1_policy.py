"""Frozen Decision-054 Sentinel-1 identities and immutable AS-201 data types."""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field, replace
from datetime import UTC, date, datetime
from hashlib import sha256
from math import isfinite
from typing import Any
from urllib.parse import quote, urlsplit

from aquasentinel.config import SARConfig
from aquasentinel.ingestion.planetary_computer import AssetAccessError, validate_asset_href
from aquasentinel.provenance import DerivedProductRecord, ProvenanceRegistry, SourceRecord
from aquasentinel.provenance.serialization import source_record_to_dict

from .sentinel1_coverage import common_coverage, coverage


class FrozenJSON(dict):
    """JSON-serializable immutable mapping; nested sequences are immutable tuples."""

    def _deny(self, *args, **kwargs):
        raise TypeError("AS-201 metadata is immutable.")

    __setitem__ = __delitem__ = clear = pop = popitem = setdefault = update = __ior__ = _deny


def _freeze(value: Any) -> Any:
    if isinstance(value, dict):
        return FrozenJSON({k: _freeze(v) for k, v in value.items()})
    if isinstance(value, (list, tuple)):
        return tuple(_freeze(v) for v in value)
    return value


POLICY_VERSION = "as201-v1"


REPRESENTATION = "RAW_GRD_AMPLITUDE"


ENVELOPE_ID = "KHARG_P0_VALIDATION_ENVELOPE"


ENVELOPE_BBOX = (49.60, 28.60, 50.70, 29.60)


ENVELOPE_GEOMETRY: dict[str, Any] = _freeze(
    {
        "type": "Polygon",
        "coordinates": [
            [
                [49.60, 28.60],
                [50.70, 28.60],
                [50.70, 29.60],
                [49.60, 29.60],
                [49.60, 28.60],
            ]
        ],
    }
)


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

    def __post_init__(self) -> None:
        object.__setattr__(self, "roles", tuple(self.roles))


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

    def __post_init__(self) -> None:
        object.__setattr__(self, "assets", tuple(self.assets))
        if self.bbox is not None:
            object.__setattr__(self, "bbox", tuple(self.bbox))
        for key in ("footprint", "provider_metadata"):
            object.__setattr__(self, key, _freeze(getattr(self, key)))
        _stable_json(_slice_payload(self))

    @property
    def thermal_noise_correction_performed(self) -> bool | None:
        return self.metadata.thermal_noise_correction_performed if self.metadata else None

    def validate(self) -> None:
        if self.policy not in FROZEN_SOURCES:
            raise Sentinel1RetrievalError("Source policy is not one of the frozen six slots.")
        if self.availability not in {"UNAVAILABLE", "RESOLVED_NOT_ACCESSED", "AVAILABLE"}:
            raise Sentinel1RetrievalError("Invalid source availability state.")
        if self.representation != REPRESENTATION:
            raise Sentinel1RetrievalError("Only raw GRD amplitude may enter AS-201 handoff.")
        if self.availability == "UNAVAILABLE" and not self.reason:
            raise Sentinel1RetrievalError("Unavailable source requires an explicit reason.")
        if self.availability != "UNAVAILABLE" and (
            self.reason is not None
            or self.discovery_source is None
            or self.source is None
            or self.footprint is None
        ):
            raise Sentinel1RetrievalError("Resolved source lacks required identity/footprint.")
        if self.availability == "AVAILABLE" and (self.header is None or self.metadata is None):
            raise Sentinel1RetrievalError("Available source lacks validated header/XML evidence.")
        if self.header is not None and (
            (self.header.width, self.header.height) != (self.policy.width, self.policy.height)
            or (
                self.header.bits_per_sample,
                self.header.samples_per_pixel,
                self.header.sample_format,
                self.header.compression,
                self.header.tile_width,
                self.header.tile_height,
            )
            != (16, 1, 1, 50000, 1024, 1024)
            or self.header.nodata not in {"0", "0.0"}
            or self.header.tiepoint_count <= 0
            or self.header.overview_count != 6
            or self.header.has_model_pixel_scale
            or self.header.has_model_transformation
        ):
            raise Sentinel1RetrievalError("Source header summary violates the raw-GRD contract.")
        if self.metadata is not None and (
            (self.metadata.product_width, self.metadata.product_height)
            != (self.policy.width, self.policy.height)
            or (
                self.metadata.product_root,
                self.metadata.calibration_root,
                self.metadata.noise_root,
                self.metadata.manifest_root,
            )
            != ("product", "calibration", "noise", "XFDU")
            or not all(
                (
                    self.metadata.calibration_has_beta0,
                    self.metadata.calibration_has_sigma0,
                    self.metadata.calibration_has_gamma,
                    self.metadata.calibration_has_dn,
                    self.metadata.noise_has_range,
                    self.metadata.noise_has_azimuth,
                )
            )
            or (
                self.metadata.thermal_noise_correction_performed is not None
                and type(self.metadata.thermal_noise_correction_performed) is not bool
            )
        ):
            raise Sentinel1RetrievalError("Source XML summary violates the metadata contract.")
        for record, item in (
            (self.discovery_source, self.policy.cdse_item_id),
            (self.source, self.policy.pc_item_id),
        ):
            if record is not None and (
                record.product_id != item
                or record.platform != "sentinel-1a"
                or record.acquired_at != self.policy.acquisition_start
                or record.collection != "sentinel-1-grd"
            ):
                raise Sentinel1RetrievalError("SourceRecord does not identify the frozen slice.")
        if (
            self.source
            and self.discovery_source
            and (
                self.source.source_id == self.discovery_source.source_id
                or self.source.catalog.rstrip("/")
                != "https://planetarycomputer.microsoft.com/api/stac/v1"
                or self.discovery_source.catalog.rstrip("/")
                != "https://stac.dataspace.copernicus.eu/v1"
            )
        ):
            raise Sentinel1RetrievalError("Discovery/access provider provenance is inconsistent.")
        if self.availability != "UNAVAILABLE" and {a.purpose for a in self.assets} != {
            *REQUIRED_VV_ASSETS,
            "measurement_vh",
        }:
            raise Sentinel1RetrievalError("Resolved source lacks unique required asset references.")
        if len({a.purpose for a in self.assets}) != len(self.assets):
            raise Sentinel1RetrievalError("Duplicate asset purpose.")
        for asset in self.assets:
            try:
                validate_asset_href(asset.href, SARConfig())
            except AssetAccessError:
                raise Sentinel1RetrievalError("Invalid stable source asset reference.") from None
        if self.fingerprint != _fingerprint(_slice_payload(self)):
            raise Sentinel1RetrievalError("Source fingerprint mismatch.")

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
    coverage_metadata: dict[str, Any] = field(default_factory=dict)
    missingness: tuple[tuple[str, str], ...] = ()
    fingerprint: str = ""

    def __post_init__(self) -> None:
        object.__setattr__(self, "slices", tuple(self.slices))
        object.__setattr__(self, "missingness", tuple(tuple(v) for v in self.missingness))
        object.__setattr__(self, "coverage_metadata", _freeze(self.coverage_metadata))

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
    common_support_metadata: dict[str, Any] = field(default_factory=dict)
    processing_parameters: dict[str, Any] = field(default_factory=dict)
    provenance: DerivedProductRecord | None = None
    limitations: tuple[str, ...] = (
        "RAW_GRD_HANDOFF_NOT_SCIENTIFIC_BACKSCATTER",
        "FOOTPRINT_SUPPORT_NOT_PIXEL_EVALUABILITY",
        "REFERENCE_NOT_PETROLEUM_NEGATIVE_FOLLOW_UP_NOT_RECOVERY",
        "NO_PETROLEUM_SOURCE_WATER_SAFETY_OR_SHUTDOWN_INFERENCE",
    )

    def __post_init__(self) -> None:
        object.__setattr__(self, "groups", tuple(self.groups))
        object.__setattr__(self, "limitations", tuple(self.limitations))
        for key in ("envelope_geometry", "common_support_metadata", "processing_parameters"):
            object.__setattr__(self, key, _freeze(getattr(self, key)))

    @property
    def product_id(self) -> str:
        return f"sentinel1_retrieval:{self.fingerprint}"

    def to_dict(self) -> dict[str, Any]:
        """Stable metadata-cache/provenance boundary, never signed transport state."""
        self.validate()
        return json.loads(
            _stable_json(
                {
                    "schema_version": "as201-retrieval-v1",
                    "product_id": self.product_id,
                    "fingerprint": self.fingerprint,
                    "ready": self.ready,
                    "parameters": self.processing_parameters,
                    "limitations": self.limitations,
                    "provenance": {
                        "product_type": self.provenance.product_type,
                        "processing_version": self.provenance.processing_version,
                        "source_ids": self.provenance.source_ids,
                        "parameters": self.provenance.parameters,
                    }
                    if self.provenance
                    else None,
                }
            )
        )

    def validate(self) -> None:
        for source in self.slices:
            source.validate()
        rebuilt = assemble_retrieval(
            self.slices, created_at=self.provenance.created_at if self.provenance else None
        )
        if (
            self.groups != rebuilt.groups
            or self.fingerprint != rebuilt.fingerprint
            or self.common_support_metadata != rebuilt.common_support_metadata
            or self.processing_parameters != rebuilt.processing_parameters
            or self.provenance != rebuilt.provenance
            or self.policy_version != POLICY_VERSION
            or self.envelope_id != ENVELOPE_ID
            or self.envelope_bbox != ENVELOPE_BBOX
            or self.envelope_geometry != ENVELOPE_GEOMETRY
            or self.limitations != rebuilt.limitations
        ):
            raise Sentinel1RetrievalError("Retrieval coverage/identity/provenance is inconsistent.")

    def register(self, registry: ProvenanceRegistry) -> None:
        self.validate()
        if self.provenance is None:
            raise Sentinel1RetrievalError(
                "No source provenance exists for an entirely missing set."
            )
        records = [r for s in self.slices for r in (s.discovery_source, s.source) if r]
        for record in records:
            previous = registry.sources.get(record.source_id)
            if previous is not None and previous != record:
                raise Sentinel1RetrievalError("Registry source identity conflict.")
        previous = registry.derived_products.get(self.product_id)
        if previous is not None and (
            previous.product_type != self.provenance.product_type
            or previous.processing_version != self.provenance.processing_version
            or previous.source_ids != self.provenance.source_ids
            or _stable_json(previous.parameters) != _stable_json(self.provenance.parameters)
        ):
            raise Sentinel1RetrievalError("Registry derived identity conflict.")
        for record in records:
            if record.source_id not in registry.sources:
                registry.add_source(record)
        if self.product_id not in registry.derived_products:
            registry.add_derived_product(self.provenance)

    @property
    def ready(self) -> bool:
        return len(self.groups) == 3 and all(group.ready for group in self.groups)

    @property
    def slices(self) -> tuple[Sentinel1SliceSource, ...]:
        return tuple(source for group in self.groups for source in group.slices)


def _dt(value: str) -> datetime:
    parsed = datetime.fromisoformat(value)
    if parsed.tzinfo is None:
        raise RuntimeError("Frozen Sentinel-1 timestamp must be timezone-aware.")
    return parsed.astimezone(UTC)


FROZEN_SOURCES = (
    FrozenSentinel1Source(
        "REFERENCE",
        1,
        "S1A_IW_GRDH_1SDV_20260424T144205_20260424T144230_064223_08158E_4192_COG",
        "S1A_IW_GRDH_1SDV_20260424T144205_20260424T144230_064223_08158E",
        "S1A_IW_GRDH_1SDV_20260424T144205_20260424T144230_064223_08158E_4192",
        _dt("2026-04-24T14:42:05.150515Z"),
        _dt("2026-04-24T14:42:30.148548Z"),
        64223,
        25835,
        16732,
    ),
    FrozenSentinel1Source(
        "REFERENCE",
        2,
        "S1A_IW_GRDH_1SDV_20260424T144230_20260424T144255_064223_08158E_BA3A_COG",
        "S1A_IW_GRDH_1SDV_20260424T144230_20260424T144255_064223_08158E",
        "S1A_IW_GRDH_1SDV_20260424T144230_20260424T144255_064223_08158E_BA3A",
        _dt("2026-04-24T14:42:30.150042Z"),
        _dt("2026-04-24T14:42:55.148075Z"),
        64223,
        25842,
        16732,
    ),
    FrozenSentinel1Source(
        "DOCUMENTARY_EVENT",
        1,
        "S1A_IW_GRDH_1SDV_20260506T144204_20260506T144229_064398_081C09_BF44_COG",
        "S1A_IW_GRDH_1SDV_20260506T144204_20260506T144229_064398_081C09",
        "S1A_IW_GRDH_1SDV_20260506T144204_20260506T144229_064398_081C09_BF44",
        _dt("2026-05-06T14:42:04.538690Z"),
        _dt("2026-05-06T14:42:29.536703Z"),
        64398,
        25835,
        16732,
    ),
    FrozenSentinel1Source(
        "DOCUMENTARY_EVENT",
        2,
        "S1A_IW_GRDH_1SDV_20260506T144229_20260506T144254_064398_081C09_A43B_COG",
        "S1A_IW_GRDH_1SDV_20260506T144229_20260506T144254_064398_081C09",
        "S1A_IW_GRDH_1SDV_20260506T144229_20260506T144254_064398_081C09_A43B",
        _dt("2026-05-06T14:42:29.538209Z"),
        _dt("2026-05-06T14:42:54.536224Z"),
        64398,
        25842,
        16732,
    ),
    FrozenSentinel1Source(
        "LATE_FOLLOW_UP",
        1,
        "S1A_IW_GRDH_1SDV_20260518T144204_20260518T144229_064573_082235_34DC_COG",
        "S1A_IW_GRDH_1SDV_20260518T144204_20260518T144229_064573_082235",
        "S1A_IW_GRDH_1SDV_20260518T144204_20260518T144229_064573_082235_34DC",
        _dt("2026-05-18T14:42:04.240283Z"),
        _dt("2026-05-18T14:42:29.238414Z"),
        64573,
        25836,
        16732,
    ),
    FrozenSentinel1Source(
        "LATE_FOLLOW_UP",
        2,
        "S1A_IW_GRDH_1SDV_20260518T144229_20260518T144254_064573_082235_E298_COG",
        "S1A_IW_GRDH_1SDV_20260518T144229_20260518T144254_064573_082235",
        "S1A_IW_GRDH_1SDV_20260518T144229_20260518T144254_064573_082235_E298",
        _dt("2026-05-18T14:42:29.239908Z"),
        _dt("2026-05-18T14:42:54.239534Z"),
        64573,
        25843,
        16733,
    ),
)


def _stable_json(value: Any) -> bytes:
    def validate(node: Any) -> None:
        if isinstance(node, dict):
            for key, item in node.items():
                if not isinstance(key, str):
                    raise Sentinel1RetrievalError("Stable metadata keys must be strings.")
                if key.casefold() in {"token", "authorization", "cookie", "sas", "sig"}:
                    raise Sentinel1RetrievalError("Credentials cannot enter stable metadata.")
                validate(item)
        elif isinstance(node, (list, tuple)):
            for item in node:
                validate(item)
        elif isinstance(node, float) and not isfinite(node):
            raise Sentinel1RetrievalError("Stable metadata cannot contain NaN or infinity.")
        elif isinstance(node, str):
            if any(term in node.casefold() for term in ("sig=", "authorization: bearer", "sv=")):
                raise Sentinel1RetrievalError("Credentials cannot enter stable metadata.")
            if node.lower().startswith(("http://", "https://")):
                try:
                    parsed = urlsplit(node)
                    valid = (
                        parsed.scheme == "https"
                        and parsed.hostname
                        and parsed.port in (None, 443)
                        and not parsed.query
                        and not parsed.fragment
                        and parsed.username is None
                    )
                except ValueError:
                    valid = False
                if not valid:
                    raise Sentinel1RetrievalError("Stable metadata requires unsigned HTTPS URLs.")

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
        parsed = datetime.fromisoformat(value)
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
        "discovery_source": source_record_to_dict(source.discovery_source)
        if source.discovery_source
        else None,
        "source": source_record_to_dict(source.source) if source.source else None,
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


def assemble_retrieval(
    slices: tuple[Sentinel1SliceSource, ...], *, created_at: datetime | None = None
) -> Sentinel1RetrievalSet:
    """Deterministic metadata support, groups and immediate-source provenance."""
    if len(slices) != 6 or {s.policy for s in slices} != set(FROZEN_SOURCES):
        raise Sentinel1RetrievalError("Retrieval must retain exactly the six required slots.")
    groups = []
    for role in ROLE_ORDER:
        ordered = tuple(
            sorted(
                (s for s in slices if s.policy.role == role),
                key=lambda s: (s.policy.acquisition_start, s.policy.pc_item_id),
            )
        )
        support = coverage(ENVELOPE_GEOMETRY, tuple(s.footprint for s in ordered if s.footprint))
        support["footprint_inventory_complete"] = all(s.footprint is not None for s in ordered)
        support["is_lower_bound"] = not support["footprint_inventory_complete"]
        missing = tuple(
            (s.policy.pc_item_id, s.reason or s.availability)
            for s in ordered
            if s.availability != "AVAILABLE"
        )
        group_payload = {
            "role": role,
            "date": ordered[0].policy.acquisition_date.isoformat(),
            "slices": [s.fingerprint for s in ordered],
            "coverage": support,
            "missingness": missing,
        }
        groups.append(
            Sentinel1AcquisitionGroup(
                role,
                ordered[0].policy.acquisition_date,
                ordered,
                support,
                missing,
                _fingerprint(group_payload),
            )
        )
    common = common_coverage(
        ENVELOPE_GEOMETRY, tuple(g.coverage_metadata["source_support"] for g in groups)
    )
    common["footprint_inventory_complete"] = all(
        g.coverage_metadata["footprint_inventory_complete"] for g in groups
    )
    common["is_lower_bound"] = not common["footprint_inventory_complete"]
    parameters = _freeze(
        {
            "policy_version": POLICY_VERSION,
            "decision": "054",
            "representation": REPRESENTATION,
            "envelope_id": ENVELOPE_ID,
            "envelope_bbox": ENVELOPE_BBOX,
            "envelope_geometry": ENVELOPE_GEOMETRY,
            "frozen_sources": [
                {
                    **asdict(p),
                    "acquisition_start": p.acquisition_start.isoformat(),
                    "acquisition_end": p.acquisition_end.isoformat(),
                }
                for p in FROZEN_SOURCES
            ],
            "groups": [g.fingerprint for g in groups],
            "common_support": common,
            "comparison_support": "COMMON_THREE_DATE_METADATA_SUPPORT",
            "source_records": [_slice_payload(s) for g in groups for s in g.slices],
        }
    )
    fingerprint = _fingerprint(parameters)
    source_ids = tuple(
        r.source_id for g in groups for s in g.slices for r in (s.discovery_source, s.source) if r
    )
    provenance = None
    if source_ids:
        provenance = DerivedProductRecord(
            f"sentinel1_retrieval:{fingerprint}",
            "sentinel1_retrieval",
            created_at or datetime.now(UTC),
            POLICY_VERSION,
            source_ids,
            parameters,
        )
        provenance.validate()
    return Sentinel1RetrievalSet(
        POLICY_VERSION,
        ENVELOPE_ID,
        ENVELOPE_BBOX,
        ENVELOPE_GEOMETRY,
        tuple(groups),
        fingerprint,
        common,
        parameters,
        provenance,
    )
