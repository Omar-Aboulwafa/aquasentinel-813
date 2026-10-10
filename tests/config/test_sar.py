from dataclasses import replace

import pytest

from aquasentinel.config import SARConfig


def test_sar_defaults_match_decision_054_provider_contract():
    settings = SARConfig()
    settings.validate()
    assert settings.discovery_collection == "sentinel-1-grd"
    assert settings.access_collection == "sentinel-1-grd"
    assert settings.allowed_asset_hosts == ("sentinel1euwest.blob.core.windows.net",)


@pytest.mark.parametrize(
    "settings",
    [
        replace(SARConfig(), discovery_endpoint="http://stac.dataspace.copernicus.eu/v1/"),
        replace(SARConfig(), access_endpoint="http://planetarycomputer.microsoft.com/api/stac/v1/"),
        replace(
            SARConfig(),
            signing_endpoint="http://planetarycomputer.microsoft.com/api/sas/v1/sign",
        ),
        replace(SARConfig(), allowed_asset_hosts=("SENTINEL1EUWEST.blob.core.windows.net",)),
    ],
)
def test_sar_rejects_insecure_or_noncanonical_service_configuration(settings):
    with pytest.raises(ValueError):
        settings.validate()
