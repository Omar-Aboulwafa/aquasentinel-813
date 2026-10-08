"""Decode the actual delivered product's BOA XML, never infer DN semantics by date."""

from __future__ import annotations

import math
import re
from dataclasses import asdict, dataclass
from typing import Any
from xml.etree import ElementTree as ET

import numpy as np

from aquasentinel.ingestion.sentinel2_assets import BANDS

MAX_XML_BYTES = 2_000_000


class ReflectanceMetadataError(ValueError):
    """The product does not establish safe surface-reflectance decoding."""


@dataclass(frozen=True)
class ReflectanceMetadata:
    processing_baseline: str
    quantification: float
    offsets: dict[str, float]
    band_ids: dict[str, str]

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def _band_name(text: str) -> str:
    if text == "B8A":
        return text
    if not re.fullmatch(r"B\d{1,2}", text):
        raise ReflectanceMetadataError("Unknown physicalBand mapping.")
    return f"B{int(text[1:]):02d}"


def parse_product_metadata(body: bytes, expected_baseline: str) -> ReflectanceMetadata:
    if len(body) > MAX_XML_BYTES:
        raise ReflectanceMetadataError("Product XML exceeds size limit.")
    if b"<!DOCTYPE" in body.upper() or b"<!ENTITY" in body.upper():
        raise ReflectanceMetadataError("XML entities/DTD are not allowed.")
    try:
        root = ET.fromstring(body)
        elements = list(root.iter())

        def named(name: str) -> list[ET.Element]:
            return [el for el in elements if el.tag.rsplit("}", 1)[-1] == name]

        def singleton(name: str) -> str:
            values = named(name)
            if len(values) != 1 or not values[0].text:
                raise ReflectanceMetadataError(f"Product XML needs exactly one {name}.")
            return values[0].text.strip()

        baseline = singleton("PROCESSING_BASELINE")
        if baseline != expected_baseline:
            raise ReflectanceMetadataError("XML baseline conflicts with delivered PC product.")
        quantification = float(singleton("BOA_QUANTIFICATION_VALUE"))
        if not math.isfinite(quantification) or quantification <= 0:
            raise ReflectanceMetadataError("BOA quantification must be finite and positive.")
        mapping, used_ids = {}, set()
        for el in named("Spectral_Information"):
            band, band_id = _band_name(el.attrib["physicalBand"]), el.attrib["bandId"]
            if not band_id.isdigit() or band in mapping or band_id in used_ids:
                raise ReflectanceMetadataError("Conflicting or duplicate XML spectral mapping.")
            mapping[band], used_ids = band_id, used_ids | {band_id}
        offsets = {}
        for el in named("BOA_ADD_OFFSET"):
            band_id, value = el.attrib["band_id"], float(el.text)
            if band_id in offsets or band_id not in used_ids or not math.isfinite(value):
                raise ReflectanceMetadataError("Conflicting or invalid XML band offset.")
            offsets[band_id] = value
        if any(band not in mapping or mapping[band] not in offsets for band in BANDS):
            raise ReflectanceMetadataError("Required reflectance band mapping/offset is missing.")
        return ReflectanceMetadata(
            baseline,
            quantification,
            {b: offsets[mapping[b]] for b in BANDS},
            {b: mapping[b] for b in BANDS},
        )
    except ReflectanceMetadataError:
        raise
    except (ET.ParseError, KeyError, TypeError, ValueError):
        raise ReflectanceMetadataError("Malformed product XML or decoding metadata.") from None


def decode_reflectance(
    dn: np.ndarray, nodata: float, band: str, metadata: ReflectanceMetadata
) -> np.ndarray:
    valid = (dn != nodata) & np.isfinite(dn)
    result = np.full(dn.shape, np.nan, dtype=np.float32)
    result[valid] = (
        dn[valid].astype(np.float32) + metadata.offsets[band]
    ) / metadata.quantification
    return result
