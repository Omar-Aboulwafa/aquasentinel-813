from copy import deepcopy
from dataclasses import replace

import numpy as np
import pytest

from aquasentinel.features import extract_spectral_features


@pytest.mark.parametrize(
    "corruption",
    [
        "order",
        "missing",
        "extra",
        "shape",
        "dtype",
        "mask_dtype",
        "mask_shape",
        "expanded",
        "invalid_finite",
        "valid_nan",
        "parent",
        "source_shortcut",
        "naive_time",
        "grid_identity",
        "id",
        "statistics",
        "diagnostics",
        "provenance_type",
        "provenance_version",
        "metadata_nan",
    ],
)
def test_typed_model_rejects_inconsistent_output(make_optical, corruption):
    mask = np.ones((2, 6), bool)
    mask[0, 0] = False
    result = deepcopy(extract_spectral_features(make_optical(mask=mask)))
    name = "ndci_like"
    if corruption == "order":
        result = replace(result, feature_order=tuple(reversed(result.feature_order)))
    elif corruption == "missing":
        del result.features[name]
    elif corruption == "extra":
        result.features["unexpected"] = result.features[name]
    elif corruption == "shape":
        result.features[name] = result.features[name][:1]
    elif corruption == "dtype":
        result.features[name] = result.features[name].astype(np.float64)
    elif corruption == "mask_dtype":
        result.feature_valid_masks[name] = result.feature_valid_masks[name].astype(np.uint8)
    elif corruption == "mask_shape":
        result.feature_valid_masks[name] = result.feature_valid_masks[name][:1]
    elif corruption == "expanded":
        result.feature_valid_masks[name][0, 0] = True
    elif corruption == "invalid_finite":
        result.features[name][0, 0] = 0
    elif corruption == "valid_nan":
        result.features[name][0, 1] = np.nan
    elif corruption == "parent":
        result = replace(result, parent_product_id="optical:wrong")
    elif corruption == "source_shortcut":
        result = replace(result, provenance=replace(result.provenance, source_ids=("pc-source",)))
    elif corruption == "naive_time":
        result = replace(result, acquired_at=result.acquired_at.replace(tzinfo=None))
    elif corruption == "grid_identity":
        result.processing_parameters["identity"]["grid"]["width"] += 1
    elif corruption == "id":
        result = replace(result, product_id="spectral:wrong")
    elif corruption == "statistics":
        result.statistics[name] = replace(result.statistics[name], minimum=999.0)
    elif corruption == "diagnostics":
        result.diagnostics[name] = replace(result.diagnostics[name], denominator_rejection_count=1)
    elif corruption == "provenance_type":
        result = replace(result, provenance=replace(result.provenance, product_type="hab_risk"))
    elif corruption == "provenance_version":
        result = replace(result, provenance=replace(result.provenance, processing_version="wrong"))
    elif corruption == "metadata_nan":
        result.processing_parameters["bad"] = float("nan")
    with pytest.raises(ValueError):
        result.validate()


def test_parent_metadata_contract_checked_before_extraction(parent):
    for change in (
        {"product_type": "unknown"},
        {"product_id": "pc-source"},
        {"processing_version": "wrong"},
    ):
        altered = replace(parent, provenance=replace(parent.provenance, **change))
        with pytest.raises(ValueError, match="AS-102"):
            extract_spectral_features(altered)


@pytest.mark.parametrize(
    "field,value",
    [
        ("formulas", {}),
        ("numerical_policy", {}),
        ("input_support_policy", "relaxed"),
        ("arithmetic_dtype", "float32"),
        ("output_dtype", "float64"),
        ("input_content_fingerprint", "not-a-digest"),
        ("parent_water_mask_digest", "a" * 64),
    ],
)
def test_rehashed_identity_cannot_bypass_frozen_model_contract(parent, field, value):
    from aquasentinel.features.spectral import feature_product_id

    result = deepcopy(extract_spectral_features(parent))
    result.processing_parameters["identity"][field] = value
    product_id = feature_product_id(result.processing_parameters["identity"])
    altered = replace(
        result, product_id=product_id, provenance=replace(result.provenance, product_id=product_id)
    )
    with pytest.raises(ValueError, match="identity"):
        altered.validate()
