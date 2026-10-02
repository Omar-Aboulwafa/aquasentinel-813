import json

import pytest

from aquasentinel.config import load_aoi


def test_load_demo_aoi() -> None:
    collection = load_aoi("data/aoi/demo_site.geojson")

    assert collection.name == "aquasentinel_demo_site"
    assert len(collection.features) == 2
    assert len(collection.get_by_role("validation_aoi")) == 1
    assert len(collection.get_by_role("validation_reference")) == 1


def test_rejects_unclosed_polygon(tmp_path) -> None:
    invalid_geojson = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "properties": {
                    "id": "bad_polygon",
                    "name": "Bad Polygon",
                    "role": "validation_aoi",
                },
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [54.0, 24.0],
                            [55.0, 24.0],
                            [55.0, 25.0],
                            [54.0, 25.0],
                        ]
                    ],
                },
            }
        ],
    }

    path = tmp_path / "invalid.geojson"
    path.write_text(json.dumps(invalid_geojson), encoding="utf-8")

    with pytest.raises(ValueError, match="must be closed"):
        load_aoi(path)


def test_rejects_invalid_longitude(tmp_path) -> None:
    invalid_geojson = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "properties": {
                    "id": "bad_point",
                    "name": "Bad Point",
                    "role": "validation_aoi",
                },
                "geometry": {
                    "type": "Point",
                    "coordinates": [200.0, 24.0],
                },
            }
        ],
    }

    path = tmp_path / "invalid_longitude.geojson"
    path.write_text(json.dumps(invalid_geojson), encoding="utf-8")

    with pytest.raises(ValueError, match="Longitude out of range"):
        load_aoi(path)