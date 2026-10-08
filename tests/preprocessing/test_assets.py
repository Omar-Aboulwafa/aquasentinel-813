from copy import deepcopy
from dataclasses import replace
from datetime import UTC, datetime

import pytest

from aquasentinel.catalog.stac import CatalogResult
from aquasentinel.config import OpticalConfig
from aquasentinel.ingestion import sentinel2_assets
from aquasentinel.ingestion.sentinel2_assets import (
    REQUIRED_ASSETS,
    ObservationMatchError,
    discovery_identity,
    match_and_resolve,
    resolve_optical_source,
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


def _processed_product(pc_item, baseline, generation):
    item = deepcopy(pc_item)
    item["id"] = item["id"].rsplit("_", 1)[0] + "_" + generation
    item["properties"]["s2:processing_baseline"] = baseline
    item["properties"]["s2:generation_time"] = datetime.strptime(
        generation, "%Y%m%dT%H%M%S"
    ).replace(tzinfo=UTC).isoformat()
    item["properties"]["s2:product_uri"] = item["id"].replace(
        "_R", f"_N{baseline.replace('.', '')}_R"
    ) + ".SAFE"
    return item


@pytest.mark.parametrize("baseline", ["05.09", "05.10"])
@pytest.mark.parametrize("reverse", [False, True])
def test_explicit_baseline_selects_unique_product(cdse_candidate, pc_item, baseline, reverse):
    products = (
        _processed_product(pc_item, "05.09", "20230428T122311"),
        _processed_product(pc_item, "05.10", "20240831T052931"),
    )
    selected = match_and_resolve(
        cdse_candidate, products[::-1] if reverse else products, OpticalConfig(),
        required_processing_baseline=baseline,
    )
    assert selected.processing_baseline == baseline
    expected = products[0 if baseline == "05.09" else 1]
    assert selected.source.product_id == expected["id"]
    assert selected.generation_time == expected["properties"]["s2:generation_time"]
    assert selected.provider_metadata["s2:product_uri"] == expected["properties"]["s2:product_uri"]
    assert selected.discovery_source == cdse_candidate.to_source_record()
    assert selected.source.source_id != selected.discovery_source.source_id
    assert {asset.key for asset in selected.assets} == set(REQUIRED_ASSETS)


@pytest.mark.parametrize("baseline,count", [(None, 2), ("05.11", 0)])
def test_baseline_constraint_does_not_fall_back(cdse_candidate, pc_item, baseline, count):
    products = (
        _processed_product(pc_item, "05.09", "20230428T122311"),
        _processed_product(pc_item, "05.10", "20240831T052931"),
    )
    with pytest.raises(ObservationMatchError, match=f"found {count}"):
        match_and_resolve(
            cdse_candidate, products, OpticalConfig(), required_processing_baseline=baseline
        )


def test_multiple_same_baseline_generations_fail(cdse_candidate, pc_item):
    products = (
        _processed_product(pc_item, "05.09", "20230428T122311"),
        _processed_product(pc_item, "05.09", "20230429T122311"),
    )
    for items in (products, products[::-1]):
        with pytest.raises(ObservationMatchError, match="found 2"):
            match_and_resolve(
                cdse_candidate, items, OpticalConfig(), required_processing_baseline="05.09"
            )


@pytest.mark.parametrize("dimension", ["acquisition", "platform", "tile", "orbit"])
def test_constraint_preserves_exact_observation_matching(cdse_candidate, pc_item, dimension):
    other = deepcopy(pc_item)
    if dimension == "acquisition":
        other["properties"]["datetime"] = "2023-04-28T06:46:29.025Z"
    elif dimension == "platform":
        other["id"] = other["id"].replace("S2B", "S2A")
        other["properties"]["platform"] = "sentinel-2a"
    elif dimension == "tile":
        other["id"] = other["id"].replace("40RBN", "40RBM")
        other["properties"]["s2:mgrs_tile"] = "40RBM"
        other["properties"]["s2:grid_square"] = "BM"
    else:
        other["id"] = other["id"].replace("R020", "R021")
        other["properties"]["sat:relative_orbit"] = 21
    selected = match_and_resolve(
        cdse_candidate, (other, pc_item), OpticalConfig(), required_processing_baseline="05.09"
    )
    assert selected.source.product_id == pc_item["id"]
    with pytest.raises(ObservationMatchError, match="found 0"):
        match_and_resolve(
            cdse_candidate, (other,), OpticalConfig(), required_processing_baseline="05.09"
        )


@pytest.mark.parametrize(
    "field,value",
    [("datetime", "2023-04-28T06:46:29.024"), ("sat:relative_orbit", 21),
     ("s2:processing_baseline", "unknown"), ("s2:generation_time", "2024-08-30T05:29:31Z"),
     ("s2:product_uri", "S2B_MSIL2A_20230428T064629_N0509_R020_T40RBN_20240831T052931.SAFE")],
)
def test_other_baseline_metadata_validated_before_filter(
    cdse_candidate, pc_item, field, value
):
    other = _processed_product(pc_item, "05.10", "20240831T052931")
    other["properties"][field] = value
    with pytest.raises(ObservationMatchError, match="metadata"):
        match_and_resolve(
            cdse_candidate, (pc_item, other), OpticalConfig(), required_processing_baseline="05.09"
        )


@pytest.mark.parametrize("baseline", ["", " 05.09", "05.09 ", "05.09\n", "5.9", "0509",
                                      "05x09", "05.009", "bad", 5.09, 509, True, False, []])
def test_invalid_selector_rejected_before_resolution(cdse_candidate, pc_item, monkeypatch, baseline):
    def forbidden(*args, **kwargs):
        pytest.fail("Invalid selector must fail before metadata validation or catalog access")

    monkeypatch.setattr(sentinel2_assets, "search_catalog", forbidden)
    monkeypatch.setattr(sentinel2_assets, "_pc_identity", forbidden)
    with pytest.raises(ObservationMatchError, match="NN.NN"):
        match_and_resolve(
            cdse_candidate, (pc_item,), OpticalConfig(), required_processing_baseline=baseline
        )
    with pytest.raises(ObservationMatchError, match="NN.NN"):
        resolve_optical_source(
            cdse_candidate, {}, OpticalConfig(), required_processing_baseline=baseline
        )


@pytest.mark.parametrize("baseline", ["05.09", "05.10"])
def test_resolver_forwards_constraint_to_validated_matching(cdse_candidate, pc_item, monkeypatch,
                                                          baseline):
    products = (
        _processed_product(pc_item, "05.09", "20230428T122311"),
        _processed_product(pc_item, "05.10", "20240831T052931"),
    )
    calls = []

    def catalog(settings, **kwargs):
        calls.append(kwargs)
        return CatalogResult(products, "fixture-license")

    monkeypatch.setattr(sentinel2_assets, "search_catalog", catalog)
    selected = resolve_optical_source(
        cdse_candidate, {"type": "Polygon"}, OpticalConfig(), required_processing_baseline=baseline
    )
    assert selected.processing_baseline == baseline
    assert len(calls) == 1
    assert calls[0]["intersects"] == {"type": "Polygon"}
    assert calls[0]["max_cloud_cover_percent"] == 100
    assert selected.source.license_name == "fixture-license"


@pytest.mark.parametrize("key", REQUIRED_ASSETS)
def test_selected_baseline_required_assets_still_enforced(cdse_candidate, pc_item, key):
    other = _processed_product(pc_item, "05.10", "20240831T052931")
    del pc_item["assets"][key]
    with pytest.raises(ObservationMatchError, match="missing"):
        match_and_resolve(
            cdse_candidate, (other, pc_item), OpticalConfig(), required_processing_baseline="05.09"
        )


@pytest.mark.parametrize(
    "field,value",
    [("href", "https://unapproved.test/B02.tif"),
     ("href", "https://sentinel2l2a01.blob.core.windows.net/B02.tif?sig=fake-secret"),
     ("type", "image/jp2"), ("type", "image/tiff"), ("type", None)],
)
def test_selected_baseline_unsafe_assets_still_rejected(cdse_candidate, pc_item, field, value):
    other = _processed_product(pc_item, "05.10", "20240831T052931")
    pc_item["assets"]["B02"][field] = value
    with pytest.raises(ObservationMatchError) as error:
        match_and_resolve(
            cdse_candidate, (other, pc_item), OpticalConfig(), required_processing_baseline="05.09"
        )
    assert "fake-secret" not in str(error.value)
    assert "https://" not in str(error.value)
