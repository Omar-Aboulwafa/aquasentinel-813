# AquaSentinel 813 — Architecture & Product Decisions

## Current AS-107 M40 publication / closeout preparation — 10 October 2026 (Asia/Dubai)

**AS-107: CLOSEOUT READY. M40 / E40 / EV-044: PUBLICATION / CLOSEOUT PASS — READY FOR PR.**
This is the pre-merge closeout preparation state, not a claim that AS-107 is
already COMPLETE / CLOSED. **The future closeout PR merge itself is the durable
closure event:** after that merge, AS-107 is **COMPLETE / CLOSED** and M40 is
**COMPLETE / MERGED / PUBLICATION-CLOSEOUT**. No extra documentation loop or
invented future merge SHA is required merely to record that event.

Verified implementation/acceptance baseline: `2bfbbd63cb5fee8e1d18a0b1099335b924e5ed9d`.
AS-106: COMPLETE / CLOSED. Decision 052 / M37: FINAL / FROZEN / MERGED via
PR #22 (`49f5276b1ad372725b21cdb2085815225c98eed4`). M38: IMPLEMENTED /
SYNTHETIC-ADVERSARIAL VALIDATION COMPLETE / MERGED via PR #23
(`7f304bb44af93d2b3a1a3e6982fefad05fb8f452`). M39: REAL ENGINEERING
ACCEPTANCE PASS / MERGED via PR #24 (`2bfbbd63cb5fee8e1d18a0b1099335b924e5ed9d`).
Actual Git parents, ancestor relationships and merge/head tree equality were
verified, rather than inferred from these status statements.

Current active development branch: none. This closeout was prepared on
`docs/as-107-closeout`, in `/workspace/aquasentinel-813-as107-m40`, directly from
that verified main. Immediate next step: owner review of the published M40
closeout; PR creation and merge need separate authorization. No M40 PR or merge
was performed in this task. AS-108 NOT STARTED; future AS-105 policy validation
NOT STARTED; P1 homogeneous 05.10 robustness NOT STARTED. Decision 053 ABSENT.

Accepted as107-v1 product: `hab_risk:113143700cb35ac9230d9c54b68b1b53e2573838a4913d4bc942e81c99903fdb`.
Input fingerprint: `084790273118f50f6c8eaf0ed380dbce730c6dbbd7e4fa0f757c5d145e894d91`.
Output fingerprint: `25cccf8e8b550a76f28ebb01a2249060de5b1cd3114a7c531ef4775adbc87dae`.
**Watch = 29.52380952380953**, evidence completeness **0.7**, component coverage
**0.7**, assessment `provisional_observational_screening`; recommendation:
**Review on the next valid acquisition**. Seven pixels / 2,800 m²; spectral
14/35 = 40.0; red-edge family evidence breadth 7/21 = 33.333333333333336;
available persistence A/B/C = 7/7/0; C/B = 0/7 = 0.0; context/exposure unavailable.
No same-pixel candidate recurrence was observed among the 7 target candidate
pixels with valid prior observational history. This does not establish no HAB,
no biological persistence, safe water or zero environmental risk.

M40 publishes existing accepted evidence without recomputing real scoring or
upstream science. Decision 050/051/052 bodies and M39 MD/JSON remain byte-identical;
sealed bundles, caches, handoffs, recovery files, modes and both safety stashes
are retained. M40 engineering quality: **1285 full tests PASS (104.18s), six existing Rasterio PendingDeprecationWarnings; Ruff/diff/new-file whitespace/credential/preservation PASS**. Local checks only;
no GitHub CI success claim. Scientific/external-data requests and EO bytes: **0**.

Policy was frozen before real scoring; no outcome tuning followed Watch. Missing
operational components were not fabricated. This is not HAB/absence confirmation,
measured chlorophyll, species/toxins, probability/calibrated confidence, water safety,
shutdown advice, complete intake risk, accuracy or lead-time validation. Exact-grid
recurrence, no motion compensation, the 25-day + 8-second gap, sparse/shared five-history
support, BOA rather than aquatic Rrs, correlated red-edge evidence and candidate-conditioned
maximum remain limitations. Al Raha is a validation AOI, not a confirmed intake.

See [M40 closeout](evidence/AS_107_CLOSEOUT.md) and [machine-readable closeout](evidence/AS_107_CLOSEOUT.json).
All earlier dated current-status and M36–M39 records below describe historical
checkpoints; their original unstarted/unpublished/unmerged wording is retained.

## Historical AS-107 M39 real engineering acceptance — before PR #24 merge — 10 October 2026 (Asia/Dubai)

**AS-106: COMPLETE / CLOSED. Decision 052 / M37: FINAL / FROZEN / MERGED.
M38: IMPLEMENTED / SYNTHETIC-ADVERSARIAL VALIDATION COMPLETE / MERGED** through
PR #23 at `7f304bb44af93d2b3a1a3e6982fefad05fb8f452`, with parents
`49f5276b1ad372725b21cdb2085815225c98eed4` and
`55533467393f394d6cb3f856b439f41fde4b0148`.
**M39 / E39 / EV-043: REAL ENGINEERING ACCEPTANCE PASS.** First real computation
used unchanged accepted April 3/28 typed parents, offline, under the pre-score
frozen policy. Exactly three public AS-107 calls; no public upstream rerun.

Under the frozen AS-107 observational screening policy, the April 28 validation AOI produced a **Watch observational screening score of 29.52380952380953**, with evidence completeness **0.7** and component coverage **0.7**. Environmental context and intake exposure remain unavailable. The result is provisional observational screening, not confirmed HAB or operational water-safety determination.

Accepted product: `hab_risk:113143700cb35ac9230d9c54b68b1b53e2573838a4913d4bc942e81c99903fdb`.
Input fingerprint: `084790273118f50f6c8eaf0ed380dbce730c6dbbd7e4fa0f757c5d145e894d91`.
Output fingerprint: `25cccf8e8b550a76f28ebb01a2249060de5b1cd3114a7c531ef4775adbc87dae`.
The sole seven-pixel / 2,800 m² authoritative region has family a=(7,7,7,7,7),
v=(0,7,0,7,0); spectral 14/35 → 40.0; red-edge 7/21 → 33.333333333333336;
persistence A/B/C=7/7/0 → 0.0. F_all=F_red=H=1.0; completeness is capped by
K=0.7, not a biological probability. Flag: incomplete_evidence. Recommendation:
**Review on the next valid acquisition**. No same-pixel candidate recurrence was
observed among the 7 target candidate pixels with valid prior observational history;
this proves neither no HAB nor safe water nor zero biological persistence/risk.

Independent integer/binary64 arithmetic, fingerprints/identity, same/reversed-order
repeats, creation-time exclusion, full parent-aware validation, 13 ordinary plus
3 attacker-rehashed tamper rejections, immutability/non-aliasing and sealed fresh
process roundtrip: PASS. Scientific network/metadata/assets/EO bytes: 0.
Decisions 050/051/052, production source/tests/config/dependencies, accepted upstream
evidence, 41 protected external hashes, 53 modes and both safety stashes preserved.
Final M39 engineering quality gate: **292 focused tests PASS (43.61s); 1285 full tests PASS (103.96s), six existing Rasterio PendingDeprecationWarnings; Ruff/diff/credential/preservation PASS.** Local engineering checks, no GitHub CI-success claim.

Evidence prepared on `data/as-107-real-acceptance`, worktree
`/workspace/aquasentinel-813-as107-m39`, directly from verified PR #23 main.
Authorized evidence commit/push is for owner review; no PR or merge in M39.
Next: owner review of published M39 evidence; PR creation and M40 closeout require
separate authorization. **M40 and AS-108 NOT STARTED**; future AS-105 policy
validation NOT RUN; P1 homogeneous 05.10 robustness NOT STARTED. No Decision 053.
Weights/bands/candidate/recurrence policy were not adjusted after seeing the outcome.
No biological calibration/accuracy, species/toxins, measured chlorophyll, probability,
calibrated confidence, water safety, intake shutdown, complete operational risk or
lead-time claim. BOA is not aquatic Rrs; correlated red-edge emphasis, sparse/shared
five-history support, long two-date gap and candidate-conditioned maximum remain
limitations. Al Raha is an analyst-defined validation AOI, not a confirmed intake.

See [M39 evidence](evidence/AS_107_REAL_ACCEPTANCE.md) and
[machine-readable audit](evidence/AS_107_REAL_ACCEPTANCE.json).
All earlier dated M36–M38/current-status sections below are historical checkpoints;
their absent-score/unstarted/unmerged wording describes their original time.

## Historical AS-107 M38 offline implementation — before PR #23 merge — 10 October 2026 (Asia/Dubai)

**AS-106: COMPLETE / CLOSED. Decision 052 / M37: FINAL / FROZEN / MERGED** via
PR #22, implementation base `49f5276b1ad372725b21cdb2085815225c98eed4`.
**M38 / E38 / EV-042: IMPLEMENTED / SYNTHETIC-ADVERSARIAL VALIDATION PASS.**
AS-107 implements the frozen explainable availability-aware observational
screening-risk policy and passes synthetic/adversarial engineering validation.
No real HAB risk score or band exists; no accepted real parents were loaded/scored.
Current active development branch: `feature/as-107-hab-risk`; worktree
`/workspace/aquasentinel-813-as107-m38`. Implementation publication is on this
feature branch, not merged into main. Owner-authorized commit/push is for review;
no PR created and no merge performed by M38. Next: owner review of the published
implementation. M39 real acceptance and M40 closeout require separate authorization.
M39/M40 and AS-108 NOT STARTED; future AS-105 policy validation NOT RUN;
P1 homogeneous 05.10 robustness NOT STARTED.

Actual M38 quality: **292 focused risk tests PASS (44.93s);
1285 full tests PASS (117.57s), six existing Rasterio warnings;
Ruff/diff/security/preservation PASS.** Engineering evidence only, not real/biological
validation. Zero dependency/config/upstream changes; Decisions 050/051/052 unchanged.
See [M38 evidence](evidence/AS_107_IMPLEMENTATION_VALIDATION.md).
All earlier dated M36/M37/current-status sections below are historical checkpoints;
their unimplemented/unstarted wording does not describe current M38.

## Historical AS-107 M37 design freeze — before PR #22 merge — 10 October 2026 (Asia/Dubai)

**AS-106: COMPLETE / CLOSED** through PR #21 merge
`6b22d32f078ef80158b2f2d7aac4f3dd07925038` (official design baseline).
**M36 / E36 / EV-040:** prior read-only feasibility/design audit COMPLETE.
**Decision 052 / M37 / E37 / EV-041: FINAL / FROZEN DESIGN — NOT IMPLEMENTED.**
The primary quantity is evidence_completeness; all current scored outputs must be
qualified as provisional_observational_screening. Policy is frozen before any
real AS-107 score; environmental context/intake exposure remain unavailable.
No production implementation, real score, scientific product or AS-108 work.

Current active development branch: none. Design prepared on
`docs/as-107-design-freeze`. Next: owner review and separately authorized design
PR/merge, then separate M38 implementation authorization. M38–M40 NOT STARTED;
AS-108 NOT STARTED; future AS-105 policy validation NOT RUN; P1 05.10 NOT STARTED.
No PR/merge in M37. Decisions 050/051 and accepted evidence remain unchanged.

See [frozen contract](AS_107_HAB_RISK.md), Decision 052 and
[M36/M37 evidence](evidence/AS_107_DESIGN_FREEZE.md). Existing dated checkpoints
below remain historical, including pre-PR #21 pending-closeout/no-052 statements.

## Historical AS-106 M35 publication / closeout preparation — before PR #21 merge — 10 October 2026 (Asia/Dubai)

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

The original planning/dated execution records below retain their then-current
stop-state instructions unchanged. Their uncommitted/no-push language is historical.

**Last updated:** 2 October 2026
**Status:** Active decision log
**Repository:** `Omar-Aboulwafa/aquasentinel-813`

This document records important project decisions and the reasoning behind them so that future ChatGPT sessions, Codex tasks, developers, or collaborators can continue the project without relying on conversation history.

---

## Decision 001 — Choose Track 03: Water Security & Marine Environments

### Decision

AquaSentinel 813 will compete under:

**Track 03 — Water Security & Marine Environments**

### Why

The track offers a strong intersection of:

- real UAE/Gulf operational relevance,
- Earth-observation suitability,
- hyperspectral relevance,
- clear public-sector / utility users,
- measurable operational impact,
- commercial potential beyond the hackathon.

Marine threats can directly affect desalination infrastructure, making the problem operational rather than purely academic.

### Consequence

The PoC is designed around seawater-intake monitoring and early-warning intelligence.

---

## Decision 002 — Focus on Desalination Intake Intelligence

### Decision

The primary product user is:

**Desalination Plant Water Quality / Operations Manager**

The primary decision supported is:

> Where and when should monitoring or field verification be prioritized?

### Why

A narrowly defined operational user is stronger than building a generic “marine monitoring platform.”

The product must support a real decision, not merely visualize satellite data.

### Consequence

AquaSentinel outputs must be translated into:

- risk level,
- evidence,
- confidence,
- exposure,
- monitoring priority,
- recommended verification.

---

## Decision 003 — Product Positioning Is Early-Warning Intelligence, Not Detection Alone

### Decision

AquaSentinel is not positioned as:

> an AI algae detector

or:

> an oil-spill map

It is positioned as:

> an explainable marine-intake early-warning and monitoring-prioritization system.

### Why

Detection alone does not create sufficient operational value.

The stronger product chain is:

Observation
→ Detection
→ Explanation
→ Exposure
→ Risk
→ Monitoring Priority
→ Human Decision

### Consequence

Every hazard module must eventually connect to an operational monitoring decision.

---

## Decision 004 — Adopt a Multi-Hazard Product Vision

### Decision

The long-term product vision is multi-hazard marine-intake intelligence.

The PoC includes:

- HAB / biological anomaly as the primary hazard.
- Oil-slick candidate detection as the secondary hazard.

### Why

A desalination operator cares about any offshore event that could affect intake conditions, not only one environmental phenomenon.

Recent Gulf-region events demonstrate that both biological anomalies and marine pollution are operationally relevant.

### Consequence

The architecture must support multiple independent hazard modules without forcing unrelated hazards into one scientific model.

---

## Decision 005 — HAB Is the Primary PoC Hazard

### Decision

The biological-anomaly / HAB pipeline is the primary and most complete PoC hazard module.

### Why

It provides:

- strong fit with Track 03,
- natural Sentinel-2 use,
- strong hyperspectral relevance,
- clear water-security value,
- historical UAE validation opportunities,
- a strong early-warning narrative.

### Consequence

The HAB pipeline receives implementation priority before advanced oil, environmental, or hyperspectral features.

---

## Decision 006 — Oil Is the Secondary PoC Hazard

### Decision

Oil-slick candidate detection is the second hazard module.

### Why

It demonstrates that AquaSentinel is a platform for intake protection rather than a single-purpose algae product.

Sentinel-1 SAR also provides a technically distinct sensing modality and cloud-independent observation.

### Consequence

The oil module should remain smaller than the HAB module during the PoC.

---

## Decision 007 — Use Sentinel-2 as the Main Biological-Anomaly Sensor

### Decision

Sentinel-2 is the P0 optical data source for HAB-related and biological water-quality anomaly analysis.

### Intended uses

- water colour,
- chlorophyll-related signals,
- red-edge features,
- temporal change,
- spectral anomaly detection.

### Why

Sentinel-2 offers:

- suitable spectral bands,
- strong public availability,
- repeat observations,
- regional coverage,
- compatibility with STAC-based workflows.

### Consequence

AS-101 begins with Sentinel-2 STAC search before any full-image processing.

---

## Decision 008 — Use Sentinel-1 SAR for Oil-Slick Candidates

### Decision

Sentinel-1 is the primary P0 source for oil-slick candidate detection.

### Why

SAR can detect surface roughness changes that may correspond to oil slicks and remains usable through cloud cover.

### Scientific constraint

Low SAR backscatter does **not** uniquely prove petroleum.

Look-alikes can include:

- low-wind areas,
- natural films,
- biological surface films,
- other surface effects.

### Consequence

Product wording must use:

> oil-slick candidate

and include confidence/context rather than claiming confirmed oil.

---

## Decision 009 — Hyperspectral Is P1, Not a P0 Dependency

### Decision

EnMAP / Satellite 813-style hyperspectral analysis is an enhancement layer.

P0 must work without it.

### Why

Hyperspectral data is valuable for:

- detailed spectral characterization,
- increased confidence,
- comparison with multispectral observations.

However, tying the entire PoC to scene availability or restricted data access creates delivery risk.

### Consequence

The baseline must work with Sentinel-2 / Sentinel-1 first.

Hyperspectral work is added only after P0 is stable.

---

## Decision 010 — Do Not Depend on Native Satellite 813 Data for the PoC

### Decision

The PoC architecture must not require direct Satellite 813 imagery to function.

### Why

Access and availability may be limited or staged by the hackathon.

### Consequence

The system must be demonstrable with openly accessible EO sources first.

Satellite 813 can later be positioned as a high-value enhancement.

---

## Decision 011 — Use Explainable Risk Before Complex ML

### Decision

Start with transparent anomaly/risk logic and simple models.

Do not start with deep learning merely for sophistication.

### Why

The PoC must be:

- explainable,
- reproducible,
- defensible to judges,
- implementable before the deadline.

### Consequence

Initial risk scoring may use configurable heuristic weights or simple baseline models.

More advanced ML is permitted only when labels, validation quality, and time justify it.

---

## Decision 012 — Risk Weights Are Hypotheses, Not Scientific Constants

### Decision

Current HAB and oil risk weights are configurable PoC assumptions.

### Why

They have not been scientifically validated as universal operational weights.

### Consequence

The product and documentation must not represent them as validated constants.

Changes to risk weighting should be documented.

---

## Decision 013 — Never Average Unrelated Hazards Into One Scientific Score

### Decision

HAB risk and oil risk remain separately interpretable.

### Why

They are scientifically different phenomena with different evidence and uncertainty.

### Consequence

If an overall site status is needed, it should reflect the highest credible active hazard rather than mathematically averaging unrelated hazard classes.

---

## Decision 014 — Remote Sensing Outputs Are Observational, Not Confirmatory

### Decision

AquaSentinel must use conservative scientific language.

Allowed wording includes:

- HAB-like spectral anomaly,
- elevated biological water-quality risk,
- oil-slick candidate,
- field verification recommended,
- observational risk,
- confidence.

### Prohibited overclaims

Do not claim satellite observations alone have:

- confirmed toxic algae,
- confirmed algal toxin,
- confirmed petroleum composition,
- certified water safe/unsafe,
- justified autonomous plant shutdown.

### Consequence

The product is decision support, not laboratory confirmation.

---

## Decision 015 — Keep Human Verification in the Loop

### Decision

AquaSentinel recommends monitoring and verification actions.

It does not autonomously shut down plant operations.

### Why

Desalination operations are safety-critical and require qualified human decision-making.

### Consequence

The primary action language is:

> prioritize field verification / increase monitoring

rather than:

> stop intake / shut down plant.

---

## Decision 016 — Use Historical Events for Validation

### Decision

The PoC will validate against documented historical events instead of showing only synthetic or random examples.

### Current candidates

Biological anomaly:

**Al Raha Beach / Al Raha Bay, Abu Dhabi — April 2023**

Oil:

**Kharg Island / Persian Gulf — May 2026**

### Why

A known event gives the judges a credible reference point.

### Consequence

The system must clearly distinguish:

- what an external report says happened,
- what the satellite-derived analysis shows.

---

## Decision 017 — Separate Validation AOI From Operational Demo Site

### Decision

The current Al Raha AOI is a validation AOI.

It must not be presented as a desalination intake.

### Why

Scientific validation and operational product demonstration serve different purposes.

### Consequence

A future operational demo AOI/intake zone should be represented separately and clearly labelled.

---

## Decision 018 — Use Analyst-Defined AOIs Transparently

### Decision

The current AOI polygon is an analyst-defined study area, not an official administrative or environmental boundary.

### Consequence

The code and product metadata must preserve this distinction.

---

## Decision 019 — Build Provenance Before Satellite Ingestion

### Decision

Provenance and lineage infrastructure was implemented before connecting to live EO catalogs.

### Why

Once real scenes begin flowing through the system, losing source identity would create technical debt and scientific credibility problems.

### Consequence

Every real EO observation and derived product should integrate with the existing provenance layer.

---

## Decision 020 — Preserve End-to-End Lineage

### Decision

Expected lineage:

Source observation
→ derived feature
→ hazard layer
→ risk product
→ operational alert

### Why

Judges and future customers should be able to trace a result back to its input data and processing version.

### Consequence

Derived data must not silently lose references to upstream sources.

---

## Decision 021 — Use Python 3.11 for the PoC

### Decision

The project uses Python 3.11.

Current environment:

`aquasentinel813`

### Why

Python 3.11 provides strong compatibility with the scientific/geospatial ecosystem required by the project.

The office machine also had newer Python versions, but the project environment was intentionally isolated.

### Consequence

Do not migrate the project to Python 3.13/3.14 during the PoC without a strong reason and explicit approval.

---

## Decision 022 — Use a `src/` Package Layout

### Decision

Application code lives under:

`src/aquasentinel`

### Why

This provides clean package isolation and reduces accidental imports from the project root.

### Consequence

New core modules should normally be added under this package.

---

## Decision 023 — Use TOML for Project Configuration

### Decision

Runtime/project defaults live in:

`config/default.toml`

### Current configurable items include

- AOI path,
- cache directory,
- date range,
- cloud-cover limit,
- risk bands,
- risk weights.

### Why

Operational/scientific parameters should not be buried in source code.

### Consequence

Avoid hard-coding configuration values when they belong in TOML.

---

## Decision 024 — Use GeoJSON for AOI Representation

### Decision

AOIs are stored in GeoJSON.

### Why

GeoJSON is:

- interoperable,
- human-readable,
- easy to map,
- compatible with future geospatial tooling.

### Consequence

Coordinate validation is part of the config/AOI layer.

---

## Decision 025 — Repository Is the Source of Truth

### Decision

Project state must live in GitHub/repository documentation, not in ChatGPT conversation memory.

### Why

The user may:

- change computers,
- start a new ChatGPT conversation,
- start a new Codex task,
- hit a context-window limit,
- involve another developer.

### Consequence

Important project state belongs in:

- `AGENTS.md`,
- `docs/PROJECT_STATE.md`,
- `docs/DECISIONS.md`,
- `docs/HANDOFF.md`,
- `.agent/PLANS.md`,
- code,
- tests,
- Git history.

---

## Decision 026 — Use a Cloud/GitHub-First Multi-Machine Workflow

### Decision

Office PC, personal PC, and Codex/cloud environments should all work from the same GitHub repository.

### Workflow

Before changing machine:

- test,
- lint,
- commit,
- push.

On the destination machine:

- pull,
- recreate/activate environment,
- install dependencies,
- test,
- continue.

### Consequence

Machine-specific state should be minimized.

---

## Decision 027 — Keep Personal GitHub Separate From Company GitHub

### Decision

The office machine uses a dedicated personal SSH alias:

`github.com-omar-personal`

Current personal repo remote:

`git@github.com-omar-personal:Omar-Aboulwafa/aquasentinel-813.git`

### Why

The machine is also connected to company systems.

### Consequence

Do not modify global Git identity or company SSH settings unless explicitly approved.

---

## Decision 028 — Use Feature Branches, Not Direct Development on `main`

### Decision

Each engineering task should use a task-specific branch.

Examples:

- `feature/as-101-sentinel2-stac`
- `feature/as-102-optical-preprocessing`
- `fix/...`
- `docs/...`
- `chore/...`

### Consequence

`main` should remain stable and merge-ready.

---

## Decision 029 — Require Tests and Ruff Before Merge

### Decision

Standard quality gate:

```text
python -m pytest -v
python -m ruff check .
```

### Consequence

Do not merge code with failing tests or lint issues.

---

## Decision 030 — Keep Dependencies Minimal

### Decision

Do not add libraries simply because they may be useful later.

### Before adding a dependency

Confirm:

1. the standard library is insufficient,
2. the dependency is needed for the current task,
3. it is mature and appropriate,
4. it does not unnecessarily duplicate another library.

### Consequence

AS-101 should add only what is required for robust STAC integration.

---

## Decision 031 — STAC Search Comes Before Image Download

### Decision

AS-101 will search/catalog Sentinel-2 observations first.

It will not yet download/process full imagery.

### Why

The correct order is:

catalog discovery
→ deterministic scene selection
→ provenance
→ retrieval
→ preprocessing

### Consequence

AS-101 acceptance criteria should focus on real scene discovery and metadata/provenance.

---

## Decision 032 — Streamlit Is the Preferred PoC UI Direction

### Decision

When the dashboard phase begins, Streamlit is the preferred first implementation unless project needs change.

### Why

It offers a fast route to:

- maps,
- controls,
- charts,
- evidence panels,
- Python-native integration.

### Consequence

Do not spend early PoC time building a complex frontend framework.

---

## Decision 033 — Live APIs Must Not Be the Only Demo Path

### Decision

The final demo should have cached/validated fallback data.

### Why

External EO and environmental services can fail, rate-limit, or require re-authentication.

### Consequence

A live API failure must not make the hackathon demo unusable.

---

## Decision 034 — P0 Reliability Beats P1 Sophistication

### Decision

When time is limited, protect:

1. real EO-derived results,
2. scientific credibility,
3. validation,
4. explainability,
5. provenance,
6. reproducibility,
7. working demo.

before protecting:

- advanced modelling,
- advanced UI,
- hyperspectral extras,
- complex drift simulation,
- visual polish.

### Consequence

P1 features may be cut without changing the core product thesis.

---

## Decision 035 — Codex Is Introduced Before AS-101

### Decision

Codex onboarding/continuity setup occurs before satellite-data engineering begins.

### Why

AS-101 is the point where implementation complexity and file count begin to increase materially.

### Consequence

Before delegating AS-101, the repository must contain enough context for Codex to work without relying on the current ChatGPT conversation.

---

## Decision 036 — First Codex Task Is Read-Only

### Decision

The first Codex task should inspect the repository and summarize its understanding without modifying code.

### Why

This validates that:

- `AGENTS.md` is effective,
- project state is understandable,
- important decisions are recoverable,
- agent assumptions can be corrected before code changes.

### Consequence

AS-101 should only be delegated after the read-only onboarding is reviewed.

---

## Decision 037 — Keep Decision History, Do Not Rewrite It Silently

### Decision

If a major project decision changes, update this file rather than deleting the old rationale without explanation.

### Preferred pattern

Add:

- changed decision,
- date,
- reason,
- impact.

### Why

Architecture history matters for understanding why the current system exists.

---

## Decision 038 — Use Configurable CDSE STAC for AS-101

### Decision

On 2 October 2026, the project owner explicitly selected Copernicus Data Space Ecosystem as the default Sentinel-2 Level-2A catalog for AS-101:

- Endpoint: `https://stac.dataspace.copernicus.eu/v1/`
- Collection: `sentinel-2-l2a`

Both are configurable. `pystac-client==0.9.0` is the only new direct dependency; it provides STAC discovery/search and pagination without introducing raster processing libraries.

### Evidence and consequences

- A real query for the configured Al Raha validation AOI and 1 March–31 May 2023 window returned 44 scenes with cloud cover <= 30%; every candidate converted to valid provenance.
- A configurable 30-second request timeout bounds network waits. No result cap is imposed; all pagination is consumed or an explicit error is raised.
- Missing required metadata fails explicitly. Platform is required because the existing `SourceRecord` requires it; platform values are never invented. Optional self URLs and licence metadata remain absent when unavailable.
- Candidate IDs include a full SHA-256 digest of the catalog endpoint plus escaped collection/item IDs to avoid provider and separator collisions.
- Only metadata and asset references are retrieved. Catalog availability is not evidence of HABs or usable water pixels, and asset accessibility has not been verified.

Reproduction and detailed evidence: `docs/AS_101_STAC_SEARCH.md`.

---

## Decision 039 — Preserve CDSE Discovery; Use Planetary Computer Raster Delivery

**Date:** 6 October 2026. **Status:** Explicitly authorized for AS-102.

### Decision

AS-101 remains the CDSE metadata workflow. AS-102 strictly matches its candidate to Planetary Computer and uses the anonymous STAC / credential-free HREF-signing / native COG path. Do not rewrite AS-101 or fall back to whole products.

### Why and consequence

FG-01 established bounded access where the prior CDSE environment probe was blocked. Match full acquisition timestamp, normalized platform, MGRS tile and relative orbit; reject zero/ambiguous/conflicting matches. Parse the structured CDSE ID when provider-specific fields are absent. PC `s2:mgrs_tile`, `s2:generation_time`, processing baseline and optional SAFE product identity are independently checked. Current PC and CDSE products have different baselines/generation dates; no pixel equivalence is asserted.

---

## Decision 040 — Attribute Pixels to the Actual PC Product

**Date:** 6 October 2026. **Status:** Explicitly authorized for AS-102.

### Decision

The actual PC raster product receives the existing provider-qualified STAC `SourceRecord` pattern. `ResolvedOpticalSource` retains observation/processing identity, unsigned assets, observed native grids/nodata and XML decoding. The preprocessed `DerivedProductRecord.source_ids` contains only this PC source; CDSE is retained as discovery/matching context in parameters.

### Why and consequence

Same acquisition is not the same processed product. Generic source/provenance models and AS-101 remain unchanged. Deterministic processing identity and JSON-only parameters preserve reproducibility without arrays or signing credentials.

---

## Decision 041 — Decode BOA Reflectance from the Delivered Product XML

**Date:** 6 October 2026. **Status:** Explicitly authorized for AS-102.

### Decision

Read bounded `product-metadata` XML and validate baseline, quantification, unique physicalBand/bandId mapping and every required additive offset. Decode `(DN + band_offset) / quantification`; mask source nodata before decoding, output float32, and retain negative/zero/unclipped values. Missing, malformed, duplicate, nonfinite or conflicting metadata fails explicitly.

### Why and consequence

Modern Sentinel-2 processing baselines make DN/10000 unsafe. The observed PC baseline-05.09 XML establishes quantification 10000 and offset -1000 for all nine required bands, including B8A; these values are parsed, not constants copied from CDSE. BOA reflectance is not automatically aquatic remote-sensing reflectance.

---

## Decision 042 — Use One Fixed 20 m Analysis Grid per AOI

**Date:** 6 October 2026. **Status:** Explicitly authorized for AS-102.

### Decision

Transform the configured WGS84 polygon envelope to a configured metric CRS, densify bounds, and snap outward to a stable 20 m lattice. The Al Raha default is EPSG:32640: bounds `[249020,2702860,255220,2707420]`, width 310, height 228, affine `[20,0,249020,0,-20,2707420]`. Polygon membership uses pixel centres.

### Why and consequence

Native 10/20 m bands and scenes from different UTM zones must share a single analysis grid. Read native assets with a bounded four-pixel halo; reflectance uses bilinear, SCL nearest. Bilinear downsampling is not an area average. Cross-CRS synthetic coverage includes EPSG:32639 → EPSG:32640; no per-tile target-grid fallback.

---

## Decision 043 — Conservative SCL and All-Band Water Support

**Date:** 6 October 2026. **Status:** Explicitly authorized for AS-102.

### Decision

Invalid classes are `{0,1,2,3,7,8,9,10,11}` plus unknowns; class 2 retains the provider meaning dark-area pixels. Classes 4/5 are valid non-water, class 6 candidate water. Export separate AOI, valid-data, water, valid-water and interpolation-support masks.

Map SCL to each native reflectance grid and remove invalid/nodata contributors before bilinear reprojection. Erode native water/nodata support by a 3×3 NumPy neighbourhood, bilinearly project the resulting binary support with zero treated as actual invalid support, and require a support value exactly 1 across all nine bands. Do not renormalize bad support away. Final water also requires AOI membership, valid target SCL and finite reflectance in every band.

### Why and consequence

Land/cloud/shadow/nodata interpolation must not manufacture usable water. The extra neighbourhood is deliberately conservative, particularly near shorelines. Report excluded counts and retention. Zero surviving water is valid; no silent mask relaxation. SCL is imperfect coastal/shallow/turbid-water truth, and separate cloud-probability assets remain outside AS-102 P0.

---

## Decision 044 — Add Only NumPy and Rasterio for AS-102

**Date:** 6 October 2026. **Status:** Explicitly authorized for AS-102.

### Decision

Add direct pins `numpy==2.2.6` and `rasterio==1.4.3`, compatible with Python 3.11; retain `pystac-client==0.9.0`. NumPy handles masks/arrays and Rasterio/GDAL handles bounded COG access, CRS transformation and resampling. Standard-library urllib/JSON/ElementTree handles signing and XML.

### Why and consequence

No SciPy, SDK, additional direct HTTP library or overlapping geospatial stack is needed. The validated environment resolves Python 3.11.16, NumPy 2.2.6, Rasterio 1.4.3 and bundled GDAL 3.9.3. Transitive wheel dependencies are not a new direct project stack. The earlier GDAL 3.10.3 access probe remains a separate historical environment/result.

---

## Decision 045 — Keep SAS Material Transient and Stable Cache Evidence Unsigned

**Date:** 6 October 2026. **Status:** Explicitly authorized for AS-102.

### Decision

Use the official configured HREF signing endpoint immediately before access. Permit only exact configured HTTPS asset hosts, validate the signed response points to the same object, reject cross-host metadata redirects, suppress/sanitize Rasterio diagnostics and exception chains, and never persist signed URLs/SAS/credentials. Stable JSON serialization rejects credentialled/query-bearing URLs.

### Why and consequence

Temporary access credentials must not become product identity or presentation evidence. Cache only AOI-sized arrays/masks under `data/cache/as102/<cache_id>/`, with deterministic identity, atomic directory publication, canonical manifest JSON and SHA-256 verification. Corrupt caches fail explicitly. Known-ID reload uses no catalog/signing/XML/raster work; it validates the configured AOI/grid and retains original processing lineage.

---

## Decision 046 — AS-103 Candidate Spectral Features with Signed BOA and Parent Lineage

**Date:** 8 October 2026 (Asia/Dubai). **Status:** Explicitly authorized for AS-103;
implemented on uncommitted feature branch for review.

### Decision

Freeze exactly ndci_like, mci_like, B05/B04, B06/B04, B03/B04 and B03/B02 in the
canonical order defined by the AS-103 contract. Candidate signals only; no event
threshold/classification or temporal baseline. Preserve authoritative AS-102
valid-water support and signed BOA. Float64 arithmetic returns float32; numerical
rejection is inclusive `abs(d) <= max(1e-4,1e-6*(|a|+|b|))`; nonfinite intermediate
or float32 results are masked NaN. Record per-feature diagnostics and finite
JSON-safe summaries, including unclipped NDCI-like out-of-range counts.

Use nominal MCI B04/B05/B06 at 665/705/740 nm with k=1.0 (not SNAP's 1.005),
coefficient 8/15, metadata-declared convention rather than provider XML wavelengths.
BOA is not aquatic Rrs. NDCI-like and B05/red ratio share an evidence family and
must not later be treated as independent biological evidence.

### Why and consequence

Pure NumPy feature extraction from verified AS-102 output is cheap and explainable;
no new dependency, configuration, disk cache, retrieval, signing or resampling is
needed. The AS-103 identity includes canonical formulas/policies/grid/parent and a
versioned fingerprint of the full mask plus five consumed bands on water support,
because frozen dataclasses do not make NumPy arrays immutable. Creation time and
feature summaries do not define identity. Registry lineage is actual PC source →
AS-102 derived product → AS-103 derived product; no raw-source shortcut or generic
schema change. AS-104 remains separately unauthorized and not started.

Contract/references: [AS-103 plan/API](AS_103_SPECTRAL_FEATURES.md).
Observed acceptance: [AS-103 evidence](evidence/AS_103_SPECTRAL_FEATURES_VALIDATION.md).

---

## Decision 047 — AS-104 Causal Per-Pixel Temporal Feature Baselines

**Date:** 8 October 2026 (Asia/Dubai).
**Status:** Explicitly authorized for AS-104.

### Decision

AS-104 is a causal, target-specific, per-feature, per-pixel temporal comparison
over validated AS-103 SpectralFeatureScene objects. For one target observation,
use explicitly bounded strictly-prior observations only. No target self-inclusion.
No future observations. No symmetric before/after baseline in as104-v1.

For every feature/pixel:

- historical centre = median
- MAD = median(abs(history - median))
- scale = 1.4826 * MAD
- signed deviation = target - centre
- standardized anomaly = deviation / scale when scale > 0
- empirical rank uses exact-tie midrank

Minimum history is an explicit API parameter. For P0 real acceptance use
`minimum_observations = 5`. Five is a P0 engineering/scientific starting rule,
not a claim of statistical sufficiency.

Zero MAD:

- centre remains valid
- scale = 0 remains valid
- signed deviation remains valid
- empirical rank remains valid
- standardized anomaly is invalid / NaN
- no epsilon
- no fallback scale estimator
- no clipping

AS-104 never combines features. Preserve feature-family metadata, including the
shared `red_edge_b5_vs_red` family for `ndci_like` and `red_edge_red_ratio`.
These must not later be interpreted as independent biological evidence.

AS-104 outputs are temporal spectral anomalies, candidate feature deviations,
observational anomalies and baseline-relative signals. They are NOT HAB detections,
bloom detections, calibrated chlorophyll, species/toxin evidence, water-safety
evidence, intake exposure, persistence, risk score, alert level, monitoring
recommendation or warning lead-time proof.

### Frozen owner modifications and implementation contract

Use semantic `as104-input-v1` fingerprints. Target: full valid-water mask, all six
feature masks, supported feature values. Selected references: feature validity
restricted to target feature support and values only on the target/reference
support intersection. Exclude reference pixels outside target support, invalid
NaN payloads, future and out-of-period scenes. Use length-delimited canonical
headers, C-order masks and little-endian float32 payloads. Copy relevant inputs;
no concurrent-copy guarantee. Selected parent IDs/times remain in identity and
provenance even when a parent contributes no valid values. Do not implement
`precision_limited_scale_count` or any float32-epsilon pseudo noise floor.

Primary API: `compute_temporal_anomaly(scenes, *, target_product_id,
reference_start, reference_end=None, minimum_observations, registry)`.
Use start <= reference acquisition < effective end <= target acquisition;
normalize UTC, default effective end to target time, sort selected references by
acquisition then product ID. Reject duplicate products/times/observations,
malformed inputs, incompatible selected grids/feature/processing contracts and
unresolved/inconsistent upstream lineage. P0 uses the same tile, relative orbit
and delivered PC processing baseline; Sentinel-2A/B may coexist. Generation
times differ and are recorded. Minimum is an integer 3 through uint32 maximum;
booleans are rejected and there is no hidden default. Sparse/empty support is a
valid empty result, not an exception.

Float64 arithmetic, centre, scale and deviation; float32 standardized anomaly and
rank; uint32 counts, zero outside target feature support; boolean masks, all
subsets of target feature support. Positive scale is used directly; mask nonfinite
or non-representable float32 standardized results. Exact rank is
`(count(history < target) + 0.5*count(history == target))/n`, range [0,1], same
minimum; rank is not probability, p-value, confidence or severity. No interpolation,
trend fitting, seasonality correction, pooling, winsorization or outlier deletion.

Identity `temporal:<SHA-256(canonical identity)>`, version `as104-v1`, includes
selected parents/times, semantic fingerprints, grid, feature/family/compatibility
contracts, effective bounds, minimum, numerical/support/statistics/dtype policies
and Python/NumPy versions. Creation time and calculated summaries are excluded.
Immediate provenance parents are target AS-103 first, then chronological selected
references: PC -> AS-102 -> AS-103 -> AS-104. Registry is read-only during
computation; caller may register the result afterward. No generic schema change,
new dependency, config field or disk cache.

### Validation and scope

Pass offline independent arithmetic, support, numerical, causality, semantic
identity, model corruption, exact multi-parent lineage and blocked-IO tests before
real work. Predeclare April 28 target, March 1–April 1 UTC reference period and
minimum 5. Use unchanged AS-101/102/103 and ignored AS-102 caches; record actual
support and blockers without widening dates, lowering minimum, relaxing masks,
mixing processing or selecting by anomalies. Preserve all historical evidence.

No AS-105/106/107/108, ML, environmental/oil context, exposure, risk/alerts,
recommendations or dashboard. Positive is not dangerous; negative is not safe;
BOA is not aquatic Rrs. Acquisition-causal retrospective comparison does not
establish historical operational availability or warning lead time. Contract:
[AS-104 plan/API](AS_104_TEMPORAL_BASELINE.md).

---

## Decision 048 — Explicit Planetary Computer Processing-Baseline Selection

**Date:** 8 October 2026 (Asia/Dubai).
**Status:** Explicitly authorized.

### Decision

AS-102 may optionally receive an explicitly required Planetary Computer
processing baseline when resolving a known Sentinel-2 observation.

Resolution order is:

1. Validate each returned Planetary Computer item's existing structured
   metadata and processing metadata.
2. Identify items matching the expected observation exactly by acquisition
   timestamp, platform, MGRS tile and relative orbit.
3. If no required processing baseline is supplied, preserve the existing
   behavior exactly: require exactly one observation match.
4. If a required processing baseline IS supplied, filter the exact observation
   matches by that baseline.
5. Require EXACTLY ONE remaining product.
6. Zero remaining products: explicit failure.
7. More than one remaining product: explicit failure.

There is NO earliest-generation fallback, latest-generation fallback, implicit
preference for CDSE generation, automatic baseline preference or mixed-baseline
fallback. The constraint is explicit and caller-controlled.

The actual selected Planetary Computer product remains authoritative for pixels.
The selected actual PC source ID, processing baseline, generation time, provider
metadata and unsigned asset references remain recorded through the existing
AS-102 identity/provenance. The separate CDSE discovery product remains
discovery/matching context.

The required-baseline selector itself is a SOURCE-RESOLUTION CONSTRAINT, not a
new pixel-processing identity dimension. Therefore, if the same actual PC product
is selected, product/cache identity remains the existing identity of that actual
product. Do not create a second cache identity merely because the caller supplied
the selector explicitly. Do not change cache schema or rewrite old cache manifests.

However, all cache-return paths MUST enforce a supplied constraint: a cached
AS-102 scene must not be returned when its recorded `pc_processing_baseline`
conflicts with `required_processing_baseline`.

This extends Decision 039. It does not change reflectance decoding, grid
construction, masks, resampling, actual-source provenance, AS-103 or AS-104
algorithms.

### Cross-worktree coordination and evidence

At base `c6accab2c5753734466a6375d1b3ce1762e99bed`, merged main ends at Decision
046. Decision 047 remains only in the separately authorized, uncommitted AS-104
worktree on `feature/as-104-temporal-baseline`; it is deliberately not copied or
renumbered here, as explicitly instructed by the owner. Decision 048 keeps its
assigned number. M19 / E18–E19 / EV-022–EV-023 are reserved for that preserved
work; this separate fix uses M20 / E20 / EV-024.

AS-104 exposed the two-product ambiguity before reference XML/raster access.
Metadata investigation found one complete 05.09 product for each of the five
frozen March observations. The fix is a source-resolution extension only, left
uncommitted for review. AS-104 remains uncommitted and its real acceptance BLOCKED
until this upstream fix is reviewed/merged and acceptance is separately rerun.
See [fix plan/API](AS_102_REQUIRED_PC_BASELINE_FIX.md) and
[validation evidence](evidence/AS_102_REQUIRED_PC_BASELINE_FIX_VALIDATION.md).

### Post-merge integration checkpoint — 9 October 2026 (Asia/Dubai)

PR #10 merged the source-selection fix at
`39f2aee90c727fc151886efbdea44daec0e3f9b4` (feature fix
`c9a415b65a101319e9c9f2fef21ad0dcd44c9347`). Decision 047 and 048 now coexist
in order; the preceding cross-worktree/pending-review text is the original
8 October fix checkpoint, preserved verbatim. AS-104 source/tests were restored
byte-identically and the combined gate passed 533 tests, Ruff/diff checks and
six existing warnings. Frozen 05.09 real acceptance was resumed but stopped at
March 4 signing (HTTP 504 observed), not observation ambiguity. No selector,
processing/cache identity, numerical rule or scientific decision changed.
See M21/E21/EV-025 and the separately dated AS-104 validation evidence.

---

## Decision 049 — Reusable Planetary Computer Account/Container SAS Token Transport

**Date:** 9 October 2026 (Asia/Dubai)
**Status:** Explicitly authorized.

AquaSentinel shall replace repeated per-asset Planetary Computer `/sign`
authentication for supported Azure Blob assets with transient reusable
SAS tokens scoped to the validated Planetary Computer storage
account/container.

The actual stable unsigned asset HREF remains authoritative for:

- source metadata
- provenance
- processing identity
- cache identity
- cache manifests
- reproducibility records

SAS tokens and signed URLs are TRANSPORT-ONLY ephemeral credentials.

They MUST NEVER be written into:

- provenance
- product identity
- processing parameters
- cache manifests
- repository files
- logs
- exception messages
- evidence documents

The public `sign_asset(href, settings)` behavior remains:

unsigned stable HREF in
→ transient signed HREF out

The caller must not need to know whether authorization used a cached or
newly acquired token.

No AS-102 caller API change is required.

### Cross-worktree coordination and implementation boundary

Decision 048 was merged via PR #10 at
`39f2aee90c727fc151886efbdea44daec0e3f9b4`. Resumed AS-104 then encountered
intermittent per-asset authentication HTTP 504s; Decision 049 follows that failure.
Decision 047/M19/E18–E19/EV-022–EV-023 and M21/E21/EV-025 remain only in the
preserved, uncommitted AS-104 worktree; their bodies are not copied or renumbered.
This separate fix uses M22/E22/EV-026. Decision 048/M20/E20/EV-024 retain their
historical meanings.

Use the configured HTTPS issuer, official account/container token route and
actual `token` / `msft:expiry` response schema. Refresh at remaining lifetime
<=60 seconds. Token acquisition alone permits at most five attempts with
0.8/1.6/3.2/6.4-second backoffs for HTTP 429/500/502/503/504 or typed transient
connection/timeouts. No subscription key, SDK, dependency/config change, caller
change, pixel-processing change, provenance change or cache-schema change.
AS-104 real acceptance remains blocked pending fix review/merge.
See [plan](AS_102_REUSABLE_PC_SAS_TOKEN_FIX.md) and
[validation](evidence/AS_102_REUSABLE_PC_SAS_TOKEN_FIX_VALIDATION.md).

---

## Decision 050 — AS-105 Predeclared Family-Aware Candidate Anomaly Geometry

**Date:** 9 October 2026 (Asia/Dubai).
**Status:** Owner-approved v1 scientific policy; M28 offline engineering review
PASS and five-history clarification accepted 10 October 2026. Feature publication
authorized; PR code review is next after publication verification. Real geometry acceptance and comparative
policy validation are separately gated and NOT RUN.

**Decision:** Freeze `as105-v1` as a predeclared P0 screening heuristic on a
validated AS-104 parent, not a fitted/validated HAB classifier. For each feature,
use rank-valid support and evidence `deviation > 0 AND rank >= float32(0.90)`.
Record nominal 0.90, actual 0.8999999761581421 and threshold bits `3f666666`.
No robust-z gate or summary, epsilon, clipping, fallback or imputation.

**Owner-review clarification — 10 October 2026 (Asia/Dubai):** Nominal 0.90 and
the frozen float32 comparison remain unchanged. This is a predeclared
empirical-rank screening threshold whose effective granularity depends on the
available historical sample count, not a statistically estimated population
90th percentile, significance, probability, confidence or severity.
AS-104's exact-tie midrank is
`(count(history < target) + 0.5 * count(history == target)) / n`.
For the accepted five-history parent, no-tie ranks are spaced by 0.2:
0.0, 0.2, 0.4, 0.6, 0.8, 1.0. Thus the unchanged threshold requires the
target to exceed all five values in a no-tie pixel. Rank 0.90 is attained only
with four values below and one exact tie; three below and two ties yields 0.80.
These decimal ranks are stored as float32 before the frozen comparison.
This is an upper-tail screening rule, not a smooth percentile estimator.
Five observations are not statistical sufficiency; future comparative validation
remains required. M29 must use the already accepted parent with minimum five;
no AS-104 math, minimum or accepted evidence is changed.

F1 `red_edge_b5_vs_red` = ndci_like + red_edge_red_ratio;
F2 `red_edge_line_height` = mci_like;
F3 `red_edge_b6_vs_red` = red_edge2_red_ratio;
F4 `visible_green_vs_red` = green_red_ratio;
F5 `visible_green_vs_blue` = green_blue_ratio.
OR member evidence gives at most one family vote. Candidates require at least
two families and a vote from F1/F2/F3. Policy support independently requires at
least two available families and available F1/F2/F3, using OR of member rank
support. Fraction uses that support denominator, not AOI/water/all-six intersection.

Use deterministic row-major int32 eight-connected components with no morphology
or size filter. Polygonize four-connected pieces, group by label, preserve exact
pixel edges and canonical winding/start/holes/parts. Geometry stays in projected
AnalysisGrid CRS; exact raster round-trip is mandatory. Area derives from affine
determinant on supported north-up square projected metre grids, not hardcoded 400.

**Options considered:** rank + direction, z + direction or combined evidence;
feature counting versus family counting; alternate thresholds/family minima;
red-edge requirement; four/eight connectivity; region filtering. Owner freezes
one explainable policy now and requires a later bounded comparative study,
without tuning against the accepted April 28 observation. F1 grouping avoids
counting two related B05/red signals twice; distinct policy families do not imply
statistical independence or proof of biological causation.

**Integrity/lineage:** pure one-parent API; defensive array copies; canonical
consumed-mask/deviation/rank fingerprint, separate complete output fingerprint,
full policy/software/grid identity and parent-aware regeneration. Existing
DerivedProductRecord references exactly the AS-104 product, preserving actual
PC → AS-102 → AS-103 → AS-104 → AS-105 without schema/cache/dependency changes.
Rehashed alternate policy is invalid under v1.

**Scientific limits:** candidate spectral anomaly geometry only. Rank is not
probability, confidence, significance or severity. No HAB/bloom confirmation,
chlorophyll, species, toxins, water safety, intake risk, persistence, confidence,
alert or lead time. BOA is not aquatic reflectance. Roughly 10% five-history
support and the absence of statistical sufficiency from five observations remain
explicit; large z from small scales is not a geometry vote.

**Required future validation — NOT RUN:** bounded predeclared comparisons of
rank + direction, z + direction and combined rank/z; rank 0.80/0.90/0.95;
family minimum 1/2/3; red-edge required/optional; connectivity 4/8; no filtering
versus separately labelled region-filter sensitivity. Add **history-depth
sensitivity** where valid EO availability permits: predeclare support around
five, moderately deeper and substantially deeper histories. Select exact depths
from valid EO availability before running the study, to assess dependence on
coarse five-history rank resolution. Do not run it now or change the accepted
AS-104 parent/minimum for M29. April 28 cannot be both
tuning data and the sole proof of superiority. This task authorizes neither
that study nor real geometry acceptance, persistence/risk/alerting or P1 05.10.

**Evidence:** [contract/plan](AS_105_HAB_ANOMALY_GEOMETRY.md),
[offline validation](evidence/AS_105_HAB_ANOMALY_GEOMETRY_VALIDATION.md),
M28/E28/EV-032; 140 geometry and 803 full tests PASS with six existing warnings.

---

## Decision 051 — AS-106 Causal Consecutive-Valid Observation Recurrence

**Date:** 10 October 2026 (Asia/Dubai).
**Status:** OWNER-APPROVED / FROZEN DESIGN ONLY. AS-106 implementation NOT STARTED.
M31–M35 are future staged work, not executed checkpoints. Decision 050 is unchanged.

### Recurrence and evaluability

AS-106 consumes fully validated AS-105 `HABAnomalyGeometryScene` observations.
For each observation, `P_t = candidate_analysis_support_mask` and
`C_t = candidate_mask`. Validity for recurrence is P, not AOI or full water.
Target P=false is unevaluable; target P=true/C=false has current streak zero.
Target C=true starts at one. Scan earlier observations backwards:

- P=false: UNKNOWN; skip, neither increment nor break.
- P=true/C=true: increment.
- P=true/C=false: break the current streak; older candidates cannot reconnect it.

`recurrent_candidate_mask = target_C AND current_streak_count >= 2`.
This means **observed multi-observation recurrence**, not continuous biological
persistence. A target candidate without prior supported observations has streak
one but recurrence is unevaluable, not established absent.

`n_prior` counts all earlier P=true observations at each target-supported pixel,
including observations older than a streak-breaking non-candidate. Define:

- `Q = target_P AND n_prior >= 1` (persistence-evaluable mask).
- A = target candidate pixels; B = `target_C AND Q`; C = recurrent target candidates.
- `candidate_history_coverage = count(B)/count(A)`.
- `recurrence_fraction = count(C)/count(B)`.

Empty denominator means `None`; a nonempty denominator with zero numerator is
0.0. Do not substitute AOI, target valid water or full AS-105 P denominators.

### Space, timing and sequence

Use exact same-grid pixel overlap only. No dilation, buffering, morphology,
neighbourhood/adjacent/diagonal matching, IoU region matching, displacement,
advection/current/wind compensation, gap filling, reprojection or resampling.
Movement without exact overlap does not recur; this is a conservative v1 limitation.

No arbitrary calendar-gap cutoff. Use timezone-aware UTC arithmetic and exact
int64 microseconds. `previous_valid_observation_gap_us` is target time minus
the most recent earlier P=true time, -1 if unavailable, including outside target
P. `current_streak_span_us` is target time minus the oldest candidate in the
current streak: zero for a singleton target candidate, -1 outside target C.
These are satellite observation gaps/spans, not bloom duration.

Require unique AS-105 IDs and unique normalized acquisition timestamps; identical
AnalysisGrid; the same AS-105 version and Decision 050 policy; compatible AS-104
comparison context. Canonicalize caller order by UTC acquisition time. Reject
missing target, duplicates, future observations, a target that is not latest,
grid mismatch, policy/version mismatch or incompatible comparison context.

The common comparison context includes AS-104 version; AS-103 feature/formula
contract; reference product IDs/times/period; minimum_observations; target
grid/AOI; provider/collection; relevant tile/orbit; and upstream processing baseline.

### Integrity, API and lineage

Use `compute_hab_persistence(geometry_scenes, *, temporal_parents,
target_geometry_product_id)`, with temporal witnesses keyed by their product IDs.
For every geometry scene, call the existing `scene.validate(temporal_parent)`.
Its internal AS-105 regeneration is explicitly permitted as **INTEGRITY
VERIFICATION**, not retrieval, extraction for a new date, tuning, new scientific
input or duplicated family-voting logic. Do not weaken or duplicate AS-105 validation.

Persistence computation must not invoke optical/spectral extraction, AS-104
temporal computation or `extract_hab_anomaly_geometry`. AS-104 witnesses are
not immediate provenance parents. Immediate `source_ids` contain only the
chronological AS-105 product IDs, including target:
PC → AS-102 → AS-103 → AS-104 → AS-105 → AS-106.

### Output, identity and fingerprints

Expected model: `HABPersistenceScene`. Primary rasters: prior-valid count and
current streak uint32; evaluable/recurrent masks bool; previous-valid gap and
streak span int64 microseconds. Defensively retain target P/C where required for
self-validation/denominators. No persistence, risk or confidence score.

Target AS-105 regions remain authoritative; no deletion, geometry editing or
cross-date matching. Summarize region size, B/history coverage, recurrent count
and recurrent/B fraction, maximum/median streak on B, maximum/median observed
recurrence span on recurrent pixels, and chronological prior support/overlap
counts with overlap/support fractions. Empty support yields None; retain zero-
recurrence and unknown-history regions. Declare summary denominators explicitly.

Freeze version `as106-v1`, product type `hab_persistence`, prefix
`hab_persistence:`, input format `as106-input-v1`, output format `as106-output-v1`.
Identity records ordered AS-105 IDs/times, explicit target, grid, recurrence >=2,
unknown-skip/noncandidate-break rules, exact-pixel semantics, no gap cutoff,
common comparison context, denominator/dtype policies and relevant software
versions. `created_at` is provenance timing, excluded from identity.

Semantic content consumes UTC timestamps/common grid; full target P/C and target
labels/region identity; prior P where target P is true; prior C where target C
AND prior P are true. No unnecessary family-vote rasters, AS-104 spectral/z/
centre/scale values, unrelated pixels or prior component labels. Parent IDs
remain lineage identity inputs independently of the consumed-content fingerprint.

Use canonical JSON headers with explicit payload-length framing, C-order bytes,
masks as uint8, counts <u4, timing <i8 and labels <i4. Output-content fingerprint
covers all scientific output arrays and typed summaries. Parent-aware result
regeneration must reject tampering even if its output fingerprint is recomputed.
Inputs remain unmodified; returned arrays/metadata must not alias parents.

### Predeclared future real sequence and boundary

Before inspecting anomaly outputs, select every eligible acquisition in
`[2023-04-01T00:00:00Z, 2023-04-28T06:46:29.024000Z]`: configured Al Raha AOI,
accepted 20 m grid, existing cloud metadata <=30%, tile 40RBN, orbit 20, both
Sentinel-2A/B, strict cross-provider time/platform/tile/orbit matching, exactly
one PC 05.09 product, required assets and unchanged AS-102/103/104/105 contracts.
Resolve metadata ambiguity first; never remove sparse-support, zero-candidate
or inconvenient observations because of anomaly outcomes.

Use the same five accepted March AS-103 reference IDs and
`[2023-03-01, 2023-04-01)`, minimum_observations=5. April temporal computations
remain target-specific because support differs; there is no common precomputed
baseline raster valid for all April targets. Existing accepted caches are March
4/9/14/24/29 and April 28 only. Earlier-April inventory is unknown and no verified
earlier-April cache exists: real acceptance is **BLOCKED ON FUTURE DATA
PREPARATION**, not an offline algorithm blocker.

Allowed claims: observed candidate recurrence, history coverage, observation
gaps and exact-pixel streaks. No continuous biological persistence, HAB/bloom
confirmation, bloom duration, concentration/species/toxins, biological causation,
sensitivity/specificity/accuracy/false-positive rate, risk/confidence, exposure,
water safety, alert or warning lead time. Shared March references are not
statistically independent confirmation. Decision 050's scientific limitations
and future comparative policy validation remain unchanged.

### Staged authorization

M31/E31/EV-035: offline implementation/adversarial validation; M32/E32/EV-036:
metadata-only April inventory, no imagery; M33/E33/EV-037: separately authorized
missing April AS-102→103→104→105 preparation/handoffs; M34/E34/EV-038: offline
real recurrence acceptance; M35/E35/EV-039: owner review/publication/merge/closeout.
None is executed or implementation-authorized by this design freeze. No new
dependency, generic provenance/cache change, AS-107+, AS-105 policy comparison
or P1 05.10 experiment is authorized.

**Design specification:** [AS-106 Persistence](AS_106_PERSISTENCE.md).

---

## Decision 052 — AS-107 Explainable Availability-Aware HAB Risk and Evidence Completeness

**Date:** 10 October 2026 (Asia/Dubai).
**Status:** FINAL / FROZEN DESIGN — NOT IMPLEMENTED. Owner-approved M37 only.
M36 audit COMPLETE; no real AS-107 score inspected/calculated, scientific product,
implementation, AS-108 or context/exposure work. Decisions 050/051 unchanged.

### Scientific scope and qualification

An explainable availability-aware provisional observational HAB-like screening-risk
layer, not complete intake operational risk. Freeze assessment_status
`provisional_observational_screening` for every scored region and site summary;
current context/exposure are unavailable, so current P0 is always provisional.
No confirmed HAB, species/toxins, chlorophyll concentration, biological certainty,
water-safety certification, shutdown advice, HAB probability, calibrated confidence,
accuracy or warning-lead-time validation. Al Raha is a validation AOI, not a confirmed intake.

### Regional components and overlap

Use unchanged AS-105 regions/labels. For family j, exact integer
`a_j=count(R intersect family_available_j)` and
`v_j=count(R intersect family_evidence_j)`. Family order/membership stays Decision
050 (F1 B05/red, F2 line height, F3 B06/red, F4 green/red, F5 green/blue); F1
still counts once. Derive regional availability from masks, not global diagnostics.

- spectral_anomaly: `S_R=100*sum(v_j)/sum(a_j)` over all five families, available
  only for positive denominator; spectral family-evidence breadth over available
  family-pixel opportunities.
- chlorophyll_red_edge_signal: `E_R=100*(v1+v2+v3)/(a1+a2+a3)` only with positive
  denominator. Scientific name: **red-edge family evidence breadth**; no
  concentration or biological-causation inference.
- persistence: region A_R=target candidates, B_R=candidates with valid prior
  history, C_R=recurrent candidates; `T_R=100*C_R/B_R` only when B_R>0.
  B_R=0 means None/unavailable/no_prior_valid_candidate_history, not absent
  recurrence. Unsupported candidates/streak=1 do not establish nonrecurrence.
  Preserve streak/timing for explanations only, without a new gap cutoff.

No raw z/rank/deviation magnitude/new threshold. F1–F3 appear in both spectral
and red-edge components: correlated/overlapping evidence, not independent
confirmation. Existing weights deliberately emphasize red-edge evidence. Record
this limitation in diagnostics, limitations and driver/explanation metadata.

### Weights, missing policy, risk and coverage

Canonical component order/raw weights q_i remain spectral_anomaly=0.35,
chlorophyll_red_edge_signal=0.20, persistence=0.15, environmental_context=0.15,
intake_exposure=0.15. Do not alter config. Require exactly these names, finite
nonboolean numeric/nonnegative weights, positive total, positive required spectral/
red-edge weights and abs(fsum(q_i)-1)<=1e-9. Retain raw and normalized weights;
these are PoC hypotheses, not validated scientific constants.

Availability-aware renormalization; never zero/neutral/imputed context/exposure.
Mandatory spectral and red-edge unavailable => no score. Persistence may be
unavailable. Context/exposure are unavailable/not_implemented. Unavailable driver:
component_value=None, effective_weight=0, contribution_points=None, explicit reason.

```text
W0 = math.fsum(all q_i in fixed canonical order)
w_i = q_i / W0
K_R = math.fsum(w_i for available components in canonical order)
risk_R = 100 * math.fsum(w_i * (x_i / 100) for available components in canonical order) / K_R
```

Zero K_R => no score. Component coverage=available configured weight/all configured
weight, evaluated canonically as K_R. P0 maximum possible coverage 0.70; persistence
unavailable with mandatory components available gives 0.55. These are configuration
consequences, not real outcomes. Renormalization can raise score when a low-valued
component becomes unavailable; coverage/reasons must remain visible.

### Evidence completeness, B=0 and zero regions

Primary field/name: evidence_completeness. For nonempty region N_R=A_R:

```text
F_all = sum(a_j for all five families) / (5 * N_R)
F_red = (a1 + a2 + a3) / (3 * N_R)
H_R = B_R / A_R
evidence_completeness_R = min(component_coverage_R, F_all, F_red, H_R)
```

Output every factor and its numerator/denominator, including integer family/history
counts. It is support/evidence completeness, not probability, biological confidence,
statistical sufficiency, accuracy or event likelihood. No second AS-104 support
multiplier; family availability already incorporates eligible temporal support.
B_R=0 => persistence unavailable/H_R=0/completeness=0; a provisional mandatory-
component score may exist. Zero completeness means missing history, not zero
HAB likelihood/anomaly, safe water or HAB absence.

Zero AS-105 candidate regions => no fabricated region; site status no_candidate_regions;
score/band/completeness/selected_region=None, observation time and evaluability/policy
support diagnostics retained. Exact wording: "No candidates under the frozen policy
in evaluable observations." Do not output risk zero/Normal/safe/absence of HAB;
distinguish from unevaluable observation using support diagnostics.

### Bands, interpretation, monitoring and aggregation

Strictly increasing nonnegative integer maxima ending at 100; reject boolean,
negative/equal/malformed thresholds. Cut points low_max+1/watch_max+1/elevated_max+1.
Defaults: Normal [0,25), Watch [25,50), Elevated [50,75), High [75,100]. Compare
unrounded binary64 values; no epsilon/snapping. Score/band/completeness/coverage/
factors/flags/recommendations separate. High stays High; no completeness multiplication.
Freeze administrative limited_evidence_completeness_threshold=0.50, uncalibrated:
<1 => incomplete_evidence; <0.50 => also limited_evidence_completeness. This
qualifies wording, never score/band or probability/biological confidence.

Recommendations: Normal "Continue scheduled observation"; Watch "Review on the
next valid acquisition"; Elevated "Prioritize targeted review and field verification";
High "High-priority field verification and increased monitoring". Unscored =>
evidence review/additional valid observations. No shutdown/unsafe-water certification/
confirmed bloom or petroleum action. Limited completeness wording visibly says
verification is required and context/exposure are unavailable.

Score each authoritative region; retain ID/label/count/area/family/persistence.
No geometry edit/merge/filter; retain one-pixel regions with single_pixel_region
limitation, no biological coherence claim. Site maximum: descending raw score,
descending completeness, ascending component label. Copy selected score/band/
completeness/coverage/drivers/recommendation/limitations together. No region average
or HAB/oil combination; screening summary, not validated whole-site risk.

### Drivers, typed API and parent-aware integrity

RiskDriver: canonical_name, component_value float|None, configured_weight,
canonical_weight, effective_weight, contribution_points float|None, availability,
unavailable_reason, typed evidence counts/denominators, definition_id and source_product_ids.
All five stored in canonical order. Available effective_weight=w_i/K_R;
contribution_points=effective_weight*component_value. Explanation order: descending
available contribution/canonical tie order, then unavailable canonical order.
Canonical risk arithmetic reconstructs raw score from driver values/weights;
display rounding is non-authoritative.

```text
compute_hab_risk(geometry_scene: HABAnomalyGeometryScene,
    persistence_scene: HABPersistenceScene, *,
    geometry_scenes: Iterable[HABAnomalyGeometryScene],
    temporal_parents: Mapping[str, TemporalFeatureScene],
    policy: HABRiskPolicy) -> HABRiskScene
```

Explicit geometry exactly matches persistence target. Call existing geometry.validate
with temporal parent and persistence.validate with complete geometry sequence/typed
witnesses. AS-104 witnesses are integrity inputs, not immediate scoring sources.
Require matching ID/time/grid/masks/labels/regions/counts/fractions/contracts.
Future risk validator regenerates outputs from validated parents and rejects even
rehash-consistent tampering. No IO/network/registry mutation/retrieval/public upstream
extraction. Existing validators' internal regeneration is integrity verification.
Frozen dataclasses/canonical tuples/defensive copies/no aliasing. Intended models:
HABRiskPolicy, RiskDriver, EvidenceCompletenessFactors, HABRegionRisk,
HABSiteRiskSummary, HABRiskStatistics, HABRiskDiagnostics, HABRiskScene.
No raster/cache/new dependency or production modules in M37.

### Lineage, identity and deterministic serialization

Immediate source_ids exactly `(target_geometry_scene.product_id, persistence_scene.product_id)`.
No fictional unavailable-component IDs or PC/AS104 shortcuts. Preserve actual PC →
AS-102 → AS-103 → AS-104 → AS-105 → AS-106; AS-107 consumes target AS-105 + AS-106;
registry may deduplicate shared ancestry. No generic provenance change.

Freeze as107-v1 / hab_risk / hab_risk:. Identity includes parent IDs/required
versions, target acquisition/grid, input fingerprint, raw/canonical weights,
component/missing/mandatory definitions, completeness/0.50 flag, continuous bands,
site/ties, monitoring/qualification/assessment and relevant software versions.
Exclude created_at/display rounding/publication metadata.

as107-input-v1 framed SHA-256: consumed target policy/candidate masks/labels,
family availability/evidence on candidate support, authoritative region identities/
consumed measurements, AS-106 regional A/B/C/recurrence/history/timing/streak/matching.
Exclude unrelated reflectance/z/rank/deviation and full AS-104 witness payloads.
Consumed-bit change changes fingerprint even if final risk is equal; parent IDs
separately enter identity. as107-output-v1 covers all regions/five drivers/components/
denominators/availability/score/band/completeness/factors/coverage/interpretation/
assessment/recommendation/site/statistics/diagnostics/limitations, excluding
resulting AS-107 ID/creation time to avoid circularity.

Float64/Python float, exact counts, math.fsum/fixed order, finite nonboolean values,
no NaN/infinity/clipping/score or band epsilon; zero denominator unavailable None.
Sorted JSON keys/fixed semantic lists/aware UTC/allow_nan=False, exact binary64
fingerprint encoding (hex policy floats acceptable), null unavailable. Mapping
order cannot affect identity. Invalid values/results rejected, not clipped.

### Validation and authorization boundary

Future synthetic/adversarial requirements and typed model details are frozen in
[AS-107 contract](AS_107_HAB_RISK.md#future-m38-synthetic-and-adversarial-acceptance--not-run),
including three/current and generic five/future components, missing/partial history,
mandatory components, empty/single/multiple regions/ties, all score/band boundaries/
neighbours, numeric/policy rejection, ordering/time exclusion, incompatible targets,
witnesses, low-completeness High and complete tamper/IO/lineage/copy controls.
Future arbitrary provider components not accepted; zero-score tests do not fabricate
invalid AS-105 candidates. Recomputed attacker hashes do not confer validity.

M39 real acceptance only after this decision merged/frozen, separate implementation
authorization, synthetic/adversarial PASS and separate acceptance authorization.
Unchanged accepted typed parents/witnesses, sealed hashes/modes, offline independent
counts/components/score/band/completeness/drivers/site/repeat/permutation/identity/
provenance/tamper/preservation. No expected real score/band; accept without tuning.
AS-108 separately owns historical accuracy/sensitivity/specificity/false positives/
biological truth/chlorophyll accuracy/toxic confirmation/optimal thresholds/lead
time/calibration/intake-decision quality. AS-108 NOT STARTED.

M36/E36/EV-040 COMPLETE; M37/E37/EV-041 design only; M38–M40 reserved NOT STARTED.
Evidence: [M37 record](evidence/AS_107_DESIGN_FREEZE.md). Owner review/design PR+merge
and separate implementation authorization required. No PR/merge/real score or
implementation in M37. Future AS-105 policy validation NOT RUN; P1 05.10 NOT STARTED.

---

## Pending Decisions

The following decisions are intentionally not final yet:

### Full geospatial dependency stack

Packages such as:

- `rioxarray`,
- `xarray`,
- `geopandas`,
- `stackstac`

should be introduced only when their task requires them.

### Final operational demo site

A future desalination/intake demonstration location must be chosen from a defensible public source.

### Hyperspectral event/site

Depends on usable EnMAP/813 data availability.

### Final fitted ML model

Only select after determining label availability and baseline performance.

---

## Decision Review Rule

Before making a change that contradicts one of these decisions:

1. identify the affected decision,
2. explain why it should change,
3. evaluate impact on scope/deadline/scientific validity,
4. update this document if the change is approved.

The purpose of this file is to prevent accidental architectural drift and loss of project reasoning.

## Historical AS-104 Execution Note — Case Representation and Cached Acceptance

9 October 2026 (Asia/Dubai): the owner-authorized M24/E24/EV-028 bug fix changes
one AS-104 provenance consistency equality to `.casefold()` comparison only.
It introduces no aliases, stored platform normalization or identity rewrite;
all other validation and Decision 047's scientific contract remain unchanged.
No Decision 050 is created. Decisions 047–049 and historical M23/E23/EV-027
remain preserved. M25/E25/EV-029 records the frozen cached 05.09 real acceptance
PASS, with minimum five, sparse support, scalar/causal/repeat verification and
unchanged AS-102/AS-103 identity. See the AS-104 validation §§6–7 for evidence.
These are execution checkpoints, not a new architectural/scientific decision.
AS-104 remains uncommitted for review; no AS-105+ or P1 05.10 study.

## Historical AS-104 Publication Execution Note — M26 / E26 / EV-030 (before PR #12 merge)

AS-104 feature commit `09b38bd9c312470e948b1f17165ec5335cfc149d` is committed
and pushed on the existing feature branch from parent `2006df7a70a4f48c66933aed96f4464d8d03084e`.
This publishes the already accepted implementation/evidence; it is not a new
scientific/architectural decision and does not create Decision 050. Current
publication status supersedes the earlier execution stop state above, while
Decisions 047–049 and M23–M25 remain historically intact. PR not yet created;
not merged. Review published commit next; no AS-105+ or P1 05.10 study.

## AS-104 Merge/Closeout Execution Note — M27 / E27 / EV-031

AS-104 is COMPLETE AND MERGED via PR #12 at `472edc737847dc8581290a372c5da28f71fc48f0`,
merged **2026-10-09T13:26:08+04:00 Asia/Dubai** / **2026-10-09T09:26:08Z**.
The two reviewed commits are implementation `09b38bd9c312470e948b1f17165ec5335cfc149d` and publication
documentation/final feature head `703af1176aeaf9ba38d31c53648907c3b1792aec`. Real acceptance PASS;
accepted math, identities, measurements and scientific guardrails are unchanged.
M23–M26 and Decisions 001–049 remain historical records. This is an execution/
history event under the existing decisions, not a new Decision 050.
No unresolved AS-104 P0 blocker; known coverage/scientific limits remain. Owner
review of the next milestone/AS-105 design before implementation requires separate
authorization. Both stashes/recovery artifacts retained; no EO rerun, new merge,
AS-105+ or P1 homogeneous-05.10 experiment.
