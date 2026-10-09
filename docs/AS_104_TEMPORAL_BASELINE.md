# AS-104 — Temporal Baseline

**Current AS-104 closeout status — 9 October 2026 (Asia/Dubai), M27/E27/EV-031:**
**AS-104: COMPLETE AND MERGED** through [PR #12](https://github.com/Omar-Aboulwafa/aquasentinel-813/pull/12).
**AS-104 implementation merge commit:** `472edc737847dc8581290a372c5da28f71fc48f0`.
Feature implementation commit: `09b38bd9c312470e948b1f17165ec5335cfc149d`.
Publication documentation commit / final PR head: `703af1176aeaf9ba38d31c53648907c3b1792aec`.
Merged **2026-10-09T09:26:08Z** / **2026-10-09T13:26:08+04:00 Asia/Dubai**.
Real acceptance **PASS**; no unresolved AS-104 P0 blocker. Known scientific and
coverage limitations remain documented. Current active development branch: **none**;
AS-104 development is closed. This closeout was prepared on `docs/as-104-closeout`.
Next step: owner review of the next milestone/AS-105 design before implementation;
separate authorization is required. AS-105+ and P1 homogeneous 05.10 **NOT STARTED**.
M23–M26/E23–E26/EV-027–EV-030 retain their dated historical blocker, fix, acceptance
and publication states, including then-pending PR/merge language. M27/E27/EV-031
records the later merge/closeout; it is an execution/history event, not Decision 050.
Both safety stashes and external recovery artifacts are retained historical recovery
material. No EO experiment rerun or source/test/math/cache changes in this closeout.
See [merge/closeout evidence §9](evidence/AS_104_TEMPORAL_BASELINE_VALIDATION.md#9-pr-12-merge-and-as-104-closeout--9-october-2026).

**Historical AS-104 publication status — before PR #12 merge, 9 October 2026 (Asia/Dubai), M26/E26/EV-030:**
Implementation and real acceptance **PASS**; feature commit
`09b38bd9c312470e948b1f17165ec5335cfc149d` is **COMMITTED AND PUSHED**,
parent/base `2006df7a70a4f48c66933aed96f4464d8d03084e`.
Branch `feature/as-104-temporal-baseline`; remote/upstream
`origin/feature/as-104-temporal-baseline`. Feature publication verified equal
local/remote SHA and a **clean worktree**. This reconciliation is documentation only.
**PR NOT YET CREATED; merge NOT YET PERFORMED.** Review the published commit and
open a PR if review passes and creation is authorized; this task creates no PR.
M23/E23/EV-027 remains historically BLOCKED; M24–M25/E24–E25/EV-028–EV-029 remain
acceptance-time PASS. Their earlier stop states below are historical, not current
Git status. M26/E26/EV-030 separates later publication from acceptance completion.
No Decision 050; both stashes/recovery artifacts retained; AS-105+ and P1 05.10
**NOT STARTED**. No science, source/tests, caches or experiment timestamps changed.
Exact publication metadata/times and unchanged acceptance evidence are in
[validation §8](evidence/AS_104_TEMPORAL_BASELINE_VALIDATION.md#8-as-104-feature-publication--9-october-2026).

The original planning/dated execution records below retain their then-current
stop-state instructions unchanged. Their uncommitted/no-push language is historical.

## Task

Explicitly authorized on 8 October 2026 (Asia/Dubai). Branch:
`feature/as-104-temporal-baseline`; exact base main:
`c6accab2c5753734466a6375d1b3ce1762e99bed`. Leave changes uncommitted for review.
This execution plan was created before AS-104 source implementation.

## Goal

Produce deterministic causal, target-specific, per-feature/pixel temporal
comparisons from validated AS-103 scenes, without interpreting events or risk.

## Inputs

AS-103 `SpectralFeatureScene` collection containing the target exactly once;
target product ID; explicit timezone-aware reference bounds; required integer
`minimum_observations` (3 through uint32 maximum, no booleans); populated
in-memory provenance registry. P0 real acceptance passes exactly 5.

## Outputs

Typed `TemporalFeatureScene` and per-feature `TemporalFeatureResult`, unchanged
grid, copied target masks, observation counts, centre/scale/deviation, signed
standardized anomaly, empirical midrank, typed summaries/diagnostics, semantic
input fingerprints and immediate-AS-103-parent provenance. No disk cache.

## Files Likely to Change

Add `src/aquasentinel/temporal/{__init__,models,baseline}.py`, focused files under
`tests/temporal/`, this plan, and
`docs/evidence/AS_104_TEMPORAL_BASELINE_VALIDATION.md`. Update only Decisions,
Project State, Handoff, Presentation Journal and Presentation Evidence Index.
Do not change upstream algorithms, generic provenance, config or dependencies.

## Dependencies

None added. Existing NumPy and standard-library dataclasses, datetime, canonical
JSON and SHA-256 suffice. Reuse existing feature/grid/provenance types and the
stable JSON guard. Computation has no retrieval, signing, raster-read or write IO.

## Acceptance Criteria

- Primary API: `compute_temporal_anomaly(scenes, *, target_product_id,
  reference_start, reference_end=None, minimum_observations, registry)`.
- References satisfy start <= acquisition < effective end <= target time;
  omitted end resolves to target time. Sort UTC acquisition then product ID.
- Reject duplicate IDs/times/observations, malformed inputs, incompatible selected
  grids/contracts/processing, invalid bounds/minimum and inconsistent lineage.
- Resolve structured observation metadata through existing AS-102 registry
  parents; do not parse arbitrary IDs or alter generic provenance.
- Per-feature/pixel history uses exact valid reference support on target support.
  Counts uint32, zero outside target feature support; all masks are subsets.
- Float64 median, MAD, scale 1.4826*MAD and signed target-minus-centre deviation.
  Centre/scale/deviation float64; anomaly/rank float32; masks bool.
- Zero scale leaves baseline/deviation/rank valid, standardized anomaly NaN.
  Positive scale is used directly: no epsilon, fallback, clipping or noise floor.
- Exact midrank `(less + 0.5*equal)/n`, range [0,1], same minimum history.
- Valid empty outputs for sparse/empty history or target, finite JSON metadata,
  explicit summary denominators and reconciled diagnostics.
- Target fingerprint includes full water/feature masks and supported values.
  Reference fingerprint includes only masks restricted to target feature support
  and values on their intersection. Ignore invalid NaN payloads and unselected
  observations. Copy relevant inputs; no concurrent-copy guarantee.
- Identity `temporal:<sha256>`, processing version `as104-v1`, excludes creation
  time and summaries. Parents: target AS-103 first, chronological references next.
- Retain all 348 existing tests and pass new offline gates before real acceptance.
- Real acceptance uses April 28 target, March 1–April 1 UTC references, minimum 5;
  never widen period, relax masks/minimum, mix processing or choose by anomalies.

## Scientific Guardrails

Candidate BOA feature deviations only: BOA is not aquatic Rrs. Five observations
do not establish significance. Rank is not probability/confidence/severity.
Positive does not mean dangerous; negative does not mean safe. Preserve feature
families and never combine them. No HAB/bloom, chlorophyll, species, toxins,
water-safety, exposure, persistence, risk, alert or monitoring recommendation.
Acquisition-causal retrospective analysis does not prove historical operational
availability or warning lead time. March is not asserted to be normal water.

## Risks

Small/irregular cloud-selected histories, zero/small scales, heterogeneous
processing, duplicate reprocessing products, coastal/atmospheric artefacts,
mutable inputs and unsupported real spatial history. Report blockers honestly;
do not change the approved contract to obtain support.

## Validation

Independent arithmetic/rank/numerical/support/causality/identity/lineage/model
tests, input/registry immutability and blocked IO. Run full pytest, Ruff and diff
check before real work. Then use unchanged AS-101/102/103 workflows and ignored
AS-102 caches for the predeclared multi-scene experiment. Record actual products,
UTC/Dubai experiment times separately from acquisitions, full support/summaries,
fingerprints/IDs/lineage, independent predeclared scalar pixels, repeated
equivalence and future-observation exclusion. If access or support blocks real
acceptance, record the exact completed evidence and stop the experiment.

## Non-Goals

AS-105 geometry, AS-106 persistence, AS-107 risk/confidence, AS-108 event
conclusions, ML, environmental context, oil/Sentinel-1, exposure, alert levels,
recommendations, dashboard, new dependencies/config/cache, commits/pushes/PRs.

## Frozen Decision 047 Contract

**Decision 047 — AS-104 Causal Per-Pixel Temporal Feature Baselines**

**Date:** 8 October 2026 (Asia/Dubai).
**Status:** Explicitly authorized for AS-104.

AS-104 is a causal, target-specific, per-feature, per-pixel temporal comparison
over validated AS-103 scenes. Use explicitly bounded strictly-prior observations
only: no self-inclusion, future observations or symmetric baseline in as104-v1.
Centre is median; MAD is median absolute deviation from that median; scale is
1.4826*MAD; deviation is target minus centre; standardized anomaly divides by
positive scale; empirical rank uses exact-tie midrank. Minimum history is an
explicit API parameter, with 5 for P0 real acceptance, not a sufficiency claim.
Zero MAD preserves centre, zero scale, deviation and rank, but masks standardized
anomaly. No epsilon, fallback scale or clipping. Never combine features; preserve
the shared red_edge_b5_vs_red family of ndci_like and red_edge_red_ratio.
Outputs are temporal spectral anomalies/candidate feature deviations/observational
anomalies/baseline-relative signals, not biological or operational conclusions.
Semantic fingerprints include target masks/supported values and selected reference
support/values only within target feature support. No whole-reference fingerprint
and no precision-limited-scale diagnostic. Identity/provenance include selected
parents, not unselected scenes. Existing registry is read-only; no schema change.
No new dependency, TOML fields or disk cache. Preserve historical evidence.

## Historical Execution Status — 8 October 2026

Plan recorded before implementation. Pure temporal implementation and 112 new
offline cases passed: full suite 460 passed, Ruff/diff checks passed, six existing
Rasterio warnings. The predeclared real attempt is BLOCKED at March 4 because
PC returns two same-observation processing products (05.09/05.10) and unchanged
AS-102 requires exactly one match. No reference rasters were read; no real temporal
product/support summaries were produced. See [validation evidence](evidence/AS_104_TEMPORAL_BASELINE_VALIDATION.md).
Implementation is uncommitted for review; real acceptance is not complete. No
commit, push or PR. AS-105+ remains unauthorized and unstarted.

## Resumed AS-104 Acceptance — 9 October 2026 — BLOCKED

Decision 048 is merged via PR #10 at `39f2aee90c727fc151886efbdea44daec0e3f9b4`.
The original AS-104 implementation/tests remain byte-for-byte preserved. The
combined suite is **533 passed**, Ruff/diff pass, six existing Rasterio warnings.
Decision 047/048 and M19/M20/E18–E20/EV-022–EV-024 retain their historical bodies
and statuses; the records now coexist chronologically in this worktree.

Three frozen real attempts on 9 October stopped while signing March 4 assets.
The last read SCL, then exhausted five bounded signing attempts for B02. A
bounded HTTP diagnostic observed 504 alongside successful responses for the same
assets; the access failure remains unresolved. Exactly zero March references
completed AS-102/103; real temporal support, counts, fingerprints, product ID,
scalar validation, future-scene exclusion and repeatability are NOT produced/run.
Target cache remains unchanged and supplies 7,963 pixels for each AS-103 feature.
This is an access blocker, **not** measured zero temporal support or a math failure.
[Full resumed evidence](evidence/AS_104_TEMPORAL_BASELINE_VALIDATION.md), M21/E21/EV-025.

Retry remains constrained to actual PC 05.09, target April 28, exactly the five
March observations, March 1 inclusive–April 1 exclusive UTC and minimum five.
No temporal/source algorithm, mask/grid/resampling, provenance schema, dependency,
configuration or cache format changed. Offline and real acceptance remain distinct.
No HAB/bloom/chlorophyll/species/toxin, water-safety, intake-risk, persistence,
alert or warning-lead-time inference. Positive is not dangerous; negative is not
safe; rank is not probability/confidence; BOA is not aquatic Rrs.

**P1 Processing Baseline Robustness Experiment — NOT STARTED**. Homogeneous
05.09 versus homogeneous 05.10 requires separate authorization, a complete
homogeneous target/reference set, and must not be called accuracy validation.
AS-105+ is NOT authorized and NOT started. No commit/push/PR; keep the safety
stash `f93950aab6fdfb40bb100158915ef12692aa1665` available. Leave all AS-104 work
uncommitted for owner review.

## Post-PR #11 Real Acceptance — 9 October 2026 — BLOCKED

Decision 049 is merged via PR #11 at `2006df7a70a4f48c66933aed96f4464d8d03084e`.
A new verified safety snapshot/stash preserved all temporal source/tests before
ff-only integration and restore; both old/new stashes remain retained. Combined
offline gate: **643 passed**, Ruff/diff PASS, six historical Rasterio warnings.

Normal production AS-102 and unchanged AS-103 completed all five frozen March
05.09 references, preserving the target grid and accepted April IDs/cache hashes.
The unchanged AS-104 call then failed at target upstream provenance validation:
observation metadata uses `sentinel-2b`, actual PC SourceRecord uses `Sentinel-2B`;
the guard at baseline.py:105–110 compares them case-sensitively. Their acquisition
timestamps agree. No temporal source/test/algorithm, source record, accepted cache
or scientific-contract change was made to bypass this representation mismatch.

M23/E23/EV-027 and [full validation §5](evidence/AS_104_TEMPORAL_BASELINE_VALIDATION.md#5-pr-11-integration-and-five-reference-0509-attempt--9-october-2026)
record actual scene IDs/fingerprints/counts/feature summaries and the blocker.
The predeclared scalar rule was first/middle/last row-major supported pixel per
feature, using masks only. Scalar/causal/repeat checks were not reached; no real
AS-104 product or support/history/statistics is claimed. Owner review/authorization
of a targeted platform-representation fix is required before another acceptance
run; preserve the frozen math, bounds, five scenes, minimum five and lineage.
No Decision 050, commit/push/PR, AS-105+ or P1 05.10 study. Work remains uncommitted.

## Targeted Platform Fix and Cached Real Acceptance — 9 October 2026 — PASS

M24/E24/EV-028 changes only `_descriptor`'s platform equality to compare
`.casefold()` values. Stored platform strings, identities, caches, provenance,
acquisition checks and all other compatibility rules are unchanged. No alias or
punctuation/whitespace normalization; no new Decision 050. Twenty regression
cases were added in test_identity_lineage.py; 132 temporal / 663 full tests and
Ruff/diff PASS with six historical Rasterio warnings. The reverse-case unit test
isolates the predicate; the existing lowercase observation schema stays intact.

M25/E25/EV-029 real acceptance PASS reused all six verified 05.09 AS-102 known-ID
caches without network, raster reads/reprocessing or cache writes. Unchanged
AS-103 reconstruction reproduced exact accepted IDs. All twelve cache-file
hashes remain unchanged. The frozen April-28 target, exact five March scenes,
half-open March window and minimum five are unchanged. Same 20 m EPSG:32640
310×228 grid; target support 7,963 for each feature and baseline/z/rank support
792/802/801/801/801/797. Insufficient support remains invalid; no fallback or
mask/date/minimum relaxation. Eighteen independent scalar checks, synthetic
future exclusion, repeat and input immutability PASS.

Full temporal results, identity/provenance and exact timestamps are in
[validation §§6–7](evidence/AS_104_TEMPORAL_BASELINE_VALIDATION.md).
Prior M23/E23/EV-027 remains the factual blocked checkpoint. The entire AS-104
worktree stays uncommitted for owner review. No commit/push/PR/merge, Decision
050, AS-105+ or P1 05.10 experiment. Engineering PASS does not establish HAB,
concentration, toxins/species, safety, risk, persistence, alerts or lead time.

## Historical Final Publication Status — M26 / E26 / EV-030 (before PR #12 merge)

AS-104 implementation and real acceptance PASS. Implementation/evidence committed
as `09b38bd9c312470e948b1f17165ec5335cfc149d` and pushed to
`origin/feature/as-104-temporal-baseline`. Feature publication worktree verified
clean. PR NOT YET CREATED; merge NOT YET PERFORMED. Review published commit and
open PR if review passes and creation is authorized. AS-105+ and P1 05.10 NOT STARTED.
The original instruction to leave implementation uncommitted and earlier
BLOCKED/PASS execution stop states remain historical. This later publication
does not rerun EO processing, alter scientific values/math or establish detection
accuracy. See validation §8 for acceptance versus publication timestamps.

## Current Final Closeout Status — M27 / E27 / EV-031

AS-104: **COMPLETE AND MERGED** via PR #12. Real acceptance **PASS**; no unresolved
AS-104 P0 blocker. Merge commit `472edc737847dc8581290a372c5da28f71fc48f0`, merged
**2026-10-09T13:26:08+04:00 Asia/Dubai** / **2026-10-09T09:26:08Z**.
Feature implementation `09b38bd9c312470e948b1f17165ec5335cfc149d` and publication docs/final head
`703af1176aeaf9ba38d31c53648907c3b1792aec` are the two merged commits across fifteen changed paths.
The accepted temporal product and scientific measurements are unchanged;
see validation §9 for merge metadata and separate acceptance/publication times.
Reproducible temporal spectral anomaly / baseline-relative comparisons over
BOA-derived features are supported. This does not establish HAB detection, bloom
confirmation, chlorophyll concentration, species, toxins, water safety, intake
risk, persistence, alerts or warning lead time. L2A BOA is not aquatic Rrs.
Five historical observations are not statistical sufficiency; approximately 10%
five-history support remains a documented limitation, not a failure or reason to
relax support. Small positive scales can produce large robust-z magnitudes.
Rank is not probability, confidence or severity.

The original plan and BLOCKED/PASS/publication checkpoint instructions remain
historical. This closeout changes documentation only and does not rerun EO.
Owner review of next milestone/AS-105 design precedes any implementation;
separate authorization required. AS-105+ and P1 05.10 NOT STARTED. Both safety
stashes/recovery artifacts retained. No Decision 050 or new merge in this task.
