# AS-104 — Temporal Baseline Validation Evidence

**Recorded:** 8 October 2026 (Asia/Dubai).
**Branch:** `feature/as-104-temporal-baseline`.
**Base main:** `c6accab2c5753734466a6375d1b3ce1762e99bed`.
**Decision:** 047; explicitly authorized, implementation uncommitted for review.
**Evidence IDs:** EV-022 (offline algorithm/identity/lineage), EV-023 (blocked real
multi-scene acceptance). AS-105/106/107/108 remain unauthorized and unstarted.

## 1. Algorithm / unit-test evidence — PASS

The execution plan was created before source implementation. Added the temporal
API/models and 112 independent offline cases covering median/MAD/1.4826,
positive/negative deviation, exact-tie midrank, zero/tiny scale, float32 overflow,
feature/date-specific support, sparse/empty outcomes, causal windows/self-exclusion,
semantic fingerprint sensitivity/independence, model/metadata corruption,
processing compatibility, exact multi-parent lineage and blocked IO/immutability.

The initial offline gate completed BEFORE the real experiment:

- Full pytest before real work: **459 passed** (348 retained +111 temporal cases).
- Ruff: passed. `git diff --check`: passed.
- Six existing Rasterio PendingDeprecationWarnings, no new warning category/count.
- Actual interpreter: existing `.venv/bin/python`, Python 3.11.16. The shell's
  default Python lacks pytest/Ruff; no package installation or dependency change.
- Registry is read-only during computation. No retrieval/signing/raster/cache or
  disk IO occurs in AS-104. No configuration, cache-format or generic-provenance change.

Final inspection after the blocked experiment added a single-pass-collection
regression: selection reuses the already validated inputs rather than iterating
the caller collection again. The final gate is **460 passed** (348 retained +112
temporal cases), Ruff/diff passed, with the same six historical warnings. This
later gate did not rerun or unblock the real experiment.

Fingerprints use `as104-input-v1`: full target water/feature masks and supported
values; reference masks only at target feature support and values only on their
intersection. Invalid NaN payloads and excluded scenes do not contribute. A parent
ID change still changes identity independently of pixel fingerprints, as required.
Reference-outside-target tests keep the registered parent ID fixed to isolate the
semantic-content rule. No precision-limited-scale diagnostic or epsilon floor.

## 2. Predeclared real multi-scene engineering acceptance — BLOCKED

This is an actual attempted experiment, not a multi-scene PASS or science result.
Frozen target: 28 April 2023, selected because earlier engineering acceptance exists.
Frozen references: `[2023-03-01T00:00:00Z, 2023-04-01T00:00:00Z)`.
Frozen minimum: **5**. Same tile **40RBN**, orbit **20**, delivered PC baseline
**05.09**, fixed grid/processing contracts. No bounds/minimum/mask changes.

- Experiment started UTC: `2026-10-08T12:28:07.712335+00:00`.
- Experiment started Asia/Dubai: `2026-10-08T16:28:07.712335+04:00`.
- Experiment stopped UTC: `2026-10-08T12:28:29.564367+00:00`.
- Experiment stopped Asia/Dubai: `2026-10-08T16:28:29.564367+04:00`.

Acquisitions below are satellite times, distinct from those experiment times.
Unchanged AS-101 rediscovered **44** configured March–May cloud-filtered candidates.
Within March, **5** discovery observations satisfy the target tile/orbit filter;
13 other March products have a different tile and/or orbit. This metadata does not
establish usable historical pixels or compatible delivered products.

### Metadata candidates — not processed/accepted references

| Acquisition UTC | Platform | CDSE discovery product | Scene cloud % |
|---|---|---|---:|
| 2023-03-04T06:47:51.024000+00:00 | sentinel-2a | `S2A_MSIL2A_20230304T064751_N0510_R020_T40RBN_20240819T072511` | 2.46 |
| 2023-03-09T06:47:19.025000+00:00 | sentinel-2b | `S2B_MSIL2A_20230309T064719_N0510_R020_T40RBN_20240823T054455` | 24.96 |
| 2023-03-14T06:46:41.024000+00:00 | sentinel-2a | `S2A_MSIL2A_20230314T064641_N0510_R020_T40RBN_20240823T041506` | 0.25 |
| 2023-03-24T06:46:21.024000+00:00 | sentinel-2a | `S2A_MSIL2A_20230324T064621_N0510_R020_T40RBN_20240824T014318` | 12.12 |
| 2023-03-29T06:46:29.024000+00:00 | sentinel-2b | `S2B_MSIL2A_20230329T064629_N0510_R020_T40RBN_20240823T165234` | 0.6 |

### Exact blocker and bounded metadata diagnosis

The experiment stopped while resolving the first reference (4 March), before any
new reference XML/raster reads or AS-102 cache writes. The unchanged
`resolve_optical_source` / `match_and_resolve` requires exactly one observation
match by acquisition + platform + MGRS tile + relative orbit. The PC catalog now
returns **two** products matching those fields for tile 40RBN. A subsequent
metadata-only query confirmed the duplication; no signed asset URL was needed.

| PC product | Acquisition UTC | Tile/orbit | Baseline | Generation UTC |
|---|---|---|---|---|
| `S2A_MSIL2A_20230304T064751_R020_T40RBN_20240819T072511` | 2023-03-04T06:47:51.024000Z | 40RBN / 20 | 05.10 | 2024-08-19T07:25:11.000000Z |
| `S2A_MSIL2A_20230304T064751_R020_T40RBN_20230304T113736` | 2023-03-04T06:47:51.024000Z | 40RBN / 20 | 05.09 | 2023-03-04T11:37:36.492429Z |

Both have platform Sentinel-2A and the exact `2023-03-04T06:47:51.024000Z`
acquisition. This is multiple processing products, not a timing-tolerance problem.
The additional two returned items cover 39RZH and are not target-tile references.
The matcher raises `ObservationMatchError` because exactly-one-match fails. We
confirmed the ambiguity without changing upstream code, injecting filtered catalog
responses into AS-102, selecting a preferred product through a workaround, mixing
baselines, or changing generic provenance. No remaining reference was processed.

### Reused target evidence and unavailable temporal evidence

The existing verified AS-102 target cache loaded and unchanged AS-103 extraction
succeeded in this attempt:

- Acquisition: `2023-04-28T06:46:29.024000+00:00`.
- Actual PC product: `S2B_MSIL2A_20230428T064629_R020_T40RBN_20230428T122311`.
- CDSE discovery product: `S2B_MSIL2A_20230428T064629_N0510_R020_T40RBN_20240831T052931`.
- AS-102 product: `optical:0725a908d21cd655e83f70d2bb11247dc0f1516f0c00ea275efc3239113ee4a6`.
- AS-103 product: `spectral:dae91b4dda0131ca2d2987321abd2ffd5c4b5ffb2e95a44880b7a5f9a67ea64b`.
- Grid: EPSG:32640, 20 m, 310 × 228; affine
  `[20,0,249020,0,-20,2707420]`; bounds `[249020,2702860,255220,2707420]`.
- Target valid-water pixels: **7,963**; target valid support **7,963 for each feature**.
- Successfully processed/selected real reference scenes: **0**.
- Real temporal per-pixel observation-count distributions, sufficient-history,
  zero-MAD/anomaly/rank counts and centre/scale/deviation/rank/anomaly summaries:
  **NOT PRODUCED**. Unprocessed historical support is unknown, not measured zero.
- Real AS-104 semantic fingerprints/product ID and multi-parent lineage:
  **NOT PRODUCED**.
- Independent temporal scalar checks at predeclared `(4,195)`, `(70,228)`, `(170,7)`,
  `(30,302)`: **NOT RUN**, historical inputs blocked.
- Real deterministic repeat and later-real-scene causal check: **NOT RUN**.
  Equivalent offline tests passed; those are not real acceptance substitutes.

The target's existing actual-PC → AS-102 → AS-103 lineage remains available in
[AS-103 evidence](AS_103_SPECTRAL_FEATURES_VALIDATION.md). No new AS-104 multi-scene
lineage or scientific result is claimed. No AS-104 rasters/cache were persisted.

### Required owner review before another real attempt

The pure AS-104 implementation is available for code/science review, but real
multi-scene acceptance remains blocked by AS-102's provider-product ambiguity.
A separately authorized upstream investigation would be needed to decide whether
explicit delivered-product/baseline selection belongs in discovery/raster matching.
That policy change is outside this task. Do not weaken exactly-one-match, change
AS-102 or widen the reference experiment without owner authorization.

## 3. Future HAB / event scientific validation — NOT PERFORMED

No HAB/bloom confirmation, calibrated chlorophyll, species/toxins, water safety,
intake exposure, persistence, risk, alert, monitoring recommendation or warning
lead-time proof. March is not called normal water. April 28 is not called a HAB
from feature/temporal outputs. External reporting is context, not EO ground truth.
BOA is not aquatic Rrs; feature families remain dependent. Five observations is
not a significance guarantee and rank is not probability/confidence/severity.
Acquisition causality does not prove historical operational product availability.

## Reproduction and review state

Run existing `.venv/bin/python -m pytest -v`, `.venv/bin/python -m ruff check .`,
`git diff --check`. Offline tests never request EO data. For a future real retry,
use the fixed target/period/minimum above and unchanged workflows unless the owner
separately authorizes a provider-product selection change. No new dependencies.
Implementation/evidence remain uncommitted, unpushed and unmerged; no PR.
AS-105+ is unauthorized and unstarted. Preserve AS-101/102/103 historical records.

## 4. Decision 048 integration and resumed frozen acceptance — 9 October 2026

**Status:** Integration/preservation/offline PASS; real multi-scene acceptance
BLOCKED by asset signing. This later checkpoint supersedes current authorization
and blocker wording only; §§1–3 and their historical evidence remain unchanged.
It does not rewrite the original two-product ambiguity as an access failure.

### Safe integration and exact preservation

- Original branch: `feature/as-104-temporal-baseline`; original HEAD
  `c6accab2c5753734466a6375d1b3ce1762e99bed`.
- Verified fetched `origin/main` exactly `39f2aee90c727fc151886efbdea44daec0e3f9b4`,
  PR #10 merge; ff-only succeeded; branch HEAD now that exact merge commit.
- Recovery patch `/workspace/as104-before-pr10-integration.patch` (45,303 bytes)
  and untracked archive `/workspace/as104-before-pr10-untracked.tar.gz` (22,924 bytes)
  were created/verified before any stash/Git movement. Full 81-file tracked/nonignored
  SHA-256 inventory, separate ten-file AS-104 inventory and original status were saved
  outside the repository. No recovery artifact was removed.
- Safety stash `f93950aab6fdfb40bb100158915ef12692aa1665` retains five tracked
  changes plus all ten untracked AS-104 files; all matched their saved hashes.
  `git stash apply` used, never pop; stash remains available.
- Four genuine documentation conflicts (Decisions, State, Handoff, Journal)
  were resolved. The evidence index auto-merged and its historical entries were
  ordered. No temporal source/test conflict, algorithm rewrite or regeneration.
- Both histories are present exactly once and in order: Decisions 046→047→048;
  M18→M19→M20; E17→E18→E19→E20; EV-021→EV-022→EV-023→EV-024.
  Original full bodies/rows and statuses were checked against the retained stash
  and merged HEAD. New later record: M21/E21/EV-025. No renumbering.
- All ten restored AS-104 files were byte-identical before evidence updates.
  Only the two plan/evidence documents subsequently gained current evidence;
  all eight source/test files remain unchanged:

| File | SHA-256 before and after |
|---|---|
| `src/aquasentinel/temporal/__init__.py` | `c2ba06ea2a457848f6659e406a8b2f36e614dcd10d8be0ab362df5d4ed8e330b` |
| `src/aquasentinel/temporal/baseline.py` | `55279b51e16c5a0bb7da6b4f7aa055fcc28dcb8461dee46ece64ccd43a43af9a` |
| `src/aquasentinel/temporal/models.py` | `acaee500c3c1447c40ab99d3bf837282ef0ab8f7578665b21aa21756585edd74` |
| `tests/temporal/__init__.py` | `bdb7f37d54dad7051a304852e9941e8eaa7efcb147d80b3c2fcf79c5231a83a1` |
| `tests/temporal/conftest.py` | `14506b87f2cf728ed18fa51dece0ada536499bd1c67140ad6b13ac0ceb38a551` |
| `tests/temporal/test_baseline.py` | `f04044a20d7b8d00b4bec26b94ba3869639e42e68116b8c657be8f55a8f20146` |
| `tests/temporal/test_identity_lineage.py` | `dc7879e2e531be0b8c4d9d69ae756ab87ee25a8d640e49427ee3582ad82d328d` |
| `tests/temporal/test_models.py` | `170ec17b532fdc21a666b81962bd2dfbc6a9fb4e5f8becb833e413bbc715f487` |

Combined offline gate **before real work**: 533 passed in 14.29s, Ruff
`All checks passed!`, `git diff --check` passed. Six unchanged Rasterio
PendingDeprecationWarnings in `rasterio/windows.py` lines 360/361; no new warning
category. This is local validation; no GitHub CI-success claim.

### Frozen experiment and exact attempts

Delivered PC baseline is **05.09**; all resolution/preprocessing/cache calls use
`required_processing_baseline="05.09"`. Target is April 28; March 1 inclusive–
April 1 exclusive UTC references; exactly five predeclared acquisitions;
`minimum_observations=5`. No wider dates, replacement scene, mixing baselines,
minimum reduction, relaxed masks, spatial filling, imputation, epsilon or fallback.

| Attempt | Start UTC | End UTC | Start Asia/Dubai (+04:00) | End Asia/Dubai (+04:00) | Observed stop |
|---|---|---|---|---|---|
| 1 | 2026-10-09T05:26:31.801976+00:00 | 2026-10-09T05:26:58.193521+00:00 | 2026-10-09T09:26:31.801976+04:00 | 2026-10-09T09:26:58.193521+04:00 | March 4 SCL signing; no completed reference |
| 2 | 2026-10-09T05:28:22.060551+00:00 | 2026-10-09T05:28:50.784014+00:00 | 2026-10-09T09:28:22.060551+04:00 | 2026-10-09T09:28:50.784014+04:00 | March 4 reflectance-band signing after SCL access; no completed reference |
| 3 | 2026-10-09T05:30:33.168331+00:00 | 2026-10-09T05:31:05.514348+00:00 | 2026-10-09T09:30:33.168331+04:00 | 2026-10-09T09:31:05.514348+04:00 | March 4 B02 signing after SCL access; five attempts exhausted; no completed reference |

Each attempt loaded/validated the accepted target cache and recomputed the same
AS-103 target, then freshly rediscovered **44 CDSE candidates**. March 4 strict
identity + explicit 05.09 resolved the exact expected product before asset
access. Its XML signing/read/decoding succeeded; attempt 2 and attempt 3 also
read native SCL. No completed March AS-102 scene, cache manifest or AS-103 product
was produced. No full tile was downloaded; reads remained the existing bounded
AOI windows. The signing failure prevented remaining references from being tried.

A bounded diagnostic on the same March 4 B02/SCL references observed three HTTP
200 successes and one HTTP 504; other direct requests also returned valid signed
identities. Only statuses/identity booleans were printed; SAS strings were not
logged/persisted. This supports intermittent signing access, not permanent
availability. No claim that every failed attempt returned 504: sanitized project
exceptions do not preserve individual transport statuses.

The third attempt used an **external scratch-harness-only** bounded retry:
maximum five attempts of the same audited signer on the same unsigned asset;
1/2/4/4-second delays, unchanged validation and settings. Five failures occurred
at one B02 signing call and no successful retry was recorded. No project source
or configuration changed. This is transport retry evidence, not a revised
selection/masking/math policy. Raw provider errors and SAS values were suppressed.

### Observation products: predeclared versus actually completed

| Acquisition UTC | Platform | Predeclared actual-PC product at required 05.09 | This resumed run |
|---|---|---|---|
| 2023-03-04T06:47:51.024+00:00 | sentinel-2a | `S2A_MSIL2A_20230304T064751_R020_T40RBN_20230304T113736` | Resolved at 05.09; preprocessing stopped, no derived IDs |
| 2023-03-09T06:47:19.025+00:00 | sentinel-2b | `S2B_MSIL2A_20230309T064719_R020_T40RBN_20230309T121958` | Frozen expected product; not reached in this resumed run |
| 2023-03-14T06:46:41.024+00:00 | sentinel-2a | `S2A_MSIL2A_20230314T064641_R020_T40RBN_20230314T123741` | Frozen expected product; not reached in this resumed run |
| 2023-03-24T06:46:21.024+00:00 | sentinel-2a | `S2A_MSIL2A_20230324T064621_R020_T40RBN_20230324T114938` | Frozen expected product; not reached in this resumed run |
| 2023-03-29T06:46:29.024+00:00 | sentinel-2b | `S2B_MSIL2A_20230329T064629_R020_T40RBN_20230329T132334` | Frozen expected product; not reached in this resumed run |
| 2023-04-28T06:46:29.024000+00:00 | sentinel-2b | `S2B_MSIL2A_20230428T064629_R020_T40RBN_20230428T122311` | Accepted cache loaded and AS-103 regenerated |

All products have tile 40RBN / relative orbit 20. Earlier EV-024 established six
metadata-only 05.09 resolutions; that earlier result is distinct from this run's
completed raster/derived-product evidence. No successful processing is inferred
for the four March dates not reached. The full six-PC product set is **not yet
used by AS-104**.

### Actually available scene support, identity and lineage

Only the target has a completed AS-102/AS-103 pair in the resumed experiment:

- **acquired_at:** `2023-04-28T06:46:29.024000+00:00`.
- **platform:** `sentinel-2b`.
- **tile:** `40RBN`.
- **relative_orbit:** `20`.
- **pc_product:** `S2B_MSIL2A_20230428T064629_R020_T40RBN_20230428T122311`.
- **processing_baseline:** `05.09`.
- **generation_time:** `2023-04-28T12:23:11.362052Z`.
- **cache_id:** `0725a908d21cd655e83f70d2bb11247dc0f1516f0c00ea275efc3239113ee4a6`.
- **as102_product_id:** `optical:0725a908d21cd655e83f70d2bb11247dc0f1516f0c00ea275efc3239113ee4a6`.
- **as103_product_id:** `spectral:dae91b4dda0131ca2d2987321abd2ffd5c4b5ffb2e95a44880b7a5f9a67ea64b`.

Grid: EPSG:32640, 20 m, width 310 × height 228; transform
[20,0,249020,0,-20,2707420], bounds [249020,2702860,255220,2707420].
AOI 67,449; valid-data 65,166; candidate water 10,211; valid water/support 7,963;
valid-water/AOI 0.11805957093507688; retained candidate water 0.7798452649103907.
All six features have 7,963 valid pixels / 100% parent-water support.
Each reference's valid-water/support statistics and AS-102/103 IDs are **not
produced**, rather than measured as zero.

Actual target lineage (separate CDSE discovery context remains in AS-102 identity):

```text
stac:ef177b34b0fa3cabbb6d613d65f1c55d8ea4c5959326bb8896ec51d111792740:sentinel-2-l2a:S2B_MSIL2A_20230428T064629_R020_T40RBN_20230428T122311
→ optical:0725a908d21cd655e83f70d2bb11247dc0f1516f0c00ea275efc3239113ee4a6
→ spectral:dae91b4dda0131ca2d2987321abd2ffd5c4b5ffb2e95a44880b7a5f9a67ea64b
```

No real AS-104 derived product exists, so no six-parent lineage or selected-parent
order is observed. The frozen expected order remains target AS-103 first, then
March 4, 9, 14, 24, 29 AS-103 parents chronologically. Reference IDs are unknown.

### Requested real temporal validation — NOT PRODUCED / NOT RUN

For all six features (ndci_like, mci_like, red_edge_red_ratio,
red_edge2_red_ratio, green_red_ratio, green_blue_ratio), history-count distributions,
insufficient/sufficient-history and numeric-rejection counts, zero-MAD counts,
valid anomaly/rank counts and centre/scale/deviation/anomaly/rank summaries are
**not produced**. No temporal target/reference semantic fingerprints, temporal
product ID, real scalar values or anomaly arrays exist. The experiment stopped
before `compute_temporal_anomaly`.

Independent scalar checks, real future-scene addition/mutation and deterministic
real temporal repeat are **NOT RUN**. Their offline tests pass; this does not
replace the requested real-product checks. Fixed predeclared coordinates were
(4,195), (70,228), (170,7), (30,302). A support-only row-major fallback rule was
recorded before reads, but never used and no pixels were selected by values.
No later scene was processed for the causal check.

This failure does not establish sparse/empty support or zero MAD. If the unchanged
experiment later reaches those outcomes, report them without altering minimum,
period, masks or numerical policy. JSON reports use `allow_nan=False`; unavailable
values stay absent/null, never JSON NaN.

### Cache and security preservation

Accepted target cache remains unchanged and ignored by Git:

| File | SHA-256, unchanged |
|---|---|
| `arrays.npz` | `01512aa7ec3e1deab0f87fddb9c3888986d449ebcdd440830a7d4805bbc4f4a1` |
| `manifest.json` | `9a5ca8d78b663426fd53732a52db387c15fe8a70acb2da93978a9f466ce15589` |

No credentials/SAS/signed URLs, raw scenes or generated caches added to repository
changes. Transport diagnostics retained only sanitized exception types/local
frame positions and HTTP statuses. Local scratch artifacts (not durable project
inputs): `/tmp/as104-resumed-acceptance{,-attempt2,-attempt3}.json` and corresponding
logs/scripts; the original `/tmp/as104-acceptance.json` was not overwritten.

### Limits and exact next step

Real acceptance is **BLOCKED** by the existing signing service; source ambiguity
is addressed by merged Decision 048. No algorithm change is justified by this
access failure. Retry the identical frozen 05.09 experiment when signing works,
then complete scalar, real causal and repeatability checks and per-feature
support evidence before claiming real temporal acceptance.

No HAB/bloom, calibrated chlorophyll, species/toxin, safety, intake-risk,
persistence, alert, warning-lead-time or probability/confidence claim. BOA is not
aquatic Rrs; five observations do not establish significance; March is not asserted
normal. Positive is not dangerous, negative is not safe.

**P1 Processing Baseline Robustness Experiment — NOT STARTED**: homogeneous
05.09 versus 05.10 requires a homogeneous target/reference set and separate
owner authorization; it is not accuracy validation. AS-105+ NOT authorized/started.
No commit/push/PR. Retain safety stash and external backups for owner review.

### Final quality and review gate after resumed-evidence updates

- `python -m pytest -v`: **533 passed, 6 warnings in 15.23s**.
- `python -m ruff check .`: **All checks passed!**
- `git diff --check`: passed; all ten untracked AS-104 files separately checked
  against `/dev/null` with no whitespace errors.
- All eight temporal source/test SHA-256 values remain identical; original
  M01–M20, E18–E20 and EV-001–EV-024 bodies/rows remain preserved as verified
  above. No unresolved conflicts or staged changes; exactly the original fifteen
  AS-104 paths are changed/untracked relative to merged HEAD. No AS-102/103 source,
  generic provenance, config, dependencies, algorithm or cache-schema diff.
- Working tree intentionally dirty for owner review; HEAD remains exact PR #10
  merge. Safety stash/recovery artifacts remain available. No commit/push/PR,
  AS-105+ or homogeneous-05.10 robustness experiment.

## 5. PR #11 integration and five-reference 05.09 attempt — 9 October 2026

**M23 / E23 / EV-027 — BLOCKED at AS-104 target provenance validation.**
The prior ambiguity and signing checkpoints (§§3–4) retain their original facts,
counts and statuses; this is a later experiment, not a rewritten success claim.

### Preservation and integration

New verified external binary diff, ten-file untracked archive and 83-file SHA-256
inventory were created before mutation. A second stash was retained, not popped;
ff-only integration reached exact PR #11 main, then the new stash was applied.
Four genuine documentation conflicts were reconciled. Temporal source/tests are
byte-identical; two AS-104 documentation files changed only for current evidence.
Decisions 046→047→048→049, M18→M19→M20→M21→M22, E17→E18→E19→E20→E21→E22 and
EV-021→EV-022→EV-023→EV-024→EV-025→EV-026 are present in order without renumbering
or duplicate bodies. Decision 048's existing later integration note is retained.

### Frozen experiment and direct result

Exactly five predeclared March references, April 28 target, UTC March 1 inclusive
through April 1 exclusive, minimum five, actual PC baseline 05.09 for every
candidate. No fallback or extra future scene; normal merged production transport,
no custom retries/instrumentation and no algorithm/dependency/config changes.
All five March AS-102/103 scenes completed on the same EPSG:32640 310×228, 20 m
grid. New AOI caches are ignored, not staged; accepted April arrays/manifest
remain unchanged. All six AS-103 feature arrays retain their feature-specific
support; valid scene count does not imply five observations at a target pixel.

The AS-104 call raised the sanitized literal project message:
`Selected scene has unresolved or inconsistent upstream provenance.`
Read-only offline diagnosis using the six known caches traced it to the target
platform guard at `src/aquasentinel/temporal/baseline.py:105–110`:
`observation_match.platform` is `sentinel-2b`, actual PC `SourceRecord.platform`
is `Sentinel-2B`; all three acquisition times agree. Corresponding case differences
exist for each reference. The upstream data representations identify the same
platform; the unchanged implementation compares them case-sensitively. No source
record/cache/temporal code was changed and no alternate calculation bypassed the
guard. This is a metadata-representation validation blocker, not transport failure
or evidence of zero temporal support.

### Unavailable temporal evidence

No successful TemporalFeatureScene was returned, so temporal history counts,
insufficient/zero-MAD/z/rank counts, centre/scale/deviation/z/rank summaries,
AS-104 fingerprints/ID/provenance are **NOT PRODUCED**, not numeric zeros.
The first/middle/last row-major supported-pixel scalar rule and tolerances were
predeclared in the external harness before reads; scalar checks were not reached.
The planned synthetic future-date control (clearly not a real future observation)
and deterministic repeat were also not reached. No future raster was processed.

### Complete safe integration, scene evidence and blocker diagnosis

The following contains exact times, product IDs, grids, per-band/all-band support,
all six features' counts/statistics/diagnostics, AS-103 input-content fingerprints
and PC→AS-102→AS-103 edges for all six real scenes. It contains no raster arrays,
signed HREFs, tokens or JSON NaN. AS-104 role-specific/combined fingerprints are
absent because validation stopped before snapshotting/reduction/identity output.

```json
{
  "integration": {
    "new_backups": [
      "/workspace/as104-before-pr11-integration.patch",
      "/workspace/as104-before-pr11-untracked.tar.gz",
      "/workspace/as104-before-pr11-sha256.json"
    ],
    "old_stash": "f93950aab6fdfb40bb100158915ef12692aa1665",
    "new_stash": "d979a433a5ab8ae600282048f184eb5fd06a8f17",
    "pre_integration_branch": "feature/as-104-temporal-baseline",
    "pre_integration_head": "39f2aee90c727fc151886efbdea44daec0e3f9b4",
    "post_ff_head": "2006df7a70a4f48c66933aed96f4464d8d03084e",
    "conflicts_resolved": [
      "docs/HANDOFF.md",
      "docs/PROJECT_STATE.md",
      "docs/PRESENTATION_JOURNAL.md",
      "docs/evidence/PRESENTATION_EVIDENCE_INDEX.md"
    ],
    "temporal_source_test_preserved_hashes": {
      "src/aquasentinel/temporal/__init__.py": "c2ba06ea2a457848f6659e406a8b2f36e614dcd10d8be0ab362df5d4ed8e330b",
      "src/aquasentinel/temporal/baseline.py": "55279b51e16c5a0bb7da6b4f7aa055fcc28dcb8461dee46ece64ccd43a43af9a",
      "src/aquasentinel/temporal/models.py": "acaee500c3c1447c40ab99d3bf837282ef0ab8f7578665b21aa21756585edd74",
      "tests/temporal/__init__.py": "bdb7f37d54dad7051a304852e9941e8eaa7efcb147d80b3c2fcf79c5231a83a1",
      "tests/temporal/conftest.py": "14506b87f2cf728ed18fa51dece0ada536499bd1c67140ad6b13ac0ceb38a551",
      "tests/temporal/test_baseline.py": "f04044a20d7b8d00b4bec26b94ba3869639e42e68116b8c657be8f55a8f20146",
      "tests/temporal/test_identity_lineage.py": "dc7879e2e531be0b8c4d9d69ae756ab87ee25a8d640e49427ee3582ad82d328d",
      "tests/temporal/test_models.py": "170ec17b532fdc21a666b81962bd2dfbc6a9fb4e5f8becb833e413bbc715f487"
    },
    "accepted_target_cache_hashes": {
      "data/cache/as102/0725a908d21cd655e83f70d2bb11247dc0f1516f0c00ea275efc3239113ee4a6/arrays.npz": "01512aa7ec3e1deab0f87fddb9c3888986d449ebcdd440830a7d4805bbc4f4a1",
      "data/cache/as102/0725a908d21cd655e83f70d2bb11247dc0f1516f0c00ea275efc3239113ee4a6/manifest.json": "9a5ca8d78b663426fd53732a52db387c15fe8a70acb2da93978a9f466ce15589"
    },
    "combined_offline_gate": {
      "pytest_passed": 643,
      "pytest_seconds": 15.92,
      "warnings": 6,
      "ruff": "PASS",
      "tracked_and_untracked_diff": "PASS"
    },
    "production_transport_instrumentation_or_overrides": false,
    "as104_unavailable_results": [
      "selected output parent order",
      "per-feature history distribution/diagnostics",
      "centre/scale/deviation/z/rank summaries",
      "AS-104 input/output semantic fingerprints",
      "combined temporal fingerprint",
      "temporal product ID/provenance",
      "independent scalar checks",
      "future-scene exclusion",
      "deterministic repeat"
    ],
    "next_review": "Targeted platform representation normalization and realistic metadata regression fixture; do not mutate raw source/provenance or accepted caches; no fix authorized by this attempt."
  },
  "real_attempt": {
    "status": "BLOCKED",
    "started_utc": "2026-10-09T07:31:08.630215+00:00",
    "integration_base": "2006df7a70a4f48c66933aed96f4464d8d03084e",
    "required_processing_baseline": "05.09",
    "reference_start": "2023-03-01T00:00:00+00:00",
    "reference_end": "2023-04-01T00:00:00+00:00",
    "minimum_observations": 5,
    "expected_reference_products": [
      [
        "2023-03-04T06:47:51.024+00:00",
        "S2A_MSIL2A_20230304T064751_R020_T40RBN_20230304T113736"
      ],
      [
        "2023-03-09T06:47:19.025+00:00",
        "S2B_MSIL2A_20230309T064719_R020_T40RBN_20230309T121958"
      ],
      [
        "2023-03-14T06:46:41.024+00:00",
        "S2A_MSIL2A_20230314T064641_R020_T40RBN_20230314T123741"
      ],
      [
        "2023-03-24T06:46:21.024+00:00",
        "S2A_MSIL2A_20230324T064621_R020_T40RBN_20230324T114938"
      ],
      [
        "2023-03-29T06:46:29.024+00:00",
        "S2B_MSIL2A_20230329T064629_R020_T40RBN_20230329T132334"
      ]
    ],
    "predeclared_scalar_rule": "For EACH feature independently: first, middle (index floor(N/2)), last row-major baseline-valid pixel; deduplicate. Selection uses support masks only, before inspecting magnitudes. If N=0, report no supported scalar checks and do not relax history.",
    "scalar_tolerance": {
      "centre_scale_deviation_rtol": 1e-14,
      "atol": 0,
      "rank_z": "exact equality after float32 cast"
    },
    "causal_control_plan": "Synthetic later-date scene cloned from accepted real target, acquisition 2023-05-03T06:46:29.024Z; model-valid feature identity, no alleged real future acquisition/source. Add, then mutate mci_like by float32 0.001 with updated summaries; excluded from registry and selected parents. No future raster processing.",
    "references": [
      {
        "acquired_at": "2023-03-04T06:47:51.024000+00:00",
        "platform": "sentinel-2a",
        "tile": "40RBN",
        "relative_orbit": 20,
        "discovery_product": "S2A_MSIL2A_20230304T064751_N0510_R020_T40RBN_20240819T072511",
        "discovery_source_id": "stac:727c9c270e50361fad55ba968c9f8e618dea21f690ff8ae24cfb77374ae151f7:sentinel-2-l2a:S2A_MSIL2A_20230304T064751_N0510_R020_T40RBN_20240819T072511",
        "pc_product": "S2A_MSIL2A_20230304T064751_R020_T40RBN_20230304T113736",
        "pc_source_id": "stac:ef177b34b0fa3cabbb6d613d65f1c55d8ea4c5959326bb8896ec51d111792740:sentinel-2-l2a:S2A_MSIL2A_20230304T064751_R020_T40RBN_20230304T113736",
        "processing_baseline": "05.09",
        "generation_time": "2023-03-04T11:37:36.492429Z",
        "cache_id": "038a425d46eead247826c4e1e735851a50325d896f1c95b99258840285bf31e1",
        "as102_product_id": "optical:038a425d46eead247826c4e1e735851a50325d896f1c95b99258840285bf31e1",
        "as103_product_id": "spectral:6409add4aef5c95cfe773bfabfa1f554bdda2968241712bda4debefa34b57130",
        "as103_input_content_fingerprint": "187251ea126ffdf774b5d347d2af23f7b693b5d947a7ed49e5d6c3cf694c0166",
        "as102_statistics": {
          "aoi_pixel_count": 67449,
          "valid_data_count": 66512,
          "candidate_water_count": 12765,
          "valid_water_count": 8674,
          "valid_water_fraction_of_aoi": 0.12860086880457827,
          "water_retained_fraction": 0.6795142969056013
        },
        "grid": {
          "crs": "EPSG:32640",
          "transform": [
            20.0,
            0.0,
            249020.0,
            0.0,
            -20.0,
            2707420.0
          ],
          "width": 310,
          "height": 228,
          "resolution": 20.0,
          "bounds": [
            249020.0,
            2702860.0,
            255220.0,
            2707420.0
          ],
          "grid_id": "88d76cf6265d9e0fa2802ed26324c02275e74721d4eb5b597cc9884a6d27aeec"
        },
        "water_support_counts_by_band": {
          "B02": 9562,
          "B03": 9562,
          "B04": 9282,
          "B05": 9562,
          "B06": 9562,
          "B07": 9562,
          "B08": 8952,
          "B8A": 9562,
          "B11": 9562
        },
        "all_band_intersection_support_in_aoi": 8674,
        "feature_statistics": {
          "ndci_like": {
            "valid_count": 8622,
            "valid_fraction_of_parent_water": 0.9940050726308508,
            "minimum": -45.373287200927734,
            "maximum": 41.66667938232422,
            "p05": -2.215840220451355,
            "median": -0.16000819951295853,
            "p95": 2.0129797220230103
          },
          "mci_like": {
            "valid_count": 8674,
            "valid_fraction_of_parent_water": 1.0,
            "minimum": -0.021573437377810478,
            "maximum": 0.09499646723270416,
            "p05": -0.0011412450287025422,
            "median": 0.0009099474118556827,
            "p95": 0.03293588943779469
          },
          "red_edge_red_ratio": {
            "valid_count": 8622,
            "valid_fraction_of_parent_water": 0.9940050726308508,
            "minimum": -34.39999771118164,
            "maximum": 49.23076629638672,
            "p05": -1.9348527252674101,
            "median": 0.6407720148563385,
            "p95": 3.124271631240844
          },
          "red_edge2_red_ratio": {
            "valid_count": 8622,
            "valid_fraction_of_parent_water": 0.9940050726308508,
            "minimum": -62.45783233642578,
            "maximum": 82.82352447509766,
            "p05": -5.270449185371399,
            "median": -0.010533556342124939,
            "p95": 5.479336762428282
          },
          "green_red_ratio": {
            "valid_count": 8622,
            "valid_fraction_of_parent_water": 0.9940050726308508,
            "minimum": -322.3600158691406,
            "maximum": 331.8125,
            "p05": -18.99515037536621,
            "median": 3.888427495956421,
            "p95": 25.236266326904286
          },
          "green_blue_ratio": {
            "valid_count": 8674,
            "valid_fraction_of_parent_water": 1.0,
            "minimum": 0.9599862694740295,
            "maximum": 2.525851249694824,
            "p05": 1.1395424127578735,
            "median": 1.3727585077285767,
            "p95": 1.9724581122398377
          }
        },
        "feature_diagnostics": {
          "ndci_like": {
            "parent_valid_water_count": 8674,
            "negative_required_input_count": 2778,
            "denominator_rejection_count": 52,
            "negative_denominator_count": 1841,
            "nonfinite_result_rejection_count": 0,
            "out_of_nominal_range_count": 1672
          },
          "mci_like": {
            "parent_valid_water_count": 8674,
            "negative_required_input_count": 5569,
            "denominator_rejection_count": 0,
            "negative_denominator_count": 0,
            "nonfinite_result_rejection_count": 0,
            "out_of_nominal_range_count": null
          },
          "red_edge_red_ratio": {
            "parent_valid_water_count": 8674,
            "negative_required_input_count": 2778,
            "denominator_rejection_count": 52,
            "negative_denominator_count": 1053,
            "nonfinite_result_rejection_count": 0,
            "out_of_nominal_range_count": null
          },
          "red_edge2_red_ratio": {
            "parent_valid_water_count": 8674,
            "negative_required_input_count": 5565,
            "denominator_rejection_count": 52,
            "negative_denominator_count": 1053,
            "nonfinite_result_rejection_count": 0,
            "out_of_nominal_range_count": null
          },
          "green_red_ratio": {
            "parent_valid_water_count": 8674,
            "negative_required_input_count": 1053,
            "denominator_rejection_count": 52,
            "negative_denominator_count": 1053,
            "nonfinite_result_rejection_count": 0,
            "out_of_nominal_range_count": null
          },
          "green_blue_ratio": {
            "parent_valid_water_count": 8674,
            "negative_required_input_count": 0,
            "denominator_rejection_count": 0,
            "negative_denominator_count": 0,
            "nonfinite_result_rejection_count": 0,
            "out_of_nominal_range_count": null
          }
        },
        "lineage_edges": [
          [
            "stac:ef177b34b0fa3cabbb6d613d65f1c55d8ea4c5959326bb8896ec51d111792740:sentinel-2-l2a:S2A_MSIL2A_20230304T064751_R020_T40RBN_20230304T113736",
            "optical:038a425d46eead247826c4e1e735851a50325d896f1c95b99258840285bf31e1"
          ],
          [
            "optical:038a425d46eead247826c4e1e735851a50325d896f1c95b99258840285bf31e1",
            "spectral:6409add4aef5c95cfe773bfabfa1f554bdda2968241712bda4debefa34b57130"
          ]
        ]
      },
      {
        "acquired_at": "2023-03-09T06:47:19.025000+00:00",
        "platform": "sentinel-2b",
        "tile": "40RBN",
        "relative_orbit": 20,
        "discovery_product": "S2B_MSIL2A_20230309T064719_N0510_R020_T40RBN_20240823T054455",
        "discovery_source_id": "stac:727c9c270e50361fad55ba968c9f8e618dea21f690ff8ae24cfb77374ae151f7:sentinel-2-l2a:S2B_MSIL2A_20230309T064719_N0510_R020_T40RBN_20240823T054455",
        "pc_product": "S2B_MSIL2A_20230309T064719_R020_T40RBN_20230309T121958",
        "pc_source_id": "stac:ef177b34b0fa3cabbb6d613d65f1c55d8ea4c5959326bb8896ec51d111792740:sentinel-2-l2a:S2B_MSIL2A_20230309T064719_R020_T40RBN_20230309T121958",
        "processing_baseline": "05.09",
        "generation_time": "2023-03-09T12:19:58.419331Z",
        "cache_id": "a412b51188a9c47a0f121a5882fbf464490a66d19a96d3f682c0955398193644",
        "as102_product_id": "optical:a412b51188a9c47a0f121a5882fbf464490a66d19a96d3f682c0955398193644",
        "as103_product_id": "spectral:dafde3d3a2a94d44b62a9d5605bce497b03021e517b7dd6b081607719f37efa1",
        "as103_input_content_fingerprint": "0a61a0afa5254da8959d38135d967d664debfa45b8aea4f3070608dd8dd198b8",
        "as102_statistics": {
          "aoi_pixel_count": 67449,
          "valid_data_count": 43880,
          "candidate_water_count": 3173,
          "valid_water_count": 2092,
          "valid_water_fraction_of_aoi": 0.031016026924046317,
          "water_retained_fraction": 0.6593129530412859
        },
        "grid": {
          "crs": "EPSG:32640",
          "transform": [
            20.0,
            0.0,
            249020.0,
            0.0,
            -20.0,
            2707420.0
          ],
          "width": 310,
          "height": 228,
          "resolution": 20.0,
          "bounds": [
            249020.0,
            2702860.0,
            255220.0,
            2707420.0
          ],
          "grid_id": "88d76cf6265d9e0fa2802ed26324c02275e74721d4eb5b597cc9884a6d27aeec"
        },
        "water_support_counts_by_band": {
          "B02": 2092,
          "B03": 2092,
          "B04": 2092,
          "B05": 2092,
          "B06": 2092,
          "B07": 2092,
          "B08": 2092,
          "B8A": 2092,
          "B11": 2092
        },
        "all_band_intersection_support_in_aoi": 2092,
        "feature_statistics": {
          "ndci_like": {
            "valid_count": 2092,
            "valid_fraction_of_parent_water": 1.0,
            "minimum": -0.4478992223739624,
            "maximum": 0.17207765579223633,
            "p05": -0.21359404399991036,
            "median": -0.1569993868470192,
            "p95": 0.11689317971467969
          },
          "mci_like": {
            "valid_count": 2092,
            "valid_fraction_of_parent_water": 1.0,
            "minimum": -0.0063513522036373615,
            "maximum": 0.08753521740436554,
            "p05": -0.0004854009326663799,
            "median": 0.0029848956037312746,
            "p95": 0.07805229648947715
          },
          "red_edge_red_ratio": {
            "valid_count": 2092,
            "valid_fraction_of_parent_water": 1.0,
            "minimum": 0.3813116252422333,
            "maximum": 1.4156855344772339,
            "p05": 0.6479975312948227,
            "median": 0.7286093831062317,
            "p95": 1.264731729030609
          },
          "red_edge2_red_ratio": {
            "valid_count": 2092,
            "valid_fraction_of_parent_water": 1.0,
            "minimum": 0.13675212860107422,
            "maximum": 1.5279388427734375,
            "p05": 0.2618812873959541,
            "median": 0.3568938672542572,
            "p95": 0.9074863225221629
          },
          "green_red_ratio": {
            "valid_count": 2092,
            "valid_fraction_of_parent_water": 1.0,
            "minimum": 0.8577972054481506,
            "maximum": 2.924053192138672,
            "p05": 1.0898411691188812,
            "median": 2.487278938293457,
            "p95": 2.733928048610687
          },
          "green_blue_ratio": {
            "valid_count": 2092,
            "valid_fraction_of_parent_water": 1.0,
            "minimum": 1.0766685009002686,
            "maximum": 1.4821453094482422,
            "p05": 1.140370148420334,
            "median": 1.252089262008667,
            "p95": 1.3313563406467437
          }
        },
        "feature_diagnostics": {
          "ndci_like": {
            "parent_valid_water_count": 2092,
            "negative_required_input_count": 0,
            "denominator_rejection_count": 0,
            "negative_denominator_count": 0,
            "nonfinite_result_rejection_count": 0,
            "out_of_nominal_range_count": 0
          },
          "mci_like": {
            "parent_valid_water_count": 2092,
            "negative_required_input_count": 0,
            "denominator_rejection_count": 0,
            "negative_denominator_count": 0,
            "nonfinite_result_rejection_count": 0,
            "out_of_nominal_range_count": null
          },
          "red_edge_red_ratio": {
            "parent_valid_water_count": 2092,
            "negative_required_input_count": 0,
            "denominator_rejection_count": 0,
            "negative_denominator_count": 0,
            "nonfinite_result_rejection_count": 0,
            "out_of_nominal_range_count": null
          },
          "red_edge2_red_ratio": {
            "parent_valid_water_count": 2092,
            "negative_required_input_count": 0,
            "denominator_rejection_count": 0,
            "negative_denominator_count": 0,
            "nonfinite_result_rejection_count": 0,
            "out_of_nominal_range_count": null
          },
          "green_red_ratio": {
            "parent_valid_water_count": 2092,
            "negative_required_input_count": 0,
            "denominator_rejection_count": 0,
            "negative_denominator_count": 0,
            "nonfinite_result_rejection_count": 0,
            "out_of_nominal_range_count": null
          },
          "green_blue_ratio": {
            "parent_valid_water_count": 2092,
            "negative_required_input_count": 0,
            "denominator_rejection_count": 0,
            "negative_denominator_count": 0,
            "nonfinite_result_rejection_count": 0,
            "out_of_nominal_range_count": null
          }
        },
        "lineage_edges": [
          [
            "stac:ef177b34b0fa3cabbb6d613d65f1c55d8ea4c5959326bb8896ec51d111792740:sentinel-2-l2a:S2B_MSIL2A_20230309T064719_R020_T40RBN_20230309T121958",
            "optical:a412b51188a9c47a0f121a5882fbf464490a66d19a96d3f682c0955398193644"
          ],
          [
            "optical:a412b51188a9c47a0f121a5882fbf464490a66d19a96d3f682c0955398193644",
            "spectral:dafde3d3a2a94d44b62a9d5605bce497b03021e517b7dd6b081607719f37efa1"
          ]
        ]
      },
      {
        "acquired_at": "2023-03-14T06:46:41.024000+00:00",
        "platform": "sentinel-2a",
        "tile": "40RBN",
        "relative_orbit": 20,
        "discovery_product": "S2A_MSIL2A_20230314T064641_N0510_R020_T40RBN_20240823T041506",
        "discovery_source_id": "stac:727c9c270e50361fad55ba968c9f8e618dea21f690ff8ae24cfb77374ae151f7:sentinel-2-l2a:S2A_MSIL2A_20230314T064641_N0510_R020_T40RBN_20240823T041506",
        "pc_product": "S2A_MSIL2A_20230314T064641_R020_T40RBN_20230314T123741",
        "pc_source_id": "stac:ef177b34b0fa3cabbb6d613d65f1c55d8ea4c5959326bb8896ec51d111792740:sentinel-2-l2a:S2A_MSIL2A_20230314T064641_R020_T40RBN_20230314T123741",
        "processing_baseline": "05.09",
        "generation_time": "2023-03-14T12:37:41.653527Z",
        "cache_id": "91cd94459703fb64b6c982d0d61403dcea8e766a99796b01d591d9ab6b9a67c2",
        "as102_product_id": "optical:91cd94459703fb64b6c982d0d61403dcea8e766a99796b01d591d9ab6b9a67c2",
        "as103_product_id": "spectral:721d847a7ed032426c8124e42507b60c3f9a6ae86a4e9ad406176646c35abff7",
        "as103_input_content_fingerprint": "89311bd86000b4c7a60e1839040022d64c5a45715e3c5fc3a5392c6bc9592462",
        "as102_statistics": {
          "aoi_pixel_count": 67449,
          "valid_data_count": 65948,
          "candidate_water_count": 10231,
          "valid_water_count": 7350,
          "valid_water_fraction_of_aoi": 0.10897122270159676,
          "water_retained_fraction": 0.7184048480109472
        },
        "grid": {
          "crs": "EPSG:32640",
          "transform": [
            20.0,
            0.0,
            249020.0,
            0.0,
            -20.0,
            2707420.0
          ],
          "width": 310,
          "height": 228,
          "resolution": 20.0,
          "bounds": [
            249020.0,
            2702860.0,
            255220.0,
            2707420.0
          ],
          "grid_id": "88d76cf6265d9e0fa2802ed26324c02275e74721d4eb5b597cc9884a6d27aeec"
        },
        "water_support_counts_by_band": {
          "B02": 7523,
          "B03": 7497,
          "B04": 7602,
          "B05": 7612,
          "B06": 7583,
          "B07": 7612,
          "B08": 7593,
          "B8A": 7612,
          "B11": 7612
        },
        "all_band_intersection_support_in_aoi": 7350,
        "feature_statistics": {
          "ndci_like": {
            "valid_count": 7350,
            "valid_fraction_of_parent_water": 1.0,
            "minimum": -10.058127403259277,
            "maximum": 29.228784561157227,
            "p05": 0.016581308655440812,
            "median": 0.09092830121517181,
            "p95": 0.20740841776132574
          },
          "mci_like": {
            "valid_count": 7350,
            "valid_fraction_of_parent_water": 1.0,
            "minimum": -0.019773438572883606,
            "maximum": 0.11635499447584152,
            "p05": -0.003755379968788475,
            "median": 0.0014121346175670624,
            "p95": 0.09187133535742759
          },
          "red_edge_red_ratio": {
            "valid_count": 7350,
            "valid_fraction_of_parent_water": 1.0,
            "minimum": -87.41450500488281,
            "maximum": 51.25545120239258,
            "p05": 1.0265063405036927,
            "median": 1.199103593826294,
            "p95": 1.509673631191253
          },
          "red_edge2_red_ratio": {
            "valid_count": 7350,
            "valid_fraction_of_parent_water": 1.0,
            "minimum": -211.45594787597656,
            "maximum": 124.39836120605469,
            "p05": -0.16308539956808088,
            "median": 1.3672099709510803,
            "p95": 1.986032766103742
          },
          "green_red_ratio": {
            "valid_count": 7350,
            "valid_fraction_of_parent_water": 1.0,
            "minimum": -163.76202392578125,
            "maximum": 289.89593505859375,
            "p05": -1.989084905385971,
            "median": -0.34662455320358276,
            "p95": 1.4881002187728882
          },
          "green_blue_ratio": {
            "valid_count": 7330,
            "valid_fraction_of_parent_water": 0.9972789115646259,
            "minimum": -279.1667175292969,
            "maximum": 226.9896240234375,
            "p05": -5.907708430290221,
            "median": 0.0869569405913353,
            "p95": 6.453824853897094
          }
        },
        "feature_diagnostics": {
          "ndci_like": {
            "parent_valid_water_count": 7350,
            "negative_required_input_count": 6071,
            "denominator_rejection_count": 0,
            "negative_denominator_count": 6052,
            "nonfinite_result_rejection_count": 0,
            "out_of_nominal_range_count": 45
          },
          "mci_like": {
            "parent_valid_water_count": 7350,
            "negative_required_input_count": 6557,
            "denominator_rejection_count": 0,
            "negative_denominator_count": 0,
            "nonfinite_result_rejection_count": 0,
            "out_of_nominal_range_count": null
          },
          "red_edge_red_ratio": {
            "parent_valid_water_count": 7350,
            "negative_required_input_count": 6071,
            "denominator_rejection_count": 0,
            "negative_denominator_count": 6028,
            "nonfinite_result_rejection_count": 0,
            "out_of_nominal_range_count": null
          },
          "red_edge2_red_ratio": {
            "parent_valid_water_count": 7350,
            "negative_required_input_count": 6557,
            "denominator_rejection_count": 0,
            "negative_denominator_count": 6028,
            "nonfinite_result_rejection_count": 0,
            "out_of_nominal_range_count": null
          },
          "green_red_ratio": {
            "parent_valid_water_count": 7350,
            "negative_required_input_count": 6028,
            "denominator_rejection_count": 0,
            "negative_denominator_count": 6028,
            "nonfinite_result_rejection_count": 0,
            "out_of_nominal_range_count": null
          },
          "green_blue_ratio": {
            "parent_valid_water_count": 7350,
            "negative_required_input_count": 4728,
            "denominator_rejection_count": 20,
            "negative_denominator_count": 4728,
            "nonfinite_result_rejection_count": 0,
            "out_of_nominal_range_count": null
          }
        },
        "lineage_edges": [
          [
            "stac:ef177b34b0fa3cabbb6d613d65f1c55d8ea4c5959326bb8896ec51d111792740:sentinel-2-l2a:S2A_MSIL2A_20230314T064641_R020_T40RBN_20230314T123741",
            "optical:91cd94459703fb64b6c982d0d61403dcea8e766a99796b01d591d9ab6b9a67c2"
          ],
          [
            "optical:91cd94459703fb64b6c982d0d61403dcea8e766a99796b01d591d9ab6b9a67c2",
            "spectral:721d847a7ed032426c8124e42507b60c3f9a6ae86a4e9ad406176646c35abff7"
          ]
        ]
      },
      {
        "acquired_at": "2023-03-24T06:46:21.024000+00:00",
        "platform": "sentinel-2a",
        "tile": "40RBN",
        "relative_orbit": 20,
        "discovery_product": "S2A_MSIL2A_20230324T064621_N0510_R020_T40RBN_20240824T014318",
        "discovery_source_id": "stac:727c9c270e50361fad55ba968c9f8e618dea21f690ff8ae24cfb77374ae151f7:sentinel-2-l2a:S2A_MSIL2A_20230324T064621_N0510_R020_T40RBN_20240824T014318",
        "pc_product": "S2A_MSIL2A_20230324T064621_R020_T40RBN_20230324T114938",
        "pc_source_id": "stac:ef177b34b0fa3cabbb6d613d65f1c55d8ea4c5959326bb8896ec51d111792740:sentinel-2-l2a:S2A_MSIL2A_20230324T064621_R020_T40RBN_20230324T114938",
        "processing_baseline": "05.09",
        "generation_time": "2023-03-24T11:49:38.144656Z",
        "cache_id": "f812d226e81f482d912b0f0450ec3623e8a707f3a1774aaeaba2b27080b03ad2",
        "as102_product_id": "optical:f812d226e81f482d912b0f0450ec3623e8a707f3a1774aaeaba2b27080b03ad2",
        "as103_product_id": "spectral:1002b083b3d7637abd67446ef171e0746fe3bd839706cadff18571ac1c51af66",
        "as103_input_content_fingerprint": "2d56879067af2cf99a854725edd38627fdbbcee56345f422e2ba477e509d1898",
        "as102_statistics": {
          "aoi_pixel_count": 67449,
          "valid_data_count": 44037,
          "candidate_water_count": 5290,
          "valid_water_count": 3834,
          "valid_water_fraction_of_aoi": 0.056842948005159454,
          "water_retained_fraction": 0.7247637051039697
        },
        "grid": {
          "crs": "EPSG:32640",
          "transform": [
            20.0,
            0.0,
            249020.0,
            0.0,
            -20.0,
            2707420.0
          ],
          "width": 310,
          "height": 228,
          "resolution": 20.0,
          "bounds": [
            249020.0,
            2702860.0,
            255220.0,
            2707420.0
          ],
          "grid_id": "88d76cf6265d9e0fa2802ed26324c02275e74721d4eb5b597cc9884a6d27aeec"
        },
        "water_support_counts_by_band": {
          "B02": 3834,
          "B03": 3834,
          "B04": 3834,
          "B05": 3834,
          "B06": 3834,
          "B07": 3834,
          "B08": 3834,
          "B8A": 3834,
          "B11": 3834
        },
        "all_band_intersection_support_in_aoi": 3834,
        "feature_statistics": {
          "ndci_like": {
            "valid_count": 3834,
            "valid_fraction_of_parent_water": 1.0,
            "minimum": -0.2994953393936157,
            "maximum": 0.16935808956623077,
            "p05": -0.19485975205898284,
            "median": -0.1491335704922676,
            "p95": 0.015654282364994186
          },
          "mci_like": {
            "valid_count": 3834,
            "valid_fraction_of_parent_water": 1.0,
            "minimum": -0.014194580726325512,
            "maximum": 0.09413103759288788,
            "p05": -0.0003997022547991946,
            "median": 0.0021132807014510036,
            "p95": 0.007818087446503336
          },
          "red_edge_red_ratio": {
            "valid_count": 3834,
            "valid_fraction_of_parent_water": 1.0,
            "minimum": 0.5390589833259583,
            "maximum": 1.4077763557434082,
            "p05": 0.6738365978002548,
            "median": 0.7404417097568512,
            "p95": 1.0318070411682128
          },
          "red_edge2_red_ratio": {
            "valid_count": 3834,
            "valid_fraction_of_parent_water": 1.0,
            "minimum": 0.22782407701015472,
            "maximum": 1.586522102355957,
            "p05": 0.2978320047259331,
            "median": 0.4238516390323639,
            "p95": 0.9709252506494518
          },
          "green_red_ratio": {
            "valid_count": 3834,
            "valid_fraction_of_parent_water": 1.0,
            "minimum": 0.8537262082099915,
            "maximum": 3.3757901191711426,
            "p05": 1.460364818572998,
            "median": 2.7054673433303833,
            "p95": 3.073758840560913
          },
          "green_blue_ratio": {
            "valid_count": 3834,
            "valid_fraction_of_parent_water": 1.0,
            "minimum": 1.0230034589767456,
            "maximum": 1.4380607604980469,
            "p05": 1.1548524856567384,
            "median": 1.2206373810768127,
            "p95": 1.2858742654323578
          }
        },
        "feature_diagnostics": {
          "ndci_like": {
            "parent_valid_water_count": 3834,
            "negative_required_input_count": 0,
            "denominator_rejection_count": 0,
            "negative_denominator_count": 0,
            "nonfinite_result_rejection_count": 0,
            "out_of_nominal_range_count": 0
          },
          "mci_like": {
            "parent_valid_water_count": 3834,
            "negative_required_input_count": 0,
            "denominator_rejection_count": 0,
            "negative_denominator_count": 0,
            "nonfinite_result_rejection_count": 0,
            "out_of_nominal_range_count": null
          },
          "red_edge_red_ratio": {
            "parent_valid_water_count": 3834,
            "negative_required_input_count": 0,
            "denominator_rejection_count": 0,
            "negative_denominator_count": 0,
            "nonfinite_result_rejection_count": 0,
            "out_of_nominal_range_count": null
          },
          "red_edge2_red_ratio": {
            "parent_valid_water_count": 3834,
            "negative_required_input_count": 0,
            "denominator_rejection_count": 0,
            "negative_denominator_count": 0,
            "nonfinite_result_rejection_count": 0,
            "out_of_nominal_range_count": null
          },
          "green_red_ratio": {
            "parent_valid_water_count": 3834,
            "negative_required_input_count": 0,
            "denominator_rejection_count": 0,
            "negative_denominator_count": 0,
            "nonfinite_result_rejection_count": 0,
            "out_of_nominal_range_count": null
          },
          "green_blue_ratio": {
            "parent_valid_water_count": 3834,
            "negative_required_input_count": 0,
            "denominator_rejection_count": 0,
            "negative_denominator_count": 0,
            "nonfinite_result_rejection_count": 0,
            "out_of_nominal_range_count": null
          }
        },
        "lineage_edges": [
          [
            "stac:ef177b34b0fa3cabbb6d613d65f1c55d8ea4c5959326bb8896ec51d111792740:sentinel-2-l2a:S2A_MSIL2A_20230324T064621_R020_T40RBN_20230324T114938",
            "optical:f812d226e81f482d912b0f0450ec3623e8a707f3a1774aaeaba2b27080b03ad2"
          ],
          [
            "optical:f812d226e81f482d912b0f0450ec3623e8a707f3a1774aaeaba2b27080b03ad2",
            "spectral:1002b083b3d7637abd67446ef171e0746fe3bd839706cadff18571ac1c51af66"
          ]
        ]
      },
      {
        "acquired_at": "2023-03-29T06:46:29.024000+00:00",
        "platform": "sentinel-2b",
        "tile": "40RBN",
        "relative_orbit": 20,
        "discovery_product": "S2B_MSIL2A_20230329T064629_N0510_R020_T40RBN_20240823T165234",
        "discovery_source_id": "stac:727c9c270e50361fad55ba968c9f8e618dea21f690ff8ae24cfb77374ae151f7:sentinel-2-l2a:S2B_MSIL2A_20230329T064629_N0510_R020_T40RBN_20240823T165234",
        "pc_product": "S2B_MSIL2A_20230329T064629_R020_T40RBN_20230329T132334",
        "pc_source_id": "stac:ef177b34b0fa3cabbb6d613d65f1c55d8ea4c5959326bb8896ec51d111792740:sentinel-2-l2a:S2B_MSIL2A_20230329T064629_R020_T40RBN_20230329T132334",
        "processing_baseline": "05.09",
        "generation_time": "2023-03-29T13:23:34.143592Z",
        "cache_id": "45360cce80a32aba72c755a3110b865575cc65d45eb96a27922f2dbc93d3aeee",
        "as102_product_id": "optical:45360cce80a32aba72c755a3110b865575cc65d45eb96a27922f2dbc93d3aeee",
        "as103_product_id": "spectral:c4de2a86bb7b15a6a8bc49373823bb944be7e6787db383b0959c93c51f3464d5",
        "as103_input_content_fingerprint": "02e8cbea849befda080e04d63bb8dd37ebb89ecd16b0fc5d4aef92976c9757bd",
        "as102_statistics": {
          "aoi_pixel_count": 67449,
          "valid_data_count": 63565,
          "candidate_water_count": 9116,
          "valid_water_count": 6156,
          "valid_water_fraction_of_aoi": 0.09126895876884758,
          "water_retained_fraction": 0.6752961825362
        },
        "grid": {
          "crs": "EPSG:32640",
          "transform": [
            20.0,
            0.0,
            249020.0,
            0.0,
            -20.0,
            2707420.0
          ],
          "width": 310,
          "height": 228,
          "resolution": 20.0,
          "bounds": [
            249020.0,
            2702860.0,
            255220.0,
            2707420.0
          ],
          "grid_id": "88d76cf6265d9e0fa2802ed26324c02275e74721d4eb5b597cc9884a6d27aeec"
        },
        "water_support_counts_by_band": {
          "B02": 6156,
          "B03": 6156,
          "B04": 6156,
          "B05": 6156,
          "B06": 6156,
          "B07": 6156,
          "B08": 6156,
          "B8A": 6156,
          "B11": 6156
        },
        "all_band_intersection_support_in_aoi": 6156,
        "feature_statistics": {
          "ndci_like": {
            "valid_count": 6156,
            "valid_fraction_of_parent_water": 1.0,
            "minimum": -0.392551064491272,
            "maximum": 0.15763480961322784,
            "p05": -0.14940788224339485,
            "median": -0.08515642583370209,
            "p95": 0.01899075275287032
          },
          "mci_like": {
            "valid_count": 6156,
            "valid_fraction_of_parent_water": 1.0,
            "minimum": -0.013115941546857357,
            "maximum": 0.09025145322084427,
            "p05": 8.007742690097075e-05,
            "median": 0.003432551515288651,
            "p95": 0.05709895957261324
          },
          "red_edge_red_ratio": {
            "valid_count": 6156,
            "valid_fraction_of_parent_water": 1.0,
            "minimum": 0.43621304631233215,
            "maximum": 1.3742671012878418,
            "p05": 0.7400263249874115,
            "median": 0.8430522680282593,
            "p95": 1.0387167632579803
          },
          "red_edge2_red_ratio": {
            "valid_count": 6156,
            "valid_fraction_of_parent_water": 1.0,
            "minimum": 0.05854372680187225,
            "maximum": 1.1014573574066162,
            "p05": 0.22384075820446014,
            "median": 0.5240996778011322,
            "p95": 0.7056565880775452
          },
          "green_red_ratio": {
            "valid_count": 6156,
            "valid_fraction_of_parent_water": 1.0,
            "minimum": 0.867425799369812,
            "maximum": 3.7518131732940674,
            "p05": 1.366832822561264,
            "median": 2.1140880584716797,
            "p95": 2.508885622024536
          },
          "green_blue_ratio": {
            "valid_count": 6156,
            "valid_fraction_of_parent_water": 1.0,
            "minimum": 1.0304661989212036,
            "maximum": 1.5292061567306519,
            "p05": 1.094659149646759,
            "median": 1.1931768655776978,
            "p95": 1.3435646891593933
          }
        },
        "feature_diagnostics": {
          "ndci_like": {
            "parent_valid_water_count": 6156,
            "negative_required_input_count": 0,
            "denominator_rejection_count": 0,
            "negative_denominator_count": 0,
            "nonfinite_result_rejection_count": 0,
            "out_of_nominal_range_count": 0
          },
          "mci_like": {
            "parent_valid_water_count": 6156,
            "negative_required_input_count": 0,
            "denominator_rejection_count": 0,
            "negative_denominator_count": 0,
            "nonfinite_result_rejection_count": 0,
            "out_of_nominal_range_count": null
          },
          "red_edge_red_ratio": {
            "parent_valid_water_count": 6156,
            "negative_required_input_count": 0,
            "denominator_rejection_count": 0,
            "negative_denominator_count": 0,
            "nonfinite_result_rejection_count": 0,
            "out_of_nominal_range_count": null
          },
          "red_edge2_red_ratio": {
            "parent_valid_water_count": 6156,
            "negative_required_input_count": 0,
            "denominator_rejection_count": 0,
            "negative_denominator_count": 0,
            "nonfinite_result_rejection_count": 0,
            "out_of_nominal_range_count": null
          },
          "green_red_ratio": {
            "parent_valid_water_count": 6156,
            "negative_required_input_count": 0,
            "denominator_rejection_count": 0,
            "negative_denominator_count": 0,
            "nonfinite_result_rejection_count": 0,
            "out_of_nominal_range_count": null
          },
          "green_blue_ratio": {
            "parent_valid_water_count": 6156,
            "negative_required_input_count": 0,
            "denominator_rejection_count": 0,
            "negative_denominator_count": 0,
            "nonfinite_result_rejection_count": 0,
            "out_of_nominal_range_count": null
          }
        },
        "lineage_edges": [
          [
            "stac:ef177b34b0fa3cabbb6d613d65f1c55d8ea4c5959326bb8896ec51d111792740:sentinel-2-l2a:S2B_MSIL2A_20230329T064629_R020_T40RBN_20230329T132334",
            "optical:45360cce80a32aba72c755a3110b865575cc65d45eb96a27922f2dbc93d3aeee"
          ],
          [
            "optical:45360cce80a32aba72c755a3110b865575cc65d45eb96a27922f2dbc93d3aeee",
            "spectral:c4de2a86bb7b15a6a8bc49373823bb944be7e6787db383b0959c93c51f3464d5"
          ]
        ]
      }
    ],
    "errors": [
      {
        "stage": "AS-104 computation",
        "acquisition_utc": "2023-04-28T06:46:29.024000+00:00",
        "exception_type": "ValueError",
        "category": "sanitized external/data/validation failure; raw exception omitted"
      }
    ],
    "production_transport_unmodified": true,
    "started_dubai": "2026-10-09T11:31:08.630215+04:00",
    "last_updated_utc": "2026-10-09T07:31:57.353103+00:00",
    "target": {
      "acquired_at": "2023-04-28T06:46:29.024000+00:00",
      "platform": "sentinel-2b",
      "tile": "40RBN",
      "relative_orbit": 20,
      "discovery_product": "S2B_MSIL2A_20230428T064629_N0510_R020_T40RBN_20240831T052931",
      "discovery_source_id": "stac:727c9c270e50361fad55ba968c9f8e618dea21f690ff8ae24cfb77374ae151f7:sentinel-2-l2a:S2B_MSIL2A_20230428T064629_N0510_R020_T40RBN_20240831T052931",
      "pc_product": "S2B_MSIL2A_20230428T064629_R020_T40RBN_20230428T122311",
      "pc_source_id": "stac:ef177b34b0fa3cabbb6d613d65f1c55d8ea4c5959326bb8896ec51d111792740:sentinel-2-l2a:S2B_MSIL2A_20230428T064629_R020_T40RBN_20230428T122311",
      "processing_baseline": "05.09",
      "generation_time": "2023-04-28T12:23:11.362052Z",
      "cache_id": "0725a908d21cd655e83f70d2bb11247dc0f1516f0c00ea275efc3239113ee4a6",
      "as102_product_id": "optical:0725a908d21cd655e83f70d2bb11247dc0f1516f0c00ea275efc3239113ee4a6",
      "as103_product_id": "spectral:dae91b4dda0131ca2d2987321abd2ffd5c4b5ffb2e95a44880b7a5f9a67ea64b",
      "as103_input_content_fingerprint": "e76edf08917ef02cfdb544d811fe6df79ea29f014842be5d29fbb03645d475d7",
      "as102_statistics": {
        "aoi_pixel_count": 67449,
        "valid_data_count": 65166,
        "candidate_water_count": 10211,
        "valid_water_count": 7963,
        "valid_water_fraction_of_aoi": 0.11805957093507688,
        "water_retained_fraction": 0.7798452649103907
      },
      "grid": {
        "crs": "EPSG:32640",
        "transform": [
          20.0,
          0.0,
          249020.0,
          0.0,
          -20.0,
          2707420.0
        ],
        "width": 310,
        "height": 228,
        "resolution": 20.0,
        "bounds": [
          249020.0,
          2702860.0,
          255220.0,
          2707420.0
        ],
        "grid_id": "88d76cf6265d9e0fa2802ed26324c02275e74721d4eb5b597cc9884a6d27aeec"
      },
      "water_support_counts_by_band": {
        "B02": 7996,
        "B03": 7996,
        "B04": 7996,
        "B05": 7996,
        "B06": 7996,
        "B07": 7996,
        "B08": 7963,
        "B11": 7996,
        "B8A": 7996
      },
      "all_band_intersection_support_in_aoi": 7963,
      "feature_statistics": {
        "ndci_like": {
          "valid_count": 7963,
          "valid_fraction_of_parent_water": 1.0,
          "minimum": -2.572964668273926,
          "maximum": 0.20351892709732056,
          "p05": -0.35202173590660096,
          "median": -0.14267197251319885,
          "p95": 0.0423086155205965
        },
        "mci_like": {
          "valid_count": 7963,
          "valid_fraction_of_parent_water": 1.0,
          "minimum": -0.01742854155600071,
          "maximum": 0.09121209383010864,
          "p05": -0.0012384170317091046,
          "median": 0.0008878124062903225,
          "p95": 0.0729243278503418
        },
        "red_edge_red_ratio": {
          "valid_count": 7963,
          "valid_fraction_of_parent_water": 1.0,
          "minimum": -0.440240740776062,
          "maximum": 1.511045217514038,
          "p05": 0.47926616072654726,
          "median": 0.7502835988998413,
          "p95": 1.0883553862571715
        },
        "red_edge2_red_ratio": {
          "valid_count": 7963,
          "valid_fraction_of_parent_water": 1.0,
          "minimum": -1.3180077075958252,
          "maximum": 1.2187410593032837,
          "p05": -0.05205329470336437,
          "median": 0.36368128657341003,
          "p95": 0.6793842673301697
        },
        "green_red_ratio": {
          "valid_count": 7963,
          "valid_fraction_of_parent_water": 1.0,
          "minimum": 0.8410873413085938,
          "maximum": 10.129327774047852,
          "p05": 1.2489951491355897,
          "median": 3.1720826625823975,
          "p95": 5.015284156799316
        },
        "green_blue_ratio": {
          "valid_count": 7963,
          "valid_fraction_of_parent_water": 1.0,
          "minimum": 0.9837192296981812,
          "maximum": 1.706419587135315,
          "p05": 1.0739787340164184,
          "median": 1.1939759254455566,
          "p95": 1.3871012568473815
        }
      },
      "feature_diagnostics": {
        "ndci_like": {
          "parent_valid_water_count": 7963,
          "negative_required_input_count": 2,
          "denominator_rejection_count": 0,
          "negative_denominator_count": 0,
          "nonfinite_result_rejection_count": 0,
          "out_of_nominal_range_count": 2
        },
        "mci_like": {
          "parent_valid_water_count": 7963,
          "negative_required_input_count": 491,
          "denominator_rejection_count": 0,
          "negative_denominator_count": 0,
          "nonfinite_result_rejection_count": 0,
          "out_of_nominal_range_count": null
        },
        "red_edge_red_ratio": {
          "parent_valid_water_count": 7963,
          "negative_required_input_count": 2,
          "denominator_rejection_count": 0,
          "negative_denominator_count": 0,
          "nonfinite_result_rejection_count": 0,
          "out_of_nominal_range_count": null
        },
        "red_edge2_red_ratio": {
          "parent_valid_water_count": 7963,
          "negative_required_input_count": 491,
          "denominator_rejection_count": 0,
          "negative_denominator_count": 0,
          "nonfinite_result_rejection_count": 0,
          "out_of_nominal_range_count": null
        },
        "green_red_ratio": {
          "parent_valid_water_count": 7963,
          "negative_required_input_count": 0,
          "denominator_rejection_count": 0,
          "negative_denominator_count": 0,
          "nonfinite_result_rejection_count": 0,
          "out_of_nominal_range_count": null
        },
        "green_blue_ratio": {
          "parent_valid_water_count": 7963,
          "negative_required_input_count": 0,
          "denominator_rejection_count": 0,
          "negative_denominator_count": 0,
          "nonfinite_result_rejection_count": 0,
          "out_of_nominal_range_count": null
        }
      },
      "lineage_edges": [
        [
          "stac:ef177b34b0fa3cabbb6d613d65f1c55d8ea4c5959326bb8896ec51d111792740:sentinel-2-l2a:S2B_MSIL2A_20230428T064629_R020_T40RBN_20230428T122311",
          "optical:0725a908d21cd655e83f70d2bb11247dc0f1516f0c00ea275efc3239113ee4a6"
        ],
        [
          "optical:0725a908d21cd655e83f70d2bb11247dc0f1516f0c00ea275efc3239113ee4a6",
          "spectral:dae91b4dda0131ca2d2987321abd2ffd5c4b5ffb2e95a44880b7a5f9a67ea64b"
        ]
      ]
    },
    "grid": {
      "crs": "EPSG:32640",
      "transform": [
        20.0,
        0.0,
        249020.0,
        0.0,
        -20.0,
        2707420.0
      ],
      "width": 310,
      "height": 228,
      "resolution": 20.0,
      "bounds": [
        249020.0,
        2702860.0,
        255220.0,
        2707420.0
      ],
      "grid_id": "88d76cf6265d9e0fa2802ed26324c02275e74721d4eb5b597cc9884a6d27aeec"
    },
    "catalog_candidate_count": 44,
    "accepted_target_cache_preservation": "PASS",
    "credential_scan": {
      "live_credential_matches": 0,
      "files_scanned": 99,
      "actual_token_available_for_in_memory_comparison": true
    },
    "completed_utc": "2026-10-09T07:31:57.353103+00:00",
    "completed_dubai": "2026-10-09T11:31:57.353103+04:00"
  },
  "read_only_diagnosis": {
    "status": "BLOCKED",
    "safe_project_validation_message": "Selected scene has unresolved or inconsistent upstream provenance.",
    "guard_location": "src/aquasentinel/temporal/baseline.py:105-110",
    "metadata_findings": [
      {
        "role": "target",
        "pc_product": "S2B_MSIL2A_20230428T064629_R020_T40RBN_20230428T122311",
        "observation_match_acquired_at": "2023-04-28T06:46:29.024000+00:00",
        "pc_source_acquired_at": "2023-04-28T06:46:29.024000+00:00",
        "as103_acquired_at": "2023-04-28T06:46:29.024000+00:00",
        "observation_platform": "sentinel-2b",
        "pc_source_platform": "Sentinel-2B"
      },
      {
        "role": "reference",
        "pc_product": "S2A_MSIL2A_20230304T064751_R020_T40RBN_20230304T113736",
        "observation_match_acquired_at": "2023-03-04T06:47:51.024000+00:00",
        "pc_source_acquired_at": "2023-03-04T06:47:51.024000+00:00",
        "as103_acquired_at": "2023-03-04T06:47:51.024000+00:00",
        "observation_platform": "sentinel-2a",
        "pc_source_platform": "Sentinel-2A"
      },
      {
        "role": "reference",
        "pc_product": "S2B_MSIL2A_20230309T064719_R020_T40RBN_20230309T121958",
        "observation_match_acquired_at": "2023-03-09T06:47:19.025000+00:00",
        "pc_source_acquired_at": "2023-03-09T06:47:19.025000+00:00",
        "as103_acquired_at": "2023-03-09T06:47:19.025000+00:00",
        "observation_platform": "sentinel-2b",
        "pc_source_platform": "Sentinel-2B"
      },
      {
        "role": "reference",
        "pc_product": "S2A_MSIL2A_20230314T064641_R020_T40RBN_20230314T123741",
        "observation_match_acquired_at": "2023-03-14T06:46:41.024000+00:00",
        "pc_source_acquired_at": "2023-03-14T06:46:41.024000+00:00",
        "as103_acquired_at": "2023-03-14T06:46:41.024000+00:00",
        "observation_platform": "sentinel-2a",
        "pc_source_platform": "Sentinel-2A"
      },
      {
        "role": "reference",
        "pc_product": "S2A_MSIL2A_20230324T064621_R020_T40RBN_20230324T114938",
        "observation_match_acquired_at": "2023-03-24T06:46:21.024000+00:00",
        "pc_source_acquired_at": "2023-03-24T06:46:21.024000+00:00",
        "as103_acquired_at": "2023-03-24T06:46:21.024000+00:00",
        "observation_platform": "sentinel-2a",
        "pc_source_platform": "Sentinel-2A"
      },
      {
        "role": "reference",
        "pc_product": "S2B_MSIL2A_20230329T064629_R020_T40RBN_20230329T132334",
        "observation_match_acquired_at": "2023-03-29T06:46:29.024000+00:00",
        "pc_source_acquired_at": "2023-03-29T06:46:29.024000+00:00",
        "as103_acquired_at": "2023-03-29T06:46:29.024000+00:00",
        "observation_platform": "sentinel-2b",
        "pc_source_platform": "Sentinel-2B"
      }
    ]
  }
}
```

### Security, limits and stop state

In-memory live-token/signature comparison scanned repository files, all AS-102
cache files and external safe experiment artifacts: **0 credential matches**.
Tokens were cleared at process exit; no live signed URL/provider body/raw exception
was printed or persisted. Existing fake SAS fixtures remain synthetic. Final
repository/cache scan and quality results are recorded separately below.

Five source scenes are not five valid observations per pixel or statistical
sufficiency. L2A BOA is not aquatic Rrs; candidate features are not confirmed HAB,
chlorophyll, species/toxins, safety, intake risk, persistence, alerts or lead time.
Rank is not probability/confidence/severity. Acquisition-causal retrospective
processing does not establish historical operational availability.

Owner review/authorization of a targeted representation-consistency fix plus real
metadata regression tests is the next gate. No new architectural/scientific
Decision 050 was created. AS-104 stays uncommitted; both safety stashes retained.
No commit/push/PR/new GitHub merge; only the authorized local ff-only integration.
AS-105+ and P1 homogeneous-05.10 experiment NOT started.

### Final offline and preservation gate

After the acceptance-attempt documentation update, the final combined gate
reported **643 passed, 6 warnings in 15.80s**. Ruff passed and
`git diff --check` passed. The warnings remain the six historical Rasterio
`PendingDeprecationWarning` instances; no new warning class was observed.
All ten non-ignored untracked files also passed independent whitespace checks.

The final read-only audit confirmed all eight temporal source/test SHA-256
hashes and the accepted April cache's two file hashes remain identical to the
pre-integration inventory. Decisions and historical milestone/engineering/
evidence bodies remain preserved in order without duplicated bodies. Both
safety stashes remain available; the index is empty and no conflicts remain.
The repository/cache scan examined **3,011 files**, found **0 unrecognized
credential-shaped values**, and recognized **16 existing synthetic signature
literals**. The experiment's separate in-memory live-token/signature scan
examined 99 files and found zero matches. Neither scan persists live secrets.

## 6. Targeted platform case-representation fix — 9 October 2026

**M24 / E24 / EV-028 — PASS; UNCOMMITTED / READY FOR REVIEW.**
Branch `feature/as-104-temporal-baseline`, HEAD and verified origin/main
`2006df7a70a4f48c66933aed96f4464d8d03084e`.

Before editing, verified the dirty AS-104 state and both existing stashes.
Saved complete `git diff --binary` to
`/workspace/as104-before-platform-case-fix.patch` (103,380 bytes), and working
file/temporal/cache SHA-256 inventory to
`/workspace/as104-before-platform-case-fix-sha256.json` (13,149 bytes).
The two original stashes and prior PR #11 backups remain untouched. No new stash,
branch switch, reset or cleaning operation.

### Exact authorized source delta

```diff
-            or observation["platform"] != source.platform
+            or observation["platform"].casefold() != source.platform.casefold()
```

Only Unicode case equality at this guard changes. No str coercion, aliases,
punctuation removal, whitespace stripping or stored value normalization.
Datetime/source serialization/tile/orbit/baseline/lineage/descriptor checks remain
unchanged. No models, AS-102/AS-103 source, transport, configuration, dependencies,
cache schema, processing version, fingerprints or scientific formulas changed.

### Focused regression evidence

Only tests/temporal/test_identity_lineage.py changed: 20 added cases covering
lowercase-observation/mixed-case-source, reverse-case predicate, exact case,
different spacecraft, punctuation/underscore/alias/family/suffix/prefix/spaces,
two acquisition mismatch paths and four invalid non-string observation values.
Full-API tests for both spacecraft check unchanged source spelling, registry,
upstream product IDs/parameters/provenance, feature arrays/masks, fingerprints
and target-first lineage. Repeated results retain identical identity.

The reverse-case example (`Sentinel-2A` / `sentinel-2a`) isolates `_descriptor`'s
consistency predicate with a downstream-validator spy. It does not broaden the
separate existing descriptor schema, which requires lowercase ObservationIdentity
platform. Real products already satisfy that schema. No schema change was made.

`python -m pytest tests/temporal -v`: **132 passed in 8.39s**.
Pre-rerun `python -m pytest -v`: **663 passed, 6 warnings in 17.77s**.
Ruff and git diff --check PASS; all ten untracked files passed independent
whitespace checks. Six historical Rasterio PendingDeprecationWarnings only.
No Decision 050. Prior §§1–5 and M23/E23/EV-027 are preserved unchanged.

## 7. Cached five-reference 05.09 real acceptance rerun — 9 October 2026

**M25 / E25 / EV-029 — PASS; UNCOMMITTED / READY FOR REVIEW.**
Engineering acceptance of deterministic temporal candidate BOA signals, not
biological/operational accuracy validation.

### Frozen inputs, output and checks

Start **2026-10-09T08:01:50.383608+00:00 UTC** /
**2026-10-09T12:01:50.383608+04:00 Asia/Dubai**.
End **2026-10-09T08:01:51.327507+00:00 UTC** /
**2026-10-09T12:01:51.327507+04:00 Asia/Dubai**.
Known-ID cache reload reused exactly R1–R5 and accepted April target at 05.09;
no network, imagery reprocessing or cache writes. A Python socket connect/DNS
audit guard observed zero attempts. All six AS-103 IDs and content fingerprints
reconstructed identically using unchanged production AS-103 code.
All twelve AS-102 cache-file hashes remain identical to the pre-fix inventory.

Window 2023-03-01 inclusive to 2023-04-01 exclusive UTC; minimum observations
five, separate April-28 target. References sorted R1→R2→R3→R4→R5, direct parents
target first then references. The same 20 m EPSG:32640 310×228 grid has ID
`88d76cf6265d9e0fa2802ed26324c02275e74721d4eb5b597cc9884a6d27aeec`.
Temporal product:
`temporal:e814b0574ab30d1841778ee3c5005ffcb313ab42473c41acc028f0a9f7804a8b`.

All six features have target support 7,963. Baseline/z/rank counts in approved
order are 792/802/801/801/801/797; insufficient counts
7,171/7,161/7,162/7,162/7,162/7,166. Zero-MAD and numerical rejection counts
are zero for each feature. About 10% of target support has all five valid
histories; missing histories are neither filled nor inferred.

18/18 independent scalar checks PASS using first/middle/last row-major
baseline-valid pixels selected solely from masks. Independent Python scalar
median/absolute deviations/MAD/1.4826/deviation/exact-tie rank are compared with
production arrays; centre/scale/deviation rtol=1e-14, atol=0; z/rank exact after
float32 casting. Exact pixels, five history values and outputs are below.

Synthetic later-date control cloned from the accepted target at May 3 was
added, then mci_like changed by float32 0.001 on 7,963 pixels with valid summaries.
Selection, arrays/masks/counts/diagnostics/statistics/fingerprints/parents/ID
remain identical. No real future observation or upstream source is claimed.
Deterministic same-input repeat PASS, allowing only provenance creation timing
to differ; input scene arrays/masks remain unchanged. Full actual PC→AS-102→
AS-103→AS-104 edges and ordered lineage are recorded below.

### Complete safe machine-readable experiment evidence

The production result distinguishes consumed-input semantic fingerprints,
output-content integrity fingerprint and full temporal-identity digest. It does
not invent a separate combined fingerprint format. Undefined numbers serialize
as null; no JSON NaN. No signed URLs/tokens/provider bodies are included.

```json
{
  "status": "PASS",
  "started_utc": "2026-10-09T08:01:50.383608+00:00",
  "integration_base": "2006df7a70a4f48c66933aed96f4464d8d03084e",
  "required_processing_baseline": "05.09",
  "reference_start": "2023-03-01T00:00:00+00:00",
  "reference_end": "2023-04-01T00:00:00+00:00",
  "minimum_observations": 5,
  "expected_reference_products": [
    [
      "2023-03-04T06:47:51.024+00:00",
      "S2A_MSIL2A_20230304T064751_R020_T40RBN_20230304T113736"
    ],
    [
      "2023-03-09T06:47:19.025+00:00",
      "S2B_MSIL2A_20230309T064719_R020_T40RBN_20230309T121958"
    ],
    [
      "2023-03-14T06:46:41.024+00:00",
      "S2A_MSIL2A_20230314T064641_R020_T40RBN_20230314T123741"
    ],
    [
      "2023-03-24T06:46:21.024+00:00",
      "S2A_MSIL2A_20230324T064621_R020_T40RBN_20230324T114938"
    ],
    [
      "2023-03-29T06:46:29.024+00:00",
      "S2B_MSIL2A_20230329T064629_R020_T40RBN_20230329T132334"
    ]
  ],
  "predeclared_scalar_rule": "For EACH feature independently: first, middle (index floor(N/2)), last row-major baseline-valid pixel; deduplicate. Selection uses support masks only, before inspecting magnitudes. If N=0, report no supported scalar checks and do not relax history.",
  "scalar_tolerance": {
    "centre_scale_deviation_rtol": 1e-14,
    "atol": 0,
    "rank_z": "exact equality after float32 cast"
  },
  "causal_control_plan": "Synthetic later-date scene cloned from accepted real target, acquisition 2023-05-03T06:46:29.024Z; model-valid feature identity, no alleged real future acquisition/source. Add, then mutate mci_like by float32 0.001 with updated summaries; excluded from registry and selected parents. No future raster processing.",
  "references": [
    {
      "acquired_at": "2023-03-04T06:47:51.024000+00:00",
      "platform": "sentinel-2a",
      "tile": "40RBN",
      "relative_orbit": 20,
      "discovery_product": "S2A_MSIL2A_20230304T064751_N0510_R020_T40RBN_20240819T072511",
      "discovery_source_id": "stac:727c9c270e50361fad55ba968c9f8e618dea21f690ff8ae24cfb77374ae151f7:sentinel-2-l2a:S2A_MSIL2A_20230304T064751_N0510_R020_T40RBN_20240819T072511",
      "pc_product": "S2A_MSIL2A_20230304T064751_R020_T40RBN_20230304T113736",
      "pc_source_id": "stac:ef177b34b0fa3cabbb6d613d65f1c55d8ea4c5959326bb8896ec51d111792740:sentinel-2-l2a:S2A_MSIL2A_20230304T064751_R020_T40RBN_20230304T113736",
      "processing_baseline": "05.09",
      "generation_time": "2023-03-04T11:37:36.492429Z",
      "cache_id": "038a425d46eead247826c4e1e735851a50325d896f1c95b99258840285bf31e1",
      "as102_product_id": "optical:038a425d46eead247826c4e1e735851a50325d896f1c95b99258840285bf31e1",
      "as103_product_id": "spectral:6409add4aef5c95cfe773bfabfa1f554bdda2968241712bda4debefa34b57130",
      "as103_input_content_fingerprint": "187251ea126ffdf774b5d347d2af23f7b693b5d947a7ed49e5d6c3cf694c0166",
      "as102_statistics": {
        "aoi_pixel_count": 67449,
        "valid_data_count": 66512,
        "candidate_water_count": 12765,
        "valid_water_count": 8674,
        "valid_water_fraction_of_aoi": 0.12860086880457827,
        "water_retained_fraction": 0.6795142969056013
      },
      "grid": {
        "crs": "EPSG:32640",
        "transform": [
          20.0,
          0.0,
          249020.0,
          0.0,
          -20.0,
          2707420.0
        ],
        "width": 310,
        "height": 228,
        "resolution": 20.0,
        "bounds": [
          249020.0,
          2702860.0,
          255220.0,
          2707420.0
        ],
        "grid_id": "88d76cf6265d9e0fa2802ed26324c02275e74721d4eb5b597cc9884a6d27aeec"
      },
      "water_support_counts_by_band": {
        "B02": 9562,
        "B03": 9562,
        "B04": 9282,
        "B05": 9562,
        "B06": 9562,
        "B07": 9562,
        "B08": 8952,
        "B11": 9562,
        "B8A": 9562
      },
      "all_band_intersection_support_in_aoi": 8674,
      "feature_statistics": {
        "ndci_like": {
          "valid_count": 8622,
          "valid_fraction_of_parent_water": 0.9940050726308508,
          "minimum": -45.373287200927734,
          "maximum": 41.66667938232422,
          "p05": -2.215840220451355,
          "median": -0.16000819951295853,
          "p95": 2.0129797220230103
        },
        "mci_like": {
          "valid_count": 8674,
          "valid_fraction_of_parent_water": 1.0,
          "minimum": -0.021573437377810478,
          "maximum": 0.09499646723270416,
          "p05": -0.0011412450287025422,
          "median": 0.0009099474118556827,
          "p95": 0.03293588943779469
        },
        "red_edge_red_ratio": {
          "valid_count": 8622,
          "valid_fraction_of_parent_water": 0.9940050726308508,
          "minimum": -34.39999771118164,
          "maximum": 49.23076629638672,
          "p05": -1.9348527252674101,
          "median": 0.6407720148563385,
          "p95": 3.124271631240844
        },
        "red_edge2_red_ratio": {
          "valid_count": 8622,
          "valid_fraction_of_parent_water": 0.9940050726308508,
          "minimum": -62.45783233642578,
          "maximum": 82.82352447509766,
          "p05": -5.270449185371399,
          "median": -0.010533556342124939,
          "p95": 5.479336762428282
        },
        "green_red_ratio": {
          "valid_count": 8622,
          "valid_fraction_of_parent_water": 0.9940050726308508,
          "minimum": -322.3600158691406,
          "maximum": 331.8125,
          "p05": -18.99515037536621,
          "median": 3.888427495956421,
          "p95": 25.236266326904286
        },
        "green_blue_ratio": {
          "valid_count": 8674,
          "valid_fraction_of_parent_water": 1.0,
          "minimum": 0.9599862694740295,
          "maximum": 2.525851249694824,
          "p05": 1.1395424127578735,
          "median": 1.3727585077285767,
          "p95": 1.9724581122398377
        }
      },
      "feature_diagnostics": {
        "ndci_like": {
          "parent_valid_water_count": 8674,
          "negative_required_input_count": 2778,
          "denominator_rejection_count": 52,
          "negative_denominator_count": 1841,
          "nonfinite_result_rejection_count": 0,
          "out_of_nominal_range_count": 1672
        },
        "mci_like": {
          "parent_valid_water_count": 8674,
          "negative_required_input_count": 5569,
          "denominator_rejection_count": 0,
          "negative_denominator_count": 0,
          "nonfinite_result_rejection_count": 0,
          "out_of_nominal_range_count": null
        },
        "red_edge_red_ratio": {
          "parent_valid_water_count": 8674,
          "negative_required_input_count": 2778,
          "denominator_rejection_count": 52,
          "negative_denominator_count": 1053,
          "nonfinite_result_rejection_count": 0,
          "out_of_nominal_range_count": null
        },
        "red_edge2_red_ratio": {
          "parent_valid_water_count": 8674,
          "negative_required_input_count": 5565,
          "denominator_rejection_count": 52,
          "negative_denominator_count": 1053,
          "nonfinite_result_rejection_count": 0,
          "out_of_nominal_range_count": null
        },
        "green_red_ratio": {
          "parent_valid_water_count": 8674,
          "negative_required_input_count": 1053,
          "denominator_rejection_count": 52,
          "negative_denominator_count": 1053,
          "nonfinite_result_rejection_count": 0,
          "out_of_nominal_range_count": null
        },
        "green_blue_ratio": {
          "parent_valid_water_count": 8674,
          "negative_required_input_count": 0,
          "denominator_rejection_count": 0,
          "negative_denominator_count": 0,
          "nonfinite_result_rejection_count": 0,
          "out_of_nominal_range_count": null
        }
      },
      "lineage_edges": [
        [
          "stac:ef177b34b0fa3cabbb6d613d65f1c55d8ea4c5959326bb8896ec51d111792740:sentinel-2-l2a:S2A_MSIL2A_20230304T064751_R020_T40RBN_20230304T113736",
          "optical:038a425d46eead247826c4e1e735851a50325d896f1c95b99258840285bf31e1"
        ],
        [
          "optical:038a425d46eead247826c4e1e735851a50325d896f1c95b99258840285bf31e1",
          "spectral:6409add4aef5c95cfe773bfabfa1f554bdda2968241712bda4debefa34b57130"
        ]
      ]
    },
    {
      "acquired_at": "2023-03-09T06:47:19.025000+00:00",
      "platform": "sentinel-2b",
      "tile": "40RBN",
      "relative_orbit": 20,
      "discovery_product": "S2B_MSIL2A_20230309T064719_N0510_R020_T40RBN_20240823T054455",
      "discovery_source_id": "stac:727c9c270e50361fad55ba968c9f8e618dea21f690ff8ae24cfb77374ae151f7:sentinel-2-l2a:S2B_MSIL2A_20230309T064719_N0510_R020_T40RBN_20240823T054455",
      "pc_product": "S2B_MSIL2A_20230309T064719_R020_T40RBN_20230309T121958",
      "pc_source_id": "stac:ef177b34b0fa3cabbb6d613d65f1c55d8ea4c5959326bb8896ec51d111792740:sentinel-2-l2a:S2B_MSIL2A_20230309T064719_R020_T40RBN_20230309T121958",
      "processing_baseline": "05.09",
      "generation_time": "2023-03-09T12:19:58.419331Z",
      "cache_id": "a412b51188a9c47a0f121a5882fbf464490a66d19a96d3f682c0955398193644",
      "as102_product_id": "optical:a412b51188a9c47a0f121a5882fbf464490a66d19a96d3f682c0955398193644",
      "as103_product_id": "spectral:dafde3d3a2a94d44b62a9d5605bce497b03021e517b7dd6b081607719f37efa1",
      "as103_input_content_fingerprint": "0a61a0afa5254da8959d38135d967d664debfa45b8aea4f3070608dd8dd198b8",
      "as102_statistics": {
        "aoi_pixel_count": 67449,
        "valid_data_count": 43880,
        "candidate_water_count": 3173,
        "valid_water_count": 2092,
        "valid_water_fraction_of_aoi": 0.031016026924046317,
        "water_retained_fraction": 0.6593129530412859
      },
      "grid": {
        "crs": "EPSG:32640",
        "transform": [
          20.0,
          0.0,
          249020.0,
          0.0,
          -20.0,
          2707420.0
        ],
        "width": 310,
        "height": 228,
        "resolution": 20.0,
        "bounds": [
          249020.0,
          2702860.0,
          255220.0,
          2707420.0
        ],
        "grid_id": "88d76cf6265d9e0fa2802ed26324c02275e74721d4eb5b597cc9884a6d27aeec"
      },
      "water_support_counts_by_band": {
        "B02": 2092,
        "B03": 2092,
        "B04": 2092,
        "B05": 2092,
        "B06": 2092,
        "B07": 2092,
        "B08": 2092,
        "B11": 2092,
        "B8A": 2092
      },
      "all_band_intersection_support_in_aoi": 2092,
      "feature_statistics": {
        "ndci_like": {
          "valid_count": 2092,
          "valid_fraction_of_parent_water": 1.0,
          "minimum": -0.4478992223739624,
          "maximum": 0.17207765579223633,
          "p05": -0.21359404399991036,
          "median": -0.1569993868470192,
          "p95": 0.11689317971467969
        },
        "mci_like": {
          "valid_count": 2092,
          "valid_fraction_of_parent_water": 1.0,
          "minimum": -0.0063513522036373615,
          "maximum": 0.08753521740436554,
          "p05": -0.0004854009326663799,
          "median": 0.0029848956037312746,
          "p95": 0.07805229648947715
        },
        "red_edge_red_ratio": {
          "valid_count": 2092,
          "valid_fraction_of_parent_water": 1.0,
          "minimum": 0.3813116252422333,
          "maximum": 1.4156855344772339,
          "p05": 0.6479975312948227,
          "median": 0.7286093831062317,
          "p95": 1.264731729030609
        },
        "red_edge2_red_ratio": {
          "valid_count": 2092,
          "valid_fraction_of_parent_water": 1.0,
          "minimum": 0.13675212860107422,
          "maximum": 1.5279388427734375,
          "p05": 0.2618812873959541,
          "median": 0.3568938672542572,
          "p95": 0.9074863225221629
        },
        "green_red_ratio": {
          "valid_count": 2092,
          "valid_fraction_of_parent_water": 1.0,
          "minimum": 0.8577972054481506,
          "maximum": 2.924053192138672,
          "p05": 1.0898411691188812,
          "median": 2.487278938293457,
          "p95": 2.733928048610687
        },
        "green_blue_ratio": {
          "valid_count": 2092,
          "valid_fraction_of_parent_water": 1.0,
          "minimum": 1.0766685009002686,
          "maximum": 1.4821453094482422,
          "p05": 1.140370148420334,
          "median": 1.252089262008667,
          "p95": 1.3313563406467437
        }
      },
      "feature_diagnostics": {
        "ndci_like": {
          "parent_valid_water_count": 2092,
          "negative_required_input_count": 0,
          "denominator_rejection_count": 0,
          "negative_denominator_count": 0,
          "nonfinite_result_rejection_count": 0,
          "out_of_nominal_range_count": 0
        },
        "mci_like": {
          "parent_valid_water_count": 2092,
          "negative_required_input_count": 0,
          "denominator_rejection_count": 0,
          "negative_denominator_count": 0,
          "nonfinite_result_rejection_count": 0,
          "out_of_nominal_range_count": null
        },
        "red_edge_red_ratio": {
          "parent_valid_water_count": 2092,
          "negative_required_input_count": 0,
          "denominator_rejection_count": 0,
          "negative_denominator_count": 0,
          "nonfinite_result_rejection_count": 0,
          "out_of_nominal_range_count": null
        },
        "red_edge2_red_ratio": {
          "parent_valid_water_count": 2092,
          "negative_required_input_count": 0,
          "denominator_rejection_count": 0,
          "negative_denominator_count": 0,
          "nonfinite_result_rejection_count": 0,
          "out_of_nominal_range_count": null
        },
        "green_red_ratio": {
          "parent_valid_water_count": 2092,
          "negative_required_input_count": 0,
          "denominator_rejection_count": 0,
          "negative_denominator_count": 0,
          "nonfinite_result_rejection_count": 0,
          "out_of_nominal_range_count": null
        },
        "green_blue_ratio": {
          "parent_valid_water_count": 2092,
          "negative_required_input_count": 0,
          "denominator_rejection_count": 0,
          "negative_denominator_count": 0,
          "nonfinite_result_rejection_count": 0,
          "out_of_nominal_range_count": null
        }
      },
      "lineage_edges": [
        [
          "stac:ef177b34b0fa3cabbb6d613d65f1c55d8ea4c5959326bb8896ec51d111792740:sentinel-2-l2a:S2B_MSIL2A_20230309T064719_R020_T40RBN_20230309T121958",
          "optical:a412b51188a9c47a0f121a5882fbf464490a66d19a96d3f682c0955398193644"
        ],
        [
          "optical:a412b51188a9c47a0f121a5882fbf464490a66d19a96d3f682c0955398193644",
          "spectral:dafde3d3a2a94d44b62a9d5605bce497b03021e517b7dd6b081607719f37efa1"
        ]
      ]
    },
    {
      "acquired_at": "2023-03-14T06:46:41.024000+00:00",
      "platform": "sentinel-2a",
      "tile": "40RBN",
      "relative_orbit": 20,
      "discovery_product": "S2A_MSIL2A_20230314T064641_N0510_R020_T40RBN_20240823T041506",
      "discovery_source_id": "stac:727c9c270e50361fad55ba968c9f8e618dea21f690ff8ae24cfb77374ae151f7:sentinel-2-l2a:S2A_MSIL2A_20230314T064641_N0510_R020_T40RBN_20240823T041506",
      "pc_product": "S2A_MSIL2A_20230314T064641_R020_T40RBN_20230314T123741",
      "pc_source_id": "stac:ef177b34b0fa3cabbb6d613d65f1c55d8ea4c5959326bb8896ec51d111792740:sentinel-2-l2a:S2A_MSIL2A_20230314T064641_R020_T40RBN_20230314T123741",
      "processing_baseline": "05.09",
      "generation_time": "2023-03-14T12:37:41.653527Z",
      "cache_id": "91cd94459703fb64b6c982d0d61403dcea8e766a99796b01d591d9ab6b9a67c2",
      "as102_product_id": "optical:91cd94459703fb64b6c982d0d61403dcea8e766a99796b01d591d9ab6b9a67c2",
      "as103_product_id": "spectral:721d847a7ed032426c8124e42507b60c3f9a6ae86a4e9ad406176646c35abff7",
      "as103_input_content_fingerprint": "89311bd86000b4c7a60e1839040022d64c5a45715e3c5fc3a5392c6bc9592462",
      "as102_statistics": {
        "aoi_pixel_count": 67449,
        "valid_data_count": 65948,
        "candidate_water_count": 10231,
        "valid_water_count": 7350,
        "valid_water_fraction_of_aoi": 0.10897122270159676,
        "water_retained_fraction": 0.7184048480109472
      },
      "grid": {
        "crs": "EPSG:32640",
        "transform": [
          20.0,
          0.0,
          249020.0,
          0.0,
          -20.0,
          2707420.0
        ],
        "width": 310,
        "height": 228,
        "resolution": 20.0,
        "bounds": [
          249020.0,
          2702860.0,
          255220.0,
          2707420.0
        ],
        "grid_id": "88d76cf6265d9e0fa2802ed26324c02275e74721d4eb5b597cc9884a6d27aeec"
      },
      "water_support_counts_by_band": {
        "B02": 7523,
        "B03": 7497,
        "B04": 7602,
        "B05": 7612,
        "B06": 7583,
        "B07": 7612,
        "B08": 7593,
        "B11": 7612,
        "B8A": 7612
      },
      "all_band_intersection_support_in_aoi": 7350,
      "feature_statistics": {
        "ndci_like": {
          "valid_count": 7350,
          "valid_fraction_of_parent_water": 1.0,
          "minimum": -10.058127403259277,
          "maximum": 29.228784561157227,
          "p05": 0.016581308655440812,
          "median": 0.09092830121517181,
          "p95": 0.20740841776132574
        },
        "mci_like": {
          "valid_count": 7350,
          "valid_fraction_of_parent_water": 1.0,
          "minimum": -0.019773438572883606,
          "maximum": 0.11635499447584152,
          "p05": -0.003755379968788475,
          "median": 0.0014121346175670624,
          "p95": 0.09187133535742759
        },
        "red_edge_red_ratio": {
          "valid_count": 7350,
          "valid_fraction_of_parent_water": 1.0,
          "minimum": -87.41450500488281,
          "maximum": 51.25545120239258,
          "p05": 1.0265063405036927,
          "median": 1.199103593826294,
          "p95": 1.509673631191253
        },
        "red_edge2_red_ratio": {
          "valid_count": 7350,
          "valid_fraction_of_parent_water": 1.0,
          "minimum": -211.45594787597656,
          "maximum": 124.39836120605469,
          "p05": -0.16308539956808088,
          "median": 1.3672099709510803,
          "p95": 1.986032766103742
        },
        "green_red_ratio": {
          "valid_count": 7350,
          "valid_fraction_of_parent_water": 1.0,
          "minimum": -163.76202392578125,
          "maximum": 289.89593505859375,
          "p05": -1.989084905385971,
          "median": -0.34662455320358276,
          "p95": 1.4881002187728882
        },
        "green_blue_ratio": {
          "valid_count": 7330,
          "valid_fraction_of_parent_water": 0.9972789115646259,
          "minimum": -279.1667175292969,
          "maximum": 226.9896240234375,
          "p05": -5.907708430290221,
          "median": 0.0869569405913353,
          "p95": 6.453824853897094
        }
      },
      "feature_diagnostics": {
        "ndci_like": {
          "parent_valid_water_count": 7350,
          "negative_required_input_count": 6071,
          "denominator_rejection_count": 0,
          "negative_denominator_count": 6052,
          "nonfinite_result_rejection_count": 0,
          "out_of_nominal_range_count": 45
        },
        "mci_like": {
          "parent_valid_water_count": 7350,
          "negative_required_input_count": 6557,
          "denominator_rejection_count": 0,
          "negative_denominator_count": 0,
          "nonfinite_result_rejection_count": 0,
          "out_of_nominal_range_count": null
        },
        "red_edge_red_ratio": {
          "parent_valid_water_count": 7350,
          "negative_required_input_count": 6071,
          "denominator_rejection_count": 0,
          "negative_denominator_count": 6028,
          "nonfinite_result_rejection_count": 0,
          "out_of_nominal_range_count": null
        },
        "red_edge2_red_ratio": {
          "parent_valid_water_count": 7350,
          "negative_required_input_count": 6557,
          "denominator_rejection_count": 0,
          "negative_denominator_count": 6028,
          "nonfinite_result_rejection_count": 0,
          "out_of_nominal_range_count": null
        },
        "green_red_ratio": {
          "parent_valid_water_count": 7350,
          "negative_required_input_count": 6028,
          "denominator_rejection_count": 0,
          "negative_denominator_count": 6028,
          "nonfinite_result_rejection_count": 0,
          "out_of_nominal_range_count": null
        },
        "green_blue_ratio": {
          "parent_valid_water_count": 7350,
          "negative_required_input_count": 4728,
          "denominator_rejection_count": 20,
          "negative_denominator_count": 4728,
          "nonfinite_result_rejection_count": 0,
          "out_of_nominal_range_count": null
        }
      },
      "lineage_edges": [
        [
          "stac:ef177b34b0fa3cabbb6d613d65f1c55d8ea4c5959326bb8896ec51d111792740:sentinel-2-l2a:S2A_MSIL2A_20230314T064641_R020_T40RBN_20230314T123741",
          "optical:91cd94459703fb64b6c982d0d61403dcea8e766a99796b01d591d9ab6b9a67c2"
        ],
        [
          "optical:91cd94459703fb64b6c982d0d61403dcea8e766a99796b01d591d9ab6b9a67c2",
          "spectral:721d847a7ed032426c8124e42507b60c3f9a6ae86a4e9ad406176646c35abff7"
        ]
      ]
    },
    {
      "acquired_at": "2023-03-24T06:46:21.024000+00:00",
      "platform": "sentinel-2a",
      "tile": "40RBN",
      "relative_orbit": 20,
      "discovery_product": "S2A_MSIL2A_20230324T064621_N0510_R020_T40RBN_20240824T014318",
      "discovery_source_id": "stac:727c9c270e50361fad55ba968c9f8e618dea21f690ff8ae24cfb77374ae151f7:sentinel-2-l2a:S2A_MSIL2A_20230324T064621_N0510_R020_T40RBN_20240824T014318",
      "pc_product": "S2A_MSIL2A_20230324T064621_R020_T40RBN_20230324T114938",
      "pc_source_id": "stac:ef177b34b0fa3cabbb6d613d65f1c55d8ea4c5959326bb8896ec51d111792740:sentinel-2-l2a:S2A_MSIL2A_20230324T064621_R020_T40RBN_20230324T114938",
      "processing_baseline": "05.09",
      "generation_time": "2023-03-24T11:49:38.144656Z",
      "cache_id": "f812d226e81f482d912b0f0450ec3623e8a707f3a1774aaeaba2b27080b03ad2",
      "as102_product_id": "optical:f812d226e81f482d912b0f0450ec3623e8a707f3a1774aaeaba2b27080b03ad2",
      "as103_product_id": "spectral:1002b083b3d7637abd67446ef171e0746fe3bd839706cadff18571ac1c51af66",
      "as103_input_content_fingerprint": "2d56879067af2cf99a854725edd38627fdbbcee56345f422e2ba477e509d1898",
      "as102_statistics": {
        "aoi_pixel_count": 67449,
        "valid_data_count": 44037,
        "candidate_water_count": 5290,
        "valid_water_count": 3834,
        "valid_water_fraction_of_aoi": 0.056842948005159454,
        "water_retained_fraction": 0.7247637051039697
      },
      "grid": {
        "crs": "EPSG:32640",
        "transform": [
          20.0,
          0.0,
          249020.0,
          0.0,
          -20.0,
          2707420.0
        ],
        "width": 310,
        "height": 228,
        "resolution": 20.0,
        "bounds": [
          249020.0,
          2702860.0,
          255220.0,
          2707420.0
        ],
        "grid_id": "88d76cf6265d9e0fa2802ed26324c02275e74721d4eb5b597cc9884a6d27aeec"
      },
      "water_support_counts_by_band": {
        "B02": 3834,
        "B03": 3834,
        "B04": 3834,
        "B05": 3834,
        "B06": 3834,
        "B07": 3834,
        "B08": 3834,
        "B11": 3834,
        "B8A": 3834
      },
      "all_band_intersection_support_in_aoi": 3834,
      "feature_statistics": {
        "ndci_like": {
          "valid_count": 3834,
          "valid_fraction_of_parent_water": 1.0,
          "minimum": -0.2994953393936157,
          "maximum": 0.16935808956623077,
          "p05": -0.19485975205898284,
          "median": -0.1491335704922676,
          "p95": 0.015654282364994186
        },
        "mci_like": {
          "valid_count": 3834,
          "valid_fraction_of_parent_water": 1.0,
          "minimum": -0.014194580726325512,
          "maximum": 0.09413103759288788,
          "p05": -0.0003997022547991946,
          "median": 0.0021132807014510036,
          "p95": 0.007818087446503336
        },
        "red_edge_red_ratio": {
          "valid_count": 3834,
          "valid_fraction_of_parent_water": 1.0,
          "minimum": 0.5390589833259583,
          "maximum": 1.4077763557434082,
          "p05": 0.6738365978002548,
          "median": 0.7404417097568512,
          "p95": 1.0318070411682128
        },
        "red_edge2_red_ratio": {
          "valid_count": 3834,
          "valid_fraction_of_parent_water": 1.0,
          "minimum": 0.22782407701015472,
          "maximum": 1.586522102355957,
          "p05": 0.2978320047259331,
          "median": 0.4238516390323639,
          "p95": 0.9709252506494518
        },
        "green_red_ratio": {
          "valid_count": 3834,
          "valid_fraction_of_parent_water": 1.0,
          "minimum": 0.8537262082099915,
          "maximum": 3.3757901191711426,
          "p05": 1.460364818572998,
          "median": 2.7054673433303833,
          "p95": 3.073758840560913
        },
        "green_blue_ratio": {
          "valid_count": 3834,
          "valid_fraction_of_parent_water": 1.0,
          "minimum": 1.0230034589767456,
          "maximum": 1.4380607604980469,
          "p05": 1.1548524856567384,
          "median": 1.2206373810768127,
          "p95": 1.2858742654323578
        }
      },
      "feature_diagnostics": {
        "ndci_like": {
          "parent_valid_water_count": 3834,
          "negative_required_input_count": 0,
          "denominator_rejection_count": 0,
          "negative_denominator_count": 0,
          "nonfinite_result_rejection_count": 0,
          "out_of_nominal_range_count": 0
        },
        "mci_like": {
          "parent_valid_water_count": 3834,
          "negative_required_input_count": 0,
          "denominator_rejection_count": 0,
          "negative_denominator_count": 0,
          "nonfinite_result_rejection_count": 0,
          "out_of_nominal_range_count": null
        },
        "red_edge_red_ratio": {
          "parent_valid_water_count": 3834,
          "negative_required_input_count": 0,
          "denominator_rejection_count": 0,
          "negative_denominator_count": 0,
          "nonfinite_result_rejection_count": 0,
          "out_of_nominal_range_count": null
        },
        "red_edge2_red_ratio": {
          "parent_valid_water_count": 3834,
          "negative_required_input_count": 0,
          "denominator_rejection_count": 0,
          "negative_denominator_count": 0,
          "nonfinite_result_rejection_count": 0,
          "out_of_nominal_range_count": null
        },
        "green_red_ratio": {
          "parent_valid_water_count": 3834,
          "negative_required_input_count": 0,
          "denominator_rejection_count": 0,
          "negative_denominator_count": 0,
          "nonfinite_result_rejection_count": 0,
          "out_of_nominal_range_count": null
        },
        "green_blue_ratio": {
          "parent_valid_water_count": 3834,
          "negative_required_input_count": 0,
          "denominator_rejection_count": 0,
          "negative_denominator_count": 0,
          "nonfinite_result_rejection_count": 0,
          "out_of_nominal_range_count": null
        }
      },
      "lineage_edges": [
        [
          "stac:ef177b34b0fa3cabbb6d613d65f1c55d8ea4c5959326bb8896ec51d111792740:sentinel-2-l2a:S2A_MSIL2A_20230324T064621_R020_T40RBN_20230324T114938",
          "optical:f812d226e81f482d912b0f0450ec3623e8a707f3a1774aaeaba2b27080b03ad2"
        ],
        [
          "optical:f812d226e81f482d912b0f0450ec3623e8a707f3a1774aaeaba2b27080b03ad2",
          "spectral:1002b083b3d7637abd67446ef171e0746fe3bd839706cadff18571ac1c51af66"
        ]
      ]
    },
    {
      "acquired_at": "2023-03-29T06:46:29.024000+00:00",
      "platform": "sentinel-2b",
      "tile": "40RBN",
      "relative_orbit": 20,
      "discovery_product": "S2B_MSIL2A_20230329T064629_N0510_R020_T40RBN_20240823T165234",
      "discovery_source_id": "stac:727c9c270e50361fad55ba968c9f8e618dea21f690ff8ae24cfb77374ae151f7:sentinel-2-l2a:S2B_MSIL2A_20230329T064629_N0510_R020_T40RBN_20240823T165234",
      "pc_product": "S2B_MSIL2A_20230329T064629_R020_T40RBN_20230329T132334",
      "pc_source_id": "stac:ef177b34b0fa3cabbb6d613d65f1c55d8ea4c5959326bb8896ec51d111792740:sentinel-2-l2a:S2B_MSIL2A_20230329T064629_R020_T40RBN_20230329T132334",
      "processing_baseline": "05.09",
      "generation_time": "2023-03-29T13:23:34.143592Z",
      "cache_id": "45360cce80a32aba72c755a3110b865575cc65d45eb96a27922f2dbc93d3aeee",
      "as102_product_id": "optical:45360cce80a32aba72c755a3110b865575cc65d45eb96a27922f2dbc93d3aeee",
      "as103_product_id": "spectral:c4de2a86bb7b15a6a8bc49373823bb944be7e6787db383b0959c93c51f3464d5",
      "as103_input_content_fingerprint": "02e8cbea849befda080e04d63bb8dd37ebb89ecd16b0fc5d4aef92976c9757bd",
      "as102_statistics": {
        "aoi_pixel_count": 67449,
        "valid_data_count": 63565,
        "candidate_water_count": 9116,
        "valid_water_count": 6156,
        "valid_water_fraction_of_aoi": 0.09126895876884758,
        "water_retained_fraction": 0.6752961825362
      },
      "grid": {
        "crs": "EPSG:32640",
        "transform": [
          20.0,
          0.0,
          249020.0,
          0.0,
          -20.0,
          2707420.0
        ],
        "width": 310,
        "height": 228,
        "resolution": 20.0,
        "bounds": [
          249020.0,
          2702860.0,
          255220.0,
          2707420.0
        ],
        "grid_id": "88d76cf6265d9e0fa2802ed26324c02275e74721d4eb5b597cc9884a6d27aeec"
      },
      "water_support_counts_by_band": {
        "B02": 6156,
        "B03": 6156,
        "B04": 6156,
        "B05": 6156,
        "B06": 6156,
        "B07": 6156,
        "B08": 6156,
        "B11": 6156,
        "B8A": 6156
      },
      "all_band_intersection_support_in_aoi": 6156,
      "feature_statistics": {
        "ndci_like": {
          "valid_count": 6156,
          "valid_fraction_of_parent_water": 1.0,
          "minimum": -0.392551064491272,
          "maximum": 0.15763480961322784,
          "p05": -0.14940788224339485,
          "median": -0.08515642583370209,
          "p95": 0.01899075275287032
        },
        "mci_like": {
          "valid_count": 6156,
          "valid_fraction_of_parent_water": 1.0,
          "minimum": -0.013115941546857357,
          "maximum": 0.09025145322084427,
          "p05": 8.007742690097075e-05,
          "median": 0.003432551515288651,
          "p95": 0.05709895957261324
        },
        "red_edge_red_ratio": {
          "valid_count": 6156,
          "valid_fraction_of_parent_water": 1.0,
          "minimum": 0.43621304631233215,
          "maximum": 1.3742671012878418,
          "p05": 0.7400263249874115,
          "median": 0.8430522680282593,
          "p95": 1.0387167632579803
        },
        "red_edge2_red_ratio": {
          "valid_count": 6156,
          "valid_fraction_of_parent_water": 1.0,
          "minimum": 0.05854372680187225,
          "maximum": 1.1014573574066162,
          "p05": 0.22384075820446014,
          "median": 0.5240996778011322,
          "p95": 0.7056565880775452
        },
        "green_red_ratio": {
          "valid_count": 6156,
          "valid_fraction_of_parent_water": 1.0,
          "minimum": 0.867425799369812,
          "maximum": 3.7518131732940674,
          "p05": 1.366832822561264,
          "median": 2.1140880584716797,
          "p95": 2.508885622024536
        },
        "green_blue_ratio": {
          "valid_count": 6156,
          "valid_fraction_of_parent_water": 1.0,
          "minimum": 1.0304661989212036,
          "maximum": 1.5292061567306519,
          "p05": 1.094659149646759,
          "median": 1.1931768655776978,
          "p95": 1.3435646891593933
        }
      },
      "feature_diagnostics": {
        "ndci_like": {
          "parent_valid_water_count": 6156,
          "negative_required_input_count": 0,
          "denominator_rejection_count": 0,
          "negative_denominator_count": 0,
          "nonfinite_result_rejection_count": 0,
          "out_of_nominal_range_count": 0
        },
        "mci_like": {
          "parent_valid_water_count": 6156,
          "negative_required_input_count": 0,
          "denominator_rejection_count": 0,
          "negative_denominator_count": 0,
          "nonfinite_result_rejection_count": 0,
          "out_of_nominal_range_count": null
        },
        "red_edge_red_ratio": {
          "parent_valid_water_count": 6156,
          "negative_required_input_count": 0,
          "denominator_rejection_count": 0,
          "negative_denominator_count": 0,
          "nonfinite_result_rejection_count": 0,
          "out_of_nominal_range_count": null
        },
        "red_edge2_red_ratio": {
          "parent_valid_water_count": 6156,
          "negative_required_input_count": 0,
          "denominator_rejection_count": 0,
          "negative_denominator_count": 0,
          "nonfinite_result_rejection_count": 0,
          "out_of_nominal_range_count": null
        },
        "green_red_ratio": {
          "parent_valid_water_count": 6156,
          "negative_required_input_count": 0,
          "denominator_rejection_count": 0,
          "negative_denominator_count": 0,
          "nonfinite_result_rejection_count": 0,
          "out_of_nominal_range_count": null
        },
        "green_blue_ratio": {
          "parent_valid_water_count": 6156,
          "negative_required_input_count": 0,
          "denominator_rejection_count": 0,
          "negative_denominator_count": 0,
          "nonfinite_result_rejection_count": 0,
          "out_of_nominal_range_count": null
        }
      },
      "lineage_edges": [
        [
          "stac:ef177b34b0fa3cabbb6d613d65f1c55d8ea4c5959326bb8896ec51d111792740:sentinel-2-l2a:S2B_MSIL2A_20230329T064629_R020_T40RBN_20230329T132334",
          "optical:45360cce80a32aba72c755a3110b865575cc65d45eb96a27922f2dbc93d3aeee"
        ],
        [
          "optical:45360cce80a32aba72c755a3110b865575cc65d45eb96a27922f2dbc93d3aeee",
          "spectral:c4de2a86bb7b15a6a8bc49373823bb944be7e6787db383b0959c93c51f3464d5"
        ]
      ]
    }
  ],
  "errors": [],
  "production_transport_unmodified": true,
  "started_dubai": "2026-10-09T12:01:50.383608+04:00",
  "last_updated_utc": "2026-10-09T08:01:51.327507+00:00",
  "target": {
    "acquired_at": "2023-04-28T06:46:29.024000+00:00",
    "platform": "sentinel-2b",
    "tile": "40RBN",
    "relative_orbit": 20,
    "discovery_product": "S2B_MSIL2A_20230428T064629_N0510_R020_T40RBN_20240831T052931",
    "discovery_source_id": "stac:727c9c270e50361fad55ba968c9f8e618dea21f690ff8ae24cfb77374ae151f7:sentinel-2-l2a:S2B_MSIL2A_20230428T064629_N0510_R020_T40RBN_20240831T052931",
    "pc_product": "S2B_MSIL2A_20230428T064629_R020_T40RBN_20230428T122311",
    "pc_source_id": "stac:ef177b34b0fa3cabbb6d613d65f1c55d8ea4c5959326bb8896ec51d111792740:sentinel-2-l2a:S2B_MSIL2A_20230428T064629_R020_T40RBN_20230428T122311",
    "processing_baseline": "05.09",
    "generation_time": "2023-04-28T12:23:11.362052Z",
    "cache_id": "0725a908d21cd655e83f70d2bb11247dc0f1516f0c00ea275efc3239113ee4a6",
    "as102_product_id": "optical:0725a908d21cd655e83f70d2bb11247dc0f1516f0c00ea275efc3239113ee4a6",
    "as103_product_id": "spectral:dae91b4dda0131ca2d2987321abd2ffd5c4b5ffb2e95a44880b7a5f9a67ea64b",
    "as103_input_content_fingerprint": "e76edf08917ef02cfdb544d811fe6df79ea29f014842be5d29fbb03645d475d7",
    "as102_statistics": {
      "aoi_pixel_count": 67449,
      "valid_data_count": 65166,
      "candidate_water_count": 10211,
      "valid_water_count": 7963,
      "valid_water_fraction_of_aoi": 0.11805957093507688,
      "water_retained_fraction": 0.7798452649103907
    },
    "grid": {
      "crs": "EPSG:32640",
      "transform": [
        20.0,
        0.0,
        249020.0,
        0.0,
        -20.0,
        2707420.0
      ],
      "width": 310,
      "height": 228,
      "resolution": 20.0,
      "bounds": [
        249020.0,
        2702860.0,
        255220.0,
        2707420.0
      ],
      "grid_id": "88d76cf6265d9e0fa2802ed26324c02275e74721d4eb5b597cc9884a6d27aeec"
    },
    "water_support_counts_by_band": {
      "B02": 7996,
      "B03": 7996,
      "B04": 7996,
      "B05": 7996,
      "B06": 7996,
      "B07": 7996,
      "B08": 7963,
      "B11": 7996,
      "B8A": 7996
    },
    "all_band_intersection_support_in_aoi": 7963,
    "feature_statistics": {
      "ndci_like": {
        "valid_count": 7963,
        "valid_fraction_of_parent_water": 1.0,
        "minimum": -2.572964668273926,
        "maximum": 0.20351892709732056,
        "p05": -0.35202173590660096,
        "median": -0.14267197251319885,
        "p95": 0.0423086155205965
      },
      "mci_like": {
        "valid_count": 7963,
        "valid_fraction_of_parent_water": 1.0,
        "minimum": -0.01742854155600071,
        "maximum": 0.09121209383010864,
        "p05": -0.0012384170317091046,
        "median": 0.0008878124062903225,
        "p95": 0.0729243278503418
      },
      "red_edge_red_ratio": {
        "valid_count": 7963,
        "valid_fraction_of_parent_water": 1.0,
        "minimum": -0.440240740776062,
        "maximum": 1.511045217514038,
        "p05": 0.47926616072654726,
        "median": 0.7502835988998413,
        "p95": 1.0883553862571715
      },
      "red_edge2_red_ratio": {
        "valid_count": 7963,
        "valid_fraction_of_parent_water": 1.0,
        "minimum": -1.3180077075958252,
        "maximum": 1.2187410593032837,
        "p05": -0.05205329470336437,
        "median": 0.36368128657341003,
        "p95": 0.6793842673301697
      },
      "green_red_ratio": {
        "valid_count": 7963,
        "valid_fraction_of_parent_water": 1.0,
        "minimum": 0.8410873413085938,
        "maximum": 10.129327774047852,
        "p05": 1.2489951491355897,
        "median": 3.1720826625823975,
        "p95": 5.015284156799316
      },
      "green_blue_ratio": {
        "valid_count": 7963,
        "valid_fraction_of_parent_water": 1.0,
        "minimum": 0.9837192296981812,
        "maximum": 1.706419587135315,
        "p05": 1.0739787340164184,
        "median": 1.1939759254455566,
        "p95": 1.3871012568473815
      }
    },
    "feature_diagnostics": {
      "ndci_like": {
        "parent_valid_water_count": 7963,
        "negative_required_input_count": 2,
        "denominator_rejection_count": 0,
        "negative_denominator_count": 0,
        "nonfinite_result_rejection_count": 0,
        "out_of_nominal_range_count": 2
      },
      "mci_like": {
        "parent_valid_water_count": 7963,
        "negative_required_input_count": 491,
        "denominator_rejection_count": 0,
        "negative_denominator_count": 0,
        "nonfinite_result_rejection_count": 0,
        "out_of_nominal_range_count": null
      },
      "red_edge_red_ratio": {
        "parent_valid_water_count": 7963,
        "negative_required_input_count": 2,
        "denominator_rejection_count": 0,
        "negative_denominator_count": 0,
        "nonfinite_result_rejection_count": 0,
        "out_of_nominal_range_count": null
      },
      "red_edge2_red_ratio": {
        "parent_valid_water_count": 7963,
        "negative_required_input_count": 491,
        "denominator_rejection_count": 0,
        "negative_denominator_count": 0,
        "nonfinite_result_rejection_count": 0,
        "out_of_nominal_range_count": null
      },
      "green_red_ratio": {
        "parent_valid_water_count": 7963,
        "negative_required_input_count": 0,
        "denominator_rejection_count": 0,
        "negative_denominator_count": 0,
        "nonfinite_result_rejection_count": 0,
        "out_of_nominal_range_count": null
      },
      "green_blue_ratio": {
        "parent_valid_water_count": 7963,
        "negative_required_input_count": 0,
        "denominator_rejection_count": 0,
        "negative_denominator_count": 0,
        "nonfinite_result_rejection_count": 0,
        "out_of_nominal_range_count": null
      }
    },
    "lineage_edges": [
      [
        "stac:ef177b34b0fa3cabbb6d613d65f1c55d8ea4c5959326bb8896ec51d111792740:sentinel-2-l2a:S2B_MSIL2A_20230428T064629_R020_T40RBN_20230428T122311",
        "optical:0725a908d21cd655e83f70d2bb11247dc0f1516f0c00ea275efc3239113ee4a6"
      ],
      [
        "optical:0725a908d21cd655e83f70d2bb11247dc0f1516f0c00ea275efc3239113ee4a6",
        "spectral:dae91b4dda0131ca2d2987321abd2ffd5c4b5ffb2e95a44880b7a5f9a67ea64b"
      ]
    ]
  },
  "grid": {
    "crs": "EPSG:32640",
    "transform": [
      20.0,
      0.0,
      249020.0,
      0.0,
      -20.0,
      2707420.0
    ],
    "width": 310,
    "height": 228,
    "resolution": 20.0,
    "bounds": [
      249020.0,
      2702860.0,
      255220.0,
      2707420.0
    ],
    "grid_id": "88d76cf6265d9e0fa2802ed26324c02275e74721d4eb5b597cc9884a6d27aeec"
  },
  "cache_reuse": "PASS: all six known IDs; no raster retrieval/reprocessing",
  "as103_reconstruction": "PASS: all six IDs and input content fingerprints identical",
  "input_immutability": "PASS",
  "product_id": "temporal:e814b0574ab30d1841778ee3c5005ffcb313ab42473c41acc028f0a9f7804a8b",
  "input_fingerprints": {
    "format": "as104-input-v1",
    "target": "0195eb2c019109f0d5217cda7ea492cc73e68d35708758535f5df92aa8d00662",
    "references": [
      "6d4e3c1af4cdcc573ace48720e082e1b44463ed1697e2e32ef88c5475821333d",
      "467d8094d9fe6becafc2f50700fb90fcef54113a159b7109e468feeebdad319d",
      "0d60d267cc5cd9058fad51a56bd18574cbba84a48cf3048783e089a0142236bb",
      "eab8fb9314e7909be9a4bde8a7122234c360dcfde1398a38c8a6f3f0478d56d2",
      "c08237875c285d9eda54f98d7b28d5dabcdcd2b53fdf5c0bc598632c1439e26d"
    ]
  },
  "identity": {
    "processing_version": "as104-v1",
    "target_product_id": "spectral:dae91b4dda0131ca2d2987321abd2ffd5c4b5ffb2e95a44880b7a5f9a67ea64b",
    "target_acquired_at": "2023-04-28T06:46:29.024000+00:00",
    "reference_product_ids": [
      "spectral:6409add4aef5c95cfe773bfabfa1f554bdda2968241712bda4debefa34b57130",
      "spectral:dafde3d3a2a94d44b62a9d5605bce497b03021e517b7dd6b081607719f37efa1",
      "spectral:721d847a7ed032426c8124e42507b60c3f9a6ae86a4e9ad406176646c35abff7",
      "spectral:1002b083b3d7637abd67446ef171e0746fe3bd839706cadff18571ac1c51af66",
      "spectral:c4de2a86bb7b15a6a8bc49373823bb944be7e6787db383b0959c93c51f3464d5"
    ],
    "reference_acquired_at": [
      "2023-03-04T06:47:51.024000+00:00",
      "2023-03-09T06:47:19.025000+00:00",
      "2023-03-14T06:46:41.024000+00:00",
      "2023-03-24T06:46:21.024000+00:00",
      "2023-03-29T06:46:29.024000+00:00"
    ],
    "reference_period": {
      "start": "2023-03-01T00:00:00+00:00",
      "end": "2023-04-01T00:00:00+00:00"
    },
    "minimum_observations": 5,
    "grid": {
      "crs": "EPSG:32640",
      "transform": [
        20.0,
        0.0,
        249020.0,
        0.0,
        -20.0,
        2707420.0
      ],
      "width": 310,
      "height": 228,
      "resolution": 20.0,
      "bounds": [
        249020.0,
        2702860.0,
        255220.0,
        2707420.0
      ],
      "grid_id": "88d76cf6265d9e0fa2802ed26324c02275e74721d4eb5b597cc9884a6d27aeec"
    },
    "feature_order": [
      "ndci_like",
      "mci_like",
      "red_edge_red_ratio",
      "red_edge2_red_ratio",
      "green_red_ratio",
      "green_blue_ratio"
    ],
    "formulas": {
      "ndci_like": {
        "formula": "(B05 - B04) / (B05 + B04)",
        "required_bands": [
          "B05",
          "B04"
        ],
        "feature_family": "red_edge_b5_vs_red",
        "units": "dimensionless",
        "scientific_name": "NDCI-like candidate red-edge contrast"
      },
      "mci_like": {
        "formula": "B05 - (B04 + (B06 - B04) * ((705.0 - 665.0) / (740.0 - 665.0)))",
        "required_bands": [
          "B04",
          "B05",
          "B06"
        ],
        "feature_family": "red_edge_line_height",
        "units": "dimensionless reflectance",
        "scientific_name": "MCI-like red-edge line height",
        "wavelengths": {
          "B04": 665.0,
          "B05": 705.0,
          "B06": 740.0
        },
        "wavelength_units": "nm",
        "nominal_wavelengths": true,
        "cloud_correction_factor": 1.0
      },
      "red_edge_red_ratio": {
        "formula": "B05 / B04",
        "required_bands": [
          "B05",
          "B04"
        ],
        "feature_family": "red_edge_b5_vs_red",
        "units": "dimensionless"
      },
      "red_edge2_red_ratio": {
        "formula": "B06 / B04",
        "required_bands": [
          "B06",
          "B04"
        ],
        "feature_family": "red_edge_b6_vs_red",
        "units": "dimensionless"
      },
      "green_red_ratio": {
        "formula": "B03 / B04",
        "required_bands": [
          "B03",
          "B04"
        ],
        "feature_family": "visible_green_vs_red",
        "units": "dimensionless"
      },
      "green_blue_ratio": {
        "formula": "B03 / B02",
        "required_bands": [
          "B03",
          "B02"
        ],
        "feature_family": "visible_green_vs_blue",
        "units": "dimensionless"
      }
    },
    "compatibility": [
      {
        "product_id": "spectral:dae91b4dda0131ca2d2987321abd2ffd5c4b5ffb2e95a44880b7a5f9a67ea64b",
        "parent_product_id": "optical:0725a908d21cd655e83f70d2bb11247dc0f1516f0c00ea275efc3239113ee4a6",
        "pc_source_id": "stac:ef177b34b0fa3cabbb6d613d65f1c55d8ea4c5959326bb8896ec51d111792740:sentinel-2-l2a:S2B_MSIL2A_20230428T064629_R020_T40RBN_20230428T122311",
        "pc_product_id": "S2B_MSIL2A_20230428T064629_R020_T40RBN_20230428T122311",
        "observation": {
          "acquired_at": "2023-04-28T06:46:29.024000+00:00",
          "mgrs_tile": "40RBN",
          "platform": "sentinel-2b",
          "relative_orbit": 20
        },
        "pc_processing_baseline": "05.09",
        "pc_generation_time": "2023-04-28T12:23:11.362052+00:00",
        "contract": {
          "as103_version": "as103-v1",
          "as102_version": "as102-v1",
          "catalog": "https://planetarycomputer.microsoft.com/api/stac/v1/",
          "collection": "sentinel-2-l2a",
          "aoi_geometry_digest": "a0fdb745672b246f569400574aa299ae4e233b8012ef54e970cdacba56687c2a",
          "bands": [
            "B02",
            "B03",
            "B04",
            "B05",
            "B06",
            "B07",
            "B08",
            "B8A",
            "B11"
          ],
          "resampling": {
            "categorical": "nearest",
            "reflectance": "bilinear"
          },
          "mask_policy": {
            "aoi": "pixel-centre",
            "invalid_scl": [
              0,
              1,
              2,
              3,
              7,
              8,
              9,
              10,
              11
            ],
            "unknown": "invalid",
            "valid_scl": [
              4,
              5,
              6
            ],
            "water_scl": 6
          },
          "interpolation_support_policy": "native-3x3-water-erosion-plus-bilinear-all-support-v1",
          "decoding": {
            "band_ids": {
              "B02": "1",
              "B03": "2",
              "B04": "3",
              "B05": "4",
              "B06": "5",
              "B07": "6",
              "B08": "7",
              "B11": "11",
              "B8A": "8"
            },
            "offsets": {
              "B02": -1000.0,
              "B03": -1000.0,
              "B04": -1000.0,
              "B05": -1000.0,
              "B06": -1000.0,
              "B07": -1000.0,
              "B08": -1000.0,
              "B11": -1000.0,
              "B8A": -1000.0
            },
            "processing_baseline": "05.09",
            "quantification": 10000.0
          }
        }
      },
      {
        "product_id": "spectral:6409add4aef5c95cfe773bfabfa1f554bdda2968241712bda4debefa34b57130",
        "parent_product_id": "optical:038a425d46eead247826c4e1e735851a50325d896f1c95b99258840285bf31e1",
        "pc_source_id": "stac:ef177b34b0fa3cabbb6d613d65f1c55d8ea4c5959326bb8896ec51d111792740:sentinel-2-l2a:S2A_MSIL2A_20230304T064751_R020_T40RBN_20230304T113736",
        "pc_product_id": "S2A_MSIL2A_20230304T064751_R020_T40RBN_20230304T113736",
        "observation": {
          "acquired_at": "2023-03-04T06:47:51.024000+00:00",
          "mgrs_tile": "40RBN",
          "platform": "sentinel-2a",
          "relative_orbit": 20
        },
        "pc_processing_baseline": "05.09",
        "pc_generation_time": "2023-03-04T11:37:36.492429+00:00",
        "contract": {
          "as103_version": "as103-v1",
          "as102_version": "as102-v1",
          "catalog": "https://planetarycomputer.microsoft.com/api/stac/v1/",
          "collection": "sentinel-2-l2a",
          "aoi_geometry_digest": "a0fdb745672b246f569400574aa299ae4e233b8012ef54e970cdacba56687c2a",
          "bands": [
            "B02",
            "B03",
            "B04",
            "B05",
            "B06",
            "B07",
            "B08",
            "B8A",
            "B11"
          ],
          "resampling": {
            "categorical": "nearest",
            "reflectance": "bilinear"
          },
          "mask_policy": {
            "aoi": "pixel-centre",
            "invalid_scl": [
              0,
              1,
              2,
              3,
              7,
              8,
              9,
              10,
              11
            ],
            "unknown": "invalid",
            "valid_scl": [
              4,
              5,
              6
            ],
            "water_scl": 6
          },
          "interpolation_support_policy": "native-3x3-water-erosion-plus-bilinear-all-support-v1",
          "decoding": {
            "band_ids": {
              "B02": "1",
              "B03": "2",
              "B04": "3",
              "B05": "4",
              "B06": "5",
              "B07": "6",
              "B08": "7",
              "B11": "11",
              "B8A": "8"
            },
            "offsets": {
              "B02": -1000.0,
              "B03": -1000.0,
              "B04": -1000.0,
              "B05": -1000.0,
              "B06": -1000.0,
              "B07": -1000.0,
              "B08": -1000.0,
              "B11": -1000.0,
              "B8A": -1000.0
            },
            "processing_baseline": "05.09",
            "quantification": 10000.0
          }
        }
      },
      {
        "product_id": "spectral:dafde3d3a2a94d44b62a9d5605bce497b03021e517b7dd6b081607719f37efa1",
        "parent_product_id": "optical:a412b51188a9c47a0f121a5882fbf464490a66d19a96d3f682c0955398193644",
        "pc_source_id": "stac:ef177b34b0fa3cabbb6d613d65f1c55d8ea4c5959326bb8896ec51d111792740:sentinel-2-l2a:S2B_MSIL2A_20230309T064719_R020_T40RBN_20230309T121958",
        "pc_product_id": "S2B_MSIL2A_20230309T064719_R020_T40RBN_20230309T121958",
        "observation": {
          "acquired_at": "2023-03-09T06:47:19.025000+00:00",
          "mgrs_tile": "40RBN",
          "platform": "sentinel-2b",
          "relative_orbit": 20
        },
        "pc_processing_baseline": "05.09",
        "pc_generation_time": "2023-03-09T12:19:58.419331+00:00",
        "contract": {
          "as103_version": "as103-v1",
          "as102_version": "as102-v1",
          "catalog": "https://planetarycomputer.microsoft.com/api/stac/v1/",
          "collection": "sentinel-2-l2a",
          "aoi_geometry_digest": "a0fdb745672b246f569400574aa299ae4e233b8012ef54e970cdacba56687c2a",
          "bands": [
            "B02",
            "B03",
            "B04",
            "B05",
            "B06",
            "B07",
            "B08",
            "B8A",
            "B11"
          ],
          "resampling": {
            "categorical": "nearest",
            "reflectance": "bilinear"
          },
          "mask_policy": {
            "aoi": "pixel-centre",
            "invalid_scl": [
              0,
              1,
              2,
              3,
              7,
              8,
              9,
              10,
              11
            ],
            "unknown": "invalid",
            "valid_scl": [
              4,
              5,
              6
            ],
            "water_scl": 6
          },
          "interpolation_support_policy": "native-3x3-water-erosion-plus-bilinear-all-support-v1",
          "decoding": {
            "band_ids": {
              "B02": "1",
              "B03": "2",
              "B04": "3",
              "B05": "4",
              "B06": "5",
              "B07": "6",
              "B08": "7",
              "B11": "11",
              "B8A": "8"
            },
            "offsets": {
              "B02": -1000.0,
              "B03": -1000.0,
              "B04": -1000.0,
              "B05": -1000.0,
              "B06": -1000.0,
              "B07": -1000.0,
              "B08": -1000.0,
              "B11": -1000.0,
              "B8A": -1000.0
            },
            "processing_baseline": "05.09",
            "quantification": 10000.0
          }
        }
      },
      {
        "product_id": "spectral:721d847a7ed032426c8124e42507b60c3f9a6ae86a4e9ad406176646c35abff7",
        "parent_product_id": "optical:91cd94459703fb64b6c982d0d61403dcea8e766a99796b01d591d9ab6b9a67c2",
        "pc_source_id": "stac:ef177b34b0fa3cabbb6d613d65f1c55d8ea4c5959326bb8896ec51d111792740:sentinel-2-l2a:S2A_MSIL2A_20230314T064641_R020_T40RBN_20230314T123741",
        "pc_product_id": "S2A_MSIL2A_20230314T064641_R020_T40RBN_20230314T123741",
        "observation": {
          "acquired_at": "2023-03-14T06:46:41.024000+00:00",
          "mgrs_tile": "40RBN",
          "platform": "sentinel-2a",
          "relative_orbit": 20
        },
        "pc_processing_baseline": "05.09",
        "pc_generation_time": "2023-03-14T12:37:41.653527+00:00",
        "contract": {
          "as103_version": "as103-v1",
          "as102_version": "as102-v1",
          "catalog": "https://planetarycomputer.microsoft.com/api/stac/v1/",
          "collection": "sentinel-2-l2a",
          "aoi_geometry_digest": "a0fdb745672b246f569400574aa299ae4e233b8012ef54e970cdacba56687c2a",
          "bands": [
            "B02",
            "B03",
            "B04",
            "B05",
            "B06",
            "B07",
            "B08",
            "B8A",
            "B11"
          ],
          "resampling": {
            "categorical": "nearest",
            "reflectance": "bilinear"
          },
          "mask_policy": {
            "aoi": "pixel-centre",
            "invalid_scl": [
              0,
              1,
              2,
              3,
              7,
              8,
              9,
              10,
              11
            ],
            "unknown": "invalid",
            "valid_scl": [
              4,
              5,
              6
            ],
            "water_scl": 6
          },
          "interpolation_support_policy": "native-3x3-water-erosion-plus-bilinear-all-support-v1",
          "decoding": {
            "band_ids": {
              "B02": "1",
              "B03": "2",
              "B04": "3",
              "B05": "4",
              "B06": "5",
              "B07": "6",
              "B08": "7",
              "B11": "11",
              "B8A": "8"
            },
            "offsets": {
              "B02": -1000.0,
              "B03": -1000.0,
              "B04": -1000.0,
              "B05": -1000.0,
              "B06": -1000.0,
              "B07": -1000.0,
              "B08": -1000.0,
              "B11": -1000.0,
              "B8A": -1000.0
            },
            "processing_baseline": "05.09",
            "quantification": 10000.0
          }
        }
      },
      {
        "product_id": "spectral:1002b083b3d7637abd67446ef171e0746fe3bd839706cadff18571ac1c51af66",
        "parent_product_id": "optical:f812d226e81f482d912b0f0450ec3623e8a707f3a1774aaeaba2b27080b03ad2",
        "pc_source_id": "stac:ef177b34b0fa3cabbb6d613d65f1c55d8ea4c5959326bb8896ec51d111792740:sentinel-2-l2a:S2A_MSIL2A_20230324T064621_R020_T40RBN_20230324T114938",
        "pc_product_id": "S2A_MSIL2A_20230324T064621_R020_T40RBN_20230324T114938",
        "observation": {
          "acquired_at": "2023-03-24T06:46:21.024000+00:00",
          "mgrs_tile": "40RBN",
          "platform": "sentinel-2a",
          "relative_orbit": 20
        },
        "pc_processing_baseline": "05.09",
        "pc_generation_time": "2023-03-24T11:49:38.144656+00:00",
        "contract": {
          "as103_version": "as103-v1",
          "as102_version": "as102-v1",
          "catalog": "https://planetarycomputer.microsoft.com/api/stac/v1/",
          "collection": "sentinel-2-l2a",
          "aoi_geometry_digest": "a0fdb745672b246f569400574aa299ae4e233b8012ef54e970cdacba56687c2a",
          "bands": [
            "B02",
            "B03",
            "B04",
            "B05",
            "B06",
            "B07",
            "B08",
            "B8A",
            "B11"
          ],
          "resampling": {
            "categorical": "nearest",
            "reflectance": "bilinear"
          },
          "mask_policy": {
            "aoi": "pixel-centre",
            "invalid_scl": [
              0,
              1,
              2,
              3,
              7,
              8,
              9,
              10,
              11
            ],
            "unknown": "invalid",
            "valid_scl": [
              4,
              5,
              6
            ],
            "water_scl": 6
          },
          "interpolation_support_policy": "native-3x3-water-erosion-plus-bilinear-all-support-v1",
          "decoding": {
            "band_ids": {
              "B02": "1",
              "B03": "2",
              "B04": "3",
              "B05": "4",
              "B06": "5",
              "B07": "6",
              "B08": "7",
              "B11": "11",
              "B8A": "8"
            },
            "offsets": {
              "B02": -1000.0,
              "B03": -1000.0,
              "B04": -1000.0,
              "B05": -1000.0,
              "B06": -1000.0,
              "B07": -1000.0,
              "B08": -1000.0,
              "B11": -1000.0,
              "B8A": -1000.0
            },
            "processing_baseline": "05.09",
            "quantification": 10000.0
          }
        }
      },
      {
        "product_id": "spectral:c4de2a86bb7b15a6a8bc49373823bb944be7e6787db383b0959c93c51f3464d5",
        "parent_product_id": "optical:45360cce80a32aba72c755a3110b865575cc65d45eb96a27922f2dbc93d3aeee",
        "pc_source_id": "stac:ef177b34b0fa3cabbb6d613d65f1c55d8ea4c5959326bb8896ec51d111792740:sentinel-2-l2a:S2B_MSIL2A_20230329T064629_R020_T40RBN_20230329T132334",
        "pc_product_id": "S2B_MSIL2A_20230329T064629_R020_T40RBN_20230329T132334",
        "observation": {
          "acquired_at": "2023-03-29T06:46:29.024000+00:00",
          "mgrs_tile": "40RBN",
          "platform": "sentinel-2b",
          "relative_orbit": 20
        },
        "pc_processing_baseline": "05.09",
        "pc_generation_time": "2023-03-29T13:23:34.143592+00:00",
        "contract": {
          "as103_version": "as103-v1",
          "as102_version": "as102-v1",
          "catalog": "https://planetarycomputer.microsoft.com/api/stac/v1/",
          "collection": "sentinel-2-l2a",
          "aoi_geometry_digest": "a0fdb745672b246f569400574aa299ae4e233b8012ef54e970cdacba56687c2a",
          "bands": [
            "B02",
            "B03",
            "B04",
            "B05",
            "B06",
            "B07",
            "B08",
            "B8A",
            "B11"
          ],
          "resampling": {
            "categorical": "nearest",
            "reflectance": "bilinear"
          },
          "mask_policy": {
            "aoi": "pixel-centre",
            "invalid_scl": [
              0,
              1,
              2,
              3,
              7,
              8,
              9,
              10,
              11
            ],
            "unknown": "invalid",
            "valid_scl": [
              4,
              5,
              6
            ],
            "water_scl": 6
          },
          "interpolation_support_policy": "native-3x3-water-erosion-plus-bilinear-all-support-v1",
          "decoding": {
            "band_ids": {
              "B02": "1",
              "B03": "2",
              "B04": "3",
              "B05": "4",
              "B06": "5",
              "B07": "6",
              "B08": "7",
              "B11": "11",
              "B8A": "8"
            },
            "offsets": {
              "B02": -1000.0,
              "B03": -1000.0,
              "B04": -1000.0,
              "B05": -1000.0,
              "B06": -1000.0,
              "B07": -1000.0,
              "B08": -1000.0,
              "B11": -1000.0,
              "B8A": -1000.0
            },
            "processing_baseline": "05.09",
            "quantification": 10000.0
          }
        }
      }
    ],
    "algorithm": {
      "temporal": "start <= reference < end <= target; strictly prior; target excluded",
      "centre": "median; mean of two middle values for even history",
      "MAD": "median(abs(history - centre))",
      "MAD_factor": 1.4826,
      "deviation": "target - centre",
      "anomaly": "deviation / scale where scale > 0",
      "zero_scale": "baseline/deviation/rank valid; standardized anomaly masked NaN",
      "positive_scale": "direct float64 division; finite float32 result required",
      "rank": "(count(history < target) + 0.5*count(history == target))/n; exact ties",
      "support": "per-feature valid history at target feature-valid pixels only",
      "count_outside_target": 0,
      "arithmetic_dtype": "float64",
      "output_dtypes": {
        "centre": "float64",
        "scale": "float64",
        "deviation": "float64",
        "anomaly": "float32",
        "rank": "float32",
        "count": "uint32",
        "mask": "bool"
      },
      "statistics": "declared support; float64 linear percentiles [5,50,95]; None if empty",
      "summary_denominator": "target feature-valid pixel count",
      "clip": false
    },
    "input_fingerprints": {
      "format": "as104-input-v1",
      "target": "0195eb2c019109f0d5217cda7ea492cc73e68d35708758535f5df92aa8d00662",
      "references": [
        "6d4e3c1af4cdcc573ace48720e082e1b44463ed1697e2e32ef88c5475821333d",
        "467d8094d9fe6becafc2f50700fb90fcef54113a159b7109e468feeebdad319d",
        "0d60d267cc5cd9058fad51a56bd18574cbba84a48cf3048783e089a0142236bb",
        "eab8fb9314e7909be9a4bde8a7122234c360dcfde1398a38c8a6f3f0478d56d2",
        "c08237875c285d9eda54f98d7b28d5dabcdcd2b53fdf5c0bc598632c1439e26d"
      ]
    },
    "target_water_mask_digest": "537ec29587bf47509921c1ab0543d9e7698c496abdc49eae35c6fdf62fa71a35",
    "software_versions": {
      "python": "3.11.16",
      "numpy": "2.2.6"
    }
  },
  "output_content_fingerprint": "2a2902f946d49487f1416d0bd6ad73c7976910fe72060f03503540a49e2678dd",
  "combined_temporal_identity_fingerprint": "e814b0574ab30d1841778ee3c5005ffcb313ab42473c41acc028f0a9f7804a8b",
  "parents": [
    "spectral:dae91b4dda0131ca2d2987321abd2ffd5c4b5ffb2e95a44880b7a5f9a67ea64b",
    "spectral:6409add4aef5c95cfe773bfabfa1f554bdda2968241712bda4debefa34b57130",
    "spectral:dafde3d3a2a94d44b62a9d5605bce497b03021e517b7dd6b081607719f37efa1",
    "spectral:721d847a7ed032426c8124e42507b60c3f9a6ae86a4e9ad406176646c35abff7",
    "spectral:1002b083b3d7637abd67446ef171e0746fe3bd839706cadff18571ac1c51af66",
    "spectral:c4de2a86bb7b15a6a8bc49373823bb944be7e6787db383b0959c93c51f3464d5"
  ],
  "selected_reference_product_ids": [
    "spectral:6409add4aef5c95cfe773bfabfa1f554bdda2968241712bda4debefa34b57130",
    "spectral:dafde3d3a2a94d44b62a9d5605bce497b03021e517b7dd6b081607719f37efa1",
    "spectral:721d847a7ed032426c8124e42507b60c3f9a6ae86a4e9ad406176646c35abff7",
    "spectral:1002b083b3d7637abd67446ef171e0746fe3bd839706cadff18571ac1c51af66",
    "spectral:c4de2a86bb7b15a6a8bc49373823bb944be7e6787db383b0959c93c51f3464d5"
  ],
  "reference_acquired_at": [
    "2023-03-04T06:47:51.024000+00:00",
    "2023-03-09T06:47:19.025000+00:00",
    "2023-03-14T06:46:41.024000+00:00",
    "2023-03-24T06:46:21.024000+00:00",
    "2023-03-29T06:46:29.024000+00:00"
  ],
  "diagnostics": {
    "ndci_like": {
      "target_valid_count": 7963,
      "insufficient_history_count": 7171,
      "baseline_numeric_rejection_count": 0,
      "baseline_eligible_count": 792,
      "zero_MAD_count": 0,
      "anomaly_numeric_rejection_count": 0,
      "valid_anomaly_count": 792,
      "valid_rank_count": 792,
      "above_baseline_count": 148,
      "equal_baseline_count": 0,
      "below_baseline_count": 644
    },
    "mci_like": {
      "target_valid_count": 7963,
      "insufficient_history_count": 7161,
      "baseline_numeric_rejection_count": 0,
      "baseline_eligible_count": 802,
      "zero_MAD_count": 0,
      "anomaly_numeric_rejection_count": 0,
      "valid_anomaly_count": 802,
      "valid_rank_count": 802,
      "above_baseline_count": 234,
      "equal_baseline_count": 0,
      "below_baseline_count": 568
    },
    "red_edge_red_ratio": {
      "target_valid_count": 7963,
      "insufficient_history_count": 7162,
      "baseline_numeric_rejection_count": 0,
      "baseline_eligible_count": 801,
      "zero_MAD_count": 0,
      "anomaly_numeric_rejection_count": 0,
      "valid_anomaly_count": 801,
      "valid_rank_count": 801,
      "above_baseline_count": 148,
      "equal_baseline_count": 0,
      "below_baseline_count": 653
    },
    "red_edge2_red_ratio": {
      "target_valid_count": 7963,
      "insufficient_history_count": 7162,
      "baseline_numeric_rejection_count": 0,
      "baseline_eligible_count": 801,
      "zero_MAD_count": 0,
      "anomaly_numeric_rejection_count": 0,
      "valid_anomaly_count": 801,
      "valid_rank_count": 801,
      "above_baseline_count": 175,
      "equal_baseline_count": 0,
      "below_baseline_count": 626
    },
    "green_red_ratio": {
      "target_valid_count": 7963,
      "insufficient_history_count": 7162,
      "baseline_numeric_rejection_count": 0,
      "baseline_eligible_count": 801,
      "zero_MAD_count": 0,
      "anomaly_numeric_rejection_count": 0,
      "valid_anomaly_count": 801,
      "valid_rank_count": 801,
      "above_baseline_count": 743,
      "equal_baseline_count": 0,
      "below_baseline_count": 58
    },
    "green_blue_ratio": {
      "target_valid_count": 7963,
      "insufficient_history_count": 7166,
      "baseline_numeric_rejection_count": 0,
      "baseline_eligible_count": 797,
      "zero_MAD_count": 0,
      "anomaly_numeric_rejection_count": 0,
      "valid_anomaly_count": 797,
      "valid_rank_count": 797,
      "above_baseline_count": 195,
      "equal_baseline_count": 0,
      "below_baseline_count": 602
    }
  },
  "statistics": {
    "ndci_like": {
      "observation_count": {
        "valid_count": 7963,
        "fraction_of_target_feature_support": 1.0,
        "minimum": 0.0,
        "maximum": 5.0,
        "p05": 2.0,
        "median": 3.0,
        "p95": 5.0
      },
      "centre": {
        "valid_count": 792,
        "fraction_of_target_feature_support": 0.09946000251161623,
        "minimum": -0.23695190250873566,
        "maximum": 0.11026861518621445,
        "p05": -0.14804000928997993,
        "median": -0.10978342592716217,
        "p95": 0.0647963859140872
      },
      "scale": {
        "valid_count": 792,
        "fraction_of_target_feature_support": 0.09946000251161623,
        "minimum": 0.010280638629198074,
        "maximum": 0.3133194215029478,
        "p05": 0.04122927657097578,
        "median": 0.10278423307612539,
        "p95": 0.17034656289875505
      },
      "deviation": {
        "valid_count": 792,
        "fraction_of_target_feature_support": 0.09946000251161623,
        "minimum": -0.4319547787308693,
        "maximum": 0.18469946086406708,
        "p05": -0.251839966326952,
        "median": -0.05620687361806631,
        "p95": 0.05805237255990502
      },
      "standardized_anomaly": {
        "valid_count": 792,
        "fraction_of_target_feature_support": 0.09946000251161623,
        "minimum": -20.817241668701172,
        "maximum": 8.105969429016113,
        "p05": -2.4377148032188414,
        "median": -0.5830224752426147,
        "p95": 0.6918993145227421
      },
      "empirical_rank": {
        "valid_count": 792,
        "fraction_of_target_feature_support": 0.09946000251161623,
        "minimum": 0.0,
        "maximum": 1.0,
        "p05": 0.0,
        "median": 0.20000000298023224,
        "p95": 0.800000011920929
      }
    },
    "mci_like": {
      "observation_count": {
        "valid_count": 7963,
        "fraction_of_target_feature_support": 1.0,
        "minimum": 0.0,
        "maximum": 5.0,
        "p05": 2.0,
        "median": 3.0,
        "p95": 5.0
      },
      "centre": {
        "valid_count": 802,
        "fraction_of_target_feature_support": 0.10071581062413663,
        "minimum": -0.0072212498635053635,
        "maximum": 0.07434562593698502,
        "p05": 7.872413880249954e-05,
        "median": 0.0017617707489989698,
        "p95": 0.0485603168606758
      },
      "scale": {
        "valid_count": 802,
        "fraction_of_target_feature_support": 0.10071581062413663,
        "minimum": 5.0961267971433694e-05,
        "maximum": 0.04774032929241657,
        "p05": 0.00041422700973926113,
        "median": 0.0017193517775391228,
        "p95": 0.02290054349077847
      },
      "deviation": {
        "valid_count": 802,
        "fraction_of_target_feature_support": 0.10071581062413663,
        "minimum": -0.01163405692204833,
        "maximum": 0.031079187989234924,
        "p05": -0.003224405704531819,
        "median": -0.001116302504669875,
        "p95": 0.017755070887505917
      },
      "standardized_anomaly": {
        "valid_count": 802,
        "fraction_of_target_feature_support": 0.10071581062413663,
        "minimum": -63.16683578491211,
        "maximum": 13.631535530090332,
        "p05": -3.944103276729584,
        "median": -0.6549563705921173,
        "p95": 1.6396136045455931
      },
      "empirical_rank": {
        "valid_count": 802,
        "fraction_of_target_feature_support": 0.10071581062413663,
        "minimum": 0.0,
        "maximum": 1.0,
        "p05": 0.0,
        "median": 0.4000000059604645,
        "p95": 0.800000011920929
      }
    },
    "red_edge_red_ratio": {
      "observation_count": {
        "valid_count": 7963,
        "fraction_of_target_feature_support": 1.0,
        "minimum": 0.0,
        "maximum": 5.0,
        "p05": 2.0,
        "median": 3.0,
        "p95": 5.0
      },
      "centre": {
        "valid_count": 801,
        "fraction_of_target_feature_support": 0.1005902298128846,
        "minimum": 0.6168777346611023,
        "maximum": 1.2478694915771484,
        "p05": 0.7411804795265198,
        "median": 0.7980107665061951,
        "p95": 1.1371716260910034
      },
      "scale": {
        "valid_count": 801,
        "fraction_of_target_feature_support": 0.1005902298128846,
        "minimum": 0.015146414923667906,
        "maximum": 0.4264246285200119,
        "p05": 0.06547233545780182,
        "median": 0.16817683131694794,
        "p95": 0.26475287833213806
      },
      "deviation": {
        "valid_count": 801,
        "fraction_of_target_feature_support": 0.1005902298128846,
        "minimum": -0.47088199853897095,
        "maximum": 0.3564022183418274,
        "p05": -0.31567609310150146,
        "median": -0.09577429294586182,
        "p95": 0.0970771312713623
      },
      "standardized_anomaly": {
        "valid_count": 801,
        "fraction_of_target_feature_support": 0.1005902298128846,
        "minimum": -17.32849884033203,
        "maximum": 8.860766410827637,
        "p05": -2.196331024169922,
        "median": -0.5318223834037781,
        "p95": 0.7170291543006897
      },
      "empirical_rank": {
        "valid_count": 801,
        "fraction_of_target_feature_support": 0.1005902298128846,
        "minimum": 0.0,
        "maximum": 1.0,
        "p05": 0.20000000298023224,
        "median": 0.20000000298023224,
        "p95": 0.800000011920929
      }
    },
    "red_edge2_red_ratio": {
      "observation_count": {
        "valid_count": 7963,
        "fraction_of_target_feature_support": 1.0,
        "minimum": 0.0,
        "maximum": 5.0,
        "p05": 2.0,
        "median": 3.0,
        "p95": 5.0
      },
      "centre": {
        "valid_count": 801,
        "fraction_of_target_feature_support": 0.1005902298128846,
        "minimum": 0.26871705055236816,
        "maximum": 0.7763176560401917,
        "p05": 0.3382423520088196,
        "median": 0.49471965432167053,
        "p95": 0.6516971588134766
      },
      "scale": {
        "valid_count": 801,
        "fraction_of_target_feature_support": 0.1005902298128846,
        "minimum": 0.024924891901016235,
        "maximum": 1.047787526589632,
        "p05": 0.1641690820455551,
        "median": 0.31705965315699575,
        "p95": 0.5194493413316086
      },
      "deviation": {
        "valid_count": 801,
        "fraction_of_target_feature_support": 0.1005902298128846,
        "minimum": -0.8400785326957703,
        "maximum": 0.3815990686416626,
        "p05": -0.5340043157339096,
        "median": -0.1471763253211975,
        "p95": 0.20651564002037048
      },
      "standardized_anomaly": {
        "valid_count": 801,
        "fraction_of_target_feature_support": 0.1005902298128846,
        "minimum": -5.031539440155029,
        "maximum": 2.3333401679992676,
        "p05": -1.91908860206604,
        "median": -0.48816028237342834,
        "p95": 0.7898089289665222
      },
      "empirical_rank": {
        "valid_count": 801,
        "fraction_of_target_feature_support": 0.1005902298128846,
        "minimum": 0.0,
        "maximum": 0.800000011920929,
        "p05": 0.20000000298023224,
        "median": 0.20000000298023224,
        "p95": 0.800000011920929
      }
    },
    "green_red_ratio": {
      "observation_count": {
        "valid_count": 7963,
        "fraction_of_target_feature_support": 1.0,
        "minimum": 0.0,
        "maximum": 5.0,
        "p05": 2.0,
        "median": 3.0,
        "p95": 5.0
      },
      "centre": {
        "valid_count": 801,
        "fraction_of_target_feature_support": 0.1005902298128846,
        "minimum": 1.292543649673462,
        "maximum": 2.7369906902313232,
        "p05": 1.3614381551742554,
        "median": 2.4037017822265625,
        "p95": 2.6595213413238525
      },
      "scale": {
        "valid_count": 801,
        "fraction_of_target_feature_support": 0.1005902298128846,
        "minimum": 0.042700309753417966,
        "maximum": 1.3345879304409027,
        "p05": 0.1584987424850464,
        "median": 0.6159053089141845,
        "p95": 1.1602798224449158
      },
      "deviation": {
        "valid_count": 801,
        "fraction_of_target_feature_support": 0.1005902298128846,
        "minimum": -0.3479304313659668,
        "maximum": 4.3790061473846436,
        "p05": -0.012746930122375488,
        "median": 1.0123701095581055,
        "p95": 2.2095420360565186
      },
      "standardized_anomaly": {
        "valid_count": 801,
        "fraction_of_target_feature_support": 0.1005902298128846,
        "minimum": -2.016026735305786,
        "maximum": 24.031648635864258,
        "p05": -0.0360703244805336,
        "median": 1.282761573791504,
        "p95": 6.976260662078857
      },
      "empirical_rank": {
        "valid_count": 801,
        "fraction_of_target_feature_support": 0.1005902298128846,
        "minimum": 0.20000000298023224,
        "maximum": 1.0,
        "p05": 0.4000000059604645,
        "median": 0.800000011920929,
        "p95": 1.0
      }
    },
    "green_blue_ratio": {
      "observation_count": {
        "valid_count": 7963,
        "fraction_of_target_feature_support": 1.0,
        "minimum": 0.0,
        "maximum": 5.0,
        "p05": 2.0,
        "median": 3.0,
        "p95": 5.0
      },
      "centre": {
        "valid_count": 797,
        "fraction_of_target_feature_support": 0.10008790656787643,
        "minimum": 1.08492112159729,
        "maximum": 1.4380607604980469,
        "p05": 1.1208915710449219,
        "median": 1.1864646673202515,
        "p95": 1.302462863922119
      },
      "scale": {
        "valid_count": 797,
        "fraction_of_target_feature_support": 0.10008790656787643,
        "minimum": 0.010990204310417175,
        "maximum": 0.24364750792980192,
        "p05": 0.027868420786857608,
        "median": 0.08580181860923766,
        "p95": 0.1619193624973297
      },
      "deviation": {
        "valid_count": 797,
        "fraction_of_target_feature_support": 0.10008790656787643,
        "minimum": -0.2294062376022339,
        "maximum": 0.447177529335022,
        "p05": -0.14520041942596434,
        "median": -0.04636836051940918,
        "p95": 0.21677150726318348
      },
      "standardized_anomaly": {
        "valid_count": 797,
        "fraction_of_target_feature_support": 0.10008790656787643,
        "minimum": -14.008895874023438,
        "maximum": 12.86109447479248,
        "p05": -2.502164793014526,
        "median": -0.579097330570221,
        "p95": 2.2868128776550267
      },
      "empirical_rank": {
        "valid_count": 797,
        "fraction_of_target_feature_support": 0.10008790656787643,
        "minimum": 0.0,
        "maximum": 1.0,
        "p05": 0.0,
        "median": 0.20000000298023224,
        "p95": 0.800000011920929
      }
    }
  },
  "lineage": [
    "stac:ef177b34b0fa3cabbb6d613d65f1c55d8ea4c5959326bb8896ec51d111792740:sentinel-2-l2a:S2B_MSIL2A_20230428T064629_R020_T40RBN_20230428T122311",
    "optical:0725a908d21cd655e83f70d2bb11247dc0f1516f0c00ea275efc3239113ee4a6",
    "spectral:dae91b4dda0131ca2d2987321abd2ffd5c4b5ffb2e95a44880b7a5f9a67ea64b",
    "stac:ef177b34b0fa3cabbb6d613d65f1c55d8ea4c5959326bb8896ec51d111792740:sentinel-2-l2a:S2A_MSIL2A_20230304T064751_R020_T40RBN_20230304T113736",
    "optical:038a425d46eead247826c4e1e735851a50325d896f1c95b99258840285bf31e1",
    "spectral:6409add4aef5c95cfe773bfabfa1f554bdda2968241712bda4debefa34b57130",
    "stac:ef177b34b0fa3cabbb6d613d65f1c55d8ea4c5959326bb8896ec51d111792740:sentinel-2-l2a:S2B_MSIL2A_20230309T064719_R020_T40RBN_20230309T121958",
    "optical:a412b51188a9c47a0f121a5882fbf464490a66d19a96d3f682c0955398193644",
    "spectral:dafde3d3a2a94d44b62a9d5605bce497b03021e517b7dd6b081607719f37efa1",
    "stac:ef177b34b0fa3cabbb6d613d65f1c55d8ea4c5959326bb8896ec51d111792740:sentinel-2-l2a:S2A_MSIL2A_20230314T064641_R020_T40RBN_20230314T123741",
    "optical:91cd94459703fb64b6c982d0d61403dcea8e766a99796b01d591d9ab6b9a67c2",
    "spectral:721d847a7ed032426c8124e42507b60c3f9a6ae86a4e9ad406176646c35abff7",
    "stac:ef177b34b0fa3cabbb6d613d65f1c55d8ea4c5959326bb8896ec51d111792740:sentinel-2-l2a:S2A_MSIL2A_20230324T064621_R020_T40RBN_20230324T114938",
    "optical:f812d226e81f482d912b0f0450ec3623e8a707f3a1774aaeaba2b27080b03ad2",
    "spectral:1002b083b3d7637abd67446ef171e0746fe3bd839706cadff18571ac1c51af66",
    "stac:ef177b34b0fa3cabbb6d613d65f1c55d8ea4c5959326bb8896ec51d111792740:sentinel-2-l2a:S2B_MSIL2A_20230329T064629_R020_T40RBN_20230329T132334",
    "optical:45360cce80a32aba72c755a3110b865575cc65d45eb96a27922f2dbc93d3aeee",
    "spectral:c4de2a86bb7b15a6a8bc49373823bb944be7e6787db383b0959c93c51f3464d5",
    "temporal:e814b0574ab30d1841778ee3c5005ffcb313ab42473c41acc028f0a9f7804a8b"
  ],
  "lineage_edges": [
    [
      "stac:ef177b34b0fa3cabbb6d613d65f1c55d8ea4c5959326bb8896ec51d111792740:sentinel-2-l2a:S2B_MSIL2A_20230428T064629_R020_T40RBN_20230428T122311",
      "optical:0725a908d21cd655e83f70d2bb11247dc0f1516f0c00ea275efc3239113ee4a6"
    ],
    [
      "optical:0725a908d21cd655e83f70d2bb11247dc0f1516f0c00ea275efc3239113ee4a6",
      "spectral:dae91b4dda0131ca2d2987321abd2ffd5c4b5ffb2e95a44880b7a5f9a67ea64b"
    ],
    [
      "spectral:dae91b4dda0131ca2d2987321abd2ffd5c4b5ffb2e95a44880b7a5f9a67ea64b",
      "temporal:e814b0574ab30d1841778ee3c5005ffcb313ab42473c41acc028f0a9f7804a8b"
    ],
    [
      "stac:ef177b34b0fa3cabbb6d613d65f1c55d8ea4c5959326bb8896ec51d111792740:sentinel-2-l2a:S2A_MSIL2A_20230304T064751_R020_T40RBN_20230304T113736",
      "optical:038a425d46eead247826c4e1e735851a50325d896f1c95b99258840285bf31e1"
    ],
    [
      "optical:038a425d46eead247826c4e1e735851a50325d896f1c95b99258840285bf31e1",
      "spectral:6409add4aef5c95cfe773bfabfa1f554bdda2968241712bda4debefa34b57130"
    ],
    [
      "spectral:6409add4aef5c95cfe773bfabfa1f554bdda2968241712bda4debefa34b57130",
      "temporal:e814b0574ab30d1841778ee3c5005ffcb313ab42473c41acc028f0a9f7804a8b"
    ],
    [
      "stac:ef177b34b0fa3cabbb6d613d65f1c55d8ea4c5959326bb8896ec51d111792740:sentinel-2-l2a:S2B_MSIL2A_20230309T064719_R020_T40RBN_20230309T121958",
      "optical:a412b51188a9c47a0f121a5882fbf464490a66d19a96d3f682c0955398193644"
    ],
    [
      "optical:a412b51188a9c47a0f121a5882fbf464490a66d19a96d3f682c0955398193644",
      "spectral:dafde3d3a2a94d44b62a9d5605bce497b03021e517b7dd6b081607719f37efa1"
    ],
    [
      "spectral:dafde3d3a2a94d44b62a9d5605bce497b03021e517b7dd6b081607719f37efa1",
      "temporal:e814b0574ab30d1841778ee3c5005ffcb313ab42473c41acc028f0a9f7804a8b"
    ],
    [
      "stac:ef177b34b0fa3cabbb6d613d65f1c55d8ea4c5959326bb8896ec51d111792740:sentinel-2-l2a:S2A_MSIL2A_20230314T064641_R020_T40RBN_20230314T123741",
      "optical:91cd94459703fb64b6c982d0d61403dcea8e766a99796b01d591d9ab6b9a67c2"
    ],
    [
      "optical:91cd94459703fb64b6c982d0d61403dcea8e766a99796b01d591d9ab6b9a67c2",
      "spectral:721d847a7ed032426c8124e42507b60c3f9a6ae86a4e9ad406176646c35abff7"
    ],
    [
      "spectral:721d847a7ed032426c8124e42507b60c3f9a6ae86a4e9ad406176646c35abff7",
      "temporal:e814b0574ab30d1841778ee3c5005ffcb313ab42473c41acc028f0a9f7804a8b"
    ],
    [
      "stac:ef177b34b0fa3cabbb6d613d65f1c55d8ea4c5959326bb8896ec51d111792740:sentinel-2-l2a:S2A_MSIL2A_20230324T064621_R020_T40RBN_20230324T114938",
      "optical:f812d226e81f482d912b0f0450ec3623e8a707f3a1774aaeaba2b27080b03ad2"
    ],
    [
      "optical:f812d226e81f482d912b0f0450ec3623e8a707f3a1774aaeaba2b27080b03ad2",
      "spectral:1002b083b3d7637abd67446ef171e0746fe3bd839706cadff18571ac1c51af66"
    ],
    [
      "spectral:1002b083b3d7637abd67446ef171e0746fe3bd839706cadff18571ac1c51af66",
      "temporal:e814b0574ab30d1841778ee3c5005ffcb313ab42473c41acc028f0a9f7804a8b"
    ],
    [
      "stac:ef177b34b0fa3cabbb6d613d65f1c55d8ea4c5959326bb8896ec51d111792740:sentinel-2-l2a:S2B_MSIL2A_20230329T064629_R020_T40RBN_20230329T132334",
      "optical:45360cce80a32aba72c755a3110b865575cc65d45eb96a27922f2dbc93d3aeee"
    ],
    [
      "optical:45360cce80a32aba72c755a3110b865575cc65d45eb96a27922f2dbc93d3aeee",
      "spectral:c4de2a86bb7b15a6a8bc49373823bb944be7e6787db383b0959c93c51f3464d5"
    ],
    [
      "spectral:c4de2a86bb7b15a6a8bc49373823bb944be7e6787db383b0959c93c51f3464d5",
      "temporal:e814b0574ab30d1841778ee3c5005ffcb313ab42473c41acc028f0a9f7804a8b"
    ]
  ],
  "observation_count_histogram": {
    "ndci_like": {
      "0": 48,
      "1": 310,
      "2": 1838,
      "3": 2984,
      "4": 1991,
      "5": 792
    },
    "mci_like": {
      "0": 48,
      "1": 305,
      "2": 1823,
      "3": 2988,
      "4": 1997,
      "5": 802
    },
    "red_edge_red_ratio": {
      "0": 48,
      "1": 311,
      "2": 1844,
      "3": 2979,
      "4": 1980,
      "5": 801
    },
    "red_edge2_red_ratio": {
      "0": 48,
      "1": 311,
      "2": 1844,
      "3": 2979,
      "4": 1980,
      "5": 801
    },
    "green_red_ratio": {
      "0": 48,
      "1": 311,
      "2": 1844,
      "3": 2979,
      "4": 1980,
      "5": 801
    },
    "green_blue_ratio": {
      "0": 49,
      "1": 304,
      "2": 1828,
      "3": 2990,
      "4": 1995,
      "5": 797
    }
  },
  "selected_scalar_pixels": {
    "ndci_like": [
      [
        4,
        196
      ],
      [
        49,
        230
      ],
      [
        169,
        7
      ]
    ],
    "mci_like": [
      [
        4,
        196
      ],
      [
        49,
        232
      ],
      [
        169,
        7
      ]
    ],
    "red_edge_red_ratio": [
      [
        4,
        196
      ],
      [
        49,
        231
      ],
      [
        169,
        7
      ]
    ],
    "red_edge2_red_ratio": [
      [
        4,
        196
      ],
      [
        49,
        231
      ],
      [
        169,
        7
      ]
    ],
    "green_red_ratio": [
      [
        4,
        196
      ],
      [
        49,
        231
      ],
      [
        169,
        7
      ]
    ],
    "green_blue_ratio": [
      [
        4,
        196
      ],
      [
        49,
        231
      ],
      [
        169,
        7
      ]
    ]
  },
  "scalar_checks": [
    {
      "row": 4,
      "column": 196,
      "feature": "ndci_like",
      "historical_values": [
        -0.3452685475349426,
        -0.2050359845161438,
        0.08135417103767395,
        -0.13192827999591827,
        -0.10666165500879288
      ],
      "target_value": -0.14446841180324554,
      "median": -0.13192827999591827,
      "absolute_deviations": [
        0.21334026753902435,
        0.07310770452022552,
        0.21328245103359222,
        0.0,
        0.025266624987125397
      ],
      "MAD": 0.07310770452022552,
      "scale": 0.10838948272168636,
      "deviation": -0.01254013180732727,
      "standardized_anomaly": -0.11569509655237198,
      "empirical_midrank": 0.4,
      "stored_rank_float32": 0.4000000059604645,
      "status": "PASS"
    },
    {
      "row": 49,
      "column": 230,
      "feature": "ndci_like",
      "historical_values": [
        14.835051536560059,
        -0.15922918915748596,
        0.11467324942350388,
        -0.09956394881010056,
        -0.05342068895697594
      ],
      "target_value": -0.18019309639930725,
      "median": -0.05342068895697594,
      "absolute_deviations": [
        14.888472225517035,
        0.10580850020051003,
        0.1680939383804798,
        0.04614325985312462,
        0.0
      ],
      "MAD": 0.10580850020051003,
      "scale": 0.15687168239727614,
      "deviation": -0.12677240744233131,
      "standardized_anomaly": -0.8081280589103699,
      "empirical_midrank": 0.0,
      "stored_rank_float32": 0.0,
      "status": "PASS"
    },
    {
      "row": 169,
      "column": 7,
      "feature": "ndci_like",
      "historical_values": [
        0.03315882384777069,
        -0.13466061651706696,
        0.0749988853931427,
        -0.12425724416971207,
        -0.18462993204593658
      ],
      "target_value": -0.4131714105606079,
      "median": -0.12425724416971207,
      "absolute_deviations": [
        0.15741606801748276,
        0.010403372347354889,
        0.19925612956285477,
        0.0,
        0.06037268787622452
      ],
      "MAD": 0.06037268787622452,
      "scale": 0.08950854704529046,
      "deviation": -0.28891416639089584,
      "standardized_anomaly": -3.227782964706421,
      "empirical_midrank": 0.0,
      "stored_rank_float32": 0.0,
      "status": "PASS"
    },
    {
      "row": 4,
      "column": 196,
      "feature": "mci_like",
      "historical_values": [
        -0.0010005207732319832,
        0.0006533326231874526,
        -0.004838230554014444,
        0.002512814709916711,
        0.000998436938971281
      ],
      "target_value": -0.0003396871325094253,
      "median": 0.0006533326231874526,
      "absolute_deviations": [
        0.0016538533964194357,
        0.0,
        0.005491563177201897,
        0.0018594820867292583,
        0.0003451043157838285
      ],
      "MAD": 0.0016538533964194357,
      "scale": 0.0024520030455314553,
      "deviation": -0.0009930197556968778,
      "standardized_anomaly": -0.4049830734729767,
      "empirical_midrank": 0.4,
      "stored_rank_float32": 0.4000000059604645,
      "status": "PASS"
    },
    {
      "row": 49,
      "column": 232,
      "feature": "mci_like",
      "historical_values": [
        -0.0001131248936871998,
        0.002032812684774399,
        0.00031177030177786946,
        0.0022656256332993507,
        0.0034265615977346897
      ],
      "target_value": 0.00021218735491856933,
      "median": 0.002032812684774399,
      "absolute_deviations": [
        0.0021459375784615986,
        0.0,
        0.0017210423829965293,
        0.00023281294852495193,
        0.001393748912960291
      ],
      "MAD": 0.001393748912960291,
      "scale": 0.0020663721383549273,
      "deviation": -0.0018206253298558295,
      "standardized_anomaly": -0.8810732960700989,
      "empirical_midrank": 0.2,
      "stored_rank_float32": 0.20000000298023224,
      "status": "PASS"
    },
    {
      "row": 169,
      "column": 7,
      "feature": "mci_like",
      "historical_values": [
        0.006310000084340572,
        0.0051758321933448315,
        0.0007554153562523425,
        -0.00035364629002287984,
        -0.0034490623511373997
      ],
      "target_value": -0.005822812207043171,
      "median": 0.0007554153562523425,
      "absolute_deviations": [
        0.00555458472808823,
        0.004420416837092489,
        0.0,
        0.0011090616462752223,
        0.004204477707389742
      ],
      "MAD": 0.004204477707389742,
      "scale": 0.006233558648976031,
      "deviation": -0.006578227563295513,
      "standardized_anomaly": -1.0552924871444702,
      "empirical_midrank": 0.0,
      "stored_rank_float32": 0.0,
      "status": "PASS"
    },
    {
      "row": 4,
      "column": 196,
      "feature": "red_edge_red_ratio",
      "historical_values": [
        0.48669201135635376,
        0.6597014665603638,
        1.1771175861358643,
        0.7668964266777039,
        0.8072370886802673
      ],
      "target_value": 0.7475362420082092,
      "median": 0.7668964266777039,
      "absolute_deviations": [
        0.2802044153213501,
        0.10719496011734009,
        0.4102211594581604,
        0.0,
        0.04034066200256348
      ],
      "MAD": 0.10719496011734009,
      "scale": 0.1589272478699684,
      "deviation": -0.01936018466949463,
      "standardized_anomaly": -0.12181790918111801,
      "empirical_midrank": 0.4,
      "stored_rank_float32": 0.4000000059604645,
      "status": "PASS"
    },
    {
      "row": 49,
      "column": 231,
      "feature": "red_edge_red_ratio",
      "historical_values": [
        -1.1004126071929932,
        0.6940829753875732,
        1.2578226327896118,
        0.8078470826148987,
        0.9200665354728699
      ],
      "target_value": 0.5692108869552612,
      "median": 0.8078470826148987,
      "absolute_deviations": [
        1.9082596898078918,
        0.11376410722732544,
        0.44997555017471313,
        0.0,
        0.11221945285797119
      ],
      "MAD": 0.11376410722732544,
      "scale": 0.1686666653752327,
      "deviation": -0.23863619565963745,
      "standardized_anomaly": -1.4148391485214233,
      "empirical_midrank": 0.2,
      "stored_rank_float32": 0.20000000298023224,
      "status": "PASS"
    },
    {
      "row": 169,
      "column": 7,
      "feature": "red_edge_red_ratio",
      "historical_values": [
        1.0685920715332031,
        0.7626416087150574,
        1.1621595621109009,
        0.7789523005485535,
        0.6882909536361694
      ],
      "target_value": 0.41525647044181824,
      "median": 0.7789523005485535,
      "absolute_deviations": [
        0.28963977098464966,
        0.016310691833496094,
        0.3832072615623474,
        0.0,
        0.09066134691238403
      ],
      "MAD": 0.09066134691238403,
      "scale": 0.13441451293230056,
      "deviation": -0.36369583010673523,
      "standardized_anomaly": -2.705777883529663,
      "empirical_midrank": 0.0,
      "stored_rank_float32": 0.0,
      "status": "PASS"
    },
    {
      "row": 4,
      "column": 196,
      "feature": "red_edge2_red_ratio",
      "historical_values": [
        0.2549339234828949,
        0.3253731429576874,
        1.0703691244125366,
        0.4605723023414612,
        0.5997211337089539
      ],
      "target_value": 0.5762258172035217,
      "median": 0.4605723023414612,
      "absolute_deviations": [
        0.20563837885856628,
        0.1351991593837738,
        0.6097968220710754,
        0.0,
        0.13914883136749268
      ],
      "MAD": 0.13914883136749268,
      "scale": 0.20630205738544463,
      "deviation": 0.11565351486206055,
      "standardized_anomaly": 0.5606028437614441,
      "empirical_midrank": 0.6,
      "stored_rank_float32": 0.6000000238418579,
      "status": "PASS"
    },
    {
      "row": 49,
      "column": 231,
      "feature": "red_edge2_red_ratio",
      "historical_values": [
        -2.6409902572631836,
        0.2748568654060364,
        1.48125159740448,
        0.5252256393432617,
        0.6921796202659607
      ],
      "target_value": 0.11384217441082001,
      "median": 0.5252256393432617,
      "absolute_deviations": [
        3.1662158966064453,
        0.25036877393722534,
        0.9560259580612183,
        0.0,
        0.16695398092269897
      ],
      "MAD": 0.25036877393722534,
      "scale": 0.37119674423933025,
      "deviation": -0.4113834649324417,
      "standardized_anomaly": -1.108262538909912,
      "empirical_midrank": 0.2,
      "stored_rank_float32": 0.20000000298023224,
      "status": "PASS"
    },
    {
      "row": 169,
      "column": 7,
      "feature": "red_edge2_red_ratio",
      "historical_values": [
        0.2743682265281677,
        0.3404255211353302,
        1.326174020767212,
        0.5996865630149841,
        0.5943074822425842
      ],
      "target_value": 0.5162648558616638,
      "median": 0.5943074822425842,
      "absolute_deviations": [
        0.3199392557144165,
        0.25388196110725403,
        0.7318665385246277,
        0.005379080772399902,
        0.0
      ],
      "MAD": 0.25388196110725403,
      "scale": 0.3764053955376148,
      "deviation": -0.07804262638092041,
      "standardized_anomaly": -0.2073366343975067,
      "empirical_midrank": 0.4,
      "stored_rank_float32": 0.4000000059604645,
      "status": "PASS"
    },
    {
      "row": 4,
      "column": 196,
      "feature": "green_red_ratio",
      "historical_values": [
        3.6317219734191895,
        2.646688461303711,
        -0.17445790767669678,
        2.5366101264953613,
        2.0997049808502197
      ],
      "target_value": 3.0751914978027344,
      "median": 2.5366101264953613,
      "absolute_deviations": [
        1.0951118469238281,
        0.11007833480834961,
        2.711068034172058,
        0.0,
        0.4369051456451416
      ],
      "MAD": 0.4369051456451416,
      "scale": 0.6477555689334868,
      "deviation": 0.538581371307373,
      "standardized_anomaly": 0.8314577341079712,
      "empirical_midrank": 0.8,
      "stored_rank_float32": 0.800000011920929,
      "status": "PASS"
    },
    {
      "row": 49,
      "column": 231,
      "feature": "green_red_ratio",
      "historical_values": [
        12.26822566986084,
        2.708528757095337,
        -0.4572450518608093,
        2.7464144229888916,
        1.9122793674468994
      ],
      "target_value": 3.9511642456054688,
      "median": 2.708528757095337,
      "absolute_deviations": [
        9.559696912765503,
        0.0,
        3.1657738089561462,
        0.03788566589355469,
        0.7962493896484375
      ],
      "MAD": 0.7962493896484375,
      "scale": 1.1805193450927733,
      "deviation": 1.2426354885101318,
      "standardized_anomaly": 1.0526176691055298,
      "empirical_midrank": 0.8,
      "stored_rank_float32": 0.800000011920929,
      "status": "PASS"
    },
    {
      "row": 169,
      "column": 7,
      "feature": "green_red_ratio",
      "historical_values": [
        3.849729299545288,
        2.3890576362609863,
        0.056184712797403336,
        2.340524911880493,
        2.2908477783203125
      ],
      "target_value": 2.7247698307037354,
      "median": 2.340524911880493,
      "absolute_deviations": [
        1.509204387664795,
        0.048532724380493164,
        2.28434019908309,
        0.0,
        0.049677133560180664
      ],
      "MAD": 0.049677133560180664,
      "scale": 0.07365131821632386,
      "deviation": 0.3842449188232422,
      "standardized_anomaly": 5.217081546783447,
      "empirical_midrank": 0.8,
      "stored_rank_float32": 0.800000011920929,
      "status": "PASS"
    },
    {
      "row": 4,
      "column": 196,
      "feature": "green_blue_ratio",
      "historical_values": [
        1.1343739032745361,
        1.1957391500473022,
        -0.5268173217773438,
        1.1843974590301514,
        1.0830378532409668
      ],
      "target_value": 1.0301190614700317,
      "median": 1.1343739032745361,
      "absolute_deviations": [
        0.0,
        0.06136524677276611,
        1.6611912250518799,
        0.050023555755615234,
        0.051336050033569336
      ],
      "MAD": 0.051336050033569336,
      "scale": 0.0761108277797699,
      "deviation": -0.1042548418045044,
      "standardized_anomaly": -1.369776725769043,
      "empirical_midrank": 0.2,
      "stored_rank_float32": 0.20000000298023224,
      "status": "PASS"
    },
    {
      "row": 49,
      "column": 231,
      "feature": "green_blue_ratio",
      "historical_values": [
        1.1235120296478271,
        1.3117016553878784,
        -1.360826015472412,
        1.2259787321090698,
        1.1097720861434937
      ],
      "target_value": 1.0791449546813965,
      "median": 1.1235120296478271,
      "absolute_deviations": [
        0.0,
        0.18818962574005127,
        2.4843380451202393,
        0.10246670246124268,
        0.013739943504333496
      ],
      "MAD": 0.10246670246124268,
      "scale": 0.1519171330690384,
      "deviation": -0.044367074966430664,
      "standardized_anomaly": -0.2920478582382202,
      "empirical_midrank": 0.2,
      "stored_rank_float32": 0.20000000298023224,
      "status": "PASS"
    },
    {
      "row": 169,
      "column": 7,
      "feature": "green_blue_ratio",
      "historical_values": [
        1.4158748388290405,
        1.1266614198684692,
        0.12768317759037018,
        1.1566284894943237,
        1.112999677658081
      ],
      "target_value": 1.1553704738616943,
      "median": 1.1266614198684692,
      "absolute_deviations": [
        0.2892134189605713,
        0.0,
        0.9989782422780991,
        0.029967069625854492,
        0.013661742210388184
      ],
      "MAD": 0.029967069625854492,
      "scale": 0.04442917742729187,
      "deviation": 0.028709053993225098,
      "standardized_anomaly": 0.6461756825447083,
      "empirical_midrank": 0.6,
      "stored_rank_float32": 0.6000000238418579,
      "status": "PASS"
    }
  ],
  "scalar_validation_status": "PASS",
  "deterministic_repeat": {
    "status": "PASS",
    "arrays_masks_statistics_diagnostics_fingerprints_parents_identity": "equal",
    "first_created_at": "2026-10-09T08:01:50.739354+00:00",
    "repeat_created_at": "2026-10-09T08:01:50.898553+00:00"
  },
  "causal_future_check": {
    "status": "PASS",
    "control_type": "synthetic later-date scene cloned from accepted real target; not a real future observation",
    "acquisition_utc": "2023-05-03T06:46:29.024000+00:00",
    "feature_mutation": "mci_like +float32 0.001 on valid support; summary updated",
    "mutation_count": 7963,
    "unselected_control_not_registered": true,
    "control_not_in_direct_parents": true,
    "selected_references_arrays_masks_diagnostics_summaries_fingerprints_parents_product_id": "unchanged",
    "future_raster_processed": false
  },
  "accepted_target_cache_hashes": {
    "data/cache/as102/038a425d46eead247826c4e1e735851a50325d896f1c95b99258840285bf31e1/arrays.npz": "7c586ae3c546f7dabea0ccc0e9f2c99e0435e4b563aedb93043e90d8077a7cea",
    "data/cache/as102/038a425d46eead247826c4e1e735851a50325d896f1c95b99258840285bf31e1/manifest.json": "36f5e8598889fd1df081f699755df3a70aed0550455a97e194eda4aae9400a50",
    "data/cache/as102/0725a908d21cd655e83f70d2bb11247dc0f1516f0c00ea275efc3239113ee4a6/arrays.npz": "01512aa7ec3e1deab0f87fddb9c3888986d449ebcdd440830a7d4805bbc4f4a1",
    "data/cache/as102/0725a908d21cd655e83f70d2bb11247dc0f1516f0c00ea275efc3239113ee4a6/manifest.json": "9a5ca8d78b663426fd53732a52db387c15fe8a70acb2da93978a9f466ce15589",
    "data/cache/as102/45360cce80a32aba72c755a3110b865575cc65d45eb96a27922f2dbc93d3aeee/arrays.npz": "dd571a6f3c6eec4fbf05879e596a17cd5a3ceca76b23fe191a709ac0233ab749",
    "data/cache/as102/45360cce80a32aba72c755a3110b865575cc65d45eb96a27922f2dbc93d3aeee/manifest.json": "fae0be0d9bcb1222aaf5c2bd1c74861dbaf7a3936f8c6561bd19d88d2d60fdd9",
    "data/cache/as102/91cd94459703fb64b6c982d0d61403dcea8e766a99796b01d591d9ab6b9a67c2/arrays.npz": "632b73ed78f14ee70a3323b670ccdfb79a94a7c9ed02a59c25f49cd22f52ce38",
    "data/cache/as102/91cd94459703fb64b6c982d0d61403dcea8e766a99796b01d591d9ab6b9a67c2/manifest.json": "be38645eae60b1d1c020a61bebf4bf61f9796c796378c36fc7ff61398d5afa1d",
    "data/cache/as102/a412b51188a9c47a0f121a5882fbf464490a66d19a96d3f682c0955398193644/arrays.npz": "6186a2706c7b5b18089b897b421d2526f64f19e853682b03a4e19edc85248352",
    "data/cache/as102/a412b51188a9c47a0f121a5882fbf464490a66d19a96d3f682c0955398193644/manifest.json": "0d0827ddccade1082fce982e188eed4f60c1e160eb88dc5033a6d0e9c7c5e6e6",
    "data/cache/as102/f812d226e81f482d912b0f0450ec3623e8a707f3a1774aaeaba2b27080b03ad2/arrays.npz": "1b4136081a45be25b787ed752c01e67419f1a98e6229663cc945592cfba950f9",
    "data/cache/as102/f812d226e81f482d912b0f0450ec3623e8a707f3a1774aaeaba2b27080b03ad2/manifest.json": "0db0e1a0492cab09dd043a89a6e6c332d533a9097c22bd2a4093bb40da2254a8"
  },
  "accepted_target_cache_preservation": "PASS",
  "credential_scan": {
    "live_credential_matches": 0,
    "files_scanned": 99,
    "actual_token_available_for_in_memory_comparison": false
  },
  "network_guard": {
    "attempts": 0,
    "network_used": false,
    "policy": "Python socket connect/DNS audit events rejected; known-ID production cache path only"
  },
  "completed_utc": "2026-10-09T08:01:51.327507+00:00",
  "completed_dubai": "2026-10-09T12:01:51.327507+04:00",
  "all_six_cache_preservation": "PASS",
  "all_six_cache_hashes": {
    "data/cache/as102/038a425d46eead247826c4e1e735851a50325d896f1c95b99258840285bf31e1/arrays.npz": "7c586ae3c546f7dabea0ccc0e9f2c99e0435e4b563aedb93043e90d8077a7cea",
    "data/cache/as102/038a425d46eead247826c4e1e735851a50325d896f1c95b99258840285bf31e1/manifest.json": "36f5e8598889fd1df081f699755df3a70aed0550455a97e194eda4aae9400a50",
    "data/cache/as102/0725a908d21cd655e83f70d2bb11247dc0f1516f0c00ea275efc3239113ee4a6/arrays.npz": "01512aa7ec3e1deab0f87fddb9c3888986d449ebcdd440830a7d4805bbc4f4a1",
    "data/cache/as102/0725a908d21cd655e83f70d2bb11247dc0f1516f0c00ea275efc3239113ee4a6/manifest.json": "9a5ca8d78b663426fd53732a52db387c15fe8a70acb2da93978a9f466ce15589",
    "data/cache/as102/45360cce80a32aba72c755a3110b865575cc65d45eb96a27922f2dbc93d3aeee/arrays.npz": "dd571a6f3c6eec4fbf05879e596a17cd5a3ceca76b23fe191a709ac0233ab749",
    "data/cache/as102/45360cce80a32aba72c755a3110b865575cc65d45eb96a27922f2dbc93d3aeee/manifest.json": "fae0be0d9bcb1222aaf5c2bd1c74861dbaf7a3936f8c6561bd19d88d2d60fdd9",
    "data/cache/as102/91cd94459703fb64b6c982d0d61403dcea8e766a99796b01d591d9ab6b9a67c2/arrays.npz": "632b73ed78f14ee70a3323b670ccdfb79a94a7c9ed02a59c25f49cd22f52ce38",
    "data/cache/as102/91cd94459703fb64b6c982d0d61403dcea8e766a99796b01d591d9ab6b9a67c2/manifest.json": "be38645eae60b1d1c020a61bebf4bf61f9796c796378c36fc7ff61398d5afa1d",
    "data/cache/as102/a412b51188a9c47a0f121a5882fbf464490a66d19a96d3f682c0955398193644/arrays.npz": "6186a2706c7b5b18089b897b421d2526f64f19e853682b03a4e19edc85248352",
    "data/cache/as102/a412b51188a9c47a0f121a5882fbf464490a66d19a96d3f682c0955398193644/manifest.json": "0d0827ddccade1082fce982e188eed4f60c1e160eb88dc5033a6d0e9c7c5e6e6",
    "data/cache/as102/f812d226e81f482d912b0f0450ec3623e8a707f3a1774aaeaba2b27080b03ad2/arrays.npz": "1b4136081a45be25b787ed752c01e67419f1a98e6229663cc945592cfba950f9",
    "data/cache/as102/f812d226e81f482d912b0f0450ec3623e8a707f3a1774aaeaba2b27080b03ad2/manifest.json": "0db0e1a0492cab09dd043a89a6e6c332d533a9097c22bd2a4093bb40da2254a8"
  }
}
```

### Scientific limits and next gate

Candidate temporal L2A BOA signals are not aquatic Rrs, confirmed HAB/bloom,
chlorophyll concentration, species/toxin evidence, water safety, intake risk or
shutdown advice, persistence, operational alerts or warning lead time. Rank is
not probability/confidence/severity. Five observations are not statistical
sufficiency. Retrospective acquisition causality does not prove historical
operational availability. Positive but small scales can yield large z values;
no clipping, epsilon/fallback, thresholds, event labels or mask relaxation.
The future control validates exclusion only and is synthetic.

Owner review is next. Entire AS-104 work remains uncommitted; both stashes and
all recovery artifacts retained. No Decision 050, commit/push/PR/merge, AS-105+
or P1 05.10 study. Final post-documentation quality/security gate is recorded below.

### Final post-documentation quality and preservation gate

`python -m pytest -v`: **663 passed, 6 warnings in 18.55s**.
`python -m ruff check .`: **PASS**. `git diff --check`: **PASS**.
All ten non-ignored untracked files passed independent whitespace checks.
Warnings remain the six historical Rasterio PendingDeprecationWarning instances.

The read-only final audit passed every check: exactly nine owner-authorized
paths changed since the pre-fix inventory (two source/test and seven documents);
the baseline delta is exactly the one `.casefold()` predicate. All other
source/tests/configuration/dependency/provenance/transport files are byte-identical.
All twelve AS-102 cache-file hashes and all six AS-102/AS-103 IDs/content
fingerprints/grids/source IDs remain unchanged. Every prior decision, milestone,
engineering and detailed evidence body is preserved; M24–M25/E24–E25/EV-028–
EV-029 occur once in order. Prior AS-104 plan/evidence and decision log remain
intact prefixes with appended execution records; no Decision 050.

Repository/cache scan: **3,010 actual files scanned**, **0 unrecognized long SAS
signature values**, **16 known synthetic signature literals**. The cached
acceptance observed zero socket/DNS attempts and acquired no live token.
No live signed URL/token was printed or persisted. Both stashes and all five
old/new recovery artifacts remain available. HEAD/origin-main and branch remain
unchanged; index empty, no conflicts, work intentionally uncommitted. No
commit/push/PR/merge, AS-105+ or P1 homogeneous-05.10 robustness experiment.
