from dataclasses import replace

import pytest

from aquasentinel.config import SARConfig, load_config


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
        replace(
            SARConfig(),
            signing_endpoint="https://planetarycomputer.microsoft.com:444/api/sas/v1/sign",
        ),
        replace(SARConfig(), signing_endpoint=None),
        replace(
            SARConfig(), allowed_asset_hosts=("sentinel1euwest.blob.core.windows.net", "other.test")
        ),
        replace(SARConfig(), access_collection="sentinel-1-rtc"),
        replace(SARConfig(), discovery_endpoint="https://other.test/stac/"),
        replace(SARConfig(), timeout_seconds=True),
    ],
)
def test_sar_rejects_insecure_or_noncanonical_service_configuration(settings):
    with pytest.raises(ValueError):
        settings.validate()


def test_sar_toml_loading_preserves_frozen_provider_contract():
    config = load_config()
    assert config.sar == SARConfig()
    assert config.catalog.collection == "sentinel-2-l2a"


def test_absent_sar_section_keeps_backward_compatible_defaults(tmp_path):
    from pathlib import Path

    path = tmp_path / "legacy.toml"
    text = Path("config/default.toml").read_text()
    start = text.index("[sar]")
    next_section = text.find("\n[", start + 1)
    path.write_text(text[:start] + (text[next_section:] if next_section >= 0 else ""))
    assert load_config(path).sar == SARConfig()
