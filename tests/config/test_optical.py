from dataclasses import replace
from pathlib import Path

import pytest

from aquasentinel.config import OpticalConfig, load_config


def test_optical_defaults_and_legacy_toml(tmp_path):
    settings = load_config().optical
    settings.validate()
    assert settings.target_crs == "EPSG:32640"
    assert settings.target_resolution == 20
    assert settings.timeout_seconds == 30
    assert tuple(settings.allowed_asset_hosts) == ("sentinel2l2a01.blob.core.windows.net",)
    path = tmp_path / "legacy.toml"
    path.write_text(Path("config/default.toml").read_text().split("[optical]")[0])
    assert load_config(path).optical == OpticalConfig()


@pytest.mark.parametrize(
    "field,value",
    [
        ("endpoint", "http://example.test"),
        ("endpoint", "https://bad^host.test"),
        ("endpoint", "https://bad-.test"),
        ("allowed_asset_hosts", ("host.-bad.test",)),
        ("allowed_asset_hosts", ("a" * 64 + ".test",)),
        ("endpoint", "https://u:p@example.test"),
        ("signing_endpoint", "https://example.test/?secret=x"),
        ("signing_endpoint", "https://example.test/#fragment"),
        ("endpoint", "https://example.test:bad"),
        ("endpoint", "https://example.test/a path"),
        ("allowed_asset_hosts", ()),
        ("allowed_asset_hosts", "example.test"),
        ("allowed_asset_hosts", ("*.test",)),
        ("allowed_asset_hosts", ("https://host.test",)),
        ("allowed_asset_hosts", ("host.test:443",)),
        ("allowed_asset_hosts", ("HOST.test",)),
        ("allowed_asset_hosts", ("host.test", "host.test")),
        ("timeout_seconds", True),
        ("timeout_seconds", 0),
        ("timeout_seconds", float("nan")),
        ("target_resolution", True),
        ("target_resolution", 0),
        ("target_resolution", float("inf")),
        ("target_resolution", "20"),
        ("target_crs", "EPSG:4326"),
        ("target_crs", "EPSG:bad"),
        ("target_crs", "EPSG:2263"),
        ("target_crs", None),
    ],
)
def test_invalid_optical_configuration(field, value):
    with pytest.raises(ValueError):
        replace(OpticalConfig(), **{field: value}).validate()
