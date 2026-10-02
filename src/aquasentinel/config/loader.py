from __future__ import annotations

import tomllib
from datetime import date
from pathlib import Path

from aquasentinel.config.models import (
    AnalysisConfig,
    AquaSentinelConfig,
    RiskBands,
    RiskWeights,
    STACConfig,
)


def load_config(
    config_path: str | Path = "config/default.toml",
    project_root: str | Path | None = None,
) -> AquaSentinelConfig:
    config_path = Path(config_path)

    if not config_path.exists():
        raise FileNotFoundError(f"Configuration file not found: {config_path}")

    with config_path.open("rb") as file:
        raw = tomllib.load(file)

    root = Path(project_root) if project_root is not None else Path.cwd()

    cloud_cover = raw["analysis"]["max_cloud_cover_percent"]
    if isinstance(cloud_cover, bool) or not isinstance(cloud_cover, (int, float)):
        raise TypeError(
            "max_cloud_cover_percent must be a real numeric value; booleans are not allowed."
        )

    analysis = AnalysisConfig(
        start_date=date.fromisoformat(raw["analysis"]["start_date"]),
        end_date=date.fromisoformat(raw["analysis"]["end_date"]),
        max_cloud_cover_percent=float(cloud_cover),
    )

    risk_bands = RiskBands(
        low_max=int(raw["risk"]["low_max"]),
        watch_max=int(raw["risk"]["watch_max"]),
        elevated_max=int(raw["risk"]["elevated_max"]),
        high_max=int(raw["risk"]["high_max"]),
    )

    config = AquaSentinelConfig(
        app_name=raw["app"]["name"],
        environment=raw["app"]["environment"],
        aoi_file=root / raw["data"]["aoi_file"],
        cache_dir=root / raw["data"]["cache_dir"],
        analysis=analysis,
        risk_bands=risk_bands,
        hab_weights=RiskWeights(
            values={
                key: float(value)
                for key, value in raw["risk"]["hab"]["weights"].items()
            }
        ),
        oil_weights=RiskWeights(
            values={
                key: float(value)
                for key, value in raw["risk"]["oil"]["weights"].items()
            }
        ),
        catalog=STACConfig(**raw.get("catalog", {})),
    )

    config.validate()
    return config
