# AS-102 — Required PC Processing-Baseline Fix Validation

**Evidence:** EV-024; journal M20 / engineering E20; Decision 048.
**Date:** 8 October 2026 (Asia/Dubai).
**Status:** PASS for offline fix validation and metadata-only source resolution;
uncommitted, unpushed, unmerged, no PR. AS-104 real acceptance remains BLOCKED.
**Fix worktree:** `/workspace/aquasentinel-813-as102-baseline-fix`.
**Branch:** `fix/as-102-required-pc-baseline`.
**Fetched origin/main / base:** `c6accab2c5753734466a6375d1b3ce1762e99bed`.

## Existing Blocker and Scope

The preserved AS-104 real attempt stopped before reference XML/raster reads:
March 4 had two exact PC products, 05.09 and 05.10, and the unchanged AS-102
resolver required one. The subsequent metadata-only investigation (8 October,
13:18:59–13:19:55 UTC / 17:18:59–17:19:55 Asia/Dubai) found exactly one complete
05.09 product for each of March 4/9/14/24/29. April 28 remains the accepted target
at 05.09; all six CDSE discovery products are 05.10. No same-processing or pixel
equivalence between CDSE and PC is asserted.

The fix adds an optional explicit source-resolution constraint. All PC metadata
is validated before filtering; exact observation matching and exactly-one
cardinality remain mandatory. No earliest/latest/CDSE-generation preference or
fallback. The selector never enters cache identity or changes pixel processing.

## Offline Gate

Used existing Python 3.11.16 environment, not new dependencies. Tests run from the
fix worktree with its `src` on pytest's configured Python path:

```text
PYTHONDONTWRITEBYTECODE=1 /workspace/aquasentinel-813/.venv/bin/python -m pytest -v
PYTHONDONTWRITEBYTECODE=1 /workspace/aquasentinel-813/.venv/bin/python -m ruff check .
git diff --check
```

- Clean merged-main baseline: **348 passed**, six historical warnings.
- Fix gate: **421 passed** (348 retained + **73 added cases**), six same warnings.
- Ruff: passed. Diff check: passed. No new warning category.
- The six PendingDeprecationWarnings remain in Rasterio `windows.py:360/361`
  during the existing local-window/signed-read logger tests, about Affine `*`.
- No GitHub CI run or CI-success claim.

Added cases cover explicit 05.09/05.10 selection and input order, None ambiguity,
zero/multiple constrained matches, exact observation exclusions, malformed
metadata before filtering, invalid selector types/format before IO, all required
assets and unsafe URL/host/media rejection, resolver/optical propagation, known-ID
and ordinary cache constraint checks, discovery-candidate checking, same-product
identity/cache/provenance reuse, XML-baseline rejection and blocked access/writes
after resolution failure. Existing decoding/grid/mask/transport/provenance tests
remain unchanged and passing.

One initial new test changed only candidate cloud cover and incorrectly expected
a SourceRecord mismatch. Cloud cover is not in that existing SourceRecord
contract. The test was corrected to change discovery product identity; no
implementation behavior was broadened. Initial Ruff import-order findings were
fixed within the two authorized test files.

## Separate Offline Accepted-Cache Verification

Checked at `2026-10-08T13:38:25.845899+00:00` UTC /
`2026-10-08T17:38:25.845899+04:00` Asia/Dubai. This was local verified-cache
loading, separate from the metadata-only smoke; no pixel preprocessing ran.
The original accepted cache was read in place with signing/XML/raster/resolution
and cache-write entry points blocked. Nothing was copied or rewritten.

- Cache ID: `0725a908d21cd655e83f70d2bb11247dc0f1516f0c00ea275efc3239113ee4a6`.
- Product ID: `optical:0725a908d21cd655e83f70d2bb11247dc0f1516f0c00ea275efc3239113ee4a6`.
- Actual product: `S2B_MSIL2A_20230428T064629_R020_T40RBN_20230428T122311`.
- None and required 05.09: PASS, identical processing parameters and provenance.
- Required 05.10: explicit `ObservationMatchError`, no fallback.
- SHA-256 comparison of both cache files before/after: unchanged.
- Forbidden entry-point calls: **0**. No new cache or second identity created.

## Real Metadata-Only Resolver Smoke

**Start UTC:** `2026-10-08T13:38:26.730440+00:00`.
**End UTC:** `2026-10-08T13:38:48.970146+00:00`.
**Start Asia/Dubai:** `2026-10-08T17:38:26.730440+04:00`.
**End Asia/Dubai:** `2026-10-08T17:38:48.970146+04:00`.

Used the fix worktree's actual resolver, existing configured Al Raha AOI and
AS-101 discovery (**44 candidates**). Each predeclared observation had exactly
one corresponding CDSE candidate. Called `resolve_optical_source` with
`required_processing_baseline="05.09"`; the unchanged paginated PC search and
structured validation run before the new baseline filter.

| Exact acquisition UTC | Platform | Resolved actual PC product | PC generation UTC | Result |
|---|---|---|---|---|
| 2023-03-04T06:47:51.024Z | sentinel-2a | S2A_MSIL2A_20230304T064751_R020_T40RBN_20230304T113736 | 2023-03-04T11:37:36.492429Z | PASS |
| 2023-03-09T06:47:19.025Z | sentinel-2b | S2B_MSIL2A_20230309T064719_R020_T40RBN_20230309T121958 | 2023-03-09T12:19:58.419331Z | PASS |
| 2023-03-14T06:46:41.024Z | sentinel-2a | S2A_MSIL2A_20230314T064641_R020_T40RBN_20230314T123741 | 2023-03-14T12:37:41.653527Z | PASS |
| 2023-03-24T06:46:21.024Z | sentinel-2a | S2A_MSIL2A_20230324T064621_R020_T40RBN_20230324T114938 | 2023-03-24T11:49:38.144656Z | PASS |
| 2023-03-29T06:46:29.024Z | sentinel-2b | S2B_MSIL2A_20230329T064629_R020_T40RBN_20230329T132334 | 2023-03-29T13:23:34.143592Z | PASS |
| 2023-04-28T06:46:29.024Z | sentinel-2b | S2B_MSIL2A_20230428T064629_R020_T40RBN_20230428T122311 | 2023-04-28T12:23:11.362052Z | PASS |

All six resolved products: PC baseline **05.09**, MGRS **40RBN**, relative orbit
**20**, advertised EPSG **32640** and product type **S2MSI2A**. All eleven required
selected asset references pass existing unsigned host/media validation:
`B02/B03/B04/B05/B06/B07/B08/B8A/B11/SCL/product-metadata`.

The existing actual-PC SourceRecord pattern remains:
`stac:ef177b34b0fa3cabbb6d613d65f1c55d8ea4c5959326bb8896ec51d111792740:sentinel-2-l2a:<PC item ID>`.
Every result retains a distinct CDSE discovery SourceRecord and the provider's
product URI, granule/datatake/datastrip identifiers and orbit state. Discovery
processing context is independently retained:

| Acquisition date | CDSE discovery product | Encoded baseline | Encoded generation UTC |
|---|---|---|---|
| March 4 | S2A_MSIL2A_20230304T064751_N0510_R020_T40RBN_20240819T072511 | 05.10 | 2024-08-19T07:25:11Z |
| March 9 | S2B_MSIL2A_20230309T064719_N0510_R020_T40RBN_20240823T054455 | 05.10 | 2024-08-23T05:44:55Z |
| March 14 | S2A_MSIL2A_20230314T064641_N0510_R020_T40RBN_20240823T041506 | 05.10 | 2024-08-23T04:15:06Z |
| March 24 | S2A_MSIL2A_20230324T064621_N0510_R020_T40RBN_20240824T014318 | 05.10 | 2024-08-24T01:43:18Z |
| March 29 | S2B_MSIL2A_20230329T064629_N0510_R020_T40RBN_20240823T165234 | 05.10 | 2024-08-23T16:52:34Z |
| April 28 | S2B_MSIL2A_20230428T064629_N0510_R020_T40RBN_20240831T052931 | 05.10 | 2024-08-31T05:29:31Z |

Smoke guards blocked signing, asset byte/XML access/parsing, raster reads/opens,
preprocessing and cache load/write entry points. Forbidden calls: **0**. The fix
worktree's configured cache directory remained absent. No tokens or signed URLs
were generated/persisted, no imagery downloaded, and no AS-103/104 output produced.

## Preservation / Historical Coordination

Original branch `feature/as-104-temporal-baseline`, original HEAD
`c6accab2c5753734466a6375d1b3ce1762e99bed`, and its uncommitted files are preserved.
Pre/post SHA-256 comparison verified all **81 tracked/non-ignored untracked
files unchanged**, with no additions/deletions and the original branch/HEAD/status
unchanged. No original-worktree test, formatter, stage, stash, reset, clean,
branch switch or implementation edit.
All previous decisions, M01–M18, E01–E17 and EV-001–EV-021 remain historical.
Per owner clarification, Decision 047 and M19/E18–E19/EV-022–EV-023 stay only in
the preserved AS-104 worktree; this fix reserves their numbers without copying.

## Limits / Stop State

Six successful resolutions prove disambiguation only, not March XML decoding,
raster readability, compatible measured native grids, valid-water history or
AS-104 acceptance. Five catalog observations do not establish five supported
observations at a pixel. No HAB, chlorophyll concentration, species/toxins, water
safety, operational risk or lead-time evidence. No GitHub CI claim.

The fix awaits review/merge. AS-104 remains uncommitted/preserved and real
acceptance BLOCKED until this fix is reviewed/merged and that experiment is
separately rerun. No AS-104 work was resumed. AS-105+ NOT authorized/NOT started.
No commit, push, PR or merge occurred.
