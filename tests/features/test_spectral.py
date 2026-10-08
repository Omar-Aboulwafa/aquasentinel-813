from copy import deepcopy

import numpy as np
import pytest

from aquasentinel.features import FEATURE_ORDER, extract_spectral_features
from aquasentinel.features.spectral import (
    ABSOLUTE_DENOMINATOR_EPSILON,
    NOMINAL_WAVELENGTHS_NM,
    RELATIVE_DENOMINATOR_EPSILON,
    _division_support,
    _float32_result,
)
from aquasentinel.preprocessing.cache import canonical_json


def test_independent_six_formula_results(parent):
    result = extract_spectral_features(parent)
    # Independent scalar arithmetic uses the actual float32 input values.
    blue, green, red, edge, edge2 = (
        float(parent.reflectance[b][0, 0]) for b in ("B02", "B03", "B04", "B05", "B06")
    )
    expected = [
        (edge - red) / (edge + red),
        edge - red - (edge2 - red) * 8 / 15,
        edge / red,
        edge2 / red,
        green / red,
        green / blue,
    ]
    assert result.feature_order == FEATURE_ORDER
    for name, value in zip(FEATURE_ORDER, expected, strict=True):
        assert result.features[name].dtype == np.float32
        np.testing.assert_allclose(result.features[name], value, rtol=1e-6)
        assert result.feature_valid_masks[name].all()
    mci = result.processing_parameters["identity"]["formulas"]["mci_like"]
    assert (
        mci["wavelengths"] == NOMINAL_WAVELENGTHS_NM == {"B04": 665.0, "B05": 705.0, "B06": 740.0}
    )
    assert mci["nominal_wavelengths"] is True
    assert mci["wavelength_units"] == "nm" and mci["cloud_correction_factor"] == 1.0
    assert mci["scientific_name"] == "MCI-like red-edge line height"
    families = result.processing_parameters["identity"]["formulas"]
    assert (
        families["ndci_like"]["feature_family"] == families["red_edge_red_ratio"]["feature_family"]
    )


@pytest.mark.parametrize("edge,expected", [(0.04, 0), (0.08, 0.04), (0.0, -0.04)])
def test_flat_positive_negative_mci(make_optical, edge, expected):
    result = extract_spectral_features(make_optical(values={"B04": 0.04, "B05": edge, "B06": 0.04}))
    np.testing.assert_allclose(result.features["mci_like"], expected, atol=1e-8)


def test_linear_continuum_mci(make_optical):
    result = extract_spectral_features(make_optical(values={"B04": 0, "B05": 8, "B06": 15}))
    np.testing.assert_array_equal(result.features["mci_like"], 0)


@pytest.mark.parametrize(
    "d", [0.0, -0.0, 1e-8, -1e-8, 1e-4, -1e-4, np.nextafter(1e-4, 0), -np.nextafter(1e-4, 0)]
)
def test_exact_absolute_boundary_rejected_in_float64_guard(d):
    # Guard receives float64 arithmetic; 1e-4 itself is not exactly representable in parent float32.
    assert not _division_support(np.array([0.01]), np.array([d]), np.array([d]))[0]


@pytest.mark.parametrize("sign", [-1, 1])
def test_just_above_absolute_boundary_accepted(sign):
    d = sign * np.nextafter(ABSOLUTE_DENOMINATOR_EPSILON, np.inf)
    assert _division_support(np.array([0.01]), np.array([d]), np.array([d]))[0]


@pytest.mark.parametrize("factor,expected", [(0.999, False), (1.0, False), (1.001, True)])
def test_relative_boundary_cancellation(factor, expected):
    a, b = np.array([100.0]), np.array([-100.0])
    assert (
        bool(_division_support(a, b, np.array([RELATIVE_DENOMINATOR_EPSILON * 200 * factor]))[0])
        is expected
    )


@pytest.mark.parametrize("red", [0.0, -0.0, 1e-8, -1e-8, 1e-4, -1e-4])
def test_pipeline_small_red_denominator(make_optical, red):
    result = extract_spectral_features(make_optical(values={"B04": red}))
    for name in ("red_edge_red_ratio", "red_edge2_red_ratio", "green_red_ratio"):
        assert not result.feature_valid_masks[name].any()
        assert np.isnan(result.features[name]).all()
        assert result.diagnostics[name].denominator_rejection_count == 12
        assert result.statistics[name].minimum is None
        assert result.statistics[name].valid_fraction_of_parent_water == 0


def test_ndci_cancellation(make_optical):
    result = extract_spectral_features(make_optical(values={"B04": 0.02, "B05": -0.02}))
    assert not result.feature_valid_masks["ndci_like"].any()
    assert result.diagnostics["ndci_like"].denominator_rejection_count == 12
    assert result.feature_valid_masks["mci_like"].all()


def test_signed_inputs_negative_denominators_and_unclipped_ndci(make_optical):
    result = extract_spectral_features(
        make_optical(values={"B04": -0.02, "B05": 0.04, "B02": -0.08})
    )
    np.testing.assert_allclose(result.features["ndci_like"], 3.0)
    np.testing.assert_allclose(result.features["red_edge_red_ratio"], -2.0)
    np.testing.assert_allclose(result.features["green_blue_ratio"], -0.75)
    assert result.diagnostics["ndci_like"].out_of_nominal_range_count == 12
    assert result.diagnostics["red_edge_red_ratio"].negative_required_input_count == 12
    assert result.diagnostics["red_edge_red_ratio"].negative_denominator_count == 12
    assert result.diagnostics["green_blue_ratio"].negative_denominator_count == 12
    assert result.diagnostics["mci_like"].denominator_rejection_count == 0
    assert result.diagnostics["mci_like"].out_of_nominal_range_count is None


def test_nonfinite_result_or_float32_overflow_rejected():
    values = np.array([np.nan, np.inf, -np.inf, float(np.finfo(np.float32).max) * 2.0, 0.0])
    result, mask = _float32_result(values, np.ones(5, bool))
    np.testing.assert_array_equal(mask, [False, False, False, False, True])
    assert np.isnan(result[:4]).all() and result[4] == 0


def test_mci_overflow_rejected_without_clipping(make_optical):
    maximum = np.finfo(np.float32).max
    result = extract_spectral_features(
        make_optical(values={"B04": -maximum, "B05": maximum, "B06": -maximum})
    )
    assert not result.feature_valid_masks["mci_like"].any()
    assert result.diagnostics["mci_like"].nonfinite_result_rejection_count == 12


@pytest.mark.parametrize("value", [np.nan, np.inf, -np.inf])
def test_nonfinite_parent_water_is_invalid(make_optical, value):
    parent = make_optical()
    parent.reflectance["B04"][0, 0] = value
    with pytest.raises(ValueError, match="finite"):
        extract_spectral_features(parent)


def test_only_parent_water_used_and_input_unchanged(make_optical):
    mask = np.array([[True, False, True], [False, True, False]])
    parent = make_optical(mask=mask)
    for band in parent.reflectance.values():
        band[~mask] = np.inf  # Even nonfinite excluded input is irrelevant to features.
    arrays = {k: v.copy() for k, v in parent.reflectance.items()}
    masks = {
        k: getattr(parent, k).copy()
        for k in (
            "aoi_mask",
            "valid_data_mask",
            "water_mask",
            "valid_water_mask",
            "interpolation_support_mask",
        )
    }
    provenance, grid = deepcopy(parent.provenance), deepcopy(parent.grid)
    result = extract_spectral_features(parent)
    np.testing.assert_array_equal(result.valid_water_mask, mask)
    assert not np.shares_memory(result.valid_water_mask, parent.valid_water_mask)
    for name in FEATURE_ORDER:
        np.testing.assert_array_equal(result.feature_valid_masks[name], mask)
        assert np.isnan(result.features[name][~mask]).all()
        assert result.statistics[name].valid_count == 3
    for band, old in arrays.items():
        np.testing.assert_array_equal(parent.reflectance[band], old)
    for name, old in masks.items():
        np.testing.assert_array_equal(getattr(parent, name), old)
    assert parent.grid == grid and parent.provenance == provenance


def test_zero_parent_water_and_json_safe_empty_summaries(make_optical):
    result = extract_spectral_features(make_optical(mask=np.zeros((2, 6), bool)))
    for name in FEATURE_ORDER:
        assert np.isnan(result.features[name]).all()
        assert result.statistics[name].valid_count == 0
        assert result.statistics[name].valid_fraction_of_parent_water is None
        assert result.statistics[name].p05 is None
        assert result.diagnostics[name].parent_valid_water_count == 0
    assert b"NaN" not in canonical_json(result.processing_parameters)


def test_mixed_diagnostic_populations_and_summary_quantiles(make_optical):
    # Negative denominators include rejected negative near-zero values; populations
    # are parent-water pixels, not just final feature support.
    parent = make_optical(
        values={"B04": [[-0.02, -1e-8, 0.02, 0, 0.02, 0.02], [0.02, 0.02, 0.02, 0.02, 0.02, 0.02]]}
    )
    result = extract_spectral_features(parent)
    diagnostics = result.diagnostics["red_edge_red_ratio"]
    assert diagnostics.negative_required_input_count == 2
    assert diagnostics.negative_denominator_count == 2
    assert diagnostics.denominator_rejection_count == 2
    assert diagnostics.nonfinite_result_rejection_count == 0
    statistics = result.statistics["red_edge_red_ratio"]
    assert statistics.valid_count == 10
    assert statistics.valid_fraction_of_parent_water == 10 / 12
    assert statistics.minimum == pytest.approx(-2.5)
    assert statistics.maximum == pytest.approx(2.5)
    assert statistics.p05 == pytest.approx(-0.25)
    assert statistics.median == statistics.p95 == pytest.approx(2.5)
