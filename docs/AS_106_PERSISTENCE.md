# AS-106 — Persistence: Frozen Design

## Current AS-106 M32 metadata inventory — 10 October 2026 (Asia/Dubai)

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
See [M31 validation](evidence/AS_106_PERSISTENCE_VALIDATION.md); the original scientific specification below remains frozen.

Earlier dated design-freeze/publication/merge checkpoints below are historical;
their old implementation/authorization states do not describe current M31.

## Historical owner-approved design freeze specification

**Date:** 10 October 2026 (Asia/Dubai).
**Status:** OWNER-APPROVED / DESIGN FROZEN ONLY — Decision 051.
**Implementation:** NOT STARTED. No source, tests or implementation validation
evidence exists for AS-106. This document is a specification, not execution evidence.
**Verified design base main:** `b1b5147d9973d8cf23d575985319bf94a55a03d4`
(PR #15 AS-105 documentation closeout). Prepared on `docs/as-106-design-freeze`.
AS-105 remains COMPLETE AND MERGED; Decision 050 is unchanged.

## Task, goal and inputs

PRD AS-106 is P0: track anomaly recurrence over consecutive valid observations.
Consume a chronological collection of frozen AS-105 HABAnomalyGeometryScene
products and their immediate TemporalFeatureScene integrity witnesses. Produce
deterministic observed recurrence evidence, separate from AS-105 geometry,
AS-107 risk/confidence and AS-108 historical-event validation.

No retrieval, optical/spectral/temporal extraction, threshold tuning or family-
voting implementation belongs in persistence computation. Decision 051 in
[the decision log](DECISIONS.md#decision-051--as-106-causal-consecutive-valid-observation-recurrence)
is authoritative; this specification expands its auditable output/acceptance plan.

## Frozen pixel semantics

For each observation P is candidate_analysis_support_mask and C is candidate_mask.
Require C contained in P through the existing full AS-105 validator.

| Target/prior condition | Meaning / action |
|---|---|
| Target P=false | Unevaluable; count storage zero does not mean absence |
| Target P=true, C=false | Current candidate streak zero |
| Target C=true | Start at one and inspect earlier observations backwards |
| Prior P=false | UNKNOWN: skip, neither increment nor break |
| Prior P=true, C=true | Increment current streak |
| Prior P=true, C=false | Break current streak; older candidates cannot reconnect |

Recurrent candidate = target C AND current_streak_count >=2. This definition
does not assign a risk threshold. A target candidate with no prior valid history
has streak one and unevaluable recurrence, not established nonrecurrence.
Invalid/cloud-obscured observations are unknown, not candidate absence.

## Evaluability and denominators

n_prior counts all earlier P=true observations at each target-P pixel, not just
observations within the current streak. Outside target P counts are zero.

| Symbol / output | Frozen definition |
|---|---|
| Q / persistence_evaluable_mask | target P AND n_prior >=1 |
| A | Target candidate pixels |
| B | Target C AND Q |
| C (global numerator set) | Recurrent target candidates |
| candidate_history_coverage | count(B)/count(A) |
| recurrence_fraction | count(C)/count(B) |

None for zero denominator; 0.0 for zero numerator/nonempty denominator. No AOI,
target-water or full AS-105 P denominator substitution. A false recurrence mask
without Q must not be interpreted as established absence of recurrence.

## Exact space and observation time

Identical AnalysisGrid and exact pixel coordinates only. No dilation, buffer,
morphology, neighbourhood/adjacent/diagonal matching, IoU matching, displacement,
advection/current/wind compensation, gap filling, reprojection or resampling.
Adjacent/diagonal candidate movement does not count; disclose this limitation.

No arbitrary calendar-gap cutoff. Normalize aware timestamps to UTC and compute
integer microseconds using timedelta days/seconds/microseconds, not floating-
point timestamps. Freeze int64 previous_valid_observation_gap_us and
current_streak_span_us, with -1 missing sentinel:

- Previous-valid gap: target time minus most recent earlier P=true time; -1 when
  absent or outside target P, whether the earlier valid observation was candidate
  or non-candidate.
- Current span: target time minus oldest candidate in the current valid streak;
  zero for singleton target candidates, -1 outside target C.

Skipped observations can lie within the span. Seconds/days are derived display
units only; neither span nor gap proves continuous biological presence/duration.

## API, sequence and integrity

Expected public API:
`compute_hab_persistence(geometry_scenes, *, temporal_parents, target_geometry_product_id)`.
Use a mapping from temporal product ID to typed temporal witness. Witnesses are
validation inputs, not semantic immediate provenance sources.

Normalize times to UTC; canonicalize chronological caller ordering. Require
unique product IDs and normalized acquisition timestamps, explicit latest target,
same grid, as105-v1 and identical frozen Decision 050 policy. Reject duplicates,
missing target, future input, target not latest, mismatches and malformed inputs.
Do not silently exclude future scenes or reproject incompatible scenes.

Require a common temporal comparison context: AS-104 version, AS-103 feature/
formulas, ordered reference IDs/times, reference period, minimum_observations,
grid/AOI, provider/collection, relevant tile/orbit and delivered processing baseline.
This must not be inferred from arbitrary product-ID string equality alone.

For every scene call `scene.validate(temporal_parent)`. The owner explicitly
permits that validator's internal AS-105 regeneration as **INTEGRITY VERIFICATION**.
No weakened validator or duplicated scientific voting logic. Do not call optical
extraction, spectral extraction, AS-104 compute_temporal_anomaly or AS-105
extract_hab_anomaly_geometry during persistence computation. Existing validator
regeneration is the deliberate exception, not new-date extraction or tuning.

Parent arrays/dictionaries remain unchanged. Work from defensive consumed-data
copies; returned arrays/metadata must not alias parents. A single target/no
prior history may produce an honest unevaluable diagnostic result, never a
multi-date recurrence claim. Guard uint32 count capacity before arithmetic.

## Expected typed output and region evidence

Model name: HABPersistenceScene.

| Field group | Expected contract |
|---|---|
| Identity | grid; ordered geometry IDs/times; target geometry ID/acquisition |
| Counts | prior_valid_observation_count and current_streak_count: uint32 |
| Support | persistence_evaluable_mask and recurrent_candidate_mask: bool |
| Timing | previous_valid_observation_gap_us and current_streak_span_us: int64 |
| Audit support | Defensive target P/C; unchanged target region IDs/labels as needed |
| Regions | Typed region summaries and chronological prior support/overlap records |
| Diagnostics | A/B/C counts, defined fractions, no-history count, declared-denominator streak histogram |
| Metadata | processing_parameters, product_id, consumed-input/output fingerprints, DerivedProductRecord |

No 0–1 persistence score, risk score or confidence score. Fractions describe
counts with named denominators, not confidence/probability/severity.

Use unchanged target regions/labels. No cross-date region rematching or geometry
modification/deletion, including zero or unknown recurrence. Per region record
pixel count, B count/history coverage, recurrent count and recurrent/B fraction;
maximum/median streak on B; maximum/median observed recurrence span on recurrent
pixels; and, for every prior date, supported region count, candidate-overlap
count and overlap/support fraction. Use None for empty supports. Timing median
must preserve exact half-microsecond values where needed, using integer
numerator/denominator rather than truncation. Region summary results must be
independently reproducible from target labels and sequence masks/times.

## Identity, byte conventions and output integrity

Freeze as106-v1; product_type hab_persistence; product prefix hab_persistence:;
input format as106-input-v1; output format as106-output-v1.

Product identity includes ordered AS-105 parent IDs/acquisition times, explicit
target, exact grid, >=2 recurrence definition, UNKNOWN-skip/valid-noncandidate-
break rules, exact-pixel semantics, no calendar cutoff, common comparison
context, denominator/dtype policies and relevant software versions. Canonical
JSON/SHA-256 produce deterministic identity. created_at is excluded.

Consumed input content is exactly:

- Every date: normalized UTC acquisition timestamp and common grid identity.
- Target: full P, full C, target component labels/region identity needed by summaries.
- Prior: P where target P is true; C where target C AND prior P are true, including
  all dates required for chronological regional overlap evidence.

Do not consume unnecessary family-vote rasters, spectral values, robust z,
centre/scale, unrelated pixels or prior labels. AS-105 IDs independently remain
lineage identity inputs: a parent-ID change can change product identity even
when the consumed-mask fingerprint is unchanged.

Follow existing framed serialization: canonical JSON header including payload
byte count; eight-byte big-endian header length; header then payload; C-order
bytes. Masks uint8; counts little-endian <u4; timing <i8; target labels <i4.
Output fingerprint covers every scientific output array and typed summary,
separate from semantic identity. Regenerate results from fully validated parents
to reject tampering even if an attacker recomputes the output fingerprint.

## Predeclared real April selection — future, not executed

Intended acquisition interval is inclusive
`[2023-04-01T00:00:00Z, 2023-04-28T06:46:29.024000Z]`.
Select every eligible observation BEFORE anomaly outputs are inspected:

- Configured Al Raha AOI, exact accepted EPSG:32640 20 m AnalysisGrid.
- Existing metadata cloud gate <=30%, tile 40RBN, relative orbit 20.
- Both Sentinel-2A/B permitted; strict acquisition/platform/tile/orbit provider match.
- Exactly one matching PC 05.09 product; required assets; unchanged upstream contracts.
- Metadata ambiguity resolved before scientific output; deterministic complete inventory.

No anomaly-dependent inclusion/exclusion. Do not remove sparse-support, zero-
candidate or inconvenient results. An eligible preparation failure is a reported
blocker, not permission to silently omit that date or weaken upstream constraints.

Use the fixed accepted March reference period `[2023-03-01, 2023-04-01)`,
minimum_observations=5 and the same accepted AS-103 references:

| Acquisition UTC | Accepted spectral product ID |
|---|---|
| 2023-03-04T06:47:51.024Z | spectral:6409add4aef5c95cfe773bfabfa1f554bdda2968241712bda4debefa34b57130 |
| 2023-03-09T06:47:19.025Z | spectral:dafde3d3a2a94d44b62a9d5605bce497b03021e517b7dd6b081607719f37efa1 |
| 2023-03-14T06:46:41.024Z | spectral:721d847a7ed032426c8124e42507b60c3f9a6ae86a4e9ad406176646c35abff7 |
| 2023-03-24T06:46:21.024Z | spectral:1002b083b3d7637abd67446ef171e0746fe3bd839706cadff18571ac1c51af66 |
| 2023-03-29T06:46:29.024Z | spectral:c4de2a86bb7b15a6a8bc49373823bb944be7e6787db383b0959c93c51f3464d5 |

Each April AS-104 computation is target-specific because valid support differs;
there is no universal precomputed baseline raster for every April target. Reuse
accepted April 28 AS-104/105 products through verified reconstruction, not a new
extraction. Witness validation remains required at future consumption.

## Known real-data prerequisite gap

Local accepted caches exist for March 4/9/14/24/29 and April 28 only. No verified
earlier-April cache exists; exact eligible earlier-April inventory remains unknown.
The historical 44-candidate AS-101 count is not a preserved complete April inventory.
Real acceptance is **BLOCKED ON FUTURE DATA PREPARATION**, not on an offline
AS-106 algorithm issue. Offline implementation is not yet started or authorized
by this document. Metadata inventory, imagery/preprocessing expansion and real
acceptance are separately gated.

Read-only accepted prerequisites remain external, not tracked or modified:
`/workspace/aquasentinel-handoffs/as104/` and
`/workspace/aquasentinel-acceptance/as105/m29/`. AS-104 handoff includes reference
descriptors, not full March spectral rasters. Future authorized preparation can
recreate those features offline from verified caches and check accepted identities.

## Staged milestone plan — all NOT STARTED

| Reserved checkpoint | Future scope / authorization boundary |
|---|---|
| M31 / E31 / EV-035 | Offline implementation + synthetic/adversarial validation; separate implementation authorization |
| M32 / E32 / EV-036 | Metadata-only April acquisition inventory; network metadata only, NO imagery download |
| M33 / E33 / EV-037 | Separately authorized missing April AS-102→AS-103→AS-104→AS-105 preparation/handoffs |
| M34 / E34 / EV-038 | Offline real AS-106 engineering acceptance from verified sequence/witnesses |
| M35 / E35 / EV-039 | Owner review / publication / merge / closeout |

These are reservations, not completed milestone/evidence entries. No implementation
validation evidence document or scientific acceptance result is created now.

## Planned implementation acceptance tests

Synthetic/adversarial gates must cover singleton/no prior support; repeated
candidates; invalid skips; noncandidate breaks; unsupported/noncandidate target;
streak three; multiple unknown gaps; exact/adjacent/diagonal pixels; empty/partial
coverage and recurrence; regional denominators; long and subsecond gaps; duplicate/
future/missing/naive-time input; grid/policy/version/comparison mismatches;
canonical ordering/repeat; parent immutability/output non-aliasing; consumed P/C
mutation and unconsumed invariance; endian/layout conventions; created_at exclusion;
output and rehashed-output tampering; AS-105-only lineage; direct summary reproduction;
None/zero semantics; uint32 safety; and no IO/cache/upstream extraction. Explicitly
allow existing AS-105 integrity regeneration and test that validation is not bypassed.
No new tests are written in this documentation task.

## Scientific boundary, dependencies and non-goals

Permitted evidence: observed multi-observation candidate recurrence, candidate
history coverage, satellite observation gaps and exact-pixel streaks. Not established:
continuous biological persistence, HAB/bloom confirmation, bloom duration,
chlorophyll concentration, species/toxins, causation, sensitivity/specificity/
accuracy/false-positive rate, risk/confidence, exposure, water safety, alerts or
warning lead time. Shared March references are not independent confirmation.
Five histories, sparse support, coarse empirical ranks and Decision 050's lack
of comparative scientific validation remain explicit limitations.

Dependencies expected NONE; existing NumPy and standard library suffice.
No upstream source/test/config/dependency/provenance/cache-format changes.
No spatial motion tracking, EO retrieval in the persistence API, AS-107+, historical-
event validation, AS-105 policy tuning/comparison or P1 05.10 experiment.

## Design-freeze validation and next action

Documentation-only gate: full pytest, Ruff, git diff --check and protected-file/
artifact preservation; expected retained baseline 803 tests and six existing
Rasterio warnings. These checks do not execute real EO acceptance or validate
AS-106 software that does not exist yet. No PR or merge in this task.
Owner review of the published design documentation, followed by explicit M31
implementation authorization, is next. M32–M35 require their separate staged gates.

## M31 implemented contract and execution plan — offline only

**Task/goal:** Implement frozen Decision 051 as deterministic recurrence evidence.
**Inputs:** Fully validated synthetic AS-105 geometry scenes and temporal witnesses.
**Outputs:** HABPersistenceScene, six primary evidence rasters plus defensive
P/C/label copies, typed global/region/prior-date summaries, DerivedProductRecord.
**Files:** Three persistence source files, six persistence test files, this plan,
M31 evidence and five continuity documents; exactly sixteen authorized paths.
**Dependencies:** NONE; existing NumPy and standard library.
**Acceptance:** Frozen recurrence/denominator/timing/context/lineage semantics,
strict whole-parent validation, no IO/upstream extraction, deterministic identity,
non-aliasing and regenerated tamper rejection; synthetic/adversarial suite PASS.
**Risks/guardrails:** UNKNOWN is not absence, observed span is not biology; no real
April execution, motion matching, policy tuning, probability/risk or accuracy claims.
**Validation:** 190 focused / 993 full tests PASS, Ruff/diff/whitespace PASS,
protected-file hash/mode checks PASS; six existing full-suite warnings only.
**Non-goals:** M32–M35, real EO/network/download, AS-107+, AS-105 policy validation, P1 05.10.

Public API now implements the expected frozen signature. `HABPersistenceScene`
retains defensive target P/C/labels. `PersistenceStatistics`,
`PersistenceRegionSummary`, `PriorRegionEvidence` and `ExactMicroseconds`
expose typed counts/fractions, regional history/recurrence, chronological overlap
records and exact median duration numerator/denominator (1 or 2). Streak maxima/
medians use B; span maxima/medians use recurrent pixels. Histogram is on A.

Common temporal context projects validated AS-104 identity version/feature order/
formulas/references/times/window/minimum/grid/algorithm and the structured upstream
contract (including AOI/catalog/collection/decoding) plus tile/orbit/baseline.
Target-specific IDs, acquisition/generation times and platform may differ; both
Sentinel-2 platforms remain permitted. The full validator checks every descriptor.

Total observation capacity is checked as well as prior-count capacity: a target-
inclusive streak must fit uint32. Exact timedelta arithmetic is checked before
int64 storage. Hashing preserves C-order/endian conventions; temporal witnesses
are validated but excluded from immediate AS-106 provenance.

See [M31 engineering evidence](evidence/AS_106_PERSISTENCE_VALIDATION.md) for test
coverage and the clearly labelled synthetic product. No real acceptance was run.
Owner feature review is next; M32–M35 remain NOT STARTED / separately authorized.

## M32 executed metadata inventory — separate from frozen design

Goal: freeze every eligible April acquisition without imagery/scientific processing.
Inputs: unchanged Al Raha geometry, exact owner-approved interval, CDSE cloud
<=30%, frozen CDSE/PC collections and strict observation identity, exact PC 05.09,
required AS-102 keys. Outputs: normalized JSON/deterministic digest, human-readable
evidence, current continuity and M32/E32/EV-036 entries; eight authorized docs paths.
Dependencies: none. External temporary audit code only; no production helper.

Acceptance: all pages consumed; every returned CDSE record disposed; all eligible
PC identities unique at 05.09; accepted target reconciled; stage audit after
selection; zero asset requests/imagery/science; protected artifacts/history
unchanged; 993 tests, Ruff, whitespace and credential gates PASS. These were met.
Sequence: April 3, April 28; digest `570792066c1997b9a403249d994c4e7367bf2f1dafc6473b6e30df20cd6481d5`. Full counts, query parameters,
exclusions and existing-stage evidence are in
[M32 record](evidence/AS_106_APRIL_METADATA_INVENTORY.md) and
[JSON](evidence/AS_106_APRIL_METADATA_INVENTORY.json).

April 3 requires separately authorized AS-102→103→104→105 preparation; April 28
is already complete through accepted evidence. Metadata compatibility/key presence
does not prove asset/XML/pixel usability; preserve frozen contracts and report any
preparation failure instead of dropping dates. M33–M35 NOT STARTED; real AS-106
acceptance NOT RUN; AS-107+/P1 05.10 NOT STARTED; future policy validation NOT RUN.
No recurrence/scientific output, raster/cache modification, Decision 052, PR or
merge is part of M32. The earlier design/M31 body remains historical and unchanged.
