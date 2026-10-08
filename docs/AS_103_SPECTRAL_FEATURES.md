# AS-103 — Spectral Feature Extraction

## Task

Implementation explicitly authorized on 8 October 2026 (Asia/Dubai), on
`feature/as-103-spectral-features` from main
`642a469414f096b4ac7cd96de895aa38f7da42ec`. Leave work uncommitted for review.

## Goal

Transform one validated AS-102 scene into deterministic candidate spectral
features, per-feature support/diagnostics, and immediate-parent provenance.

## Inputs

`PreprocessedOpticalScene`: verified float32 BOA bands, fixed AnalysisGrid,
authoritative valid-water mask and AS-102 derived provenance. No credentials.

## Outputs

Typed `SpectralFeatureScene`; six canonical float32 arrays and boolean masks;
JSON-safe typed statistics/diagnostics; input content fingerprint and deterministic
product ID; `DerivedProductRecord` referencing only the AS-102 derived product.

## Files Likely to Change

Add `src/aquasentinel/features/{__init__,models,spectral}.py`, focused
`tests/features/`, this execution plan/API contract and
`docs/evidence/AS_103_SPECTRAL_FEATURES_VALIDATION.md`. Update Decisions,
Project State, Handoff, Presentation Journal and Presentation Evidence Index.
Do not alter AS-102, generic provenance, configuration or dependencies.

## Dependencies

No new dependencies. Existing NumPy supplies arithmetic and masks; the standard
library supplies dataclasses, canonical JSON and SHA-256. Existing grid/provenance
types and stable JSON guard are reused without invoking cache or raster access.

## Acceptance Criteria

- Exact six-feature order/formulas/families; nominal MCI 665/705/740 nm, k=1.0.
- Validate parent; preserve its mask; no feature mask expands parent water.
- Float64 arithmetic, float32 output; unstable division or nonfinite results
  become masked NaN. Preserve signed reflectance and unclipped outputs.
- Fixed absolute/relative epsilons 1e-4/1e-6, inclusive rejection boundary.
- Typed statistics and diagnostics; empty values use None in JSON.
- Canonical input fingerprint of full mask and five consumed band values under
  water; deterministic identity excluding creation time and statistics.
- Exact PC source → AS-102 derived → AS-103 derived registry lineage.
- Offline tests, one verified cached real-scene acceptance and manual pixel
  checks; no retrieval, signing, raster reads, writes or AS-103 disk cache.
- Existing 265-test baseline retained; pytest, Ruff and diff checks pass.

## Scientific Guardrails

BOA is not aquatic Rrs. ndci_like is not calibrated chlorophyll; mci_like is a
Sentinel-2 red-edge line-height analogue, not the official SNAP product. These
signals establish no event, HAB, species, toxin, water safety, shutdown, risk or
lead time. No bloom threshold; no clipping. Correlated B05/red features are not
independent biological evidence. Coastal adjacency, shallow bottom, sediment,
glint, atmospheric-correction residuals and SCL errors remain limitations.

## Risks

Signed BOA cancellation, numerically small denominators, mutable parent arrays,
tuple/list JSON representation differences, false lineage shortcuts and misuse
of feature diagnostics as biological evidence. Define finite/canonical model
invariants, input snapshots/fingerprints and exact parent references.

## Validation

Offline formula/numerical/support/model/immutability/identity/lineage/no-I/O tests.
Then use verified AS-102 cache
`0725a908d21cd655e83f70d2bb11247dc0f1516f0c00ea275efc3239113ee4a6`,
310×228 EPSG:32640 and 7,963 water pixels; timestamp the actual experiment,
record six feature summaries/diagnostics, independent pixel checks, repeated
equivalence, fingerprint and exact lineage. Block access/write entry points
during extraction. Run `python -m pytest -v`, `python -m ruff check .`,
`git diff --check`; inspect all new files and scope before reporting.

## Non-Goals

AS-104, temporal baselines/anomalies, persistence, HAB classification,
chlorophyll calibration, ML, exposure/risk, remote access, resampling,
new dependencies/configuration, AS-103 disk cache, commits/pushes/PRs.

## Execution Status

Plan written before implementation. Implementation, 83 new offline cases and one cached real-scene acceptance are complete for feature-branch review. Full suite: 348 passed, Ruff/diff checks passed; six existing Rasterio warnings. Changes are uncommitted/unpushed/unmerged; no PR. AS-104 NOT authorized and NOT started.


## Final API and Formula Contract

`aquasentinel.features.extract_spectral_features(scene)` accepts only a validated
AS-102 `PreprocessedOpticalScene` with consistent `preprocessed_optical_scene`
provenance. It copies the full parent mask and five consumed band arrays before
fingerprinting/arithmetic, returns a validated `SpectralFeatureScene`, and makes
no external-access or disk-write calls. The grid is unchanged. No AS-103 cache.

| Canonical feature | Formula | Feature family |
|---|---|---|
| ndci_like | (B05 − B04) / (B05 + B04) | red_edge_b5_vs_red |
| mci_like | B05 − [B04 + (B06 − B04) × (705−665)/(740−665)] | red_edge_line_height |
| red_edge_red_ratio | B05 / B04 | red_edge_b5_vs_red |
| red_edge2_red_ratio | B06 / B04 | red_edge_b6_vs_red |
| green_red_ratio | B03 / B04 | visible_green_vs_red |
| green_blue_ratio | B03 / B02 | visible_green_vs_blue |

MCI nominal B04/B05/B06 wavelengths are 665/705/740 nm, coefficient 8/15;
`nominal_wavelengths=true`, `cloud_correction_factor=1.0`, scientific name
“MCI-like red-edge line height”. These are a declared convention, not fields
retrieved from product XML. SNAP's 1.005 thin-cloud correction is not implemented.
All ratios are dimensionless; line height is in dimensionless reflectance units.

## Numerical and Diagnostic Contract

Only original AS-102 valid-water pixels enter arithmetic. Every input scene must
validate, including finite values in all nine bands under water; feature-specific
finite support is defended separately. Preserve negative inputs/denominators;
float64 arithmetic returns float32 without clipping.

For NDCI-like use denominator B05+B04 and scale |B05|+|B04|; for each ratio use
the denominator band and scale |numerator band|+|denominator band|. Reject when
`abs(d) <= max(1e-4, 1e-6*scale)`. These fixed v1 implementation constants are
numerical guards, not bloom thresholds or calibrated noise floors. No new TOML
fields. Nonfinite float64 results or float32 overflow are also rejected. Rejections
become false masks and NaN; no offsets, zero substitution or forced ranges.

Each feature reports valid_count, valid_fraction_of_parent_water, min/max and
p05/median/p95 using linear percentiles of the final float32 outputs in float64.
These are single-scene summaries, not AS-104 temporal statistics. Empty summaries
use None; an empty parent gives fraction None, while zero feature support with a
nonempty parent gives fraction 0.0. Metadata JSON contains no arrays or NaN.

Diagnostic populations are parent-valid-water pixels: negative_required_input_count
counts any required input <0; negative_denominator_count includes negative
rejected denominators (signed zero is not <0). Denominator and nonfinite-result
rejections are disjoint and reconcile with feature count. NDCI-like nominal-range
count uses valid float32 outputs strictly outside [-1,1]. Other features have no
nominal output range and use None. MCI-like denominator counts are zero.

## Fingerprint, Identity and Provenance

Fingerprint format `as103-input-v1` uses SHA-256 over length-delimited canonical
JSON segment headers and payloads. Headers include byte counts, shape, band names,
counts, dtype and order. Full spatial mask is C-order uint8; values for B02/B03/
B04/B05/B06 on mask support are C-order little-endian float32. The canonical band
order is fixed. Excluded pixels and unconsumed bands do not contribute. Parent
arrays are mutable despite frozen dataclasses; the fingerprint prevents a changed
consumed input from reusing the old feature identity. No concurrent-mutation
transaction guarantee is claimed; callers must not mutate an input during extraction.

Canonical JSON identity includes parent ID/version, input fingerprint, full grid,
acquisition timestamp normalized to UTC, feature order/formulas/bands/families,
nominal wavelengths, numerical/support/dtype/statistics policies and Python/NumPy
versions. A separate mask digest lets model validation check the preserved spatial
mask without retaining reflectance. Product ID is `spectral:<SHA-256(identity)>`;
creation time and calculated statistics are excluded. The stable JSON guard rejects
credentialled/query-bearing URLs; no URLs are needed by AS-103.

Provenance type is `spectral_feature_scene`, version `as103-v1`, source_ids exactly
`(parent AS-102 derived product ID,)`. Existing registry supports this edge; register
PC source, then AS-102, then AS-103. CDSE stays contextual provenance in the parent,
not an additional pixel-source edge. The generic schema and AS-102 are unchanged.

## Scientific References and Limits

- [ESA SNAP documentation](https://step.esa.int/main/doc/), Sentinel-2 MCI algorithm
  specification: owner-approved basis for nominal B4/B5/B6 at 665/705/740 nm.
  AquaSentinel deliberately uses k=1.0 and the name mci_like rather than claiming
  the official SNAP MCI product. The versioned help page retrieval attempted on
  8 October returned environmental HTTP 403; no successful reference retrieval is
  claimed, and no provider XML wavelength claim is made.
- Mishra, S. and Mishra, D.R. (2012), “Normalized difference chlorophyll index:
  A novel model for remote estimation of chlorophyll-a concentration in turbid
  productive waters”, Remote Sensing of Environment 117, 394–406,
  [DOI 10.1016/j.rse.2011.10.016](https://doi.org/10.1016/j.rse.2011.10.016).
  Its water Rrs bands around 665/708 nm do not make our L2A BOA 665/705 nm feature
  a calibrated chlorophyll product.

BOA is not aquatic Rrs. Coastal adjacency, shallow bottom, sediment, glint,
atmospheric-correction residuals and SCL errors affect the signals. ndci_like and
red_edge_red_ratio are mathematically related: (ratio−1)/(ratio+1) where both are
defined; they must not later count as independent biological evidence. There is no
event threshold, anomaly/HAB classification, chlorophyll concentration, species,
toxin, safe/unsafe water, shutdown, risk, exposure, persistence or lead-time result.

## Reproduction and Review

Run `python -m pytest tests/features -v`, `python -m pytest -v`,
`python -m ruff check .`, `git diff --check` in the existing Python 3.11 environment.
Load the documented parent cache using `preprocess_optical_scene(context,
known_cache_id=...)`, then call `extract_spectral_features(parent)`; extraction has
no cache or network dependency. Missing parent cache uses only the established
AS-102 provisioning workflow. [Acceptance evidence](evidence/AS_103_SPECTRAL_FEATURES_VALIDATION.md)
records full summaries, independent scalar checks, blocked-I/O repeat and lineage.
Review the uncommitted feature branch before any publication; AS-104 remains unauthorized.
