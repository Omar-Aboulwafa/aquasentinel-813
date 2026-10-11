# AS-201 M55 — Controlled Six-Source Live Acceptance After M54

## Terminal result and authorized execution

**M55 / E55 / EV-059: AS201_LIVE_ACCEPTANCE_AFTER_M54 = FAIL.**
Exactly one top-level run: `search_sentinel1(SARConfig())`, then
`validate_retrieval_access(...)`, each called once. Unchanged merged production code
naturally traversed all six frozen slices. No restart, manual slice retry, alternate
workflow, production patch or source/date substitution. Final assembly reached **K**;
**ready=false** and all six sources are **UNAVAILABLE / METADATA_INVALID**.

Official baseline: `cea91ab8b7fa8dbf4618a32c0a51ea1b2356f721`, PR #35 merge. Exact parents:
`9403faf7f7bd8c0a71e5d262338974647831ad93` and
`0ed27201c05be3a2bf614f5a556963909b40e7e0`.
Fresh clean branch: `validation/as-201-live-acceptance-after-manifest-utc-fix`. M55/E55/EV-059 confirmed unused before allocation.
Decision 054 remains FINAL / FROZEN / MERGED; Decisions 050–054 unchanged.
M49/M51/M53 historical FAIL and M50/M52/M54 corrections remain intact.

**Goal/inputs:** evaluate the existing Decision-054 six-source engineering metadata
boundary after merged M54, using normal SARConfig and frozen exact identities.
**Outputs/files:** this MD/JSON and four continuity/index files only; no dependencies.
**Acceptance:** complete catalogs, six exact matches/assets/VV headers and all XML
validation, all six AVAILABLE, all groups/retrieval ready, valid lineage and zero pixels/science.
**Risk/guardrails:** preserve actual failures, distinguish NOT_REACHED, no scientific
or live-readiness inference from offline success. Engineering quality gates follow the run.

Live execution, Asia/Dubai:
**2026-10-11T14:17:18.539819+04:00 → 2026-10-11T14:18:18.281097+04:00**.
UTC: `2026-10-11T10:17:18.539819+00:00` → `2026-10-11T10:18:18.281097+00:00`.
Passive external observation delegates original calls; no extra provider request or
second validation. Logging/profile/trace state restored and transient token cache
discarded. An exclusive external marker prevents another top-level invocation.

## Reached catalogs, resolution, header and XML-access gates

CDSE A–D: root, collection and search construction PASS; **3 pages**,
**[10, 10, 6]**, **26 records**, final next link absent.
PC E–H: root, collection and construction PASS; **1 page**,
**24 records**, final next link absent.
I: all six exact CDSE and PC identities normalize; all six asset sets (36 references)
resolve. Exact corresponding IDs/intervals/source lineage are preserved in JSON.

All six original VV TIFF structural validators returned successfully: **162
HTTP206 ranges / 98,592 bytes**. Every delivered span equals its
requested length; original metadata/image-block overlap rejection passed. Observed
headers retain uint16, one band, ZSTD, nodata0, 1024² tiles, six overviews and geographic
tiepoints; no affine model is fabricated. **No VH header read**.

All 24 required manifest/product_vv/calibration_vv/noise_vv XMLs fetched with HTTP200
within original budgets; parseable roots are XFDU/product/calibration/noise. Root-role
validation passed before the manifest error. **Retrieval/root role is not identity/LUT PASS.**
Failed final source header/metadata remain null exactly as production emitted;
observed headers are separate evidence, not injected into unavailable sources.

## Six-slice validation matrix

| Role / slice | CDSE | PC | Assets | VV TIFF | Manifest | Product XML | Calibration XML | Noise XML | Final state |
|---|---|---|---|---|---|---|---|---|---|
| REFERENCE / 1 | PASS | PASS | PASS (6) | PASS | FAIL | NOT_REACHED | NOT_REACHED | NOT_REACHED | UNAVAILABLE / METADATA_INVALID |
| REFERENCE / 2 | PASS | PASS | PASS (6) | PASS | FAIL | NOT_REACHED | NOT_REACHED | NOT_REACHED | UNAVAILABLE / METADATA_INVALID |
| DOCUMENTARY_EVENT / 1 | PASS | PASS | PASS (6) | PASS | FAIL | NOT_REACHED | NOT_REACHED | NOT_REACHED | UNAVAILABLE / METADATA_INVALID |
| DOCUMENTARY_EVENT / 2 | PASS | PASS | PASS (6) | PASS | FAIL | NOT_REACHED | NOT_REACHED | NOT_REACHED | UNAVAILABLE / METADATA_INVALID |
| LATE_FOLLOW_UP / 1 | PASS | PASS | PASS (6) | PASS | FAIL | NOT_REACHED | NOT_REACHED | NOT_REACHED | UNAVAILABLE / METADATA_INVALID |
| LATE_FOLLOW_UP / 2 | PASS | PASS | PASS (6) | PASS | FAIL | NOT_REACHED | NOT_REACHED | NOT_REACHED | UNAVAILABLE / METADATA_INVALID |

NOT_REACHED means the relevant scientific-metadata validator did not execute;
the XML files nevertheless were fetched. No later check is labelled PASS or FAIL.

## First new failure boundary, from this run only

First error: **J1**, repeated at J2–J6. Call chain:
`validate_retrieval_access → validate_slice_access → validate_metadata_xml →
_validate_metadata_xml → _validate_manifest → _unique_text(platform, "familyName")`.

Underlying exception: **`Sentinel1MetadataError: XML requires one consistent familyName value.`**
Production final reason: **METADATA_INVALID**.
The parser expects exactly one consistent nonempty `familyName` child-text value
within the single platform element. The same-run trace identifies that exact field
and operation; it does not establish whether the provider value is absent, ambiguous,
attribute-based or another representation. No provider-schema defect is asserted.
No extra diagnostic retrieval, raw provider-response persistence or correction.

Because the unchanged manifest validator reached `familyName`, its earlier exact
UTC start/stop equality, IW/ascending, relative orbit101, GRD and single platform
number A guards all passed. Thus **M54's exact manifest-time boundary passed live
for all six slices**, while **whole manifest validation failed**.
The later `familyName == Sentinel-1` comparison and native VV measurement witness
were not reached. `_validate_luts` and ADS validation were not entered; product
dimensions/geolocation/incidence, calibration/noise LUTs and thermal state remain
**NOT_REACHED**. This is engineering progress, not complete retrieval readiness.

## Actual request / byte accounting

| Category | Actual requests | Response-body bytes |
|---|---:|---:|
| CDSE_ROOT | 1 | 3,670 |
| CDSE_COLLECTION | 1 | 11,989 |
| CDSE_SEARCH_PAGE | 3 | 436,326 |
| PC_ROOT | 1 | 2,135 |
| PC_COLLECTION | 1 | 11,147 |
| PC_SEARCH_PAGE | 1 | 206,182 |
| TOKEN | 1 | 402 |
| TIFF | 162 | 98,592 |
| MANIFEST | 6 | 151,650 |
| PRODUCT | 6 | 10,685,021 |
| CALIBRATION | 6 | 6,093,708 |
| NOISE | 6 | 2,560,801 |
| **Total** | **195** | **20,261,623** |

**30 signing operations**, **30 token-ready returns**,
**1 token HTTP acquisition** reused transiently. Counts/bytes are this
run's measured values, not copied from M53. No transport retry observed or added.
Token contents/hash, SAS/signed query, Authorization, cookies and request URLs are
not persisted in request evidence; only sanitized host/role/status/count/bytes/stage.
Stable unsigned production asset references remain in the actual retrieval lineage.
Body-byte accounting excludes HTTP headers/wire framing.

ZIP requests/bytes **0/0**; image-block requests/bytes **0/0**; SAR pixel reads/bytes
**0/0**; scientific SAR compute **0**. No calibration/noise application, sigma0/gamma0,
dB conversion, reprojection, mosaicking, speckle filtering, oil detection, persistence
or risk scoring. Git operations/offline synthetic tests are separate engineering activity.

## Production identity, provenance and support

Actual retrieval product: **`sentinel1_retrieval:b2d9afb757d3551dcee8c6ae79624cbb33a03b1b8207cc025ade79ce22076a08`**; ready=false.

| Role / slice | Actual final fingerprint |
|---|---|
| REFERENCE / 1 | `b5b9cf9a0b7639e9e71f2419e61f4d6028eff67b63ef82a605bf5ec48552c324` |
| REFERENCE / 2 | `3e2e5650ad45a9109480bc8b7a0b4033fa01161d496b99e3d40620bad55145a3` |
| DOCUMENTARY_EVENT / 1 | `48232b5e8f89a8e180542516fd6a9ad307646bd2921d083d4bac27297c04d260` |
| DOCUMENTARY_EVENT / 2 | `b8087ea3e38372d9079b9b840c2970c3b1da4d6d35010cd38615bb980027e543` |
| LATE_FOLLOW_UP / 1 | `6085492426e3f0b18d27665e7999ba53d787288861ef051ab577f970eb9d0a5d` |
| LATE_FOLLOW_UP / 2 | `324dff021fdb0d165339d8cf92c78d45bb93c9d3114609859c714075d4e19132` |

Actual group fingerprints/readiness:

- REFERENCE: `50a4651d1ce56049d32f7f3687ac8c34ddd0b14c39a86f2f4dcbd1572d74a44d`; ready=false (both required slices unavailable).
- DOCUMENTARY_EVENT: `10ad25c2629fc23f99bce14c27df538987a1c68b9b62e80f5b855900b475858d`; ready=false (both required slices unavailable).
- LATE_FOLLOW_UP: `500a5dd6e330bdb02df35a2dc61eb8bdf041d82c43bbc9265238fd57e2a5eef4`; ready=false (both required slices unavailable).

Group readiness follows the unchanged all-AVAILABLE property; final source states
and fingerprints are from the production result. Six CDSE discovery and six PC
SourceRecords plus retrieval DerivedProductRecord are present; **12 immediate source IDs**.
Registry mutation: zero. Common footprint inventory is complete, is_lower_bound=false,
with original per-date/common support and explicit gap geometries preserved in JSON.
Metadata footprints do not establish valid pixels or compensate for unavailable slices.
The unchanged production `to_dict()` result is retained in JSON. That stable
serialization already excludes provenance creation timing; no production value
or fingerprint is modified to form this evidence.

The retrieval fingerprint equals the historical M53 fingerprint because final
availability/reason/accepted metadata state is unchanged. The later diagnostic failure
boundary is not part of that source identity. This equality is not a PASS signal;
M55's evidence digest records the distinct execution/failure trace.

## Engineering gates and preservation

**250 focused / 1548 full tests PASS**, 6 existing Rasterio PendingDeprecationWarnings; Ruff PASS; diff/strict JSON/digest/security/preservation **PASS**.
Focused 1.08 s; full 36.45 s.
Tests PASS does not override live FAIL; no GitHub CI-success claim.
Exactly six authorized documentation/evidence paths change; source, tests, config,
dependencies, entire Decisions file and accepted scientific evidence remain byte-identical.
M49–M54 MD/JSON are unchanged. **44 protected hashes / 57 modes / all three stashes**,
sealed bundles/caches/handoffs and recovery artifacts retained. No raw provider response,
credential, signed href or new scientific raster/cache product is persisted.

Schema: `as201-m55-live-acceptance-after-m54-v1`. Semantic SHA-256: **`875eb97e3b48c6ff99d2ea819466a852ca424880ef56b469e773be1992765e5e`**.
Canonical input: semantic object only, sorted keys, compact UTF-8, ensure_ascii=false,
allow_nan=false, fixed source/request order. Execution/creation times, quality timings,
display prose and future commit SHA excluded. Independent reconstruction/repeat must
match. [EV-059 JSON](AS_201_LIVE_ACCEPTANCE_AFTER_M54.json).

## Stop / owner review

**M55 LIVE FAIL. LIVE_READINESS = UNPROVED.** Preserve the newly reached familyName
failure and NOT_REACHED checks. No production fix, alternate workflow or live retry
inside M55. Any subsequent localization/correction/retry needs separate authorization.
No petroleum/source/chemistry, safety or shutdown inference.
**AS-202 NOT STARTED. Decision 055 ABSENT. No PR or merge in M55.**
