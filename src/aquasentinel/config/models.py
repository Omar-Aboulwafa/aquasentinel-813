from __future__ import annotations

import re
from dataclasses import dataclass, field
from datetime import date
from math import isfinite
from pathlib import Path
from urllib.parse import urlsplit


@dataclass(frozen=True)
class STACConfig:
    endpoint: str = "https://stac.dataspace.copernicus.eu/v1/"
    collection: str = "sentinel-2-l2a"
    timeout_seconds: float = 30.0

    def validate(self) -> None:
        if not isinstance(self.endpoint, str) or not self.endpoint.strip():
            raise ValueError("STAC endpoint must be a non-empty HTTP(S) URL.")
        try:
            parsed = urlsplit(self.endpoint)
            _ = parsed.port  # Validate a supplied port before any catalog request.
        except ValueError as exc:
            raise ValueError("STAC endpoint has an invalid host or port.") from exc
        if (
            self.endpoint != self.endpoint.strip()
            or any(character.isspace() for character in self.endpoint)
            or parsed.scheme not in {"http", "https"}
            or not parsed.hostname
            or parsed.username is not None
            or parsed.password is not None
            or parsed.query
            or parsed.fragment
        ):
            raise ValueError("STAC endpoint must be an HTTP(S) URL without credentials or query.")
        if not isinstance(self.collection, str) or not self.collection.strip():
            raise ValueError("STAC collection cannot be empty.")
        if self.collection != self.collection.strip():
            raise ValueError("STAC collection cannot have surrounding whitespace.")
        if (
            isinstance(self.timeout_seconds, bool)
            or not isinstance(self.timeout_seconds, (int, float))
            or not isfinite(self.timeout_seconds)
            or self.timeout_seconds <= 0
        ):
            raise ValueError("STAC timeout_seconds must be a finite positive number.")


@dataclass(frozen=True)
class RiskWeights:
    values: dict[str, float]

    def validate(self) -> None:
        if not self.values:
            raise ValueError("Risk weights cannot be empty.")

        if any(value < 0 for value in self.values.values()):
            raise ValueError("Risk weights cannot contain negative values.")

        total = sum(self.values.values())
        if abs(total - 1.0) > 1e-9:
            raise ValueError(f"Risk weights must sum to 1.0, got {total:.6f}.")


@dataclass(frozen=True)
class RiskBands:
    low_max: int
    watch_max: int
    elevated_max: int
    high_max: int

    def validate(self) -> None:
        values = [
            self.low_max,
            self.watch_max,
            self.elevated_max,
            self.high_max,
        ]

        if values != sorted(values):
            raise ValueError("Risk-band thresholds must be ordered.")

        if self.high_max != 100:
            raise ValueError("High risk maximum must be 100.")


@dataclass(frozen=True)
class AnalysisConfig:
    start_date: date
    end_date: date
    max_cloud_cover_percent: float

    def validate(self) -> None:
        if self.start_date > self.end_date:
            raise ValueError("Analysis start_date must be before end_date.")

        if not 0 <= self.max_cloud_cover_percent <= 100:
            raise ValueError("Cloud cover must be between 0 and 100.")


def _is_hostname(host: object) -> bool:
    return (
        isinstance(host, str)
        and 0 < len(host) <= 253
        and "." in host
        and all(
            re.fullmatch(r"[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?", label)
            for label in host.split(".")
        )
    )


@dataclass(frozen=True)
class OpticalConfig:
    """Planetary Computer raster delivery and a fixed metric analysis grid."""

    endpoint: str = "https://planetarycomputer.microsoft.com/api/stac/v1/"
    collection: str = "sentinel-2-l2a"
    signing_endpoint: str = "https://planetarycomputer.microsoft.com/api/sas/v1/sign"
    allowed_asset_hosts: tuple[str, ...] = ("sentinel2l2a01.blob.core.windows.net",)
    target_crs: str = "EPSG:32640"
    target_resolution: float = 20.0
    timeout_seconds: float = 30.0

    def validate(self) -> None:
        from rasterio.crs import CRS

        for url in (self.endpoint, self.signing_endpoint):
            STACConfig(url, self.collection, self.timeout_seconds).validate()
            if urlsplit(url).scheme != "https" or not _is_hostname(urlsplit(url).hostname):
                raise ValueError("Optical service URLs must use HTTPS and valid DNS hostnames.")
        if not isinstance(self.allowed_asset_hosts, (tuple, list)) or not self.allowed_asset_hosts:
            raise ValueError("Optical allowed_asset_hosts must be a non-empty sequence.")
        for host in self.allowed_asset_hosts:
            if not _is_hostname(host):
                raise ValueError("Optical asset hosts must be exact lowercase hostnames.")
        if len(set(self.allowed_asset_hosts)) != len(self.allowed_asset_hosts):
            raise ValueError("Optical asset hosts must be unique.")
        if (
            isinstance(self.target_resolution, bool)
            or not isinstance(self.target_resolution, (int, float))
            or not isfinite(self.target_resolution)
            or self.target_resolution <= 0
        ):
            raise ValueError("Optical target_resolution must be finite and positive.")
        try:
            if not isinstance(self.target_crs, str) or not self.target_crs.startswith("EPSG:"):
                raise ValueError
            crs = CRS.from_string(self.target_crs)
            if not crs.is_projected or crs.linear_units != "metre":
                raise ValueError
        except (ValueError, TypeError) as exc:
            raise ValueError("Optical target_crs must be a projected metric EPSG CRS.") from exc


@dataclass(frozen=True)
class AquaSentinelConfig:
    app_name: str
    environment: str
    aoi_file: Path
    cache_dir: Path
    analysis: AnalysisConfig
    risk_bands: RiskBands
    hab_weights: RiskWeights
    oil_weights: RiskWeights
    catalog: STACConfig = field(default_factory=STACConfig)
    optical: OpticalConfig = field(default_factory=OpticalConfig)

    def validate(self) -> None:
        if not self.app_name.strip():
            raise ValueError("Application name cannot be empty.")

        self.analysis.validate()
        self.risk_bands.validate()
        self.hab_weights.validate()
        self.oil_weights.validate()
        self.catalog.validate()
        self.optical.validate()

        if not self.aoi_file.exists():
            raise FileNotFoundError(f"AOI file not found: {self.aoi_file}")
