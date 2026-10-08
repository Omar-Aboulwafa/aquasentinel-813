# AS-103 — Spectral Feature Acceptance Evidence

**Recorded:** 8 October 2026 (Asia/Dubai). **Status:** One cached real-scene
acceptance PASS; implementation uncommitted/unpushed/unmerged for review.
**Branch:** `feature/as-103-spectral-features`.
**Base main:** `642a469414f096b4ac7cd96de895aa38f7da42ec`.
**Evidence IDs:** EV-019 (features/diagnostics), EV-020 (identity/lineage/offline quality).
AS-104 is NOT authorized and NOT started. This is not a HAB/anomaly interpretation.

## Experiment and Input

- Started UTC: `2026-10-08T09:52:47.133486+00:00`.
- Started Asia/Dubai: `2026-10-08T13:52:47.133486+04:00`.
- Completed UTC: `2026-10-08T09:52:47.209734+00:00`.
- Acquisition: `2023-04-28T06:46:29.024000+00:00`; experiment time is distinct.
- Actual PC raster product: `S2B_MSIL2A_20230428T064629_R020_T40RBN_20230428T122311`.
- Existing verified parent cache: `0725a908d21cd655e83f70d2bb11247dc0f1516f0c00ea275efc3239113ee4a6`.
- Parent derived product: `optical:0725a908d21cd655e83f70d2bb11247dc0f1516f0c00ea275efc3239113ee4a6`.
- Grid EPSG:32640, 20 m; width 310, height 228; bounds
  `[249020,2702860,255220,2707420]`, affine `[20,0,249020,0,-20,2707420]`.
- Parent valid-water count: **7,963**. No parent cache provisioning, new raster
  reads, downloads, resampling, mask changes or external requests were needed.

## Feature Summaries

All six feature arrays are float32 (228,310), with same-shape boolean masks.
Fractions use parent-valid-water count 7,963. Statistics summarize retained
float32 values; percentiles use NumPy linear interpolation in float64.

| Feature | Valid count | Parent-water fraction | Minimum | Maximum | p05 | Median | p95 |
|---|---:|---:|---:|---:|---:|---:|---:|
| ndci_like | 7963 | 1.0 | -2.572964668273926 | 0.20351892709732056 | -0.35202173590660096 | -0.14267197251319885 | 0.0423086155205965 |
| mci_like | 7963 | 1.0 | -0.01742854155600071 | 0.09121209383010864 | -0.0012384170317091046 | 0.0008878124062903225 | 0.0729243278503418 |
| red_edge_red_ratio | 7963 | 1.0 | -0.440240740776062 | 1.511045217514038 | 0.47926616072654726 | 0.7502835988998413 | 1.0883553862571715 |
| red_edge2_red_ratio | 7963 | 1.0 | -1.3180077075958252 | 1.2187410593032837 | -0.05205329470336437 | 0.36368128657341003 | 0.6793842673301697 |
| green_red_ratio | 7963 | 1.0 | 0.8410873413085938 | 10.129327774047852 | 1.2489951491355897 | 3.1720826625823975 | 5.015284156799316 |
| green_blue_ratio | 7963 | 1.0 | 0.9837192296981812 | 1.706419587135315 | 1.0739787340164184 | 1.1939759254455566 | 1.3871012568473815 |

## Diagnostics

Counts are over parent valid-water support. A negative input is diagnostic, not
invalidity. Denominator rejection and nonfinite-result rejection are disjoint.
There is no event threshold. None means no nominal-range policy applies.

| Feature | Parent water | Negative required input | Denominator rejection | Negative denominator | Nonfinite rejection | Outside nominal range |
|---|---:|---:|---:|---:|---:|---:|
| ndci_like | 7963 | 2 | 0 | 0 | 0 | 2 |
| mci_like | 7963 | 491 | 0 | 0 | 0 | None |
| red_edge_red_ratio | 7963 | 2 | 0 | 0 | 0 | None |
| red_edge2_red_ratio | 7963 | 491 | 0 | 0 | 0 | None |
| green_red_ratio | 7963 | 0 | 0 | 0 | 0 | None |
| green_blue_ratio | 7963 | 0 | 0 | 0 | 0 | None |

The two NDCI-like outputs below −1 were retained; they are not HAB evidence.
491 parent-water pixels had at least one negative B04/B05/B06 input; those values
remain eligible when numerically stable. No denominator/nonfinite exclusions
occurred in this scene; offline tests establish those failure/edge cases.

## Independent Scalar Pixel Checks

Four selected common-support pixels were independently checked with scalar Python
arithmetic from the original float32 BOA band values (not by calling the feature
math implementation). Values below show the independent float64 calculations;
feature outputs agreed after float32 representation (rtol 1e-6, atol 1e-8).
Rows/columns are zero-based. The fourth pixel includes a negative B06.

| Row, column | B02 | B03 | B04 | B05 | B06 |
|---|---:|---:|---:|---:|---:|
| 4, 195 | 0.03780156001448631 | 0.0383109375834465 | 0.011735937558114529 | 0.00930000003427267 | 0.007199999876320362 |
| 70, 228 | 0.040565624833106995 | 0.04874062538146973 | 0.010567187331616879 | 0.006599999964237213 | 0.0017999999690800905 |
| 170, 7 | 0.07987187802791595 | 0.09604687243700027 | 0.08695937693119049 | 0.07779999822378159 | 0.07649999856948853 |
| 30, 302 | 0.045140624046325684 | 0.05711718648672104 | 0.013920312747359276 | 0.008200000040233135 | -9.999999747378752e-05 |

| Row, column | ndci_like | mci_like | B05/B04 | B06/B04 | B03/B04 | B03/B02 |
|---|---:|---:|---:|---:|---:|---:|
| 4, 195 | -0.11579885674900517 | -1.6770760218302525e-05 | 0.7924377569512895 | 0.6135001861306 | 3.2644121863921587 | 1.013475040944474 |
| 70, 228 | -0.23109128472884716 | 0.0007086458926399549 | 0.6245748993670345 | 0.17033860691524938 | 4.612450205707857 | 1.2015253205638 |
| 170, 7 | -0.05559245838844452 | -0.003581043581167856 | 0.8946706033248539 | 0.8797210981631308 | 1.1045027669989007 | 1.202511757685615 |
| 30, 302 | -0.25859999187419913 | 0.001757187423451493 | 0.5890672278026727 | -0.007183746463796786 | 4.103153968114426 | 1.265316722872603 |

## Determinism, Fingerprint and Lineage

Input fingerprint (`as103-input-v1`):
`e76edf08917ef02cfdb544d811fe6df79ea29f014842be5d29fbb03645d475d7`.

AS-103 product:
`spectral:dae91b4dda0131ca2d2987321abd2ffd5c4b5ffb2e95a44880b7a5f9a67ea64b`.

Registry lineage was exactly:

1. Actual PC SourceRecord: `stac:ef177b34b0fa3cabbb6d613d65f1c55d8ea4c5959326bb8896ec51d111792740:sentinel-2-l2a:S2B_MSIL2A_20230428T064629_R020_T40RBN_20230428T122311`.
2. AS-102 parent DerivedProductRecord: `optical:0725a908d21cd655e83f70d2bb11247dc0f1516f0c00ea275efc3239113ee4a6`.
3. AS-103 feature DerivedProductRecord: `spectral:dae91b4dda0131ca2d2987321abd2ffd5c4b5ffb2e95a44880b7a5f9a67ea64b`.

The immediate AS-103 source_ids contains only the AS-102 parent, not the raw PC
source or CDSE discovery source. Existing generic registry/schema are unchanged.

Repeated extraction returned equal arrays/masks (including NaNs), statistics,
diagnostics, processing parameters, fingerprint and product ID; creation timestamp
is excluded. Input bands, valid-water mask and provenance remained unchanged.
Every pixel outside each feature's valid support was NaN, and no mask expanded
beyond parent water.

## Offline Access/Write Boundary and Quality

The verified parent was loaded before the protected feature-extraction scope.
Extraction/repeat ran with catalog, signing, metadata/raster reads and cache-write
functions replaced by failing sentinels, plus builtins/Path file opening and
writing, network connection/urlopen, rasterio.open and NumPy save functions blocked.
No sentinel was called. Only small evidence summaries were written outside that
scope; no AS-103 feature raster/cache was persisted.

- Existing baseline: 265 tests.
- New AS-103 offline cases: 83.
- Final full suite: **348 passed**; six existing Rasterio PendingDeprecationWarnings.
- Ruff: passed. `git diff --check`: passed.
- No new dependency/configuration, AS-102/provenance algorithm or cache-format change.

Normal tests use synthetic fixtures, independently calculated formulas, signed/
zero/boundary/cancellation values, support/empty cases, float32 overflow,
model/provenance tampering, identity/fingerprint sensitivity and blocked I/O.
No external data calls are needed by AS-103 tests.

## Reproduce and Limitations

Use the existing Python 3.11 environment. Load the parent via
`preprocess_optical_scene(context, known_cache_id="0725a908d21cd655e83f70d2bb11247dc0f1516f0c00ea275efc3239113ee4a6")`,
then call `extract_spectral_features(parent)` twice. Compare arrays/masks and
summaries/IDs, check independent scalar formulas and register PC→AS-102→AS-103.
The execution plan/API defines all formulas and byte-level fingerprint rules.

This is one cached observation, not a temporal or event analysis. BOA is not
water Rrs, ndci_like is not calibrated chlorophyll, and mci_like is an analogue
using declared nominal wavelengths/k=1.0. Coastal adjacency, sediment, shallow
bottoms, glint, atmospheric-correction residuals and SCL errors remain.
There is no HAB/species/toxin/water-safety/shutdown/exposure/risk/persistence/
lead-time claim. Feature correlations are not independent biological evidence.
Scientific reference-page retrieval was blocked with HTTP 403; the accepted
reference basis is documented without claiming a live literature fetch.

Presentation capture still needed: sanitized feature/support/diagnostic maps
(V18), formula/lineage card (V19), and independent future science validation.
No screenshot is claimed to exist. No commit/push/PR; AS-104 has not started.
