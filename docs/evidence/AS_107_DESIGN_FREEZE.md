# AS-107 M36 / M37 — Audit Record and Owner-Approved Design Freeze

## Scope and baseline

**Date:** 10 October 2026 (Asia/Dubai).
**M37 / E37 / EV-041: FINAL / FROZEN DESIGN — NOT IMPLEMENTED.**
Documentation/policy only; no real HAB risk score, AS-107 scientific product,
production module, source/test/config change, AS-108 or context/exposure work.
Official main/base `6b22d32f078ef80158b2f2d7aac4f3dd07925038`: verified fetched
PR #21 merge subject, with parents `82e30c00a30ed893ad47c44c5a1e363661370d35`
and `872604eb25ec190b63fb0b8018ff7ba0c6b3cc8c`. AS-106 COMPLETE / CLOSED.
Clean isolated worktree `/workspace/aquasentinel-813-as107-m37`, branch
`docs/as-107-design-freeze`, created directly from that origin/main.

## M36 / E36 / EV-040 — prior read-only audit COMPLETE

Recorded retrospectively from the completed owner-reviewed M36 design audit and
M37 authorization, not a new M36 experiment. Existing config supplies five weights
and bands; no production risk/scoring module. AS-105 masks/labels provide regional
family availability/evidence; AS-106 provides regional recurrence/history/timing.
AS-104 remains a typed integrity witness, not a direct scoring parent. Audit
recommended explicit missing semantics, pooled family-pixel denominators,
reconstructable explanations and qualified completeness before freeze.
No real score was calculated and no outcome-selected formula was compared.

## M37 / E37 / EV-041 — frozen policy

[Decision 052](../DECISIONS.md#decision-052--as-107-explainable-availability-aware-hab-risk-and-evidence-completeness)
and [AS-107 contract](../AS_107_HAB_RISK.md) freeze the owner's policy before real
scoring. Primary field evidence_completeness; assessment_status
provisional_observational_screening. Existing raw weights unchanged; all component
formulas, renormalization, coverage, integer denominators, B=0/zero-region semantics,
overlap disclosure, continuous bands, 0.50 administrative interpretation flag,
region/site/driver ordering, recommendations, witnesses/lineage/fingerprints,
numeric serialization and future test/acceptance boundaries are documented.
Future M38 implementation, M39 real acceptance and M40 publication NOT STARTED.
Decision 052 is FINAL/FROZEN DESIGN/NOT IMPLEMENTED; design publication is separate
from implementation authorization. No expected real score or band is recorded.

## Numbering and historical preservation

Repository maximum before edits was M35/E35/EV-039. Use M36/E36/EV-040 for prior
audit and M37/E37/EV-041 for freeze; reserve M38/E38/EV-042, M39/E39/EV-043 and
M40/E40/EV-044 only. No future execution evidence is claimed.
Earlier M01–M35/E01–E35/EV-001–EV-039 bodies and dated statuses stay historical.
Old M35 current headers in continuity files are relabelled pre-PR #21 historical;
accepted AS-105/106 evidence and contracts untouched. Decisions 050/051 sections
verified byte-identical; Decision 052 is appended separately.

## Preservation and credential boundary

Before edits: 117 tracked-file hashes, 41 protected external-file hashes, 53 modes
and exact stash inventory recorded outside Git. Accepted caches, sealed handoffs,
M29/M33/M34 bundles and recovery artifacts are read/hash-checked only; no array
loading/reconstruction, score estimation or numeric outcome prediction.
Safety stashes retained untouched: f93950aab6fdfb40bb100158915ef12692aa1665 and
d979a433a5ab8ae600282048f184eb5fd06a8f17. No secrets/signed URLs/credentials added.

## M37 actual engineering quality gates

- Full `python -m pytest -v` actually rerun in the M37 worktree: **993 passed,
  6 existing Rasterio PendingDeprecationWarnings**, 62.32 seconds.
- `python -m ruff check .`: **PASS**, all checks passed.
- `git diff --check` and separate checks for both new Markdown files: **PASS**.
- Authorized paths only: seven documentation files. All 112 other tracked files
  hash-identical, including 37 source files, 40 tests, configuration and dependencies.
- Historical-content audit: additions only except explicit historical M35 header
  relabelling; all earlier checkpoint bodies retained. Decisions 050/051 verified
  byte-identical, with unchanged section hashes (trailing blank lines normalized):
  050 `ab1c196a8e204e6c81784ae7de9083b2fa5cd6d295d68fa74742e95c4aa9ce26`;
  051 `f3f79a2f85ca3fb33e70518fedbf59f7946932fbc2cec1dae4ebed9a0a05a36b`.
- All 41 protected external-file hashes, 53 modes and exact stash inventory:
  **PASS / UNCHANGED**. No production risk module; credential-pattern scan of
  additions **PASS**, no signed URLs/tokens/private keys. New document file links PASS.

This actual regression run is distinct from the previously recorded historical
993-test baseline. Existing tests verify regression baseline, not unimplemented
AS-107 code/science. Gates used the existing Python 3.11 environment, this
worktree's src path and disabled pytest/Ruff caches; no dependency installation.
Only Git fetch and final branch push use network; scientific/EO/metadata/raster/
signing requests and downloads are zero. No real parent validator/EO processing
or scientific product reconstruction is run by M37; authorized existing pytest
synthetic engineering validation is distinct from real execution.

## Publication and stop

After passing gates, commit docs only: `docs: freeze AS-107 risk policy`; push
origin/docs/as-107-design-freeze with upstream tracking. No PR/merge performed.
Owner review and separately authorized design PR/merge precede M38 authorization.
No AS-107 implementation or real score; AS-108 NOT STARTED; future AS-105 policy
validation NOT RUN; P1 homogeneous 05.10 robustness NOT STARTED.
