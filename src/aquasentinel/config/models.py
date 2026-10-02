from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from pathlib import Path


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

    def validate(self) -> None:
        if not self.app_name.strip():
            raise ValueError("Application name cannot be empty.")

        self.analysis.validate()
        self.risk_bands.validate()
        self.hab_weights.validate()
        self.oil_weights.validate()

        if not self.aoi_file.exists():
            raise FileNotFoundError(f"AOI file not found: {self.aoi_file}")