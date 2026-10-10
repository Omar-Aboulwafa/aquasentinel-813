# AquaSentinel 813 — Project State

## Current AS-106 M35 publication / closeout preparation — 10 October 2026 (Asia/Dubai)

**M35 / E35 / EV-039: PUBLICATION / CLOSEOUT PASS — READY FOR PR.**
**AS-106 before this closeout merge: CLOSEOUT READY.** Official real-acceptance
baseline merged via PR #20: `82e30c00a30ed893ad47c44c5a1e363661370d35`.
M31/M32/M33/M34 are **COMPLETE AND MERGED** via PR #17/#18/#19/#20;
M34 real engineering acceptance PASS. Decision 051 is FINAL / FROZEN / MERGED via
PR #16; its original dated design/scientific body and Decision 050 are unchanged.
No Decision 052.

**Durable closure rule:** AS-106 closure becomes official when this closeout branch
is merged to main. That merge itself makes **AS-106 COMPLETE / CLOSED** and
**M35 COMPLETE / MERGED / PUBLICATION-CLOSEOUT**. No extra post-merge documentation
loop is required merely to record that future merge SHA. Until then, M35 preparation
is complete and official closure is pending merge; this note records that preparation.
Current active development branch: none. This closeout was prepared on
`docs/as-106-closeout`. AS-107+ is NOT STARTED / NOT AUTHORIZED; owner design review
and separate authorization are required.

Accepted `as106-v1` product:
`hab_persistence:c576478b6b6d85894e5317e65a1d0fd6cee38ed1c406d452b10f97712d2cc3bb`.
Input fingerprint: `2f8f6f1c37bd9f8a236109ab821e6e426f222840c4a74f623d2e78bd76529ab7`.
Output fingerprint: `7739a3f97c0e88113a17629678a0ef31bdb14594400f0568c0dfdfdb5dabafef`.
Frozen April sequence: `2023-04-03T06:46:21.024000Z` →
`2023-04-28T06:46:29.024000Z`; unchanged M32 selection digest:
`570792066c1997b9a403249d994c4e7367bf2f1dafc6473b6e30df20cd6481d5`.
**P802 / Q793 / A7 / B7 / C0; history coverage 7/7=1.0; recurrence 0/7=0.0;
streak 1→7; exact observation gap 2,160,008,000,000 µs (25 days + 8 seconds).**

**No same-pixel candidate recurrence was observed among the 7 target candidate
pixels with valid prior observational history.** Exact-pixel observation only:
no neighborhood/motion/current compensation; unsupported history is UNKNOWN.
Two eligible dates retained; shared March references are not independent confirmation,
five histories are not statistical sufficiency, and the long gap proves neither
continuous biological presence nor absence. April 3's ~13% upstream policy coverage
is separate from target-candidate history 7/7. No species/toxin/HAB/absence-of-HAB,
risk/confidence/probability/water-safety/operational decision claim.

Anti-cherry-picking record: metadata froze all eligible dates before recurrence
inspection; both dates used the same contract; April 3 had 88 AS-105 candidates,
April 28 had 7, recurrence was 0, and zero was retained. No date, threshold, family
rule, connectivity or spatial tolerance was changed to strengthen the demo.
M34's four typed parents/common contract, 9/9 arrays/dtypes, Boolean/global/time/region
oracles, validator, same/reverse repeats, identity/fingerprints/time exclusion,
immutability/non-aliasing, seven tamper controls including rehash and sealed bundle
roundtrip all PASS. These are accepted engineering integrity results, not biology
or accuracy validation; they were not rerun during M35.

M35 changes only eight docs/evidence paths. No new science, upstream rerun, EO/data
network or download. Accepted bundle rehashed locally read-only and preserved;
caches/handoffs/M29/M32/M33/M34, modes, safety stashes and recovery files retained.
M35 final pytest/Ruff/diff/security results are recorded in the closeout evidence;
no GitHub CI-success claim. Historical M34 baseline is 993 tests/six Rasterio warnings.

Next: owner review of this prepared closeout and separately authorized PR/merge.
AS-107 may later consume observational recurrence, history coverage, exact timing
and provenance; it must not reinterpret them as biological truth. AS-107 design/
implementation remains separate. Future AS-105 policy validation REQUIRED / NOT RUN;
P1 05.10 NOT STARTED. No PR or merge performed in this task.

See [M35 closeout](evidence/AS_106_CLOSEOUT.md) and
[normalized closeout](evidence/AS_106_CLOSEOUT.json).
All older dated execution/design/evidence sections below are historical: their
M34/M35 unstarted, missing-stage, authorization and not-closed states remain intact
and do not describe current M35. The immutable Decision 051 design-freeze status
is its original historical checkpoint, not a current implementation-status claim.

## Historical AS-106 M34 real engineering acceptance — before PR #20 merge — 10 October 2026 (Asia/Dubai)

**M31 / M32 / M33: COMPLETE AND MERGED** via PR #17 / #18 / #19.
Official M34 base (PR #19 merge): `4cde14ee448079163c2a08f3951f8dac294f8dac`.
**M34 / E34 / EV-038: REAL AS-106 ENGINEERING ACCEPTANCE PASS / COMPLETE.**
Prepared on `data/as-106-real-acceptance`; no algorithm development. Decisions
050/051 scientific bodies unchanged; Decision 052 absent.

Frozen sequence: `2023-04-03T06:46:21.024000Z` → April 28 target
`2023-04-28T06:46:29.024000Z`. M32 selection digest unchanged:
`570792066c1997b9a403249d994c4e7367bf2f1dafc6473b6e30df20cd6481d5`.
Four accepted typed AS-104/105 objects reconstructed from read-only, checksum-verified
handoffs. No metadata/raster/XML retrieval or public upstream processing. All shared
grid/comparison/policy contracts and known input counts validated before computation.

Real `as106-v1` product:
`hab_persistence:c576478b6b6d85894e5317e65a1d0fd6cee38ed1c406d452b10f97712d2cc3bb`.
**Target P=802; Q=793; A=7; B=7; C=0.** Candidate-history coverage **7/7 = 1.0**;
recurrence fraction **0/7 = 0.0**; no target candidates lack prior history. Streak
histogram on A: **1→7**. Previous-valid gap: **2,160,008,000,000 µs** wherever Q,
-1 elsewhere; all target candidate spans 0 µs, -1 outside candidates. The single
AS-105 target region/labels are preserved; no recurrent span exists (regional
recurrent-span summaries are None).

**No same-pixel candidate recurrence was observed among the 7 target candidate
pixels with valid prior observational history.** This is observational engineering
acceptance, not biological/event validation or absence of HAB. April 3's ~13%
upstream policy coverage is a separate denominator, not target-history coverage.
Shared five March references are not independent confirmation/statistical sufficiency;
exact pixels cannot track motion; the 25-day+8-second gap does not establish continuous
biological presence or absence. No risk/confidence/probability/accuracy/safety claim.

Independent Boolean/global/region/time oracles and **9/9 exact arrays/dtypes PASS**;
parent-aware validation, same/reverse-order repeat, creation-time identity exclusion,
input immutability/output non-aliasing and seven tamper controls (including rehash)
PASS. External four-file acceptance bundle is read-only (files 0444, directory 0555);
fresh offline typed bundle roundtrip PASS. Scientific network/public upstream/transport
attempts **0**. Integrity validators' internal regeneration is the approved exception.

**190 focused persistence / 993 full tests PASS; Ruff/diff/whitespace/security PASS**;
six existing full-suite Rasterio warnings. Local checks, not GitHub CI. Only eight
docs/evidence paths change; source/tests/config/dependencies unchanged. All pre-existing
accepted caches/handoffs/M29/M32/M33, recovery files, modes and both safety stashes
preserved. New M34 bundle stays outside Git.

Foundation/continuity complete → AS-101/102/103/104/105 merged → AS-106 M31 offline
implementation merged → M32 frozen inventory merged → M33 upstream handoff merged →
**M34 real engineering acceptance complete** → **owner review and separately gated
M35 publication/closeout next**. AS-106 is **not fully closed**.
**M35: NOT STARTED.** AS-107+ / P1 05.10 NOT STARTED; future AS-105 policy validation
NOT RUN. No PR or merge in this task; this owner-authorized M34 evidence commit/push
is not M35 formal publication/closeout.

See [M34 evidence](evidence/AS_106_REAL_ACCEPTANCE.md) and
[normalized evidence](evidence/AS_106_REAL_ACCEPTANCE.json).
Older dated M33/M32/M31/design states below are historical and remain intact;
their earlier authorization/unstarted/readiness statements are not current status.

## Historical AS-106 M33 upstream preparation — before PR #19 merge — 10 October 2026 (Asia/Dubai)

**M31: COMPLETE / MERGED via PR #17. M32: COMPLETE / MERGED via PR #18.**
Official M33 base: `200affdb7fb6f8801744a192511e4200cc0d100d`. **M33 / E33 / EV-037:
APRIL-3 UPSTREAM PREPARATION + VERIFIED HANDOFF PASS / COMPLETE.** Prepared on
`data/as-106-april3-upstream-preparation`; no algorithm development or new Decision.
Decisions 050/051 remain frozen; Decision 052 absent.

The M32 sequence remains April 3 + April 28, selection SHA-256
`570792066c1997b9a403249d994c4e7367bf2f1dafc6473b6e30df20cd6481d5`. Only the exact April 3 observation
`2023-04-03T06:46:21.024000Z` was newly processed through existing AS-102→103→104→105,
using the frozen PC 05.09 product, fixed five March references and unchanged policy.
April 28 was reconstructed read-only for comparison/integrity, not newly extracted.

April 3: AS-102 valid water **6,096**; all six AS-103 features valid **6,096**;
AS-104 five-history eligible support **784/794/793/793/793/789** in canonical feature
order; zero-MAD counts **0**. Common April 3/April 28 comparison contract **PASS**.
AS-105 policy-evaluable **P = 794**, candidates **88**, candidate/P **11.083123%**,
**15 regions / 35,200 m²**. This is frozen observational anomaly geometry, not HAB
confirmation. No date or threshold was changed after seeing the result.

The separate external read-only M33 handoff stores **88 arrays** plus typed metadata.
Fresh offline reconstruction of both April dates **PASS**; April 3 typed parent-aware
geometry validation, semantic hashes/IDs/statistics/regions **PASS**. Network, public
extraction and recurrence entrypoints were blocked in that readiness test; their
call counts are zero. Existing validator regeneration is an integrity check only.

**408 focused / 993 full tests PASS; Ruff PASS; diff/new-file whitespace PASS**;
six existing full-suite Rasterio PendingDeprecationWarnings. Local checks, not CI.
No source/test/config/dependency change. Pre-existing accepted caches, April 28
handoff/M29 bundle, M32 inventory, both safety stashes and recovery material remain
byte-identical; historical permissions retained. New April 3 cache/handoff stay out
of Git. No credentials/signed asset URLs persisted.

Foundation/continuity complete → AS-101/102/103/104/105 merged → Decisions
048/049/050/051 retained → AS-106 M31 offline implementation merged → M32 frozen
metadata inventory merged → **M33 April 3 upstream preparation complete** →
**M34 INPUTS READY; owner review and separate M34 authorization required**.
**M34 / M35: NOT STARTED. REAL AS-106 ACCEPTANCE: NOT RUN.** AS-106 is not yet
complete. AS-107+ / P1 05.10 NOT STARTED; future AS-105 policy validation NOT RUN.
No PR or merge in this task. Immediate priority: owner review of M33 evidence and
verified handoffs before separately authorizing real recurrence acceptance.

See [M33 evidence](evidence/AS_106_APRIL3_UPSTREAM_PREPARATION.md) and
[normalized evidence](evidence/AS_106_APRIL3_UPSTREAM_PREPARATION.json).
The dated M32/M31/design and older status sections below are historical checkpoints;
their earlier missing/unstarted/authorization states are retained, not current.
M33 evidence publication is not M35.

## Historical AS-106 M32 metadata inventory — before PR #18 merge — 10 October 2026 (Asia/Dubai)

**M31: COMPLETE AND MERGED** via PR #17 at implementation merge commit
`723e13a900dba30b73a8a2da39df1d984233a2f4`. **M32 / E32 / EV-036: METADATA-ONLY APRIL
ACQUISITION INVENTORY PASS / COMPLETE.** Decision 051's scientific body is
unchanged; no Decision 052. Inventory prepared on
`data/as-106-april-metadata-inventory`, directly from that official main base.
No active algorithm development in M32.

**12 CDSE records / 2 post-filter candidates / 2 exact PC 05.09 matches /
2 eligible acquisitions:** `2023-04-03T06:46:21.024000Z` (Sentinel-2A) and
`2023-04-28T06:46:29.024000Z` (Sentinel-2B). Every returned record has a
disposition; 10 excluded records fail frozen tile/orbit rules. All 11 required
AS-102 asset keys are present in both selected PC metadata records. April 28
reconciles to the accepted target product. No pixel-equivalence claim.

Selection inventory SHA-256:
`570792066c1997b9a403249d994c4e7367bf2f1dafc6473b6e30df20cd6481d5`.
The sequence was selected metadata-first, before existing-stage availability
was audited; no anomaly values, support fractions or candidate outcomes were
used. **10 metadata HTTP requests**, only to
`stac.dataspace.copernicus.eu` and `planetarycomputer.microsoft.com`;
complete pagination, no credentials needed, **ZERO asset requests / ZERO
imagery bytes**. No raster/XML/thumbnail fetch, signing or new-date processing.

April 3: AS-102/103/104/105 **missing in audited accepted artifacts**;
future status `needs_as102_as103_as104_as105`. April 28: all four stages
**present through verified cache/evidence/handoff identities**;
`already_complete_for_sequence`. Existing AS-103 PASS descriptors are evidence,
not a new AS-103 disk cache. An eligible preparation failure must be reported,
never silently remove a date or weaken a frozen contract.

**993 tests PASS; Ruff PASS; diff/new-file whitespace PASS**; six retained
Rasterio PendingDeprecationWarnings. No source/test/config/dependency change;
accepted caches, AS-104 handoff, M29 bundle, safety stashes and recovery material
are retained unchanged. These are local checks, not GitHub CI claims.

Foundation/continuity complete → AS-101/102/103/104/105 merged → Decisions
048/049/050/051 retained → AS-106 M31 offline implementation merged → M32
metadata-only sequence frozen → **owner review and separate M33 authorization
required**. **M33 upstream preparation / M34 real recurrence acceptance /
M35 publication-closeout: NOT STARTED. REAL AS-106 ACCEPTANCE: NOT RUN.**
AS-107+ / P1 05.10 NOT STARTED; future AS-105 comparative policy validation NOT
RUN. Immediate priority: owner review of this frozen inventory and the April 3
AS-102→103→104→105 prerequisite before any separately authorized preparation.

See [M32 evidence](evidence/AS_106_APRIL_METADATA_INVENTORY.md) and
[normalized inventory](evidence/AS_106_APRIL_METADATA_INVENTORY.json).
The dated M31 implementation, design-freeze and earlier states below are
historical; their old PR/merge/authorization/inventory states are preserved and
do not describe current M32. This metadata evidence publication is not M35.

## Historical AS-106 M31 offline implementation — before PR #17 merge — 10 October 2026 (Asia/Dubai)

**M31 / E31 / EV-035: OFFLINE IMPLEMENTATION + SYNTHETIC/ADVERSARIAL VALIDATION PASS.**
Decision 051 is merged through PR #16 at official base
`57185444f0cc963cc899a25cd8179d7a31f12119`; its scientific body is unchanged.
Feature branch: `feature/as-106-persistence`; isolated worktree
`/workspace/aquasentinel-813-as106`. Owner authorized implementation and final
commit/push with `feat: implement AS-106 persistence`; owner feature review is next.
**PR NOT CREATED; FEATURE NOT MERGED.** These are local engineering checks, not CI.

**190 focused persistence tests / 993 full tests PASS**; Ruff and tracked/new-file
whitespace checks PASS. Focused suite has no warnings; full suite retains only
six existing Rasterio PendingDeprecationWarnings. No dependency or upstream
source/test/config/provenance-schema/cache-format change.

Pure recurrence over validated AS-105 parents; UNKNOWN skipped, supported
noncandidate breaks, exact pixels only, UTC int64 microseconds, honest B/A and
C/B fractions. Existing AS-105 validator regeneration is permitted integrity
verification, not new extraction. Immediate lineage parents are AS-105 only.
Real artifacts remain preserved and were not used for AS-106 computation.

**REAL AS-106 ACCEPTANCE: NOT RUN / BLOCKED ON FUTURE DATA PREPARATION.**
**REAL APRIL SEQUENCE PREPARATION: NOT STARTED.** M32 metadata inventory, M33
upstream preparation, M34 real acceptance and M35 publication/closeout remain
**NOT STARTED** and separately gated. No EO/service network attempts or imagery
downloads. AS-107+ / P1 05.10 NOT STARTED; future AS-105 policy validation NOT RUN.
See [AS-106 specification](AS_106_PERSISTENCE.md) and [M31 validation](evidence/AS_106_PERSISTENCE_VALIDATION.md).

Earlier dated design-freeze/publication/merge checkpoints below are historical;
their old implementation/authorization states do not describe current M31.

## Historical AS-106 design freeze — 10 October 2026 (Asia/Dubai)

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
See [AS-106 frozen design](AS_106_PERSISTENCE.md) and Decision 051.

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
See [AS-105 contract](AS_105_HAB_ANOMALY_GEOMETRY.md) and [M29 validation](evidence/AS_105_HAB_ANOMALY_GEOMETRY_VALIDATION.md#m29--real-geometry-engineering-acceptance--10-october-2026).

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

See [AS-105 contract](AS_105_HAB_ANOMALY_GEOMETRY.md) and [M28 validation](evidence/AS_105_HAB_ANOMALY_GEOMETRY_VALIDATION.md).

**Last updated:** 10 October 2026 (Asia/Dubai)
**Repository:** `Omar-Aboulwafa/aquasentinel-813`
**Default branch:** `main`
**Current active development branch:** `feature/as-106-persistence`. AS-106 M31 offline implementation/synthetic validation PASS; owner feature review is next. Real April preparation/acceptance and M32–M35 NOT STARTED. AS-107+ and P1 05.10 NOT STARTED; no real EO processing.
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
[validation §§6–7](evidence/AS_104_TEMPORAL_BASELINE_VALIDATION.md).

M23/E23/EV-027 remains the earlier **BLOCKED** platform-casing attempt; its body
and all prior checkpoint/decision bodies remain preserved. No Decision 050.
Both retained stashes and old/new external recovery artifacts remain available.
AS-104 stays **UNCOMMITTED / READY FOR REVIEW**. Owner review is the next gate;
no commit/push/PR/merge, AS-105+, or P1 homogeneous-05.10 experiment. PASS is
engineering acceptance of temporal candidate BOA signals, not biological or
operational accuracy, risk, persistence, alert or warning-lead-time validation.
Earlier dated checkpoint statements below are historical; this update governs
current state. Final quality/security verification is recorded in validation §7.

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
[AS-104 validation](evidence/AS_104_TEMPORAL_BASELINE_VALIDATION.md#5-pr-11-integration-and-five-reference-0509-attempt--9-october-2026).
Owner review/authorization of a targeted platform-representation fix and realistic
metadata tests is the next gate; do not mutate source records or accepted caches
to bypass it. AS-104 remains uncommitted for review. No new Decision 050, commit,
push, PR or GitHub merge; only the required local ff-only integration occurred.
AS-105+ and P1 homogeneous-05.10 study NOT started. No hazard, science accuracy,
operational risk, persistence, alert or warning-lead-time claim.

**Decision 048 implementation merge commit:** `39f2aee90c727fc151886efbdea44daec0e3f9b4` (PR #10); exact Decision 049 fix base.
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
[resumed evidence](evidence/AS_104_TEMPORAL_BASELINE_VALIDATION.md) / M21/E21/EV-025.
**P1 Processing Baseline Robustness Experiment — NOT STARTED**: homogeneous
05.09 versus homogeneous 05.10 requires separate authorization and is not
accuracy validation. AS-105+ is NOT authorized and NOT started. No commit,
push or PR in this integration task; retain the verified safety stash.

**Closeout preparation branch:** This closeout was prepared on `docs/as-103-post-merge-closeout`.
**AS-103 implementation merge commit:** `b770d0561da9ac2b81ca2d4b8e784adff66ee231` (merged via PR #8).
**AS-102 closeout preparation branch:** The AS-102 closeout was prepared on `docs/as-102-post-merge-closeout`.
**AS-102 implementation merge commit:** `627b6ae8a509509dbb2d5d43bbdc6d74e0ce2aac` (merged via PR #6).

**Historical Decision 049 fix checkpoint (9 October 2026, Asia/Dubai):** Decision
048 is merged via PR #10. Resumed AS-104 then encountered intermittent PC `/sign`
HTTP 504s. Only the separate reusable-account/container-token transport fix is
active here; no AS-104 algorithm work or real acceptance was resumed in this task.
Fix gate: **531 tests passed** (421 main baseline +110 net new transport cases),
Ruff/diff PASS, same six historical Rasterio warnings. Fresh March-4 smoke:
**1** anonymous token HTTP attempt/acquisition, **11/11** signed assets, bounded
XML/TIFF reads **1,024/4,096 bytes** via HTTP **206**, and **0** additional token
requests for B03/SCL/XML reuse. This is transport evidence only.
Original AS-104 status, 83 file hashes, accepted cache hashes and retained safety
stash remain unchanged. Decision 047/M19/E18–E19/EV-022–EV-023 and M21/E21/EV-025
remain only there; their bodies are not copied here. Decision 049/M22/E22/EV-026
belong to this isolated fix. Earlier Decision 048/AS-103 status wording below is
historical; this update governs current state. AS-104 real acceptance remains
BLOCKED pending Decision 049 review/merge. No commit/push/PR/merge; AS-105+ and
P1 homogeneous-05.10 robustness study NOT started.

**Historical AS-104 checkpoint (8 October 2026, Asia/Dubai):** Decision 047 supersedes
older AS-104 authorization statements in the preserved AS-103 checkpoints. Pure
API/models and offline validation are in review; real acceptance is blocked by
multiple same-observation PC processing products in unchanged AS-102 matching.
No commit/push/PR; no AS-105+ authorization. See the AS-104 section below.

**PoC deadline:** 11 October 2026
**Challenge:** Arab Youth Space Hackathon 2026 — Track 03: Water Security & Marine Environments

---

## 1. Current Status

AquaSentinel 813 is at the following stage:

**Foundation/continuity complete → AS-101/102/103/104/105 MERGED → Decision 051 MERGED/FROZEN → AS-106 M31 OFFLINE IMPLEMENTATION/SYNTHETIC VALIDATION PASS → owner feature review next (PR NOT CREATED / FEATURE NOT MERGED) → real April acceptance BLOCKED ON FUTURE DATA PREPARATION → M32–M35 / AS-107+ NOT STARTED; future AS-105 policy validation NOT RUN; P1 05.10 NOT STARTED.**

Completed engineering foundations:

- AS-001 — Repository Scaffold.
- AS-002 — Configuration & AOI Model.
- AS-003 — Provenance Model.

Continuity setup and Codex read-only onboarding are complete:

- AS-000C.1 — `AGENTS.md` completed and merged into `main`.
- AS-000C.2 — `docs/PROJECT_STATE.md` completed and merged into `main`.
- AS-000C.3–AS-000C.6 — PRD, decisions, handoff, and execution-plan documentation completed and merged into `main`.
- AS-000C.7 — Codex read-only onboarding **COMPLETED** on 2 October 2026 at `779069d`.
- AS-000C.8 — Codex development handoff **COMPLETED** with explicit AS-101 implementation authorization on 2 October 2026.

Completed AS-101 implementation and next milestone:

- AS-101 — Sentinel-2 STAC Search: completed on `feature/as-101-sentinel2-stac`, based on `origin/main` at `51f4ede`. Implementation is committed at `41a0b0b217cace909c906b7aedcb9cc6d0026f53` and documentation at `b3f0e9f878375f5fbfccb35519eeac5cc8fa48af`. AS-101, including the approved review fixes, is merged into `main` via [PR #2](https://github.com/Omar-Aboulwafa/aquasentinel-813/pull/2) at merge commit `1b83a732155ee01c01b7d33cb50115725cfb08c3`.
- Quality gate: **97 tests passed**, Ruff passed, and `git diff --check` passed.
- Real CDSE query returned **44 scenes** for the configured Al Raha AOI, 1 March–31 May 2023, cloud cover <= 30%; all converted to valid provenance records.
- AS-102 was explicitly authorized on 6 October 2026 and is **COMPLETE AND MERGED** through [PR #6](https://github.com/Omar-Aboulwafa/aquasentinel-813/pull/6). Implementation commit: `fe3d27046c40600010753957ee8921d57071ec48`. Merge commit: `627b6ae8a509509dbb2d5d43bbdc6d74e0ce2aac`, merged `2026-10-08T07:06:46Z` / `2026-10-08T11:06:46+04:00` Asia/Dubai. AS-103 is complete and merged through PR #8; AS-104 is COMPLETE AND MERGED through PR #12 at 472edc7, with implementation and frozen real acceptance PASS; AS-105 is COMPLETE AND MERGED through PR #14 at `24a260cff130238c731f7cb62fc47eb74230b4dc`, with M28 implementation/adversarial validation PASS and M29 real engineering acceptance PASS. Decision 051 remains frozen; AS-106 M31 offline implementation/synthetic validation PASS, with owner feature review next. M32–M35 and real April preparation/acceptance NOT STARTED; future AS-105 comparative policy validation REQUIRED / NOT RUN; AS-107+ and P1 05.10 NOT STARTED. See §23 and `docs/AS_102_OPTICAL_PREPROCESSING.md`.
- AS-103 is **COMPLETE AND MERGED** through [PR #8](https://github.com/Omar-Aboulwafa/aquasentinel-813/pull/8). Implementation commit: `5638bc8b4ab06f235f908642f714a7cc83b35709`. AS-103 implementation merge commit: `b770d0561da9ac2b81ca2d4b8e784adff66ee231`, merged `2026-10-08T10:43:24Z` / `2026-10-08T14:43:24+04:00` Asia/Dubai. See §24 and journal M18 / EV-021 for final review/merge and preserved acceptance evidence.

---

## 2. Product Definition

### Working product name

**AquaSentinel 813**

### Product vision

AquaSentinel 813 is an explainable, multi-hazard marine-intake intelligence system that combines Earth observation and environmental context to identify marine hazards offshore, assess their relevance to monitored desalination intake zones, and prioritize earlier field verification.

### Core principle

> AquaSentinel watches the sea before a threat reaches the intake.

### Primary user

Desalination Plant Water Quality / Operations Manager.

### Primary operational decision

> Where and when should monitoring or field verification be prioritized?

### PoC hazard scope

**Primary hazard:**
- HAB / biological water-quality anomaly.

**Secondary hazard:**
- Oil-slick / marine surface-pollution candidate.

### Product logic

Observation
→ Detection
→ Explanation
→ Exposure
→ Risk
→ Monitoring Priority
→ Human Decision

---

## 3. Scientific Guardrails

The product must avoid overclaiming what satellite observations prove.

Preferred language:

- HAB-like spectral anomaly.
- Elevated biological water-quality risk.
- Oil-slick candidate.
- Observational risk.
- Monitoring priority.
- Field verification recommended.
- Confidence.

The product must not claim that satellite data alone has:

- confirmed toxic algae,
- confirmed algal toxins,
- confirmed petroleum composition,
- certified water as safe or unsafe,
- justified autonomous desalination-plant shutdown.

Remote sensing supports earlier operational awareness and prioritization. Field and laboratory verification remain necessary.

---

## 4. Sensor Strategy

### Sentinel-2

Primary use:

- water colour,
- chlorophyll-related signals,
- red-edge features,
- biological/spectral anomaly detection,
- temporal comparison.

### Sentinel-1 SAR

Primary use:

- marine surface-slick candidates,
- oil-related surface anomalies,
- cloud-independent observation.

### EnMAP / future hyperspectral data

Primary use:

- detailed spectral characterization,
- confidence enhancement,
- multispectral-vs-hyperspectral comparison.

Hyperspectral data is a P1 enhancement, not a P0 dependency.

### Supporting environmental data

Potential P1 context:

- sea-surface temperature,
- currents,
- ERA5 wind,
- historical environmental conditions.

---

## 5. Current Technical Baseline

### Runtime

- Python: `3.11.17`
- Conda environment: `aquasentinel813`
- Project directory on office PC: `D:\aquasentinel-813`

### Development tools

- pytest
- Ruff
- Git
- GitHub
- VS Code

### Package layout

Python package:

`src/aquasentinel`

### Configuration

Main config:

`config/default.toml`

Current configuration includes:

- app metadata,
- AOI path,
- cache path,
- analysis date window,
- maximum cloud cover,
- risk bands,
- HAB PoC weights,
- oil PoC weights.

The current risk weights are PoC hypotheses, not validated scientific constants.

### AOI

Current validation GeoJSON:

`data/aoi/demo_site.geojson`

Current validation AOI:

- Al Raha Bay / Al Raha Beach validation area.
- Analyst-defined polygon.
- Includes a public geographic reference point.
- Does not represent a desalination intake.
- Must not be presented as an official environmental or administrative boundary.

---

## 6. AS-001 — Repository Scaffold — COMPLETE

Implemented:

- Git repository initialized.
- Default branch is `main`.
- Personal Git identity configured locally for the repository.
- Personal GitHub SSH alias configured separately from company access.
- GitHub personal repository created:
  - `Omar-Aboulwafa/aquasentinel-813`
- Python 3.11 Conda environment created.
- Editable package installation works.
- `pyproject.toml` created.
- `.gitignore` created.
- `.env.example` created.
- README created.
- Initial package created.
- Initial smoke test created.
- pytest and Ruff configured.

Initial foundation commit:

`f878acc chore: scaffold AquaSentinel 813 project`

---

## 7. AS-002 — Configuration & AOI Model — COMPLETE

Implemented modules:

- `src/aquasentinel/config/models.py`
- `src/aquasentinel/config/loader.py`
- `src/aquasentinel/config/aoi.py`
- `src/aquasentinel/config/__init__.py`
- `src/aquasentinel/runtime.py`

Implemented capabilities:

- TOML config loading.
- Analysis-date validation.
- Cloud-cover validation.
- Risk-band validation.
- Risk-weight normalization validation.
- AOI file-path validation.
- GeoJSON FeatureCollection loading.
- Point validation.
- Polygon validation.
- Longitude/latitude range validation.
- Polygon closure validation.
- Duplicate feature-ID rejection.
- Role lookup.
- Runtime context combining config and AOI.

Current demo AOI:

`data/aoi/demo_site.geojson`

AS-002 feature commit:

`f606ac5 feat: add configuration and AOI runtime model`

AS-002 merge commit:

`113ca44 merge: complete AS-002 configuration and AOI model`

---

## 8. AS-003 — Provenance Model — COMPLETE

Implemented package:

`src/aquasentinel/provenance/`

Implemented modules:

- `models.py`
- `serialization.py`
- `registry.py`
- `persistence.py`
- `__init__.py`

Implemented capabilities:

### Source records

Tracks:

- source ID,
- platform,
- source product ID,
- acquisition timestamp,
- catalog,
- collection,
- source URL when available,
- licence when available.

### Derived product records

Tracks:

- derived product ID,
- product type,
- creation timestamp,
- processing version,
- upstream source IDs,
- processing parameters.

### Validation

Implemented:

- non-empty identifiers,
- timezone-aware timestamps,
- source-reference requirements,
- duplicate-ID protection,
- JSON-serializable processing-parameter validation.

### Serialization

Implemented:

- source record → dictionary,
- derived record → dictionary,
- dictionary → source record,
- dictionary → derived record,
- JSON writing,
- UTC timestamp normalization,
- provenance schema version.

Current provenance schema version:

`1.0`

### Provenance registry

Implemented:

- add source,
- add derived product,
- reject duplicate records,
- reject unknown upstream references,
- retrieve source,
- retrieve derived product,
- recursively resolve lineage.

Expected lineage:

Source observation
→ derived feature
→ hazard layer
→ risk product
→ operational alert

### Registry persistence

Implemented:

- save full provenance registry to JSON manifest,
- restore registry from manifest,
- resolve multi-step derived dependencies while loading.

AS-003 feature commit:

`e2baedc feat: add provenance tracking and lineage registry`

AS-003 merge commit:

`db79260 merge: complete AS-003 provenance model`

`db79260` is the known `main` state immediately before Codex/continuity setup began.

---

## 9. Current Test / Quality Status

AS-106 M31: **190 focused / 993 full tests PASS**, Ruff/diff/new-file whitespace
PASS. No focused warnings or new warnings; only six retained Rasterio warnings
in the full suite. All 803 pre-AS-106 tests remain passing. This is synthetic
engineering acceptance, not real recurrence, biological accuracy or GitHub CI.

Historical AS-105 M28/M29 baseline: 140 geometry / 803 full tests PASS, six
existing Rasterio warnings; accepted M29 real engineering evidence is unchanged.
Historical AS-104 reviewed baseline: 663 tests PASS and six existing warnings;
frozen scalar/causal/repeat checks remain PASS. M32–M35, AS-107+ and P1 05.10
are NOT STARTED; future AS-105 policy validation is NOT RUN.

Historical merged AS-103 reviewed baseline: **348 tests passed**, Ruff/diff check passed; six existing non-blocking Rasterio PendingDeprecationWarnings only, with no new AS-103 warnings. No configured/reported GitHub Actions/workflow CI run; no GitHub CI pass is claimed. No new dependency; AS-104 NOT authorized and NOT started.

Historical merged AS-102 quality baseline: **265 tests passed**, Ruff passed, and `git diff --check` passed, with six non-blocking Rasterio deprecation warnings. The historical 6 October implementation acceptance was **213 tests passed**; see §23 for live acceptance/cache evidence and final review/merge. The historical baselines below remain distinct.

At the completion of AS-003:

- pytest: **17 passed**
- Ruff: **All checks passed**
- `main` working tree: clean
- `main` synchronized with `origin/main`

Standard quality gate:

```text
python -m pytest -v
python -m ruff check .
```

These commands must continue to pass before merge.

---

## 10. Git / Account Setup

This office computer is also used with company systems.

The AquaSentinel repository must use the user's personal GitHub account without changing company Git configuration.

Personal GitHub account:

`Omar-Aboulwafa`

Personal repository SSH remote pattern:

`git@github.com-omar-personal:Omar-Aboulwafa/aquasentinel-813.git`

Current `origin` should remain:

`git@github.com-omar-personal:Omar-Aboulwafa/aquasentinel-813.git`

Personal SSH alias:

`github.com-omar-personal`

Do not modify machine-global Git identity or the company's GitHub configuration without explicit approval.

---

## 11. Multi-Machine Strategy

The project must be usable from:

- office PC,
- personal PC,
- Codex/cloud environments.

The repository is the source of truth.

### Before switching machines

Run:

1. tests,
2. Ruff,
3. commit,
4. push.

### On the other machine

Run:

1. pull/fetch,
2. activate or recreate the Python 3.11 environment,
3. install the project and development dependencies,
4. run tests,
5. continue from a task-specific branch.

Do not use Git to transfer:

- `.env`,
- passwords,
- tokens,
- SSH private keys,
- machine-specific secrets.

---

## 12. Codex / Continuity Strategy

Reason for AS-000C:

The project must not depend on one ChatGPT conversation or one agent context window.

Repository documentation must allow a new ChatGPT session, Codex task, another computer, or another developer to recover current project state.

### Required continuity files

- `AGENTS.md`
- `docs/PROJECT_STATE.md`
- `docs/DECISIONS.md`
- `docs/HANDOFF.md`
- `.agent/PLANS.md`

All required continuity files are committed and merged into `main`.

### Agent startup sequence

A new coding agent should:

1. Read `AGENTS.md`.
2. Read `docs/PROJECT_STATE.md`.
3. Read relevant decision/architecture documentation.
4. Inspect the current branch.
5. Run `git status`.
6. Inspect relevant tests/code.
7. Run the current test suite before making meaningful changes when practical.

Do not rely on chat memory for critical project decisions.

---

## 13. AS-000C — Codex & Continuity Setup — COMPLETE

### AS-000C.1 — AGENTS.md

Status:

**Completed and merged into `main`.**

Purpose:

- repository-level coding-agent instructions,
- scope protection,
- scientific guardrails,
- Git rules,
- dependency rules,
- testing rules,
- agent workflow.

### AS-000C.2 — PROJECT_STATE.md

Status:

**Completed and merged into `main`.**

### AS-000C.3 — PRD / scope reference

Status:

**Completed and merged into `main`.**

The approved AquaSentinel PRD is available at `docs/AquaSentinel_813_PRD_v1.0.md`.

### AS-000C.4 — DECISIONS.md

Status:

**Completed and merged into `main`.**

Must capture major decisions and reasons, including:

- why Track 03,
- why multi-hazard vision,
- why HAB is the primary PoC hazard,
- why oil is secondary,
- why Sentinel-2 for biological anomaly,
- why Sentinel-1 for oil,
- why hyperspectral is P1,
- why satellite outputs remain observational,
- why Python 3.11,
- why provenance was built before data ingestion,
- why the repo is the source of truth.

### AS-000C.5 — HANDOFF.md

Status:

**Completed and merged into `main`.**

Must enable a fresh human or agent to continue with minimal context.

### AS-000C.6 — `.agent/PLANS.md`

Status:

**Completed and merged into `main`.**

Defines how longer Codex tasks should be planned and reported.

### AS-000C.7 — Codex read-only onboarding

Status:

**COMPLETED.**

Completed on 2 October 2026 at `779069d`. Codex inspected the repository documentation, architecture, configuration/AOI, provenance, and tests, and returned a structured onboarding report without modifying repository files. Repository understanding has been verified.

### AS-000C.8 — Codex development handoff

Status:

**COMPLETED.**

AS-101 was explicitly authorized on 2 October 2026 as the first development task after onboarding. The handoff specified CDSE as the default provider, catalog-only scope, minimal dependencies, provenance integration, offline tests, a real-data smoke test, and initial review before committing. Onboarding alone did not authorize implementation; the separate development instruction did.

---

## 14. AS-101 — Sentinel-2 STAC Search — COMPLETE AND MERGED

### Name

**AS-101 — Sentinel-2 STAC Search**

### Goal

Given:

- configured AOI,
- configured date window,
- configured cloud-cover limit,

return real Sentinel-2 observations suitable for downstream water analysis.

### Initial task scope

AS-101 should focus on:

- selecting a stable STAC catalog/endpoint,
- catalog search,
- AOI intersection,
- time-range filtering,
- cloud-cover filtering,
- deterministic result representation,
- conversion of returned observations into AquaSentinel provenance records,
- tests.

### Explicit non-goals for AS-101

Do not yet:

- download full Sentinel-2 imagery,
- implement atmospheric correction,
- compute HAB indices,
- build the dashboard,
- build the ML risk model.

Search/catalog integration comes first.

### Implementation and validation

- Configurable CDSE STAC endpoint, collection, and per-request timeout.
- Primary validation Polygon passed as `intersects`; inclusive UTC date window and `eo:cloud_cover <= threshold` query.
- Full pagination without a result cap; explicit errors for incomplete/cyclic pagination, catalog failures, and missing/malformed item metadata.
- Typed metadata candidates sorted by acquisition time and item ID; identical duplicates collapsed and conflicting duplicates rejected.
- Provider-qualified `SourceRecord` mapping; upstream provenance models remain unchanged.
- Only new direct dependency: `pystac-client==0.9.0`.
- **97 tests passed**, including all 17 original tests; Ruff and `git diff --check` passed.
- Live CDSE smoke test on 2 October 2026 returned **44 scenes**, from `2023-03-04T06:47:51.024Z` through `2023-05-28T06:46:29.024Z`; provenance conversion succeeded for every scene.

Implementation and smoke-test details: `docs/AS_101_STAC_SEARCH.md`.

AS-101 is complete and merged into `main` via PR #2 at merge commit `1b83a732155ee01c01b7d33cb50115725cfb08c3`. No raster imagery was downloaded, and catalog availability does not demonstrate HAB detection or usable water pixels. AS-102 is now complete and merged through PR #6; see §23. This establishes preprocessing, not HAB detection or aquatic suitability.

---

## 15. Planned Milestones After AS-101

Expected sequence:

- AS-101 — Sentinel-2 STAC Search (complete and merged via PR #2).
- AS-102 — Optical Preprocessing (COMPLETE AND MERGED through PR #6).
- AS-103 — Spectral Feature Extraction (COMPLETE AND MERGED through PR #8).
- AS-104 — Temporal Baseline (COMPLETE AND MERGED through PR #12; implementation and real acceptance PASS).
- AS-105 — HAB Anomaly Geometry.
- AS-106 — Persistence.
- AS-107 — HAB Risk & Confidence.
- AS-108 — HAB Historical Validation.

Then oil pipeline work:

- AS-201 — Sentinel-1 retrieval.
- AS-202 — SAR preprocessing.
- AS-203 — Low-backscatter candidate detection.
- AS-204 — Candidate filtering.
- AS-205 — Temporal/reference comparison.
- AS-206 — Oil risk & confidence.
- AS-207 — Historical oil validation.

P1 environmental/hyperspectral work should not block P0.

---

## 16. Validation Strategy

### HAB validation

Primary candidate:

**Al Raha Beach / Al Raha Bay, Abu Dhabi — April 2023**

Target analysis:

- pre-event,
- event,
- post-event/recovery.

Questions:

- was there a meaningful satellite-observable anomaly,
- which features changed,
- did the anomaly persist,
- could an earlier monitoring signal have been raised?

### Oil validation

Primary candidate:

**Kharg Island / Persian Gulf — May 2026**

Target analysis:

- Sentinel-1 slick-like anomaly,
- multi-date persistence/change,
- optical/context support when available,
- exposure demonstration.

Historical event reports and EO-derived observations must remain clearly distinguished.

---

## 17. PoC Scope Protection

P0 must be protected.

If schedule pressure increases, simplify or remove P1 work before weakening:

1. real EO-derived results,
2. scientific credibility,
3. validation,
4. explainability,
5. provenance,
6. reproducibility,
7. working demo.

Possible P1 cuts include:

- advanced drift simulation,
- hyperspectral integration,
- fitted ML classifier,
- advanced exports,
- visual polish.

---

## 18. Known Risks

### Technical

- cloud cover may prevent optical validation on ideal dates,
- Sentinel-1 oil detection has natural/low-wind look-alikes,
- hyperspectral scenes may not coincide with historical events,
- public external services may require credentials or become temporarily unavailable.

### Scientific

- water-colour anomaly is not equivalent to toxic HAB confirmation,
- low SAR backscatter is not equivalent to confirmed petroleum,
- risk weights remain PoC hypotheses until properly validated,
- limited labelled Gulf data may make anomaly detection preferable to overfit classification.

### Delivery

- deadline is close,
- scope expansion is a major risk,
- live API dependence during demo is risky.

Mitigation:

- maintain cached validated demo assets,
- preserve provenance,
- keep P0 independent of P1 external data where possible,
- record limitations explicitly.

---

## 19. Important Repository Rules

Never commit:

- `.env`,
- API credentials,
- SSH private keys,
- passwords,
- proprietary company credentials,
- large raw EO scenes,
- runtime caches.

Use:

- `.env.example`,
- STAC/product references,
- provenance manifests,
- reproducible scripts,
- small fixtures.

All meaningful code changes require tests where appropriate.

---

## 20. How to Resume the Project in a Fresh Session

Use the following recovery procedure:

1. Open the repository.
2. Read `AGENTS.md`.
3. Read this file.
4. Run:
   - `git status`
   - `git branch --show-current`
   - `git log --oneline --graph --decorate -8`
5. Activate the `aquasentinel813` Python 3.11 environment.
6. Run:
   - `python -m pytest -v`
   - `python -m ruff check .`
7. Read `docs/DECISIONS.md` and `docs/HANDOFF.md` when available.
8. Continue the next incomplete task listed in this document.

Do not reconstruct important project state from memory when repository evidence exists.

---

## 21. Immediate Next Action

Owner review of the published AS-106 M31 feature implementation and synthetic
engineering evidence. No PR is created or merge performed here. Decision 051
is unchanged. Do not automatically advance: M32 metadata-only April inventory,
M33 missing-date upstream preparation, M34 offline real recurrence acceptance
and M35 publication/closeout all require their own authorization and are NOT STARTED.
Real acceptance remains blocked on future preparation; no verified earlier-April
cache/inventory exists. Preserve accepted handoffs/bundles/cache hashes, both
safety stashes and recovery artifacts. AS-107+ / P1 05.10 NOT STARTED; future
AS-105 policy validation REQUIRED / NOT RUN.

---

## 22. Definition of Current Success

At the current point, the project is healthy if:

- `main` remains clean and synchronized,
- the test suite passes,
- Ruff passes,
- continuity documentation is committed,
- a new session/agent can understand the project without chat history,
- AS-101 is complete and merged into `main` via PR #2, with passing offline checks and a successful real catalog smoke test,
- AS-102 is COMPLETE AND MERGED through PR #6 with final reviewed checks and traceable evidence; AS-103 is COMPLETE AND MERGED through PR #8 with reviewed feature/identity/lineage evidence; AS-104 is COMPLETE AND MERGED through PR #12 at 472edc7, with implementation and frozen real acceptance PASS; AS-105 is COMPLETE AND MERGED through PR #14 at `24a260cff130238c731f7cb62fc47eb74230b4dc`, with M28 implementation/adversarial validation PASS and M29 real engineering acceptance PASS. Decision 051 remains frozen; AS-106 M31 offline implementation/synthetic validation PASS, with owner feature review next. M32–M35 and real April preparation/acceptance NOT STARTED; future AS-105 comparative policy validation REQUIRED / NOT RUN; AS-107+ and P1 05.10 NOT STARTED.


## 23. AS-102 — Optical Preprocessing — COMPLETE AND MERGED

The AS-102/AS-103 handoffs below preserve their merge-time checkpoints, including
the then-current AS-104 authorization status. M27 above and the final closeout
handoff supersede those next-step instructions; their historical bodies are retained.

AS-102 was explicitly authorized on 6 October 2026 and is **COMPLETE AND MERGED** through [PR #6](https://github.com/Omar-Aboulwafa/aquasentinel-813/pull/6). Implementation commit: `fe3d27046c40600010753957ee8921d57071ec48`. Merge commit: `627b6ae8a509509dbb2d5d43bbdc6d74e0ce2aac`, merged `2026-10-08T07:06:46Z` / `2026-10-08T11:06:46+04:00` Asia/Dubai. AS-103 is complete and merged through PR #8; AS-104 remains NOT authorized and NOT started.

- CDSE discovery is preserved; Planetary Computer supplies the actual raster product, with strict time/platform/tile/orbit matching and independent product provenance.
- Nine native reflectance bands plus SCL and product XML; XML-driven offsets/quantification, bounded COG reads, fixed 20 m EPSG:32640 AOI grid (310 × 228), bilinear reflectance/nearest SCL, and all-band conservative interpolation/water support.
- Fresh real acceptance began `2026-10-06T10:07:14.660936+00:00` / `2026-10-06T14:07:14.660936+04:00` Asia/Dubai. CDSE returned 44 candidates; known April 28 observation matched PC baseline 05.09 separately from CDSE 05.10.
- AOI 67,449 pixels; valid data 65,166; candidate water 10,211; retained valid water 7,963; AOI water fraction 0.11805957093507688 (11.805957%); water retention 0.7798452649103907 (77.984526%). Excluded candidate water: 2,248. These are mask outcomes, not confirmed water/HAB or aquatic suitability.
- AOI cache/checksum reload is equivalent and uses no network/signing/raster work when the cache ID is known. Runtime cache material remains ignored.
- AS-102 final reviewed quality baseline: **265 tests passed**, Ruff passed, `git diff --check` passed. Six Rasterio deprecation warnings remain non-blocking. The historical 6 October implementation acceptance was **213 tests passed** (all prior 97 retained), with two transitive Affine warnings. Python 3.11.16 / NumPy 2.2.6 / Rasterio 1.4.3 / GDAL 3.9.3 in that cloud run. GitHub reported clean/mergeable before merge and no configured/reported CI/workflow checks; no GitHub CI pass is claimed.
- Decisions 039–045 record the newly authorized contract. EV-016/EV-017 and journal M15 preserve the 6 October implementation evidence; EV-018 and journal M16 record final review/merge. Historical EV-014 PENDING and later FG-01 PASS/READY plus EV-015 remain preserved.
- L2A BOA reflectance is not aquatic Rrs; coastal/turbid/mixed-water SCL errors remain. No indices, chlorophyll, HAB/toxin/water-safety/intake-risk or lead-time conclusions were computed.

Plan/API/limits: `docs/AS_102_OPTICAL_PREPROCESSING.md`. Real evidence: `docs/evidence/AS_102_OPTICAL_PREPROCESSING_VALIDATION.md`. No source cache, raw scene or signing credentials belong in Git.


## 24. AS-103 — Spectral Feature Extraction — COMPLETE AND MERGED

AS-103 is **COMPLETE AND MERGED** through [PR #8](https://github.com/Omar-Aboulwafa/aquasentinel-813/pull/8). Implementation commit: `5638bc8b4ab06f235f908642f714a7cc83b35709`. AS-103 implementation merge commit: `b770d0561da9ac2b81ca2d4b8e784adff66ee231`, merged `2026-10-08T10:43:24Z` / `2026-10-08T14:43:24+04:00` Asia/Dubai.

Final reviewed baseline: **348 tests passed**, Ruff passed and `git diff --check` passed; six existing non-blocking Rasterio PendingDeprecationWarnings only, with no new AS-103 warnings. No GitHub Actions/workflow CI run was configured/reported; no GitHub CI success is claimed.

AS-103 development is closed. AS-104 — Temporal Baseline is NEXT PLANNED only, NOT authorized and NOT started; a future agent must obtain separate explicit authorization before implementing it. The completed stage produces candidate per-scene BOA spectral signals only, not temporal anomalies, HAB presence, chlorophyll concentration, species, toxins, water safety, intake exposure, operational risk, persistence or warning lead time.

### Historical implementation/acceptance checkpoint — M17 / EV-019–EV-020

The following records the initial feature-branch acceptance state. Its uncommitted/unpushed/unmerged wording is historical; the later review/publication stage is M18 / EV-021. The cached real-scene experiment was not rerun during merge review or this documentation closeout.

AS-103 was explicitly authorized on 8 October 2026 and is implemented/validated on `feature/as-103-spectral-features`, based on main `642a469414f096b4ac7cd96de895aa38f7da42ec`. Changes remain uncommitted, unpushed and unmerged for code review; no PR. AS-104 is next planned but NOT authorized and NOT started.

- Execution plan was written before implementation; Decision 046 freezes the accepted contract.
- Pure `extract_spectral_features(scene)` with six canonical signed-BOA candidate features;
  nominal MCI 665/705/740 nm, k=1.0, no threshold or event inference.
- Float64 arithmetic, float32 arrays, feature-specific masks within unchanged AS-102 water;
  fixed 1e-4/1e-6 denominator guards, NaN outside support, typed statistics/diagnostics.
- Versioned SHA-256 mask/five-band input fingerprint and canonical deterministic identity;
  immediate AS-102 derived parent lineage, not a raw-source shortcut. No AS-103 disk cache.
- Cached acceptance at `2026-10-08T09:52:47.133486+00:00` UTC / `2026-10-08T13:52:47.133486+04:00`
  Asia/Dubai: same EPSG:32640 310×228 grid, 7,963 parent pixels and 7,963 valid pixels
  for each feature; no denominator/nonfinite exclusions. Two unclipped NDCI-like values
  outside [-1,1]; negative-input counts 2 for B05/red and 491 for B06-inclusive features.
- Repeated arrays/masks/summaries/identity and PC→AS-102→AS-103 lineage verified;
  four independent scalar pixel checks; external access/write entry points blocked.
- **348 tests passed** (265 retained +83 new), Ruff and diff checks passed.
  Six existing Rasterio PendingDeprecationWarnings; no new AS-103 warnings.
- AS-102 source/config/dependencies/cache format and generic provenance were preserved.
- BOA is not aquatic Rrs; features are not HAB, chlorophyll concentration, species,
  toxins, safety, shutdown, risk or lead-time evidence. Temporal/event validation remains
  future. Reference-page retrieval HTTP 403 is recorded without claiming a live fetch.

Read [AS-103 execution plan/API](AS_103_SPECTRAL_FEATURES.md) and
[acceptance evidence](evidence/AS_103_SPECTRAL_FEATURES_VALIDATION.md).
Use `extract_spectral_features(parent)` after the existing verified AS-102 cache reload;
no feature cache or network is required. AS-103 implementation is complete and merged; see journal M18 / EV-021 for final review/publication.
AS-104 — Temporal Baseline remains NEXT PLANNED only, NOT authorized and NOT started.


## 25. AS-104 — Historical Initial Review Checkpoint (8 October 2026)

**Date:** 8 October 2026 (Asia/Dubai). **Branch:**
`feature/as-104-temporal-baseline`; exact base main
`c6accab2c5753734466a6375d1b3ce1762e99bed`. Decision 047 was explicitly authorized.
The execution plan was written before source implementation. No commit/push/PR.

The pure target-ID API selects UTC-normalized strictly-prior observations within
explicit bounds. Per-feature/pixel median, MAD, scale 1.4826, signed deviation,
standardized anomaly and exact-tie midrank preserve target support. Zero scale
retains baseline/deviation/rank but masks standardized anomaly. Semantic hashes
consume reference values/support only within target feature support. No precision
noise-floor diagnostic, epsilon, fallback, clipping or feature combination.
Immediate parents are target AS-103 then chronological references; registry remains
read-only. No dependency/config/cache-format/upstream/provenance-schema changes.

**Offline gate:** 460 tests passed (348 retained +112 temporal cases), Ruff/diff
checks passed; six existing Rasterio PendingDeprecationWarnings, no new warnings.
Use existing `.venv/bin/python` (3.11.16) in this cloud checkout; the default shell
Python lacks pytest/Ruff. No installation was required.

**Real acceptance: BLOCKED, not complete.** Fixed target April 28, references
March 1–April 1 UTC, minimum 5. AS-101 returned 44 configured candidates; five
March observations match tile 40RBN/orbit 20. First reference March 4 has two PC
products for the exact same observation: baselines 05.09 and 05.10. Unchanged
AS-102 rejects exactly-one-match ambiguity. The experiment stopped before any
reference raster reads; zero historical scenes were processed. Reused target has
7,963 valid pixels per feature, but real temporal support/summaries, AS-104 ID,
scalar checks and later-real-scene causality were NOT produced/run. Offline tests
are not substitutes for real multi-scene evidence. No selection workaround or
upstream algorithm change was made.

**Next action:** owner code/science review of the uncommitted AS-104 implementation
and the provider-product ambiguity blocker. A separate authorization would be
required to investigate/change AS-102 delivered-product selection or retry with a
changed contract. Do not widen dates, lower minimum, mix baselines or relax masks.
AS-105/106/107/108 remain NOT authorized and NOT started. No HAB/event, significance,
probability/confidence, risk, safety or historical warning lead-time claim.

[Plan/API](AS_104_TEMPORAL_BASELINE.md), [EV-022/EV-023 evidence](evidence/AS_104_TEMPORAL_BASELINE_VALIDATION.md),
journal M19 / engineering E18–E19. Prior AS-101/102/103 records are historical and
remain preserved; this separately dated update controls current AS-104 state.

## 26. Decision 048 — Historical Pre-Merge Fix Review Checkpoint

- Explicitly authorized 8 October 2026; base `c6accab2c5753734466a6375d1b3ce1762e99bed`.
- Separate branch/worktree; no AS-104 file copied, changed, staged or committed.
- Optional keyword-only `required_processing_baseline` in matching, resolution
  and optical entry points. None preserves strict existing behavior; explicit
  NN.NN filters validated exact matches then still requires exactly one.
- Known-ID and ordinary cache returns enforce recorded actual baseline. The
  selector is not a new identity dimension; schema, manifests, pixels and lineage
  stay unchanged. Existing April cache accepts 05.09/rejects 05.10 without writes.
- **421 tests passed** (348 retained +73 new); Ruff/diff passed; same six historical
  Rasterio warnings. Real metadata smoke March 4/9/14/24/29 plus April 28: **6/6**
  resolved the exact expected 05.09 products with forbidden access/write calls **0**.
- Source resolution only: no March XML/raster/support or AS-104 success claim.
- Decision 047 and M19/E18–E19/EV-022–EV-023 remain in the original AS-104 worktree;
  owner-approved cross-worktree numbering uses M20/E20/EV-024 here. Decisions 039
  and all prior milestone/evidence entries remain unchanged.
- [Plan/API](AS_102_REQUIRED_PC_BASELINE_FIX.md),
  [validation](evidence/AS_102_REQUIRED_PC_BASELINE_FIX_VALIDATION.md).
- Fix uncommitted/unpushed/unmerged; no PR. AS-104 uncommitted/preserved, real
  acceptance BLOCKED pending upstream review/merge and separate rerun; AS-105+
  NOT authorized/NOT started.

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

## Historical Decision 049 — Reusable PC SAS Transport Fix — IN REVIEW

Plan: [AS-102 reusable-token fix](AS_102_REUSABLE_PC_SAS_TOKEN_FIX.md).
Evidence: [EV-026 validation](evidence/AS_102_REUSABLE_PC_SAS_TOKEN_FIX_VALIDATION.md).
Branch/worktree/base are recorded in the header. Decision 049 is explicitly
owner-authorized; implementation and documentation remain uncommitted for review.

`sign_asset(href, settings)` preserves its public API and strict unsigned-HREF
allowlist. Derive validated Azure account/container and official token route from
the configured HTTPS SAS issuer; no hardcoded asset scope, API key, SDK, new
config or dependency. Private process-memory tokens are reused across assets/
scenes while >60 seconds remain and refreshed at <=60 seconds. At most five
acquisition attempts for HTTP 429/500/502/503/504 or typed transient connection/
timeouts, with 0.8/1.6/3.2/6.4-second delays. Invalid payload/security/type errors
and other HTTP statuses are terminal. Never persist/log token or signed HREF.

Stable unsigned source/provenance/cache identity remains unchanged. Existing
bounded HTTP reader/redirect/security checks and all XML/raster callers remain
unchanged, with no generic provenance/schema/decoding/grid/mask/resampling or
AS-103/AS-104 algorithm change. No new raster/cache product was created.

**531 passed**, Ruff/diff PASS, six unchanged Rasterio warnings. Real March-4
05.09 smoke at 06:44:49–06:44:51 UTC / 10:44:49–10:44:51 Asia/Dubai on 9 October:
one anonymous token HTTP 200, eleven transient signs from one scope, XML 1,024
bytes and B02 TIFF header 4,096 bytes (both 206), three reuse signs with zero
additional token requests. No full processing or AS-104 acceptance claim.

Preserve original `/workspace/aquasentinel-813` on
`feature/as-104-temporal-baseline` at `39f2aee90c727fc151886efbdea44daec0e3f9b4`:
never switch/stash/apply/drop/reset/clean/stage/commit/format/edit it for this fix.
Safety stash `f93950aab6fdfb40bb100158915ef12692aa1665` stays intact. Cross-worktree
history belongs to its existing owner; this fix uses only Decision 049/M22/E22/
EV-026, preserving Decision 048/M20/E20/EV-024 history. Next gate is owner review
and merge of this fix before separately rerunning AS-104 real acceptance.
No AS-105+, P1 05.10 study or GitHub CI-success claim.

## PR #11 integration / AS-104 real acceptance handoff — M23 / EV-027

Both safety stashes remain retained: older
`f93950aab6fdfb40bb100158915ef12692aa1665` and NEW
`d979a433a5ab8ae600282048f184eb5fd06a8f17` (applied without pop).
External recovery files remain available at:
`/workspace/as104-before-pr11-integration.patch`,
`/workspace/as104-before-pr11-untracked.tar.gz`,
`/workspace/as104-before-pr11-sha256.json`. No source/tests were rewritten.

All five March 05.09 parents are cached under ignored `data/cache/as102/`; keep
large rasters/cache files out of Git. Their existing known-ID API can reload them
without transport or writes. The accepted target cache arrays/manifest hashes
remain byte-identical. Full safe per-scene data and the representation mismatch
are recorded in validation §5. No AS-104 output has been produced. Do not lower
minimum five, change dates/masks, add scenes, mix baselines or patch provenance
in memory to obtain a result. Review the target platform comparison first.
No AS-105+, P1 study, commit/push/PR or new scientific decision.

## Historical platform consistency fix and cached real acceptance — M24–M25 / EV-028–EV-029

The earlier M23 handoff above is preserved as the blocked checkpoint. The
case-only fix and cache-only acceptance are now PASS; owner review is next.
Use known cache IDs and unchanged AS-103 reconstruction if reproducing this
experiment. Do not redownload imagery or relax the frozen scientific contract.
The fix's pre-state patch/inventory are
`/workspace/as104-before-platform-case-fix.patch` and
`/workspace/as104-before-platform-case-fix-sha256.json`.
Both safety stashes remain untouched. See the current header and validation
§§6–7 for exact IDs, temporal support, lineage and independent checks.
No AS-104 commit/push/PR/merge; no AS-105+ or P1 05.10 work.

## Historical AS-104 publication handoff — M26 / E26 / EV-030 (before PR #12 merge)

Feature implementation/evidence commit `09b38bd9c312470e948b1f17165ec5335cfc149d`
is published on `origin/feature/as-104-temporal-baseline` from parent/base
`2006df7a70a4f48c66933aed96f4464d8d03084e`. Exactly fifteen paths were committed;
663 tests/Ruff/diff PASS before commit. Feature publication verified local/remote
equality and a clean worktree. This later reconciliation is documentation only.
Review the published commit and open a PR if review passes and creation is
authorized. PR NOT YET CREATED; merge NOT YET PERFORMED. Both stashes and recovery
artifacts retained. AS-105+ and P1 05.10 NOT STARTED. Earlier stop states above
remain historical, not instructions to recommit the implementation.

## Historical AS-104 merged closeout handoff — M27 / E27 / EV-031

AS-104: **COMPLETE AND MERGED** through PR #12; real acceptance **PASS**.
Implementation merge commit: `472edc737847dc8581290a372c5da28f71fc48f0`.
Feature implementation: `09b38bd9c312470e948b1f17165ec5335cfc149d`; final head / publication docs:
`703af1176aeaf9ba38d31c53648907c3b1792aec`. Merge time: **2026-10-09T13:26:08+04:00 Asia/Dubai**
(**2026-10-09T09:26:08Z**), separately from acceptance and feature publication.
Current active development branch: none; this closeout was prepared on
`docs/as-104-closeout`. No unresolved AS-104 P0 blocker; known limitations remain.
Reproducible temporal spectral anomaly / baseline-relative comparisons over
BOA-derived features are supported. This does not establish HAB detection, bloom
confirmation, chlorophyll concentration, species, toxins, water safety, intake
risk, persistence, alerts or warning lead time. L2A BOA is not aquatic Rrs.
Five historical observations are not statistical sufficiency; approximately 10%
five-history support remains a documented limitation, not a failure or reason to
relax support. Small positive scales can produce large robust-z magnitudes.
Rank is not probability, confidence or severity.

Owner review of the next milestone/AS-105 design before implementation is next;
separate authorization required. Both safety stashes and all external recovery
artifacts are retained historical recovery material. No Decision 050, EO rerun,
AS-105+ or P1 05.10 experiment. M23–M26 historical bodies remain preserved.
