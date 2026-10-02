from aquasentinel.runtime import build_runtime_context


def test_build_runtime_context() -> None:
    context = build_runtime_context()

    assert context.config.app_name == "AquaSentinel 813"
    assert context.aoi.name == "aquasentinel_demo_site"
    assert context.primary_validation_aoi.feature_id == "raha_validation_aoi"
    assert context.primary_validation_aoi.geometry_type == "Polygon"


def test_runtime_risk_weights_are_normalized() -> None:
    context = build_runtime_context()

    assert sum(context.config.hab_weights.values.values()) == 1.0
    assert sum(context.config.oil_weights.values.values()) == 1.0