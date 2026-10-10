# AS-201 M50 — STAC Geometry Boundary Interoperability Correction

## Scope and baseline

**M50 / E50 / EV-054: OFFLINE INTEROPERABILITY CORRECTION COMPLETE.**
This is an engineering correction, not a scientific decision or live-readiness gate.
M50/E50/EV-054 were confirmed unused before allocation. Decision 055 remains absent.

Official main `29b7b46edc877a50645865aad4a1e9f62d34d6f5` is the PR #31 merge, with parents
`392603b5b074d515eb6c137e33395c7f0b1256ac` and
`3481c89ec77fc30330d1110397ae39b15daf964c`. The fresh branch
`fix/as-201-stac-geometry-boundary` was created from that exact clean baseline.
Prepared 11 October 2026 (Asia/Dubai); existing Python 3.11 environment reused.

## Localized cause and minimal correction

M49 localization established that Client.open, get_collection and collection.license
pass. At `client.search(...)`, pystac-client 0.9.0 deep-copies the `intersects`
dictionary. Reconstructing AquaSentinel's FrozenJSON invokes its mutation guard:
`TypeError: AS-201 metadata is immutable.` PySTAC is 1.15.2. This is an internal
client-boundary interoperability defect, not a provider metadata defect.

Only `src/aquasentinel/ingestion/sentinel1_resolver.py` changes in production.
Immediately before the two provider searches, it creates independent ordinary JSON:

```python
geometry = json.loads(json.dumps(ENVELOPE_GEOMETRY, allow_nan=False))
```

Both CDSE and PC searches receive this built-in dict with list coordinate containers.
No FrozenJSON, tuples or mutable aliases to the frozen policy remain in the boundary
object. Finite JSON serialization preserves the exact Polygon ring:
[49.60,28.60], [50.70,28.60], [50.70,29.60], [49.60,29.60], [49.60,28.60].
The internal policy remains immutable. No change to FrozenJSON, shared STAC,
Sentinel-2, provider/source selection, dependencies or Decision 054 semantics.

## Offline proof

Two new tests in `tests/ingestion/test_sentinel1_contract.py`:

1. Recursively assert exact built-in dict/list/scalar types, no FrozenJSON or tuple,
   exact geometry, both provider boundaries, and no optical cloud query. Mutate the
   boundary copy and prove the frozen source unchanged; root and nested policy
   mutation still raise TypeError.
2. Reproduce the original TypeError through the real Client.search constructor with
   synthetic root metadata. Then run the corrected public search with real
   pystac-client construction/deepcopy, collection parsing, shared IO and pagination.
   Only HTTP responses are replaced. Three pages per provider resolve all six
   synthetic slots; both providers retain the exact envelope and no cloud query.

This proves the previously failing offline construction path, not live availability.

## Actual engineering gates

- Focused SAR/non-optical suite: **136 passed**.
- Full repository `python -m pytest -v`: **1434 passed**, six existing Rasterio
  PendingDeprecationWarnings. Existing Sentinel-2 tests are unchanged and pass.
- `python -m ruff check .`: PASS.
- `git diff --check` and new-file whitespace: PASS.
- Strict finite JSON, independent semantic-digest reconstruction/repeat: PASS.
- Added-content credential/signed-URL scan: PASS. Existing synthetic hostile URL
  fixtures remain test inputs, not live credentials.
- Changed-path and preservation audits: PASS; no GitHub CI success claim.

## Historical and external preservation

M49 [MD](AS_201_LIVE_ACCEPTANCE.md) and [JSON](AS_201_LIVE_ACCEPTANCE.json) are
**byte-identical**. Its original **AS201_LIVE_ACCEPTANCE = FAIL** and later failure
localization remain valid historical evidence. This correction does not relabel
that run PASS. Full M49 live acceptance has **not** been retried.

The entire Decisions file (including frozen bodies 050–054), policy module,
shared catalog, optical production, configuration/dependencies and all prior
accepted evidence files except the continuity index are byte-identical. No upstream
scientific artifact, cache format, envelope/source identity or threshold changes.

Protected external files: **44/44 SHA-256 unchanged**; **57/57 modes unchanged**.
All three stash inventory entries are unchanged, including historical safety stashes
`f93950aab6fdfb40bb100158915ef12692aa1665` and
`d979a433a5ab8ae600282048f184eb5fd06a8f17`, and recovery stash
`d128ae2a00e61e28db274f682666e21361a69efb`.
Existing external recovery artifacts remain available; no scientific cache created.

## Accounting, digest and next authorization

Provider/CDSE/PC/signing/TIFF/XML requests: **0 each**.
SAR pixel reads/bytes: **0/0**. Scientific SAR compute calls: **0**.
Synthetic metadata engineering tests are not real provider access or SAR science.
No calibration, noise correction, dB, reprojection, mosaicking, filtering or detection.

Schema: **as201-m50-stac-geometry-boundary-v1**.
Semantic SHA-256: **`a9df1d3507b347113036ef82edc5a9909d46c47d2cb9ed53591d8baf897a7004`**.
Canonicalization: JSON `semantic` only; sorted keys, compact separators, UTF-8,
ensure_ascii=false, allow_nan=false, stable array order. No new commit SHA,
creation/request timestamp, signed URL or pixel value enters the digest.
See [EV-054 JSON](AS_201_STAC_GEOMETRY_BOUNDARY_FIX.json).

Next: owner review → separately authorized fix PR/merge → separately authorized
controlled M49 live acceptance retry. No PR, merge or live retry in M50.
**AS-202 NOT STARTED; Decision 055 ABSENT.** No live-readiness claim.
