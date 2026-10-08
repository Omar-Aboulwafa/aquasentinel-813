from datetime import UTC, datetime

import pytest

from aquasentinel.config import OpticalConfig
from aquasentinel.ingestion.sentinel2 import AssetReference, Sentinel2Candidate
from aquasentinel.ingestion.sentinel2_assets import BANDS, REQUIRED_ASSETS, match_and_resolve


@pytest.fixture
def cdse_candidate():
    return Sentinel2Candidate(
        "S2B_MSIL2A_20230428T064629_N0510_R020_T40RBN_20240831T052931",
        datetime(2023, 4, 28, 6, 46, 29, 24000, tzinfo=UTC),
        "sentinel-2b",
        "sentinel-2-l2a",
        1.2,
        "https://stac.dataspace.copernicus.eu/v1/",
        None,
        "CC-BY-4.0",
        (AssetReference("B02", "s3://cdse/B02.jp2", None, ("data",)),),
    )


@pytest.fixture
def pc_item():
    return {
        "type": "Feature",
        "id": "S2B_MSIL2A_20230428T064629_R020_T40RBN_20230428T122311",
        "collection": "sentinel-2-l2a",
        "properties": {
            "datetime": "2023-04-28T06:46:29.024Z",
            "platform": "sentinel-2b",
            "eo:cloud_cover": 1.2,
            "s2:mgrs_tile": "40RBN",
            "s2:utm_zone": 40,
            "s2:latitude_band": "R",
            "s2:grid_square": "BN",
            "sat:relative_orbit": 20,
            "s2:processing_baseline": "05.09",
            "s2:generation_time": "2023-04-28T12:23:11.362052Z",
        },
        "assets": {
            key: {
                "href": f"https://sentinel2l2a01.blob.core.windows.net/test/{key}."
                + ("xml" if key == "product-metadata" else "tif"),
                "type": "application/xml"
                if key == "product-metadata"
                else "image/tiff; application=geotiff; profile=cloud-optimized",
                "roles": ["metadata" if key == "product-metadata" else "data"],
            }
            for key in REQUIRED_ASSETS
        },
    }


@pytest.fixture
def resolved(cdse_candidate, pc_item):
    return match_and_resolve(
        cdse_candidate, (pc_item,), OpticalConfig(), license_name="proprietary"
    )


def xml_body(offset=-1000, quantification=10000, baseline="05.09"):
    physical = ("B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B8A", "B9", "B10", "B11", "B12")
    mapping = "".join(
        f'<Spectral_Information bandId="{i}" physicalBand="{name}"/>'
        for i, name in enumerate(physical)
    )
    offsets = "".join(f'<BOA_ADD_OFFSET band_id="{i}">{offset}</BOA_ADD_OFFSET>' for i in range(13))
    return (
        f'<root xmlns="urn:test"><PROCESSING_BASELINE>{baseline}</PROCESSING_BASELINE>'
        f"<BOA_QUANTIFICATION_VALUE>{quantification}</BOA_QUANTIFICATION_VALUE>"
        f"{mapping}{offsets}</root>"
    ).encode()


@pytest.fixture
def product_xml():
    return xml_body()


@pytest.fixture
def band_order():
    return BANDS
