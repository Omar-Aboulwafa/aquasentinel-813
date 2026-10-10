from aquasentinel.catalog.stac import search_catalog


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
