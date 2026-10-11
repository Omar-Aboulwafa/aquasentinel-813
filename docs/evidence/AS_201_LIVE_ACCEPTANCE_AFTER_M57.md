# AS-201 M58 — Controlled Live Acceptance After M57

## Result and scope

**M58 / E58 / EV-062: AS201_LIVE_ACCEPTANCE_AFTER_M57 = FAIL.**
Official main/base: `225efc896bf74d87f62741e05a4251ac86d07395` — PR #36 merge, exact parents
`cea91ab8b7fa8dbf4618a32c0a51ea1b2356f721` and
`016f35d41195b17bff2da47de336380451862f9e`.
Fresh branch: `validation/as-201-live-acceptance-after-platform-family-fix`; numbering unused before this task.
One public `search_sentinel1(SARConfig())` call and one public
`validate_retrieval_access(...)` call, with unchanged production functions.
No monkeypatches, manual retries, restarts, source substitutions, alternate dates
or second diagnostic workflow. Passive tracing recorded existing traffic/guard progress.
An external accounting-setup failure occurred before any start marker/public call/
traffic while inspecting a cached callable; setup was corrected before the sole run.
Trace/profile/logging state restored; transient signing state discarded.
Execution: `2026-10-11T12:08:23.471979+00:00` to `2026-10-11T12:09:23.797012+00:00` (UTC).
No production/test/config/dependency edits or new Decision.

## Actual progress and first new failure

Both catalogs complete: CDSE 3 pages (10 + 10 + 6 records), PC 1 page (24 records).
All six exact CDSE and PC identities and six-asset sets PASS. All six VV TIFF
structural validations PASS. All 24 required XML bodies fetched and safely parsed;
root roles match. **All six complete manifests now PASS live**: exact acquisition
interval, IW, ascending, relative orbit 101, GRD, one platform, number A, direct
familyName cardinality/text, case-only platform identity and native VV witness.
M54 UTC and M57 scope/case corrections crossed their actual live boundaries.

The first new failing operation, repeated naturally in each frozen slice:

`_validate_metadata_xml` → `_validate_luts` →
`_parse_time(_unique_text(vector, "azimuthTime"), "calibration.azimuthTime")`.

Exception: **Sentinel1RetrievalError**.
Sanitized text: **`Sentinel-1 item calibration.azimuthTime must be timezone-aware.`**
Field: `calibrationVector/azimuthTime`. Generic strict parser rejects an unzoned
calibration-vector timestamp. The field's text/raw XML is not retained here.
No provider-defect or schema-validity classification is asserted; no diagnostic
request or correction was performed. All six production outcomes:
**UNAVAILABLE / METADATA_INVALID**. Final assembly reaches **K**, ready=false.

Production validates LUTs before ADS headers. Product/calibration/noise ADS
identity and intervals, noise range/azimuth LUTs, geolocation/incidence, native
sample spacing, dimensions and thermal metadata are **NOT_REACHED**. Fetched or
parsed XML is not equivalent to successful complete metadata validation.
Calibration vector structure/coordinates progressed only to the first timestamp;
no complete calibration LUT PASS is claimed.

## Six-slice matrix

| Frozen role / slice | CDSE | PC | Assets | VV TIFF | Complete manifest + witness | Calibration LUT | Later metadata gates | Final |
|---|---|---|---|---|---|---|---|---|
| REFERENCE / 1 | PASS | PASS | PASS | PASS | PASS | FAIL | NOT_REACHED | UNAVAILABLE / METADATA_INVALID |
| REFERENCE / 2 | PASS | PASS | PASS | PASS | PASS | FAIL | NOT_REACHED | UNAVAILABLE / METADATA_INVALID |
| DOCUMENTARY_EVENT / 1 | PASS | PASS | PASS | PASS | PASS | FAIL | NOT_REACHED | UNAVAILABLE / METADATA_INVALID |
| DOCUMENTARY_EVENT / 2 | PASS | PASS | PASS | PASS | PASS | FAIL | NOT_REACHED | UNAVAILABLE / METADATA_INVALID |
| LATE_FOLLOW_UP / 1 | PASS | PASS | PASS | PASS | PASS | FAIL | NOT_REACHED | UNAVAILABLE / METADATA_INVALID |
| LATE_FOLLOW_UP / 2 | PASS | PASS | PASS | PASS | PASS | FAIL | NOT_REACHED | UNAVAILABLE / METADATA_INVALID |

JSON records every individual check as PASS, FAIL or NOT_REACHED, exact frozen
CDSE/PC/native product identities, headers, safe XML body hashes/byte counts,
original exception trace and final fingerprints. Overall XML_complete is FAIL,
derived from the captured original validator exception; later checks remain
NOT_REACHED. No validators were rerun for reporting.

## Actual requests and bytes

| Role | HTTP requests | Response-body bytes | HTTP status counts |
|---|---:|---:|---|
| CALIBRATION | 6 | 6,093,708 | 200: 6 |
| CDSE_COLLECTION | 1 | 11,989 | 200: 1 |
| CDSE_ROOT | 1 | 3,670 | 200: 1 |
| CDSE_SEARCH_PAGE | 3 | 436,326 | 200: 3 |
| MANIFEST | 6 | 151,650 | 200: 6 |
| NOISE | 6 | 2,560,801 | 200: 6 |
| PC_COLLECTION | 1 | 11,147 | 200: 1 |
| PC_ROOT | 1 | 2,135 | 200: 1 |
| PC_SEARCH_PAGE | 1 | 206,182 | 200: 1 |
| PRODUCT | 6 | 10,685,021 | 200: 6 |
| TIFF | 162 | 98,592 | 206: 162 |
| TOKEN | 1 | 402 | 200: 1 |
| TOTAL | 195 | 20,261,623 | All successful transport responses |

**30 signing operations; 1 token HTTP acquisition.** No token value/body/hash,
signed href/query, Authorization header or cookie is persisted. Accounting stores
only role/hostname/status/stage/count/bytes; TIFF ranges are structural metadata.
Bytes exclude HTTP/TLS overhead. All 162 VV ranges return HTTP206, totaling 98,592
bytes; image-block overlap is rejected by the unchanged successful header validator.
No VH TIFF request. XML bodies remained transient; only safe SHA-256/length persisted.
Stable unsigned asset references in actual retrieval provenance are retained.

## Actual provenance, coverage and identities

Product: `sentinel1_retrieval:b2d9afb757d3551dcee8c6ae79624cbb33a03b1b8207cc025ade79ce22076a08`.
Retrieval fingerprint: `b2d9afb757d3551dcee8c6ae79624cbb33a03b1b8207cc025ade79ce22076a08`.
Original stable serialization validates source/retrieval identity and provenance.
Six CDSE discovery records and six distinct actual PC source records: **12 immediate
source IDs**. Source record parameters and original provenance are in JSON.

Six slice fingerprints:

- REFERENCE / 1: `b5b9cf9a0b7639e9e71f2419e61f4d6028eff67b63ef82a605bf5ec48552c324`
- REFERENCE / 2: `3e2e5650ad45a9109480bc8b7a0b4033fa01161d496b99e3d40620bad55145a3`
- DOCUMENTARY_EVENT / 1: `48232b5e8f89a8e180542516fd6a9ad307646bd2921d083d4bac27297c04d260`
- DOCUMENTARY_EVENT / 2: `b8087ea3e38372d9079b9b840c2970c3b1da4d6d35010cd38615bb980027e543`
- LATE_FOLLOW_UP / 1: `6085492426e3f0b18d27665e7999ba53d787288861ef051ab577f970eb9d0a5d`
- LATE_FOLLOW_UP / 2: `324dff021fdb0d165339d8cf92c78d45bb93c9d3114609859c714075d4e19132`

Three group fingerprints/readiness:

- REFERENCE: `50a4651d1ce56049d32f7f3687ac8c34ddd0b14c39a86f2f4dcbd1572d74a44d`; ready=false.
- DOCUMENTARY_EVENT: `10ad25c2629fc23f99bce14c27df538987a1c68b9b62e80f5b855900b475858d`; ready=false.
- LATE_FOLLOW_UP: `500a5dd6e330bdb02df35a2dc61eb8bdf041d82c43bbc9265238fd57e2a5eef4`; ready=false.

Common support: COMMON_THREE_DATE_METADATA_SUPPORT, EPSG:4326 footprint support;
footprint inventory complete=true, is_lower_bound=false. Coverage gaps remain
explicit, with NODATA_OR_UNAVAILABLE_NEVER_ZERO_ANOMALY semantics. No raster
pixel-evaluability claim. All three groups ready=false; final retrieval ready=false.
The final failure-state product ID equals M55 because final source availability /
reason remains unchanged. M58's distinct trace/digest captures the later boundary;
product-ID equality must not erase the new manifest PASS or calibration failure.

## Forbidden execution and scientific boundary

ZIP downloads/bytes, image-block requests/bytes, SAR pixel reads/bytes, calibration
application, thermal-noise correction application, sigma0/gamma0 computation, dB
conversion, reprojection, mosaicking, speckle filtering, oil detection, persistence/
risk scoring and scientific SAR compute: **all zero**. AS-202 NOT STARTED.
RAW_GRD_AMPLITUDE is not calibrated scientific backscatter or oil detection.
**LIVE_READINESS UNPROVED; SAR_SCIENTIFIC_READINESS UNPROVED; OIL_DETECTION NOT STARTED.
Decision 055 ABSENT.** Test success never overrides this live FAIL.

## Engineering quality and preservation

Focused AS-201/Sentinel-1: **330 passed in 1.1s**.
Full repository: **1617 passed, 6 warnings in 36.53s**.
Six existing Rasterio PendingDeprecationWarnings; no new warnings.
Offline test processes deny external socket connections; **0 attempts** in both.
Ruff, tracked/new-file whitespace, strict finite JSON, independently reconstructed
semantic digest/repeat, credential/signed-URL scan and preservation audit: **PASS**.
No GitHub CI success is claimed.

Only six authorized docs/evidence paths change. Source/tests/config/dependencies,
Decisions 050–054 entire file/frozen bodies, all prior accepted scientific evidence,
M55 historical FAIL, M56 diagnostic and M57 offline PASS remain byte-identical.
**44 protected external hashes / 57 modes / all three safety stashes** unchanged;
recovery artifacts retained, data inventory unchanged, no scientific product created.

## Semantic digest and owner handoff

Semantic SHA-256: `8dccb213233b984e59eebc41a02db5bd442150b84c4c249c8e8fd8a3b9ae527e`.
Canonical JSON: sorted keys, compact comma/colon separators, UTF-8,
ensure_ascii=false, allow_nan=false; array order retained. Volatile execution times,
quality/preservation summaries and the new commit SHA are excluded. Independent
reparse/key-order reversal reconstruction produces the same digest.

**M55 HISTORICAL LIVE FAIL → M56 DIAGNOSTIC COMPLETE → M57 OFFLINE CORRECTION PASS
→ M58 LIVE FAIL at calibration.azimuthTime.** No historical blocker erased.
Next: owner review; any publication/merge, focused localization/correction or later
live attempt requires separate authorization. No PR, merge, fix, second live run,
AS-202 or Decision 055 in M58.
