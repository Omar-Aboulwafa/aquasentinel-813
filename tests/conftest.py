"""Small synthetic STAC responses; no live data or raster assets in tests."""

import json
from dataclasses import replace

import pytest
from pystac_client.stac_api_io import StacApiIO

from aquasentinel.config import STACConfig
from aquasentinel.runtime import build_runtime_context

ENDPOINT = "https://example.test/v1/"


@pytest.fixture
def candidate_item():
    def make(item_id="S2_TEST_A", timestamp="2023-04-15T06:30:00Z", cloud_cover=12.5):
        return {
            "type": "Feature",
            "stac_version": "1.0.0",
            "id": item_id,
            "collection": "sentinel-2-l2a",
            "geometry": {"type": "Point", "coordinates": [54.55, 24.44]},
            "bbox": [54.55, 24.44, 54.55, 24.44],
            "properties": {
                "datetime": timestamp,
                "platform": "sentinel-2a",
                "eo:cloud_cover": cloud_cover,
            },
            "links": [{"rel": "self", "href": f"{ENDPOINT}items/{item_id}"}],
            "assets": {
                "B04": {
                    "href": f"s3://test-bucket/{item_id}/B04.tif",
                    "type": "image/tiff; application=geotiff",
                    "roles": ["data", "reflectance"],
                },
            },
        }

    return make


@pytest.fixture
def search_context():
    context = build_runtime_context()
    return replace(context, config=replace(context.config, catalog=STACConfig(endpoint=ENDPOINT)))


@pytest.fixture
def stac_server(monkeypatch):
    """Exercise the real client/IO/pagination with only HTTP responses replaced."""
    responses = {
        ENDPOINT: {
            "type": "Catalog",
            "stac_version": "1.0.0",
            "id": "synthetic-catalog",
            "description": "Offline fixture",
            "conformsTo": [
                "https://api.stacspec.org/v1.0.0/core",
                "https://api.stacspec.org/v1.0.0/collections",
                "https://api.stacspec.org/v1.0.0/item-search",
                "https://api.stacspec.org/v1.0.0/item-search#query",
            ],
            "links": [
                {"rel": "self", "href": ENDPOINT},
                {"rel": "root", "href": ENDPOINT},
                {"rel": "search", "href": f"{ENDPOINT}search", "type": "application/geo+json"},
                {"rel": "data", "href": f"{ENDPOINT}collections"},
            ],
        },
        f"{ENDPOINT}collections/sentinel-2-l2a": {
            "type": "Collection",
            "stac_version": "1.0.0",
            "id": "sentinel-2-l2a",
            "description": "Synthetic collection",
            "license": "fixture-license",
            "extent": {
                "spatial": {"bbox": [[-180, -90, 180, 90]]},
                "temporal": {"interval": [["2015-01-01T00:00:00Z", None]]},
            },
            "links": [],
        },
        f"{ENDPOINT}search": {"type": "FeatureCollection", "features": [], "links": []},
    }
    calls = []

    def request(self, href, method=None, **kwargs):
        calls.append((href, method, kwargs.get("parameters"), self.timeout))
        response = responses[href]
        if isinstance(response, Exception):
            raise response
        return json.dumps(response)

    monkeypatch.setattr(StacApiIO, "request", request)
    return responses, calls
