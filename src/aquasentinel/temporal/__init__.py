"""Causal candidate-feature comparisons; no event interpretation or IO."""

from aquasentinel.temporal.baseline import compute_temporal_anomaly
from aquasentinel.temporal.models import TemporalFeatureResult, TemporalFeatureScene

__all__ = ["TemporalFeatureResult", "TemporalFeatureScene", "compute_temporal_anomaly"]
