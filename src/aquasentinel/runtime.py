from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from aquasentinel.config import (
    AOICollection,
    AOIFeature,
    AquaSentinelConfig,
    load_aoi,
    load_config,
)


@dataclass(frozen=True)
class RuntimeContext:
    config: AquaSentinelConfig
    aoi: AOICollection

    @property
    def validation_aois(self) -> tuple[AOIFeature, ...]:
        return self.aoi.get_by_role("validation_aoi")

    @property
    def primary_validation_aoi(self) -> AOIFeature:
        validation_aois = self.validation_aois

        if not validation_aois:
            raise ValueError("Runtime context contains no validation AOI.")

        return validation_aois[0]


def build_runtime_context(
    config_path: str | Path = "config/default.toml",
    project_root: str | Path | None = None,
) -> RuntimeContext:
    root = (
        Path(project_root).resolve()
        if project_root is not None
        else Path.cwd().resolve()
    )

    config = load_config(
        config_path=config_path,
        project_root=root,
    )

    aoi = load_aoi(config.aoi_file)

    return RuntimeContext(
        config=config,
        aoi=aoi,
    )