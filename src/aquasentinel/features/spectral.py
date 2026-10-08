"""Deterministic signed-BOA band math, numerical support and stable identity only."""

from __future__ import annotations

import platform
from copy import deepcopy
from dataclasses import asdict
from datetime import UTC, datetime
from hashlib import sha256

import numpy as np

from aquasentinel.features.models import (
    FeatureDiagnostics,
    SpectralFeatureScene,
    feature_statistics,
)
from aquasentinel.preprocessing.cache import canonical_json
from aquasentinel.preprocessing.models import PreprocessedOpticalScene
from aquasentinel.provenance import DerivedProductRecord

FEATURE_ORDER = (
    "ndci_like",
    "mci_like",
    "red_edge_red_ratio",
    "red_edge2_red_ratio",
    "green_red_ratio",
    "green_blue_ratio",
)
CONSUMED_BANDS = ("B02", "B03", "B04", "B05", "B06")
PROCESSING_VERSION = "as103-v1"
ABSOLUTE_DENOMINATOR_EPSILON = 1e-4
RELATIVE_DENOMINATOR_EPSILON = 1e-6
NOMINAL_WAVELENGTHS_NM = {"B04": 665.0, "B05": 705.0, "B06": 740.0}
SUPPORT_POLICY = "AS-102 valid_water_mask only; finite required bands"
STATISTICS_POLICY = "finite float32 outputs; float64 linear percentiles [5,50,95]"
FORMULA_DEFINITIONS = {
    "ndci_like": {
        "formula": "(B05 - B04) / (B05 + B04)",
        "required_bands": ["B05", "B04"],
        "feature_family": "red_edge_b5_vs_red",
        "units": "dimensionless",
        "scientific_name": "NDCI-like candidate red-edge contrast",
    },
    "mci_like": {
        "formula": "B05 - (B04 + (B06 - B04) * ((705.0 - 665.0) / (740.0 - 665.0)))",
        "required_bands": ["B04", "B05", "B06"],
        "feature_family": "red_edge_line_height",
        "units": "dimensionless reflectance",
        "scientific_name": "MCI-like red-edge line height",
        "wavelengths": NOMINAL_WAVELENGTHS_NM,
        "wavelength_units": "nm",
        "nominal_wavelengths": True,
        "cloud_correction_factor": 1.0,
    },
    "red_edge_red_ratio": {
        "formula": "B05 / B04",
        "required_bands": ["B05", "B04"],
        "feature_family": "red_edge_b5_vs_red",
        "units": "dimensionless",
    },
    "red_edge2_red_ratio": {
        "formula": "B06 / B04",
        "required_bands": ["B06", "B04"],
        "feature_family": "red_edge_b6_vs_red",
        "units": "dimensionless",
    },
    "green_red_ratio": {
        "formula": "B03 / B04",
        "required_bands": ["B03", "B04"],
        "feature_family": "visible_green_vs_red",
        "units": "dimensionless",
    },
    "green_blue_ratio": {
        "formula": "B03 / B02",
        "required_bands": ["B03", "B02"],
        "feature_family": "visible_green_vs_blue",
        "units": "dimensionless",
    },
}


def input_content_fingerprint(bands: dict[str, np.ndarray], mask: np.ndarray) -> str:
    """Length-delimited C-order mask and consumed finite little-endian float32 values."""
    digest = sha256()

    def segment(header: dict, data: bytes) -> None:
        encoded = canonical_json({**header, "byte_count": len(data)})
        digest.update(len(encoded).to_bytes(8, "big"))
        digest.update(encoded)
        digest.update(data)

    segment(
        {
            "format": "as103-input-v1",
            "shape": list(mask.shape),
            "band_order": list(CONSUMED_BANDS),
            "mask_dtype": "uint8",
            "order": "C",
        },
        np.asarray(mask, dtype=np.uint8).tobytes(order="C"),
    )
    for name in CONSUMED_BANDS:
        selected = np.asarray(bands[name][mask], dtype="<f4")
        if not np.isfinite(selected).all():
            raise ValueError("Consumed valid-water reflectance must be finite.")
        segment(
            {"band": name, "count": int(selected.size), "dtype": "<f4"}, selected.tobytes(order="C")
        )
    return digest.hexdigest()


def feature_product_id(identity: dict) -> str:
    return "spectral:" + sha256(canonical_json(identity)).hexdigest()


def numerical_policy() -> dict:
    return {
        "absolute_denominator_epsilon": ABSOLUTE_DENOMINATOR_EPSILON,
        "relative_denominator_epsilon": RELATIVE_DENOMINATOR_EPSILON,
        "reject": "abs(d) <= max(abs_epsilon, rel_epsilon * (abs(a) + abs(b)))",
        "finite_float64_and_float32_required": True,
        "clip": False,
    }


def _division_support(a: np.ndarray, b: np.ndarray, denominator: np.ndarray) -> np.ndarray:
    threshold = np.maximum(
        ABSOLUTE_DENOMINATOR_EPSILON,
        RELATIVE_DENOMINATOR_EPSILON * (np.abs(a) + np.abs(b)),
    )
    return np.isfinite(a) & np.isfinite(b) & (np.abs(denominator) > threshold)


def _float32_result(values: np.ndarray, support: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Reject nonfinite intermediates and float32 overflow; no clipping or replacement."""
    with np.errstate(over="ignore", invalid="ignore"):
        output = values.astype(np.float32)
    valid = support & np.isfinite(values) & np.isfinite(output)
    output[~valid] = np.nan
    return output, valid


def extract_spectral_features(scene: PreprocessedOpticalScene) -> SpectralFeatureScene:
    """Pure per-scene extraction; no retrieval, resampling, cache writes or event logic."""
    scene.validate()
    parent = scene.provenance
    if (
        parent.product_type != "preprocessed_optical_scene"
        or parent.product_id != "optical:" + scene.cache_id
        or parent.parameters != scene.processing_parameters
        or parent.processing_version
        != scene.processing_parameters["identity"]["processing_version"]
    ):
        raise ValueError("Input must carry consistent AS-102 derived provenance.")
    mask = scene.valid_water_mask.copy()
    bands = {name: scene.reflectance[name].copy() for name in CONSUMED_BANDS}
    fingerprint = input_content_fingerprint(bands, mask)
    # Operate only on eligible pixels; excluded values cannot influence results or diagnostics.
    water = {name: band[mask].astype(np.float64) for name, band in bands.items()}
    parent_count = int(np.count_nonzero(mask))
    identity = {
        "processing_version": PROCESSING_VERSION,
        "parent_product_id": parent.product_id,
        "parent_processing_version": parent.processing_version,
        "input_content_fingerprint": fingerprint,
        "grid": scene.grid.to_dict(),
        "acquired_at": scene.acquired_at.astimezone(UTC).isoformat(),
        "feature_order": list(FEATURE_ORDER),
        "formulas": deepcopy(FORMULA_DEFINITIONS),
        "numerical_policy": numerical_policy(),
        "input_support_policy": SUPPORT_POLICY,
        "arithmetic_dtype": "float64",
        "output_dtype": "float32",
        "statistics_policy": STATISTICS_POLICY,
        "parent_water_mask_digest": sha256(mask.astype(np.uint8).tobytes(order="C")).hexdigest(),
        "software_versions": {"python": platform.python_version(), "numpy": np.__version__},
    }
    features, masks, statistics, diagnostics = {}, {}, {}, {}
    for name in FEATURE_ORDER:
        required = FORMULA_DEFINITIONS[name]["required_bands"]
        negative_inputs = np.logical_or.reduce([water[b] < 0 for b in required])
        support = np.ones(parent_count, dtype=bool)
        denominator_rejections = negative_denominators = 0
        with np.errstate(over="ignore", invalid="ignore", divide="ignore"):
            if name == "mci_like":
                wavelength = NOMINAL_WAVELENGTHS_NM
                coefficient = (wavelength["B05"] - wavelength["B04"]) / (
                    wavelength["B06"] - wavelength["B04"]
                )
                result = water["B05"] - (water["B04"] + (water["B06"] - water["B04"]) * coefficient)
            else:
                a, b = (water[band] for band in required)
                denominator = a + b if name == "ndci_like" else b
                numerator = a - b if name == "ndci_like" else a
                support = _division_support(a, b, denominator)
                denominator_rejections = int(np.count_nonzero(~support))
                # Count signed denominators over all parent water, including rejected ones.
                negative_denominators = int(np.count_nonzero(denominator < 0))
                result = np.full(parent_count, np.nan, dtype=np.float64)
                np.divide(numerator, denominator, out=result, where=support)
        output, valid = _float32_result(result, support)
        array = np.full(scene.grid.shape, np.nan, dtype=np.float32)
        feature_mask = np.zeros(scene.grid.shape, dtype=bool)
        array[mask], feature_mask[mask] = output, valid
        features[name], masks[name] = array, feature_mask
        statistics[name] = feature_statistics(array, feature_mask, parent_count)
        diagnostics[name] = FeatureDiagnostics(
            parent_count,
            int(np.count_nonzero(negative_inputs)),
            denominator_rejections,
            negative_denominators,
            int(np.count_nonzero(support & ~valid)),
            int(np.count_nonzero(valid & ((output < -1) | (output > 1))))
            if name == "ndci_like"
            else None,
        )
    parameters = {
        "identity": identity,
        "statistics": {k: asdict(v) for k, v in statistics.items()},
        "diagnostics": {k: asdict(v) for k, v in diagnostics.items()},
        "scientific_limit": "Candidate signed-BOA signals only; not aquatic Rrs or HAB evidence.",
    }
    product_id = feature_product_id(identity)
    provenance = DerivedProductRecord(
        product_id,
        "spectral_feature_scene",
        datetime.now(UTC),
        PROCESSING_VERSION,
        (parent.product_id,),
        parameters,
    )
    result_scene = SpectralFeatureScene(
        scene.grid,
        parent.product_id,
        scene.acquired_at,
        FEATURE_ORDER,
        features,
        masks,
        mask,
        statistics,
        diagnostics,
        parameters,
        product_id,
        provenance,
    )
    result_scene.validate()
    return result_scene
