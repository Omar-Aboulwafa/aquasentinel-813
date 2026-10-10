from dataclasses import replace
from pathlib import Path

import pytest

from aquasentinel.config import STACConfig, load_config
from aquasentinel.ingestion.sentinel2 import search_sentinel2
from aquasentinel.runtime import build_runtime_context


def test_catalog_defaults():
    config = load_config()
    assert config.catalog.endpoint == "https://stac.dataspace.copernicus.eu/v1/"
    assert config.catalog.collection == "sentinel-2-l2a"
    assert config.catalog.timeout_seconds == 30


@pytest.mark.parametrize("threshold", [30, 12.5])
def test_numeric_toml_cloud_threshold_loads(tmp_path, threshold):
    text = Path("config/default.toml").read_text()
    path = tmp_path / "numeric-cloud.toml"
    path.write_text(
        text.replace("max_cloud_cover_percent = 30", f"max_cloud_cover_percent = {threshold}")
    )
    assert load_config(path).analysis.max_cloud_cover_percent == float(threshold)


@pytest.mark.parametrize("literal", ["true", "false", '"30"'])
def test_non_numeric_toml_cloud_threshold_rejected_before_catalog_request(
    tmp_path, stac_server, literal
):
    _, calls = stac_server
    text = Path("config/default.toml").read_text()
    path = tmp_path / "invalid-cloud.toml"
    path.write_text(
        text.replace("max_cloud_cover_percent = 30", f"max_cloud_cover_percent = {literal}")
    )
    with pytest.raises(TypeError, match="max_cloud_cover_percent must be a real numeric value"):
        search_sentinel2(build_runtime_context(config_path=path))
    assert calls == []


def test_catalog_configurable_and_old_config_still_loads(tmp_path):
    text = Path("config/default.toml").read_text()
    # Change the optical endpoint only; SAR retains its separate frozen provider.
    custom = text.replace("https://stac.dataspace.copernicus.eu/v1/", "https://other.test/stac/", 1)
    custom = custom.replace('collection = "sentinel-2-l2a"', 'collection = "custom-l2a"')
    custom = custom.replace("timeout_seconds = 30", "timeout_seconds = 7.5")
    path = tmp_path / "custom.toml"
    path.write_text(custom)
    assert load_config(path).catalog == STACConfig("https://other.test/stac/", "custom-l2a", 7.5)

    before, rest = text.split("[catalog]\n")
    _, analysis = rest.split("[analysis]\n")
    path.write_text(before + "[analysis]\n" + analysis)
    legacy = load_config(path)
    assert legacy.catalog == STACConfig()
    assert legacy.analysis == load_config().analysis
    assert legacy.hab_weights == load_config().hab_weights


@pytest.mark.parametrize(
    "endpoint",
    [
        "",
        " ",
        "ftp://example.test",
        "https:///missing-host",
        "https://user:secret@example.test",
        "https://example.test?q=1",
        "https://example.test/#fragment",
        " https://example.test",
        "https://example.test:invalid",
        "https://example.test:70000",
        "https://example.test/a path",
    ],
)
def test_invalid_catalog_endpoint(endpoint):
    with pytest.raises(ValueError, match="STAC endpoint"):
        replace(STACConfig(), endpoint=endpoint).validate()


@pytest.mark.parametrize("collection", ["", " ", " sentinel-2-l2a", None])
def test_invalid_collection(collection):
    with pytest.raises(ValueError, match="STAC collection"):
        replace(STACConfig(), collection=collection).validate()


@pytest.mark.parametrize("timeout", [0, -1, float("nan"), float("inf"), True, "30"])
def test_invalid_timeout(timeout):
    with pytest.raises(ValueError, match="timeout_seconds"):
        replace(STACConfig(), timeout_seconds=timeout).validate()
