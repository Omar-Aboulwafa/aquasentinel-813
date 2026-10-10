from aquasentinel.catalog.stac import search_catalog


def test_sentinel1_non_optical_search_consumes_all_pages(search_context, stac_server):
    from dataclasses import replace

    responses, calls = stac_server
    endpoint = search_context.config.catalog.endpoint
    collection = responses[endpoint + "collections/sentinel-2-l2a"].copy()
    collection["id"] = "sentinel-1-grd"
    responses[endpoint + "collections/sentinel-1-grd"] = collection
    for index in range(3):
        url = endpoint + ("search" if index == 0 else f"page{index}")
        responses[url] = {
            "type": "FeatureCollection",
            "features": [{"id": f"S1_{index}"}],
            "links": (
                [
                    {
                        "rel": "next",
                        "href": endpoint + f"page{index + 1}",
                        "method": "POST",
                        "merge": True,
                        "body": {"cursor": str(index + 1)},
                    }
                ]
                if index < 2
                else []
            ),
        }
    result = search_catalog(
        replace(search_context.config.catalog, collection="sentinel-1-grd"),
        intersects={"type": "Polygon", "coordinates": []},
        datetime_interval="2026-04-24T00:00:00Z/2026-05-18T23:59:59Z",
    )
    assert [item["id"] for item in result.items] == ["S1_0", "S1_1", "S1_2"]
    assert calls[-1][0] == endpoint + "page2"
    assert all("query" not in call[2] for call in calls if call[2])


def test_catalog_query_can_be_omitted_for_non_optical_search(search_context, stac_server):
    _, calls = stac_server
    result = search_catalog(
        search_context.config.catalog,
        intersects={
            "type": "Polygon",
            "coordinates": [[[49.6, 28.6], [50.7, 28.6], [50.7, 29.6], [49.6, 29.6], [49.6, 28.6]]],
        },
        datetime_interval="2026-04-24T00:00:00Z/2026-05-18T23:59:59Z",
        query=None,
    )
    assert result.items == ()
    parameters = calls[-1][2]
    assert "query" not in parameters
    assert "eo:cloud_cover" not in repr(parameters)
