"""Bounded Sentinel-1 header/XML access validation for AS-201."""

from __future__ import annotations

import struct
from dataclasses import replace
from typing import Any, Callable
from urllib.request import Request, build_opener
from xml.etree import ElementTree as ET

from aquasentinel.config import SARConfig
from aquasentinel.ingestion.planetary_computer import (
    AssetAccessError,
    _SameHostRedirect,
    read_bytes,
    sign_asset,
)
from aquasentinel.ingestion.sentinel1_policy import (
    FrozenSentinel1Source,
    Sentinel1AcquisitionGroup,
    Sentinel1HeaderSummary,
    Sentinel1MetadataError,
    Sentinel1MetadataSummary,
    Sentinel1RetrievalError,
    Sentinel1RetrievalSet,
    Sentinel1SliceSource,
    _fingerprint,
    _parse_time,
    _with_fingerprint,
)


def _safe_range_bytes(url: str, *, timeout: float, start: int, end: int) -> bytes:
    """Read one exact HTTP range with sanitized failures and no pixel decoding."""
    if (
        isinstance(start, bool)
        or isinstance(end, bool)
        or not isinstance(start, int)
        or not isinstance(end, int)
        or start < 0
        or end < start
        or end - start + 1 > 256 * 1024
    ):
        raise AssetAccessError("Invalid bounded metadata range request.")
    expected = end - start + 1
    try:
        request = Request(
            url,
            headers={
                "User-Agent": "AquaSentinel813/as201-v1",
                "Range": f"bytes={start}-{end}",
            },
        )
        with build_opener(_SameHostRedirect()).open(request, timeout=timeout) as response:
            status = response.getcode()
            body = response.read(expected + 1)
        if status != 206 or len(body) != expected:
            raise AssetAccessError("Range response is not the exact requested metadata span.")
        return body
    except (OSError, ValueError, TypeError, KeyError, AttributeError, AssetAccessError):
        pass
    raise AssetAccessError("Bounded HTTPS range metadata request failed.") from None


def _ifd_scalar(entry: tuple[int, int, int, bytes]) -> int | None:
    _, field_type, count, raw = entry
    if count != 1:
        return None
    if field_type == 3:
        return struct.unpack("<H", raw[:2])[0]
    if field_type in {4, 13}:
        return struct.unpack("<I", raw)[0]
    return None


def _inline_ascii(entry: tuple[int, int, int, bytes]) -> str | None:
    _, field_type, count, raw = entry
    if field_type != 2 or count <= 0 or count > 4:
        return None
    return raw[:count].rstrip(b"\x00").decode("ascii", errors="strict")


def _parse_tiff_ifd(
    header: bytes,
    ifd: bytes,
    expected: FrozenSentinel1Source,
) -> Sentinel1HeaderSummary:
    if len(header) != 8 or header[:4] != b"II*\x00":
        raise Sentinel1MetadataError("Sentinel-1 measurement is not classic little-endian TIFF.")
    if len(ifd) < 2:
        raise Sentinel1MetadataError("TIFF IFD metadata is incomplete.")
    count = struct.unpack("<H", ifd[:2])[0]
    if len(ifd) != 2 + 12 * count + 4:
        raise Sentinel1MetadataError("TIFF IFD range length is inconsistent.")
    entries: dict[int, tuple[int, int, int, bytes]] = {}
    for index in range(count):
        raw = ifd[2 + index * 12:2 + (index + 1) * 12]
        tag, field_type, value_count = struct.unpack("<HHI", raw[:8])
        entries[tag] = (tag, field_type, value_count, raw[8:12])

    def scalar(tag: int, default: int | None = None) -> int:
        entry = entries.get(tag)
        value = _ifd_scalar(entry) if entry else default
        if value is None:
            raise Sentinel1MetadataError(f"Required TIFF tag {tag} is missing or unsupported.")
        return value

    width, height = scalar(256), scalar(257)
    bits = scalar(258)
    compression = scalar(259)
    samples = scalar(277, 1)
    tile_width, tile_height = scalar(322), scalar(323)
    sample_format = scalar(339, 1)
    nodata = _inline_ascii(entries[42113]) if 42113 in entries else None
    tiepoint_entry = entries.get(33922)
    tiepoint_count = tiepoint_entry[2] // 6 if tiepoint_entry and tiepoint_entry[2] % 6 == 0 else 0
    subifd = entries.get(330)
    overview_count = subifd[2] if subifd and subifd[1] in {4, 13} else None

    if (width, height) != (expected.width, expected.height):
        raise Sentinel1MetadataError("TIFF dimensions conflict with frozen M46 header contract.")
    if bits != 16 or samples != 1 or sample_format != 1:
        raise Sentinel1MetadataError("TIFF is not one-band unsigned uint16.")
    if compression != 50000 or (tile_width, tile_height) != (1024, 1024):
        raise Sentinel1MetadataError("TIFF compression/tile contract differs from M46.")
    if nodata not in {"0", "0.0"}:
        raise Sentinel1MetadataError("TIFF nodata must be explicit inline zero.")
    if tiepoint_count <= 0:
        raise Sentinel1MetadataError("TIFF must expose native geographic tiepoints.")
    if overview_count != 6:
        raise Sentinel1MetadataError("TIFF must expose the six verified overview directories.")
    return Sentinel1HeaderSummary(
        width=width,
        height=height,
        bits_per_sample=bits,
        samples_per_pixel=samples,
        compression=compression,
        tile_width=tile_width,
        tile_height=tile_height,
        sample_format=sample_format,
        nodata=nodata,
        tiepoint_count=tiepoint_count,
        overview_count=overview_count,
        has_model_pixel_scale=33550 in entries,
        has_model_transformation=34264 in entries,
    )


def read_tiff_header(
    url: str,
    expected: FrozenSentinel1Source,
    *,
    timeout: float,
    range_reader: Callable[..., bytes] = _safe_range_bytes,
) -> Sentinel1HeaderSummary:
    """Read TIFF structural metadata only using explicit non-image byte ranges."""
    header = range_reader(url, timeout=timeout, start=0, end=7)
    if len(header) != 8 or header[:4] != b"II*\x00":
        raise Sentinel1MetadataError("Sentinel-1 measurement is not classic little-endian TIFF.")
    ifd_offset = struct.unpack("<I", header[4:8])[0]
    if ifd_offset < 8:
        raise Sentinel1MetadataError("TIFF first IFD offset is invalid.")
    count_bytes = range_reader(url, timeout=timeout, start=ifd_offset, end=ifd_offset + 1)
    count = struct.unpack("<H", count_bytes)[0]
    if count <= 0 or count > 4096:
        raise Sentinel1MetadataError("TIFF IFD entry count is outside safe bounds.")
    ifd_end = ifd_offset + 2 + 12 * count + 4 - 1
    ifd = range_reader(url, timeout=timeout, start=ifd_offset, end=ifd_end)
    return _parse_tiff_ifd(header, ifd, expected)


def _local(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def _texts(root: ET.Element, name: str) -> list[str]:
    return [
        element.text.strip()
        for element in root.iter()
        if _local(element.tag).lower() == name.lower()
        and isinstance(element.text, str)
        and element.text.strip()
    ]


def _unique_text(root: ET.Element, name: str, *, required: bool = True) -> str | None:
    values = set(_texts(root, name))
    if not values and not required:
        return None
    if len(values) != 1:
        raise Sentinel1MetadataError(f"XML requires one consistent {name} value.")
    return next(iter(values))


def _parse_xml(xml: bytes, role: str) -> ET.Element:
    try:
        root = ET.fromstring(xml)
    except ET.ParseError:
        raise Sentinel1MetadataError(f"{role} XML is malformed.") from None
    return root


def _validate_ads_header(root: ET.Element, expected: FrozenSentinel1Source, role: str) -> None:
    mission = _unique_text(root, "missionId")
    product = _unique_text(root, "productType")
    polarisation = _unique_text(root, "polarisation")
    mode = _unique_text(root, "mode")
    start = _parse_time(_unique_text(root, "startTime"), f"{role}.startTime")
    stop = _parse_time(_unique_text(root, "stopTime"), f"{role}.stopTime")
    if mission != "S1A" or not str(product).upper().startswith("GRD"):
        raise Sentinel1MetadataError(f"{role} XML mission/product identity is invalid.")
    if str(polarisation).upper() != "VV" or mode != "IW":
        raise Sentinel1MetadataError(f"{role} XML polarization/mode identity is invalid.")
    if start != expected.acquisition_start or stop != expected.acquisition_end:
        raise Sentinel1MetadataError(f"{role} XML acquisition interval mismatches frozen source.")
    orbit = _unique_text(root, "absoluteOrbitNumber", required=False)
    if orbit is not None:
        try:
            if int(orbit) != expected.absolute_orbit:
                raise ValueError
        except ValueError:
            raise Sentinel1MetadataError(f"{role} XML absolute orbit is invalid.") from None


def validate_metadata_xml(
    *,
    manifest: bytes,
    product: bytes,
    calibration: bytes,
    noise: bytes,
    expected: FrozenSentinel1Source,
    header: Sentinel1HeaderSummary,
) -> Sentinel1MetadataSummary:
    manifest_root = _parse_xml(manifest, "manifest")
    product_root = _parse_xml(product, "product")
    calibration_root = _parse_xml(calibration, "calibration")
    noise_root = _parse_xml(noise, "noise")
    roots = {
        "manifest": _local(manifest_root.tag),
        "product": _local(product_root.tag),
        "calibration": _local(calibration_root.tag),
        "noise": _local(noise_root.tag),
    }
    if roots["manifest"].upper() != "XFDU":
        raise Sentinel1MetadataError("Manifest XML has an unexpected root role.")
    if roots["product"].lower() != "product":
        raise Sentinel1MetadataError("Product annotation XML has an unexpected root role.")
    if roots["calibration"].lower() != "calibration":
        raise Sentinel1MetadataError("Calibration XML has an unexpected root role.")
    if roots["noise"].lower() != "noise":
        raise Sentinel1MetadataError("Noise XML has an unexpected root role.")
    xml_roots = (
        ("product", product_root),
        ("calibration", calibration_root),
        ("noise", noise_root),
    )
    for role, root in xml_roots:
        _validate_ads_header(root, expected, role)

    samples = int(_unique_text(product_root, "numberOfSamples"))
    lines = int(_unique_text(product_root, "numberOfLines"))
    if (samples, lines) != (header.width, header.height):
        raise Sentinel1MetadataError("Product XML dimensions conflict with TIFF header.")
    thermal = _unique_text(product_root, "thermalNoiseCorrectionPerformed", required=False)
    thermal_state = None
    if thermal is not None:
        if thermal.lower() not in {"true", "false"}:
            raise Sentinel1MetadataError("thermalNoiseCorrectionPerformed must be boolean text.")
        thermal_state = thermal.lower() == "true"

    calibration_names = {_local(element.tag).lower() for element in calibration_root.iter()}
    noise_names = {_local(element.tag).lower() for element in noise_root.iter()}
    required_calibration = {
        "betanought": "beta0",
        "sigmanought": "sigma0",
        "gamma": "gamma",
        "dn": "dn",
    }
    present = {
        label: any(name == xml_name for name in calibration_names)
        for xml_name, label in required_calibration.items()
    }
    if not all(present.values()):
        raise Sentinel1MetadataError("Calibration XML lacks required beta/sigma/gamma/DN LUTs.")
    range_noise = "noiserangevectorlist" in noise_names
    azimuth_noise = "noiseazimuthvectorlist" in noise_names
    if not range_noise or not azimuth_noise:
        raise Sentinel1MetadataError("Noise XML must expose both range and azimuth structures.")

    return Sentinel1MetadataSummary(
        product_root=roots["product"],
        calibration_root=roots["calibration"],
        noise_root=roots["noise"],
        manifest_root=roots["manifest"],
        thermal_noise_correction_performed=thermal_state,
        product_width=samples,
        product_height=lines,
        calibration_has_beta0=present["beta0"],
        calibration_has_sigma0=present["sigma0"],
        calibration_has_gamma=present["gamma"],
        calibration_has_dn=present["dn"],
        noise_has_range=range_noise,
        noise_has_azimuth=azimuth_noise,
    )


def validate_slice_access(
    source: Sentinel1SliceSource,
    settings: SARConfig,
    *,
    signer: Callable[[str, SARConfig], str] = sign_asset,
    range_reader: Callable[..., bytes] = _safe_range_bytes,
    byte_reader: Callable[..., bytes] = read_bytes,
) -> Sentinel1SliceSource:
    """Validate headers/XML only. No raster sample/pixel read is performed."""
    if source.availability != "RESOLVED_NOT_ACCESSED":
        return source
    try:
        measurement = source.asset("measurement_vv")
        signed_measurement = signer(measurement.href, settings)
        header = read_tiff_header(
            signed_measurement,
            source.policy,
            timeout=settings.timeout_seconds,
            range_reader=range_reader,
        )
        payloads: dict[str, bytes] = {}
        limits = {
            "manifest": 2 * 1024 * 1024,
            "product_vv": 4 * 1024 * 1024,
            "calibration_vv": 2 * 1024 * 1024,
            "noise_vv": 2 * 1024 * 1024,
        }
        for purpose, limit in limits.items():
            asset = source.asset(purpose)
            signed = signer(asset.href, settings)
            payloads[purpose] = byte_reader(
                signed,
                timeout=settings.timeout_seconds,
                max_bytes=limit,
            )
        metadata = validate_metadata_xml(
            manifest=payloads["manifest"],
            product=payloads["product_vv"],
            calibration=payloads["calibration_vv"],
            noise=payloads["noise_vv"],
            expected=source.policy,
            header=header,
        )
        return _with_fingerprint(
            replace(
                source,
                availability="AVAILABLE",
                reason=None,
                header=header,
                metadata=metadata,
                fingerprint="",
            )
        )
    except AssetAccessError:
        return _with_fingerprint(
            replace(source, availability="UNAVAILABLE", reason="ACCESS_BLOCKED", fingerprint="")
        )
    except (Sentinel1RetrievalError, ValueError, TypeError, UnicodeError, ET.ParseError):
        return _with_fingerprint(
            replace(source, availability="UNAVAILABLE", reason="METADATA_INVALID", fingerprint="")
        )


def validate_retrieval_access(
    retrieval: Sentinel1RetrievalSet,
    settings: SARConfig,
    **kwargs: Any,
) -> Sentinel1RetrievalSet:
    groups = tuple(
        Sentinel1AcquisitionGroup(
            group.role,
            group.acquisition_date,
            tuple(validate_slice_access(source, settings, **kwargs) for source in group.slices),
        )
        for group in retrieval.groups
    )
    payload = {
        "policy_version": retrieval.policy_version,
        "envelope_id": retrieval.envelope_id,
        "envelope_bbox": retrieval.envelope_bbox,
        "envelope_geometry": retrieval.envelope_geometry,
        "groups": [
            {
                "role": group.role,
                "acquisition_date": group.acquisition_date.isoformat(),
                "slices": [source.fingerprint for source in group.slices],
            }
            for group in groups
        ],
    }
    return replace(retrieval, groups=groups, fingerprint=_fingerprint(payload))
