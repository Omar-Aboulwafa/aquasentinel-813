from copy import deepcopy
from dataclasses import replace
from datetime import UTC, date, datetime

import pytest

from aquasentinel.config import AOICollection, STACConfig
from aquasentinel.ingestion.sentinel2 import (
    InvalidSearchInputError,
    MalformedItemMetadataError,
    MissingItemMetadataError,
    normalize_item,
    search_sentinel2,
)
from aquasentinel.provenance import ProvenanceRegistry, source_record_to_dict


def test_normalization_and_provenance(search_context, candidate_item):
    scene = normalize_item(
        candidate_item(), search_context.config.catalog, collection_license="fixture-license"
    )
    assert scene.item_id == "S2_TEST_A"
    assert scene.acquired_at == datetime(2023, 4, 15, 6, 30, tzinfo=UTC)
    assert scene.platform == "sentinel-2a"
    assert scene.collection == "sentinel-2-l2a"
    assert scene.cloud_cover_percent == 12.5
    assert scene.catalog == search_context.config.catalog.endpoint
    assert scene.source_url.endswith("/items/S2_TEST_A")
    assert scene.assets[0].key == "B04"
    assert scene.assets[0].href == "s3://test-bucket/S2_TEST_A/B04.tif"
    assert scene.assets[0].roles == ("data", "reflectance")
    assert scene.assets[0].media_type == "image/tiff; application=geotiff"
    record = scene.to_source_record()
    record.validate()
    registry = ProvenanceRegistry()
    registry.add_source(record)
    assert registry.get_source(record.source_id) == record
    assert source_record_to_dict(record)["license_name"] == "fixture-license"
    assert record.product_id == scene.item_id
    assert record.platform == scene.platform
    assert record.catalog == scene.catalog
    assert record.collection == scene.collection
    assert record.source_url == scene.source_url
    assert record.acquired_at == scene.acquired_at


def test_provider_qualified_ids_and_separator_escaping(search_context, candidate_item):
    item = candidate_item("scene:with/separators")
    settings = search_context.config.catalog
    first = normalize_item(item, settings).to_source_record()
    second = normalize_item(item, replace(settings, endpoint="https://another.test/v1/"))
    assert first.source_id != second.to_source_record().source_id
    assert first.source_id.endswith(":sentinel-2-l2a:scene%3Awith%2Fseparators")
    assert first.source_id == normalize_item(item, settings).to_source_record().source_id
    assert (
        first.source_id
        == normalize_item(item, replace(settings, endpoint=settings.endpoint[:-1]))
        .to_source_record()
        .source_id
    )


def test_optional_metadata_not_invented(search_context, candidate_item):
    item = candidate_item()
    item["links"] = []
    scene = normalize_item(item, search_context.config.catalog)
    assert scene.source_url is None
    assert scene.license_name is None
    item["properties"]["license"] = "item-license"
    assert (
        normalize_item(
            item, search_context.config.catalog, collection_license="collection-license"
        ).license_name
        == "item-license"
    )


def test_relative_assets_resolved_and_asset_order_normalized(search_context, candidate_item):
    item = candidate_item()
    item["assets"]["B04"]["href"] = "./B04.tif"
    item["assets"]["B04"]["roles"] = ["reflectance", "data", "data"]
    item["assets"]["B02"] = {"href": "s3://test-bucket/B02.tif"}
    scene = normalize_item(item, search_context.config.catalog)
    assert [asset.key for asset in scene.assets] == ["B02", "B04"]
    assert scene.assets[1].href == "https://example.test/v1/items/B04.tif"
    assert scene.assets[1].roles == ("data", "reflectance")


def test_order_and_exact_duplicates(search_context, stac_server, candidate_item):
    responses, _ = stac_server
    items = [
        candidate_item("b"),
        candidate_item("a"),
        candidate_item("early", "2023-03-01T00:00:00Z"),
        candidate_item("b"),
    ]
    page = responses[search_context.config.catalog.endpoint + "search"]
    page["features"] = items
    first = search_sentinel2(search_context)
    page["features"] = list(reversed(items))
    assert first == search_sentinel2(search_context)
    assert [scene.item_id for scene in first] == ["early", "a", "b"]


@pytest.mark.parametrize("reverse", [False, True])
def test_conflicting_duplicates_rejected(search_context, stac_server, candidate_item, reverse):
    responses, _ = stac_server
    items = [candidate_item(cloud_cover=10), candidate_item(cloud_cover=20)]
    responses[search_context.config.catalog.endpoint + "search"]["features"] = (
        list(reversed(items)) if reverse else items
    )
    with pytest.raises(MalformedItemMetadataError, match="Conflicting duplicate"):
        search_sentinel2(search_context)


def test_utc_boundaries_and_local_filter_recheck(search_context, stac_server, candidate_item):
    responses, _ = stac_server
    responses[search_context.config.catalog.endpoint + "search"]["features"] = [
        candidate_item("first", "2023-03-01T04:00:00+04:00", 30),
        candidate_item("last", "2023-05-31T23:59:59.999999Z", 0),
        candidate_item("before", "2023-02-28T23:59:59Z", 10),
        candidate_item("after", "2023-06-01T00:00:00Z", 10),
        candidate_item("cloudy", cloud_cover=30.1),
    ]
    assert [scene.item_id for scene in search_sentinel2(search_context)] == ["first", "last"]


@pytest.mark.parametrize("field", ["datetime", "eo:cloud_cover", "platform"])
def test_missing_required_properties_are_explicit(search_context, candidate_item, field):
    item = candidate_item()
    del item["properties"][field]
    with pytest.raises(MissingItemMetadataError, match=field):
        normalize_item(item, search_context.config.catalog)


def test_missing_cloud_is_not_silently_dropped(search_context, stac_server, candidate_item):
    responses, _ = stac_server
    item = candidate_item()
    del item["properties"]["eo:cloud_cover"]
    responses[search_context.config.catalog.endpoint + "search"]["features"] = [item]
    with pytest.raises(MissingItemMetadataError, match="eo:cloud_cover"):
        search_sentinel2(search_context)


@pytest.mark.parametrize(
    "field,value",
    [
        ("datetime", "not-a-date"),
        ("datetime", "2023-04-15T00:00:00"),
        ("datetime", 123),
        ("platform", ""),
        ("platform", []),
        ("eo:cloud_cover", "12"),
        ("eo:cloud_cover", True),
        ("eo:cloud_cover", -1),
        ("eo:cloud_cover", 101),
        ("eo:cloud_cover", float("nan")),
        ("eo:cloud_cover", float("inf")),
    ],
)
def test_malformed_properties(search_context, candidate_item, field, value):
    item = candidate_item()
    item["properties"][field] = value
    with pytest.raises(MalformedItemMetadataError, match=field):
        normalize_item(item, search_context.config.catalog)


@pytest.mark.parametrize("field", ["id", "collection", "properties", "assets"])
def test_missing_required_item_fields(search_context, candidate_item, field):
    item = candidate_item()
    del item[field]
    with pytest.raises(MissingItemMetadataError, match=field):
        normalize_item(item, search_context.config.catalog)


@pytest.mark.parametrize(
    "change",
    [
        {"type": "Collection"},
        {"collection": "sentinel-1"},
        {"properties": []},
        {"assets": []},
        {"assets": {"B04": {}}},
        {"links": ["bad-link"]},
    ],
)
def test_malformed_item_structure(search_context, candidate_item, change):
    item = candidate_item()
    item.update(deepcopy(change))
    with pytest.raises((MalformedItemMetadataError, MissingItemMetadataError)):
        normalize_item(item, search_context.config.catalog)


def test_relative_assets_require_self_url(search_context, candidate_item):
    item = candidate_item()
    item["links"] = []
    item["assets"]["B04"]["href"] = "relative.tif"
    with pytest.raises(MalformedItemMetadataError, match="relative asset"):
        normalize_item(item, search_context.config.catalog)


def test_invalid_polygon_rejected_before_network(search_context, stac_server):
    _, calls = stac_server
    feature = replace(search_context.primary_validation_aoi, geometry_type="Point")
    context = replace(search_context, aoi=AOICollection("bad", (feature,)))
    with pytest.raises(InvalidSearchInputError, match="Polygon"):
        search_sentinel2(context)
    assert calls == []


@pytest.mark.parametrize(
    "change",
    [
        {"start_date": date(2024, 1, 1)},
        {"max_cloud_cover_percent": 101},
        {"max_cloud_cover_percent": True},
    ],
)
def test_invalid_analysis_rejected_before_network(search_context, stac_server, change):
    _, calls = stac_server
    config = replace(
        search_context.config, analysis=replace(search_context.config.analysis, **change)
    )
    with pytest.raises(InvalidSearchInputError):
        search_sentinel2(replace(search_context, config=config))
    assert calls == []


def test_endpoint_collection_and_timeout_remain_configurable(
    search_context, stac_server, candidate_item
):
    responses, calls = stac_server
    settings = STACConfig(
        endpoint="https://custom.test/stac/", collection="custom-l2a", timeout_seconds=2
    )
    old = search_context.config.catalog.endpoint
    root = deepcopy(responses[old])
    root["links"] = [
        {"rel": "self", "href": settings.endpoint},
        {"rel": "root", "href": settings.endpoint},
        {"rel": "search", "href": settings.endpoint + "search", "type": "application/geo+json"},
        {"rel": "data", "href": settings.endpoint + "collections"},
    ]
    responses[settings.endpoint] = root
    collection = deepcopy(responses[old + "collections/sentinel-2-l2a"])
    collection["id"] = settings.collection
    responses[settings.endpoint + "collections/custom-l2a"] = collection
    item = candidate_item()
    item["collection"] = settings.collection
    responses[settings.endpoint + "search"] = {
        "type": "FeatureCollection",
        "features": [item],
        "links": [],
    }
    context = replace(search_context, config=replace(search_context.config, catalog=settings))
    (scene,) = search_sentinel2(context)
    assert scene.catalog == settings.endpoint
    assert scene.collection == settings.collection
    assert calls[-1][2]["collections"] == (settings.collection,)
    assert all(call[3] == 2 for call in calls)
