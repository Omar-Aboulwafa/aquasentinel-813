from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class AOIFeature:
    feature_id: str
    name: str
    role: str
    geometry_type: str
    coordinates: Any


@dataclass(frozen=True)
class AOICollection:
    name: str
    features: tuple[AOIFeature, ...]

    def get_by_role(self, role: str) -> tuple[AOIFeature, ...]:
        return tuple(feature for feature in self.features if feature.role == role)


def _validate_position(position: list[float]) -> None:
    if len(position) < 2:
        raise ValueError("A GeoJSON position must contain longitude and latitude.")

    longitude = float(position[0])
    latitude = float(position[1])

    if not -180 <= longitude <= 180:
        raise ValueError(f"Longitude out of range: {longitude}")

    if not -90 <= latitude <= 90:
        raise ValueError(f"Latitude out of range: {latitude}")


def _validate_point(coordinates: list[float]) -> None:
    _validate_position(coordinates)


def _validate_polygon(coordinates: list[list[list[float]]]) -> None:
    if not coordinates:
        raise ValueError("Polygon must contain at least one linear ring.")

    exterior_ring = coordinates[0]

    if len(exterior_ring) < 4:
        raise ValueError("Polygon exterior ring must contain at least four positions.")

    if exterior_ring[0] != exterior_ring[-1]:
        raise ValueError("Polygon exterior ring must be closed.")

    for ring in coordinates:
        for position in ring:
            _validate_position(position)


def load_aoi(path: str | Path) -> AOICollection:
    path = Path(path)

    if not path.exists():
        raise FileNotFoundError(f"AOI GeoJSON file not found: {path}")

    with path.open(encoding="utf-8") as file:
        raw = json.load(file)

    if raw.get("type") != "FeatureCollection":
        raise ValueError("AOI GeoJSON must be a FeatureCollection.")

    raw_features = raw.get("features")

    if not isinstance(raw_features, list) or not raw_features:
        raise ValueError("AOI FeatureCollection must contain at least one feature.")

    features: list[AOIFeature] = []
    seen_ids: set[str] = set()

    for raw_feature in raw_features:
        properties = raw_feature.get("properties", {})
        geometry = raw_feature.get("geometry")

        if not isinstance(geometry, dict):
            raise TypeError("Every AOI feature must contain a geometry.")

        feature_id = str(properties.get("id", "")).strip()
        name = str(properties.get("name", "")).strip()
        role = str(properties.get("role", "")).strip()

        if not feature_id:
            raise ValueError("Every AOI feature must have a non-empty properties.id.")

        if feature_id in seen_ids:
            raise ValueError(f"Duplicate AOI feature id: {feature_id}")

        seen_ids.add(feature_id)

        if not name:
            raise ValueError(f"Feature {feature_id} must have a name.")

        if not role:
            raise ValueError(f"Feature {feature_id} must have a role.")

        geometry_type = geometry.get("type")
        coordinates = geometry.get("coordinates")

        if geometry_type == "Point":
            _validate_point(coordinates)
        elif geometry_type == "Polygon":
            _validate_polygon(coordinates)
        else:
            raise ValueError(
                f"Unsupported geometry type for feature {feature_id}: {geometry_type}"
            )

        features.append(
            AOIFeature(
                feature_id=feature_id,
                name=name,
                role=role,
                geometry_type=geometry_type,
                coordinates=coordinates,
            )
        )

    collection = AOICollection(
        name=str(raw.get("name", path.stem)),
        features=tuple(features),
    )

    if not collection.get_by_role("validation_aoi"):
        raise ValueError("AOI collection must contain a validation_aoi feature.")

    return collection
