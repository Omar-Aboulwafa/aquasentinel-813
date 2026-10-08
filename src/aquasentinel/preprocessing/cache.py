"""Atomic AOI-only cache with stable keys, file checksums and offline known-ID reload."""

from __future__ import annotations

import json
import os
import re
import shutil
import tempfile
from dataclasses import asdict
from hashlib import sha256
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit
from zipfile import BadZipFile

import numpy as np

from aquasentinel.ingestion.sentinel2 import AssetReference
from aquasentinel.ingestion.sentinel2_assets import (
    BANDS,
    ObservationIdentity,
    ResolvedOpticalSource,
)
from aquasentinel.preprocessing.models import (
    AnalysisGrid,
    PreprocessedOpticalScene,
    SceneStatistics,
)
from aquasentinel.provenance.serialization import (
    derived_product_from_dict,
    derived_product_to_dict,
    source_record_from_dict,
    source_record_to_dict,
)

MASK_NAMES = (
    "aoi_mask",
    "valid_data_mask",
    "water_mask",
    "valid_water_mask",
    "interpolation_support_mask",
)


class CacheCorruptionError(ValueError):
    """Cached evidence failed checksum, identity, schema or grid validation."""


def _stable(value: Any) -> None:
    if isinstance(value, dict):
        for item in value.values():
            _stable(item)
    elif isinstance(value, (list, tuple)):
        for item in value:
            _stable(item)
    elif isinstance(value, str) and value.lower().startswith(("https://", "http://")):
        parsed = urlsplit(value)
        if parsed.query or parsed.fragment or parsed.username is not None:
            raise ValueError("Signed/credentialled URL cannot enter stable processing metadata.")


def canonical_json(payload: Any) -> bytes:
    _stable(payload)
    return (
        json.dumps(payload, sort_keys=True, separators=(",", ":"), allow_nan=False) + "\n"
    ).encode()


def cache_identity(parameters: dict[str, Any]) -> str:
    return sha256(canonical_json(parameters)).hexdigest()


def _cache_path(root: str | Path, cache_id: str) -> Path:
    if not isinstance(cache_id, str) or not re.fullmatch(r"[a-f0-9]{64}", cache_id):
        raise ValueError("Cache ID must be a SHA-256 digest.")
    return Path(root) / "as102" / cache_id


def _resolved_dict(resolved: ResolvedOpticalSource) -> dict[str, Any]:
    return {
        "source": source_record_to_dict(resolved.source),
        "discovery_source": source_record_to_dict(resolved.discovery_source),
        "identity": resolved.identity.to_dict(),
        "processing_baseline": resolved.processing_baseline,
        "generation_time": resolved.generation_time,
        "discovery_processing": resolved.discovery_processing,
        "assets": [asdict(a) for a in resolved.assets],
        "provider_metadata": resolved.provider_metadata,
        "native_grids": resolved.native_grids,
        "decoding_metadata": resolved.decoding_metadata,
    }


def _resolved_from_dict(payload: dict[str, Any]) -> ResolvedOpticalSource:
    from datetime import datetime

    identity = payload["identity"]
    return ResolvedOpticalSource(
        source_record_from_dict(payload["source"]),
        source_record_from_dict(payload["discovery_source"]),
        ObservationIdentity(
            datetime.fromisoformat(identity["acquired_at"]),
            identity["platform"],
            identity["mgrs_tile"],
            identity["relative_orbit"],
        ),
        payload["processing_baseline"],
        payload["generation_time"],
        payload["discovery_processing"],
        tuple(
            AssetReference(a["key"], a["href"], a["media_type"], tuple(a["roles"]))
            for a in payload["assets"]
        ),
        payload["provider_metadata"],
        payload["native_grids"],
        payload["decoding_metadata"],
    )


def write_cache(scene: PreprocessedOpticalScene, root: str | Path) -> Path:
    scene.validate()
    destination = _cache_path(root, scene.cache_id)
    destination.parent.mkdir(parents=True, exist_ok=True)
    if destination.exists():
        load_cache(root, scene.cache_id)
        return destination
    temporary = Path(tempfile.mkdtemp(prefix=".as102-", dir=destination.parent))
    try:
        arrays = {
            **scene.reflectance,
            "scl": scene.scl,
            **{key: getattr(scene, key) for key in MASK_NAMES},
        }
        np.savez_compressed(temporary / "arrays.npz", **arrays)
        checksum = sha256((temporary / "arrays.npz").read_bytes()).hexdigest()
        manifest = {
            "schema": "as102-cache-v1",
            "cache_id": scene.cache_id,
            "grid": scene.grid.to_dict(),
            "resolved_source": _resolved_dict(scene.resolved_source),
            "statistics": asdict(scene.statistics),
            "processing_parameters": scene.processing_parameters,
            "provenance": derived_product_to_dict(scene.provenance),
            "files": {"arrays.npz": checksum},
        }
        (temporary / "manifest.json").write_bytes(canonical_json(manifest))
        os.rename(temporary, destination)
    except Exception:
        shutil.rmtree(temporary, ignore_errors=True)
        raise
    return destination


def load_cache(root: str | Path, cache_id: str) -> PreprocessedOpticalScene:
    """No imports/calls to STAC, signing or raster transport are needed here."""
    destination = _cache_path(root, cache_id)
    try:
        manifest = json.loads((destination / "manifest.json").read_bytes())
        canonical_json(manifest)  # Reject signed/credentialled URLs even in a tampered manifest.
        if manifest["schema"] != "as102-cache-v1" or manifest["cache_id"] != cache_id:
            raise ValueError
        if manifest["files"].keys() != {"arrays.npz"}:
            raise ValueError
        data_file = destination / "arrays.npz"
        if sha256(data_file.read_bytes()).hexdigest() != manifest["files"]["arrays.npz"]:
            raise ValueError
        parameters = manifest["processing_parameters"]
        if cache_identity(parameters["identity"]) != cache_id:
            raise ValueError
        if canonical_json(manifest["grid"]) != canonical_json(
            parameters["identity"]["target_grid"]
        ):
            raise ValueError
        grid = AnalysisGrid.from_dict(manifest["grid"])
        if not 0 < grid.width * grid.height <= 10_000_000:
            raise ValueError
        with np.load(data_file, allow_pickle=False) as archive:
            if set(archive.files) != {*BANDS, "scl", *MASK_NAMES}:
                raise ValueError
            reflectance = {band: archive[band].copy() for band in BANDS}
            masks = {name: archive[name].copy() for name in MASK_NAMES}
            scl = archive["scl"].copy()
        scene = PreprocessedOpticalScene(
            _resolved_from_dict(manifest["resolved_source"]),
            grid,
            reflectance,
            scl,
            **masks,
            statistics=SceneStatistics(**manifest["statistics"]),
            processing_parameters=parameters,
            cache_id=cache_id,
            provenance=derived_product_from_dict(manifest["provenance"]),
        )
        scene.validate()
        from aquasentinel.preprocessing.masks import scene_statistics

        if scene.statistics != scene_statistics(
            scene.aoi_mask, scene.valid_data_mask, scene.water_mask, scene.valid_water_mask
        ):
            raise ValueError
        identity = parameters["identity"]
        resolved = scene.resolved_source
        consistency_pairs = (
            (source_record_to_dict(resolved.source), identity["pc_source"]),
            (source_record_to_dict(resolved.discovery_source), identity["discovery_source"]),
            (resolved.identity.to_dict(), identity["observation_match"]),
            (resolved.processing_baseline, identity["pc_processing_baseline"]),
            (resolved.generation_time, identity["pc_generation_time"]),
            (resolved.discovery_processing, identity["discovery_processing"]),
            (resolved.provider_metadata, identity["pc_provider_metadata"]),
            ([asdict(asset) for asset in resolved.assets], identity["assets"]),
            (resolved.decoding_metadata, identity["decoding"]),
            (resolved.native_grids, parameters["source_grids"]),
        )
        if any(canonical_json(actual) != canonical_json(expected)
               for actual, expected in consistency_pairs):
            raise ValueError
        provenance = scene.provenance
        if (
            provenance.product_id != f"optical:{cache_id}"
            or provenance.product_type != "preprocessed_optical_scene"
            or provenance.processing_version != identity["processing_version"]
            or provenance.source_ids != (resolved.source.source_id,)
            or provenance.parameters != parameters
        ):
            raise ValueError
        return scene
    except (OSError, ValueError, TypeError, KeyError, AttributeError, EOFError, BadZipFile):
        raise CacheCorruptionError(
            "AS-102 cache failed checksum, identity or grid validation."
        ) from None
