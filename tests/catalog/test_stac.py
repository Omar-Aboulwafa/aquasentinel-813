import pytest
from pystac_client.exceptions import APIError

from aquasentinel.catalog.stac import CatalogMetadataError
from aquasentinel.ingestion.sentinel2 import search_sentinel2


def test_search_parameters_and_no_raster_requests(search_context, stac_server, candidate_item):
    responses, calls = stac_server
    endpoint = search_context.config.catalog.endpoint
    responses[endpoint + "search"]["features"] = [candidate_item()]
    assert len(search_sentinel2(search_context)) == 1
    assert [call[0] for call in calls] == [
        endpoint,
        endpoint + "collections/sentinel-2-l2a",
        endpoint + "search",
    ]
    _, method, parameters, timeout = calls[-1]
    assert timeout == 30
    assert method == "POST"
    assert parameters["collections"] == ("sentinel-2-l2a",)
    assert parameters["intersects"] == {
        "type": "Polygon",
        "coordinates": search_context.primary_validation_aoi.coordinates,
    }
    assert parameters["datetime"] == "2023-03-01T00:00:00Z/2023-05-31T23:59:59.999999Z"
    assert parameters["query"] == {"eo:cloud_cover": {"lte": 30.0}}
    assert "limit" not in parameters


def test_all_pages_consumed_and_sorted(search_context, stac_server, candidate_item):
    responses, calls = stac_server
    endpoint = search_context.config.catalog.endpoint
    responses[endpoint + "search"] = {
        "type": "FeatureCollection",
        "features": [candidate_item("late", "2023-05-01T00:00:00Z")],
        "links": [{"rel": "next", "href": endpoint + "page2"}],
    }
    responses[endpoint + "page2"] = {
        "type": "FeatureCollection",
        "features": [candidate_item("early", "2023-03-01T00:00:00Z")],
        "links": [],
    }
    assert [scene.item_id for scene in search_sentinel2(search_context)] == ["early", "late"]
    assert calls[-1][0] == endpoint + "page2"


def test_valid_zero_results(search_context, stac_server):
    assert search_sentinel2(search_context) == ()


def test_post_pagination_preserves_body_and_query(search_context, stac_server, candidate_item):
    responses, calls = stac_server
    endpoint = search_context.config.catalog.endpoint
    responses[endpoint + "search"] = {
        "type": "FeatureCollection",
        "features": [candidate_item("a")],
        "links": [
            {
                "rel": "next",
                "href": endpoint + "page2",
                "method": "POST",
                "merge": True,
                "body": {"token": "2"},
            }
        ],
    }
    responses[endpoint + "page2"] = {
        "type": "FeatureCollection",
        "features": [candidate_item("b")],
        "links": [],
    }
    assert len(search_sentinel2(search_context)) == 2
    assert calls[-1][1] == "POST"
    assert calls[-1][2]["token"] == "2"
    assert calls[-1][2]["query"] == {"eo:cloud_cover": {"lte": 30.0}}


def test_pagination_cycle_fails_instead_of_looping(search_context, stac_server, candidate_item):
    responses, calls = stac_server
    endpoint = search_context.config.catalog.endpoint
    page = {
        "type": "FeatureCollection",
        "features": [candidate_item()],
        "links": [{"rel": "next", "href": endpoint + "page2"}],
    }
    responses[endpoint + "search"] = page
    responses[endpoint + "page2"] = page
    with pytest.raises(CatalogMetadataError, match="repeats"):
        search_sentinel2(search_context)
    assert len(calls) == 4


@pytest.mark.parametrize(
    "page",
    [
        {},
        {"type": "FeatureCollection"},
        {"type": "FeatureCollection", "features": None},
        {"type": "FeatureCollection", "features": [], "links": ["invalid"]},
        {"type": "FeatureCollection", "features": [], "links": [{"rel": "next", "href": "next"}]},
    ],
)
def test_malformed_page_is_not_empty_success(search_context, stac_server, page):
    responses, _ = stac_server
    responses[search_context.config.catalog.endpoint + "search"] = page
    with pytest.raises(CatalogMetadataError):
        search_sentinel2(search_context)


@pytest.mark.parametrize("stage", ["root", "search", "next"])
def test_catalog_errors_propagate_without_partial_results(
    search_context, stac_server, candidate_item, stage
):
    responses, _ = stac_server
    endpoint = search_context.config.catalog.endpoint
    failure = APIError("network/catalog failure")
    if stage == "root":
        responses[endpoint] = failure
    elif stage == "search":
        responses[endpoint + "search"] = failure
    else:
        responses[endpoint + "search"] = {
            "type": "FeatureCollection",
            "features": [candidate_item()],
            "links": [{"rel": "next", "href": endpoint + "page2"}],
        }
        responses[endpoint + "page2"] = failure
    with pytest.raises(APIError, match="network/catalog failure") as error:
        search_sentinel2(search_context)
    assert error.value is failure
