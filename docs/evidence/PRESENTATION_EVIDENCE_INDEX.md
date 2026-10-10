# AquaSentinel 813 — Presentation Evidence Index

## Current AS-106 design freeze — 10 October 2026 (Asia/Dubai)

**Decision 051: OWNER-APPROVED / FROZEN DESIGN ONLY.** AS-105 remains COMPLETE
AND MERGED; Decisions 001–050 and completed M01–M30 history are preserved.
**AS-106 IMPLEMENTATION: NOT STARTED; no implementation authorization here.**
Prepared on `docs/as-106-design-freeze`, from approved main
`b1b5147d9973d8cf23d575985319bf94a55a03d4` (PR #15).
Real AS-106 acceptance: **BLOCKED ON FUTURE DATA PREPARATION**; earlier-April
eligible inventory remains unknown and no verified earlier-April cache exists.
M31–M35 / E31–E35 / EV-035–EV-039 are **future reservations, all NOT STARTED**.
Owner review of the published frozen design, then explicit M31 implementation
authorization, is next. Metadata-only M32 and upstream-data M33 are separate gates.
AS-107+ and P1 05.10: **NOT STARTED**; future AS-105 policy validation **REQUIRED /
NOT RUN**. No source/test/config/dependency change, real EO processing, EO-service
query, imagery download, PR or merge in this design-freeze task.
See [AS-106 frozen design](../AS_106_PERSISTENCE.md) and [Decision 051](../DECISIONS.md#decision-051--as-106-causal-consecutive-valid-observation-recurrence).

The dated AS-105 closeout and earlier checkpoint text below retains its historical
next-step/authorization meaning; it does not authorize or describe current AS-106 work.

## Historical AS-105 M30 closeout — 10 October 2026 (Asia/Dubai)

**AS-105: COMPLETE AND MERGED** via [PR #14](https://github.com/Omar-Aboulwafa/aquasentinel-813/pull/14).
**M30 / E30 / EV-034:** merge/publication closeout only; frozen Decision 050
implementation and M29 real engineering acceptance are now on official main.
**M28 implementation/adversarial validation PASS; M29 real engineering acceptance PASS.**
Decision 050 is **MERGED / unchanged**; no Decision 051 is created.
**AS-105 implementation merge commit:** `24a260cff130238c731f7cb62fc47eb74230b4dc`.
Merged **2026-10-10T06:24:09Z / 2026-10-10T10:24:09+04:00 Asia/Dubai**.
Implementation commit `57100b2e53e941f3a7fdfdfc40b61d2b4043c0e5`;
M29 documentation commit / final feature head `1ac9fab9db48cca5625ead20e7133c79101a46d8`.

Foundation/continuity complete → AS-101/102/103 merged → Decisions 048/049 merged → AS-104 COMPLETE AND MERGED → AS-105 M28 implementation/adversarial PASS → AS-105 M29 real engineering acceptance PASS → PR #14 MERGED → AS-105 COMPLETE AND MERGED → next milestone requires separate owner design review/authorization → AS-106+ NOT STARTED; P1 05.10 NOT STARTED.

Current active development branch: **none**. AS-105 development is closed.
This closeout was prepared on `docs/as-105-closeout`; AS-106+ is not authorized
and **NOT STARTED**. Immediate next step: **Owner review of the next milestone /
AS-106 design before implementation.** Future comparative policy validation:
**REQUIRED / NOT RUN**. P1 05.10 robustness: **NOT STARTED**.

Accepted M29 evidence is unchanged: target water **7,963**, P **802 / 10.071581%**,
**7 candidates / 0.872818% of P**, descriptive candidates/water **0.087907%**;
**projected-grid candidate area 2,800 m² / 0.0028 km²**. One region, zero one-pixel
regions, one MultiPolygon with three parts; F2/F4 votes, family counts **0, 7, 0, 7, 0**.
The corrected red_edge_red_ratio rank-.4/.6 counts remain **240/92**, not the earlier
238/93 chat transcription. No scientific identity, measurement or experiment time changed.

This proves reproducible candidate spectral anomaly geometry under frozen v1 only,
not HAB/bloom confirmation, concentration/species/toxins, causation, sensitivity,
specificity/accuracy/false-positive rate, persistence, risk/confidence, water safety,
intake exposure, alert or warning lead time. Rank is not probability/confidence/
significance/severity; families are not statistically independent. Five histories
are not statistical sufficiency; ~10% evaluable support is a material limitation.
No historical-event comparison or new real geometry/upstream processing was run.

All earlier M01–M29 / E01–E29 / EV-001–EV-033 and Decisions 001–050 are preserved.
The dated M28/M29 status blocks, milestone/evidence entries and their pre-merge
publication wording below are **historical checkpoints**, not current status.
Both safety stashes and external recovery artifacts remain retained; read-only
AS-104 handoff, M29 bundle and twelve accepted AS-102 cache hashes remain unchanged.
This closeout creates no PR and performs no merge. Local test results are not
GitHub CI success or scientific accuracy.

## Historical AS-105 M29 status — before PR #14 merge, 10 October 2026 (Asia/Dubai)

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
See [AS-105 contract](../AS_105_HAB_ANOMALY_GEOMETRY.md) and [M29 validation](AS_105_HAB_ANOMALY_GEOMETRY_VALIDATION.md#m29--real-geometry-engineering-acceptance--10-october-2026).

## Historical AS-105 M28 status — before M29, 10 October 2026 (Asia/Dubai)

Owner-authorized **offline implementation only**; Decision 050 / M28 / E28 / EV-032.
**PASS — OWNER-REVIEWED / FEATURE PUBLICATION AUTHORIZED** on
`feature/as-105-hab-anomaly-geometry`, isolated worktree
`/workspace/aquasentinel-813-as105`, verified base
`4e322df220f8cab2805fccf9a2b32dd825f29218`.
Foundation/continuity complete → AS-101/102/103 merged → Decisions 048/049 merged
→ AS-104 COMPLETE AND MERGED → AS-105 frozen-policy offline implementation PASS
→ owner rank-granularity clarification accepted → feature publication
→ PR code review next after publication verification.

140 synthetic geometry cases PASS; full **803 passed**, Ruff/diff/whitespace
PASS; only six existing Rasterio warnings. No upstream algorithms, tests,
configuration, dependencies, provenance schema or cache format changed.
All 55 mandated adversarial requirements and controls A–E pass; this is
engineering evidence, not HAB accuracy. Rank is not probability/confidence/
significance/severity and evidence families are not independent measurements.

Real AS-105 geometry acceptance: **NOT RUN**; real counts/fraction/area/regions
remain **UNKNOWN**. Its future checkpoint is reserved and has **not been created**.
Future predeclared comparative policy validation: **REQUIRED / NOT RUN**;
AS-106+ and P1 homogeneous 05.10: **NOT STARTED**.
The owner authorized feature commit/push on 10 October 2026 after the final
quality/preservation gates. This record accompanies that feature publication;
verify the exact Git SHA/remote before PR review. **PR NOT CREATED; NOT MERGED.**
Real acceptance and future studies remain separately gated. The verified external
AS-104 handoff, twelve accepted cache hashes, both safety stashes and recovery
artifacts remain intact; the handoff is read-only and not tracked.

Earlier dated checkpoint status statements below retain their historical
meaning, including earlier AS-105 non-authorization and absence of Decision 050.
This M28 block governs current status; M01–M27/E01–E27/EV-001–EV-031 stay intact.

Owner-review clarification (same M28/Decision 050): with five histories,
no-tie empirical ranks are 0.0/0.2/0.4/0.6/0.8/1.0; the frozen 0.90 screen
requires all five below, or four below plus one exact tie. It is not a population
90th-percentile estimator or significance. Four synthetic regression cases pass.
Future predeclared history-depth sensitivity is required where valid EO permits;
choose exact depths before running it. M29 retains the accepted minimum-five
parent. No real geometry execution or new checkpoint.

See [AS-105 contract](../AS_105_HAB_ANOMALY_GEOMETRY.md) and [M28 validation](AS_105_HAB_ANOMALY_GEOMETRY_VALIDATION.md).

**Historical AS-104 closeout status — 9 October 2026 (Asia/Dubai), M27/E27/EV-031:**
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
See [merge/closeout evidence §9](AS_104_TEMPORAL_BASELINE_VALIDATION.md#9-pr-12-merge-and-as-104-closeout--9-october-2026).

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
[validation §8](AS_104_TEMPORAL_BASELINE_VALIDATION.md#8-as-104-feature-publication--9-october-2026).

**Historical platform-fix / cached acceptance checkpoint — before feature publication, 9 October 2026 (Asia/Dubai):**
The owner-authorized consistency predicate now compares `.casefold()` values only.
It does not strip punctuation/whitespace, map aliases, or rewrite stored platform
strings, source records, products, fingerprints or caches. Acquisition and all
other provenance/compatibility checks remain unchanged. Only
`temporal/baseline.py` and `tests/temporal/test_identity_lineage.py` changed in
source/tests: one predicate and 20 regression cases. The reverse-case unit case
isolates this predicate; the existing descriptor schema still requires lowercase
observation platforms. Full-API tests use the real lowercase-observation /
mixed-case-source pattern for both Sentinel-2A and Sentinel-2B.

M24/E24/EV-028 records the bug fix, with **132 temporal tests PASS** and the
pre-rerun combined **663 passed**, Ruff/diff PASS, six historical Rasterio warnings.
M25/E25/EV-029 records **real acceptance PASS**, reusing all six known-ID 05.09
AS-102 caches with no network or imagery reprocessing. Unchanged AS-103
reconstruction reproduced all six accepted IDs/content fingerprints. All 12
cache-file hashes remain identical. The exact five March acquisitions, April-28
target, March half-open window and minimum five were retained.

Cached rerun: **08:01:50.383608–08:01:51.327507 UTC** /
**12:01:50.383608–12:01:51.327507 +04:00 Asia/Dubai**. On the unchanged 20 m
EPSG:32640 310×228 grid, all features have 7,963 target-supported pixels.
Baseline/z/rank counts in approved feature order are
**792 / 802 / 801 / 801 / 801 / 797**; insufficient counts are
**7,171 / 7,161 / 7,162 / 7,162 / 7,162 / 7,166**. Zero MAD and both numerical
rejection counts are zero for every feature. Sparse history remains masked;
five scenes are not five valid observations at every pixel.

**18/18 independent scalar checks PASS**, synthetic later-scene addition/mutation
causal check PASS, deterministic repeat PASS, input immutability PASS.
Product: `temporal:e814b0574ab30d1841778ee3c5005ffcb313ab42473c41acc028f0a9f7804a8b`.
Immediate provenance parents are target AS-103 first, then R1–R5 chronologically;
each branch retains actual PC → AS-102 → AS-103 → AS-104 lineage. The future
control is synthetic and excluded, not evidence of future EO availability.
Full counts, summaries, fingerprints, parents and scalar records are in
[validation §§6–7](AS_104_TEMPORAL_BASELINE_VALIDATION.md).

M23/E23/EV-027 remains the earlier **BLOCKED** platform-casing attempt; its body
and all prior checkpoint/decision bodies remain preserved. No Decision 050.
Both retained stashes and old/new external recovery artifacts remain available.
AS-104 stays **UNCOMMITTED / READY FOR REVIEW**. Owner review is the next gate;
no commit/push/PR/merge, AS-105+, or P1 homogeneous-05.10 experiment. PASS is
engineering acceptance of temporal candidate BOA signals, not biological or
operational accuracy, risk, persistence, alert or warning-lead-time validation.
Earlier dated checkpoint statements below are historical; this update governs
current state. Final quality/security verification is recorded in validation §7.

**Created:** 6 October 2026 (Asia/Dubai).

**Historical PR #10 integration checkpoint — 9 October 2026 (Asia/Dubai):** Decision 048 is
merged through PR #10 at `39f2aee90c727fc151886efbdea44daec0e3f9b4` (fix commit
`c9a415b65a101319e9c9f2fef21ad0dcd44c9347`). The existing AS-104 branch was
fast-forwarded from `c6accab2c5753734466a6375d1b3ce1762e99bed`, then its retained
safety stash was applied. Genuine documentation conflicts were reconciled;
all ten restored AS-104 files matched the pre-integration SHA-256 inventory.
Temporal source/tests remain byte-for-byte unchanged. The combined offline gate
passed: **533 tests**, Ruff/diff checks, the same six Rasterio warnings.
The original Decision 047 → 048, M19 → M20, E18 → E19 → E20 and
EV-022 → EV-023 → EV-024 bodies/statuses are preserved in order. Their
cross-worktree/pending-merge wording describes the original dated checkpoints.
The frozen April 28 / exactly-five March / minimum-five / delivered-05.09 real
acceptance was resumed in three separately timestamped attempts. All stopped at
March 4 asset signing; a bounded diagnostic observed intermittent HTTP 504 and
successful responses for the same assets. The third attempt read SCL but
exhausted five attempts signing B02. **Real acceptance remains BLOCKED**: zero
completed reference scenes and no real temporal product. No scientific/mask/math/
grid contract was relaxed. Implementation remains uncommitted; see
[resumed evidence](AS_104_TEMPORAL_BASELINE_VALIDATION.md) / M21/E21/EV-025.
**P1 Processing Baseline Robustness Experiment — NOT STARTED**: homogeneous
05.09 versus homogeneous 05.10 requires separate authorization and is not
accuracy validation. AS-105+ is NOT authorized and NOT started. No commit,
push or PR in this integration task; retain the verified safety stash.

**Purpose:** Compact claim-to-evidence index for the [presentation journal](../PRESENTATION_JOURNAL.md). This pack preserves the CDSE investigation, the **historical Planetary Computer metadata-only checkpoint**, and the [later successful final raster gate](AS_102_PLANETARY_COMPUTER_RASTER_GATE.md). Historical records do not themselves certify perpetual external-service availability or authorize implementation. The separately authorized M15 update adds actual AS-102 implementation evidence EV-016/EV-017 and Decisions 039–045; AS-103 is COMPLETE AND MERGED through PR #8; EV-019/EV-020 preserve its earlier feature-branch acceptance stage, and EV-021 records the later final code-review/publication stage. AS-102 is COMPLETE AND MERGED through PR #6; EV-018 records the final reviewed/merged stage while EV-016/EV-017 preserve their historical acceptance checkpoint.

**Later evidence stage recorded:** 6 October 2026 (Asia/Dubai), FG-01. Original experiment timestamp not supplied; this is a later experiment than the preserved metadata-only checkpoint, not a new probe run by this documentation task.

**New implementation evidence:** EV-016/EV-017, fresh experiment started `2026-10-06T10:07:14.660936+00:00` UTC / `2026-10-06T14:07:14.660936+04:00` Asia/Dubai. Base `0867708ea62676dcbcd0f5f83577cc120d633f26`, branch `feature/as-102-optical-preprocessing`. This new experiment has exact timestamps, typed processing evidence and offline tests, unlike the original supplied historical reconstructions.

**Final review/merge update:** 8 October 2026 (Asia/Dubai), EV-018. Feature `fe3d27046c40600010753957ee8921d57071ec48`; [PR #6](https://github.com/Omar-Aboulwafa/aquasentinel-813/pull/6); merge `627b6ae8a509509dbb2d5d43bbdc6d74e0ce2aac` at `2026-10-08T07:06:46Z` / `2026-10-08T11:06:46+04:00`. Final reviewed baseline: 265 tests passed, Ruff/diff checks passed; six non-blocking Rasterio warnings. No configured/reported GitHub CI/workflow checks. At the AS-102 merge checkpoint AS-103 was NOT authorized and NOT started; the later AS-103 authorization/acceptance is recorded separately below.

**Historical AS-103 acceptance checkpoint:** 8 October 2026, EV-019/EV-020; explicitly authorized candidate-feature implementation, uncommitted/unpushed/unmerged. Six features, 7,963 valid pixels each; 348-test branch baseline. AS-104 NOT authorized and NOT started.

**Historical AS-103 final review/merge update:** 8 October 2026 (Asia/Dubai), M18 / EV-021. AS-103 is **COMPLETE AND MERGED** through [PR #8](https://github.com/Omar-Aboulwafa/aquasentinel-813/pull/8). Implementation `5638bc8b4ab06f235f908642f714a7cc83b35709`; AS-103 implementation merge commit `b770d0561da9ac2b81ca2d4b8e784adff66ee231`, merged `2026-10-08T10:43:24Z` / `2026-10-08T14:43:24+04:00` Asia/Dubai. Final reviewed baseline: 348 tests passed, Ruff/diff checks passed; six existing non-blocking Rasterio PendingDeprecationWarnings only, no new AS-103 warnings. No GitHub Actions/workflow CI run was configured/reported; no GitHub CI success is claimed. AS-103 development is closed. AS-104 — Temporal Baseline is NEXT PLANNED only, NOT authorized and NOT started. No real-scene experiment was rerun during merge review or this documentation closeout.

**Historical AS-104 checkpoint — 8 October 2026 (Asia/Dubai):** Decision 047 explicitly
authorized implementation; M19 / E18–E19 / EV-022–EV-023 records an uncommitted
offline PASS and BLOCKED real multi-scene attempt. This supersedes older AS-104
status wording while preserving EV-001–EV-021 as historical records. No new merge,
GitHub CI, HAB/event or operational-performance claim. AS-105+ remains unstarted.

## Evidence standard and temporal boundary

**Historical PR #11 acceptance checkpoint — 9 October 2026 (Asia/Dubai):**
Decision 049 is merged through PR #11 at
`2006df7a70a4f48c66933aed96f4464d8d03084e` (fix commit
`9181e0da40898f5c729b8596367bb3e4719317d0`). The branch was fast-forwarded and
its NEW safety stash applied without dropping either stash. Four genuine
documentation conflicts were reconciled; all eight temporal source/test hashes
remain unchanged. Combined offline gate: **643 passed**, Ruff/diff PASS, six
existing Rasterio warnings. Decisions 046→047→048→049, milestones M18–M22,
engineering E17–E22 and detailed evidence EV-021–EV-026 coexist in order without
renumbering or duplicated bodies; earlier statuses remain historical.

The frozen 05.09 April-28 / exactly-five March / minimum-five real experiment ran
07:31:08.630215–07:31:57.353103 UTC / 11:31:08.630215–11:31:57.353103 Dubai.
**5/5 March AS-102 and AS-103 scenes completed** with normal production transport,
unchanged EPSG:32640 310×228 grid and masks. Valid-water counts:
8,674 / 2,092 / 7,350 / 3,834 / 6,156. Accepted April cache/feature IDs remain
unchanged; target supports 7,963 pixels per feature. March 4 has 52 denominator
exclusions in B04-denominator features; March 14 has 20 green/blue exclusions.

**AS-104 real acceptance is BLOCKED**, now at its target provenance guard:
`observation_match.platform` is `sentinel-2b`, but actual PC `SourceRecord.platform`
is `Sentinel-2B`. All three target acquisition timestamps agree. The unchanged
case-sensitive comparison at `temporal/baseline.py:105–110` rejects the target
before numerical reduction. March products have the corresponding same casing
mismatch. Transport succeeded; this is a representation/validation blocker, not
measured zero temporal support. No history distributions, temporal summaries,
AS-104 fingerprints/ID/lineage, scalar checks, future control or deterministic
repeat were produced/run. No code/test/cache-contract change or workaround.

M23/E23/EV-027 records this factual attempt, with full safe scene statistics,
IDs/fingerprints, support and diagnostic metadata in
[AS-104 validation](AS_104_TEMPORAL_BASELINE_VALIDATION.md#5-pr-11-integration-and-five-reference-0509-attempt--9-october-2026).
Owner review/authorization of a targeted platform-representation fix and realistic
metadata tests is the next gate; do not mutate source records or accepted caches
to bypass it. AS-104 remains uncommitted for review. No new Decision 050, commit,
push, PR or GitHub merge; only the required local ff-only integration occurred.
AS-105+ and P1 homogeneous-05.10 study NOT started. No hazard, science accuracy,
operational risk, persistence, alert or warning-lead-time claim.

**Historical upstream fix checkpoint — 8 October 2026:** Decision 048 / M20 / E20 /
EV-024 adds separately authorized source disambiguation, uncommitted for review.
AS-104 was explicitly authorized and remains uncommitted/preserved in its original
worktree; real acceptance is still BLOCKED pending upstream review/merge and a
separate rerun. Decision 047 and M19/E18–E19/EV-022–EV-023 remain there only, per
owner clarification; their numbers are reserved, not reused. Earlier AS-103
closeout authorization statements retain their historical checkpoint meaning.

**Historical Decision 049 fix checkpoint — 9 October 2026:** Decision 048 is merged via PR
#10 at `39f2aee90c727fc151886efbdea44daec0e3f9b4`. AS-104 resumed and then hit
intermittent per-asset SAS HTTP 504s. Decision 049/M22/E22/EV-026 now records a
separate, uncommitted reusable-token transport fix and fresh bounded smoke.
Decision 047/M19/E18–E19/EV-022–EV-023 and M21/E21/EV-025 stay only in the
preserved uncommitted AS-104 worktree; their bodies are not copied. Historical
EV-001–EV-024 rows remain unchanged. AS-104 acceptance is still BLOCKED pending
Decision 049 review/merge. AS-105+ and P1 homogeneous-05.10 study NOT started.

The historical probe reports and later raster-gate report transcribe the project owner's supplied factual reconstruction of completed investigations. “Directly observed” refers to those reported observations, not a new live probe performed when writing these documents. Original command logs, full STAC responses, exact experiment timestamps, and screenshots are not attached. Their absence is explicitly retained as a capture limitation.

Use these classifications: **directly observed evidence**, **provider/STAC-advertised metadata**, **inference**, **blocker**, **recommendation**, and **unverified claim**. An advertised format or grid does not prove a successful raster read. A provider recommendation is not an approved technical decision. A pending result must remain pending until a separately recorded experiment supports it.

EV-001–EV-008 index existing repository evidence. EV-009–EV-013 preserve the historical investigations. **EV-014 progresses from historical PENDING to later FG-01 PASS / READY**; both stages appear below, and the original PENDING row is preserved. EV-015 separates metadata-driven PC decoding from raster-access success. Record creation date, acquisition date, processing date, and experiment date must remain distinct.

EV-016/EV-017 retain the 6 October experiment and feature-branch status at that date. Their uncommitted/unmerged/review-pending wording is historical; **EV-018 supersedes that Git status** without changing the original experiment or its 213-test baseline.

EV-019/EV-020 and journal M17 retain the original AS-103 feature-branch acceptance state and experiment timestamp. Their uncommitted/not-merged statuses are intentional historical truth; **EV-021 / M18 supersedes that Git status** with a separately dated final review/merge checkpoint, preserving the 348-test baseline and all real-scene evidence.

## Claim index

Earlier evidence rows retain their recorded checkpoint statuses. EV-030 records
publication; EV-031 records the later PR #12 merge/closeout without rewriting
EV-027–EV-030. Their pending PR/merge instructions are historical.

| Evidence ID | Claim | Status | Metric/result | Source document | Suggested presentation use | Visual still needed? | Final validation needed? |
|---|---|---|---|---|---|---|---|
| EV-001 | Product thesis / Track 03 | Current approved product decisions | Water-quality/operations manager; monitoring/field-verification priority; two planned P0 hazards | [Decisions 001–015](../DECISIONS.md); [PRD §§1–5](../AquaSentinel_813_PRD_v1.0.md) | Problem/user/decision opening | Yes: operator-to-decision diagram | Yes for claimed operational impact; not for recorded thesis |
| EV-002 | AS-001 repository foundation | Completed engineering fact | Python 3.11, `src/` packaging, pytest/Ruff; `f878acc` | [Project State §6](../PROJECT_STATE.md); [pyproject](../../pyproject.toml) | Reproducible engineering foundation | Yes: package/setup capture | Fresh clean-environment reproduction before demo |
| EV-003 | AS-002 config/AOI | Completed engineering fact | TOML/GeoJSON validation and runtime context; `f606ac5`, `113ca44` | [Project State §7](../PROJECT_STATE.md); [runtime](../../src/aquasentinel/runtime.py) | Explicit geographic/scientific inputs | Yes: labelled Al Raha study map | Operational intake geometry remains separate/pending |
| EV-004 | AS-003 provenance | Completed engineering fact | Schema 1.0; historical 17-test project baseline; `e2baedc`, `db79260` | [Project State §§8–9](../PROJECT_STATE.md); [provenance](../../src/aquasentinel/provenance/) | Trace a future result to its source | Yes: labelled source/derived example | Real end-to-end derived hazard lineage remains future |
| EV-005 | Codex continuity | Completed recorded onboarding/handoff | AS-000C.1–8 completed; read-only audit at `779069d`; separate AS-101 authorization | [Project State §13](../PROJECT_STATE.md); [Handoff §§16–19](../HANDOFF.md) | Recoverable multi-machine/agent workflow | Yes: continuity sequence | Original full audit artifact not retained in tracked snapshot |
| EV-006 | AS-101 real Sentinel-2 search | Completed implementation and recorded experiment | AOI/date/cloud search, full pagination, deterministic candidates/provenance; PR #2 merge `1b83a73` | [AS-101 report](../AS_101_STAC_SEARCH.md) | Connect the use case to real catalog data | Yes: query-to-source diagram | Live services can change; raster usability not established |
| EV-007 | 44 candidate scenes | Directly observed catalog experiment | 44 unique products; 44/44 provenance conversions; 0.12–24.96% scene cloud; recorded 2 Oct 2026 | [AS-101 live result](../AS_101_STAC_SEARCH.md); [CDSE probe](AS_102_CDSE_ACCESS_PROBE.md) | First live-data evidence card | Yes: dated result card | Not a fixed future count; usable-water analysis pending |
| EV-008 | 97-test quality baseline | Recorded engineering validation | 97 tests passed, Ruff passed, diff check passed; 17 original tests retained | [AS-101 validation](../AS_101_STAC_SEARCH.md); [journal E09](../PRESENTATION_JOURNAL.md) | Quality/review evidence | Yes: dated test summary | Rerun before release; not scientific accuracy |
| EV-009 | CDSE reflectance offset discovery | Provider/STAC-advertised metadata; decoding inference | Scale `0.0001`, offset `-0.1`; valid DN decoding `DN * 0.0001 - 0.1` | [CDSE reflectance record](AS_102_CDSE_ACCESS_PROBE.md#reflectance-scaleoffset-discovery) | Explain why raw stored values need product semantics | Yes: sanitized metadata fields and formula | Yes: per-band metadata excerpts and decoded real sample |
| EV-010 | CDSE raster-access blocker | Observed environmental blocker; S3/OIDC route advertised | Proxy blocked live raster/header/window attempts; no full download; bounded access unverified | [CDSE access record](AS_102_CDSE_ACCESS_PROBE.md#access-route-and-blocker) | Catalog-versus-pixel-access distinction | Yes: access-boundary diagram | Yes: runtime transport and bounded read; do not infer universal provider denial |
| EV-011 | Planetary Computer STAC accessibility | Directly observed catalog evidence | Anonymous STAC READY / HTTP 200; corresponding item identified | [PC catalog result](AS_102_PLANETARY_COMPUTER_PROBE.md#directly-observed-catalog-result) | Evidence that an alternative catalog was reachable | Yes: sanitized catalog response | Raster signing/access still pending at this checkpoint |
| EV-012 | Same acquisition / different processed product | Metadata-supported inference; pixel equivalence unverified | Acquisition/platform/tile/orbit match; CDSE baseline 05.10/Aug 2024 versus PC 05.09/Apr 2023 | [Identity comparison](AS_102_PLANETARY_COMPUTER_PROBE.md#cross-provider-identity-finding) | Explain provenance during provider evaluation | Yes: comparison table | Metadata capture still needed; no pixel-equivalence claim |
| EV-013 | Planetary Computer COG delivery path | Provider/STAC-advertised metadata; viable-path inference | Nine proposed reflectance bands + SCL; B02 10 m, B05/SCL 20 m COG; host `sentinel2l2a01.blob.core.windows.net` | [PC assets/access](AS_102_PLANETARY_COMPUTER_PROBE.md#asset-inventory-and-advertised-delivery-path) | Potential route to bounded raster access | Yes: host-to-window diagram | Yes: allowlist/access, signing, header/window support, decoding |
| EV-014 | AS-102 bounded raster read | **PENDING — unverified at this evidence point** | No bounded read had yet been performed in the recorded PC stage; no DN/window result | [PC readiness](AS_102_PLANETARY_COMPUTER_PROBE.md#readiness-and-next-evidence) | Explicit remaining feasibility gate | Yes: actual tiny-window evidence after verification | **Yes; do not mark successful from catalog/COG metadata** |
| EV-014 · FG-01 | AS-102 bounded raster read — later final gate | **PASS / READY for tested PC product/path** | 3 successful bounded raster reads; 4 credential-free HTTP 200 signing operations; product XML read; metadata-driven B02/B05 decoding; **8/8 readiness gates passed** | [Later raster-gate record](AS_102_PLANETARY_COMPUTER_RASTER_GATE.md) | Show progression from catalog metadata to real bounded pixels | Yes: sanitized header/window/signing captures | Historical result reported; complete-band preprocessing, scientific suitability, and repeatability captures remain future |
| EV-015 | Metadata-driven PC reflectance decoding | Observed XML and DN samples; metadata-derived interpretation | XML 53,347 bytes; baseline 05.09; quantification 10000; offset -1000; B02 bandId 1/B05 bandId 4; `(DN - 1000) / 10000` | [XML and decoding evidence](AS_102_PLANETARY_COMPUTER_RASTER_GATE.md#product-xml-and-metadata-driven-interpretation) | Explain modern-baseline offsets with actual product metadata | Yes: XML field/band-map excerpt and sample table | Mechanics established for tested bands; aquatic suitability, quality masking, and pixel equivalence not established |
| EV-016 | Full-AOI AS-102 optical preprocessing | **PASS — implemented/validated on uncommitted feature branch** | 9 float32 bands + uint8 SCL/masks, (228,310), 20 m EPSG:32640; AOI 67,449; valid data 65,166; candidate water 10,211; valid water 7,963; AOI fraction 11.805957%, retention 77.984526%, excluded 2,248 | [Timestamped real validation](AS_102_OPTICAL_PREPROCESSING_VALIDATION.md); journal M15 | Real pixel/grid/mask evidence without hazard claims | Yes: AOI/candidate/retained/excluded map | Independent aquatic/HAB scientific validation remains future |
| EV-017 | Actual-PC lineage, verified AOI cache and quality gate | **PASS — implementation acceptance; not merged** | PC-only pixel lineage; CDSE discovery separate; SHA-256/canonical atomic cache; array/source/provenance-equivalent known-ID reload with catalog/signing/XML/raster calls blocked; 213 tests passed (97 retained), Ruff/diff check passed | [Cache/quality evidence](AS_102_OPTICAL_PREPROCESSING_VALIDATION.md); Decisions 039–045 | Reproducible, traceable inputs for future features | Yes: lineage/checksum/test card | Clean-machine/full-product demo and Git review remain pending |
| EV-018 | AS-102 final security/cache/provenance review and merge | **COMPLETE AND MERGED — 8 October 2026** | Final reviewed implementation `fe3d27046c40600010753957ee8921d57071ec48`; PR #6; merge `627b6ae8a509509dbb2d5d43bbdc6d74e0ce2aac`; 265 tests passed, Ruff/diff checks passed; canonical HTTPS/redirect protections, transient SAS containment, strict matching/asset rejection, bounded reads, conservative support and cache/provenance tamper checks; six non-blocking Rasterio warnings | [PR #6](https://github.com/Omar-Aboulwafa/aquasentinel-813/pull/6); [journal M16](../PRESENTATION_JOURNAL.md#m16--as-102-code-review-security-hardening-merge-and-closeout); committed source/tests | Reviewed/merged preprocessing and engineering reproducibility only; does NOT support HAB confirmation, chlorophyll concentration, toxin detection, water safety, desalination shutdown, warning lead time or operational risk accuracy | Yes: sanitized merge/commit/local-quality card | No configured/reported GitHub CI checks; independent science and full-product validation remain outstanding |
| EV-019 | Per-scene AS-103 candidate spectral features and numerical diagnostics | **PASS — authorized feature-branch acceptance, uncommitted** | 6 float32 arrays/masks (228,310); 7,963 valid pixels each; no denominator/nonfinite exclusions; two NDCI-like outputs below −1 retained; 491 negative-input pixels for B06 features | [Timestamped AS-103 evidence](AS_103_SPECTRAL_FEATURES_VALIDATION.md); journal M17 | Explain candidate signals and numerical support before temporal science | Yes: V18 sanitized maps | No HAB, chlorophyll concentration, toxins, species, safety, risk or lead-time claim; independent science remains future |
| EV-020 | AS-103 content identity, immediate-parent lineage and offline quality | **PASS — authorized feature-branch acceptance, not merged** | Versioned mask/five-band fingerprint; deterministic repeat; exact PC→AS-102→AS-103 registry chain; four scalar pixel checks; no access/write calls; 348 tests (265 retained +83 new), Ruff/diff pass, six existing Rasterio warnings | [AS-103 validation](AS_103_SPECTRAL_FEATURES_VALIDATION.md); [contract](../AS_103_SPECTRAL_FEATURES.md); Decision 046 | Reproducible candidate inputs for future AS-104 | Yes: V19 lineage/formula card | Code review/publication pending; no AS-104 authorization or GitHub CI/science claim |
| EV-021 | AS-103 final code review and merge | **COMPLETE AND MERGED — 8 October 2026** | Implementation `5638bc8b4ab06f235f908642f714a7cc83b35709`; PR #8; merge `b770d0561da9ac2b81ca2d4b8e784adff66ee231` at `2026-10-08T10:43:24Z` / `2026-10-08T14:43:24+04:00` Asia/Dubai; 348 tests passed, Ruff/diff checks passed; six existing non-blocking Rasterio warnings only, no new AS-103 warnings; typed model/arithmetic, inclusive denominator guards, NaN/support, consumed-content fingerprint/identity and immediate-parent lineage reviewed; real-scene evidence independently reviewed | [PR #8](https://github.com/Omar-Aboulwafa/aquasentinel-813/pull/8); [journal M18](../PRESENTATION_JOURNAL.md#m18--as-103-code-review-merge-and-closeout); committed source/tests and historical AS-103 acceptance evidence | Reviewed/merged spectral feature engineering, deterministic per-scene feature generation and reproducible lineage/identity only; does NOT support temporal anomaly, HAB confirmation, chlorophyll concentration, species/toxin identification, water safety, intake exposure, operational risk accuracy or warning lead time | Yes: V20 sanitized merge/local-quality card | No configured/reported GitHub Actions/workflow CI run or CI-success claim; independent science remains future; AS-104 NOT authorized and NOT started |
| EV-024 | Explicit PC processing-baseline source resolution and unchanged cache identity | **PASS — isolated fix offline/metadata gates; uncommitted, not merged** | 421 tests (348 retained +73 added), Ruff/diff pass, same six warnings; 5/5 frozen March references plus April target resolve at 05.09 with all eleven required assets and 0 forbidden signing/XML/raster/preprocessing/cache calls; accepted target cache retains identity/provenance/bytes and rejects 05.10 | [Timestamped fix validation](AS_102_REQUIRED_PC_BASELINE_FIX_VALIDATION.md); [plan/API](../AS_102_REQUIRED_PC_BASELINE_FIX.md); Decision 048; M20/E20 | Explain acquisition versus processing-product ambiguity and explicit failure-safe selection | Yes: sanitized ambiguity/constraint/quality card, pending | Upstream code review/merge and separate frozen AS-104 acceptance rerun; no March asset/decoding/support, temporal/HAB, operational accuracy or GitHub CI-success claim |
| EV-026 | Reusable transient PC account/container SAS transport | **PASS — offline/bounded transport smoke; UNCOMMITTED / READY FOR REVIEW** | 531 tests (421 main +110 net new), Ruff/diff PASS, six unchanged warnings; fresh March-4 05.09 all-eleven same-scope signs with 1 anonymous HTTP 200 token attempt, XML 1,024 bytes/B02 4,096 bytes via 206, zero additional acquisition for reuse; original worktree/cache hashes and stash preserved | [Timestamped validation](AS_102_REUSABLE_PC_SAS_TOKEN_FIX_VALIDATION.md); [plan](../AS_102_REUSABLE_PC_SAS_TOKEN_FIX.md); Decision 049; M22/E22 | Scoped credential reuse without changing scientific source identity | Yes: sanitized one-request/eleven-assets card; capture pending | No full processing, AS-104 acceptance, five usable histories, science/operational accuracy, availability guarantee or GitHub CI-success claim; review/merge remains next |
| EV-028 | AS-104 case-only platform consistency fix | **PASS — UNCOMMITTED / READY FOR REVIEW** | One equality predicate, 20 regression cases, 132 temporal and 663 full tests/Ruff/diff PASS; stored values/identities unchanged | [Validation §6](AS_104_TEMPORAL_BASELINE_VALIDATION.md#6-targeted-platform-case-representation-fix--9-october-2026); M24/E24 | Fix representation compatibility while preserving scientific identity | Yes: before/after predicate card; capture pending | No aliases, science change, Decision 050, publication or accuracy claim |
| EV-029 | AS-104 cached five-reference 05.09 acceptance rerun | **PASS — UNCOMMITTED / READY FOR REVIEW** | Six known-ID cache reloads/unchanged AS-103 IDs; 792–802 eligible pixels from 7,963 target support; 18 scalar checks, synthetic causal exclusion, repeat PASS; zero network | [Validation §7](AS_104_TEMPORAL_BASELINE_VALIDATION.md#7-cached-five-reference-0509-real-acceptance-rerun--9-october-2026); M25/E25 | Honest sparse temporal support and reproducible lineage | Yes: history-count/support card; capture pending | Five scenes are not statistical sufficiency; no HAB, concentration, safety, operational risk, persistence, alerts/lead time or CI-success claim |
| EV-030 | AS-104 reviewed implementation/evidence publication | **COMMITTED AND PUSHED — PR NOT YET CREATED, NOT MERGED** | Feature `09b38bd`, parent `2006df7`, 15 paths; pre-commit 663 tests/Ruff/diff PASS, six warnings; remote SHA equality/clean worktree, accepted identities/hashes/history preserved | [Publication §8](AS_104_TEMPORAL_BASELINE_VALIDATION.md#8-as-104-feature-publication--9-october-2026); M26/E26 | Separate measured acceptance from reviewable Git publication | Yes: acceptance → commit → branch → pending review diagram; capture pending | No new EO experiment, merge, GitHub CI success, statistical sufficiency or hazard/operational validation |
| EV-031 | AS-104 merged through PR #12 and formally closed | **COMPLETE AND MERGED — REAL ACCEPTANCE PASS** | Merge `472edc7`, final head `703af11`, two commits/fifteen paths, 663-test reviewed baseline, six historical warnings; preserved 18/18 scalar/causal/repeat evidence, identities/hashes and recovery | [Closeout §9](AS_104_TEMPORAL_BASELINE_VALIDATION.md#9-pr-12-merge-and-as-104-closeout--9-october-2026); M27/E27; PR #12 | Distinguish acceptance/publication/merge; disclose sparse support and authorization boundaries | Yes: milestone timeline/support/merge card; capture pending | No new scientific experiment, HAB/operational claim, statistical sufficiency or GitHub CI success; future design requires authorization |
| EV-032 | AS-105 frozen-policy offline candidate anomaly geometry | **PASS — SYNTHETIC / OWNER-RECONCILED / PUBLICATION AUTHORIZED** | 140 geometry/803 total tests, all 55 adversarial requirements and controls A–E; Ruff/diff/whitespace PASS, six existing warnings; exact threshold/family/support/polygons/lineage and protected hashes | [M28 validation](AS_105_HAB_ANOMALY_GEOMETRY_VALIDATION.md); [contract](../AS_105_HAB_ANOMALY_GEOMETRY.md); Decision 050; M28/E28 | Explainable predeclared rule, honest support and exact candidate geometry | Yes: labelled synthetic vote/threshold/round-trip card, capture pending | Real geometry metrics UNKNOWN; no real acceptance, future policy comparison, HAB accuracy, biological causation, probability/confidence/risk, alerts, persistence or CI-success claim |
| EV-033 | AS-105 M29 real geometry engineering acceptance | **PASS — OWNER-REVIEWED; NOT YET PR-MERGED** | P 802 / water 7,963; 7 candidates, 7/802=0.872818%; projected-grid candidate area 2,800 m²; one eight-connected MultiPolygon region/three pieces, F2/F4 votes; independent checks/repeat/immutability/bundle PASS; 140 focused/803 full tests | [M29 validation](AS_105_HAB_ANOMALY_GEOMETRY_VALIDATION.md#m29--real-geometry-engineering-acceptance--10-october-2026); M29/E29; external local checksummed bundle NOT tracked | Reproducible frozen candidate anomaly geometry with explicit sparse support | V23 capture pending; no screenshot claimed | No HAB/event/biological/accuracy/risk/confidence/persistence/alert/lead-time or CI-success claim; future comparative policy validation REQUIRED / NOT RUN |
| EV-034 | AS-105 PR #14 merge and formal closeout | **COMPLETE AND MERGED** | Actual merge `24a260cff130238c731f7cb62fc47eb74230b4dc`, 10 Oct 2026 06:24:09 UTC / 10:24:09 Dubai; 2 commits / 18 files; M28/M29 PASS unchanged | [PR #14](https://github.com/Omar-Aboulwafa/aquasentinel-813/pull/14); [merge closeout](AS_105_HAB_ANOMALY_GEOMETRY_VALIDATION.md#m30--pr-14-merge-and-as-105-closeout--10-october-2026); M30/E30 | Reviewed frozen-policy engineering evidence on official main | Merge/timeline/support card capture pending | Publication event only; no new scientific validation/CI claim; future policy validation REQUIRED / NOT RUN; AS-106+ and P1 05.10 NOT STARTED |

### EV-021 final AS-103 review and merge

This later checkpoint records the owner-approved final implementation and real-scene
acceptance review, followed by verified publication/PR #8 merge. Review evidence:

- Typed model invariants (`models.py`) and feature arithmetic (`spectral.py`): PASS.
- Inclusive denominator epsilon guards and NaN/feature-support behavior: reviewed/tested PASS.
- Input fingerprint and consumed B02–B06 identity sensitivity: reviewed/tested PASS.
- Unconsumed B07/B08/B8A/B11 identity independence and timestamp-independent identity: reviewed/tested PASS.
- Exact PC→AS-102→AS-103 immediate-parent lineage and direct raw-source shortcut rejection: reviewed/tested PASS.
- M17 real-scene acceptance evidence, including independent scalar checks: review PASS.

M17's experiment began `2026-10-08T09:52:47.133486+00:00` UTC /
`2026-10-08T13:52:47.133486+04:00` Asia/Dubai. The later merge occurred at
`2026-10-08T10:43:24Z` / `2026-10-08T14:43:24+04:00` Asia/Dubai.
The scene was not rerun during merge review or this documentation closeout.
EV-019/EV-020 remain unchanged, including their historical statuses and 348-test baseline.
The preserved scene has six candidate features, 7,963 pixels each (100% parent water),
two below-−1 NDCI-like values retained/diagnosed and signed BOA preserved.

BOA is not aquatic Rrs; ndci_like is not calibrated chlorophyll; mci_like is an
analogue. Correlated NDCI-like/B05-red features are not independent biological
evidence. No event threshold, HAB/event classification, temporal baseline/anomaly,
species/toxins, safe/unsafe certification, autonomous plant action, intake exposure,
operational risk, persistence, warning lead-time accuracy or scientific accuracy is
established. AS-104 is NEXT PLANNED only, NOT authorized and NOT started.
No GitHub Actions/workflow CI run was configured/reported; local quality checks do
not imply GitHub CI success.

### EV-022 — AS-104 offline temporal engineering

**Status:** PASS — authorized implementation, uncommitted for review.
**Date:** 8 October 2026 (Asia/Dubai).
**Claim:** Causal target-ID selection, per-feature/pixel median/MAD/signed deviation,
positive-scale standardized anomaly, exact midrank, semantic target-support input
fingerprints, typed masks/counts/summaries, immediate-AS-103 multi-parent provenance
and blocked IO/immutability. 460 tests passed (348 +112), Ruff/diff PASS; six existing
Rasterio warnings. No dependency/config/cache-format/provenance-schema changes.
**Evidence:** [AS-104 plan/API](../AS_104_TEMPORAL_BASELINE.md), Decision 047,
[validation](AS_104_TEMPORAL_BASELINE_VALIDATION.md), journal M19 / E18.
**Limits:** Offline math/provenance evidence, not real multi-scene acceptance,
biological/event validation, risk, confidence/probability or warning lead time.
No commit/push/PR; AS-105+ unauthorized/unstarted.

### EV-023 — AS-104 fixed-window real acceptance blocked by provider ambiguity

**Status:** BLOCKED — real multi-scene acceptance NOT complete.
**Date:** 8 October 2026 (Asia/Dubai); actual attempt UTC
12:28:07.712335–12:28:29.564367 / Dubai 16:28:07.712335–16:28:29.564367.
**Claim:** Existing April 28 cache/AS-103 target reused (7,963 valid pixels/feature).
AS-101 returned 44 candidates; five March dates match tile 40RBN/orbit 20. The first
reference, March 4, has two PC products with the exact same acquisition/platform/
tile/orbit but baselines 05.09 and 05.10. Unchanged AS-102 exactly-one matching
raises ObservationMatchError; experiment stops before reference raster reads.
**Evidence:** [Timestamped AS-104 validation/blocker](AS_104_TEMPORAL_BASELINE_VALIDATION.md),
journal M19 / E19; stable product IDs, fixed bounds and metadata-only diagnosis.
**Limits:** Zero processed references; real support/summaries, temporal fingerprints/
ID/lineage, scalar checks and future-real-scene check NOT produced/run. No silent
selection workaround, window widening, minimum lowering, baseline mixing or mask
relaxation. Separately authorize any upstream selection-policy investigation.
No HAB/event, science accuracy or operational availability/lead-time claim.
**Visual:** V21 blocker/causal-contract card planned, no screenshot/anomaly map exists.

### EV-024 required-PC-baseline upstream fix

New metadata smoke: `2026-10-08T13:38:26.730440+00:00`–
`2026-10-08T13:38:48.970146+00:00` UTC, or
`2026-10-08T17:38:26.730440+04:00`–`2026-10-08T17:38:48.970146+04:00`
Asia/Dubai. The exact predeclared March products and accepted April product resolve
at 05.09 using the new optional constraint; no XML/rasters were accessed and no
cache was created. Separate offline loading of the accepted April cache verified
matching/contradicting constraints without altering its files or provenance.
This fixes ambiguity at metadata level only, not AS-104 real acceptance.
EV-022–EV-023 remain reserved in the untouched AS-104 worktree. All historical
EV-001–EV-021 rows remain unchanged, including EV-014 PENDING/later PASS progression.

### EV-025 — PR #10 integration and frozen AS-104 signing-access blocker

**Status:** Integration/preservation/offline PASS; real acceptance BLOCKED.
**Date:** 9 October 2026 (Asia/Dubai); exact three attempt times in validation §4.
**Claim:** Exact merged main `39f2aee90c727fc151886efbdea44daec0e3f9b4` integrated
ff-only; retained verified stash restored; four documentation conflicts reconciled;
Decision 047→048, M19→M20, E18–E20 and EV-022–EV-024 preserved without renumbering
or rewriting historical statuses. Eight temporal source/test files byte-identical;
533 tests, Ruff/diff PASS; six existing warnings. Frozen delivered-05.09 attempts
resolved March 4 product, read XML/SCL, then signing prevented completion;
last B02 signing exhausted five bounded attempts. Diagnostic observed intermittent
HTTP 504/200. Zero completed March references; accepted target 7,963 pixels/feature.
**Evidence:** [Timestamped resumed validation](AS_104_TEMPORAL_BASELINE_VALIDATION.md#4-decision-048-integration-and-resumed-frozen-acceptance--9-october-2026),
PR #10, journal M21 / E21, retained recovery/hash inventories and safety stash.
**Limits:** No real temporal support/counts/statistics/fingerprints/product/lineage,
scalar, future-scene or repeat result. Support is unknown, not measured zero;
not HAB, calibrated chlorophyll, biological/operational accuracy or GitHub CI.
**Next:** Retry identical 05.09 contract when signing is available; do not widen
bounds, reduce minimum, mix processing or relax masks. Keep changes uncommitted;
stash retained. P1 05.10 comparison and AS-105+ NOT STARTED.
**Visual:** V22 sanitized gate chronology/HTTP status card planned, no anomaly map.

### EV-026 reusable-token transport — later stage

Fresh transport experiment: `2026-10-09T06:44:49.076690+00:00`–
`2026-10-09T06:44:51.406274+00:00` UTC / 10:44:49–10:44:51 Asia/Dubai.
One token HTTP 200, eleven signs on the actual March-4 05.09 account/container,
two tiny HTTP 206 prefix/header reads, then zero extra acquisition requests for
three cache-reuse signs. Report contains safe counters/status/latency/bytes only.
No SAS credentials, product cache or full preprocessing created. EV-026 does not
supersede EV-024's historical metadata experiment; it records a new transport
stage after PR #10. EV-025 remains only in the preserved AS-104 worktree.

### EV-027 — PR #11 integration and real five-reference 05.09 acceptance attempt

**Status:** Integration/preservation/offline and AS-102/103 references PASS;
AS-104 real acceptance **BLOCKED**. Uncommitted for review.
**Date:** 9 October 2026; exact experiment UTC 07:31:08.630215–07:31:57.353103 /
Dubai 11:31:08.630215–11:31:57.353103 +04:00.
**Claim:** Exact ff-only PR #11 integration; second retained stash and external
recovery artifacts; eight temporal source/test hashes preserved. Combined suite
643 passed, Ruff/diff PASS, six existing warnings. Normal production transport
completed five predeclared actual 05.09 March AS-102/103 scenes, identical target
grid, and retained target cache identity/bytes. AS-104 target provenance guard
rejects lower-case observation `sentinel-2b` against source label `Sentinel-2B`.
Timestamps match; no temporal reduction occurred.
**Evidence:** [Validation §5](AS_104_TEMPORAL_BASELINE_VALIDATION.md#5-pr-11-integration-and-five-reference-0509-attempt--9-october-2026), M23/E23, PR #11 / 2006df7;
full safe per-scene IDs/fingerprints/statistics/support and diagnosis.
**Limits:** No real temporal distributions/arrays/masks/statistics, semantic
fingerprints/ID/lineage, scalar checks, causal future control or repeat result;
missing outputs are unmeasured, not zero. No new Decision 050, algorithm change,
cache rewrite, contract relaxation, hazard/accuracy/operational or GitHub CI claim.
**Visual:** Five-reference support table and sanitized platform-label guard card;
capture pending, no temporal anomaly screenshot.

### EV-014 evidence progression

| Stage / record date | Status | Evidence boundary |
|---|---|---|
| Historical checkpoint, recorded 6 Oct 2026 | **PENDING** | Anonymous catalog/advertised COGs only; [original report](AS_102_PLANETARY_COMPUTER_PROBE.md) remains unchanged |
| Later experiment FG-01, recorded 6 Oct 2026 | **PASS / READY** | GDAL 3.10.3 B02 64×64, B05 32×32, SCL 32×32 reads; signed XML and metadata-driven decoding; [new report](AS_102_PLANETARY_COMPUTER_RASTER_GATE.md) |

Original experiment timestamps were not supplied; report dates do not imply the experiments happened simultaneously. **At FG-01: AS-102 raster-access prerequisite READY; AS-102 NOT YET IMPLEMENTED; AS-103 NOT STARTED.** This historical state is preserved; the later EV-016/EV-017 record supports AS-102 feature-branch implementation acceptance, with AS-103 still not started at that checkpoint. EV-019/EV-020 records the subsequent separately authorized AS-103 acceptance. The SCL sample contains 353/1024 raw water-class pixels, not a final usable-water count. Exact transferred raster bytes were not measured.

No visual is claimed to exist merely because it is suggested here. A metadata inventory, 44 catalog products, and 97 passing software tests do not establish HAB detection, aquatic reflectance suitability, a safe/unsafe water decision, or operational warning lead time.

## Remaining evidence and presentation gaps

- Original probe task/command transcripts, dates/times, tool versions, sanitized STAC/asset metadata excerpts, and actual screenshots.
- CDSE raster transport/authentication and bounded range/window access; no provider-global access conclusion from the environment proxy blocker.
- The later FG-01 report now records credential-free signing, B02/B05/SCL headers/windows, and XML-based decoding. Original timestamps/commands/8-gate checklist, sanitized original XML/header/status captures still need evidence; EV-016 independently records later all-band preprocessing; do not relabel the earlier checkpoint as successful.
- Complete per-provider inventories and field provenance; no cross-provider pixel-equivalence result.
- Exact raster-transfer bytes were not measured; compressed blocks may exceed the requested pixel window. No byte-efficiency claim is supported.
- EV-016/EV-017 now records one real scene’s aligned optical arrays, mask/fraction statistics, actual-PC lineage and offline cache replay. Historical HAB/oil validation, false positives, operational demo site, full product/demo fallback and measured impact remain future evidence. EV-019/EV-020 adds candidate features only, not temporal/scientific interpretation.
- AS-102 contract/provider choice and implementation were separately authorized and recorded by Decisions 039–045 / M15. Final Git review/publication is recorded separately by EV-018 / M16 and PR #6. Presentation captures remain pending; the separate AS-103 authorization is recorded in Decision 046 / M17, not granted by this pack. EV-021 / M18 and PR #8 separately record AS-103 final review/merge. AS-104 remains NOT authorized and NOT started.

## Presentation capture rule

For every important experiment, future agents must record:

- Command/task purpose and the exact bounded method used.
- Experiment timestamp/date and timezone, separately from the report-creation date and product dates.
- Source/provider and stable catalog/collection references.
- Item/product identity, acquisition context, and processing baseline/version where relevant.
- Quantitative result, units/denominator, and whether it is observed, advertised, inferred, or unverified.
- Limitation, failure/blocker, remaining uncertainty, and authorization boundary.
- Screenshot/visual requirement, caption, capture status, and attribution/licence.
- Repository evidence file and relevant commit/PR reference when available.

Do **not** store credentials, SAS tokens, signed URLs, or secrets. Use sanitized unsigned references and metadata excerpts. Do not commit full EO scenes or runtime caches as presentation evidence.

After an evidence record exists, update the journal and affected EV entries. Preserve the old dated checkpoint when adding a later successful or failed gate; never rewrite a metadata-only stage as if it already contained pixel evidence. Scientific/provider decisions continue to be governed by the existing decision log and explicit authorization.

### EV-028 — Targeted platform case-representation consistency fix

**Status:** PASS — uncommitted for owner review. Date: 9 October 2026 (Asia/Dubai).
**Finding:** Only `_descriptor`'s platform equality changes to `.casefold()`.
No aliases, punctuation/space stripping, stored value normalization or identity
rewrite. Acquisition, lineage and every other compatibility rule are unchanged.
**Validation:** 20 added regressions; 132 temporal / 663 full tests, Ruff/diff PASS;
six historical Rasterio warnings. Reverse-case unit test isolates the predicate;
the existing lowercase observation descriptor schema remains unchanged.
**Evidence:** [Validation §6](AS_104_TEMPORAL_BASELINE_VALIDATION.md#6-targeted-platform-case-representation-fix--9-october-2026), M24/E24, source/test delta and external pre-fix patch/hash inventory.
**Limit:** Bug fix under Decision 047; no Decision 050 or new scientific result.

### EV-029 — Cached real five-reference 05.09 temporal acceptance rerun

**Status:** PASS — uncommitted for owner review. Date: 9 October 2026 (Asia/Dubai).
**Experiment:** 08:01:50.383608–08:01:51.327507 UTC /
12:01:50.383608–12:01:51.327507 +04:00. Exactly five fixed March references and
accepted April-28 target, March half-open window and minimum five. Six existing
known-ID 05.09 caches reused; unchanged AS-103 reconstruction reproduced exact
IDs; all 12 cache-file hashes preserved. Zero network attempts or raster writes.
**Result:** Six features each have target support 7,963. Baseline/z/rank counts
792/802/801/801/801/797; insufficient counts 7,171/7,161/7,162/7,162/7,162/7,166.
Zero MAD/numerical rejection counts zero. 18/18 independent scalar checks,
synthetic future addition/mutation exclusion, deterministic repeat and input
immutability PASS. Target-first/R1–R5 immediate parents and full upstream lineage.
**Product:** `temporal:e814b0574ab30d1841778ee3c5005ffcb313ab42473c41acc028f0a9f7804a8b`.
**Evidence:** [Validation §7](AS_104_TEMPORAL_BASELINE_VALIDATION.md#7-cached-five-reference-0509-real-acceptance-rerun--9-october-2026), M25/E25, complete safe JSON distributions/summaries/fingerprints/parents/scalar records.
**Limit:** Engineering acceptance only; rank is not probability/confidence/
severity and five observations are not statistical sufficiency. No aquatic Rrs,
HAB, concentration, species/toxins, safety, intake risk, persistence, alert,
warning lead-time or GitHub CI-success claim. Synthetic control is not a real
future observation. M23/E23/EV-027 remains historically BLOCKED; no publication,
AS-105+ or P1 homogeneous-05.10 experiment.

### EV-030 — AS-104 implementation and accepted evidence committed and pushed

**Status:** COMMITTED AND PUSHED for PR review; PR NOT YET CREATED, NOT MERGED.
**Date:** 9 October 2026 (Asia/Dubai), after M25 acceptance. Git commit
12:50:47 +04:00; remote publication verified by tracking-ref fetch at
12:52:09 +04:00. Exact push-completion second is not recorded.
**Publication:** Branch `feature/as-104-temporal-baseline`; feature commit
`09b38bd9c312470e948b1f17165ec5335cfc149d`, parent/base
`2006df7a70a4f48c66933aed96f4464d8d03084e`, message
`feat: implement AS-104 temporal baseline`, exactly **15 paths**. Pushed to
`origin/feature/as-104-temporal-baseline`; SHA equality/upstream/clean worktree
verified. No cache, credentials, external recovery or temporary scripts committed.
**Validation:** Before feature commit, 663 tests/Ruff/diff PASS with six existing
Rasterio warnings. M25/E25/EV-029 real acceptance, scalar 18/18, synthetic causal
and repeat checks PASS; all twelve cache hashes and six AS-103 IDs unchanged.
**Evidence:** [Publication §8](AS_104_TEMPORAL_BASELINE_VALIDATION.md#8-as-104-feature-publication--9-october-2026), M26/E26 and exact Git commit/remote metadata.
**Limit:** No new EO processing or scientific values. M23/E23/EV-027 remains
BLOCKED, M24–M25/E24–E25/EV-028–EV-029 remain acceptance-time PASS with original
stop states. Roughly 10% support is not failure/statistical sufficiency; small
positive scales can yield large z. No Decision 050, merge, GitHub CI success,
AS-105+ or P1 05.10 study. Review published commit and open PR only when authorized.

### EV-031 — AS-104 PR #12 merge and formal closeout

**Status:** AS-104 COMPLETE AND MERGED; real acceptance PASS; no unresolved AS-104
P0 blocker. Known scientific/coverage limitations remain documented.
**Date:** 9 October 2026, **2026-10-09T13:26:08+04:00 Asia/Dubai** /
**2026-10-09T09:26:08Z** merge; distinct from M25 acceptance and M26 publication.
**Merge:** PR #12, title `feat: implement AS-104 temporal baseline`; base `main`
at `2006df7a70a4f48c66933aed96f4464d8d03084e`, head `feature/as-104-temporal-baseline` at
`703af1176aeaf9ba38d31c53648907c3b1792aec`, merge `472edc737847dc8581290a372c5da28f71fc48f0`. Two commits/fifteen changed
paths: implementation `09b38bd9c312470e948b1f17165ec5335cfc149d` plus publication docs `703af1176aeaf9ba38d31c53648907c3b1792aec`.
**Evidence:** [Merge/closeout §9](AS_104_TEMPORAL_BASELINE_VALIDATION.md#9-pr-12-merge-and-as-104-closeout--9-october-2026), M27/E27 and verified Git merge metadata.
**Validation:** Final pre-merge 663 tests, Ruff/diff PASS, six existing Rasterio
warnings; accepted scalar 18/18, synthetic causal and repeat PASS. Temporal
product/fingerprint, eligible counts and all accepted AS-102 cache hashes /
AS-103 identities are preserved. This docs-only closeout does not rerun EO.
**Limit:** About 10% five-history support is retained, not hidden or relaxed.
Five observations are not statistical sufficiency; small positive scales can
yield large z. Rank is not probability/confidence/severity. No HAB/bloom,
chlorophyll, species/toxins, safety, intake risk, persistence, alerts, lead-time
or GitHub CI-success claim. EV-027 blocker, EV-028 fix, EV-029 acceptance and
EV-030 PR-pending publication remain historical. No Decision 050.
**Next:** Owner review of next milestone/AS-105 design before implementation;
separate authorization required. Both safety stashes/recovery artifacts retained;
AS-105+ and P1 homogeneous 05.10 NOT STARTED. No closeout PR or new merge in this task.

### EV-032 — AS-105 M28 offline geometry implementation

**Date/status:** Offline implementation 9 October 2026; owner-review clarification
10 October 2026 (Asia/Dubai), same Decision 050 / M28 / E28. PASS, synthetic only;
feature publication authorized, PR review follows Git/remote verification. Base `4e322df`.

**Observed engineering evidence:** 140 geometry cases/803 full tests PASS,
Ruff/diff and new-file whitespace PASS; six historical Rasterio warnings only.
Controls A–E cover deterministic repeat, valid irrelevant mutation, consumed-bit
identity/classification changes, eight-neighbour components and exact polygons.
All 55 mandated adversarial requirements pass, including output/provenance/policy
tampering and blocked IO/upstream paths. Protected source/tests/cache/handoff
hashes and safety stashes/recovery material remain unchanged.

**Evidence:** [offline validation](AS_105_HAB_ANOMALY_GEOMETRY_VALIDATION.md) and
[frozen contract](../AS_105_HAB_ANOMALY_GEOMETRY.md). Verified external AS-104
handoff is prerequisite evidence only, not a real geometry experiment.

**Limit:** Real candidate counts/fraction/area/regions/fragmentation/votes UNKNOWN;
real acceptance and future policy comparison NOT RUN, future checkpoint not
created. Rank is not probability/confidence/significance/severity; families are
not independent or biological proof. No HAB/concentration/species/toxins/safety/
intake-risk/persistence/alert/lead-time or GitHub CI-success claim. AS-106+ and
P1 05.10 NOT STARTED. EV-001–EV-031 remain historical and unchanged.

EV-032 owner-review addendum, 10 October: unchanged float32 0.90 policy has
coarse n=5 empirical-rank granularity; four new synthetic regressions PASS.
No smooth population-percentile, significance/probability/confidence/severity
claim. Predeclared future history-depth sensitivity is required and NOT RUN;
M29 retains the accepted minimum-five parent. This is the same checkpoint,
not new real geometry evidence.

### EV-033 — AS-105 M29 real geometry engineering acceptance

**Date/status:** 10 October 2026 (Asia/Dubai); first execution
05:45:15.046037–05:45:15.173566 UTC / 09:45:15.046037–09:45:15.173566 +04:00;
acceptance completed 05:45:46.711968 UTC / 09:45:46.711968 +04:00.
Owner review PASS; later documentation publication is separate. M28 implementation
`57100b2e53e941f3a7fdfdfc40b61d2b4043c0e5` is COMMITTED / PUSHED; no PR/merge timestamp, feature NOT YET PR-MERGED.

**Identity:** `hab_geometry:70876fbcb25e8a37abaa238a59e1da32fec9066792e6239db68e284b7bd18682`, input `c50d9f6300060ab9f194c1a0b8808de340eb53326268a52ef083ad7f994b2bc5`, output `ff976ec800ec2dfc966e4f373dd3f2442938a06a10254dd4ea7a86280dd0a765`,
version as105-v1; immediate parent `temporal:e814b0574ab30d1841778ee3c5005ffcb313ab42473c41acc028f0a9f7804a8b`. Grid EPSG:32640, 20 m, 310×228,
ID `88d76cf6265d9e0fa2802ed26324c02275e74721d4eb5b597cc9884a6d27aeec`.
**Result:** P **802** / target water **7,963**, coverage **10.071581%**;
C **7**, fraction **7/802 = 0.872818%**; descriptive C/water **0.087907%**;
**projected-grid candidate area 2,800 m² / 0.0028 km²**. One eight-connected
region, one MultiPolygon, three four-connected pieces; F2/F4 agreement,
family pixel counts **0,7,0,7,0**. Not three independent regions or biological proof.
**Granularity:** no supported float32(.90); observed .0/.2/.4/.6/.8/1 ranks made
>=float32(.90) equivalent to rank==1 for this parent only. Another four-below/
one-exact-tie five-history pixel can attain .90; unchanged algorithm/threshold.
Future history-depth sensitivity REQUIRED / NOT RUN.

**Engineering evidence:** exact handoff/parent/scene validation; independent
literal feature/family/P/C masks, labels/seeds/count, determinant area and exact
polygon rasterization PASS; repeat **27/27**, parent immutability **61/61**, external
bundle read-back/checksum audit PASS; zero real connection/HTTP/upstream/cache-load
attempts, no tuning/repository edits during execution. Focused **140**, full **803**
tests PASS, Ruff/diff PASS, six existing Rasterio warnings only. Protected handoff,
12 caches, both safety stashes and 13 recovery artifacts unchanged.
**Evidence:** [full M29 tables, region, timestamps and hashes](AS_105_HAB_ANOMALY_GEOMETRY_VALIDATION.md#m29--real-geometry-engineering-acceptance--10-october-2026);
M29/E29; `/workspace/aquasentinel-acceptance/as105/m29/`, external local evidence
artifact **NOT tracked in Git**, four read-only files with exact recorded hashes.
**Limits:** M29 establishes reproducible real candidate spectral anomaly geometry only. It does NOT establish confirmed HAB/bloom, chlorophyll concentration, species/toxins, biological causation, sensitivity/specificity/accuracy/false-positive rate, event agreement, persistence, risk/confidence, water safety, intake exposure, alert or warning lead time. No comparison with the historical April event was performed. Rank is not probability/confidence/significance/severity; policy families are not statistically independent. Five observations are not statistical sufficiency.
**Publication correction:** Owner confirmed verified red_edge_red_ratio rank-.4/.6 counts **240/92**, correcting the earlier chat transcription **238/93**; acceptance JSON hash unchanged, no rerun.
**Next:** Owner review of M29 documentation/publication followed by PR preparation;
future comparative policy validation REQUIRED / NOT RUN; no PR/merge, AS-106+
or P1 05.10. Decision 050 unchanged, no Decision 051. EV-001–EV-032 retained.

### EV-034 — AS-105 PR #14 merge and formal closeout

**Date/status:** 10 October 2026; **AS-105 COMPLETE AND MERGED**, M30 / E30 / EV-034.
PR #14 “feat: implement AS-105 HAB anomaly geometry” merged into `main` at
**2026-10-10T06:24:09Z / 2026-10-10T10:24:09+04:00 Asia/Dubai**.
Actual merge `24a260cff130238c731f7cb62fc47eb74230b4dc`; base before merge
`4e322df220f8cab2805fccf9a2b32dd825f29218`; head
`feature/as-105-hab-anomaly-geometry`, final head/M29 documentation commit
`1ac9fab9db48cca5625ead20e7133c79101a46d8`; implementation
`57100b2e53e941f3a7fdfdfc40b61d2b4043c0e5`. Two commits, 18 files,
3,315 additions / 30 deletions. No provisional merge SHA is used.

**Evidence:** [verified merge record](AS_105_HAB_ANOMALY_GEOMETRY_VALIDATION.md#m30--pr-14-merge-and-as-105-closeout--10-october-2026)
and [PR #14](https://github.com/Omar-Aboulwafa/aquasentinel-813/pull/14).
M28 synthetic/adversarial PASS and M29 real engineering PASS remain separate
historical records. EV-033 retains its original pre-merge checkpoint text.
Decision 050 is merged and unchanged; no Decision 051. The accepted product,
input/output fingerprints, 802/7,963 support, seven candidates, projected-grid
2,800 m² / 0.0028 km² area, one region/three parts and corrected rank counts
240/92 remain unchanged. No real processing rerun.

**Preservation/limits:** Source/tests byte-identical to official main; external
handoff/M29 bundle remain read-only, twelve accepted cache hashes unchanged,
both safety stashes and recovery artifacts retained. Local 803-test baseline,
Ruff/diff PASS and six existing Rasterio warnings do not establish CI success
or scientific accuracy. Scientific guardrails, sparse support and empirical
rank limitations remain intact; no HAB/event/biological/risk/operational claim.
Future comparative policy validation **REQUIRED / NOT RUN** across the original
predeclared dimensions. Merge/support-boundary visual capture pending.

**Next:** Owner review of the next milestone / AS-106 design before implementation.
AS-106+ is not authorized and **NOT STARTED**; P1 05.10 **NOT STARTED**.
This documentation closeout creates no PR and performs no merge.

## AS-106 design freeze and future evidence reservations — 10 October 2026

Decision 051 is owner-approved/frozen design only; [specification](../AS_106_PERSISTENCE.md).
This is not AS-106 implementation or real validation evidence. Historical
EV-001–EV-034 retain their original bodies and dates. No completed EV-035–EV-039
evidence record or implementation-validation placeholder document is created.

| Reserved future IDs | Scope | Current status |
|---|---|---|
| M31 / E31 / EV-035 | Offline implementation + synthetic/adversarial validation | NOT STARTED; separate implementation authorization |
| M32 / E32 / EV-036 | Metadata-only April inventory; network metadata only, NO imagery | NOT STARTED |
| M33 / E33 / EV-037 | Separately authorized missing April AS-102→103→104→105 preparation/handoffs | NOT STARTED |
| M34 / E34 / EV-038 | Offline real AS-106 engineering acceptance | BLOCKED ON FUTURE DATA PREPARATION / NOT STARTED |
| M35 / E35 / EV-039 | Owner review/publication/merge/closeout | NOT STARTED |

Existing accepted dates are March 4/9/14/24/29 and April 28; no verified earlier-
April cache or complete eligible inventory. Freeze every eligible April acquisition
before anomaly inspection, unchanged 05.09/grid/tile/orbit/cloud contracts and
the same accepted March references. Sparse/zero-candidate dates are not removed.
No recurrence measurement or biological/risk/confidence claim is supplied here.
AS-107+ / P1 05.10 NOT STARTED; AS-105 policy validation REQUIRED / NOT RUN.
