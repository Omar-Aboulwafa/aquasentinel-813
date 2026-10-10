# AS-107 M38 — Offline Implementation / Synthetic-Adversarial Validation

## Scope, authority and baseline

10 October 2026 (Asia/Dubai). M38 / E38 / EV-042:
**IMPLEMENTED / SYNTHETIC-ADVERSARIAL VALIDATION PASS.**
Owner authorization is M38 only. Decision 052 FINAL / FROZEN / MERGED through
PR #22: `49f5276b1ad372725b21cdb2085815225c98eed4`, parents
`6b22d32f078ef80158b2f2d7aac4f3dd07925038` and
`5430383611437e939cebce89608c001889eea487`. Fetched and verified exactly.
Clean isolated branch `feature/as-107-hab-risk`, worktree
`/workspace/aquasentinel-813-as107-m38`, starts directly at that official main.
AS-106 COMPLETE / CLOSED. No Decision 053; frozen Decisions 050/051/052 unchanged.

## Implementation and scientific boundary

Four focused production modules: risk/__init__.py, models.py, policy.py, scoring.py.
Strict five-name finite/nonbool/nonnegative/total/mandatory weight validation;
canonical raw/normalized metadata and strict integer-max band validation at the
risk boundary, without altering the generic configuration loader/schema/values.
Exact typed witnesses and full AS-105/106 parent validation before any score.
Regional masks provide integer family a/v; spectral/red-edge pooled breadth;
regional persistence C/B with B=0 unavailable. Existing F1 OR counts once.
Context/exposure are None/not_implemented, zero effective weight/None contribution,
empty source IDs, no provider hooks. Mandatory components have no fallback.
Frozen binary64/fsum available-weight score and coverage; minimum-factor
evidence_completeness with all numerators/denominators; no secondary AS-104 penalty.
Separate raw band/completeness/flags/recommendations; no clipping/epsilon/tuning.
All regions retained, including one-pixel limits; maximum-region site with frozen
ties and together-copied evidence. Empty sites preserve evaluability and exact frozen
no-candidates wording, never zero/Normal/safety. Overlap and provisional qualification
are explicit in policy, region/site outputs, diagnostics and limitations.

Frozen/slotted scientific records/canonical tuples, defensive independent mutable
metadata copies. No risk raster/cache/writer/new dependency. Immediate provenance
is (target AS-105 geometry ID, AS-106 persistence ID); AS-104 typed witnesses remain
integrity-only. Parent/regional IDs and geometry summary references remain authoritative.
as107-v1/hab_risk identity, as107-input-v1 consumed masks/counts/timing and
as107-output-v1 all output semantics use framed SHA-256, exact binary64 float
encoding, stable credential guards and fixed UTC/order/null semantics.
Creation timestamp/display/publication excluded. validate regenerates from full
authoritative parents + external policy, comparing semantics, fingerprints, ID,
parameters and provenance; attacker-updated local hashes do not confer validity.

No accepted real AS-105/106 objects, cache rasters or scientific arrays loaded for
risk, no real denominators/components/completeness/score/band or predicted outcome.
All scoring in M38 tests is synthetic. No EO/data/raster/XML/signing/catalog request,
real upstream rerun, threshold selection, context/exposure implementation or AS-108.
Only Git fetch/push use network. Existing tests' synthetic parent generation and
required internal integrity regeneration are separate from real processing.

## Actual validation — performed in this M38 worktree

- Focused `python -m pytest tests/risk -v`: **292 passed**, **44.93s**, no warnings.
- Full `python -m pytest -v`: **1285 passed**, **6 existing Rasterio
  PendingDeprecationWarnings**, **117.57s**. Actual run, not copied M37 baseline.
- `python -m ruff check .`: **PASS**, all checks passed.
- `git diff --check` plus every new file's whitespace and staged diff: **PASS**.
- Existing Python 3.11 environment with this worktree's src path; pytest/Ruff cache
  and bytecode writes disabled. No dependency installation/configuration change.
- Local engineering checks only; no GitHub CI-success or real-science claim.

## Synthetic and adversarial coverage

tests/risk/test_policy.py: strict weights/types/total/positive mandatory/names,
continuous integer-max bands, all frozen score boundaries and immediate nextafter
neighbours, display-rounding independence, missing mandatory/zero score/zero coverage,
all-five synthetic arithmetic kernel only, invalid components and exact completeness flags.
test_scoring.py: three components, integer opportunities/F1 vote pooling, reconstructable
driver arithmetic, B=0 and partial B/A, regional availability, empty/evaluable versus
empty/unevaluable, one/multiple regions, maximum/ties, recommendations and High with
low completeness preserving band. No invalid zero-evidence candidate fabricated.
test_identity_lineage.py: creation-time exclusion, reordered maps/sequence/generator,
consumed-bit/time/count fingerprints, unconsumed evidence exclusion, valid family
change with equal pooled score but different identity, recursive PC→102→103→104→105→106→107
lineage, full validator calls, incompatible/missing witnesses, parent tamper with
stale/recomputed local hashes, no IO/network/cache/registry/public extraction and
parent snapshots/non-aliasing. Synthetic upstream fixtures reused unchanged.
test_models.py: frozen models/defensive metadata copies, semantic region/driver/factor/
site/statistics/diagnostic/policy tamper (including rehashed local output/parameters/IDs),
numeric types/finite rules/canonical containers, PC/AS104 shortcuts, recommendation
policy tamper and synthetic credential URL rejection without echo.

## Preservation and publication

Pre-edit snapshot: 119 tracked-file hashes, Decisions 050/051/052 full-section hashes,
41 protected external-file hashes, 53 permission records and exact stash inventory.
Preservation audit PASS: existing source/tests/config/dependencies and accepted
AS-105/106 evidence byte-identical; six pre-existing docs receive additions and
historical-header labels only. Scientific/policy bodies of all three decisions
byte-identical. No scientific product/data/cache/generated artifact committed.
Both historical safety stashes retained unchanged:
`f93950aab6fdfb40bb100158915ef12692aa1665` and
`d979a433a5ab8ae600282048f184eb5fd06a8f17`.
All protected external hashes/modes and recovery material unchanged. Stable-metadata
credential scan PASS; credential-shaped URL tests contain explicitly synthetic
example.test values only, never a live token/secret or signed real href.

M36/M37 and their earlier evidence bodies remain historical. M38/E38/EV-042 is
engineering implementation/validation only; no new architectural/scientific Decision.
Owner-authorized feature publication: `feat: implement AS-107 HAB risk scoring`,
pushed to origin/feature/as-107-hab-risk for review after all gates. Exact commit SHA,
remote equality/upstream and clean status verified through Git and final task report;
not embedded in its own commit. No PR/merge. M39 real acceptance and M40 closeout
require separate owner authorization and remain NOT STARTED. No expected real risk
outcome recorded. AS-108 NOT STARTED; future AS-105 policy validation NOT RUN;
P1 homogeneous 05.10 robustness NOT STARTED.
