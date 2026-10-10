# AS-106 — M31 Offline Persistence Engineering Validation

**Date:** 10 October 2026 (Asia/Dubai).
**Checkpoint:** M31 / E31 / EV-035 — OFFLINE IMPLEMENTATION + SYNTHETIC/ADVERSARIAL PASS.
**Base:** `57185444f0cc963cc899a25cd8179d7a31f12119` (PR #16 Decision 051 merge).
**Branch:** `feature/as-106-persistence`.
**Scope:** Synthetic/adversarial only; no real artifacts consumed for recurrence.
Decision 051 scientific body is frozen and unchanged; no Decision 052.
Feature publication authorized; owner review is next. No PR or merge in this task.

## Actual quality results

| Gate | Actual result |
|---|---|
| `python -m pytest tests/persistence -v` | 190 passed in 32.44 s; no warnings |
| `python -m pytest -v` | 993 passed in 61.10 s; all 803 retained tests pass |
| Warnings | Six existing Rasterio PendingDeprecationWarnings only; no new warnings |
| `python -m ruff check .` | PASS |
| `git diff --check` and new-file whitespace checks | PASS |
| Upstream tracked file / external hash / mode preservation | PASS |
| EO/data/service network attempts | 0 |
| Imagery/data download / real EO processing | NONE |

Tests used the existing Python 3.11 virtual environment, the isolated worktree's
`src` on PYTHONPATH, bytecode disabled and pytest/Ruff caches disabled. No package
installation or dependency/configuration change. Local checks are not GitHub CI.

## Synthetic/adversarial coverage

| Test file | Evidence covered |
|---|---|
| `tests/persistence/test_recurrence.py` | Singleton/no history, supported candidates, UNKNOWN skips, noncandidate breaks, all-prior counts, unsupported/noncandidate targets, three-date/multiple-gap streaks; exact/adjacent/diagonal pixels; A/B/C/Q, partial/empty denominators, histogram; long/subsecond gaps/sentinels; uint32/int64 legal boundaries and rejection; twelve seeded scalar-oracle sequences |
| `tests/persistence/test_models.py` | Empty/missing/duplicate/future/naive-time/typed sequence checks; missing/wrong witnesses; unchanged AS-105 validation; every projected comparison field and individually valid incompatible temporal contexts; every output array dtype/shape/tamper; metadata/summary/prior-evidence/provenance and rehashed tamper; typed region records |
| `tests/persistence/test_identity_lineage.py` | Caller permutation/UTC normalization/repeat; created_at exclusion; consumed mutations and unconsumed invariance; canonical layout/endian boundary; legitimate parent ID changes despite equal consumed masks; every AS-105 validator invoked; recursive PC→AS-102→AS-103→AS-104→AS-105→AS-106 lineage; immutable arrays/metadata/provenance and no aliasing; strict no-file/network/cache/upstream-extractor guards |
| `tests/persistence/test_regions.py` | Independent target-region counts and prior support/overlap; unchanged region IDs/order/geometry, zero-recurrence/history regions retained; exact partial fractions; half-microsecond median and overflow-safe integer midpoint |

All scientific output arrays, retained masks/labels, typed global statistics and
region/prior-date summaries are covered by `as106-output-v1`. Parent-aware
validation regenerates expected science; updating the stored fingerprint and
provenance parameters does not hide tampering. No generic registry mutation.
Existing AS-105 internal regeneration is explicitly permitted INTEGRITY VERIFICATION;
public extraction functions remain guarded/prohibited during the AS-106 API call.

Twelve seeded synthetic sequences each contain seven dates over a 2×3 grid.
Independent scalar calculations verify count, Q, streak, recurrence, previous-
valid gap and streak span at all six pixels: 72 pixel histories checked. These
are constructed inputs, not observational or accuracy evidence.

## Reproducible synthetic example — NOT REAL EO

The default two-date synthetic fixture has a 2×3 grid with all six pixels supported
and candidate at both dates. Acquisition labels are synthetic test timestamps.

- Product: `hab_persistence:dffe3e8466ca81022d5282759e97d66506bf84a96e8f9fbde0e5fef3b25e4542`.
- Input format `as106-input-v1`; digest `a191c885c44d83e33581a6752dd34be6927e631fad13f88c52531ff26241fa15`.
- Output format `as106-output-v1`; digest `a755cf9826eb05d5528427f6c690d8c4a37f877b7bb49ecb209739a9f60c6cf6`.
- A/B/C = 6/6/6; candidate-history coverage = 1.0; recurrence fraction = 1.0;
  histogram on A = {"2": 6}. These are engineering fixture values only.
- Caller permutation and deterministic repeat preserve identity and output.
- Exact regional span median example [1 µs, 2 µs] is numerator 3 / denominator 2.

No recurrence map/result is produced from accepted April 28 or any real April sequence.
No real handoff reconstruction or new-date upstream processing was performed.

## Preservation and security

Existing tracked sources/tests/config/dependencies/provenance/cache code are
byte-identical to base. Accepted AS-104 handoff (3 files), AS-105 M29 bundle
(4 files), twelve accepted AS-102 cache files and thirteen external recovery
artifacts retain their hashes; protected directory/file modes are unchanged.
Both safety stashes remain available and untouched:
`f93950aab6fdfb40bb100158915ef12692aa1665` and
`d979a433a5ab8ae600282048f184eb5fd06a8f17`.
Decision 051 and earlier historical decision/milestone/evidence bodies are
preserved. Changed files contain no live SAS tokens, credential-bearing URLs,
passwords/private keys or generated raster/cache data. Exactly 16 authorized paths.

## Scientific boundary and next authorization

This establishes deterministic offline recurrence engineering only. It does NOT
establish continuous biological persistence, HAB/bloom confirmation, biological
bloom duration, chlorophyll, species/toxins, biological causation, sensitivity/
specificity/accuracy/false-positive rate, risk/confidence, exposure, water safety,
alerts or warning lead time. Exact-pixel motion limitation and observation gaps
remain visible; shared March references are not independent confirmation.

Real AS-106 acceptance: NOT RUN / BLOCKED ON FUTURE DATA PREPARATION.
No verified earlier-April cache; eligible acquisition inventory remains unknown.
REAL APRIL SEQUENCE PREPARATION: NOT STARTED.
M32 / E32 / EV-036 metadata-only inventory: NOT STARTED.
M33 / E33 / EV-037 upstream preparation: NOT STARTED.
M34 / E34 / EV-038 offline real acceptance: NOT STARTED.
M35 / E35 / EV-039 publication/closeout: NOT STARTED.
AS-107+: NOT STARTED. Future AS-105 policy validation: NOT RUN.
P1 05.10 robustness: NOT STARTED. Owner M31 feature review is the next step.
