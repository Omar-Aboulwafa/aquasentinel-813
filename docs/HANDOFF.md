# AquaSentinel 813 — Handoff Guide

## Current AS-201 M48 implementation — 11 October 2026 (Asia/Dubai)

**Decision 054 / M47 FINAL / FROZEN DESIGN / MERGED**, via PR #29 at
`1d2d994c7a04cca712485ce53dc9132db50615a8`. **M48 / E48 / EV-052: AS-201 RAW-GRD
RETRIEVAL / SOURCE IMPLEMENTATION COMPLETE; OFFLINE ENGINEERING VALIDATION PASS.**
This is source/header/XML engineering, not SAR preprocessing or oil detection.
AS-107 COMPLETE / CLOSED; AS-108 P0 case study COMPLETE / MERGED with POST
UNAVAILABLE and PARTIALLY_CONSISTENT remain unchanged.

Active implementation branch: `feature/as-201-sentinel1-retrieval`.
Existing WIP `d6f89ce07eaf6216308f39087ce094877d2bfd02` is preserved without rewriting.
Related remote correction `2abbe5a64e4017b8fc30ba243e3fe4c30f509a3c` was also
reviewed and preserved as an ancestor before the final completion commit.
Its twelve original paths were reviewed; follow-up corrections complete footprint
support/gaps, immutable models, group/set identities and derived retrieval lineage,
and harden raw TIFF/XML/transport validation. Both source slots/date and all six
slots remain explicit on failure. Missing footprint support is a lower bound,
never zero anomaly; metadata support does not establish pixel evaluability.

Engineering gates/results and review findings are in
[EV-052 implementation evidence](evidence/AS_201_IMPLEMENTATION_VALIDATION.md) and [JSON](evidence/AS_201_IMPLEMENTATION_VALIDATION.json).
Final M48 gate: **147 focused / 1432 full tests PASS**, six existing Rasterio
warnings; Ruff/diff/strict JSON/credential/preservation checks PASS.
No new real-provider probe, SAR pixels, scientific compute or scientific product.
M46 access evidence is historical and is not a six-slice live M48 acceptance claim.
Frozen Decisions 050–054, accepted HAB evidence, caches, stashes and recovery
material remain preserved. Shapely 2.1.2 is used only for metadata polygon topology.

**AS-202 NOT STARTED; Decision 055 ABSENT.** Calibration/noise correction, dB,
reprojection, resampling, mosaicking, speckle filtering, masking and oil detection
remain outside AS-201. Future AS-105 policy validation and P1 05.10 NOT STARTED.
Immediate next step: owner review of published M48 implementation → separately
authorized PR/merge. Any six-slice provider metadata acceptance or AS-202 design
requires separate owner direction. No M48 PR or merge performed; no CI claim.

## Historical AS-201 M47 design freeze — before PR #29 merge — 11 October 2026 (Asia/Dubai)

**AS-107 COMPLETE / CLOSED. AS-108 P0 RETROSPECTIVE OBSERVATIONAL-CONSISTENCY
CASE STUDY COMPLETE / MERGED with POST UNAVAILABLE**, via PR #28 at
`9a8a15c489a6aa3e678b642d2ccf5160affc56bd`. M44 PARTIALLY_CONSISTENT and all accepted scientific evidence
remain unchanged. M45/E45/EV-049 and M46/E46/EV-050 are now recorded historically
as completed read-only predecessor audits; PC_GRD_ACCESS_GATE PASS.
**Decision 054 / M47 / E47 / EV-051: FINAL / FROZEN DESIGN / NOT IMPLEMENTED.**

Frozen Kharg envelope EPSG:4326 [49.60,28.60,50.70,29.60], explicit source gaps and
common three-date comparison support; Apr24 REFERENCE → May6 DOCUMENTARY_EVENT →
May18 LATE_FOLLOW_UP, same S1A IW ascending orbit101 VV/VH, both slices/date.
CDSE discovery → exact PC GRD access mapping; RAW_GRD_AMPLITUDE; runtime-only
tokens; no provider fallback. Actual headers/XML roles govern provider defects.
SIGMA0_ELLIPSOID is a candidate, NOT FROZEN; AS-202 numerics/downstream rules remain
unfrozen. No pixels, SAR science, petroleum/source confirmation or intake invented.

Current active scientific development branch: none. This design was prepared on
`docs/as-201-design-freeze`. **AS-201 implementation and AS-202 NOT STARTED;
Decision 055 ABSENT.** Future AS-105 policy validation and P1 05.10 NOT STARTED.
Immediate next step: owner review → separately authorized M47 PR/merge → separate
AS-201 implementation authorization. No M47 PR or merge performed.
See [contract](AS_201_SENTINEL1_RETRIEVAL.md), [freeze evidence](evidence/AS_201_DESIGN_FREEZE.md)
and [JSON](evidence/AS_201_DESIGN_FREEZE.json). Engineering results are recorded in
the freeze evidence; historical checkpoints below retain their original states.

## Historical AS-108 M44 reporting — before PR #28 merge — 10 October 2026 (Asia/Dubai)

**AS-107 COMPLETE / CLOSED. Decision 053/M42 FINAL / FROZEN DESIGN / MERGED.**
M43 metadata selection COMPLETE / MERGED via PR #27 at `865cd14398c6bcdbeaed6a19210f5615beb638e6`.
**M44 / E44 / EV-048: RETROSPECTIVE CASE-STUDY REPORTING COMPLETE.**
**AS-108 P0: RETROSPECTIVE OBSERVATIONAL-CONSISTENCY CASE STUDY COMPLETE WITH POST UNAVAILABLE.**
Decision 053 category: **PARTIALLY_CONSISTENT**, from accepted evidence and unchanged
criteria: five descriptive PRE records evaluable; April 3 AS-105 P = 794 / candidates = 88,
April 28 P = 802 / candidates = 7 plus accepted Watch = 29.52380952380953; required POST
geometry endpoint absent. PRE is not independently scored or biologically negative.
April 3 AS-106/107 remains missing; no score fabricated.

April 28 accepted completeness/coverage = 0.7/0.7, provisional_observational_screening,
Review on the next valid acquisition, exact-grid persistence A/B/C = 7/7/0 remain
unchanged. No same-pixel recurrence is not proof of no HAB or biological persistence.
POST provisional May 3 identity retained: no exact PC 05.09 match, no pixels,
no scientific product/risk/negative/recovery label; no May 8/13/28 query/substitution.
M43 digest `df487999defada56023a7e76be69c507b2b1ff11d81de1480737eca86a1ad4de` unchanged.

This is a retrospective month/area observational-consistency case, not blind,
prospective, independent April preregistration, biological accuracy, species/toxin/
chlorophyll confirmation, probability, calibrated confidence, water safety or
shutdown advice. April outcomes were known before Decision 053; categories frozen
before May metadata, unavailable POST preserved. Exact onset-relative lead time
NOT ESTIMABLE. Scientific processing/EO/documentary requests in M44: **zero**.
Prepared on `data/as-108-case-study`; current active scientific development branch:
none. No Decision 054. AS-201, future AS-105 policy validation and P1 05.10 NOT STARTED.

Case SHA-256: `ccc5f04f304a8b4bb8a367331069a5ca54776433e7c0fea0c67d662e68e0772a`.
Engineering gates: **1285 full tests PASS (100.78s)**; six existing Rasterio
PendingDeprecationWarnings; Ruff PASS; diff/new-file whitespace PASS; strict finite
JSON, independent digest/repeat, predicate, credential and preservation checks PASS.
Engineering fixtures attempted no external network; no GitHub CI success claimed.
Immediate next step: owner review → separately authorized M44 PR/merge → separate
AS-201 Sentinel-1 retrieval/design authorization. No PR created or merge performed.
See [case report](evidence/AS_108_HISTORICAL_CASE_STUDY.md) and [JSON](evidence/AS_108_HISTORICAL_CASE_STUDY.json). Earlier checkpoints retain their original historical facts.

## Historical AS-108 M43 POST metadata selection — before PR #27 merge — 10 October 2026 (Asia/Dubai)

**AS-107: COMPLETE / CLOSED. Decision 053 / M42: FINAL / FROZEN DESIGN / MERGED**
via PR #26 at `8bb56f12f2cd683d4a96f069c5d049bf4a39799e` (parents
`14149113e58788621d6aef91f039b95781c67434` and
`9e7254edc7680c5da31e796f82be2b8537833b9b`).
**M43 / E43 / EV-047: POST METADATA INVENTORY / SELECTION COMPLETE; selection UNAVAILABLE.**
Six complete CDSE pages yielded **26 provider records / 26 distinct observation
keys / 13 acquisition timestamps**. Four pass CDSE metadata eligibility. Earliest:
**2023-05-03T06:46:21.024000Z**, Sentinel-2A, 40RBN/orbit20, cloud metadata **0.57%**.
The fixed existing PC resolver query returned **0 items / 0 exact PC05.09 matches**.
Selected PC ID/baseline: null. No later acquisition substituted or queried on PC.
This is metadata-selection UNAVAILABLE, **not a scientific consistency category**.

Selection SHA-256: `df487999defada56023a7e76be69c507b2b1ff11d81de1480737eca86a1ad4de`.
POST pixels, asset/signing/range requests, scientific processing and new risk scores:
**0 / NOT STARTED**. No May water-support inspection, recovery/negative label,
observational-consistency conclusion or upstream policy change. M42 evidence,
Decisions 050–053 and accepted scientific evidence remain unchanged.

Prepared on `data/as-108-post-selection`, worktree
`/workspace/aquasentinel-813-as108-m43`. Immediate next step: owner review of the
UNAVAILABLE metadata evidence, then separately authorize M44 case-study reporting
from accepted PRE/EVENT evidence with POST explicitly UNAVAILABLE. PR/merge and
any further compatibility investigation need separate authorization. **M44, AS-108 scientific execution and AS-201 NOT STARTED.**
Engineering gates: 1285 full tests PASS (106.24s), six existing Rasterio PendingDeprecationWarnings; Ruff PASS; diff/new-file whitespace PASS. No GitHub CI success claimed.
See [M43 evidence](evidence/AS_108_POST_METADATA_SELECTION.md) and
[complete inventory/selection digest](evidence/AS_108_POST_METADATA_SELECTION.json).
Earlier dated checkpoints below remain historical; no outcome tuned or hidden.

## Historical AS-108 M42 design freeze — before PR #26 merge — 10 October 2026 (Asia/Dubai)

**AS-107: COMPLETE / CLOSED. M40: COMPLETE / MERGED / PUBLICATION-CLOSEOUT**
through PR #25 at `14149113e58788621d6aef91f039b95781c67434`, with verified parents
`2bfbbd63cb5fee8e1d18a0b1099335b924e5ed9d` and
`88189f5ed85767f5022fa8e6c8ceee55b42f6c85`. Its merge-effective closure is now in force.
**M41 / E41 / EV-045: read-only feasibility/source audit COMPLETE**, recorded here
retrospectively; M41 changed no repository file. Its documentary access blocker was
resolved by externally verified EAD facts supplied by the project owner for M42;
Codex did not independently access the source, and no personal owner inspection
is claimed.
**Decision 053 / M42 / E42 / EV-046: FINAL / FROZEN DESIGN — NOT EXECUTED.**
AS-108 remains P0 before AS-201. No AS-108 validation outcome is computed here.

Frozen objective: **retrospective observational-consistency case study**, one event,
not biological accuracy. EAD **Marine Water Quality Report 2023**, listed
**21 November 2024**, documents a Raha Beach Red Tide incident in **April 2023**.
Timing **MONTH_LEVEL**; lead-time status **MONTH_LEVEL_ONLY**, exact days early not
estimable. Spatial precision **AREA_LEVEL_ONLY**; AOI/event relationship
**AREA_LEVEL_CONTEXTUAL_ALIGNMENT**. Al Raha remains analyst-defined, not an EAD
incident/sampling footprint or confirmed desalination intake. EAD species/toxin
context stays external: Pseudo-nitzschia multistriata / domoic acid; incident toxin
measurement NOT ESTABLISHED; AquaSentinel species/toxin inference NONE.

PRE `[2023-03-01,2023-04-01)` retains March 4/9/14/24/29 as descriptive context,
never self-baseline-scored or biological negatives. EVENT `[2023-04-01,2023-05-01)`
retains April 3 through accepted AS-105 and April 28 through accepted AS-107.
POST `[2023-05-01,2023-06-01)` requires one future metadata-selected **earliest
compatible May acquisition** before pixels; no fallback, honest UNAVAILABLE allowed.
Same AOI, cloud <=30%, 40RBN/orbit20, exact PC05.09 match and full grid/upstream
contract. No May metadata or pixels retrieved in M42; no frozen policy adjusted.

Immutable April 28 reference: `hab_risk:113143700cb35ac9230d9c54b68b1b53e2573838a4913d4bc942e81c99903fdb`;
**29.52380952380953 / Watch**, completeness/coverage **0.7/0.7**,
`provisional_observational_screening`, **Review on the next valid acquisition**,
A/B/C **7/7/0**. No rerun or new historical-validation classification in this task.
Decisions 050/051/052 and accepted EO evidence remain unchanged. No Decision 054.

Prepared on documentation branch `docs/as-108-design-freeze`, worktree
`/workspace/aquasentinel-813-as108-m42`; current active scientific development branch:
none. Immediate next step: owner review of Decision 053/design, with separate
PR/merge authorization; then separately authorize **M43 metadata-only POST selection**.
Validation execution, AS-201, future AS-105 policy validation and P1 05.10 NOT STARTED.
Deadline 11 October 2026 (Asia/Dubai): protect oil P0, demo and presentation.
M42 engineering quality: **1285 full tests PASS (115.87s), six existing Rasterio PendingDeprecationWarnings; Ruff PASS; diff/new-file whitespace PASS**; no GitHub CI-success claim.
New documentary/EO metadata/assets/real scientific calls: **0**.

See [AS-108 contract](AS_108_HAB_HISTORICAL_VALIDATION.md), [freeze evidence](evidence/AS_108_DESIGN_FREEZE.md),
and [machine-readable design](evidence/AS_108_DESIGN_FREEZE.json). Earlier dated status/milestone bodies
remain historical; their original unstarted/unmerged wording describes that time.

## Historical AS-107 M40 closeout preparation — before PR #25 merge — 10 October 2026 (Asia/Dubai)

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

**Historical Decision 048 fix checkpoint (8 October 2026, Asia/Dubai):** AS-104
discovered PC processing-product ambiguity. Its uncommitted worktree remains
byte-for-byte preserved. Only the separate AS-102 required-baseline fix is active
here: 421 tests (348 retained +73 new), Ruff/diff pass, same six Rasterio warnings,
6/6 metadata-only resolutions at 05.09. Real AS-104 acceptance remains BLOCKED
until this upstream fix is reviewed/merged and acceptance separately rerun.
Earlier AS-103-closeout authorization language below is historical; this update
governs current authorization. No commit/push/PR/merge; AS-105+ remains unstarted.

This file is the fast handoff document for a new ChatGPT session, Codex task, developer, or second machine.

**Historical AS-104 checkpoint (8 October 2026, Asia/Dubai):** Decision 047 supersedes
older AS-104 authorization statements in the preserved AS-103 checkpoints. Pure
API/models and offline validation are in review; real acceptance is blocked by
multiple same-observation PC processing products in unchanged AS-102 matching.
No commit/push/PR; no AS-105+ authorization. See the AS-104 section below.

---

## 1. What This Project Is

AquaSentinel 813 is an explainable, multi-hazard marine-intake intelligence system being developed for the Arab Youth Space Hackathon 2026 — Track 03: Water Security & Marine Environments.

Core product principle:

> AquaSentinel watches the sea before a threat reaches the intake.

Primary user:

> Desalination Plant Water Quality / Operations Manager.

Primary operational decision:

> Where and when should monitoring or field verification be prioritized?

The PoC currently focuses on:

- HAB / biological water anomaly as the primary hazard.
- Oil-slick candidate detection as the secondary hazard.

The product is decision support, not autonomous plant control.

---

## 2. Read These Files First

A new agent or developer should read these in order:

1. `AGENTS.md`
2. `docs/PROJECT_STATE.md`
3. `docs/DECISIONS.md`
4. `docs/AquaSentinel_813_PRD_v1.0.md`
5. `.agent/PLANS.md` when available

These files together contain the project scope, scientific guardrails, architecture, completed work, and next steps.

---

## 3. Current Engineering State

Completed:

- AS-001 — Repository Scaffold.
- AS-002 — Configuration & AOI Model.
- AS-003 — Provenance Model.

Completed continuity setup and Codex read-only onboarding:

- AS-000C.1 — `AGENTS.md` completed and merged into `main`.
- AS-000C.2 — `PROJECT_STATE.md` completed and merged into `main`.
- AS-000C.3 — PRD completed and merged under `docs/`.
- AS-000C.4 — `DECISIONS.md` completed and merged into `main`.
- AS-000C.5 — `HANDOFF.md` completed and merged into `main`.
- AS-000C.6 — `.agent/PLANS.md` completed and merged into `main`.
- AS-000C.7 — Codex read-only onboarding **COMPLETED** on 2 October 2026 at `779069d`.
- AS-000C.8 — Codex development handoff **COMPLETED** with explicit AS-101 implementation authorization on 2 October 2026.

Current project phase:

**Foundation/continuity complete → AS-101/102/103/104/105 MERGED → Decision 051 MERGED/FROZEN → AS-106 M31 OFFLINE IMPLEMENTATION/SYNTHETIC VALIDATION PASS → owner feature review next (PR NOT CREATED / FEATURE NOT MERGED) → real April acceptance BLOCKED ON FUTURE DATA PREPARATION → M32–M35 / AS-107+ NOT STARTED; future AS-105 policy validation NOT RUN; P1 05.10 NOT STARTED.**

Current implementation and next milestone:

- AS-101 — Sentinel-2 STAC Search was completed on `feature/as-101-sentinel2-stac` from base `51f4ede`. Implementation commit `41a0b0b`, documentation commit `b3f0e9f`, and the approved review fixes are merged into `main` via [PR #2](https://github.com/Omar-Aboulwafa/aquasentinel-813/pull/2) at merge commit `1b83a732155ee01c01b7d33cb50115725cfb08c3`.
- **97 tests passed**, Ruff passed, and `git diff --check` passed. A real CDSE query returned 44 scenes and every scene converted to valid provenance.
- See `docs/AS_101_STAC_SEARCH.md` for usage, semantics, and smoke-test evidence.
- AS-102 was explicitly authorized on 6 October 2026 and is **COMPLETE AND MERGED** through [PR #6](https://github.com/Omar-Aboulwafa/aquasentinel-813/pull/6). Implementation commit: `fe3d27046c40600010753957ee8921d57071ec48`. Merge commit: `627b6ae8a509509dbb2d5d43bbdc6d74e0ce2aac`, merged `2026-10-08T07:06:46Z` / `2026-10-08T11:06:46+04:00` Asia/Dubai. AS-103 is complete and merged through PR #8; AS-104 is COMPLETE AND MERGED through PR #12 at 472edc7, with implementation and frozen real acceptance PASS; AS-105 is COMPLETE AND MERGED through PR #14 at `24a260cff130238c731f7cb62fc47eb74230b4dc`, with M28 implementation/adversarial validation PASS and M29 real engineering acceptance PASS. Decision 051 remains frozen; AS-106 M31 offline implementation/synthetic validation PASS, with owner feature review next. M32–M35 and real April preparation/acceptance NOT STARTED; future AS-105 comparative policy validation REQUIRED / NOT RUN; AS-107+ and P1 05.10 NOT STARTED. See §22 for usage and validation evidence.
- AS-103 is **COMPLETE AND MERGED** through [PR #8](https://github.com/Omar-Aboulwafa/aquasentinel-813/pull/8). Implementation commit: `5638bc8b4ab06f235f908642f714a7cc83b35709`. AS-103 implementation merge commit: `b770d0561da9ac2b81ca2d4b8e784adff66ee231`, merged `2026-10-08T10:43:24Z` / `2026-10-08T14:43:24+04:00` Asia/Dubai. See §23 and journal M18 / EV-021 for final review/merge and preserved acceptance evidence.

---

## 4. Known Good Git State Before Continuity Setup

Known `main` merge commit before AS-000C work:

`db79260 merge: complete AS-003 provenance model`

Known feature commit for AS-003:

`e2baedc feat: add provenance tracking and lineage registry`

Known AS-002 merge commit:

`113ca44 merge: complete AS-002 configuration and AOI model`

Known AS-001 initial commit:

`f878acc chore: scaffold AquaSentinel 813 project`

Do not assume these remain the latest commits after this handoff file is merged. Always inspect Git.

---

## 5. Required Startup Checks

When resuming the project, run:

```text
git branch --show-current
git status
git log --oneline --graph --decorate -8
```

Then activate the Python environment:

```text
conda activate aquasentinel813
```

Then run:

```text
python --version
python -m pytest -v
python -m ruff check .
```

Expected Python major/minor:

`3.11`

At the completion of AS-003, the known test baseline was:

`17 passed`

and Ruff reported:

`All checks passed!`

A higher test count later is normal.

---

## 6. Office-PC Setup

Current office-PC project path:

`D:\aquasentinel-813`

Current Conda environment:

`aquasentinel813`

Personal GitHub account:

`Omar-Aboulwafa`

Personal GitHub SSH alias:

`github.com-omar-personal`

Expected origin:

`git@github.com-omar-personal:Omar-Aboulwafa/aquasentinel-813.git`

This machine also has company Git/GitHub usage.

Do not alter global Git identity or company SSH settings unless explicitly requested.

---

## 7. Personal-PC Setup Strategy

On the personal machine, use the same personal GitHub repository.

Recommended sequence:

1. Configure personal GitHub authentication.
2. Clone the repository.
3. Create a Python 3.11 environment.
4. Install the project:

```text
python -m pip install -e ".[dev]"
```

5. Run:

```text
python -m pytest -v
python -m ruff check .
```

6. Continue from a task-specific branch.

Do not manually copy code folders between machines when Git can synchronize them.

---

## 8. Multi-Machine Working Rule

Before leaving one machine:

1. run tests,
2. run Ruff,
3. inspect `git status`,
4. commit meaningful work,
5. push.

On the next machine:

1. fetch/pull,
2. activate/recreate the environment,
3. install updated dependencies if needed,
4. run tests,
5. continue.

Do not move secrets through Git.

---

## 9. Scientific Guardrails

Preferred wording:

- HAB-like spectral anomaly.
- Elevated biological water-quality risk.
- Oil-slick candidate.
- Observational risk.
- Confidence.
- Field verification recommended.
- Monitoring priority.

Do not claim that satellite observations alone have:

- confirmed toxic algae,
- confirmed algal toxins,
- confirmed petroleum composition,
- certified water as safe or unsafe,
- justified autonomous plant shutdown.

The system supports earlier awareness and human verification.

---

## 10. Current Sensor Strategy

### Sentinel-2

Primary P0 source for:

- water colour,
- chlorophyll-related signals,
- red-edge features,
- biological/spectral anomaly detection,
- temporal monitoring.

### Sentinel-1 SAR

Primary P0 source for:

- surface-slick candidates,
- oil-related surface anomalies,
- cloud-independent marine observation.

### EnMAP / future hyperspectral data

P1 enhancement for:

- detailed spectral characterization,
- confidence enhancement,
- multispectral-vs-hyperspectral comparison.

Hyperspectral is not a P0 dependency.

---

## 11. Current Validation Strategy

### HAB / biological anomaly

Primary candidate:

**Al Raha Beach / Al Raha Bay, Abu Dhabi — April 2023**

Current validation AOI:

`data/aoi/demo_site.geojson`

Important:

- the AOI polygon is analyst-defined,
- it is not an official boundary,
- it is not a desalination intake.

### Oil

Primary candidate:

**Kharg Island / Persian Gulf — May 2026**

Historical reports and EO-derived evidence must remain clearly separated.

---

## 12. Current Architecture

Core reasoning chain:

Observation
→ Detection
→ Explanation
→ Exposure
→ Risk
→ Monitoring Priority
→ Human Decision

Existing implemented foundations (including AS-102 merged through PR #6):

### Configuration and AOI

`src/aquasentinel/config/`

Includes:

- configuration models,
- TOML loading,
- AOI GeoJSON loading,
- validation,
- runtime context.

### Provenance

`src/aquasentinel/provenance/`

Includes:

- source records,
- derived product records,
- JSON serialization,
- registry,
- lineage tracking,
- persistence.

Expected lineage:

Source observation
→ derived feature
→ hazard layer
→ risk product
→ operational alert

---

## 13. Configuration

Current default config:

`config/default.toml`

Current configuration includes:

- application metadata,
- AOI path,
- cache path,
- analysis date window,
- maximum cloud cover,
- risk bands,
- HAB PoC weights,
- oil PoC weights.

Risk weights are PoC hypotheses, not validated scientific constants.

---

## 14. What Not to Do

Do not:

- begin major refactors unrelated to the active task,
- develop directly on `main` unless explicitly approved,
- introduce large dependency stacks preemptively,
- commit `.env`,
- commit SSH keys,
- commit credentials,
- commit raw large EO scenes,
- claim confirmed toxic algae from satellite evidence,
- claim confirmed oil from a low-backscatter SAR feature alone,
- make hyperspectral data a hard dependency,
- average unrelated hazards into one scientific score,
- bypass provenance for convenience.

---

## 15. AS-101 Implementation and Next Engineering Task

AS-101 was explicitly authorized and is now complete and merged into `main` via PR #2 at merge commit `1b83a732155ee01c01b7d33cb50115725cfb08c3`. AS-102 was explicitly authorized on 6 October 2026 and is **COMPLETE AND MERGED** through [PR #6](https://github.com/Omar-Aboulwafa/aquasentinel-813/pull/6). Implementation commit: `fe3d27046c40600010753957ee8921d57071ec48`. Merge commit: `627b6ae8a509509dbb2d5d43bbdc6d74e0ce2aac`, merged `2026-10-08T07:06:46Z` / `2026-10-08T11:06:46+04:00` Asia/Dubai. AS-103 is complete and merged through PR #8; AS-104 is COMPLETE AND MERGED through PR #12 at 472edc7, with implementation and frozen real acceptance PASS; AS-105 is COMPLETE AND MERGED through PR #14 at `24a260cff130238c731f7cb62fc47eb74230b4dc`, with M28 implementation/adversarial validation PASS and M29 real engineering acceptance PASS. Decision 051 remains frozen; AS-106 M31 offline implementation/synthetic validation PASS, with owner feature review next. M32–M35 and real April preparation/acceptance NOT STARTED; future AS-105 comparative policy validation REQUIRED / NOT RUN; AS-107+ and P1 05.10 NOT STARTED.

### AS-101 — Sentinel-2 STAC Search

Goal:

Given:

- configured AOI,
- configured date window,
- configured cloud-cover threshold,

return real Sentinel-2 observations suitable for downstream analysis.

Implemented AS-101 scope:

- use the explicitly selected CDSE default endpoint/provider, with configurable endpoint and collection,
- search by AOI,
- search by date interval,
- filter by cloud cover,
- deterministic result representation,
- map results into AquaSentinel provenance records,
- add tests.

Do not yet:

- download full imagery,
- run atmospheric correction,
- compute HAB indices,
- build ML risk models,
- build the dashboard.

---

## 16. First Codex Task — COMPLETED

The first Codex task was read-only and completed successfully on 2 October 2026 at `779069d`. Repository documentation, architecture, configuration/AOI, provenance, and tests were inspected, and Codex's understanding was verified without modifying repository files.

Read-only onboarding prompt reference:

```text
Read AGENTS.md, docs/PROJECT_STATE.md, docs/DECISIONS.md, docs/HANDOFF.md, and docs/AquaSentinel_813_PRD_v1.0.md.

Then inspect the repository structure, current Git branch/status, pyproject.toml, existing tests, config/AOI implementation, runtime context, and provenance implementation.

Do not modify any file.

Return:
1. your understanding of the product,
2. completed engineering milestones,
3. current architecture,
4. scientific guardrails,
5. current test/quality expectations,
6. what AS-101 should accomplish,
7. likely files/modules AS-101 should add or modify,
8. dependencies you think AS-101 actually needs,
9. any ambiguity, risk, or contradiction you detect.

Do not implement AS-101 yet.
```

Codex onboarding is complete. AS-000C.8 was completed by the separate explicit AS-101 development authorization on 2 October 2026.

---

## 17. AS-101 Codex Handoff Rule

Read-only onboarding was accepted, and AS-101 subsequently received explicit implementation authorization. Onboarding completion alone did not authorize code changes. Future milestones require separate authorization.

The AS-101 task should include:

- explicit acceptance criteria,
- a dedicated feature branch,
- test expectations,
- provenance integration,
- minimal dependencies,
- no full imagery processing.

Codex should report:

- files changed,
- dependency changes,
- tests added,
- test results,
- Ruff results,
- limitations,
- next recommended task.

---

## 18. Definition of a Healthy Handoff

A new agent/developer should be able to answer, without chat history:

- What is AquaSentinel?
- Who is the primary user?
- What decision does it support?
- Which hazards are P0?
- Which sensors serve which hazards?
- What scientific claims are prohibited?
- What has already been implemented?
- What is the known-good quality baseline?
- What is the next task?
- What must not be changed casually?

If those answers are unclear, repository documentation is incomplete.

---

## 19. Recovery From Context Loss

If a ChatGPT/Codex context window is lost:

1. reopen the repository,
2. read `AGENTS.md`,
3. read `docs/PROJECT_STATE.md`,
4. read `docs/DECISIONS.md`,
5. read this file,
6. inspect Git history,
7. run tests/Ruff,
8. continue from the next incomplete task.

Do not recreate prior decisions from memory when repository documentation exists.

---

## 20. Human Owner Checkpoint

Before a major scope or architecture change, ask the project owner when the change affects:

- primary product positioning,
- hazard scope,
- scientific interpretation,
- validation strategy,
- dependency architecture,
- deadline-critical P0 functionality,
- external service/provider commitment,
- model claims,
- operational recommendations.

Small implementation details inside approved acceptance criteria do not require constant re-approval.

---

## 21. Final Handoff Summary

Current project phase:

**Foundation/continuity complete → AS-101/102/103/104/105 MERGED → Decision 051 MERGED/FROZEN → AS-106 M31 OFFLINE IMPLEMENTATION/SYNTHETIC VALIDATION PASS → owner feature review next (PR NOT CREATED / FEATURE NOT MERGED) → real April acceptance BLOCKED ON FUTURE DATA PREPARATION → M32–M35 / AS-107+ NOT STARTED; future AS-105 policy validation NOT RUN; P1 05.10 NOT STARTED.**

Immediate priority:

**Review the published AS-106 M31 feature and synthetic/adversarial validation. M31 PASS; no PR/merge. M32 metadata-only inventory, M33 upstream preparation, M34 real acceptance and M35 closeout are NOT STARTED / separately authorized. Real April acceptance BLOCKED ON FUTURE DATA PREPARATION. Preserve upstream contracts and accepted artifacts/stashes. AS-107+ / P1 05.10 NOT STARTED; future AS-105 policy validation NOT RUN.**

Core constraint:

**Protect scientific credibility and P0 delivery before sophistication.**


## 22. AS-102 Merged Implementation Handoff

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

### Resume/reproduce

Read `docs/AS_102_OPTICAL_PREPROCESSING.md` and `docs/evidence/AS_102_OPTICAL_PREPROCESSING_VALIDATION.md` before changing code. On this cloud checkout, use `source .venv/bin/activate` (Python 3.11); existing office/home Conda guidance above remains valid. Reinstall the updated project dependencies in the relevant Python 3.11 environment before testing on another machine; do not assume runtime caches are shared by Git.

Public entry point: `aquasentinel.preprocessing.optical.preprocess_optical_scene(context, candidate)`. The candidate comes from existing `search_sentinel2(context)`. Offline replay: `preprocess_optical_scene(context, known_cache_id=cache_id)` validates cache/AOI/grid and performs no external-data work. Canonical default cache ID from the real acceptance:

`0725a908d21cd655e83f70d2bb11247dc0f1516f0c00ea275efc3239113ee4a6`

Cache is local under `data/cache/as102/<cache_id>/`, containing AOI arrays and unsigned manifest/provenance. If absent, follow the documented strict live workflow; if corrupt, fail and investigate rather than silently reuse it. All water consumers must apply `valid_water_mask`; a finite band value alone is not eligibility. Zero retained water is a valid outcome. Captured presentation screenshots/maps and independent aquatic/HAB validation remain outstanding.


## 23. AS-103 — Spectral Feature Extraction — COMPLETE AND MERGED

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


## 24. AS-104 — Historical Initial Review Checkpoint (8 October 2026)

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

## 25. Decision 048 — Historical Pre-Merge Fix Handoff

Read [fix plan/API](AS_102_REQUIRED_PC_BASELINE_FIX.md), Decision 048 and
[EV-024 validation](evidence/AS_102_REQUIRED_PC_BASELINE_FIX_VALIDATION.md).
Branch `fix/as-102-required-pc-baseline`; worktree
`/workspace/aquasentinel-813-as102-baseline-fix`; exact base
`c6accab2c5753734466a6375d1b3ce1762e99bed`. No dependency/config/schema changes.

Three existing APIs now accept optional keyword-only `required_processing_baseline`.
None retains exactly-one observation matching; an explicit NN.NN baseline filters
validated exact matches and still fails on zero/multiple products. No generation
fallback or CDSE-processing preference. Actual PC lineage and separate discovery
context remain recorded in existing identity. Same actual product means same
cache/product identity. Known-cache reload checks the constraint without access
or writes, and regular cache reuse checks it before returning.

Real metadata smoke on March 4/9/14/24/29 and April 28 resolved all expected 05.09
products, full eleven-asset set, tile 40RBN/orbit 20; **6/6 PASS**, **0** forbidden
signing/XML/raster/preprocessing/cache calls. Existing April cache ID
`0725a908d21cd655e83f70d2bb11247dc0f1516f0c00ea275efc3239113ee4a6` is unchanged,
accepts 05.09 and rejects 05.10. Local fix gate **421 passed**, Ruff/diff pass,
six unchanged historical Rasterio warnings; no GitHub CI claim.

The original `/workspace/aquasentinel-813` stays on
`feature/as-104-temporal-baseline` at the same base with all AS-104 changes intact.
Never stash, stage, reset, clean, switch, move, delete or edit it for this fix.
Decision 047 remains there; M19/E18–E19/EV-022–EV-023 are reserved there, while this
fix uses owner-approved M20/E20/EV-024. No original AS-104 docs are imported.
All earlier decisions/milestone/evidence records retain their historical wording.

Stop state: upstream fix uncommitted for review, no commit/push/PR/merge. AS-104
real acceptance BLOCKED until this fix is reviewed/merged and the unchanged
target/March period/minimum-five experiment separately rerun. Metadata success
does not prove XML, raster, water support, temporal acceptance or a hazard.
AS-105+ NOT authorized and NOT started.

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
