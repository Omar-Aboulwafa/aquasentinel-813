# AS-105 — Predeclared Family-Aware Candidate Anomaly Geometry

## Current AS-105 M29 status — 10 October 2026 (Asia/Dubai)

**M28: COMPLETE / COMMITTED / PUSHED**, implementation `57100b2e53e941f3a7fdfdfc40b61d2b4043c0e5`,
branch `feature/as-105-hab-anomaly-geometry`, remote
`origin/feature/as-105-hab-anomaly-geometry`, base main `4e322df220f8cab2805fccf9a2b32dd825f29218`.
**M29 / E29 / EV-033: REAL ENGINEERING ACCEPTANCE PASS; OWNER REVIEW PASS.**
Decision 050 remains unchanged; M29 is an execution/evidence checkpoint, not
Decision 051. The accepted AS-104 handoff was the only real input; no network,
upstream reprocessing or AS-102 cache loading, and no policy tuning.

Foundation/continuity complete → AS-101/102/103 merged → Decisions 048/049 merged → AS-104 COMPLETE AND MERGED → AS-105 M28 COMPLETE / COMMITTED / PUSHED → AS-105 M29 REAL ENGINEERING ACCEPTANCE PASS → owner review of M29 documentation/publication followed by PR preparation → AS-105 FEATURE NOT YET PR-MERGED → AS-106+ NOT STARTED; P1 05.10 NOT STARTED.

Target valid water **7,963**; policy-evaluable support P **802** (**10.071581%**
coverage diagnostic); candidates **7**, fraction **7/802 = 0.872818%** of P.
**Projected-grid candidate area: 2,800 m² / 0.0028 km².** One eight-connected
region, one MultiPolygon with three four-connected pieces; F2/F4 agreement.
P is not full AOI/ocean/risk coverage, and its coverage is not candidate fraction.
Sparse-history support remains material; no masks were relaxed.

Frozen real product: `hab_geometry:70876fbcb25e8a37abaa238a59e1da32fec9066792e6239db68e284b7bd18682`.
First extraction **2026-10-10T05:45:15.046037+00:00–05:45:15.173566+00:00** /
**09:45:15.046037–09:45:15.173566 +04:00 Asia/Dubai**;
acceptance completed **05:45:46.711968 UTC / 09:45:46.711968 +04:00**.
Execution/acceptance precede owner review and this later documentation publication;
no PR or merge timestamp exists. **PR NOT CREATED; FEATURE NOT YET MERGED.**

Independent masks/families/P/C, components, area and polygon round-trip PASS;
repeat **27/27 arrays**, parent immutability **61/61**, bundle read-back PASS.
M29 gates: **140 focused / 803 full tests PASS**, Ruff/diff PASS;
only six existing Rasterio PendingDeprecationWarnings. These are local checks,
not GitHub CI or scientific accuracy. External local evidence bundle:
`/workspace/aquasentinel-acceptance/as105/m29/`, **NOT tracked in Git**.

M29 establishes reproducible real candidate spectral anomaly geometry only. It does NOT establish confirmed HAB/bloom, chlorophyll concentration, species/toxins, biological causation, sensitivity/specificity/accuracy/false-positive rate, event agreement, persistence, risk/confidence, water safety, intake exposure, alert or warning lead time. No comparison with the historical April event was performed. Rank is not probability/confidence/significance/severity; policy families are not statistically independent. Five observations are not statistical sufficiency.
Future comparative policy validation: **REQUIRED / NOT RUN**, including
predeclared history-depth sensitivity; AS-106+ and P1 05.10 **NOT STARTED**.
Immediate next step: **owner review of M29 documentation/publication followed by
PR preparation**; no PR creation or merge in this task. All earlier M01–M28,
E01–E28, EV-001–EV-032 and Decisions 001–050 remain historical and preserved.
The old M28 status below describes its earlier checkpoint, not current status.
See [AS-105 contract](AS_105_HAB_ANOMALY_GEOMETRY.md) and [M29 validation](evidence/AS_105_HAB_ANOMALY_GEOMETRY_VALIDATION.md#m29--real-geometry-engineering-acceptance--10-october-2026).

## Historical M28 implementation/publication boundary

9 October 2026 (Asia/Dubai): owner-authorized **M28 offline implementation only**.
Branch `feature/as-105-hab-anomaly-geometry`, base
`4e322df220f8cab2805fccf9a2b32dd825f29218`.
Implementation/adversarial synthetic validation and owner-review clarification
**PASS / FEATURE PUBLICATION AUTHORIZED** on 10 October 2026 (Asia/Dubai). Decision 050 records the scientific policy; M28/E28/EV-032
records implementation evidence. Owner-authorized commit/push follows final gates;
this record accompanies publication. PR code review is next after Git/remote
verification; no PR creation or merge is authorized in this task.

Input: a validated `TemporalFeatureScene` from AS-104 v1. Output: deterministic,
explainable **candidate spectral anomaly geometry** on its existing grid.
AS-104 math, AS-103 features, AS-102 processing, generic provenance and caches
are unchanged. No new dependencies: existing NumPy, Rasterio and standard library.

Real AS-105 acceptance has **NOT RUN** and is not authorized here. M29 / E29 / EV-033 remain reserved and NOT CREATED. Real candidate pixel count, fraction, area,
region count, fragmentation and family-vote distribution remain **UNKNOWN**.
Future policy comparison is required and **NOT RUN**. AS-106+ and P1 homogeneous
05.10 robustness are **NOT STARTED**.

## Historical M28 plan and implementation scope

Goal: translate predeclared per-feature temporal evidence into family agreement,
an explicit evaluable support population, eight-connected regions and exact
projected pixel-edge polygons. Retain every candidate, including single pixels.

Execution steps completed:

1. Fetch/verify the approved main base and create an isolated worktree.
2. Snapshot existing worktrees, accepted cache/handoff hashes, stashes and recovery material.
3. Implement the frozen policy, typed output, deterministic spatial kernels and integrity checks.
4. Exercise the offline synthetic controls and all mandated adversarial cases.
5. Run focused/full tests, Ruff and tracked/untracked whitespace checks.
6. Record Decision 050 and M28/E28/EV-032; original 9 October stop was uncommitted.
7. Reconcile the 10 October owner clarification and four synthetic regression
   cases; publish exactly the approved 18 paths after final quality/preservation gates.

Four source modules: `geometry/__init__.py`, `models.py`, `hab.py`, `spatial.py`.
Seven test files under `tests/geometry/`; this document and its validation record;
five continuity/decision/presentation files. Exactly 18 repository paths.

Acceptance criteria: correct policy at the exact float32 boundary, no expansion
outside eligible water support, exact component/polygon/area correspondence,
consumed-bit-sensitive identity, parent-aware tamper rejection, immediate AS-104
lineage, parent immutability, no IO/upstream recalculation, all existing tests
retained and protected files byte-identical. See [offline validation](evidence/AS_105_HAB_ANOMALY_GEOMETRY_VALIDATION.md).

Risks addressed: duplicate family evidence, sparse support denominators, unstable
polygon ordering, diagonal bridges, nonrepresentable area, irrelevant versus
consumed input mutations and metadata tampering. Remaining scientific risks are
correlated evidence families, small historical samples and an unvalidated
screening heuristic. Performance on real-scene fragmentation has not been measured.

## Frozen policy — as105-v1

Canonical feature order remains AS-103's order:
`ndci_like`, `mci_like`, `red_edge_red_ratio`, `red_edge2_red_ratio`,
`green_red_ratio`, `green_blue_ratio`.

| Family | Canonical name | Members |
|---|---|---|
| F1 | `red_edge_b5_vs_red` | `ndci_like`, `red_edge_red_ratio` |
| F2 | `red_edge_line_height` | `mci_like` |
| F3 | `red_edge_b6_vs_red` | `red_edge2_red_ratio` |
| F4 | `visible_green_vs_red` | `green_red_ratio` |
| F5 | `visible_green_vs_blue` | `green_blue_ratio` |

These are distinct policy evidence families, **not statistically independent
measurements**. In particular, the two F1 features cannot contribute two votes.

For each feature `f`:

```text
S_f = rank_valid_mask
E_f = S_f AND (deviation > 0) AND (empirical_rank >= float32(0.90))
```

Threshold identity explicitly records nominal decimal `0.90`, dtype `float32`,
actual value `0.8999999761581421` and big-endian IEEE-754 hex `3f666666`.
The stored float32 threshold passes; its immediate predecessor fails.
Both +0.0 and -0.0 deviations fail. No epsilon, clipping, fallback or imputation.
Supported rank/deviation can vote when robust z is unavailable, including zero
MAD. Large z alone cannot vote. Robust z is neither consumed nor summarized.

### Owner-review clarification — five-history rank granularity

10 October 2026 (Asia/Dubai): the nominal 0.90 threshold and float32 comparison
are unchanged. It is a predeclared empirical-rank screening threshold whose
effective granularity depends on available historical sample count. It is not
a statistically estimated population 90th percentile, significance, probability,
confidence or severity.

The frozen AS-104 exact-tie midrank is
`(count(history < target) + 0.5 * count(history == target)) / n`.
The accepted real parent reserved for future M29 uses minimum five and exactly
five references. With n=5 and no ties, ranks are
`0.0, 0.2, 0.4, 0.6, 0.8, 1.0`: spacing 0.2.
Therefore rank >=0.90 means the target exceeds all five historical values when
there are no ties. Exactly 0.90 is possible only with four values below and one
equal, `(4 + 0.5*1)/5`. Three below and two equal gives 0.80 and fails.
Ranks are stored as float32 and use the frozen threshold's float32 semantics;
positive deviation remains separately required.

This upper-tail screen is not a smooth percentile estimator. Five observations
are not statistical sufficiency. Four synthetic regression cases exercise the
unchanged AS-104 calculation followed by AS-105; no real handoff or upstream
numerical implementation is changed. This clarification stays within M28 and
Decision 050; it creates no real-acceptance checkpoint.

For each family `j`, availability `A_j = OR(S_f)` and evidence `V_j = OR(E_f)`
over its members. Each family contributes at most one vote. Candidate policy:

```text
C = (sum(V_j) >= 2) AND any(V_F1, V_F2, V_F3)
P = (sum(A_j) >= 2) AND any(A_F1, A_F2, A_F3)
```

`P` is policy-evaluable support, independent of observed ranks/directions and
candidate classification. `C` is contained in `P` and AS-104 valid water.
Candidate fraction is `count(C) / count(P)`; empty P yields `None`, while
nonempty P with no candidates yields `0.0`. It is not a fraction of AOI, all
water or the intersection of all six feature masks. Feature/family diagnostics
use their own support/availability denominators, with `None` for empty support.

## Spatial semantics

Eight-neighbour deque flood fill scans candidate pixels in row-major order.
The first candidate pixel seeds label 1, then 2, etc.; background is 0 and
labels are int32. Neighbour offsets have fixed lexicographic order. Explicit
overflow rejection prevents label wrap. There is no minimum size, morphological
operation, filtering, smoothing, gap fill or interpolated bridge.

Rasterio polygonizes **four-connected pieces** of the already assigned labels,
in integer pixel coordinates. Pieces sharing an eight-connected label are
grouped into one region, possibly `MultiPolygon`. Diagonal contact never adds
a bridging pixel. Outer rings wind counterclockwise in projected coordinates,
holes clockwise. Pixel-space lexicographic ring starts, sorted holes and sorted
parts make representation independent of GDAL emission order. Affine mapping
preserves exact grid edges; no rounding, simplification, buffering or support
snapping. Corner-touch/pinched fixtures are checked by exact raster round-trip;
this is a grid-support contract, not a general OGC topology-repair facility.

The geometry is a projected geometry mapping in `AnalysisGrid.crs`, **not WGS84
longitude/latitude GeoJSON**. Every generated geometry must rasterize back to
the exact original labels with centre-based rasterization (`all_touched=False`).

V1 accepts explicit EPSG projected metre grids with finite, nonsingular,
north-up square affine pixels and consistent resolution, dimensions and bounds.
Geographic, foot-unit, rotated/sheared, rectangular, inconsistent and malformed
grids fail. Pixel area is `abs(a*e - b*d)`, not a hardcoded 400. Region area is
pixel count × pixel area; km² divides by 1,000,000. Call it **projected-grid candidate area**, not confirmed bloom extent.

## API and typed output

```text
extract_hab_anomaly_geometry(parent: TemporalFeatureScene)
    -> HABAnomalyGeometryScene
scene.validate(parent)
```

The public extractor has only the immediate parent argument; no tuning knobs.
It validates the parent, copies mutable arrays, performs pure computation and
does not mutate a registry, retrieve assets, access caches or run upstream stages.

Frozen scene fields: grid, parent temporal product ID, target acquisition;
feature support/evidence dictionaries; family availability/evidence dictionaries;
policy support mask; uint8 available-family/vote counts; Boolean candidate mask;
int32 labels; ordered region tuple; typed statistics/diagnostics; processing
parameters; deterministic product ID; `DerivedProductRecord`.

Each frozen region contains its deterministic ID and label, seed row/column,
canonical geometry, pixel count, m²/km² area, projected bbox, participating
families, per-family evidence pixel counts, maximum/median family votes and
per-feature finite-supported deviation/rank count/minimum/median/maximum.
Missing regional feature support has count 0 and `None` summaries.
Median uses the sorted middle value, or the float64 midpoint for even counts;
same-sign extreme pairs use half-sums to avoid finite-input overflow. Ordinary
midpoint arithmetic is preserved; input values are never clipped or imputed.
No robust-z region summary. Scene statistics include support/candidate counts,
policy fraction, area, region count, one-pixel count, largest/median sizes/areas,
size bins (`1`, `2-4`, `5-9`, `10-49`, `50+`) and vote histograms 0–5 separately
over P and candidates. Output arrays never alias parent buffers; frozen
dataclasses still contain mutable NumPy buffers, so `.validate(parent)` detects
later tampering rather than promising deep immutability.

## Identity, fingerprints and provenance

Processing version: `as105-v1`; type: `hab_anomaly_geometry`; ID:
`hab_geometry:<sha256(canonical identity)>`. Identity includes immediate parent
ID/version, target UTC, full grid/grid ID, consumed fingerprint, complete frozen
policy (orders/mapping, threshold bits, direction, minimum families, red-edge
requirement, components/polygon/area/statistics/denominator, no morphology/filter)
and Python/NumPy/Rasterio/GDAL versions. `created_at` is excluded.

`as105-input-v1` SHA-256 hashes canonical length-delimited segments: 8-byte
unsigned big-endian JSON-header length, canonical JSON bytes (including payload
byte count), then raw payload. Fixed order: grid, mapping/orders, each complete
rank-valid mask as uint8 C order, its supported deviations as little-endian
float64 row-major and its supported ranks as little-endian float32 row-major.
Consumed values must be finite; exact bits, including signed zero, are retained.
Memory order and source endianness canonicalize to the same fingerprint.

Excluded: robust z, anomaly mask, baseline centre/scale, observation counts,
parent statistics, unsupported NaN payloads, provenance timing and the whole
parent output hash. Parent validation still enforces the original AS-104 native
dtype/NaN contract; only the fingerprint helper's endian canonicalization is
tested on endian-converted arrays. No upstream contract is weakened.

`as105-output-v1` separately hashes all output masks/counts/labels, canonical
geometries, region measurements/summaries and scene statistics/diagnostics.
Product-derived region IDs are excluded from this hash to avoid circularity.
Input-bit changes alter identity even without a classification change.

Immediate provenance `source_ids` is exactly `(parent.product_id,)`. Existing
registry recursion yields actual PC → AS-102 → AS-103 → AS-104 → AS-105.
No generic schema change, direct PC/optical/spectral shortcut or mutable registry
side effect. `.validate(parent)` validates AS-104, regenerates private kernels
and compares all support/evidence/count/label arrays and their shape/dtype/order,
geometry round-trip, measurements, summaries, metadata, identities, fingerprints
and provenance. Rehashing an altered policy cannot make it valid as105-v1.

## Verified real-parent prerequisite — not AS-105 execution

Accepted AS-104 temporal product:
`temporal:e814b0574ab30d1841778ee3c5005ffcb313ab42473c41acc028f0a9f7804a8b`.
Accepted output fingerprint:
`2a2902f946d49487f1416d0bd6ad73c7976910fe72060f03503540a49e2678dd`.
No real arrays were loaded by AS-105 in M28.

External read-only handoff: `/workspace/aquasentinel-handoffs/as104/` followed by
the temporal identity digest. It is not tracked in Git. Its prior verified
reconstruction recorded 61/61 arrays, `allow_pickle=False` round-trip and
`scene.validate()` PASS. M28 checks only file hashes/permissions, not those
arrays through the extractor. Exact SHA-256 values and preservation results are
in [prerequisite evidence](evidence/AS_105_HAB_ANOMALY_GEOMETRY_VALIDATION.md#verified-handoff-prerequisite).

## Scientific limitations and future validation

This predeclared P0 heuristic is an explainable engineering screening policy,
not an empirically optimized or validated HAB classifier. Rank is not probability,
confidence, significance or severity. Agreement is not biological causation.
BOA-derived signals are not aquatic remote-sensing reflectance or concentration.
No confirmed HAB/bloom, chlorophyll, species, toxins, water safety, intake risk,
persistence, confidence, alert or warning lead-time inference is established.

The AS-104 limitation remains: roughly 10% of target-valid support has all five
historical observations. Five observations are not statistical sufficiency;
small positive scales can yield large z. AS-105 neither relaxes those masks nor
uses z to hide sparse support. P measures where this policy can be evaluated,
not where the ocean has been comprehensively assessed.

Required **future**, bounded, predeclared comparative study must include:

- rank + direction, z + direction, combined rank/z;
- rank thresholds 0.80 / 0.90 / 0.95;
- family minimum 1 / 2 / 3;
- red-edge required / optional;
- connectivity 4 / 8;
- no filtering versus separately labelled region-filter sensitivity.
- **history-depth sensitivity:** where valid EO availability permits, predeclare
  comparisons around five, moderately deeper and substantially deeper histories;
  choose exact depths from valid EO availability before running the study.

History-depth sensitivity must assess whether conclusions depend excessively
on coarse five-observation empirical ranks. It is NOT RUN, and does not change
minimum_observations=5 or the accepted frozen AS-104 parent for M29.

Do not optimize on April 28 and then use it as the sole proof of superiority.
This study is not authorized/run now. Separately authorized M29 real engineering
acceptance is PASS under the unchanged policy; see the dated M29 evidence below. No persistence, risk/confidence, historical
accuracy validation, intake exposure, alerting, monitoring recommendations, ML,
threshold fitting, full-scene export or new cache system is implemented here.

## M29 real acceptance under the unchanged contract

Owner-reviewed M29 / E29 / EV-033 PASS on 10 October 2026 (Asia/Dubai), using
implementation `57100b2e53e941f3a7fdfdfc40b61d2b4043c0e5` and the frozen accepted AS-104 parent
`temporal:e814b0574ab30d1841778ee3c5005ffcb313ab42473c41acc028f0a9f7804a8b`. Version `as105-v1`, input fingerprint `c50d9f6300060ab9f194c1a0b8808de340eb53326268a52ef083ad7f994b2bc5`,
output fingerprint `ff976ec800ec2dfc966e4f373dd3f2442938a06a10254dd4ea7a86280dd0a765`. The observed result is 7 candidate pixels out of
802 policy-evaluable pixels, one eight-connected region and three polygon pieces;
projected-grid candidate area 2,800 m² / 0.0028 km². The support coverage is
802/7,963 = 10.071581%, not comprehensive water assessment or risk coverage.
No supported rank equalled float32(0.90); supported ranks in this parent were
limited to 0/float32(.2)/float32(.4)/float32(.6)/float32(.8)/1. Thus >=float32(.90)
selected rank 1.0 for these observed pixels only. The algorithm remains >=float32(.90),
and four-below/one-exact-tie can still yield .90 in another five-history pixel.
Future predeclared history-depth sensitivity remains required and NOT RUN.

Exact feature/family/rank tables, sole region, timestamps, bundle hashes and all
independent acceptance checks are in [AS-105 contract](AS_105_HAB_ANOMALY_GEOMETRY.md) and [M29 validation](evidence/AS_105_HAB_ANOMALY_GEOMETRY_VALIDATION.md#m29--real-geometry-engineering-acceptance--10-october-2026). No real execution rerun in this
documentation task. PR NOT CREATED; feature NOT YET PR-MERGED; AS-106+ and P1
05.10 NOT STARTED. M28 synthetic results remain historically distinct.
