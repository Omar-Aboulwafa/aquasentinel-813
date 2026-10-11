# AS-201 M52 — CDSE Sentinel-1 Product-Type Interoperability Correction

## Status, lineage and execution plan

**M52 / E52 / EV-056: OFFLINE PRODUCT-TYPE INTEROPERABILITY CORRECTION PASS.**
Official main `e137795686d8f97bbd8ba6bc0465616783586ae0` is PR #32's merge, parents
`29b7b46edc877a50645865aad4a1e9f62d34d6f5` and
`43dafb556ee8583ca57d46c07a9d93ba45adbc94`.
Fresh branch `fix/as-201-cdse-product-type-normalization` starts from the exact M51 FAIL evidence commit
`8b32ec53e052d1ca6472bcf0fd442d9102b8669f`, whose sole parent is that official main. M51 changes only its six
reviewed documentation/evidence paths. Future PR history retains that evidence
commit followed by this correction; neither prior commit nor validation branch is rewritten.
M52/E52/EV-056 were confirmed unused; Decision 055 remains absent.

**Task/goal:** accept the exact official CDSE product representation without
loosening the frozen IW GRDH Level-1 source contract.
**Inputs:** merged Decision 054; immutable M51 metadata/failure evidence; externally
verified official CDSE fact supplied by owner authorization; existing synthetic fixtures.
**Outputs/files:** minimal resolver membership correction, focused regressions in
`tests/ingestion/test_sentinel1_contract.py`, this MD/JSON evidence and four continuity/index files.
**Dependencies:** none added, removed or upgraded; existing environment reused.
**Acceptance:** all six exact synthetic CDSE sources normalize; existing PC GRD/GRDH
behavior preserved; wrong types and conflicting higher-priority fields rejected;
all source/time/mode/orbit/polarization/cardinality guards preserved; offline gates pass.
**Risks/guardrails:** this changes metadata interoperability only, not SAR science;
provider access/header/XML readiness still unproved. No source substitution or fallback.
**Validation:** focused SAR/non-optical tests, full pytest, Ruff, whitespace, finite
JSON, independent digest repeat, credential scan and protected hash/mode/stash audit.
**Non-goals:** live retry, any provider request, pixels, SAR preprocessing/detection,
AS-202, Decision 055, PR creation or merge.

## Proven root cause and supplied-provider-fact provenance

[Historical M51 FAIL](AS_201_LIVE_ACCEPTANCE_RETRY.md),
commit `8b32ec53e052d1ca6472bcf0fd442d9102b8669f`, reached both catalogs and complete pagination but rejected all
six CDSE records inside `sentinel1_resolver._normalize_item(...)`.
`properties.sar:product_type` and `properties.s1:product_type` were absent;
`properties["product:type"]` was the string **`IW_GRDH_1S`**.
The old check accepted only `GRD` / `GRDH`, raising sanitized
`Sentinel1RetrievalError: Source is not GRDH-compatible Level-1 GRD.`
It produced `UNAVAILABLE / DISCOVERY_IDENTITY_INVALID` for all six slots, not a
provider metadata defect. PC normalization/asset access was not reached.

The owner authorization supplies an **externally verified official-provider fact**:
CDSE STAC documentation defines `IW_GRDH_1S` and demonstrates it for `sentinel-1-grd`.
Codex did not independently retrieve or inspect that documentation during M52.
No source-access time/URL is invented. This representation maps to the already
frozen IW high-resolution Level-1 GRD semantics; Decision 054 is unchanged.

## Exact correction and fail-closed contract

Only the resolver's exact case-sensitive membership set changes:
`{"GRD", "GRDH"}` → **`{"GRD", "GRDH", "IW_GRDH_1S"}`**.
Provider metadata is not rewritten. No substring, prefix, suffix, regex or arbitrary
`*_GRDH_*` acceptance. The fallback expression stays byte-identical:
`sar:product_type` → `s1:product_type` → `product:type`.
An explicitly incompatible or null higher-priority value still rejects the record;
a valid `product:type="IW_GRDH_1S"` cannot rescue it.

Independent exact ID/collection/start/end, S1A/IW/VV+VH/ascending/orbit101,
optional absolute orbit, native PC identity, footprint, unsigned URL, exactly-one
match, two-slice/date and six-slot guards stay unchanged. Shared STAC, optical,
FrozenJSON, endpoints, envelope, source policy, config and dependencies are untouched.

## Focused offline regressions

**41 new parametrized cases**, using synthetic fixtures and no provider traffic:

- Six direct normalizations, one for each exact frozen CDSE source, with M51's
  field shape; input metadata is unchanged.
- One six-source public resolver test: all six `RESOLVED_NOT_ACCESSED`; normalized
  parameters, fingerprint and product ID equal the existing GRD fixture; ready=false.
- Six PC regressions: GRD/GRDH accepted at all three existing field positions.
- Eleven rejection cases: EW_GRDH_1S, IW_GRDM_1S, IW_SLC__1S, GRDM, SLC, unknown,
  OTHER_GRDH_1S, IW_GRDH_1S_extra, prefix_IW_GRDH_1S, lowercase iw_grdh_1s and empty string.
- Seven explicit conflict/null cases, including incompatible sar:product_type with
  valid s1:product_type and product:type fallback; final discovery identity is invalid.
- Ten strict identity rejection cases for ID, collection, start/end precision,
  platform, mode, polarization, orbit direction, relative and absolute orbit.

Existing native-PC/cardinality/representation/security/metadata tests remain passing.
M50's actual pystac-client construction and synthetic pagination tests remain passing.
The contract test file's socket.connect guard forbids external network.
The focused suite covers the same three files as M51: `test_sentinel1.py`,
`test_sentinel1_contract.py` and `test_stac_non_optical.py`.
Synthetic source resolution is not real six-source header/XML acceptance.

## Quality, preservation and scientific boundary

**177 focused / 1475 full tests PASS**, 6 existing Rasterio PendingDeprecationWarnings; Ruff/diff/strict JSON/digest/security/preservation PASS.
No GitHub CI success is claimed. Only the resolver, one test file, four continuity
files and two new evidence files change. Entire Decisions file (050–054), M49/M50/M51
MD/JSON and other accepted evidence remain byte-identical. All **44 protected
external hashes / 57 modes / 3 stashes** remain unchanged; recovery artifacts retained.
No raw provider responses, credential/signing query or generated raster/cache product
is persisted. Semantic JSON is strictly finite; independent digest repeat is required.

**Provider requests 0; CDSE 0; PC 0; signing 0; TIFF/XML 0; SAR pixel reads/bytes 0/0;
scientific SAR compute 0.** Git fetch/push are separate from provider traffic.
No calibration, noise correction, sigma0/gamma0, dB, reprojection, mosaicking,
speckle filtering, detection, persistence or oil-risk computation.
Offline engineering fixtures are not real scientific processing.

M49 remains historical FAIL; M50 merged correction preserved; **M51 remains
AS201_LIVE_ACCEPTANCE_RETRY = FAIL**. No live retry occurs in M52, and real access
readiness remains **UNPROVED** pending separately authorized acceptance.
**AS-202 NOT STARTED; Decision 055 ABSENT. No PR or merge in M52.**

Schema: **as201-m52-cdse-product-type-fix-v1**.
Semantic SHA-256: **`c79dc7714ad2ad6895c4e58da4e7f4122f137c18755481379bc245702900bf23`**; hash JSON `semantic` only with sorted keys,
compact UTF-8, ensure_ascii=false, allow_nan=false and stable six-source order.
Creation/execution times, future commit SHA and display prose are excluded.
See [EV-056 JSON](AS_201_CDSE_PRODUCT_TYPE_FIX.json).

Next: owner review → separately authorized PR/merge containing preserved M51
failure evidence and M52 correction → separately authorized controlled live acceptance.
Do not retry or start AS-202 in this task.
