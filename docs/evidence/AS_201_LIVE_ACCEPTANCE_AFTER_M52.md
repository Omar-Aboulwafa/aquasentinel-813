# AS-201 M53 — Controlled Six-Source Live Acceptance After M52

## Terminal result and execution contract

**M53 / E53 / EV-057: AS201_LIVE_ACCEPTANCE_AFTER_M52 = FAIL.**
Exactly one top-level live execution of merged public `search_sentinel1(SARConfig())`
then `validate_retrieval_access(...)`. All six frozen sources are preserved;
no alternative pipeline, substitution, production fix, restart or manual slice retry.
The original validator traversed all six normally. Final assembly reached **K**,
but **ready=false**; every slice is **UNAVAILABLE / METADATA_INVALID**.

Official baseline `9403faf7f7bd8c0a71e5d262338974647831ad93` is PR #33's merge, exact parents
`e137795686d8f97bbd8ba6bc0465616783586ae0` and
`033086c6ffb7f21db0544e1b369a1367a06ac11d`.
Fresh clean branch: `validation/as-201-live-acceptance-after-product-type-fix`. M53/E53/EV-057 confirmed unused before allocation.
Decision 054 remains FINAL / FROZEN / MERGED. Decisions 050–054 are byte-identical.
M49 historical FAIL, M50 correction, M51 historical FAIL and M52 correction remain intact.

**Task/goal:** evaluate the merged exact six-source retrieval/access boundary, not SAR science.
**Inputs:** frozen Decision 054, normal SARConfig, approved provider/asset hosts, merged M50/M52 corrections.
**Outputs/files:** this MD/JSON evidence and four continuity/index files only.
**Dependencies:** none added, removed or upgraded.
**Acceptance:** all exact identities and required VV structural/XML checks must pass,
all six AVAILABLE, ready=true, zero image blocks/pixels/scientific SAR work.
**Risk/guardrails:** preserve partial/failing outcomes; do not infer readiness from catalog or offline success.
**Validation:** focused/full offline engineering tests, Ruff, finite JSON, digest repeat,
security, whitespace and protected hash/mode/stash audit after the single live run.
**Non-goals:** production fixes, extra requests, VH header access, pixels, SAR preprocessing,
oil detection, AS-202, Decision 055, PR or merge.

Live execution (Asia/Dubai): **2026-10-11T04:21:28.214975+04:00 →
2026-10-11T04:22:28.612157+04:00**.
UTC: **2026-10-11T00:21:28.214975+00:00 → 2026-10-11T00:22:28.612157+00:00**.
External instrumentation observed original calls; logging/profile state restored and
transient token cache discarded. An exclusive external marker prevents a second run.

## Catalog, identity and access stages

A–D: CDSE root/collection/construction passed; complete **3-page** search returned
**10 + 10 + 6 = 26** provider records, no next link on the final page.
E–H: PC root/collection/construction passed; complete **1-page** search returned
**24** provider records, no next link.
I: all **six CDSE + six exact PC** identities normalized; exact source matching and
all **36 stable asset references** resolved. All six entered RESOLVED_NOT_ACCESSED.
M52's exact IW_GRDH_1S acceptance crosses the historical M51 product-type rejection.

J1–J6: each source's **VV** structural metadata passed the original TIFF validator:
classic little-endian, uint16, one band, nodata0, ZSTD50000, 1024² tiles, six overviews,
210 geographic tiepoints, no affine pixel-scale/model-transformation contract.
All **162 range responses were HTTP206**; each requested span was returned exactly.
The original validator's metadata-span/image-block overlap check passed for all six.
**No VH header read** was added; VH remains a resolved stable auxiliary asset.

Each slice fetched its existing manifest/product_vv/calibration_vv/noise_vv XMLs
within existing limits. All 24 XML GETs returned HTTP200, and root-role checks passed.
**Fetching/parseable roles do not establish XML identity/LUT validation.**
All six failed at manifest/startTime before subsequent identity/LUT/geolocation checks.
No successful metadata summary was produced. Final source header/metadata remain
null as emitted by production; observed successful headers are recorded separately,
not injected into the failed source objects.

| Frozen role / slice | Exact PC source | Observed VV structural validation | Production final state |
|---|---|---|---|
| REFERENCE / 1 | `S1A_IW_GRDH_1SDV_20260424T144205_20260424T144230_064223_08158E` | PASS; 27 ranges / 16,432 bytes | UNAVAILABLE / METADATA_INVALID |
| REFERENCE / 2 | `S1A_IW_GRDH_1SDV_20260424T144230_20260424T144255_064223_08158E` | PASS; 27 ranges / 16,432 bytes | UNAVAILABLE / METADATA_INVALID |
| DOCUMENTARY_EVENT / 1 | `S1A_IW_GRDH_1SDV_20260506T144204_20260506T144229_064398_081C09` | PASS; 27 ranges / 16,432 bytes | UNAVAILABLE / METADATA_INVALID |
| DOCUMENTARY_EVENT / 2 | `S1A_IW_GRDH_1SDV_20260506T144229_20260506T144254_064398_081C09` | PASS; 27 ranges / 16,432 bytes | UNAVAILABLE / METADATA_INVALID |
| LATE_FOLLOW_UP / 1 | `S1A_IW_GRDH_1SDV_20260518T144204_20260518T144229_064573_082235` | PASS; 27 ranges / 16,432 bytes | UNAVAILABLE / METADATA_INVALID |
| LATE_FOLLOW_UP / 2 | `S1A_IW_GRDH_1SDV_20260518T144229_20260518T144254_064573_082235` | PASS; 27 ranges / 16,432 bytes | UNAVAILABLE / METADATA_INVALID |

Exact corresponding CDSE IDs, microsecond acquisition intervals, stable references
and normalized source lineage are retained in the JSON. No source is substituted.

## First new failure boundary — same-run evidence only

First failure: **J1**, then the identical manifest-time rejection occurs at J2–J6.
Call chain: `validate_retrieval_access → validate_slice_access → validate_metadata_xml
→ _validate_metadata_xml → _validate_manifest → _parse_time`.

Exact underlying exception:
`Sentinel1RetrievalError: Sentinel-1 item manifest.startTime must be timezone-aware.`
Production emits the unchanged reason **METADATA_INVALID**.

The first manifest/startTime is the string **`2026-04-24T14:42:05.150515`**.
It is ISO-like with fractional seconds but no Z/UTC offset. The current parser calls
`datetime.fromisoformat(value)`, then rejects `parsed.tzinfo is None` before exact UTC
interval comparison. Per-slice safe timestamp excerpts are in the JSON.
This is an observed provider-time representation rejected by the existing contract;
M53 does **not** establish the provider's timezone standard, infer a timezone,
classify the provider as defective, or modify the parser. Later XML checks are
**NOT REACHED**, not PASS. No extra diagnostic provider request is made and no patch
is proposed or implemented inside M53.

## Actual request and byte accounting

| Category | Actual requests | Response-body bytes delivered |
|---|---:|---:|
| CDSE_ROOT | 1 | 3,670 |
| CDSE_COLLECTION | 1 | 11,989 |
| CDSE_SEARCH_PAGE | 3 | 436,326 |
| PC_ROOT | 1 | 2,135 |
| PC_COLLECTION | 1 | 11,147 |
| PC_SEARCH_PAGE | 1 | 206,182 |
| TOKEN | 1 | 400 |
| TIFF | 162 | 98,592 |
| MANIFEST | 6 | 151,650 |
| PRODUCT | 6 | 10,685,021 |
| CALIBRATION | 6 | 6,093,708 |
| NOISE | 6 | 2,560,801 |
| **Total** | **195** | **20,261,621** |

**30 sign operations / 30 token-ready returns; one token HTTP acquisition**, reused
transiently across the same allowlisted account/container. No token response hash,
token value, signed href/query, Authorization or cookie is persisted. Only token
request count/status/hostname/path/body byte count is retained. No transport retry
was observed; no custom retries were added. Body bytes exclude wire framing/headers.

ZIP requests/bytes **0/0**; image-block requests/bytes **0/0**;
SAR pixel reads/bytes **0/0**; scientific SAR compute **0**.
No calibration application, thermal-noise correction, sigma0/gamma0 computation,
dB, reprojection, mosaicking, speckle, slick detection, persistence or oil risk.
Metadata XML reads are not scientific use of LUTs or raster pixels.
Git network operations and offline/synthetic engineering tests are separate accounting.

## Deterministic identities, support and provenance

Actual partial/unavailable-state retrieval:
**`sentinel1_retrieval:b2d9afb757d3551dcee8c6ae79624cbb33a03b1b8207cc025ade79ce22076a08`**.

| Frozen role / slice | Actual final slice fingerprint |
|---|---|
| REFERENCE / 1 | `b5b9cf9a0b7639e9e71f2419e61f4d6028eff67b63ef82a605bf5ec48552c324` |
| REFERENCE / 2 | `3e2e5650ad45a9109480bc8b7a0b4033fa01161d496b99e3d40620bad55145a3` |
| DOCUMENTARY_EVENT / 1 | `48232b5e8f89a8e180542516fd6a9ad307646bd2921d083d4bac27297c04d260` |
| DOCUMENTARY_EVENT / 2 | `b8087ea3e38372d9079b9b840c2970c3b1da4d6d35010cd38615bb980027e543` |
| LATE_FOLLOW_UP / 1 | `6085492426e3f0b18d27665e7999ba53d787288861ef051ab577f970eb9d0a5d` |
| LATE_FOLLOW_UP / 2 | `324dff021fdb0d165339d8cf92c78d45bb93c9d3114609859c714075d4e19132` |

Actual group fingerprints:

- REFERENCE: `50a4651d1ce56049d32f7f3687ac8c34ddd0b14c39a86f2f4dcbd1572d74a44d`
- DOCUMENTARY_EVENT: `10ad25c2629fc23f99bce14c27df538987a1c68b9b62e80f5b855900b475858d`
- LATE_FOLLOW_UP: `500a5dd6e330bdb02df35a2dc61eb8bdf041d82c43bbc9265238fd57e2a5eef4`

All **six CDSE discovery + six PC source records** and the derived retrieval
provenance are present (12 immediate source IDs); registry mutation is zero.
Common footprint inventory is complete, is_lower_bound=false, with metadata source
support and small explicit three-date gaps as returned by original assembly.
The full canonical support/gap geometries are in the JSON.
**Metadata footprint coverage is not valid-pixel support.** Complete footprints,
provenance and fingerprints do not override six unavailable access-validation slots.
These identities describe the actual deterministic failed metadata state; they do
not establish a live-ready handoff, calibrated backscatter or oil detection.

## Engineering quality and preservation

**177 focused / 1475 full tests PASS**, 6 existing Rasterio PendingDeprecationWarnings; Ruff/diff/strict JSON/digest/security/preservation PASS.
Recorded timings: focused 0.99 s; full 36.43 s.
Local test success is not live provider success; no GitHub CI-success claim.
Only six documentation/evidence paths change. Source/tests/config/dependencies,
entire Decisions file, all prior accepted scientific evidence, M49/M50/M51/M52
MD/JSON are byte-identical. All **44 protected hashes / 57 modes / 3 stashes**,
sealed caches/handoffs and existing recovery artifacts are unchanged.
No generated scientific raster/cache product or raw provider response was persisted.
Strict finite JSON, independent canonical semantic digest repeat, new-file whitespace
and credential/signed-URL scan pass.

Schema **as201-m53-live-acceptance-after-m52-v1**.
Semantic SHA-256 **`984cdb35b7364150d687d86f4a3478f2e93ca7015843b58425f109687ab0078d`**. Hash JSON semantic only: sorted keys, compact UTF-8,
ensure_ascii=false, allow_nan=false, stable source/request ordering. Execution/creation
timestamps, future commit SHA and display prose are excluded.
See [EV-057 JSON](AS_201_LIVE_ACCEPTANCE_AFTER_M52.json).

## Stop state and owner handoff

**M53 FAIL. Live six-source readiness remains UNPROVED.**
Both catalog/identity and VV TIFF gates progressed, but required manifest identity
did not pass. Preserve this exact outcome for owner review; any investigation,
production correction or live retry requires separate authorization.
M49 and M51 remain historical FAIL; M50/M52 remain merged engineering corrections.
No petroleum/spill/source confirmation, safety or shutdown inference.
**AS-202 NOT STARTED. Decision 055 ABSENT. No PR or merge in M53.**
