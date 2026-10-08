from copy import deepcopy
from dataclasses import replace

import pytest

from aquasentinel.config import OpticalConfig
from aquasentinel.ingestion.sentinel2_assets import (
    REQUIRED_ASSETS,
    ObservationMatchError,
    discovery_identity,
    match_and_resolve,
)


def test_strict_same_acquisition_different_product(resolved, cdse_candidate):
    assert resolved.source.product_id != cdse_candidate.item_id
    assert resolved.source.source_id != resolved.discovery_source.source_id
    assert resolved.identity.tile == "40RBN"
    assert resolved.identity.relative_orbit == 20
    assert resolved.processing_baseline == "05.09"
    assert resolved.discovery_processing["processing_baseline"] == "05.10"
    assert {a.key for a in resolved.assets} == set(REQUIRED_ASSETS)


def test_zero_and_ambiguous_match(cdse_candidate, pc_item):
    for items in ((), (pc_item, pc_item)):
        with pytest.raises(ObservationMatchError, match="exactly one"):
            match_and_resolve(cdse_candidate, items, OpticalConfig())


@pytest.mark.parametrize(
    "field,value",
    [
        ("s2:grid_square", "BM"),
        ("sat:relative_orbit", 21),
        ("platform", "sentinel-2a"),
        ("datetime", "2023-04-28T06:46:30.024Z"),
        ("datetime", "2023-04-28T06:46:29.024"),
        ("s2:generation_time", "2023-04-29T12:23:11Z"),
        ("s2:processing_baseline", "unknown"),
        ("s2:utm_zone", None),
    ],
)
def test_conflicting_pc_metadata(cdse_candidate, pc_item, field, value):
    pc_item["properties"][field] = value
    with pytest.raises(ObservationMatchError):
        match_and_resolve(cdse_candidate, (pc_item,), OpticalConfig())


def test_well_formed_wrong_tile_or_orbit_is_no_match(cdse_candidate, pc_item):
    for tile, orbit in [("40RBM", 20), ("40RBN", 21)]:
        item = deepcopy(pc_item)
        item["id"] = item["id"].replace("T40RBN", f"T{tile}").replace("R020", f"R{orbit:03d}")
        item["properties"]["s2:grid_square"] = tile[-2:]
        item["properties"]["s2:mgrs_tile"] = tile
        item["properties"]["sat:relative_orbit"] = orbit
        with pytest.raises(ObservationMatchError, match="found 0"):
            match_and_resolve(cdse_candidate, (item,), OpticalConfig())


@pytest.mark.parametrize(
    "item_id", ["bad", "S2B_MSIL2A_20230230T064629_N0510_R020_T40RBN_20240831T052931"]
)
def test_malformed_cdse_product(cdse_candidate, item_id):
    with pytest.raises(ObservationMatchError):
        discovery_identity(replace(cdse_candidate, item_id=item_id))


def test_discovery_conflicting_platform(cdse_candidate):
    with pytest.raises(ObservationMatchError):
        discovery_identity(replace(cdse_candidate, platform="sentinel-2a"))


@pytest.mark.parametrize("key", REQUIRED_ASSETS)
def test_required_asset_missing(cdse_candidate, pc_item, key):
    del pc_item["assets"][key]
    with pytest.raises(ObservationMatchError, match="missing"):
        match_and_resolve(cdse_candidate, (pc_item,), OpticalConfig())


@pytest.mark.parametrize(
    "href",
    [
        "https://unapproved.test/B02.tif",
        "https://sentinel2l2a01.blob.core.windows.net/B02.tif?temporary=secret",
    ],
)
def test_asset_host_or_signed_reference_rejected(cdse_candidate, pc_item, href):
    pc_item["assets"]["B02"]["href"] = href
    with pytest.raises(ObservationMatchError, match="stable unsigned") as error:
        match_and_resolve(cdse_candidate, (pc_item,), OpticalConfig())
    assert href not in str(error.value)
    assert "secret" not in str(error.value)
    assert "temporary=" not in str(error.value)
    assert error.value.__context__ is None
    assert error.value.__cause__ is None


def test_signed_source_self_reference_rejected(cdse_candidate, pc_item):
    pc_item["links"] = [
        {"rel": "self", "href": "https://planetarycomputer.microsoft.com/item?temporary=fake"}
    ]
    with pytest.raises(ObservationMatchError, match="Stable source"):
        match_and_resolve(cdse_candidate, (pc_item,), OpticalConfig())


def test_conflicting_product_uri_baseline_rejected(cdse_candidate, pc_item):
    pc_item["properties"]["s2:product_uri"] = (
        "S2B_MSIL2A_20230428T064629_N0510_R020_T40RBN_20230428T122311.SAFE"
    )
    with pytest.raises(ObservationMatchError):
        match_and_resolve(cdse_candidate, (pc_item,), OpticalConfig())


@pytest.mark.parametrize("assets", [[], ["fake-token"], None, "fake-token", 42])
def test_assets_non_object_rejected(cdse_candidate, pc_item, assets):
    pc_item["assets"] = assets
    with pytest.raises(ObservationMatchError, match="assets must be an object") as error:
        match_and_resolve(cdse_candidate, (pc_item,), OpticalConfig())
    assert "fake-token" not in str(error.value)


@pytest.mark.parametrize("href", [None, 42, "https://[malformed/?sig=fake-token",
                                  "http://sentinel2l2a01.blob.core.windows.net/B02.tif?sig=fake-token"])
def test_invalid_required_href_sanitized(cdse_candidate, pc_item, href):
    pc_item["assets"]["B02"]["href"] = href
    with pytest.raises(ObservationMatchError, match="stable unsigned") as error:
        match_and_resolve(cdse_candidate, (pc_item,), OpticalConfig())
    assert "fake-token" not in str(error.value)
    assert "sig=" not in str(error.value)
    assert "http" not in str(error.value)
    assert error.value.__context__ is None
    assert error.value.__cause__ is None
