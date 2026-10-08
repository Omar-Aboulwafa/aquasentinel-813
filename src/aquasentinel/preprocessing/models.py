"""Typed AOI preprocessing outputs with explicit masks and fraction definitions."""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from datetime import datetime
from hashlib import sha256
from typing import Any

import numpy as np
from numpy.typing import NDArray
from rasterio import Affine

from aquasentinel.ingestion.sentinel2_assets import BANDS, ResolvedOpticalSource
from aquasentinel.provenance import DerivedProductRecord


@dataclass(frozen=True)
class AnalysisGrid:
    crs: str
    transform: Affine
    width: int
    height: int
    resolution: float
    bounds: tuple[float, float, float, float]
    grid_id: str

    @property
    def shape(self) -> tuple[int, int]:
        return self.height, self.width

    def to_dict(self) -> dict[str, Any]:
        return {**asdict(self), "transform": list(self.transform)[:6], "bounds": list(self.bounds)}

    @classmethod
    def from_dict(cls, payload: dict[str, Any]) -> AnalysisGrid:
        return cls(
            **{
                **payload,
                "transform": Affine(*payload["transform"]),
                "bounds": tuple(payload["bounds"]),
            }
        )


@dataclass(frozen=True)
class SceneStatistics:
    aoi_pixel_count: int
    valid_data_count: int
    candidate_water_count: int
    valid_water_count: int
    valid_water_fraction_of_aoi: float | None
    water_retained_fraction: float | None


@dataclass(frozen=True)
class PreprocessedOpticalScene:
    resolved_source: ResolvedOpticalSource
    grid: AnalysisGrid
    reflectance: dict[str, NDArray[np.float32]]
    scl: NDArray[np.uint8]
    aoi_mask: NDArray[np.bool_]
    valid_data_mask: NDArray[np.bool_]
    water_mask: NDArray[np.bool_]
    valid_water_mask: NDArray[np.bool_]
    interpolation_support_mask: NDArray[np.bool_]
    statistics: SceneStatistics
    processing_parameters: dict[str, Any]
    cache_id: str
    provenance: DerivedProductRecord

    @property
    def source_id(self) -> str:
        return self.resolved_source.source.source_id

    @property
    def item_id(self) -> str:
        return self.resolved_source.source.product_id

    @property
    def acquired_at(self) -> datetime:
        return self.resolved_source.source.acquired_at

    @property
    def band_order(self) -> tuple[str, ...]:
        return BANDS

    def validate(self) -> None:
        if tuple(self.reflectance) != BANDS:
            raise ValueError("Reflectance requires all nine bands in canonical order.")
        for array in self.reflectance.values():
            if array.shape != self.grid.shape or array.dtype != np.float32:
                raise ValueError("Reflectance array shape/dtype differs from the analysis grid.")
        if self.scl.shape != self.grid.shape or self.scl.dtype != np.uint8:
            raise ValueError("SCL shape/dtype differs from the analysis grid.")
        for mask in (
            self.aoi_mask,
            self.valid_data_mask,
            self.water_mask,
            self.valid_water_mask,
            self.interpolation_support_mask,
        ):
            if mask.shape != self.grid.shape or mask.dtype != bool:
                raise ValueError("Quality mask shape/dtype differs from the analysis grid.")
        if np.any(
            self.valid_water_mask
            & ~(
                self.aoi_mask
                & self.valid_data_mask
                & self.water_mask
                & self.interpolation_support_mask
            )
        ):
            raise ValueError("Valid-water pixels lack mandatory quality/support.")
        if any(
            not np.all(np.isfinite(b[self.valid_water_mask])) for b in self.reflectance.values()
        ):
            raise ValueError("Valid-water reflectance must be finite in every band.")
        if self.provenance.source_ids != (self.source_id,):
            raise ValueError("Derived pixel lineage must reference the actual PC source only.")
        if self.resolved_source.native_grids != self.processing_parameters["source_grids"]:
            raise ValueError("Typed source grids differ from processing evidence.")
        if (
            self.resolved_source.decoding_metadata
            != self.processing_parameters["identity"]["decoding"]
        ):
            raise ValueError("Typed source decoding differs from product XML evidence.")
        self.provenance.validate()


def geometry_digest(geometry: dict[str, Any]) -> str:
    encoded = (
        json.dumps(geometry, sort_keys=True, separators=(",", ":"), allow_nan=False) + "\n"
    ).encode()
    return sha256(encoded).hexdigest()
