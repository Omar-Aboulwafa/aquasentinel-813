# AS-201 M51 — Controlled Six-Source Live Acceptance Retry

## Terminal result and baseline

**M51 / E51 / EV-055: AS201_LIVE_ACCEPTANCE_RETRY = FAIL.**
One top-level execution of merged public `search_sentinel1(SARConfig())`, followed
once by merged `validate_retrieval_access(...)`. No bypass, custom resolver,
production fix, substitution or manual full restart. All six exact frozen slots remain.

Official main `e137795686d8f97bbd8ba6bc0465616783586ae0` is PR #32's merge, with exact parents
`29b7b46edc877a50645865aad4a1e9f62d34d6f5` and
`43dafb556ee8583ca57d46c07a9d93ba45adbc94`.
Fresh clean branch: `validation/as-201-live-acceptance-retry`.
M51/E51/EV-055 were confirmed unused; EV-055 does not imply Decision 055.
Decision 054 remains FINAL / FROZEN / MERGED; its historical M47 body is unchanged.

Live execution UTC: **2026-10-10T23:03:49.124630+00:00 → 2026-10-10T23:04:03.461471+00:00**.
External instrumentation delegated to original public/library/transport functions;
it observed requests and sanitized stage exceptions, restored patched functions
and scoped logging state, and discarded transient token-cache state. No token issued.
An exclusive external start marker prevents a second top-level invocation.

## Stage trace and localized failure

A–D: CDSE root, collection, search construction and complete pagination succeeded.
Three search pages returned **10 + 10 + 6 = 26 provider records**; final page had no next link.
E–H: PC root, collection, search construction and complete pagination succeeded.
One page returned **24 records**; no next link. Frozen exact CDSE/PC IDs were observed.
Their presence alone does not prove native identity compatibility or access readiness.

**I: all six CDSE normalizations failed** in
`sentinel1_resolver._normalize_item(...)`, at `product not in {"GRD", "GRDH"}`.
For each exact CDSE record, `sar:product_type` and `s1:product_type` are absent;
fallback `properties["product:type"]` is the string **`"IW_GRDH_1S"`**.
The code permits only **`"GRD"` / `"GRDH"`** at that check.
Safe underlying exception for every slot:
`Sentinel1RetrievalError: Source is not GRDH-compatible Level-1 GRD.`
Production catches it and preserves `UNAVAILABLE / DISCOVERY_IDENTITY_INVALID`.
This localizes a provider product-type representation rejected by the resolver;
no provider metadata defect is established, and no correction is attempted here.
PC source normalization/asset resolution is not reached for any slot.

J1–J6: public per-slice validator visits each UNAVAILABLE slot and returns it unchanged.
No asset is dereferenced. K: normal final assembly completes with **ready=false**.
Stage completion means an operation returned, not that identity/access gates passed.
No fatal uncaught exception; six caught identity failures cause the terminal FAIL.

## Six actual slot outcomes

All retain S1A/IW/GRDH-compatible GRD/ascending relative-orbit101/VV+VH as required
policy, not as a claim that all live validation stages accepted them. Exact full
microsecond intervals, native IDs and expected dimensions are in the JSON.

| Frozen role / slice | CDSE identity | PC identity required | Actual final state | VV header + required XML |
|---|---|---|---|---|
| REFERENCE / 1 | `S1A_IW_GRDH_1SDV_20260424T144205_20260424T144230_064223_08158E_4192_COG` | `S1A_IW_GRDH_1SDV_20260424T144205_20260424T144230_064223_08158E` | UNAVAILABLE / DISCOVERY_IDENTITY_INVALID | NOT EVALUATED |
| REFERENCE / 2 | `S1A_IW_GRDH_1SDV_20260424T144230_20260424T144255_064223_08158E_BA3A_COG` | `S1A_IW_GRDH_1SDV_20260424T144230_20260424T144255_064223_08158E` | UNAVAILABLE / DISCOVERY_IDENTITY_INVALID | NOT EVALUATED |
| DOCUMENTARY_EVENT / 1 | `S1A_IW_GRDH_1SDV_20260506T144204_20260506T144229_064398_081C09_BF44_COG` | `S1A_IW_GRDH_1SDV_20260506T144204_20260506T144229_064398_081C09` | UNAVAILABLE / DISCOVERY_IDENTITY_INVALID | NOT EVALUATED |
| DOCUMENTARY_EVENT / 2 | `S1A_IW_GRDH_1SDV_20260506T144229_20260506T144254_064398_081C09_A43B_COG` | `S1A_IW_GRDH_1SDV_20260506T144229_20260506T144254_064398_081C09` | UNAVAILABLE / DISCOVERY_IDENTITY_INVALID | NOT EVALUATED |
| LATE_FOLLOW_UP / 1 | `S1A_IW_GRDH_1SDV_20260518T144204_20260518T144229_064573_082235_34DC_COG` | `S1A_IW_GRDH_1SDV_20260518T144204_20260518T144229_064573_082235` | UNAVAILABLE / DISCOVERY_IDENTITY_INVALID | NOT EVALUATED |
| LATE_FOLLOW_UP / 2 | `S1A_IW_GRDH_1SDV_20260518T144229_20260518T144254_064573_082235_E298_COG` | `S1A_IW_GRDH_1SDV_20260518T144229_20260518T144254_064573_082235` | UNAVAILABLE / DISCOVERY_IDENTITY_INVALID | NOT EVALUATED |

Both slices/date retained. VV header, manifest, product/calibration/noise XML,
thermal-noise state and PC asset accessibility are **NOT EVALUATED** for every slice.
No M46 header/XML or M48 synthetic result fills missing live evidence.

## Coverage, fingerprints and provenance

Normal unavailable-state retrieval identity:
`sentinel1_retrieval:fbdcf8ff01b4ea21ec8046c374c02188d182f72192fe00008fc7ce7eb43cfad7`.
Six slice and three group fingerprints were generated by production and are
recorded exactly in JSON. They identify the **unavailable metadata state**, not
an accepted ready six-source handoff.
All normalized discovery/pixel-source SourceRecords are null; derived provenance
is **null**. No registry is mutated or fabricated lineage produced.

Normal common support is an empty MultiPolygon **lower bound**, with
`footprint_inventory_complete=false`, `is_lower_bound=true`; the full envelope
is shown as a gap. This describes missing accepted footprint inventory, not
measured zero provider coverage, valid-pixel support, absence of slicks or oil area.

## Actual request / byte accounting

| Category | Requests | Response-body bytes delivered |
|---|---:|---:|
| CDSE_ROOT | 1 | 3,670 |
| CDSE_COLLECTION | 1 | 11,989 |
| CDSE_SEARCH_PAGE | 3 | 436,326 |
| PC_ROOT | 1 | 2,135 |
| PC_COLLECTION | 1 | 11,147 |
| PC_SEARCH_PAGE | 1 | 206,182 |
| TOKEN | 0 | 0 |
| TIFF | 0 | 0 |
| MANIFEST | 0 | 0 |
| PRODUCT | 0 | 0 |
| CALIBRATION | 0 | 0 |
| NOISE | 0 | 0 |
| **Total provider retrieval** | **8** | **671,449** |

All eight responses HTTP200. Search pages: CDSE **3**, PC **1**.
No transport retry, signing/token, TIFF-range or XML request occurred.
Bytes are response-body bytes delivered to HTTP clients, not wire framing/headers.
Git operations and offline engineering tests are excluded.
Product ZIP requests **0**; image-block requests **0**;
SAR pixel reads/bytes **0/0**; scientific SAR compute calls **0**.
No raster dataset/sample/mask/statistics access, calibration, noise correction,
dB, reprojection, mosaicking, speckle, water mask, detection, temporal SAR or oil risk.

## Historical, scientific and integrity boundary

M49 [FAIL evidence](AS_201_LIVE_ACCEPTANCE.md) remains byte-identical, including
later localization. M50 [offline correction](AS_201_STAC_GEOMETRY_BOUNDARY_FIX.md)
remains byte-identical and merged via PR #32. M51 crossed its previously failing
client-construction boundary live, but failed at a different metadata identity check.
Neither earlier failure is hidden or retroactively relabelled PASS.

No production/test/config/dependency change. Entire Decisions file (050–054),
prior accepted evidence except continuity index, 44 protected external hashes,
57 protected modes and all three stash entries are unchanged. External recovery
artifacts retained; no raster/cache scientific product created.

**136 focused / 1434 full tests PASS**, six existing Rasterio PendingDeprecationWarnings; Ruff/diff/JSON/digest/security/preservation PASS.
Strict finite JSON and independent digest reconstruction/repeat are required.
Credential/signed-URL scans exclude raw responses, signed hrefs, SAS, cookies and
Authorization headers from published evidence. Only selected stable metadata,
safe request paths/status/body hashes, source states and sanitized exceptions persist.

Semantic SHA-256: **`d255801335110cc74f11e1d045a1c5cdf7cabb37c085fbcf890512feb11bc336`**; schema **as201-m51-live-acceptance-retry-v1**.
Canonical input is JSON `semantic` only, sorted compact UTF-8, ensure_ascii=false,
allow_nan=false, stable slot order. Execution times and future commit SHA are excluded.
See [EV-055 JSON](AS_201_LIVE_ACCEPTANCE_RETRY.json).

Even a future retrieval PASS would not establish oil detection, petroleum/spill
confirmation, source attribution, water safety or shutdown advice. This retry is FAIL.
**AS-202 NOT STARTED. Decision 055 ABSENT. No PR or merge in M51.**
Next: owner review of this failure; separately authorize a minimal SAR-only CDSE
GRDH product-type interoperability correction and offline regressions, then a
separately authorized controlled live gate. Do not retry or broaden policy here.
