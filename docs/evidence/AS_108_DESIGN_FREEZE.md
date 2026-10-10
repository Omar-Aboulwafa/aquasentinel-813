# AS-108 M42 — Historical Validation Design Freeze

## Status and scope

**Decision 053 / M42 / E42 / EV-046: FINAL / FROZEN DESIGN — NOT EXECUTED.**
Prepared 10 October 2026 (Asia/Dubai). Documentation/policy only, no production
source/tests/config/dependency changes and no scientific validation outcome.
[Canonical methodology](../AS_108_HAB_HISTORICAL_VALIDATION.md) and
[machine-readable contract](AS_108_DESIGN_FREEZE.json) define future execution.
No Decision 054, PR or merge. AS-201 NOT STARTED.

## Official baseline and AS-107 closure

Verified origin/main: `14149113e58788621d6aef91f039b95781c67434`; PR #25 merge parents:
`2bfbbd63cb5fee8e1d18a0b1099335b924e5ed9d` and
`88189f5ed85767f5022fa8e6c8ceee55b42f6c85`.
AS-107 **COMPLETE / CLOSED**, M40 **COMPLETE / MERGED / PUBLICATION-CLOSEOUT**:
the merged branch's durable closure condition is effective. AS-108 remains P0
before AS-201 in the PRD. Isolated branch `docs/as-108-design-freeze`, clean at
base before edits, worktree `/workspace/aquasentinel-813-as108-m42`.

## Historical M41 and numbering

M41 read-only feasibility/source audit was owner-reviewed in chat; it made no
repository changes or design freeze. Seven accepted optical caches, five March
references, April 3 through AS-105 and April 28 through AS-107 were inventoried;
no accepted May processed scene/full May metadata inventory was available.
Six documentary request attempts failed with proxy403, including EAD's exact PDF;
no source passage was independently read by Codex. M41 recommended REVISE before
freeze and called out missing POST, causal PRE and source precision constraints.
Its EO metadata/assets/bytes/scientific calls were zero.

M42 authorization supplied independently verified official EAD listing/PDF facts
from outside Codex. This later resolution preserves M41's original blocker.
Journal continuity requires a historical entry for a meaningful audit, so unused
**M41/E41/EV-045** are now recorded retrospectively, explicitly not an M41 edit.
Unused **M42/E42/EV-046** identify this design freeze; no existing ID overwritten.
Decision 053 was absent before editing; it is the new design decision.

## External reference verification provenance

Publisher **Environment Agency – Abu Dhabi**; official category **Marine Water
Quality**; resource **Marine Water Quality Report 2023**; listing publication
**21 November 2024**. The reporting-year/publication-year distinction resolves
the earlier filename/citation ambiguity. [Official PDF](https://www.ead.gov.ae/-/media/Project/EAD/EAD/Documents/KnowledgeHub/Resources-and-Materials/MWQ-ANNUAL-REPORT-2024-EN.pdf).

The project owner supplied externally verified official EAD source facts in the
M42 authorization. The verification step occurred outside Codex; Codex did not
independently retrieve or inspect the source during M42. The repository records
the supplied verification facts and their stated limitations; it does not claim
that the project owner personally performed the external inspection.
Verification facts supplied on 10 October 2026 (Asia/Dubai). **No new documentary
request or independent report access in M42.** Exact outside access timestamp and
PDF page/heading not supplied; null in the event schema. Supplied statement summaries are not invented direct quotes.
EAD reports 23 Abu Dhabi algal bloom incidents in 2023, one Raha Beach Red Tide
incident in April, attributed to Pseudo-nitzschia multistriata; the report states
that species releases domoic acid. Incident-specific toxin measurement **NOT
ESTABLISHED**. Satellite species/toxin inference **NONE**.

## Frozen scientific and selection boundaries

Timing MONTH_LEVEL / April 2023; no exact onset/peak/sample/end/recovery day.
Lead time MONTH_LEVEL_ONLY, exact days early NOT ESTIMABLE. Location Raha Beach,
AREA_LEVEL_ONLY; analyst AOI relationship AREA_LEVEL_CONTEXTUAL_ALIGNMENT, not
incident/sampling/intake geometry or biological pixel truth.

PRE `[2023-03-01,2023-04-01)` is descriptive March 4/9/14/24/29 context, no
self-baseline scoring/negative labels. EVENT `[2023-04-01,2023-05-01)` retains both
April 3/28; highest accepted stage reported, no missing scores fabricated.
POST `[2023-05-01,2023-06-01)` is one future earliest metadata-eligible compatible
May attempt: same AOI, L2A, CDSE cloud<=30%, 40RBN/orbit20, exactly one PC05.09,
existing grid/upstream contract; complete metadata audit and ID freeze before pixels.
No fallback, no outcome-dependent date/threshold/AOI/weight/family/recurrence change.
A failed selected POST remains UNAVAILABLE; no invented recovery.

Primary unit one event_case; secondary acquisition/region/pixel support. Explicit
N_discovered/N_metadata_eligible/N_processing_attempted/N_evaluable/N_unavailable/
N_candidate_geometry/N_scored/N_watch_or_higher, query scope, reused/retained counts
and all scientific support denominators remain distinct; unknown/null and zero
handling frozen. CONSISTENT/PARTIALLY_CONSISTENT/INCONCLUSIVE/UNAVAILABLE definitions
are documented but **not applied** here. No biological accuracy, significance,
probability/confidence, safety or exact lead-time claim. Unmatched observational
anomaly is not automatically a false positive; a missing candidate is not a false
negative. Full criteria are in Decision 053/canonical methodology/JSON.

## Retrospective-validation semantics

April 3 and April 28 scientific outputs were already known before Decision 053.
AS-108 is therefore not blind, prospective, or independently pre-registered
validation of those April outputs. The observational-consistency categories are
frozen before any new May POST metadata selection or scientific processing; they
are reporting/interpretation rules for a retrospective case study. They MUST NOT
be presented as evidence of predictive validation, prospective detection
performance, independent model validation, or unbiased accuracy estimation.
The future May result MUST NOT be used to revise these categories. This
clarification changes no category criterion and computes or predicts no category.

## Immutable accepted April 28 reference

Product `hab_risk:113143700cb35ac9230d9c54b68b1b53e2573838a4913d4bc942e81c99903fdb`; input fingerprint `084790273118f50f6c8eaf0ed380dbce730c6dbbd7e4fa0f757c5d145e894d91`;
output fingerprint `25cccf8e8b550a76f28ebb01a2249060de5b1cd3114a7c531ef4775adbc87dae`. Score **29.52380952380953**, hex
`0x1.d861861861863p+4`, **Watch**, completeness/coverage **0.7/0.7**,
`provisional_observational_screening`, **Review on the next valid acquisition**,
A/B/C **7/7/0**. No same-pixel candidate recurrence was observed among the seven
target candidates with valid prior history; neither no HAB nor biological absence.
This is a historical reference, not a newly calculated validation result.

## Minimum scope and deadline protection

One reference, fixed phase windows, existing PRE and both EVENT records, immutable
Watch example, stage/evaluability inventory, one future attempted POST, preserved
missingness, denominator-aware qualified case summary and presentation limitations.
Deadline **11 October 2026 (Asia/Dubai)**. Stop at minimum defensible P0; protect
AS-201 oil work, demo, presentation and reproducibility. No secondary Fujairah,
P1 context, fitted ML, hyperspectral, multi-event accuracy or complex statistics.

## Preservation and engineering gates

Before editing: **134 tracked file hashes**, **44 protected external hashes**,
**57 modes** and exact safety-stash inventory snapshotted. Accepted AS-104/105/106/107
records, sealed bundles/caches/handoffs/recovery files and source/tests/config/
dependencies remain unchanged. No permissions rewritten or stashes applied/dropped.

| Frozen decision body | SHA-256 retained |
|---|---|
| Decision 050 | `d3623a363868a57609f50488679ad01ac9df0554b638c489731eab994ae04773` |
| Decision 051 | `4c279549a1c9bd132febcc6fe4cdbd53346cbf8c8cb98a08c3253eb453c02eea` |
| Decision 052 | `a871997701eb5c0069c848f55e45d7d15f2a2e606c712d68a60a1ee54b47cdf5` |

Accepted M39 MD hash: `344da2c7b9b1ee521dcde273b167a39d4e452f435dfe80036a8af196ff3b3f3f`.
Accepted M39 JSON hash: `dc97694a9fb1090e30add0d697431bfa9c1eaead783eed7a94050713967cd4c2`.
Both known safety stashes retained:
`f93950aab6fdfb40bb100158915ef12692aa1665` and
`d979a433a5ab8ae600282048f184eb5fd06a8f17`.

M42 engineering quality: **1285 full tests PASS (115.87s), six existing Rasterio PendingDeprecationWarnings; Ruff PASS; diff/new-file whitespace PASS**.
Diff/new-file whitespace/security/preservation: **PASS — only eight authorized docs/evidence paths; source/tests/config/dependencies, Decisions 050/051/052, accepted evidence, 44 external hashes, 57 modes and both safety stashes preserved; credential scan PASS**.
Repository tests use existing synthetic/local fixtures; no real EO science or
accepted-parent reconstruction. No GitHub CI success claim.
New documentary requests **0**, EO metadata requests **0**, EO assets/bytes **0**,
real scientific compute calls **0**. Administrative Git fetch/publication only.

## Publication and next authorization

Prepared on `docs/as-108-design-freeze` for owner review; commit/push is authorized,
PR/merge is separate. Decision 053 FINAL / FROZEN DESIGN — NOT EXECUTED.
Next after review and separate merge approval: separately authorize **AS-108 M43
metadata-only POST inventory/selection**; later pixels/validation require separate
execution authorization. No May observation selected, no case classification,
AS-201 NOT STARTED, no Decision 054, no future AS-105 policy study/P1 05.10.
