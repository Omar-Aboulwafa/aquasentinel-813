import numpy as np
import pytest

from aquasentinel.ingestion.sentinel2_assets import BANDS
from aquasentinel.preprocessing.metadata import (
    MAX_XML_BYTES,
    ReflectanceMetadataError,
    decode_reflectance,
    parse_product_metadata,
)

from .conftest import xml_body


def test_xml_namespace_and_band_specific_decoding(product_xml):
    xml = product_xml.replace(
        b'<BOA_ADD_OFFSET band_id="8">-1000', b'<BOA_ADD_OFFSET band_id="8">-900'
    )
    metadata = parse_product_metadata(xml, "05.09")
    assert metadata.quantification == 10000
    assert metadata.band_ids["B02"] == "1"
    assert metadata.band_ids["B8A"] == "8"
    assert metadata.offsets["B8A"] == -900
    assert set(metadata.offsets) == set(BANDS)


@pytest.mark.parametrize(
    "xml",
    [
        b"not-xml",
        b'<!DOCTYPE x [<!ENTITY dangerous "x">]><x/>',
        b"x" * (MAX_XML_BYTES + 1),
        xml_body(quantification=0),
        xml_body(quantification="nan"),
        xml_body(offset="inf"),
        xml_body().replace(b'<BOA_ADD_OFFSET band_id="1">-1000</BOA_ADD_OFFSET>', b""),
        xml_body().replace(b"</root>", b'<BOA_ADD_OFFSET band_id="1">-900</BOA_ADD_OFFSET></root>'),
        xml_body().replace(b'physicalBand="B8A"', b'physicalBand="B8"'),
        xml_body().replace(b'bandId="8"', b'bandId="7"'),
        xml_body().replace(
            b"</root>", b"<BOA_QUANTIFICATION_VALUE>10000</BOA_QUANTIFICATION_VALUE></root>"
        ),
    ],
)
def test_unsafe_xml_rejected(xml):
    with pytest.raises(ReflectanceMetadataError):
        parse_product_metadata(xml, "05.09")


def test_processing_baseline_conflict(product_xml):
    with pytest.raises(ReflectanceMetadataError, match="baseline"):
        parse_product_metadata(product_xml, "05.10")


def test_nodata_first_negative_zero_unclipped_float32(product_xml):
    decoded = decode_reflectance(
        np.array([[0, 500, 1000, 2000, 20000]], dtype=np.uint16),
        0,
        "B02",
        parse_product_metadata(product_xml, "05.09"),
    )
    assert decoded.dtype == np.float32
    assert np.isnan(decoded[0, 0])
    np.testing.assert_allclose(decoded[0, 1:], [-0.05, 0, 0.1, 1.9])
