# AS-102 — Explicit Required Planetary Computer Baseline Fix

## Task

Decision 048 upstream source-resolution fix, explicitly authorized on 8 October
2026 (Asia/Dubai). Worktree `/workspace/aquasentinel-813-as102-baseline-fix`, branch
`fix/as-102-required-pc-baseline`, base
`c6accab2c5753734466a6375d1b3ce1762e99bed`. This plan exists before source edits.
The original uncommitted AS-104 worktree must remain byte-for-byte preserved.

## Goal

Allow a caller to require a specific delivered PC processing baseline for an
exact Sentinel-2 observation, retaining deterministic exactly-one resolution.

## Existing Blocker

AS-104 real acceptance stopped before reference XML/raster reads because the
March 4 observation has two exact PC products, at baselines 05.09 and 05.10.
The later metadata investigation found exactly one complete 05.09 product for
each of the five frozen March observations. The accepted April target is 05.09;
CDSE discovery products are 05.10. Do not conflate acquisition and processing.

## Inputs

Existing CDSE candidate, configured AOI/optical settings and optional explicit
`required_processing_baseline: str | None`. Known-cache reload remains supported.

## Outputs

Existing `ResolvedOpticalSource` / `PreprocessedOpticalScene`, or explicit
`ObservationMatchError` on invalid constraint or zero/multiple remaining products.
New offline tests and metadata-only six-observation validation evidence.

## Exact API Changes

Add keyword-only `required_processing_baseline: str | None = None` to
`match_and_resolve`, `resolve_optical_source`, and `preprocess_optical_scene`.
Validate None or exactly the existing NN.NN baseline format before external
resolution, cache loading/return or access. Validate every returned PC item's
structured metadata first; collect exact acquisition/platform/tile/orbit matches;
apply the optional baseline constraint; require exactly one remaining product.
Check the recorded actual baseline on every cache-return path.

## Files Likely to Change

Only these eleven authorized paths:

- `src/aquasentinel/ingestion/sentinel2_assets.py`
- `src/aquasentinel/preprocessing/optical.py`
- `tests/preprocessing/test_assets.py`
- `tests/preprocessing/test_optical_cache.py`
- `docs/AS_102_REQUIRED_PC_BASELINE_FIX.md`
- `docs/evidence/AS_102_REQUIRED_PC_BASELINE_FIX_VALIDATION.md`
- `docs/DECISIONS.md`
- `docs/PROJECT_STATE.md`
- `docs/HANDOFF.md`
- `docs/PRESENTATION_JOURNAL.md`
- `docs/evidence/PRESENTATION_EVIDENCE_INDEX.md`

## No Dependency, Configuration or Cache-Schema Changes

Reuse the installed Python 3.11 environment with the fix worktree's `src` on the
import path. No dependency installation, TOML selector, cache-schema change,
generic provenance change, decoding/grid/mask/transport change or AS-103 change.

## Acceptance Criteria

- Explicit 05.09 and 05.10 select their unique exact products independent of order.
- None retains current ambiguity failure; zero/multiple constrained matches fail.
- Malformed selector/PC metadata and unsafe/missing assets remain rejected.
- Known-cache and ordinary cache returns satisfy the supplied constraint.
- Existing candidate/AOI/grid/cache validation remains intact.
- Same actual product means identical cache/product identity and provenance.
- Resolution failure performs no signing, XML/raster reads or cache writes.
- All 348 merged-main tests and added offline cases pass; Ruff/diff checks pass.
- Only after offline gates, all five March products and April target resolve at
  05.09 using real metadata, with asset access/preprocessing/writes prohibited.

## Backward Compatibility

Existing calls without the selector retain exactly-one observation semantics.
Old manifests are read without modification; no new identity field or second
cache key is introduced. A matching selector permits normal cache reuse; a
conflicting selector fails explicitly, including known-ID offline reload.

## Provenance / Identity Impact

The selector is a source-resolution constraint, not pixel processing. Existing
identity/provenance already records the actual PC source, baseline, generation,
provider metadata and unsigned assets. Preserve separate CDSE discovery context.
Do not persist the selector as another identity dimension or mutate old provenance.

## Validation

Run in this fix worktree: `python -m pytest -v`, `python -m ruff check .`,
`git diff --check`, name/status/stat inspection. Baseline is 348, not AS-104's
uncommitted 460. Then metadata-only resolver smoke on March 4/9/14/24/29 and
April 28, exact tile 40RBN/orbit 20/platform/acquisition, required baseline 05.09.
Block signing/XML/raster/cache-write entry points during smoke. Separately compare
original AS-104 file hashes and branch/HEAD/status without running tests there.

## Scientific / Operational Guardrails

Do not widen reference dates, reduce minimum five, change target, mix delivered
baselines, choose by feature values or prefer generation order. Source resolution
does not establish XML coefficients, raster readability, usable water support,
AS-104 real acceptance, HAB presence, chlorophyll, toxins, species, water safety,
operational risk or lead time. Preserve all historical evidence and decisions.

## Non-Goals

AS-104 implementation/acceptance rerun, AS-105+, imagery or XML retrieval, new
caches, upstream algorithms/refactoring, commits, pushes, PRs or merges.

## Rollback / Failure Behavior

Leave the fix uncommitted in its separate worktree for review. No fallback for
zero/multiple products; no writes on resolution failure. If base moves before
starting or another file becomes necessary, stop and report. Never stash, reset,
clean, switch, stage, move, delete or alter the original AS-104 worktree.

## Execution Status

Source/tests implemented only in the separate fix worktree. Merged baseline
348 passed; fix gate **421 passed** (73 new), Ruff/diff pass, same six historical
Rasterio warnings. Six real metadata resolutions at required 05.09 passed with
all access/write guards untouched. Separate accepted-April-cache offline check
preserved file hashes, parameters, provenance and identity; 05.10 was rejected.
Decision 047 stays in the original AS-104 worktree per owner clarification;
M19/E18–E19/EV-022–EV-023 stay reserved there, M20/E20/EV-024 identify this fix.
See [evidence](evidence/AS_102_REQUIRED_PC_BASELINE_FIX_VALIDATION.md).
Uncommitted/unpushed/unmerged, no PR. AS-104 preserved and real acceptance still
BLOCKED pending upstream review/merge and separate rerun; AS-105+ unstarted.
