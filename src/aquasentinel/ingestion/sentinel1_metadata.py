"""Bounded Sentinel-1 header/XML access validation for AS-201."""

from __future__ import annotations

import re
import struct
from collections.abc import Callable
from dataclasses import replace
from datetime import UTC, datetime
from hashlib import sha256
from itertools import pairwise
from math import isfinite
from typing import Any
from urllib.request import Request, build_opener
from xml.etree import ElementTree as ET

from aquasentinel.config import SARConfig
from aquasentinel.ingestion.planetary_computer import (
    AssetAccessError,
    _SameHostRedirect,
    read_bytes,
    sign_asset,
    validate_asset_href,
)
from aquasentinel.ingestion.sentinel1_policy import (
    FrozenSentinel1Source,
    Sentinel1HeaderSummary,
    Sentinel1MetadataError,
    Sentinel1MetadataSummary,
    Sentinel1RetrievalError,
    Sentinel1RetrievalSet,
    Sentinel1SliceSource,
    _with_fingerprint,
    assemble_retrieval,
)


def _safe_range_bytes(url: str, *, timeout: float, start: int, end: int) -> bytes:
    """Exact range response only, including Content-Range; never a full raster GET."""
    if (
        type(start) is not int
        or type(end) is not int
        or start < 0
        or end < start
        or end - start + 1 > 256 * 1024
    ):
        raise AssetAccessError("Invalid bounded metadata range request.")
    expected = end - start + 1
    validate_asset_href(url, SARConfig(), signed=True)
    try:
        request = Request(
            url, headers={"User-Agent": "AquaSentinel813/as201-v1", "Range": f"bytes={start}-{end}"}
        )
        with build_opener(_SameHostRedirect()).open(request, timeout=timeout) as response:
            import re

            span = re.fullmatch(
                r"bytes (\d+)-(\d+)/(\d+)", response.headers.get("Content-Range", "")
            )
            if (
                response.getcode() != 206
                or not span
                or (int(span[1]), int(span[2])) != (start, end)
                or int(span[3]) <= end
            ):
                raise AssetAccessError("Incorrect metadata range response.")
            body = response.read(expected + 1)
        if len(body) != expected:
            raise AssetAccessError("Incorrect metadata range length.")
        return body
    except (OSError, ValueError, TypeError, KeyError, AttributeError, AssetAccessError):
        pass
    raise AssetAccessError("Bounded HTTPS range metadata request failed.") from None


def _entries(ifd: bytes) -> dict[int, tuple[int, int, bytes]]:
    if len(ifd) < 2:
        raise Sentinel1MetadataError("TIFF IFD metadata is incomplete.")
    count = struct.unpack("<H", ifd[:2])[0]
    if count <= 0 or count > 4096 or len(ifd) != 2 + 12 * count + 4:
        raise Sentinel1MetadataError("TIFF IFD size is invalid.")
    result = {}
    for index in range(count):
        raw = ifd[2 + index * 12 : 2 + (index + 1) * 12]
        tag, kind, size = struct.unpack("<HHI", raw[:8])
        if tag in result or size <= 0:
            raise Sentinel1MetadataError("TIFF duplicate/empty tag is invalid.")
        result[tag] = (kind, size, raw[8:])
    return result


def _scalar(entries, tag, default=None):
    value = entries.get(tag)
    if value is None:
        if default is None:
            raise Sentinel1MetadataError("Required TIFF scalar is absent.")
        return default
    kind, count, raw = value
    if count != 1 or kind not in (3, 4, 13):
        raise Sentinel1MetadataError("TIFF scalar type is invalid.")
    return struct.unpack("<H" if kind == 3 else "<I", raw[:2] if kind == 3 else raw)[0]


def _parse_tiff_ifd(header, ifd, expected, *, overview_count=None):
    if len(header) != 8 or header[:4] != b"II*\x00":
        raise Sentinel1MetadataError("Expected classic little-endian TIFF.")
    entries = _entries(ifd)
    width, height = _scalar(entries, 256), _scalar(entries, 257)
    nodata_entry = entries.get(42113)
    nodata = None
    if nodata_entry and nodata_entry[0] == 2 and nodata_entry[1] <= 4:
        nodata = nodata_entry[2][: nodata_entry[1]].rstrip(b"\x00").decode("ascii")
    tiepoint = entries.get(33922)
    points = tiepoint[1] // 6 if tiepoint and tiepoint[0] == 12 and tiepoint[1] % 6 == 0 else 0
    if overview_count is None:
        sub = entries.get(330)
        overview_count = sub[1] if sub and sub[0] in (4, 13) else None
    if (width, height) != (expected.width, expected.height):
        raise Sentinel1MetadataError("TIFF dimensions mismatch the frozen source.")
    if (_scalar(entries, 258), _scalar(entries, 277, 1), _scalar(entries, 339, 1)) != (16, 1, 1):
        raise Sentinel1MetadataError("Expected one-band unsigned uint16 TIFF.")
    if _scalar(entries, 259) != 50000 or (_scalar(entries, 322), _scalar(entries, 323)) != (
        1024,
        1024,
    ):
        raise Sentinel1MetadataError("TIFF compression/block contract is invalid.")
    if nodata not in {"0", "0.0"} or not points or overview_count != 6:
        raise Sentinel1MetadataError("TIFF nodata/tiepoint/overview contract is invalid.")
    if 33550 in entries or 34264 in entries:
        raise Sentinel1MetadataError(
            "Native geographic tiepoints cannot be replaced with an affine."
        )
    return Sentinel1HeaderSummary(
        width, height, 16, 1, 50000, 1024, 1024, 1, nodata, points, overview_count, False, False
    )


def read_tiff_header(url, expected, *, timeout, range_reader=_safe_range_bytes):
    """Traverse metadata directories/tags only; never dereference image-block offsets."""
    requested = []
    image_blocks = []
    total = 0

    def read(start, size):
        nonlocal total
        if type(start) is not int or type(size) is not int or start < 0 or size <= 0:
            raise Sentinel1MetadataError("Invalid TIFF metadata span.")
        total += size
        if size > 256 * 1024 or total > 4 * 1024 * 1024 or start + size > 2**32:
            raise Sentinel1MetadataError("TIFF metadata budget exceeded.")
        requested.append((start, start + size))
        result = range_reader(url, timeout=timeout, start=start, end=start + size - 1)
        if len(result) != size:
            raise Sentinel1MetadataError("TIFF metadata span is truncated.")
        return result

    def values(entry):
        kind, count, raw = entry
        sizes = {2: 1, 3: 2, 4: 4, 12: 8, 13: 4}
        if kind not in sizes or count > 32768:
            raise Sentinel1MetadataError("Unsupported/bounded TIFF metadata type.")
        size = count * sizes[kind]
        body = raw[:size] if size <= 4 else read(struct.unpack("<I", raw)[0], size)
        if kind == 2:
            return body
        return struct.unpack("<" + {3: "H", 4: "I", 12: "d", 13: "I"}[kind] * count, body)

    try:
        header = read(0, 8)
        if header[:4] != b"II*\x00":
            raise Sentinel1MetadataError("Expected classic little-endian TIFF.")
        pending = [struct.unpack("<I", header[4:])[0]]
        seen = set()
        directories = []
        while pending:
            offset = pending.pop(0)
            if offset < 8 or offset in seen or len(seen) >= 7:
                raise Sentinel1MetadataError("TIFF directory cycle/count is invalid.")
            seen.add(offset)
            count = struct.unpack("<H", read(offset, 2))[0]
            if not 0 < count <= 4096:
                raise Sentinel1MetadataError("TIFF directory entry count is invalid.")
            ifd = read(offset, 2 + 12 * count + 4)
            entries = _entries(ifd)
            directories.append((ifd, entries))
            next_ifd = struct.unpack("<I", ifd[-4:])[0]
            if next_ifd:
                pending.append(next_ifd)
            if 330 in entries:
                pending.extend(values(entries[330]))
            if 324 not in entries or 325 not in entries:
                raise Sentinel1MetadataError("Tile offset/count metadata is required.")
            if any(entries[tag][0] not in (3, 4) for tag in (324, 325)):
                raise Sentinel1MetadataError("Image block indexes must be unsigned integers.")
            offsets, lengths = values(entries[324]), values(entries[325])
            if (
                len(offsets) != len(lengths)
                or not offsets
                or any(n <= 0 for n in lengths)
                or any(a < 8 or a + b > 2**32 for a, b in zip(offsets, lengths))
            ):
                raise Sentinel1MetadataError("Invalid image block index metadata.")
            image_blocks.extend((a, a + b) for a, b in zip(offsets, lengths))
        if len(directories) != 7:
            raise Sentinel1MetadataError("Six overview directories are required.")
        base = directories[0][1]
        summary = _parse_tiff_ifd(header, directories[0][0], expected, overview_count=6)
        for level, (_, directory) in enumerate(directories[1:], start=1):
            # Providers can use integer floor or ceil for reduced dimensions.
            factor = 2**level
            for tag, native in ((256, expected.width), (257, expected.height)):
                if _scalar(directory, tag) not in {
                    native // factor,
                    (native + factor - 1) // factor,
                }:
                    raise Sentinel1MetadataError("Overview dimensions are inconsistent.")
        tiepoints = values(base[33922])
        if any(not isinstance(v, (int, float)) or not isfinite(v) for v in tiepoints):
            raise Sentinel1MetadataError("Tiepoints must be finite.")
        if 34735 not in base:
            raise Sentinel1MetadataError("Geographic CRS metadata is required.")
        keys = values(base[34735])
        if len(keys) < 4 or len(keys) != 4 + 4 * keys[3]:
            raise Sentinel1MetadataError("GeoKey directory is invalid.")
        geo = {keys[i]: keys[i + 3] for i in range(4, len(keys), 4) if keys[i + 1] == 0}
        if geo.get(1024) != 2 or geo.get(2048) != 4326:
            raise Sentinel1MetadataError("Native geolocation must be WGS84 geographic.")
        if any(a < d and c < b for a, b in requested for c, d in image_blocks):
            raise Sentinel1MetadataError("Metadata range overlaps an image-block span.")
        return summary
    except AssetAccessError:
        raise
    except (OSError, ValueError, TypeError, KeyError, AttributeError, struct.error):
        pass
    raise Sentinel1MetadataError("TIFF structural metadata validation failed.") from None


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
    if (
        not isinstance(xml, bytes)
        or len(xml) > 4 * 1024 * 1024
        or any(marker in xml.upper() for marker in (b"<!DOCTYPE", b"<!ENTITY"))
    ):
        raise Sentinel1MetadataError("XML must be bounded and have no DTD/entities.")
    try:
        root = ET.fromstring(xml)
    except ET.ParseError:
        raise Sentinel1MetadataError(f"{role} XML is malformed.") from None
    return root


def _parse_safe_metadata_time(root: ET.Element, name: str, field: str) -> datetime:
    """Parse reviewed SAFE timeType fields, whose specification defines UTC."""
    raw_values = [e.text for e in root.iter() if _local(e.tag).casefold() == name.casefold()]
    if any(not isinstance(v, str) or not v or v != v.strip() for v in raw_values):
        raise Sentinel1MetadataError(f"SAFE {field} must be nonempty unpadded timestamp text.")
    value = _unique_text(root, name)
    if re.search(r"[.,]\d{7}", value):
        raise Sentinel1MetadataError(f"SAFE {field} exceeds microsecond precision.")
    try:
        parsed = datetime.fromisoformat(value)
    except ValueError:
        raise Sentinel1MetadataError(f"SAFE {field} timestamp is invalid.") from None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=UTC)
    return parsed.astimezone(UTC)


def _validate_ads_header(root: ET.Element, expected: FrozenSentinel1Source, role: str) -> None:
    headers = [e for e in root.iter() if _local(e.tag) == "adsHeader"]
    if len(headers) != 1:
        raise Sentinel1MetadataError("XML requires exactly one ADS identity header.")
    root = headers[0]
    mission = _unique_text(root, "missionId")
    product = _unique_text(root, "productType")
    polarisation = _unique_text(root, "polarisation")
    mode = _unique_text(root, "mode")
    start = _parse_safe_metadata_time(root, "startTime", f"{role}.startTime")
    stop = _parse_safe_metadata_time(root, "stopTime", f"{role}.stopTime")
    if mission != "S1A" or product not in {"GRD", "GRDH"}:
        raise Sentinel1MetadataError(f"{role} XML mission/product identity is invalid.")
    if str(polarisation).upper() != "VV" or mode != "IW":
        raise Sentinel1MetadataError(f"{role} XML polarization/mode identity is invalid.")
    if start != expected.acquisition_start or stop != expected.acquisition_end:
        raise Sentinel1MetadataError(f"{role} XML acquisition interval mismatches frozen source.")
    orbit = _unique_text(root, "absoluteOrbitNumber")
    if orbit is not None:
        try:
            if int(orbit) != expected.absolute_orbit:
                raise ValueError
        except ValueError:
            raise Sentinel1MetadataError(f"{role} XML absolute orbit is invalid.") from None


def _parse_manifest_time(root: ET.Element, name: str) -> datetime:
    """Interpret unzoned manifest acquisition times as UTC at this boundary only."""
    raw_values = [e.text for e in root.iter() if _local(e.tag).casefold() == name.casefold()]
    if any(not isinstance(v, str) or v != v.strip() for v in raw_values):
        raise Sentinel1MetadataError(f"Manifest {name} must be unpadded timestamp text.")
    value = _unique_text(root, name)
    if re.search(r"[.,]\d{7}", value):
        raise Sentinel1MetadataError(f"Manifest {name} exceeds microsecond precision.")
    try:
        parsed = datetime.fromisoformat(value)
    except ValueError:
        raise Sentinel1MetadataError(f"Manifest {name} timestamp is invalid.") from None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=UTC)
    return parsed.astimezone(UTC)


def _validate_manifest(root, expected):
    start = _parse_manifest_time(root, "startTime")
    stop = _parse_manifest_time(root, "stopTime")
    if (start, stop) != (expected.acquisition_start, expected.acquisition_end):
        raise Sentinel1MetadataError("Manifest interval mismatch.")
    if _unique_text(root, "mode") != "IW" or _unique_text(root, "pass").casefold() != "ascending":
        raise Sentinel1MetadataError("Manifest mode/orbit direction mismatch.")
    if _unique_text(root, "relativeOrbitNumber") != "101":
        raise Sentinel1MetadataError("Manifest relative orbit mismatch.")
    if _unique_text(root, "productType") != "GRD":
        raise Sentinel1MetadataError("Manifest product mismatch.")
    platforms = [e for e in root.iter() if _local(e.tag) == "platform"]
    if len(platforms) != 1 or _unique_text(platforms[0], "number") != "A":
        raise Sentinel1MetadataError("Manifest platform mismatch.")
    families = [e for e in platforms[0] if _local(e.tag).lower() == "familyname"]
    if (
        len(families) != 1
        or not isinstance(families[0].text, str)
        or not families[0].text.strip()
    ):
        raise Sentinel1MetadataError("Manifest requires one nonempty direct platform familyName.")
    family = families[0].text.strip()
    if family.casefold() != "Sentinel-1".casefold():
        raise Sentinel1MetadataError("Manifest platform family mismatch.")
    hrefs = [v for e in root.iter() for k, v in e.attrib.items() if _local(k) == "href"]
    parts = expected.native_source_product_id.lower().split("_")
    witness = f"s1a-iw-grd-vv-{parts[4]}-{parts[5]}-{parts[6]}-{parts[7]}"
    if not any(witness in href and "/measurement/" in "/" + href for href in hrefs):
        raise Sentinel1MetadataError("Manifest lacks matching VV native measurement identity.")


def _numeric_values(root, name, *, integers=False, minimum=None):
    value = _unique_text(root, name)
    try:
        parts = value.split()
        numbers = [int(s) if integers else float(s) for s in parts]
    except (ValueError, TypeError):
        raise Sentinel1MetadataError("XML numeric metadata is invalid.") from None
    if not numbers or any(
        not isfinite(v) or (minimum is not None and v < minimum) for v in numbers
    ):
        raise Sentinel1MetadataError("XML numeric metadata is nonfinite/outside structure bounds.")
    elements = [e for e in root.iter() if _local(e.tag) == name]
    if (
        len(elements) == 1
        and "count" in elements[0].attrib
        and int(elements[0].attrib["count"]) != len(numbers)
    ):
        raise Sentinel1MetadataError("XML declared element count mismatch.")
    return numbers


def _vectors(root, name):
    result = [e for e in root.iter() if _local(e.tag) == name]
    if not result:
        raise Sentinel1MetadataError("Required XML vectors are empty.")
    containers = [e for e in root.iter() if _local(e.tag) == name + "List"]
    if len(containers) != 1 or int(containers[0].attrib.get("count", len(result))) != len(result):
        raise Sentinel1MetadataError("XML vector container count mismatch.")
    return result


def _validate_luts(calibration, noise, product):
    for vector in _vectors(calibration, "calibrationVector"):
        pixels = _numeric_values(vector, "pixel", integers=True)
        if any(a >= b for a, b in pairwise(pixels)):
            raise Sentinel1MetadataError("Calibration coordinates must be ordered.")
        _numeric_values(vector, "line", integers=True)
        _parse_safe_metadata_time(vector, "azimuthTime", "calibration.azimuthTime")
        for field in ("betaNought", "sigmaNought", "gamma", "dn"):
            values = _numeric_values(vector, field, minimum=0)
            if len(values) != len(pixels) or any(v == 0 for v in values):
                raise Sentinel1MetadataError("Calibration LUT coordinate/value lengths invalid.")
    for vector in _vectors(noise, "noiseRangeVector"):
        pixels = _numeric_values(vector, "pixel", integers=True)
        values = _numeric_values(vector, "noiseRangeLut", minimum=0)
        if len(pixels) != len(values) or any(a >= b for a, b in pairwise(pixels)):
            raise Sentinel1MetadataError("Range noise LUT coordinates/length mismatch.")
        _numeric_values(vector, "line", integers=True)
        _parse_safe_metadata_time(vector, "azimuthTime", "noise.azimuthTime")
    for vector in _vectors(noise, "noiseAzimuthVector"):
        lines = _numeric_values(vector, "line", integers=True)
        values = _numeric_values(vector, "noiseAzimuthLut", minimum=0)
        if len(lines) != len(values) or any(a >= b for a, b in pairwise(lines)):
            raise Sentinel1MetadataError("Azimuth noise LUT coordinates/length mismatch.")
        for lo, hi in (
            ("firstAzimuthLine", "lastAzimuthLine"),
            ("firstRangeSample", "lastRangeSample"),
        ):
            if (
                _numeric_values(vector, lo, integers=True)[0]
                > _numeric_values(vector, hi, integers=True)[0]
            ):
                raise Sentinel1MetadataError("Azimuth noise coordinate block bounds invalid.")
    for point in _vectors(product, "geolocationGridPoint"):
        for name in ("line", "pixel", "latitude", "longitude", "height", "incidenceAngle"):
            values = _numeric_values(point, name, integers=name in ("line", "pixel"))
            if len(values) != 1:
                raise Sentinel1MetadataError("Geolocation fields must be scalar.")
        if (
            not -90 <= _numeric_values(point, "latitude")[0] <= 90
            or not -180 <= _numeric_values(point, "longitude")[0] <= 180
        ):
            raise Sentinel1MetadataError("Geolocation is outside WGS84.")
    for field in ("rangePixelSpacing", "azimuthPixelSpacing"):
        if _numeric_values(product, field) != [10]:
            raise Sentinel1MetadataError("Native sample spacing mismatch.")


def _validate_metadata_xml(
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
    _validate_manifest(manifest_root, expected)
    _validate_luts(calibration_root, noise_root, product_root)
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


def validate_metadata_xml(**kwargs: Any) -> Sentinel1MetadataSummary:
    try:
        return _validate_metadata_xml(**kwargs)
    except (ValueError, TypeError, KeyError, AttributeError, ET.ParseError, OverflowError):
        pass
    raise Sentinel1MetadataError("Required XML metadata contract is invalid.") from None


def validate_slice_access(
    source: Sentinel1SliceSource,
    settings: SARConfig,
    *,
    signer: Callable[[str, SARConfig], str] = sign_asset,
    range_reader: Callable[..., bytes] = _safe_range_bytes,
    byte_reader: Callable[..., bytes] = read_bytes,
) -> Sentinel1SliceSource:
    """Validate headers/XML only. No raster sample/pixel read is performed."""
    settings.validate()
    source.validate()
    if source.availability != "RESOLVED_NOT_ACCESSED":
        return source
    try:
        measurement = source.asset("measurement_vv")
        signed_measurement = signer(measurement.href, settings)
        try:
            header = read_tiff_header(
                signed_measurement,
                source.policy,
                timeout=settings.timeout_seconds,
                range_reader=range_reader,
            )
        finally:
            signed_measurement = None
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
            try:
                payloads[purpose] = byte_reader(
                    signed,
                    timeout=settings.timeout_seconds,
                    max_bytes=limit,
                )
                if len(payloads[purpose]) > limit:
                    raise Sentinel1MetadataError("XML metadata size budget exceeded.")
            finally:
                signed = None
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
                provider_metadata={
                    **source.provider_metadata,
                    "metadata_SHA256": {k: sha256(v).hexdigest() for k, v in payloads.items()},
                },
                fingerprint="",
            )
        )
    except (AssetAccessError, OSError):
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
    slices = tuple(validate_slice_access(source, settings, **kwargs) for source in retrieval.slices)
    created_at = retrieval.provenance.created_at if retrieval.provenance else None
    return assemble_retrieval(slices, created_at=created_at)
