# AquaSentinel 813 — Presentation Evidence Journal

## Current AS-201 M61 — controlled live acceptance after M60 — PASS

**M61 / E61 / EV-065: AS201_LIVE_ACCEPTANCE_AFTER_M60 = PASS.**
Prepared on `validation/as-201-live-acceptance-after-safe-utc-fix` from PR #37 merge
`23887f0d4782ea8711b06e5566e66f4a3839a7fa` (parents `225efc896bf74d87f62741e05a4251ac86d07395`
and `505336537683f4a23b2fe4b3c206b768328f829f`). One unchanged public search/access
run; no restart, manual retry, patch, extra diagnostic or validator rerun.

All six exact sources, assets, VV TIFF headers, complete manifests/calibration/
noise-range/noise-azimuth/geolocation/native-spacing/ADS/dimensions/thermal/
required structures **PASS**. All slices AVAILABLE; three groups and final set ready.
360 SAFE timestamps pass live; generic strict parser unchanged. All 18 noise-azimuth
vectors have matching line/LUT lengths and all four bounds; passive summary only,
from original fetched/parsed XML, no extra request or optionality rule.

**195 HTTP requests / 20,261,623 bytes / 30 signs / 1 token acquisition** measured.
VH/ZIP/image-block/pixel/scientific SAR work **zero**. Production provenance validates;
12 CDSE/PC source IDs and common support unchanged. Accepted product:
`sentinel1_retrieval:de51027c6daa0f2812c0f2e43a041619ca1f290d16773e68c2da9f673bdbcc6e`.
**493 focused / 1780 full tests PASS**, six existing Rasterio warnings;
zero external socket attempts; Ruff/diff/JSON/digest/security/preservation PASS.

**LIVE_READINESS = PROVED_AT_AS201_METADATA_ACCESS_BOUNDARY** for the six frozen
sources. **SAR_SCIENTIFIC_READINESS UNPROVED; OIL_DETECTION / AS-202 NOT STARTED;
Decision 055 ABSENT.** M58 HISTORICAL LIVE FAIL / M59 diagnostic / M60 offline PASS
remain unchanged. Source/tests/config/deps/Decisions 050–054/accepted evidence,
protected hashes/modes/stashes/recovery preserved. No PR or merge in M61.
Next: owner review; publication/merge and later science require separate authorization.
Evidence: [EV-065 MD](evidence/AS_201_LIVE_ACCEPTANCE_AFTER_M60.md) /
[JSON](evidence/AS_201_LIVE_ACCEPTANCE_AFTER_M60.json).

## Historical AS-201 M60 — offline correction before PR #37 merge / M61

**M60 / E60 / EV-064: OFFLINE SAFE XML UTC-TIME INTEROPERABILITY CORRECTION PASS.**
Prepared on `fix/as-201-safe-xml-utc-time-normalization` from exact published M59
`dd35cbbce43bfe482bc573408893365e089e950a`; official main `225efc896bf74d87f62741e05a4251ac86d07395`.
The M60 authorization supplies the official Sentinel-1 Product Specification
S1-RS-MDA-52-7441 (2025, Issue/Revision 3/16/2, 01/10/2025): timeType is UTC
with microsecond resolution. Codex made no independent external source request.
M59's 360 naive timestamps remain immutable empirical evidence; no re-fetch.

One SAFE-local helper handles only product/calibration/noise ADS start/stop and
calibration/noise-range vector azimuthTime. Raw nonempty/unpadded text,
<=6 fractional digits, exact frozen ADS equality and all later guards stay enforced.
Generic time parser, M54 manifest and M57 platform/native witness remain unchanged.
Six sources × naive/Z/+00/equivalent +04 complete metadata PASS offline;
80 malformed, 18 interval mismatch and 41 later-guard cases rejected.
**493 focused / 1780 full tests PASS**, six existing Rasterio warnings;
Ruff/diff/finite JSON/digest/security/preservation PASS. Provider/sign/token/TIFF/XML/
image-block/pixel/scientific traffic **zero**; test external socket attempts zero.

**M58 HISTORICAL LIVE FAIL; M59 DIAGNOSTIC COMPLETE; LIVE_READINESS UNPROVED;
SAR_SCIENTIFIC_READINESS UNPROVED; AS-202 NOT STARTED; Decision 055 ABSENT.**
M49–M59 evidence, Decisions 050–054, unrelated source/tests/config/dependencies,
protected hashes/modes/stashes/recovery remain unchanged. Next: owner review;
PR/merge/live retry require separate authorization. No PR or merge in M60.
Evidence: [EV-064 MD](evidence/AS_201_SAFE_XML_UTC_TIME_FIX.md) /
[JSON](evidence/AS_201_SAFE_XML_UTC_TIME_FIX.json).

## Historical AS-201 M59 — diagnostic before M60 specification-backed correction

**M59 / E59 / EV-063: SAFE_XML_TIME_REPRESENTATION_DIAGNOSTIC_COMPLETE.**
Prepared on `diagnostic/as-201-safe-xml-time-representation` from published M58
`376754bed59eedbe9cbce47978ae5a52ae481410`; official main `225efc896bf74d87f62741e05a4251ac86d07395`.
Exactly 18 existing product/calibration/noise XML GETs, each once; **18/18 body
hashes/lengths match M58**. All 360 consumed timestamps are timezone-naive ISO
with six fractional digits, no explicit offset/whitespace: 36 ADS + 162 calibration
vectors + 162 noise-range vectors. Generic parser rejects all 360. All ADS
wall-clock fields match frozen acquisition fields; UTC meaning is not inferred.
**UTC_SEMANTICS_REQUIRES_OWNER/SPEC REVIEW.** Same rejection independently
reproduced at noise and ADS boundaries; no complete validator/later gate PASS claim.

**18 signs / 1 token / 19 HTTP200 requests / 19,339,930 response-body bytes**.
CDSE/PC STAC/manifest/TIFF/VH/ZIP/image-block/pixels/scientific SAR compute **zero**.
M58 not rerun; no monkeypatch, production fix, raw XML or credentials persisted.
**330 focused / 1617 full tests PASS**, six existing Rasterio warnings;
Ruff/diff/JSON/digest/security/preservation PASS. Source/tests/config/dependencies,
Decisions 050–054, M58/earlier evidence, 49 protected hashes/62 modes/three stashes /
recovery retained unchanged. **M58 HISTORICAL LIVE FAIL; M57 OFFLINE CORRECTION
PASS; LIVE_READINESS UNPROVED; AS-202 NOT STARTED; Decision 055 ABSENT.**
Next: owner/spec review; separately authorize any correction/offline regressions,
publication/merge or live acceptance. No PR/merge or parser change in M59.
Evidence: [EV-063 MD](evidence/AS_201_SAFE_XML_TIME_DIAGNOSTIC.md) /
[JSON](evidence/AS_201_SAFE_XML_TIME_DIAGNOSTIC.json).

## Historical AS-201 M58 — live FAIL before M59 time representation diagnostic

**M58 / E58 / EV-062: AS201_LIVE_ACCEPTANCE_AFTER_M57 = FAIL.**
One unchanged public search/access-validation run from PR #36 merge
`225efc896bf74d87f62741e05a4251ac86d07395`; prepared on `validation/as-201-live-acceptance-after-platform-family-fix`.
Both catalogs complete; all six CDSE/PC identities, stable asset sets, VV headers
and **complete manifests including platform familyName + native VV witness PASS**.
All 24 required XMLs fetched. All six then fail generic strict calibration-vector
`calibration.azimuthTime`: `Sentinel-1 item calibration.azimuthTime must be timezone-aware.`
Final UNAVAILABLE / METADATA_INVALID; assembly reaches K, ready=false.
Later ADS identity/interval, dimensions, noise LUT, geolocation/incidence, native
spacing and thermal guards NOT_REACHED. No repair, restart or second diagnostic.

**195 requests / 20,261,623 response-body bytes; 162 HTTP206 VV structural ranges /
98,592 bytes; 30 signing operations / 1 transient token HTTP acquisition.**
ZIP/image-block/SAR pixel reads/bytes/scientific compute **zero**; no VH TIFF.
Passive tracing only, no live monkeypatches or production edits.
**330 focused / 1617 full tests PASS**, six existing Rasterio warnings;
Ruff/diff/strict JSON/digest/security/preservation PASS. All source/tests/config/
dependencies, Decisions 050–054, historical evidence, 44 protected hashes/57 modes /
three safety stashes/recovery artifacts preserved. No signed href/secret persisted.
**M55 HISTORICAL LIVE FAIL; M56 DIAGNOSTIC COMPLETE; M57 OFFLINE CORRECTION PASS;
LIVE_READINESS UNPROVED; AS-202 NOT STARTED; Decision 055 ABSENT.**
Next: owner review; any PR/merge, localization/fix or live attempt requires separate
authorization. No PR, merge, correction or second live attempt in M58.
Evidence: [EV-062 MD](evidence/AS_201_LIVE_ACCEPTANCE_AFTER_M57.md) /
[JSON](evidence/AS_201_LIVE_ACCEPTANCE_AFTER_M57.json).

## Historical AS-201 M57 — offline correction before PR #36 merge / M58

**M57 / E57 / EV-061: OFFLINE MANIFEST PLATFORM FAMILYNAME INTEROPERABILITY
CORRECTION PASS.** Prepared on `fix/as-201-manifest-platform-familyname` from M56
`839b593a6f79722235494ab40c6df345ea17c7de`; main remains
`cea91ab8b7fa8dbf4618a32c0a51ea1b2356f721`. M55/M56 evidence preserved.
Only manifest platform familyName now requires exactly one nonempty direct child
and case-only Sentinel-1 identity equality. Nested instrument families are excluded;
platform number A, shared XML/time helpers, earlier/later guards remain unchanged.

**69 new offline cases; 330 focused / 1617 full tests PASS**, six existing Rasterio
warnings; Ruff/diff/JSON/digest/security/preservation PASS. Exact six-source M56
representation crosses the complete synthetic metadata validator, not live readiness.
Provider requests/signing/pixels/scientific SAR compute **zero**; M55/M56 not rerun.
Prior evidence, Decisions 050–054, resolver/policy/shared STAC/optical/config/
dependencies, 44 protected hashes/57 modes/three stashes preserved.
**M55 HISTORICAL LIVE FAIL; M56 DIAGNOSTIC COMPLETE; LIVE_READINESS UNPROVED;
AS-202 NOT STARTED; Decision 055 ABSENT.** No PR or merge.
Next: owner review → separately authorized publication/merge → separately
authorized controlled live engineering acceptance. No retry or SAR science in M57.
Evidence: [EV-061 MD](evidence/AS_201_MANIFEST_PLATFORM_FIX.md) /
[JSON](evidence/AS_201_MANIFEST_PLATFORM_FIX.json).

## Historical AS-201 M56 — diagnostic before M57 offline correction

**M56 / E56 / EV-060: MANIFEST_PLATFORM_REPRESENTATION_DIAGNOSTIC_COMPLETE.**
Prepared on `diagnostic/as-201-manifest-platform-familyname` from published M55
`ff00aafed870b0f427532159c4eb4ac3d08691d9`; official main remains
`cea91ab8b7fa8dbf4618a32c0a51ea1b2356f721`.
All six manifests: one platform, number `A`, direct family `SENTINEL-1`, nested
instrument family `Synthetic Aperture Radar` (`abbreviation="SAR"`). Recursive
`familyName` lookup sees two distinct values and raises the exact M55 exception.
Direct-child scoping alone would still fail the later case-sensitive `Sentinel-1`
literal; both representation facts are diagnosed, with no production fix.

Exactly **6 signing operations / 1 token HTTP acquisition / 6 manifest HTTP200 GETs
/ 151,650 manifest bytes**; each body SHA matches M55. No retry, catalog, TIFF,
other XML, ZIP/image-block/pixel access or SAR science. M55 was not rerun.
**261 focused / 1548 full tests PASS**, six existing Rasterio warnings;
Ruff/diff/JSON/digest/security/preservation PASS. Source/tests/config/dependencies,
Decisions 050–054, M49–M55/upstream evidence, 44 protected hashes/57 modes/three
stashes unchanged. No raw XML/credential/signed href persisted.
**M55 HISTORICAL LIVE FAIL; LIVE_READINESS UNPROVED; AS-202 NOT STARTED;
Decision 055 ABSENT.** No PR or merge. Next: owner review → separately authorized
minimal manifest-boundary correction/offline regressions → separately authorized
live engineering gate. No correction implemented in M56.
Evidence: [EV-060 MD](evidence/AS_201_MANIFEST_PLATFORM_DIAGNOSTIC.md) /
[JSON](evidence/AS_201_MANIFEST_PLATFORM_DIAGNOSTIC.json).

## Historical AS-201 M55 — live FAIL before M56 diagnostic

**M55 / E55 / EV-059: AS201_LIVE_ACCEPTANCE_AFTER_M54 = FAIL.**
One unchanged public search/access-validation run from PR #35 merge `cea91ab8b7fa8dbf4618a32c0a51ea1b2356f721`;
prepared on `validation/as-201-live-acceptance-after-manifest-utc-fix`. Decision 054 and M50/M52/M54 corrections merged/frozen;
M49/M51/M53 historical FAIL evidence preserved.
Both catalogs complete; all six CDSE/PC identities and stable asset sets resolve.
All six VV headers PASS; all 24 XMLs fetched. Manifest exact UTC acquisition matching
now passes, but all six fail `_unique_text(platform, "familyName")`:
`XML requires one consistent familyName value.` Final **UNAVAILABLE / METADATA_INVALID**;
assembly reaches K, **ready=false**. Native measurement witness/product/LUT/geolocation/
thermal checks NOT_REACHED. No production fix, restart, manual retry or extra diagnostic request.

**195 requests / 20,261,623 response-body bytes**;
162 HTTP206 VV structural ranges / 98,592 bytes;
30 sign operations / 1 transient token HTTP request.
ZIP/image-block/pixel reads/bytes **0/0**; scientific SAR compute **0**. No VH access.
12-source lineage and complete footprint metadata do not establish access readiness.

**250 focused / 1548 full tests PASS**, 6 existing Rasterio PendingDeprecationWarnings; Ruff PASS; diff/strict JSON/digest/security/preservation **PASS**.
Source/tests/config/dependencies/Decisions 050–054 and M49–M54 evidence preserved;
44 protected external hashes / 57 modes / three stashes retained. No secret/signed href persisted.
**LIVE_READINESS UNPROVED. AS-202 NOT STARTED. Decision 055 ABSENT.**
Next: owner review; any publication/merge, localization/correction or live retry
requires separate authorization. No PR or merge in M55.
Evidence: [EV-059 MD](evidence/AS_201_LIVE_ACCEPTANCE_AFTER_M54.md) and
[JSON](evidence/AS_201_LIVE_ACCEPTANCE_AFTER_M54.json).

## Historical AS-201 M54 — offline correction before PR #35 merge / M55

**M54 / E54 / EV-058: OFFLINE MANIFEST UTC-TIME INTEROPERABILITY CORRECTION PASS.**
Prepared on `fix/as-201-manifest-utc-time-normalization` from preserved M53 evidence commit
`42855ac22844ede60e37c5136944de879a0a9080`; official main `9403faf7f7bd8c0a71e5d262338974647831ad93`.
Only manifest acquisition start/stop may interpret naive time as UTC, followed by
the unchanged exact frozen-interval comparison. Generic parser and non-manifest XML
time boundaries remain strict; all later XML guards remain unchanged.

**73 new offline cases; 250 focused / 1548 full tests PASS**, six existing Rasterio
PendingDeprecationWarnings; Ruff/diff/strict JSON/digest/security/preservation
**PASS**. Decisions 050–054, M49–M53 evidence,
resolver/shared STAC/optical/config/dependencies and protected external hashes/modes/
three safety stashes preserved. Provider requests **0**; SAR pixel reads/bytes **0/0**;
scientific SAR compute **0**. No live retry, PR or merge.

**M53 remains HISTORICAL LIVE FAIL. LIVE_READINESS UNPROVED. AS-202 NOT STARTED.
Decision 055 ABSENT.** Offline success does not establish later live XML/LUT readiness.
Next: owner review; separately authorize publication/merge and any controlled live
acceptance retry. No AS-202 work.
Evidence: [EV-058 MD](evidence/AS_201_MANIFEST_UTC_TIME_FIX.md) and
[JSON](evidence/AS_201_MANIFEST_UTC_TIME_FIX.json).

## Historical AS-201 M53 — controlled live FAIL before M54 offline correction

**M53 / E53 / EV-057: AS201_LIVE_ACCEPTANCE_AFTER_M52 = FAIL.**
One public search/access-validation run from PR #33 merge `9403faf7f7bd8c0a71e5d262338974647831ad93`;
prepared on `validation/as-201-live-acceptance-after-product-type-fix`. M50/M52 corrections and Decision 054 are merged/frozen;
M49/M51 historical FAIL evidence remains intact.
Both catalogs complete (3 CDSE + 1 PC pages); all six CDSE/PC identities and stable
assets resolve. All six VV TIFF structural validations PASS (162 HTTP206 metadata
ranges / 98,592 bytes). All required XMLs fetched, but all six fail manifest/startTime
timezone validation: `Sentinel-1 item manifest.startTime must be timezone-aware.`
Final slots **UNAVAILABLE / METADATA_INVALID**; assembly reaches K, **ready=false**.
Later XML identity/LUT checks NOT REACHED; no repair, restart or manual slice retry.

**195 requests / 20,261,621 response-body bytes**; 30 sign operations, 1 transient token
request; 24 XML GETs. ZIP/image-block/pixel reads/bytes **0/0**; scientific SAR compute **0**.
No VH header access. Six discovery/six PC sources and derived retrieval provenance exist;
complete footprint inventory is metadata support, not accepted pixel evaluability.
Retrieval `sentinel1_retrieval:b2d9afb757d3551dcee8c6ae79624cbb33a03b1b8207cc025ade79ce22076a08` identifies failed metadata state, not readiness.

**177 focused / 1475 full tests PASS**, 6 existing Rasterio PendingDeprecationWarnings; Ruff/diff/strict JSON/digest/security/preservation PASS.
Source/tests/config/dependencies/Decisions050–054 and all historical evidence preserved;
44 external hashes / 57 modes / 3 stashes unchanged. No secret/signed href persisted.
**Live readiness UNPROVED. AS-202 NOT STARTED. Decision 055 ABSENT.**
Next: owner review of M53 outcome; separately authorize publication, investigation
or correction. No additional provider request, production patch, PR or merge in M53.
Evidence: [EV-057 MD](evidence/AS_201_LIVE_ACCEPTANCE_AFTER_M52.md) and
[JSON](evidence/AS_201_LIVE_ACCEPTANCE_AFTER_M52.json).

## Historical AS-201 M52 — offline correction before PR #33 merge / M53

**M52 / E52 / EV-056: OFFLINE PRODUCT-TYPE INTEROPERABILITY CORRECTION PASS.**
Prepared on `fix/as-201-cdse-product-type-normalization` from M51 FAIL evidence commit
`8b32ec53e052d1ca6472bcf0fd442d9102b8669f`; official main remains `e137795686d8f97bbd8ba6bc0465616783586ae0`, PR #32.
The SAR resolver now accepts exactly `IW_GRDH_1S` alongside `GRD` / `GRDH`.
Field precedence and all exact frozen source guards stay unchanged; incompatible
higher-priority product metadata is not rescued by a valid fallback.
Official CDSE representation fact is externally verified and supplied in owner
authorization; Codex did not retrieve the documentation in M52.

**177 focused / 1475 full tests PASS**, 6 existing Rasterio PendingDeprecationWarnings; Ruff/diff/strict JSON/digest/security/preservation PASS.
**41 new offline cases**; six synthetic CDSE sources resolve without access,
existing normalized identities remain equal. Shared STAC/optical/config/dependencies,
Decisions 050–054, M49/M50/M51 evidence, protected hashes/modes/stashes preserved.
**M51 remains historical FAIL. Live readiness UNPROVED; no M52 live retry.**
Provider requests **0**; SAR pixel reads/bytes **0/0**; scientific SAR compute **0**.
**AS-202 NOT STARTED; Decision 055 ABSENT.** No PR or merge in M52.
Next: owner review → separately authorize PR/merge with M51 evidence + M52 fix
→ separately authorize controlled live acceptance. No provider fallback or science.
Evidence: [EV-056 MD](evidence/AS_201_CDSE_PRODUCT_TYPE_FIX.md) and
[JSON](evidence/AS_201_CDSE_PRODUCT_TYPE_FIX.json).

## Historical AS-201 M51 — controlled live acceptance retry before M52 correction — FAIL

**M51 / E51 / EV-055: AS201_LIVE_ACCEPTANCE_RETRY = FAIL.**
One top-level merged public search/access-validation run from main `e137795686d8f97bbd8ba6bc0465616783586ae0`,
PR #32. M49 historical FAIL and M50 merged offline correction remain unchanged.
CDSE/PC catalog search and complete pagination succeed; the corrected client
construction is reached live. Stage I rejects all six CDSE records:
`properties.product:type="IW_GRDH_1S"` is outside the resolver's GRD/GRDH literals.
All six final slots: **UNAVAILABLE / DISCOVERY_IDENTITY_INVALID**; ready=false.
J1–J6 preserve unavailable slots without asset access; final assembly reaches K.

Accounting: **8 HTTP200 requests / 671,449 body bytes**; CDSE 3 search pages,
PC 1. Signing/TIFF/XML/ZIP/image-block requests **0**; SAR pixel reads/bytes
**0/0**; scientific SAR compute **0**. No production fix or full restart.
Unavailable-state fingerprints exist; normalized sources/derived provenance null,
coverage incomplete empty lower bound. Header/XML validation NOT EVALUATED.
Engineering: **136 focused / 1434 full tests PASS**, six existing Rasterio PendingDeprecationWarnings; Ruff/diff/JSON/digest/security/preservation PASS.

Prepared on `validation/as-201-live-acceptance-retry`; Decision 054 unchanged.
Next: owner review → separately authorize SAR product-type interoperability fix
and offline tests → separately authorize live acceptance. **AS-202 NOT STARTED;
Decision 055 ABSENT.** No PR/merge; no oil-detection or live-readiness claim.
Evidence: [EV-055 MD](evidence/AS_201_LIVE_ACCEPTANCE_RETRY.md) and
[JSON](evidence/AS_201_LIVE_ACCEPTANCE_RETRY.json).

## Historical AS-201 M50 — offline correction before PR #32 merge / M51 retry

**M50 / E50 / EV-054: OFFLINE INTEROPERABILITY CORRECTION COMPLETE.**
Baseline: PR #31 merge `29b7b46edc877a50645865aad4a1e9f62d34d6f5`.
M49 localization identified FrozenJSON deepcopy rejection at `client.search(...)`,
not a provider metadata defect. The SAR resolver now gives both catalog clients
plain independent finite JSON; frozen Decision-054 envelope and internal guards
remain unchanged. Shared STAC, optical behavior and dependencies are unchanged.

Offline gates: **136 focused / 1434 full tests PASS**, six existing Rasterio
warnings; Ruff/diff/strict JSON/digest/security/preservation PASS. Real client
construction and three synthetic pages per provider pass. Provider requests **0**;
SAR pixel reads/bytes **0/0**; scientific SAR compute **0**.

M49 historical **AS201_LIVE_ACCEPTANCE = FAIL** and its localization evidence are
byte-identical and merged via PR #31. Full live acceptance **NOT RETRIED**;
six-source live readiness is not established by this offline correction.
Prepared on `fix/as-201-stac-geometry-boundary`.
Next: owner review → separately authorized fix PR/merge → separately authorized
controlled live retry. **AS-202 NOT STARTED; Decision 055 ABSENT.**
No PR/merge or GitHub CI-success claim in M50.
Evidence: [EV-054 MD](evidence/AS_201_STAC_GEOMETRY_BOUNDARY_FIX.md) and
[JSON](evidence/AS_201_STAC_GEOMETRY_BOUNDARY_FIX.json).

## Historical AS-201 M49 live provider acceptance — before M50 correction — 11 October 2026 (Asia/Dubai)

M48 implementation is **MERGED via PR #30** at
`392603b5b074d515eb6c137e33395c7f0b1256ac`; Decision 054 remains FINAL / FROZEN / MERGED.
**M49 / E49 / EV-053: AS201_LIVE_ACCEPTANCE = FAIL — catalog metadata contract
rejection, field/cause not localized.** The unchanged public search raised
`CatalogMetadataError` after CDSE root/collection HTTP200 responses, before
returning a retrieval set. Six-source access validation was not reached.
All six frozen slots remain NOT EVALUATED; no alternate source or patch was used.

Actual provider accounting: **2 CDSE requests / 15,659 response-body bytes**;
PC/token/TIFF/XML requests **0**. ZIP/image-block/pixel reads/bytes/scientific
SAR compute **0**. Coverage, six source/three group/set fingerprints and retrieval
provenance remain unavailable, not invented from M46 or M48 fixtures.
Diagnostic limitation: only exception class and request status/path/body hashes
were retained; exact offending field or code-vs-provider cause is not established.
See [EV-053 MD](evidence/AS_201_LIVE_ACCEPTANCE.md) and
[JSON](evidence/AS_201_LIVE_ACCEPTANCE.json).

Prepared on `validation/as-201-live-acceptance`; no active scientific development.
Engineering gate: **1432 tests PASS**, six existing Rasterio warnings; Ruff,
diff/JSON/digest/security/preservation PASS. Production/tests/config/dependencies,
Decisions 050–054, accepted evidence, external hashes/modes and stashes preserved.
**AS-202 NOT STARTED; Decision 055 ABSENT.** No M49 PR/merge or CI-success claim.
Immediate next step: owner review → separately authorize catalog failure
localization/correction/retry. No provider probes continued after the failure.
AS-107 COMPLETE / CLOSED and AS-108 qualified P0 case study remain unchanged.
Future AS-105 policy validation and P1 05.10 NOT STARTED.

## Historical AS-201 M48 implementation — before PR #30 merge — 11 October 2026 (Asia/Dubai)

**Decision 054 / M47 FINAL / FROZEN DESIGN / MERGED**, via PR #29 at
`1d2d994c7a04cca712485ce53dc9132db50615a8`. **M48 / E48 / EV-052: AS-201 RAW-GRD
RETRIEVAL / SOURCE IMPLEMENTATION COMPLETE; OFFLINE ENGINEERING VALIDATION PASS.**
This is source/header/XML engineering, not SAR preprocessing or oil detection.
AS-107 COMPLETE / CLOSED; AS-108 P0 case study COMPLETE / MERGED with POST
UNAVAILABLE and PARTIALLY_CONSISTENT remain unchanged.

Active implementation branch: `feature/as-201-sentinel1-retrieval`.
Existing WIP `d6f89ce07eaf6216308f39087ce094877d2bfd02` is preserved without rewriting.
Related remote correction `2abbe5a64e4017b8fc30ba243e3fe4c30f509a3c` was also
reviewed and preserved as an ancestor before the final completion commit.
Its twelve original paths were reviewed; follow-up corrections complete footprint
support/gaps, immutable models, group/set identities and derived retrieval lineage,
and harden raw TIFF/XML/transport validation. Both source slots/date and all six
slots remain explicit on failure. Missing footprint support is a lower bound,
never zero anomaly; metadata support does not establish pixel evaluability.

Engineering gates/results and review findings are in
[EV-052 implementation evidence](evidence/AS_201_IMPLEMENTATION_VALIDATION.md) and [JSON](evidence/AS_201_IMPLEMENTATION_VALIDATION.json).
Final M48 gate: **147 focused / 1432 full tests PASS**, six existing Rasterio
warnings; Ruff/diff/strict JSON/credential/preservation checks PASS.
No new real-provider probe, SAR pixels, scientific compute or scientific product.
M46 access evidence is historical and is not a six-slice live M48 acceptance claim.
Frozen Decisions 050–054, accepted HAB evidence, caches, stashes and recovery
material remain preserved. Shapely 2.1.2 is used only for metadata polygon topology.

**AS-202 NOT STARTED; Decision 055 ABSENT.** Calibration/noise correction, dB,
reprojection, resampling, mosaicking, speckle filtering, masking and oil detection
remain outside AS-201. Future AS-105 policy validation and P1 05.10 NOT STARTED.
Immediate next step: owner review of published M48 implementation → separately
authorized PR/merge. Any six-slice provider metadata acceptance or AS-202 design
requires separate owner direction. No M48 PR or merge performed; no CI claim.

## Historical AS-201 M47 design freeze — before PR #29 merge — 11 October 2026 (Asia/Dubai)

**AS-107 COMPLETE / CLOSED. AS-108 P0 RETROSPECTIVE OBSERVATIONAL-CONSISTENCY
CASE STUDY COMPLETE / MERGED with POST UNAVAILABLE**, via PR #28 at
`9a8a15c489a6aa3e678b642d2ccf5160affc56bd`. M44 PARTIALLY_CONSISTENT and all accepted scientific evidence
remain unchanged. M45/E45/EV-049 and M46/E46/EV-050 are now recorded historically
as completed read-only predecessor audits; PC_GRD_ACCESS_GATE PASS.
**Decision 054 / M47 / E47 / EV-051: FINAL / FROZEN DESIGN / NOT IMPLEMENTED.**

Frozen Kharg envelope EPSG:4326 [49.60,28.60,50.70,29.60], explicit source gaps and
common three-date comparison support; Apr24 REFERENCE → May6 DOCUMENTARY_EVENT →
May18 LATE_FOLLOW_UP, same S1A IW ascending orbit101 VV/VH, both slices/date.
CDSE discovery → exact PC GRD access mapping; RAW_GRD_AMPLITUDE; runtime-only
tokens; no provider fallback. Actual headers/XML roles govern provider defects.
SIGMA0_ELLIPSOID is a candidate, NOT FROZEN; AS-202 numerics/downstream rules remain
unfrozen. No pixels, SAR science, petroleum/source confirmation or intake invented.

Current active scientific development branch: none. This design was prepared on
`docs/as-201-design-freeze`. **AS-201 implementation and AS-202 NOT STARTED;
Decision 055 ABSENT.** Future AS-105 policy validation and P1 05.10 NOT STARTED.
Immediate next step: owner review → separately authorized M47 PR/merge → separate
AS-201 implementation authorization. No M47 PR or merge performed.
See [contract](AS_201_SENTINEL1_RETRIEVAL.md), [freeze evidence](evidence/AS_201_DESIGN_FREEZE.md)
and [JSON](evidence/AS_201_DESIGN_FREEZE.json). Engineering results are recorded in
the freeze evidence; historical checkpoints below retain their original states.

## Historical AS-108 M44 reporting — before PR #28 merge — 10 October 2026 (Asia/Dubai)

**AS-107 COMPLETE / CLOSED. Decision 053/M42 FINAL / FROZEN DESIGN / MERGED.**
M43 metadata selection COMPLETE / MERGED via PR #27 at `865cd14398c6bcdbeaed6a19210f5615beb638e6`.
**M44 / E44 / EV-048: RETROSPECTIVE CASE-STUDY REPORTING COMPLETE.**
**AS-108 P0: RETROSPECTIVE OBSERVATIONAL-CONSISTENCY CASE STUDY COMPLETE WITH POST UNAVAILABLE.**
Decision 053 category: **PARTIALLY_CONSISTENT**, from accepted evidence and unchanged
criteria: five descriptive PRE records evaluable; April 3 AS-105 P = 794 / candidates = 88,
April 28 P = 802 / candidates = 7 plus accepted Watch = 29.52380952380953; required POST
geometry endpoint absent. PRE is not independently scored or biologically negative.
April 3 AS-106/107 remains missing; no score fabricated.

April 28 accepted completeness/coverage = 0.7/0.7, provisional_observational_screening,
Review on the next valid acquisition, exact-grid persistence A/B/C = 7/7/0 remain
unchanged. No same-pixel recurrence is not proof of no HAB or biological persistence.
POST provisional May 3 identity retained: no exact PC 05.09 match, no pixels,
no scientific product/risk/negative/recovery label; no May 8/13/28 query/substitution.
M43 digest `df487999defada56023a7e76be69c507b2b1ff11d81de1480737eca86a1ad4de` unchanged.

This is a retrospective month/area observational-consistency case, not blind,
prospective, independent April preregistration, biological accuracy, species/toxin/
chlorophyll confirmation, probability, calibrated confidence, water safety or
shutdown advice. April outcomes were known before Decision 053; categories frozen
before May metadata, unavailable POST preserved. Exact onset-relative lead time
NOT ESTIMABLE. Scientific processing/EO/documentary requests in M44: **zero**.
Prepared on `data/as-108-case-study`; current active scientific development branch:
none. No Decision 054. AS-201, future AS-105 policy validation and P1 05.10 NOT STARTED.

Case SHA-256: `ccc5f04f304a8b4bb8a367331069a5ca54776433e7c0fea0c67d662e68e0772a`.
Engineering gates: **1285 full tests PASS (100.78s)**; six existing Rasterio
PendingDeprecationWarnings; Ruff PASS; diff/new-file whitespace PASS; strict finite
JSON, independent digest/repeat, predicate, credential and preservation checks PASS.
Engineering fixtures attempted no external network; no GitHub CI success claimed.
Immediate next step: owner review → separately authorized M44 PR/merge → separate
AS-201 Sentinel-1 retrieval/design authorization. No PR created or merge performed.
See [case report](evidence/AS_108_HISTORICAL_CASE_STUDY.md) and [JSON](evidence/AS_108_HISTORICAL_CASE_STUDY.json). Earlier checkpoints retain their original historical facts.

## Historical AS-108 M43 POST metadata selection — before PR #27 merge — 10 October 2026 (Asia/Dubai)

**AS-107: COMPLETE / CLOSED. Decision 053 / M42: FINAL / FROZEN DESIGN / MERGED**
via PR #26 at `8bb56f12f2cd683d4a96f069c5d049bf4a39799e` (parents
`14149113e58788621d6aef91f039b95781c67434` and
`9e7254edc7680c5da31e796f82be2b8537833b9b`).
**M43 / E43 / EV-047: POST METADATA INVENTORY / SELECTION COMPLETE; selection UNAVAILABLE.**
Six complete CDSE pages yielded **26 provider records / 26 distinct observation
keys / 13 acquisition timestamps**. Four pass CDSE metadata eligibility. Earliest:
**2023-05-03T06:46:21.024000Z**, Sentinel-2A, 40RBN/orbit20, cloud metadata **0.57%**.
The fixed existing PC resolver query returned **0 items / 0 exact PC05.09 matches**.
Selected PC ID/baseline: null. No later acquisition substituted or queried on PC.
This is metadata-selection UNAVAILABLE, **not a scientific consistency category**.

Selection SHA-256: `df487999defada56023a7e76be69c507b2b1ff11d81de1480737eca86a1ad4de`.
POST pixels, asset/signing/range requests, scientific processing and new risk scores:
**0 / NOT STARTED**. No May water-support inspection, recovery/negative label,
observational-consistency conclusion or upstream policy change. M42 evidence,
Decisions 050–053 and accepted scientific evidence remain unchanged.

Prepared on `data/as-108-post-selection`, worktree
`/workspace/aquasentinel-813-as108-m43`. Immediate next step: owner review of the
UNAVAILABLE metadata evidence, then separately authorize M44 case-study reporting
from accepted PRE/EVENT evidence with POST explicitly UNAVAILABLE. PR/merge and
any further compatibility investigation need separate authorization. **M44, AS-108 scientific execution and AS-201 NOT STARTED.**
Engineering gates: 1285 full tests PASS (106.24s), six existing Rasterio PendingDeprecationWarnings; Ruff PASS; diff/new-file whitespace PASS. No GitHub CI success claimed.
See [M43 evidence](evidence/AS_108_POST_METADATA_SELECTION.md) and
[complete inventory/selection digest](evidence/AS_108_POST_METADATA_SELECTION.json).
Earlier dated checkpoints below remain historical; no outcome tuned or hidden.

## Historical AS-108 M42 design freeze — before PR #26 merge — 10 October 2026 (Asia/Dubai)

**AS-107: COMPLETE / CLOSED. M40: COMPLETE / MERGED / PUBLICATION-CLOSEOUT**
through PR #25 at `14149113e58788621d6aef91f039b95781c67434`, with verified parents
`2bfbbd63cb5fee8e1d18a0b1099335b924e5ed9d` and
`88189f5ed85767f5022fa8e6c8ceee55b42f6c85`. Its merge-effective closure is now in force.
**M41 / E41 / EV-045: read-only feasibility/source audit COMPLETE**, recorded here
retrospectively; M41 changed no repository file. Its documentary access blocker was
resolved by externally verified EAD facts supplied by the project owner for M42;
Codex did not independently access the source, and no personal owner inspection
is claimed.
**Decision 053 / M42 / E42 / EV-046: FINAL / FROZEN DESIGN — NOT EXECUTED.**
AS-108 remains P0 before AS-201. No AS-108 validation outcome is computed here.

Frozen objective: **retrospective observational-consistency case study**, one event,
not biological accuracy. EAD **Marine Water Quality Report 2023**, listed
**21 November 2024**, documents a Raha Beach Red Tide incident in **April 2023**.
Timing **MONTH_LEVEL**; lead-time status **MONTH_LEVEL_ONLY**, exact days early not
estimable. Spatial precision **AREA_LEVEL_ONLY**; AOI/event relationship
**AREA_LEVEL_CONTEXTUAL_ALIGNMENT**. Al Raha remains analyst-defined, not an EAD
incident/sampling footprint or confirmed desalination intake. EAD species/toxin
context stays external: Pseudo-nitzschia multistriata / domoic acid; incident toxin
measurement NOT ESTABLISHED; AquaSentinel species/toxin inference NONE.

PRE `[2023-03-01,2023-04-01)` retains March 4/9/14/24/29 as descriptive context,
never self-baseline-scored or biological negatives. EVENT `[2023-04-01,2023-05-01)`
retains April 3 through accepted AS-105 and April 28 through accepted AS-107.
POST `[2023-05-01,2023-06-01)` requires one future metadata-selected **earliest
compatible May acquisition** before pixels; no fallback, honest UNAVAILABLE allowed.
Same AOI, cloud <=30%, 40RBN/orbit20, exact PC05.09 match and full grid/upstream
contract. No May metadata or pixels retrieved in M42; no frozen policy adjusted.

Immutable April 28 reference: `hab_risk:113143700cb35ac9230d9c54b68b1b53e2573838a4913d4bc942e81c99903fdb`;
**29.52380952380953 / Watch**, completeness/coverage **0.7/0.7**,
`provisional_observational_screening`, **Review on the next valid acquisition**,
A/B/C **7/7/0**. No rerun or new historical-validation classification in this task.
Decisions 050/051/052 and accepted EO evidence remain unchanged. No Decision 054.

Prepared on documentation branch `docs/as-108-design-freeze`, worktree
`/workspace/aquasentinel-813-as108-m42`; current active scientific development branch:
none. Immediate next step: owner review of Decision 053/design, with separate
PR/merge authorization; then separately authorize **M43 metadata-only POST selection**.
Validation execution, AS-201, future AS-105 policy validation and P1 05.10 NOT STARTED.
Deadline 11 October 2026 (Asia/Dubai): protect oil P0, demo and presentation.
M42 engineering quality: **1285 full tests PASS (115.87s), six existing Rasterio PendingDeprecationWarnings; Ruff PASS; diff/new-file whitespace PASS**; no GitHub CI-success claim.
New documentary/EO metadata/assets/real scientific calls: **0**.

See [AS-108 contract](AS_108_HAB_HISTORICAL_VALIDATION.md), [freeze evidence](evidence/AS_108_DESIGN_FREEZE.md),
and [machine-readable design](evidence/AS_108_DESIGN_FREEZE.json). Earlier dated status/milestone bodies
remain historical; their original unstarted/unmerged wording describes that time.

## Historical AS-107 M40 closeout preparation — before PR #25 merge — 10 October 2026 (Asia/Dubai)

**AS-107: CLOSEOUT READY. M40 / E40 / EV-044: PUBLICATION / CLOSEOUT PASS — READY FOR PR.**
This is the pre-merge closeout preparation state, not a claim that AS-107 is
already COMPLETE / CLOSED. **The future closeout PR merge itself is the durable
closure event:** after that merge, AS-107 is **COMPLETE / CLOSED** and M40 is
**COMPLETE / MERGED / PUBLICATION-CLOSEOUT**. No extra documentation loop or
invented future merge SHA is required merely to record that event.

Verified implementation/acceptance baseline: `2bfbbd63cb5fee8e1d18a0b1099335b924e5ed9d`.
AS-106: COMPLETE / CLOSED. Decision 052 / M37: FINAL / FROZEN / MERGED via
PR #22 (`49f5276b1ad372725b21cdb2085815225c98eed4`). M38: IMPLEMENTED /
SYNTHETIC-ADVERSARIAL VALIDATION COMPLETE / MERGED via PR #23
(`7f304bb44af93d2b3a1a3e6982fefad05fb8f452`). M39: REAL ENGINEERING
ACCEPTANCE PASS / MERGED via PR #24 (`2bfbbd63cb5fee8e1d18a0b1099335b924e5ed9d`).
Actual Git parents, ancestor relationships and merge/head tree equality were
verified, rather than inferred from these status statements.

Current active development branch: none. This closeout was prepared on
`docs/as-107-closeout`, in `/workspace/aquasentinel-813-as107-m40`, directly from
that verified main. Immediate next step: owner review of the published M40
closeout; PR creation and merge need separate authorization. No M40 PR or merge
was performed in this task. AS-108 NOT STARTED; future AS-105 policy validation
NOT STARTED; P1 homogeneous 05.10 robustness NOT STARTED. Decision 053 ABSENT.

Accepted as107-v1 product: `hab_risk:113143700cb35ac9230d9c54b68b1b53e2573838a4913d4bc942e81c99903fdb`.
Input fingerprint: `084790273118f50f6c8eaf0ed380dbce730c6dbbd7e4fa0f757c5d145e894d91`.
Output fingerprint: `25cccf8e8b550a76f28ebb01a2249060de5b1cd3114a7c531ef4775adbc87dae`.
**Watch = 29.52380952380953**, evidence completeness **0.7**, component coverage
**0.7**, assessment `provisional_observational_screening`; recommendation:
**Review on the next valid acquisition**. Seven pixels / 2,800 m²; spectral
14/35 = 40.0; red-edge family evidence breadth 7/21 = 33.333333333333336;
available persistence A/B/C = 7/7/0; C/B = 0/7 = 0.0; context/exposure unavailable.
No same-pixel candidate recurrence was observed among the 7 target candidate
pixels with valid prior observational history. This does not establish no HAB,
no biological persistence, safe water or zero environmental risk.

M40 publishes existing accepted evidence without recomputing real scoring or
upstream science. Decision 050/051/052 bodies and M39 MD/JSON remain byte-identical;
sealed bundles, caches, handoffs, recovery files, modes and both safety stashes
are retained. M40 engineering quality: **1285 full tests PASS (104.18s), six existing Rasterio PendingDeprecationWarnings; Ruff/diff/new-file whitespace/credential/preservation PASS**. Local checks only;
no GitHub CI success claim. Scientific/external-data requests and EO bytes: **0**.

Policy was frozen before real scoring; no outcome tuning followed Watch. Missing
operational components were not fabricated. This is not HAB/absence confirmation,
measured chlorophyll, species/toxins, probability/calibrated confidence, water safety,
shutdown advice, complete intake risk, accuracy or lead-time validation. Exact-grid
recurrence, no motion compensation, the 25-day + 8-second gap, sparse/shared five-history
support, BOA rather than aquatic Rrs, correlated red-edge evidence and candidate-conditioned
maximum remain limitations. Al Raha is a validation AOI, not a confirmed intake.

See [M40 closeout](evidence/AS_107_CLOSEOUT.md) and [machine-readable closeout](evidence/AS_107_CLOSEOUT.json).
All earlier dated current-status and M36–M39 records below describe historical
checkpoints; their original unstarted/unpublished/unmerged wording is retained.

## Historical AS-107 M39 real engineering acceptance — before PR #24 merge — 10 October 2026 (Asia/Dubai)

**AS-106: COMPLETE / CLOSED. Decision 052 / M37: FINAL / FROZEN / MERGED.
M38: IMPLEMENTED / SYNTHETIC-ADVERSARIAL VALIDATION COMPLETE / MERGED** through
PR #23 at `7f304bb44af93d2b3a1a3e6982fefad05fb8f452`, with parents
`49f5276b1ad372725b21cdb2085815225c98eed4` and
`55533467393f394d6cb3f856b439f41fde4b0148`.
**M39 / E39 / EV-043: REAL ENGINEERING ACCEPTANCE PASS.** First real computation
used unchanged accepted April 3/28 typed parents, offline, under the pre-score
frozen policy. Exactly three public AS-107 calls; no public upstream rerun.

Under the frozen AS-107 observational screening policy, the April 28 validation AOI produced a **Watch observational screening score of 29.52380952380953**, with evidence completeness **0.7** and component coverage **0.7**. Environmental context and intake exposure remain unavailable. The result is provisional observational screening, not confirmed HAB or operational water-safety determination.

Accepted product: `hab_risk:113143700cb35ac9230d9c54b68b1b53e2573838a4913d4bc942e81c99903fdb`.
Input fingerprint: `084790273118f50f6c8eaf0ed380dbce730c6dbbd7e4fa0f757c5d145e894d91`.
Output fingerprint: `25cccf8e8b550a76f28ebb01a2249060de5b1cd3114a7c531ef4775adbc87dae`.
The sole seven-pixel / 2,800 m² authoritative region has family a=(7,7,7,7,7),
v=(0,7,0,7,0); spectral 14/35 → 40.0; red-edge 7/21 → 33.333333333333336;
persistence A/B/C=7/7/0 → 0.0. F_all=F_red=H=1.0; completeness is capped by
K=0.7, not a biological probability. Flag: incomplete_evidence. Recommendation:
**Review on the next valid acquisition**. No same-pixel candidate recurrence was
observed among the 7 target candidate pixels with valid prior observational history;
this proves neither no HAB nor safe water nor zero biological persistence/risk.

Independent integer/binary64 arithmetic, fingerprints/identity, same/reversed-order
repeats, creation-time exclusion, full parent-aware validation, 13 ordinary plus
3 attacker-rehashed tamper rejections, immutability/non-aliasing and sealed fresh
process roundtrip: PASS. Scientific network/metadata/assets/EO bytes: 0.
Decisions 050/051/052, production source/tests/config/dependencies, accepted upstream
evidence, 41 protected external hashes, 53 modes and both safety stashes preserved.
Final M39 engineering quality gate: **292 focused tests PASS (43.61s); 1285 full tests PASS (103.96s), six existing Rasterio PendingDeprecationWarnings; Ruff/diff/credential/preservation PASS.** Local engineering checks, no GitHub CI-success claim.

Evidence prepared on `data/as-107-real-acceptance`, worktree
`/workspace/aquasentinel-813-as107-m39`, directly from verified PR #23 main.
Authorized evidence commit/push is for owner review; no PR or merge in M39.
Next: owner review of published M39 evidence; PR creation and M40 closeout require
separate authorization. **M40 and AS-108 NOT STARTED**; future AS-105 policy
validation NOT RUN; P1 homogeneous 05.10 robustness NOT STARTED. No Decision 053.
Weights/bands/candidate/recurrence policy were not adjusted after seeing the outcome.
No biological calibration/accuracy, species/toxins, measured chlorophyll, probability,
calibrated confidence, water safety, intake shutdown, complete operational risk or
lead-time claim. BOA is not aquatic Rrs; correlated red-edge emphasis, sparse/shared
five-history support, long two-date gap and candidate-conditioned maximum remain
limitations. Al Raha is an analyst-defined validation AOI, not a confirmed intake.

See [M39 evidence](evidence/AS_107_REAL_ACCEPTANCE.md) and
[machine-readable audit](evidence/AS_107_REAL_ACCEPTANCE.json).
All earlier dated M36–M38/current-status sections below are historical checkpoints;
their absent-score/unstarted/unmerged wording describes their original time.

## Historical AS-107 M38 offline implementation — before PR #23 merge — 10 October 2026 (Asia/Dubai)

**AS-106: COMPLETE / CLOSED. Decision 052 / M37: FINAL / FROZEN / MERGED** via
PR #22, implementation base `49f5276b1ad372725b21cdb2085815225c98eed4`.
**M38 / E38 / EV-042: IMPLEMENTED / SYNTHETIC-ADVERSARIAL VALIDATION PASS.**
AS-107 implements the frozen explainable availability-aware observational
screening-risk policy and passes synthetic/adversarial engineering validation.
No real HAB risk score or band exists; no accepted real parents were loaded/scored.
Current active development branch: `feature/as-107-hab-risk`; worktree
`/workspace/aquasentinel-813-as107-m38`. Implementation publication is on this
feature branch, not merged into main. Owner-authorized commit/push is for review;
no PR created and no merge performed by M38. Next: owner review of the published
implementation. M39 real acceptance and M40 closeout require separate authorization.
M39/M40 and AS-108 NOT STARTED; future AS-105 policy validation NOT RUN;
P1 homogeneous 05.10 robustness NOT STARTED.

Actual M38 quality: **292 focused risk tests PASS (44.93s);
1285 full tests PASS (117.57s), six existing Rasterio warnings;
Ruff/diff/security/preservation PASS.** Engineering evidence only, not real/biological
validation. Zero dependency/config/upstream changes; Decisions 050/051/052 unchanged.
See [M38 evidence](evidence/AS_107_IMPLEMENTATION_VALIDATION.md).
All earlier dated M36/M37/current-status sections below are historical checkpoints;
their unimplemented/unstarted wording does not describe current M38.

## Historical AS-107 M37 design freeze — before PR #22 merge — 10 October 2026 (Asia/Dubai)

**AS-106: COMPLETE / CLOSED** through PR #21 merge
`6b22d32f078ef80158b2f2d7aac4f3dd07925038` (official design baseline).
**M36 / E36 / EV-040:** prior read-only feasibility/design audit COMPLETE.
**Decision 052 / M37 / E37 / EV-041: FINAL / FROZEN DESIGN — NOT IMPLEMENTED.**
The primary quantity is evidence_completeness; all current scored outputs must be
qualified as provisional_observational_screening. Policy is frozen before any
real AS-107 score; environmental context/intake exposure remain unavailable.
No production implementation, real score, scientific product or AS-108 work.

Current active development branch: none. Design prepared on
`docs/as-107-design-freeze`. Next: owner review and separately authorized design
PR/merge, then separate M38 implementation authorization. M38–M40 NOT STARTED;
AS-108 NOT STARTED; future AS-105 policy validation NOT RUN; P1 05.10 NOT STARTED.
No PR/merge in M37. Decisions 050/051 and accepted evidence remain unchanged.

See [frozen contract](AS_107_HAB_RISK.md), Decision 052 and
[M36/M37 evidence](evidence/AS_107_DESIGN_FREEZE.md). Existing dated checkpoints
below remain historical, including pre-PR #21 pending-closeout/no-052 statements.

## Historical AS-106 M35 publication / closeout preparation — before PR #21 merge — 10 October 2026 (Asia/Dubai)

**M35 / E35 / EV-039: PUBLICATION / CLOSEOUT PASS — READY FOR PR.**
**AS-106 before this closeout merge: CLOSEOUT READY.** Official real-acceptance
baseline merged via PR #20: `82e30c00a30ed893ad47c44c5a1e363661370d35`.
M31/M32/M33/M34 are **COMPLETE AND MERGED** via PR #17/#18/#19/#20;
M34 real engineering acceptance PASS. Decision 051 is FINAL / FROZEN / MERGED via
PR #16; its original dated design/scientific body and Decision 050 are unchanged.
No Decision 052.

**Durable closure rule:** AS-106 closure becomes official when this closeout branch
is merged to main. That merge itself makes **AS-106 COMPLETE / CLOSED** and
**M35 COMPLETE / MERGED / PUBLICATION-CLOSEOUT**. No extra post-merge documentation
loop is required merely to record that future merge SHA. Until then, M35 preparation
is complete and official closure is pending merge; this note records that preparation.
Current active development branch: none. This closeout was prepared on
`docs/as-106-closeout`. AS-107+ is NOT STARTED / NOT AUTHORIZED; owner design review
and separate authorization are required.

Accepted `as106-v1` product:
`hab_persistence:c576478b6b6d85894e5317e65a1d0fd6cee38ed1c406d452b10f97712d2cc3bb`.
Input fingerprint: `2f8f6f1c37bd9f8a236109ab821e6e426f222840c4a74f623d2e78bd76529ab7`.
Output fingerprint: `7739a3f97c0e88113a17629678a0ef31bdb14594400f0568c0dfdfdb5dabafef`.
Frozen April sequence: `2023-04-03T06:46:21.024000Z` →
`2023-04-28T06:46:29.024000Z`; unchanged M32 selection digest:
`570792066c1997b9a403249d994c4e7367bf2f1dafc6473b6e30df20cd6481d5`.
**P802 / Q793 / A7 / B7 / C0; history coverage 7/7=1.0; recurrence 0/7=0.0;
streak 1→7; exact observation gap 2,160,008,000,000 µs (25 days + 8 seconds).**

**No same-pixel candidate recurrence was observed among the 7 target candidate
pixels with valid prior observational history.** Exact-pixel observation only:
no neighborhood/motion/current compensation; unsupported history is UNKNOWN.
Two eligible dates retained; shared March references are not independent confirmation,
five histories are not statistical sufficiency, and the long gap proves neither
continuous biological presence nor absence. April 3's ~13% upstream policy coverage
is separate from target-candidate history 7/7. No species/toxin/HAB/absence-of-HAB,
risk/confidence/probability/water-safety/operational decision claim.

Anti-cherry-picking record: metadata froze all eligible dates before recurrence
inspection; both dates used the same contract; April 3 had 88 AS-105 candidates,
April 28 had 7, recurrence was 0, and zero was retained. No date, threshold, family
rule, connectivity or spatial tolerance was changed to strengthen the demo.
M34's four typed parents/common contract, 9/9 arrays/dtypes, Boolean/global/time/region
oracles, validator, same/reverse repeats, identity/fingerprints/time exclusion,
immutability/non-aliasing, seven tamper controls including rehash and sealed bundle
roundtrip all PASS. These are accepted engineering integrity results, not biology
or accuracy validation; they were not rerun during M35.

M35 changes only eight docs/evidence paths. No new science, upstream rerun, EO/data
network or download. Accepted bundle rehashed locally read-only and preserved;
caches/handoffs/M29/M32/M33/M34, modes, safety stashes and recovery files retained.
M35 final pytest/Ruff/diff/security results are recorded in the closeout evidence;
no GitHub CI-success claim. Historical M34 baseline is 993 tests/six Rasterio warnings.

Next: owner review of this prepared closeout and separately authorized PR/merge.
AS-107 may later consume observational recurrence, history coverage, exact timing
and provenance; it must not reinterpret them as biological truth. AS-107 design/
implementation remains separate. Future AS-105 policy validation REQUIRED / NOT RUN;
P1 05.10 NOT STARTED. No PR or merge performed in this task.

See [M35 closeout](evidence/AS_106_CLOSEOUT.md) and
[normalized closeout](evidence/AS_106_CLOSEOUT.json).
All older dated execution/design/evidence sections below are historical: their
M34/M35 unstarted, missing-stage, authorization and not-closed states remain intact
and do not describe current M35. The immutable Decision 051 design-freeze status
is its original historical checkpoint, not a current implementation-status claim.

## Historical AS-106 M34 real engineering acceptance — before PR #20 merge — 10 October 2026 (Asia/Dubai)

**M31 / M32 / M33: COMPLETE AND MERGED** via PR #17 / #18 / #19.
Official M34 base (PR #19 merge): `4cde14ee448079163c2a08f3951f8dac294f8dac`.
**M34 / E34 / EV-038: REAL AS-106 ENGINEERING ACCEPTANCE PASS / COMPLETE.**
Prepared on `data/as-106-real-acceptance`; no algorithm development. Decisions
050/051 scientific bodies unchanged; Decision 052 absent.

Frozen sequence: `2023-04-03T06:46:21.024000Z` → April 28 target
`2023-04-28T06:46:29.024000Z`. M32 selection digest unchanged:
`570792066c1997b9a403249d994c4e7367bf2f1dafc6473b6e30df20cd6481d5`.
Four accepted typed AS-104/105 objects reconstructed from read-only, checksum-verified
handoffs. No metadata/raster/XML retrieval or public upstream processing. All shared
grid/comparison/policy contracts and known input counts validated before computation.

Real `as106-v1` product:
`hab_persistence:c576478b6b6d85894e5317e65a1d0fd6cee38ed1c406d452b10f97712d2cc3bb`.
**Target P=802; Q=793; A=7; B=7; C=0.** Candidate-history coverage **7/7 = 1.0**;
recurrence fraction **0/7 = 0.0**; no target candidates lack prior history. Streak
histogram on A: **1→7**. Previous-valid gap: **2,160,008,000,000 µs** wherever Q,
-1 elsewhere; all target candidate spans 0 µs, -1 outside candidates. The single
AS-105 target region/labels are preserved; no recurrent span exists (regional
recurrent-span summaries are None).

**No same-pixel candidate recurrence was observed among the 7 target candidate
pixels with valid prior observational history.** This is observational engineering
acceptance, not biological/event validation or absence of HAB. April 3's ~13%
upstream policy coverage is a separate denominator, not target-history coverage.
Shared five March references are not independent confirmation/statistical sufficiency;
exact pixels cannot track motion; the 25-day+8-second gap does not establish continuous
biological presence or absence. No risk/confidence/probability/accuracy/safety claim.

Independent Boolean/global/region/time oracles and **9/9 exact arrays/dtypes PASS**;
parent-aware validation, same/reverse-order repeat, creation-time identity exclusion,
input immutability/output non-aliasing and seven tamper controls (including rehash)
PASS. External four-file acceptance bundle is read-only (files 0444, directory 0555);
fresh offline typed bundle roundtrip PASS. Scientific network/public upstream/transport
attempts **0**. Integrity validators' internal regeneration is the approved exception.

**190 focused persistence / 993 full tests PASS; Ruff/diff/whitespace/security PASS**;
six existing full-suite Rasterio warnings. Local checks, not GitHub CI. Only eight
docs/evidence paths change; source/tests/config/dependencies unchanged. All pre-existing
accepted caches/handoffs/M29/M32/M33, recovery files, modes and both safety stashes
preserved. New M34 bundle stays outside Git.

Foundation/continuity complete → AS-101/102/103/104/105 merged → AS-106 M31 offline
implementation merged → M32 frozen inventory merged → M33 upstream handoff merged →
**M34 real engineering acceptance complete** → **owner review and separately gated
M35 publication/closeout next**. AS-106 is **not fully closed**.
**M35: NOT STARTED.** AS-107+ / P1 05.10 NOT STARTED; future AS-105 policy validation
NOT RUN. No PR or merge in this task; this owner-authorized M34 evidence commit/push
is not M35 formal publication/closeout.

See [M34 evidence](evidence/AS_106_REAL_ACCEPTANCE.md) and
[normalized evidence](evidence/AS_106_REAL_ACCEPTANCE.json).
Older dated M33/M32/M31/design states below are historical and remain intact;
their earlier authorization/unstarted/readiness statements are not current status.

## Historical AS-106 M33 upstream preparation — before PR #19 merge — 10 October 2026 (Asia/Dubai)

**M31: COMPLETE / MERGED via PR #17. M32: COMPLETE / MERGED via PR #18.**
Official M33 base: `200affdb7fb6f8801744a192511e4200cc0d100d`. **M33 / E33 / EV-037:
APRIL-3 UPSTREAM PREPARATION + VERIFIED HANDOFF PASS / COMPLETE.** Prepared on
`data/as-106-april3-upstream-preparation`; no algorithm development or new Decision.
Decisions 050/051 remain frozen; Decision 052 absent.

The M32 sequence remains April 3 + April 28, selection SHA-256
`570792066c1997b9a403249d994c4e7367bf2f1dafc6473b6e30df20cd6481d5`. Only the exact April 3 observation
`2023-04-03T06:46:21.024000Z` was newly processed through existing AS-102→103→104→105,
using the frozen PC 05.09 product, fixed five March references and unchanged policy.
April 28 was reconstructed read-only for comparison/integrity, not newly extracted.

April 3: AS-102 valid water **6,096**; all six AS-103 features valid **6,096**;
AS-104 five-history eligible support **784/794/793/793/793/789** in canonical feature
order; zero-MAD counts **0**. Common April 3/April 28 comparison contract **PASS**.
AS-105 policy-evaluable **P = 794**, candidates **88**, candidate/P **11.083123%**,
**15 regions / 35,200 m²**. This is frozen observational anomaly geometry, not HAB
confirmation. No date or threshold was changed after seeing the result.

The separate external read-only M33 handoff stores **88 arrays** plus typed metadata.
Fresh offline reconstruction of both April dates **PASS**; April 3 typed parent-aware
geometry validation, semantic hashes/IDs/statistics/regions **PASS**. Network, public
extraction and recurrence entrypoints were blocked in that readiness test; their
call counts are zero. Existing validator regeneration is an integrity check only.

**408 focused / 993 full tests PASS; Ruff PASS; diff/new-file whitespace PASS**;
six existing full-suite Rasterio PendingDeprecationWarnings. Local checks, not CI.
No source/test/config/dependency change. Pre-existing accepted caches, April 28
handoff/M29 bundle, M32 inventory, both safety stashes and recovery material remain
byte-identical; historical permissions retained. New April 3 cache/handoff stay out
of Git. No credentials/signed asset URLs persisted.

Foundation/continuity complete → AS-101/102/103/104/105 merged → Decisions
048/049/050/051 retained → AS-106 M31 offline implementation merged → M32 frozen
metadata inventory merged → **M33 April 3 upstream preparation complete** →
**M34 INPUTS READY; owner review and separate M34 authorization required**.
**M34 / M35: NOT STARTED. REAL AS-106 ACCEPTANCE: NOT RUN.** AS-106 is not yet
complete. AS-107+ / P1 05.10 NOT STARTED; future AS-105 policy validation NOT RUN.
No PR or merge in this task. Immediate priority: owner review of M33 evidence and
verified handoffs before separately authorizing real recurrence acceptance.

See [M33 evidence](evidence/AS_106_APRIL3_UPSTREAM_PREPARATION.md) and
[normalized evidence](evidence/AS_106_APRIL3_UPSTREAM_PREPARATION.json).
The dated M32/M31/design and older status sections below are historical checkpoints;
their earlier missing/unstarted/authorization states are retained, not current.
M33 evidence publication is not M35.

## Historical AS-106 M32 metadata inventory — before PR #18 merge — 10 October 2026 (Asia/Dubai)

**M31: COMPLETE AND MERGED** via PR #17 at implementation merge commit
`723e13a900dba30b73a8a2da39df1d984233a2f4`. **M32 / E32 / EV-036: METADATA-ONLY APRIL
ACQUISITION INVENTORY PASS / COMPLETE.** Decision 051's scientific body is
unchanged; no Decision 052. Inventory prepared on
`data/as-106-april-metadata-inventory`, directly from that official main base.
No active algorithm development in M32.

**12 CDSE records / 2 post-filter candidates / 2 exact PC 05.09 matches /
2 eligible acquisitions:** `2023-04-03T06:46:21.024000Z` (Sentinel-2A) and
`2023-04-28T06:46:29.024000Z` (Sentinel-2B). Every returned record has a
disposition; 10 excluded records fail frozen tile/orbit rules. All 11 required
AS-102 asset keys are present in both selected PC metadata records. April 28
reconciles to the accepted target product. No pixel-equivalence claim.

Selection inventory SHA-256:
`570792066c1997b9a403249d994c4e7367bf2f1dafc6473b6e30df20cd6481d5`.
The sequence was selected metadata-first, before existing-stage availability
was audited; no anomaly values, support fractions or candidate outcomes were
used. **10 metadata HTTP requests**, only to
`stac.dataspace.copernicus.eu` and `planetarycomputer.microsoft.com`;
complete pagination, no credentials needed, **ZERO asset requests / ZERO
imagery bytes**. No raster/XML/thumbnail fetch, signing or new-date processing.

April 3: AS-102/103/104/105 **missing in audited accepted artifacts**;
future status `needs_as102_as103_as104_as105`. April 28: all four stages
**present through verified cache/evidence/handoff identities**;
`already_complete_for_sequence`. Existing AS-103 PASS descriptors are evidence,
not a new AS-103 disk cache. An eligible preparation failure must be reported,
never silently remove a date or weaken a frozen contract.

**993 tests PASS; Ruff PASS; diff/new-file whitespace PASS**; six retained
Rasterio PendingDeprecationWarnings. No source/test/config/dependency change;
accepted caches, AS-104 handoff, M29 bundle, safety stashes and recovery material
are retained unchanged. These are local checks, not GitHub CI claims.

Foundation/continuity complete → AS-101/102/103/104/105 merged → Decisions
048/049/050/051 retained → AS-106 M31 offline implementation merged → M32
metadata-only sequence frozen → **owner review and separate M33 authorization
required**. **M33 upstream preparation / M34 real recurrence acceptance /
M35 publication-closeout: NOT STARTED. REAL AS-106 ACCEPTANCE: NOT RUN.**
AS-107+ / P1 05.10 NOT STARTED; future AS-105 comparative policy validation NOT
RUN. Immediate priority: owner review of this frozen inventory and the April 3
AS-102→103→104→105 prerequisite before any separately authorized preparation.

See [M32 evidence](evidence/AS_106_APRIL_METADATA_INVENTORY.md) and
[normalized inventory](evidence/AS_106_APRIL_METADATA_INVENTORY.json).
The dated M31 implementation, design-freeze and earlier states below are
historical; their old PR/merge/authorization/inventory states are preserved and
do not describe current M32. This metadata evidence publication is not M35.

## Historical AS-106 M31 offline implementation — before PR #17 merge — 10 October 2026 (Asia/Dubai)

**M31 / E31 / EV-035: OFFLINE IMPLEMENTATION + SYNTHETIC/ADVERSARIAL VALIDATION PASS.**
Decision 051 is merged through PR #16 at official base
`57185444f0cc963cc899a25cd8179d7a31f12119`; its scientific body is unchanged.
Feature branch: `feature/as-106-persistence`; isolated worktree
`/workspace/aquasentinel-813-as106`. Owner authorized implementation and final
commit/push with `feat: implement AS-106 persistence`; owner feature review is next.
**PR NOT CREATED; FEATURE NOT MERGED.** These are local engineering checks, not CI.

**190 focused persistence tests / 993 full tests PASS**; Ruff and tracked/new-file
whitespace checks PASS. Focused suite has no warnings; full suite retains only
six existing Rasterio PendingDeprecationWarnings. No dependency or upstream
source/test/config/provenance-schema/cache-format change.

Pure recurrence over validated AS-105 parents; UNKNOWN skipped, supported
noncandidate breaks, exact pixels only, UTC int64 microseconds, honest B/A and
C/B fractions. Existing AS-105 validator regeneration is permitted integrity
verification, not new extraction. Immediate lineage parents are AS-105 only.
Real artifacts remain preserved and were not used for AS-106 computation.

**REAL AS-106 ACCEPTANCE: NOT RUN / BLOCKED ON FUTURE DATA PREPARATION.**
**REAL APRIL SEQUENCE PREPARATION: NOT STARTED.** M32 metadata inventory, M33
upstream preparation, M34 real acceptance and M35 publication/closeout remain
**NOT STARTED** and separately gated. No EO/service network attempts or imagery
downloads. AS-107+ / P1 05.10 NOT STARTED; future AS-105 policy validation NOT RUN.
See [AS-106 specification](AS_106_PERSISTENCE.md) and [M31 validation](evidence/AS_106_PERSISTENCE_VALIDATION.md).

Earlier dated design-freeze/publication/merge checkpoints below are historical;
their old implementation/authorization states do not describe current M31.

## Historical AS-106 design freeze — 10 October 2026 (Asia/Dubai)

**Decision 051: OWNER-APPROVED / FROZEN DESIGN ONLY.** AS-105 remains COMPLETE
AND MERGED; Decisions 001–050 and completed M01–M30 history are preserved.
**AS-106 IMPLEMENTATION: NOT STARTED; no implementation authorization here.**
Prepared on `docs/as-106-design-freeze`, from approved main
`b1b5147d9973d8cf23d575985319bf94a55a03d4` (PR #15).
Real AS-106 acceptance: **BLOCKED ON FUTURE DATA PREPARATION**; earlier-April
eligible inventory remains unknown and no verified earlier-April cache exists.
M31–M35 / E31–E35 / EV-035–EV-039 are **future reservations, all NOT STARTED**.
Owner review of the published frozen design, then explicit M31 implementation
authorization, is next. Metadata-only M32 and upstream-data M33 are separate gates.
AS-107+ and P1 05.10: **NOT STARTED**; future AS-105 policy validation **REQUIRED /
NOT RUN**. No source/test/config/dependency change, real EO processing, EO-service
query, imagery download, PR or merge in this design-freeze task.
See [AS-106 frozen design](AS_106_PERSISTENCE.md) and Decision 051.

The dated AS-105 closeout and earlier checkpoint text below retains its historical
next-step/authorization meaning; it does not authorize or describe current AS-106 work.

## Historical AS-105 M30 closeout — 10 October 2026 (Asia/Dubai)

**AS-105: COMPLETE AND MERGED** via [PR #14](https://github.com/Omar-Aboulwafa/aquasentinel-813/pull/14).
**M30 / E30 / EV-034:** merge/publication closeout only; frozen Decision 050
implementation and M29 real engineering acceptance are now on official main.
**M28 implementation/adversarial validation PASS; M29 real engineering acceptance PASS.**
Decision 050 is **MERGED / unchanged**; no Decision 051 is created.
**AS-105 implementation merge commit:** `24a260cff130238c731f7cb62fc47eb74230b4dc`.
Merged **2026-10-10T06:24:09Z / 2026-10-10T10:24:09+04:00 Asia/Dubai**.
Implementation commit `57100b2e53e941f3a7fdfdfc40b61d2b4043c0e5`;
M29 documentation commit / final feature head `1ac9fab9db48cca5625ead20e7133c79101a46d8`.

Foundation/continuity complete → AS-101/102/103 merged → Decisions 048/049 merged → AS-104 COMPLETE AND MERGED → AS-105 M28 implementation/adversarial PASS → AS-105 M29 real engineering acceptance PASS → PR #14 MERGED → AS-105 COMPLETE AND MERGED → next milestone requires separate owner design review/authorization → AS-106+ NOT STARTED; P1 05.10 NOT STARTED.

Current active development branch: **none**. AS-105 development is closed.
This closeout was prepared on `docs/as-105-closeout`; AS-106+ is not authorized
and **NOT STARTED**. Immediate next step: **Owner review of the next milestone /
AS-106 design before implementation.** Future comparative policy validation:
**REQUIRED / NOT RUN**. P1 05.10 robustness: **NOT STARTED**.

Accepted M29 evidence is unchanged: target water **7,963**, P **802 / 10.071581%**,
**7 candidates / 0.872818% of P**, descriptive candidates/water **0.087907%**;
**projected-grid candidate area 2,800 m² / 0.0028 km²**. One region, zero one-pixel
regions, one MultiPolygon with three parts; F2/F4 votes, family counts **0, 7, 0, 7, 0**.
The corrected red_edge_red_ratio rank-.4/.6 counts remain **240/92**, not the earlier
238/93 chat transcription. No scientific identity, measurement or experiment time changed.

This proves reproducible candidate spectral anomaly geometry under frozen v1 only,
not HAB/bloom confirmation, concentration/species/toxins, causation, sensitivity,
specificity/accuracy/false-positive rate, persistence, risk/confidence, water safety,
intake exposure, alert or warning lead time. Rank is not probability/confidence/
significance/severity; families are not statistically independent. Five histories
are not statistical sufficiency; ~10% evaluable support is a material limitation.
No historical-event comparison or new real geometry/upstream processing was run.

All earlier M01–M29 / E01–E29 / EV-001–EV-033 and Decisions 001–050 are preserved.
The dated M28/M29 status blocks, milestone/evidence entries and their pre-merge
publication wording below are **historical checkpoints**, not current status.
Both safety stashes and external recovery artifacts remain retained; read-only
AS-104 handoff, M29 bundle and twelve accepted AS-102 cache hashes remain unchanged.
This closeout creates no PR and performs no merge. Local test results are not
GitHub CI success or scientific accuracy.

## Historical AS-105 M29 status — before PR #14 merge, 10 October 2026 (Asia/Dubai)

**M28: COMPLETE / COMMITTED / PUSHED**, implementation `57100b2e53e941f3a7fdfdfc40b61d2b4043c0e5`,
branch `feature/as-105-hab-anomaly-geometry`, remote
`origin/feature/as-105-hab-anomaly-geometry`, base main `4e322df220f8cab2805fccf9a2b32dd825f29218`.
**M29 / E29 / EV-033: REAL ENGINEERING ACCEPTANCE PASS; OWNER REVIEW PASS.**
Decision 050 remains unchanged; M29 is an execution/evidence checkpoint, not
Decision 051. The accepted AS-104 handoff was the only real input; no network,
upstream reprocessing or AS-102 cache loading, and no policy tuning.

Foundation/continuity complete → AS-101/102/103 merged → Decisions 048/049 merged → AS-104 COMPLETE AND MERGED → AS-105 M28 COMPLETE / COMMITTED / PUSHED → AS-105 M29 REAL ENGINEERING ACCEPTANCE PASS → owner review of M29 documentation/publication followed by PR preparation → AS-105 FEATURE NOT YET PR-MERGED → AS-106+ NOT STARTED; P1 05.10 NOT STARTED.

Target valid water **7,963**; policy-evaluable support P **802** (**10.071581%**
coverage diagnostic); candidates **7**, fraction **7/802 = 0.872818%** of P.
**Projected-grid candidate area: 2,800 m² / 0.0028 km².** One eight-connected
region, one MultiPolygon with three four-connected pieces; F2/F4 agreement.
P is not full AOI/ocean/risk coverage, and its coverage is not candidate fraction.
Sparse-history support remains material; no masks were relaxed.

Frozen real product: `hab_geometry:70876fbcb25e8a37abaa238a59e1da32fec9066792e6239db68e284b7bd18682`.
First extraction **2026-10-10T05:45:15.046037+00:00–05:45:15.173566+00:00** /
**09:45:15.046037–09:45:15.173566 +04:00 Asia/Dubai**;
acceptance completed **05:45:46.711968 UTC / 09:45:46.711968 +04:00**.
Execution/acceptance precede owner review and this later documentation publication;
no PR or merge timestamp exists. **PR NOT CREATED; FEATURE NOT YET MERGED.**

Independent masks/families/P/C, components, area and polygon round-trip PASS;
repeat **27/27 arrays**, parent immutability **61/61**, bundle read-back PASS.
M29 gates: **140 focused / 803 full tests PASS**, Ruff/diff PASS;
only six existing Rasterio PendingDeprecationWarnings. These are local checks,
not GitHub CI or scientific accuracy. External local evidence bundle:
`/workspace/aquasentinel-acceptance/as105/m29/`, **NOT tracked in Git**.

M29 establishes reproducible real candidate spectral anomaly geometry only. It does NOT establish confirmed HAB/bloom, chlorophyll concentration, species/toxins, biological causation, sensitivity/specificity/accuracy/false-positive rate, event agreement, persistence, risk/confidence, water safety, intake exposure, alert or warning lead time. No comparison with the historical April event was performed. Rank is not probability/confidence/significance/severity; policy families are not statistically independent. Five observations are not statistical sufficiency.
Future comparative policy validation: **REQUIRED / NOT RUN**, including
predeclared history-depth sensitivity; AS-106+ and P1 05.10 **NOT STARTED**.
Immediate next step: **owner review of M29 documentation/publication followed by
PR preparation**; no PR creation or merge in this task. All earlier M01–M28,
E01–E28, EV-001–EV-032 and Decisions 001–050 remain historical and preserved.
The old M28 status below describes its earlier checkpoint, not current status.
See [AS-105 contract](AS_105_HAB_ANOMALY_GEOMETRY.md) and [M29 validation](evidence/AS_105_HAB_ANOMALY_GEOMETRY_VALIDATION.md#m29--real-geometry-engineering-acceptance--10-october-2026).

## Historical AS-105 M28 status — before M29, 10 October 2026 (Asia/Dubai)

Owner-authorized **offline implementation only**; Decision 050 / M28 / E28 / EV-032.
**PASS — OWNER-REVIEWED / FEATURE PUBLICATION AUTHORIZED** on
`feature/as-105-hab-anomaly-geometry`, isolated worktree
`/workspace/aquasentinel-813-as105`, verified base
`4e322df220f8cab2805fccf9a2b32dd825f29218`.
Foundation/continuity complete → AS-101/102/103 merged → Decisions 048/049 merged
→ AS-104 COMPLETE AND MERGED → AS-105 frozen-policy offline implementation PASS
→ owner rank-granularity clarification accepted → feature publication
→ PR code review next after publication verification.

140 synthetic geometry cases PASS; full **803 passed**, Ruff/diff/whitespace
PASS; only six existing Rasterio warnings. No upstream algorithms, tests,
configuration, dependencies, provenance schema or cache format changed.
All 55 mandated adversarial requirements and controls A–E pass; this is
engineering evidence, not HAB accuracy. Rank is not probability/confidence/
significance/severity and evidence families are not independent measurements.

Real AS-105 geometry acceptance: **NOT RUN**; real counts/fraction/area/regions
remain **UNKNOWN**. Its future checkpoint is reserved and has **not been created**.
Future predeclared comparative policy validation: **REQUIRED / NOT RUN**;
AS-106+ and P1 homogeneous 05.10: **NOT STARTED**.
The owner authorized feature commit/push on 10 October 2026 after the final
quality/preservation gates. This record accompanies that feature publication;
verify the exact Git SHA/remote before PR review. **PR NOT CREATED; NOT MERGED.**
Real acceptance and future studies remain separately gated. The verified external
AS-104 handoff, twelve accepted cache hashes, both safety stashes and recovery
artifacts remain intact; the handoff is read-only and not tracked.

Earlier dated checkpoint status statements below retain their historical
meaning, including earlier AS-105 non-authorization and absence of Decision 050.
This M28 block governs current status; M01–M27/E01–E27/EV-001–EV-031 stay intact.

Owner-review clarification (same M28/Decision 050): with five histories,
no-tie empirical ranks are 0.0/0.2/0.4/0.6/0.8/1.0; the frozen 0.90 screen
requires all five below, or four below plus one exact tie. It is not a population
90th-percentile estimator or significance. Four synthetic regression cases pass.
Future predeclared history-depth sensitivity is required where valid EO permits;
choose exact depths before running it. M29 retains the accepted minimum-five
parent. No real geometry execution or new checkpoint.

See [AS-105 contract](AS_105_HAB_ANOMALY_GEOMETRY.md) and [M28 validation](evidence/AS_105_HAB_ANOMALY_GEOMETRY_VALIDATION.md).

**Historical AS-104 closeout status — 9 October 2026 (Asia/Dubai), M27/E27/EV-031:**
**AS-104: COMPLETE AND MERGED** through [PR #12](https://github.com/Omar-Aboulwafa/aquasentinel-813/pull/12).
**AS-104 implementation merge commit:** `472edc737847dc8581290a372c5da28f71fc48f0`.
Feature implementation commit: `09b38bd9c312470e948b1f17165ec5335cfc149d`.
Publication documentation commit / final PR head: `703af1176aeaf9ba38d31c53648907c3b1792aec`.
Merged **2026-10-09T09:26:08Z** / **2026-10-09T13:26:08+04:00 Asia/Dubai**.
Real acceptance **PASS**; no unresolved AS-104 P0 blocker. Known scientific and
coverage limitations remain documented. Current active development branch: **none**;
AS-104 development is closed. This closeout was prepared on `docs/as-104-closeout`.
Next step: owner review of the next milestone/AS-105 design before implementation;
separate authorization is required. AS-105+ and P1 homogeneous 05.10 **NOT STARTED**.
M23–M26/E23–E26/EV-027–EV-030 retain their dated historical blocker, fix, acceptance
and publication states, including then-pending PR/merge language. M27/E27/EV-031
records the later merge/closeout; it is an execution/history event, not Decision 050.
Both safety stashes and external recovery artifacts are retained historical recovery
material. No EO experiment rerun or source/test/math/cache changes in this closeout.
See [merge/closeout evidence §9](evidence/AS_104_TEMPORAL_BASELINE_VALIDATION.md#9-pr-12-merge-and-as-104-closeout--9-october-2026).

**Historical AS-104 publication status — before PR #12 merge, 9 October 2026 (Asia/Dubai), M26/E26/EV-030:**
Implementation and real acceptance **PASS**; feature commit
`09b38bd9c312470e948b1f17165ec5335cfc149d` is **COMMITTED AND PUSHED**,
parent/base `2006df7a70a4f48c66933aed96f4464d8d03084e`.
Branch `feature/as-104-temporal-baseline`; remote/upstream
`origin/feature/as-104-temporal-baseline`. Feature publication verified equal
local/remote SHA and a **clean worktree**. This reconciliation is documentation only.
**PR NOT YET CREATED; merge NOT YET PERFORMED.** Review the published commit and
open a PR if review passes and creation is authorized; this task creates no PR.
M23/E23/EV-027 remains historically BLOCKED; M24–M25/E24–E25/EV-028–EV-029 remain
acceptance-time PASS. Their earlier stop states below are historical, not current
Git status. M26/E26/EV-030 separates later publication from acceptance completion.
No Decision 050; both stashes/recovery artifacts retained; AS-105+ and P1 05.10
**NOT STARTED**. No science, source/tests, caches or experiment timestamps changed.
Exact publication metadata/times and unchanged acceptance evidence are in
[validation §8](evidence/AS_104_TEMPORAL_BASELINE_VALIDATION.md#8-as-104-feature-publication--9-october-2026).

**Historical platform-fix / cached acceptance checkpoint — before feature publication, 9 October 2026 (Asia/Dubai):**
The owner-authorized consistency predicate now compares `.casefold()` values only.
It does not strip punctuation/whitespace, map aliases, or rewrite stored platform
strings, source records, products, fingerprints or caches. Acquisition and all
other provenance/compatibility checks remain unchanged. Only
`temporal/baseline.py` and `tests/temporal/test_identity_lineage.py` changed in
source/tests: one predicate and 20 regression cases. The reverse-case unit case
isolates this predicate; the existing descriptor schema still requires lowercase
observation platforms. Full-API tests use the real lowercase-observation /
mixed-case-source pattern for both Sentinel-2A and Sentinel-2B.

M24/E24/EV-028 records the bug fix, with **132 temporal tests PASS** and the
pre-rerun combined **663 passed**, Ruff/diff PASS, six historical Rasterio warnings.
M25/E25/EV-029 records **real acceptance PASS**, reusing all six known-ID 05.09
AS-102 caches with no network or imagery reprocessing. Unchanged AS-103
reconstruction reproduced all six accepted IDs/content fingerprints. All 12
cache-file hashes remain identical. The exact five March acquisitions, April-28
target, March half-open window and minimum five were retained.

Cached rerun: **08:01:50.383608–08:01:51.327507 UTC** /
**12:01:50.383608–12:01:51.327507 +04:00 Asia/Dubai**. On the unchanged 20 m
EPSG:32640 310×228 grid, all features have 7,963 target-supported pixels.
Baseline/z/rank counts in approved feature order are
**792 / 802 / 801 / 801 / 801 / 797**; insufficient counts are
**7,171 / 7,161 / 7,162 / 7,162 / 7,162 / 7,166**. Zero MAD and both numerical
rejection counts are zero for every feature. Sparse history remains masked;
five scenes are not five valid observations at every pixel.

**18/18 independent scalar checks PASS**, synthetic later-scene addition/mutation
causal check PASS, deterministic repeat PASS, input immutability PASS.
Product: `temporal:e814b0574ab30d1841778ee3c5005ffcb313ab42473c41acc028f0a9f7804a8b`.
Immediate provenance parents are target AS-103 first, then R1–R5 chronologically;
each branch retains actual PC → AS-102 → AS-103 → AS-104 lineage. The future
control is synthetic and excluded, not evidence of future EO availability.
Full counts, summaries, fingerprints, parents and scalar records are in
[validation §§6–7](evidence/AS_104_TEMPORAL_BASELINE_VALIDATION.md).

M23/E23/EV-027 remains the earlier **BLOCKED** platform-casing attempt; its body
and all prior checkpoint/decision bodies remain preserved. No Decision 050.
Both retained stashes and old/new external recovery artifacts remain available.
AS-104 stays **UNCOMMITTED / READY FOR REVIEW**. Owner review is the next gate;
no commit/push/PR/merge, AS-105+, or P1 homogeneous-05.10 experiment. PASS is
engineering acceptance of temporal candidate BOA signals, not biological or
operational accuracy, risk, persistence, alert or warning-lead-time validation.
Earlier dated checkpoint statements below are historical; this update governs
current state. Final quality/security verification is recorded in validation §7.

**Created:** 6 October 2026

**Evidence-pack update:** 6 October 2026 (Asia/Dubai). The [claim index](evidence/PRESENTATION_EVIDENCE_INDEX.md) and [CDSE](evidence/AS_102_CDSE_ACCESS_PROBE.md) / [Planetary Computer](evidence/AS_102_PLANETARY_COMPUTER_PROBE.md) reports now preserve the owner's supplied reconstruction of earlier investigations. The PC record is the historical checkpoint before a bounded raster read, not a later final-gate result. Original experiment timestamps, raw transcripts, and screenshots remain capture gaps; no live probe was rerun for this update.

**Later gate update:** 6 October 2026 (Asia/Dubai), stage FG-01. The separate [final PC raster-gate report](evidence/AS_102_PLANETARY_COMPUTER_RASTER_GATE.md) records the owner's supplied results of a later successful experiment. M09–M13 and the original PC report preserve their earlier checkpoint; M14 adds the later PASS / READY stage. No experiment was rerun for this documentation update, and original experiment timestamps remain unspecified.

**Historical PR #10 integration checkpoint — 9 October 2026 (Asia/Dubai):** Decision 048 is
merged through PR #10 at `39f2aee90c727fc151886efbdea44daec0e3f9b4` (fix commit
`c9a415b65a101319e9c9f2fef21ad0dcd44c9347`). The existing AS-104 branch was
fast-forwarded from `c6accab2c5753734466a6375d1b3ce1762e99bed`, then its retained
safety stash was applied. Genuine documentation conflicts were reconciled;
all ten restored AS-104 files matched the pre-integration SHA-256 inventory.
Temporal source/tests remain byte-for-byte unchanged. The combined offline gate
passed: **533 tests**, Ruff/diff checks, the same six Rasterio warnings.
The original Decision 047 → 048, M19 → M20, E18 → E19 → E20 and
EV-022 → EV-023 → EV-024 bodies/statuses are preserved in order. Their
cross-worktree/pending-merge wording describes the original dated checkpoints.
The frozen April 28 / exactly-five March / minimum-five / delivered-05.09 real
acceptance was resumed in three separately timestamped attempts. All stopped at
March 4 asset signing; a bounded diagnostic observed intermittent HTTP 504 and
successful responses for the same assets. The third attempt read SCL but
exhausted five attempts signing B02. **Real acceptance remains BLOCKED**: zero
completed reference scenes and no real temporal product. No scientific/mask/math/
grid contract was relaxed. Implementation remains uncommitted; see
[resumed evidence](evidence/AS_104_TEMPORAL_BASELINE_VALIDATION.md) / M21/E21/EV-025.
**P1 Processing Baseline Robustness Experiment — NOT STARTED**: homogeneous
05.09 versus homogeneous 05.10 requires separate authorization and is not
accuracy validation. AS-105+ is NOT authorized and NOT started. No commit,
push or PR in this integration task; retain the verified safety stash.

**Purpose:** Source of truth for the hackathon presentation narrative and its supporting evidence.

**Initial journal repository snapshot:** `cf1ed231348d60feae190cb79a5d94e9bf194c85`; locally available `origin/main`: `acbe2c113006922cfe3ffb9813165b16fa48c75f`. Their tracked file trees are identical.

**AS-102 closeout checkpoint:** 8 October 2026 (Asia/Dubai), M16 / EV-018. AS-102 is COMPLETE AND MERGED through [PR #6](https://github.com/Omar-Aboulwafa/aquasentinel-813/pull/6), implementation `fe3d27046c40600010753957ee8921d57071ec48`, merge `627b6ae8a509509dbb2d5d43bbdc6d74e0ce2aac`. Final reviewed baseline: 265 tests passed, Ruff/diff checks passed; six non-blocking Rasterio warnings. No configured/reported GitHub CI checks. M15 / EV-016–EV-017 preserve the earlier implementation acceptance and its 213-test result; historical reconstruction entries and probe reports remain preserved.

**Scope:** Historical reconstruction plus separately authorized AS-102/AS-103/AS-104 implementation, evidence and publication updates. This journal records decisions and experiments; it does not grant AS-103 or Git publication authorization.

This journal indexes repository evidence. It does not replace the [project state](PROJECT_STATE.md), [decision log](DECISIONS.md), [handoff](HANDOFF.md), or [PRD](AquaSentinel_813_PRD_v1.0.md). Those documents govern scope and authorization. Code/tests and Git history establish implementation history; a recorded live result establishes only the experiment it describes.

Status labels used throughout:

- **Completed fact:** supported by repository implementation, documentation or Git history; commit/merge status is reported separately.
- **Current decision:** an explicitly approved decision, cited by number; this journal records it without granting authorization.
- **Recorded experiment:** a documented observation, with its date and limits.
- **Provider/STAC-advertised metadata:** reported item/asset properties, distinguished from independently read raster headers/pixels.
- **Inference / recommendation / blocker / unverified claim:** conclusions, suggested next steps, obstacles, and missing verification are labelled separately in the probe records.
- **Evidence gap:** a requested story point without a supporting tracked report; outcome and date remain unverified from repository evidence.
- **Future plan:** intended work or proposed presentation material; neither implemented nor authorized by this journal.

Dates follow the source documents when they describe an event. Git dates retain their timezone when precision matters: AS-101 commits dated 2 October in UTC fall on 3 October in UAE time. The PRD delivery calendar is a plan, not a completion record. Lessons and presentation takeaways below are retrospective interpretations of the cited evidence, not claims of measured operational impact.

**Historical AS-103 acceptance checkpoint:** 8 October 2026, M17 / EV-019–EV-020: six candidate features, 7,963 valid pixels each, two unclipped NDCI-like out-of-range values, verified immediate-parent lineage and 348-test branch baseline. Uncommitted/unpushed/unmerged; AS-104 unauthorized.

**Historical AS-103 closeout update:** 8 October 2026 (Asia/Dubai), M18 / EV-021. AS-103 is **COMPLETE AND MERGED** through [PR #8](https://github.com/Omar-Aboulwafa/aquasentinel-813/pull/8). Implementation `5638bc8b4ab06f235f908642f714a7cc83b35709`; AS-103 implementation merge commit `b770d0561da9ac2b81ca2d4b8e784adff66ee231`, merged `2026-10-08T10:43:24Z` / `2026-10-08T14:43:24+04:00` Asia/Dubai. Final reviewed baseline: 348 tests passed, Ruff/diff checks passed; six existing non-blocking Rasterio PendingDeprecationWarnings only, no new AS-103 warnings. No GitHub Actions/workflow CI run was configured/reported. M17 / EV-019–EV-020 preserve the earlier acceptance checkpoint and experiment timestamp; no replacement real-scene experiment is claimed. AS-104 NOT authorized and NOT started.

**Historical AS-104 checkpoint — 8 October 2026 (Asia/Dubai):** Decision 047 explicitly
authorized temporal implementation. M19 / E18–E19 / EV-022–EV-023 records the
uncommitted offline PASS and separately BLOCKED real attempt. This supersedes
older AS-104 status statements without rewriting M01–M18 or their evidence.
AS-105+ remains unauthorized and unstarted. No commit, push or PR.

## 1. Executive project story

**Historical PR #11 acceptance checkpoint — 9 October 2026 (Asia/Dubai):**
Decision 049 is merged through PR #11 at
`2006df7a70a4f48c66933aed96f4464d8d03084e` (fix commit
`9181e0da40898f5c729b8596367bb3e4719317d0`). The branch was fast-forwarded and
its NEW safety stash applied without dropping either stash. Four genuine
documentation conflicts were reconciled; all eight temporal source/test hashes
remain unchanged. Combined offline gate: **643 passed**, Ruff/diff PASS, six
existing Rasterio warnings. Decisions 046→047→048→049, milestones M18–M22,
engineering E17–E22 and detailed evidence EV-021–EV-026 coexist in order without
renumbering or duplicated bodies; earlier statuses remain historical.

The frozen 05.09 April-28 / exactly-five March / minimum-five real experiment ran
07:31:08.630215–07:31:57.353103 UTC / 11:31:08.630215–11:31:57.353103 Dubai.
**5/5 March AS-102 and AS-103 scenes completed** with normal production transport,
unchanged EPSG:32640 310×228 grid and masks. Valid-water counts:
8,674 / 2,092 / 7,350 / 3,834 / 6,156. Accepted April cache/feature IDs remain
unchanged; target supports 7,963 pixels per feature. March 4 has 52 denominator
exclusions in B04-denominator features; March 14 has 20 green/blue exclusions.

**AS-104 real acceptance is BLOCKED**, now at its target provenance guard:
`observation_match.platform` is `sentinel-2b`, but actual PC `SourceRecord.platform`
is `Sentinel-2B`. All three target acquisition timestamps agree. The unchanged
case-sensitive comparison at `temporal/baseline.py:105–110` rejects the target
before numerical reduction. March products have the corresponding same casing
mismatch. Transport succeeded; this is a representation/validation blocker, not
measured zero temporal support. No history distributions, temporal summaries,
AS-104 fingerprints/ID/lineage, scalar checks, future control or deterministic
repeat were produced/run. No code/test/cache-contract change or workaround.

M23/E23/EV-027 records this factual attempt, with full safe scene statistics,
IDs/fingerprints, support and diagnostic metadata in
[AS-104 validation](evidence/AS_104_TEMPORAL_BASELINE_VALIDATION.md#5-pr-11-integration-and-five-reference-0509-attempt--9-october-2026).
Owner review/authorization of a targeted platform-representation fix and realistic
metadata tests is the next gate; do not mutate source records or accepted caches
to bypass it. AS-104 remains uncommitted for review. No new Decision 050, commit,
push, PR or GitHub merge; only the required local ff-only integration occurred.
AS-105+ and P1 homogeneous-05.10 study NOT started. No hazard, science accuracy,
operational risk, persistence, alert or warning-lead-time claim.

**Historical Decision 048 fix checkpoint — 8 October 2026:** The owner separately authorized
AS-104, whose uncommitted work and real-acceptance blocker are preserved in its
original worktree. This separate upstream fix uses M20/E20/EV-024. M19/E18–E19/
EV-022–EV-023 and Decision 047 remain only in that worktree, reserved and not copied
here per owner clarification. Prior AS-103-closeout authorization statements
above/below describe their historical checkpoints; this update governs current
state. The fix is uncommitted for review; AS-104 acceptance is still BLOCKED.

**Historical Decision 049 fix checkpoint — 9 October 2026:** Decision 048 is merged via
PR #10 at `39f2aee90c727fc151886efbdea44daec0e3f9b4`. Resumed AS-104 encountered
intermittent per-asset authentication HTTP 504s. This later, separately authorized
transport fix uses Decision 049/M22/E22/EV-026; it remains uncommitted for review.
The unchanged AS-104 worktree owns Decision 047/M19/E18–E19/EV-022–EV-023 and
M21/E21/EV-025; their record bodies are not imported or renumbered here. Historical
M01–M20/E01–E20/EV-001–EV-024 retain checkpoint meaning. AS-104 real acceptance
remains BLOCKED pending transport-fix review/merge; AS-105+ and P1 homogeneous-
05.10 experiment NOT started.

**Product thesis / current decisions:** AquaSentinel 813 competes in Track 03 — Water Security & Marine Environments. It targets the Desalination Plant Water Quality / Operations Manager and the question: **Where and when should monitoring or field verification be prioritized?** The intended value is offshore awareness before a threat reaches an intake, with evidence, confidence, exposure, and human verification. Sources: Decisions 001–004 and PRD sections 1–5 and 22.

The P0 product vision contains two separately interpretable hazards: Sentinel-2 HAB-like biological anomalies first, and Sentinel-1 oil-slick candidates second. Hyperspectral characterization, SST, currents, wind, and advanced drift are P1 enhancements. Transparent anomaly/risk logic precedes fitted ML; risk weights are hypotheses. These are design commitments, not delivered hazard capabilities. Sources: Decisions 005–015 and 034.

**Completed facts:** The repository first established reproducible packaging, validated configuration/AOI inputs, and provenance. Continuity documents and read-only Codex onboarding preceded explicit AS-101 authorization. AS-101 now discovers deterministic, fully paginated Sentinel-2 L2A candidates and converts them to provenance. It was merged through [PR #2](https://github.com/Omar-Aboulwafa/aquasentinel-813/pull/2) at `1b83a732155ee01c01b7d33cb50115725cfb08c3`; post-merge documentation was merged through [PR #3](https://github.com/Omar-Aboulwafa/aquasentinel-813/pull/3) at `acbe2c113006922cfe3ffb9813165b16fa48c75f`.

**Recorded experiment:** A 2 October CDSE metadata search returned 44 unique candidate scenes for the analyst-defined Al Raha validation polygon, 1 March–31 May 2023, with scene cloud cover <= 30%. Provenance conversion/serialization succeeded for 44/44. The recorded quality baseline is 97 tests, Ruff passed, and `git diff --check` passed. Source: [AS-101 report](AS_101_STAC_SEARCH.md).

**Current repository phase:** Foundation/continuity complete → AS-101/102/103/104/105 MERGED → Decision 051 MERGED/FROZEN → AS-106 M31 OFFLINE IMPLEMENTATION/SYNTHETIC VALIDATION PASS → owner feature review next (PR NOT CREATED / FEATURE NOT MERGED) → real April acceptance BLOCKED ON FUTURE DATA PREPARATION → M32–M35 / AS-107+ NOT STARTED; future AS-105 policy validation NOT RUN; P1 05.10 NOT STARTED.

**Presentation boundary:** Catalog discovery alone proves metadata availability. The historical reports retain advertised CDSE scale/offset, its access blocker, PC catalog/COG metadata, and the same-acquisition/different-product finding. At that earlier checkpoint, signing, decoding, and bounded reads remained unverified and EV-014 was PENDING. The later FG-01 experiment establishes credential-free signing, bounded B02/B05/SCL reads, and XML-driven B02/B05 decoding for the tested PC product/path: EV-014 later stage PASS / READY, EV-015 decoding evidence. Neither stage proves final usable-water pixels, HABs, chlorophyll concentration, toxins, water safety, warning lead time, or operational intake risk. Those historical stages did not authorize a provider change or implementation. The separately authorized M15 / EV-016–EV-017 now records actual full-AOI AS-102 arrays/masks/lineage/cache and Decisions 039–045; M17 / EV-019–EV-020 records the later candidate-feature acceptance; M18 / EV-021 separately records final review and merge through PR #8. At that AS-103 closeout checkpoint, AS-104 was NOT authorized and NOT started; M25–M26 separately record its later accepted and published implementation. These mask outcomes also do not establish the scientific/operational claims above.

## 2. Chronological milestone timeline

Each milestone preserves its status and next-step instructions at the recorded
time. M26 separately records publication; M27 records the later PR #12 merge
and closeout. Their earlier next-step instructions remain historical.

### M01 — Track 03 selection and product thesis

- **Date:** Recorded in continuity documents committed 2 October 2026 (`5f67e5d`); original selection date is not recorded.
- **Task / milestone ID:** Product definition; Decisions 001–018.
- **Status:** Current decisions; product capabilities remain a PoC goal.
- **Problem / question:** How can EO support a concrete coastal water-security decision?
- **Why it mattered:** A defined operator and action give the project a defensible use case.
- **Options considered:** Generic marine monitoring, algae detection alone, oil mapping alone, and operational intake intelligence are contrasted in Decisions 002–004; no scored track comparison is recorded.
- **Decision:** Track 03; multi-hazard intake intelligence, HAB primary and oil secondary, with human verification.
- **Rationale:** UAE/Gulf relevance, suitable sensors, public-sector/utility users, and a clear operational value chain.
- **Implementation / experiment:** Frozen PRD and decision log; no customer or operational-impact experiment recorded.
- **Evidence:** [Decisions 001–018](DECISIONS.md); [PRD sections 1–5, 22–23](AquaSentinel_813_PRD_v1.0.md); commit `5f67e5d`.
- **Quantitative result:** Two P0 hazard classes planned; no measured warning lead time, avoided downtime, or buyer validation.
- **Limitation:** Al Raha is a validation study area, not a desalination intake; business models are hypotheses.
- **Lesson learned:** The user decision should determine the sensor and evidence design.
- **Impact on next step:** Prioritize Sentinel-2 discovery and scientific traceability before advanced models/UI.
- **Presentation takeaway:** “Watch offshore; explain the evidence; prioritize verification.”
- **Recommended visual:** Proposed operator → observation → evidence → monitoring-priority diagram; not yet captured.
- **Candidate slide title:** “A water-security decision, grounded in offshore evidence.”

### M02 — AS-001 repository foundation

- **Date:** 2 October 2026; initial commit at `14:14:18+04:00`.
- **Task / milestone ID:** AS-001 — Repository Scaffold.
- **Status:** Completed fact.
- **Problem / question:** How can development be reproducible and isolated from other office-machine projects?
- **Why it mattered:** The project must run across office, personal, and cloud environments without moving secrets.
- **Options considered:** Python 3.11 isolation versus newer machine Python versions; `src/` layout versus root imports; personal Git identity separate from company access. No benchmark comparison recorded.
- **Decision:** Python 3.11, `src/aquasentinel`, editable installation, pytest/Ruff, repository-local personal Git setup.
- **Rationale:** Scientific ecosystem compatibility and clean package/account isolation.
- **Implementation / experiment:** Packaging, README, ignore rules, environment example, initial package and smoke test.
- **Evidence:** `f878acc chore: scaffold AquaSentinel 813 project`; [Project State §6](PROJECT_STATE.md); [pyproject.toml](../pyproject.toml); [smoke test](../tests/test_smoke.py); Decisions 021–022 and 027–029.
- **Quantitative result:** Python major/minor pinned to 3.11; a separate initial passing-test count is not documented here.
- **Limitation:** Packaging proves infrastructure, not EO or hazard functionality.
- **Lesson learned:** Reproducibility begins with a small runnable package and an explicit quality gate.
- **Impact on next step:** AS-002 can add validated runtime inputs on a stable foundation.
- **Presentation takeaway:** The project started with repeatable engineering rather than a one-machine demonstration.
- **Recommended visual:** Proposed package tree plus setup/test commands; capture pending.
- **Candidate slide title:** “A foundation that another machine can reproduce.”

### M03 — AS-002 configuration and AOI model

- **Date:** 2 October 2026; feature `14:43:36+04:00`, merge `14:46:36+04:00`.
- **Task / milestone ID:** AS-002 — Configuration & AOI Model.
- **Status:** Completed fact; associated AOI decisions remain current.
- **Problem / question:** How can site, dates, thresholds, and risk assumptions vary without editing source code?
- **Why it mattered:** Invalid geometry or hidden assumptions can contaminate subsequent EO analysis.
- **Options considered:** Hard-coded settings versus TOML; transparent GeoJSON AOI versus an implied operational intake. Sources: Decisions 017–018 and 023–024.
- **Decision:** Validated TOML settings, GeoJSON features/roles, and a runtime context combining them.
- **Rationale:** Human-readable inputs, interoperability, explicit validation, and scientific honesty about the study area.
- **Implementation / experiment:** Date/cloud/risk validation; point/polygon/range/closure checks; duplicate feature-ID rejection; role lookup and runtime construction.
- **Evidence:** Feature `f606ac5`, merge `113ca44`; [configuration package](../src/aquasentinel/config/); [runtime](../src/aquasentinel/runtime.py); [AOI](../data/aoi/demo_site.geojson); [configuration tests](../tests/config/); Project State §7.
- **Quantitative result:** Configured analysis window 1 March–31 May 2023 and cloud threshold 30%; these are settings, not measured performance.
- **Limitation:** The analyst-defined Al Raha polygon and public reference point are neither an official boundary nor an intake; risk weights are unvalidated hypotheses.
- **Lesson learned:** Configuration must preserve the meaning of an AOI as well as its coordinates.
- **Impact on next step:** AS-101 receives validated search inputs; future operational-site selection remains separate.
- **Presentation takeaway:** “A study area is explicit, configurable, and honestly labelled.”
- **Recommended visual:** Proposed AOI map with “validation polygon” and “public reference point” labels; not yet captured.
- **Candidate slide title:** “Define the question geographically before searching.”

### M04 — AS-003 provenance before ingestion

- **Date:** 2 October 2026; feature `15:03:29+04:00`, merge `15:04:59+04:00`.
- **Task / milestone ID:** AS-003 — Provenance Model.
- **Status:** Completed fact; end-to-end hazard lineage is still future work.
- **Problem / question:** How will a future alert remain traceable to observations and processing versions?
- **Why it mattered:** Source identity lost during ingestion cannot be recovered reliably from a final risk map.
- **Options considered:** Ingest first and retrofit lineage versus build provenance first; Decision 019 explicitly adopts the latter.
- **Decision:** Typed source/derived records, validation, serialization, registry, recursive lineage, and JSON persistence.
- **Rationale:** Traceability must be available when the first real scenes arrive.
- **Implementation / experiment:** Reject duplicate IDs, missing upstream references, naive timestamps, and non-JSON processing parameters; restore multi-step dependencies from manifests.
- **Evidence:** Feature `e2baedc`, merge `db79260`; [provenance package](../src/aquasentinel/provenance/); [provenance tests](../tests/provenance/); Project State §§8–9; Decisions 019–020.
- **Quantitative result:** Provenance schema `1.0`; historical whole-project baseline **17 tests passed**, Ruff passed, as recorded at AS-003 completion.
- **Limitation:** A tested lineage registry is not evidence of a delivered feature → hazard → risk → alert pipeline.
- **Lesson learned:** Scientific explanations require traceable inputs, not just readable scores.
- **Impact on next step:** Every AS-101 candidate can be validated as an existing `SourceRecord` without replacing the provenance model.
- **Presentation takeaway:** “Every future result should answer: which source and which processing?”
- **Recommended visual:** Proposed source → feature → hazard → risk → alert diagram, distinguishing implemented registry from future products.
- **Candidate slide title:** “Build the evidence trail before the data flows.”

### M05 — AS-000C continuity and Codex onboarding

- **Date:** 2 October 2026; continuity merge `ccf38d3`, onboarding recorded at `779069d`, onboarding documentation `a01ae65` merged via PR #1 at `51f4ede`.
- **Task / milestone ID:** AS-000C.1–AS-000C.8.
- **Status:** Completed fact, including separate explicit AS-101 development authorization.
- **Problem / question:** Can a fresh developer/agent recover scope, scientific constraints, architecture, and next actions without chat memory?
- **Why it mattered:** Multiple machines and context loss make undocumented knowledge a delivery risk.
- **Options considered:** Conversation-dependent continuity versus repository documents; immediate coding versus first read-only onboarding.
- **Decision:** Repository as source of truth; startup checks and read-only audit before a separately authorized development handoff.
- **Rationale:** Validate understanding before allowing code changes, while preserving personal/company account separation.
- **Implementation / experiment:** AGENTS, state, decisions, PRD, handoff, and plan guidance; documented audit of config/AOI, provenance, tests, and architecture.
- **Evidence:** Commits `5f67e5d`, `160a2dd`, `ccf38d3`, `779069d`, `a01ae65`, `51f4ede`; [AGENTS](../AGENTS.md); [execution plans](../.agent/PLANS.md); Project State §13; Handoff §§16–19; Decisions 025–028 and 035–037.
- **Quantitative result:** Eight continuity/onboarding/handoff subtasks recorded complete; onboarding date 2 October. No onboarding performance metric recorded.
- **Limitation:** The full standalone onboarding audit is not a tracked artifact in this snapshot; completion is recorded by the continuity documents.
- **Lesson learned:** A reviewed read-only understanding check is distinct from implementation permission.
- **Impact on next step:** AS-101 becomes the first expressly authorized Codex development task; later milestones still require authorization.
- **Presentation takeaway:** “An agent handoff is reproducible project context, not conversation memory.”
- **Recommended visual:** Proposed continuity-file map and onboarding → authorization → development sequence.
- **Candidate slide title:** “Make the project recoverable before adding complexity.”

### M06 — AS-101 deterministic Sentinel-2 STAC discovery

- **Date:** Implemented/validated 2 October 2026 per AS-101 report; feature commit `2026-10-02T20:05:10Z`; merged 3 October at `00:24:55+04:00`.
- **Task / milestone ID:** AS-101 — Sentinel-2 STAC Search.
- **Status:** Completed fact; current provider decision is Decision 038.
- **Problem / question:** Which real L2A products intersect the validation AOI within the configured dates/cloud limit?
- **Why it mattered:** Downstream processing needs real, deterministic, provenance-bearing candidates before raster work.
- **Options considered:** Catalog-first versus full imagery work; STAC client versus maintaining a custom protocol; minimal dependency versus the PRD's broader future geospatial stack. No recorded provider benchmark.
- **Decision:** Configurable CDSE STAC (`https://stac.dataspace.copernicus.eu/v1/`, `sentinel-2-l2a`), using only new direct dependency `pystac-client==0.9.0`.
- **Rationale:** Owner-selected provider, STAC pagination support, bounded request waits, and scope protection.
- **Implementation / experiment:** Polygon `intersects`; inclusive UTC days; cloud query and local rechecks; complete GET/POST pagination; typed sorted candidates; duplicate/conflict rules; provider-qualified source IDs.
- **Evidence:** Feature `41a0b0b217cace909c906b7aedcb9cc6d0026f53`; documentation `b3f0e9f878375f5fbfccb35519eeac5cc8fa48af`; merge `1b83a732155ee01c01b7d33cb50115725cfb08c3`; [catalog](../src/aquasentinel/catalog/stac.py); [ingestion](../src/aquasentinel/ingestion/sentinel2.py); [AS-101 report](AS_101_STAC_SEARCH.md); Decisions 030–031 and 038.
- **Quantitative result:** Configurable 30-second per-request timeout; no result cap; initial historical quality gate 92 tests passed at `b3f0e9f`, later superseded by 97.
- **Limitation:** Per-request timeout is not a total search deadline. Asset references contain key/href/type/roles, not a reflectance-decoding or raster-alignment contract.
- **Lesson learned:** Complete pagination and explicit metadata failures protect against plausible-looking partial results.
- **Impact on next step:** AS-102 must establish actual asset access and pixel semantics; AS-101 does not establish either.
- **Presentation takeaway:** “Find real observations completely, and preserve their identity.”
- **Recommended visual:** Proposed query → pagination → sorted candidates → `SourceRecord` diagram; capture pending.
- **Candidate slide title:** “From an AOI question to traceable satellite candidates.”

### M07 — Real CDSE search: 44 candidates and 44 valid source records

- **Date:** 2 October 2026, as recorded in AS-101 documentation.
- **Task / milestone ID:** AS-101 real-data smoke test.
- **Status:** Recorded experiment; not a raster or event-validation experiment.
- **Problem / question:** Does the implemented search work against the real selected provider?
- **Why it mattered:** Offline protocol tests alone cannot demonstrate real catalog coverage.
- **Options considered:** Fixture-only acceptance versus a real metadata smoke test; execution plans require live evidence for external-data work.
- **Decision:** Query configured Al Raha polygon, 1 March–31 May 2023, cloud cover <= 30%, and validate every returned source record.
- **Rationale:** Exercise the actual integration while staying inside metadata-only scope.
- **Implementation / experiment:** Live credential-free HTTPS metadata search, followed by provenance conversion and serialization; reproduction command retained in the AS-101 report.
- **Evidence:** [AS-101 “Recorded real-data result” and reproduction](AS_101_STAC_SEARCH.md); Decision 038; commit `b3f0e9f`.
- **Quantitative result:** **44 unique candidate scenes; 44/44 provenance conversions/serializations**. Earliest `2023-03-04T06:47:51.024Z`; latest `2023-05-28T06:46:29.024Z`; scene cloud range **0.12–24.96%**; first candidate retained **47 asset references**.
- **Limitation:** Products can overlap tiles; 44 is not a count of independent dates. Scene cloud percentage is not AOI water-pixel quality. Catalog reprocessing may change future counts.
- **Lesson learned:** Live discovery and scientific usability are separate acceptance questions.
- **Impact on next step:** Investigate usable raster windows, scale/offset, masks, and alignment before deriving features.
- **Presentation takeaway:** “44 real candidate products, all traceable; water analysis still to be established.”
- **Recommended visual:** Proposed observed-count card and acquisition span with the query constraints printed beside it; do not invent a complete per-date plot from five example items.
- **Candidate slide title:** “The first live evidence: 44 candidate observations.”

### M08 — Review fix, 97-test baseline, and post-merge closeout

- **Date:** Review commits `2026-10-02T20:21:40Z` and `20:21:46Z`; PR #2 and closeout PR #3 merged 3 October 2026.
- **Task / milestone ID:** AS-101 final review and documentation closeout.
- **Status:** Completed fact; 97 is the recorded current quality baseline.
- **Problem / question:** Could a TOML boolean cloud threshold silently become numeric, and did documents accurately reflect committed/merged state?
- **Why it mattered:** `float(True)` would disguise invalid input and weaken the configured scientific filter.
- **Options considered:** Coercion versus rejecting booleans/non-numeric values before conversion. The implemented fix stays local to the cloud threshold.
- **Decision:** Preserve integer/float input; reject boolean/string input before any catalog request; update review and merge status without starting the next milestone.
- **Rationale:** Strict meaning at the configuration boundary and a trustworthy handoff.
- **Implementation / experiment:** Loader type check; parameterized valid thresholds `30`, `12.5`; invalid `true`, `false`, and `"30"` with zero catalog calls. Documentation preserved the 17-test historical baseline.
- **Evidence:** Fix `f57f6bf23e5a7d7eb97c190e5d0308e20d46ca37`; review docs `35caa900597773b4eecf9271ecee22d1b43ebe32`; closeout `cf1ed231348d60feae190cb79a5d94e9bf194c85`; [loader](../src/aquasentinel/config/loader.py); [focused tests](../tests/config/test_catalog.py); PR #2 merge `1b83a73`, PR #3 merge `acbe2c1`.
- **Quantitative result:** Five added parameterized cases; baseline **92 → 97 tests passed**, all 17 original tests retained; Ruff and diff check passed.
- **Limitation:** Test count measures executed cases, not algorithm accuracy, EO water suitability, or code coverage percentage.
- **Lesson learned:** Small type-coercion defects can alter scientific settings; documentation state requires review too.
- **Impact on next step:** AS-101 is closed out on main. AS-102 remains a separately authorized future task.
- **Presentation takeaway:** “The review hardened the meaning of the inputs, not just the happy path.”
- **Recommended visual:** Proposed valid/invalid threshold matrix and test-summary screenshot; capture pending.
- **Candidate slide title:** “A review gate that protects scientific inputs.”

### M09 — CDSE reflectance offset discovery

- **Date:** Report created 6 October 2026; original experiment timestamp not supplied. Acquisition is 28 April 2023, not the probe date.
- **Task / milestone ID:** AS-102 preparation — reflectance semantics investigation; EV-009.
- **Status:** Recorded provider/STAC-advertised metadata and decoding inference; no pixel verification.
- **Problem / question:** What provider/product metadata determines correct surface-reflectance decoding?
- **Why it mattered:** Stored values require product-specific scale/offset before scientific features can be interpreted.
- **Options considered:** DN/10000 alone versus applying the advertised additive offset; no comparative decoded-pixel experiment recorded.
- **Decision:** No scientific policy is changed; the report records the selected CDSE product's advertised semantics.
- **Rationale:** Preserve actual metadata instead of assuming a universal conversion.
- **Implementation / experiment:** Earlier item/raster metadata inspection, now transcribed from the owner's supplied record; no new probe or decoding implementation.
- **Evidence:** [CDSE reflectance record](evidence/AS_102_CDSE_ACCESS_PROBE.md#reflectance-scaleoffset-discovery); [EV-009](evidence/PRESENTATION_EVIDENCE_INDEX.md).
- **Quantitative result:** Advertised scale `0.0001`, offset `-0.1`, baseline `05.10`; inferred valid-value formula `DN * 0.0001 - 0.1`.
- **Limitation:** No read DN/decoded sample; raw per-band metadata excerpt still needed. L2A BOA reflectance is not automatically aquatic remote-sensing reflectance or HAB evidence.
- **Lesson learned:** Ignoring an advertised offset changes reflectance semantics; do not transfer it to another product without evidence.
- **Impact on next step:** Future handling must mask DN=0 before decoding and avoid automatic clamping of valid negatives; validate the actual product metadata/pixels before implementation.
- **Presentation takeaway:** “Reflectance decoding follows the product's metadata, including its offset.”
- **Recommended visual:** Sanitized scale/offset excerpt and metadata-based formula, labelled as advertised; capture pending.
- **Candidate slide title:** “What do the stored pixel values actually mean?”

### M10 — CDSE raster-access investigation and environmental blocker

- **Date:** Report created 6 October 2026; original probe timestamp not supplied.
- **Task / milestone ID:** AS-102 preparation — CDSE asset access; EV-010.
- **Status:** Recorded metadata investigation and proxy blocker; bounded raster access unverified.
- **Problem / question:** Can the catalog's referenced raster assets be read in the intended runtime?
- **Why it mattered:** Metadata availability does not imply authenticated or windowed pixel access.
- **Options considered:** CDSE's advertised S3/OIDC access route versus a possible alternative raster backend; no successful transport comparison recorded at this point.
- **Decision:** Decision 038 remains CDSE catalog discovery; no raster-provider decision adopted here.
- **Rationale:** Keep access feasibility distinct from AS-101's completed catalog scope.
- **Implementation / experiment:** Selected item metadata inspected; attempted raster/header/window access blocked by the environment proxy; no full raster/product download.
- **Evidence:** [CDSE access probe](evidence/AS_102_CDSE_ACCESS_PROBE.md); [EV-010 index](evidence/PRESENTATION_EVIDENCE_INDEX.md).
- **Quantitative result:** Selected item `S2B_MSIL2A_20230428T064629_N0510_R020_T40RBN_20240831T052931`; 47 assets; nine proposed bands plus SCL and `CLD_20m` available; JP2, EPSG:32640, 10/20 m advertised.
- **Limitation:** Headers, dimensions/dtype, actual authenticated transport, and window/range support unverified; proxy blocking is not a demonstrated provider-side denial.
- **Lesson learned:** Access must be demonstrated at the asset layer separately from the catalog layer.
- **Impact on next step:** Preserve a successful bounded access record before claiming readable pixels; retain original command/timestamp/metadata capture gaps.
- **Presentation takeaway:** “Discovery is one gate; reading pixels is another.”
- **Recommended visual:** Catalog-versus-asset access matrix with an explicit environment proxy boundary; capture pending.
- **Candidate slide title:** “A searchable catalog does not guarantee accessible pixels.”

### M11 — Planetary Computer catalog and advertised COG investigation

- **Date:** Report created 6 October 2026; original experiment timestamp not supplied. Historical checkpoint before asset-host allowlisting and raster reads.
- **Task / milestone ID:** AS-102 preparation — alternative raster backend; EV-011 and EV-013.
- **Status:** Recorded anonymous catalog success; advertised asset metadata; raster access/signing still unverified at this stage.
- **Problem / question:** Does Planetary Computer provide a practical raster-access alternative?
- **Why it mattered:** Public catalog accessibility and advertised COG delivery could reduce access friction, if pixel access is later verified.
- **Options considered:** Existing CDSE discovery/access route versus PC's catalog/COG path; no backend pivot approved.
- **Decision:** Existing CDSE AS-101 decision is unchanged; PC remains a viable investigation rather than an adopted dependency.
- **Rationale:** Handoff §20 and plan §6 distinguish provider evaluation from commitment.
- **Implementation / experiment:** Anonymous STAC/item inspection; identified matching observation and raster host; stopped before raster access because another allowlist update was required.
- **Evidence:** [PC probe](evidence/AS_102_PLANETARY_COMPUTER_PROBE.md); [EV-011/013 index](evidence/PRESENTATION_EVIDENCE_INDEX.md).
- **Quantitative result:** STAC READY / HTTP 200; item `S2B_MSIL2A_20230428T064629_R020_T40RBN_20230428T122311`; nine bands plus SCL; B02 10 m and B05/SCL 20 m COG advertised; host `sentinel2l2a01.blob.core.windows.net`.
- **Limitation:** No separate cloud-probability asset observed in this item; no explicit per-band raster scale/offset advertised. Signing, product-metadata decoding, native headers, and bounded reads unverified at this checkpoint.
- **Lesson learned:** Reachable STAC and a COG description still leave separate asset-access and decoding gates.
- **Impact on next step:** Verify the asset-host/signing path and read product metadata before a tiny-window probe; do not persist signed URLs/tokens.
- **Presentation takeaway:** “An alternative catalog was reachable; its pixel-access path still needed validation.”
- **Recommended visual:** Sanitized catalog-response and host-to-COG diagram labelled as a pre-read checkpoint; capture pending.
- **Candidate slide title:** “Test the path from public catalog to usable raster.”

### M12 — Same acquisition / different processing product

- **Date:** Comparison recorded 6 October 2026; original probe timestamp not supplied.
- **Task / milestone ID:** AS-102 preparation — cross-provider identity; EV-012.
- **Status:** Metadata-supported inference; pixel equivalence unverified.
- **Problem / question:** If two providers represent one observation, do they serve the same processing product?
- **Why it mattered:** A raster backend change must not silently substitute differently processed inputs under the original source identity.
- **Options considered:** Item ID equality versus acquisition/platform/tile/orbit identity; processed-product interchangeability is unsupported.
- **Decision:** Preserve existing provider-qualified source identity; no equivalence/substitution policy adopted here.
- **Rationale:** Decisions 019–020 require the actual raster input's provenance.
- **Implementation / experiment:** Compared the reported CDSE and PC identity/processing fields, without a raster equality test.
- **Evidence:** [Cross-provider table](evidence/AS_102_PLANETARY_COMPUTER_PROBE.md#cross-provider-identity-finding); [CDSE identity](evidence/AS_102_CDSE_ACCESS_PROBE.md#providerstac-advertised-identity); EV-012.
- **Quantitative result:** Both acquire `2023-04-28T06:46:29.024Z`, Sentinel-2B, tile 40RBN, orbit 20. CDSE baseline 05.10/reprocessed Aug 2024; PC baseline 05.09/generated `2023-04-28T12:23:11.362052Z`; different product IDs.
- **Limitation:** Same underlying acquisition does not establish identical processed pixels. No cross-provider pixel comparison or equivalence metric.
- **Lesson learned:** Preserve product provenance as well as observation context.
- **Impact on next step:** If PC later supplies pixels, use a provider-qualified source record for that actual PC product and retain discovery/matching context separately.
- **Presentation takeaway:** “One acquisition, different processing baselines and product identities.”
- **Recommended visual:** Side-by-side identity table from the evidence report, with pixel equivalence explicitly unverified; capture pending.
- **Candidate slide title:** “One observation can have more than one processed product.”

### M13 — AS-102 access-gate status at the documented checkpoint

- **Date:** Repository implementation state documented 3 October 2026; historical probe checkpoint recorded 6 October 2026; exact experiment date not supplied.
- **Task / milestone ID:** AS-102 — Optical Preprocessing readiness boundary; EV-014.
- **Status:** PC catalog READY; raster implementation NOT READY at this evidence point; bounded read PENDING. This is not a later final-gate result.
- **Problem / question:** Is there enough reproducible asset and decoding evidence to begin optical preprocessing?
- **Why it mattered:** Cloud/land/water masks and alignment require readable pixels with defined semantics.
- **Options considered:** CDSE advertised S3/OIDC/JP2 and PC advertised COG path; no final backend, grid, or masking decision recorded.
- **Decision:** AS-102 remains not authorized and not started according to Project State/Handoff; no active development branch.
- **Rationale:** Catalog/metadata feasibility neither proves raster readiness nor authorizes implementation.
- **Implementation / experiment:** Historical metadata/access investigations now documented; no bounded PC read at that stage and no preprocessing package implemented by this task.
- **Evidence:** [PC readiness](evidence/AS_102_PLANETARY_COMPUTER_PROBE.md#readiness-and-next-evidence); [EV-014](evidence/PRESENTATION_EVIDENCE_INDEX.md); Project State §§1, 14–15 and 21–22; Handoff §§3 and 15.
- **Quantitative result:** HTTP 200 catalog result and advertised B02/B05/SCL path; no measured window/DN result, valid-water fraction, or aligned product in this checkpoint.
- **Limitation:** Asset allowlisting/signing, PC scale/offset decoding, bounded reads, and any later final-gate report remain evidence gaps here; do not claim latest external readiness from this historical stage.
- **Lesson learned:** Keep feasibility, authorization, implementation, and scientific validation as separate states.
- **Impact on next step:** Record any later gate as a separately dated experiment, then seek explicit AS-102 implementation authorization; do not start AS-103.
- **Presentation takeaway:** “Catalog access worked; a bounded pixel read remained the next evidence gate.”
- **Recommended visual:** Checkpoint readiness matrix with raster reads/decoding marked pending; capture pending.
- **Candidate slide title:** “What was proved before the first bounded raster read?”

### M14 — Final PC raster-access gate: real bounded pixels and XML-driven decoding

- **Date:** Later experiment stage FG-01 recorded 6 October 2026 (Asia/Dubai); exact original experiment timestamp not supplied. It follows the metadata-only PC checkpoint; product acquisition/generation dates are separate.
- **Task / milestone ID:** AS-102 raster-access prerequisite; EV-014 later stage and EV-015.
- **Status:** Recorded access experiment PASS / READY for the tested product/path; AS-102 NOT YET IMPLEMENTED; AS-103 NOT STARTED.
- **Problem / question:** Can AquaSentinel retrieve real Sentinel-2 pixels without full-scene download or user credentials?
- **Why it mattered:** Readable pixels and defensible decoding are prerequisites for future optical masks/alignment and feature extraction.
- **Options considered:** Bounded COG access was tested; no full-product/SAFE fallback was used. No comparative backend benchmark is recorded.
- **Decision:** Record the successful access prerequisite separately from implementation/provider authorization; Decision 038 and the scientific decisions remain unchanged.
- **Rationale:** Actual reads and retrieved product metadata resolve access/decoding uncertainties left open by advertised assets, while preserving product-specific provenance.
- **Implementation / experiment:** GDAL 3.10.3 `/vsicurl/` header inspection and tiny same-footprint reads after temporary credential-free SAS signing; signed product XML retrieved. Results transcribed from the owner's completed experiment; no new network probe in this documentation task.
- **Evidence:** [Final raster-gate record](evidence/AS_102_PLANETARY_COMPUTER_RASTER_GATE.md); [EV-014 progression / EV-015](evidence/PRESENTATION_EVIDENCE_INDEX.md). Item `S2B_MSIL2A_20230428T064629_R020_T40RBN_20230428T122311`, baseline 05.09.
- **Quantitative result:** **8/8 access gates passed; 4 credential-free HTTP 200 signing operations; 3 bounded reads:** B02 64×64, B05 32×32, SCL 32×32 over a shared approximately 640×640 m footprint. Raw SCL water class **353/1024**. Product XML **53,347 bytes**, quantification **10000**, additive offset **-1000**; XML band IDs B02=1, B05=4. Metadata-derived decoding `(DN - 1000) / 10000`.
- **Limitation:** Only three raster assets were read; no all-band preprocessing, aquatic atmospheric validation, final valid-water count, or pixel equivalence with CDSE. No exact transferred raster-byte measurement. Original timestamp, command/8-gate checklist, and screenshots still need capture.
- **Lesson learned:** A tested COG path plus actual product XML can establish access/decoding mechanics without a full-scene download; scientific water usability remains a distinct gate.
- **Impact on next step:** Raster-access prerequisite READY, not implementation authorization. Future PC-based products must retain the actual PC source identity, grids/nodata/XML decoding metadata, and exclude SAS from provenance/cache/logs. Masks/alignment and AS-103 are not started here.
- **Presentation takeaway:** “From catalog metadata to real satellite pixels — reproducibly, remotely, and without downloading the full scene.” Apply this to the tested product/path; original reproduction transcript still needs capture.
- **Recommended visual:** Future pipeline: PC STAC → temporary SAS signing → COG range/window access → product XML → reflectance decoding → future AS-102 masks/alignment; sanitized signing/header/window/XML/SCL captures still needed.
- **Candidate slide title:** “From catalog references to real, bounded satellite pixels.”

### M15 — AS-102: real full-AOI optical preprocessing and offline cache replay

- **Date:** Fresh finalized experiment `2026-10-06T10:07:14.660936+00:00` UTC / `2026-10-06T14:07:14.660936+04:00` Asia/Dubai; completed `2026-10-06T10:07:43.753204+00:00` UTC. Implementation/evidence record: 6 October 2026.
- **Task / milestone ID:** AS-102 — Optical Preprocessing; EV-016 (real arrays/masks), EV-017 (quality/cache/provenance).
- **Status:** Explicitly authorized implementation COMPLETE for feature-branch acceptance; uncommitted, unpushed, not merged. AS-103 unauthorized and not started. This is a new live experiment, not the owner-supplied historical probe reconstruction.
- **Problem / question:** Could AS-101 discovery become fully aligned, metadata-decoded, conservatively masked AOI pixels with reproducible actual-product lineage?
- **Why it mattered:** Catalog candidates and three tiny access windows did not provide all-band inputs for future features. Modern offsets, coast-adjacent interpolation and distinct provider products could otherwise corrupt meaning or attribution.
- **Options considered:** Existing CDSE delivery versus tested PC COG delivery; broad geospatial frameworks versus NumPy/Rasterio; assumed DN/10000 versus actual product XML; per-tile versus fixed AOI grids; raw SCL water versus conservative all-band support. Choices were explicitly frozen by the owner, not independently expanded by this implementation.
- **Decision:** Newly authorized Decisions 039–045: retain CDSE discovery; actual PC pixels/source; XML semantics; fixed 20 m grid; conservative SCL/support; only NumPy/Rasterio; transient signing and stable cache evidence.
- **Rationale:** FG-01 established credential-free PC access. Same acquisition does not establish same processing product. A reproducible, bounded pipeline is necessary before any scientific feature work.
- **Implementation / experiment:** New strict matching/assets/signing/XML/alignment/mask/model/cache modules and offline synthetic/local tests; fresh current CDSE query followed by eleven PC asset resolutions, native AOI-window reads, XML decoding and all-band reprojection. Base `0867708ea62676dcbcd0f5f83577cc120d633f26`, branch `feature/as-102-optical-preprocessing`; Python 3.11.16, NumPy 2.2.6, Rasterio 1.4.3 / GDAL 3.9.3. Normal pytest performs no external-data calls. A first fresh run produced the same grid/counts/cache identity; the finalized run repeated bounded access rather than relying on that initial cache.
- **Evidence:** [AS-102 plan/API](AS_102_OPTICAL_PREPROCESSING.md); [EV-016/EV-017 validation](evidence/AS_102_OPTICAL_PREPROCESSING_VALIDATION.md); implementation/tests; Decisions 039–045. CDSE `S2B_MSIL2A_20230428T064629_N0510_R020_T40RBN_20240831T052931` versus actual PC `S2B_MSIL2A_20230428T064629_R020_T40RBN_20230428T122311`: same timestamp/platform/40RBN/orbit 20, baselines 05.10 versus 05.09.
- **Quantitative result:** 44 CDSE candidates; 9 float32 band arrays plus uint8 SCL and five masks, all (228,310); fixed EPSG:32640 / 20 m. AOI 67,449, valid data 65,166, candidate water 10,211, valid water 7,963; AOI fraction 11.805957%, retention 77.984526%, excluded water 2,248 (22.015474%). XML quantification 10000 / offsets -1000 parsed for all nine bands. 213 offline tests pass (97 existing +116 added), Ruff/diff check pass. SHA-256 cache reload is array/source/statistics/provenance-equivalent with catalog/signing/XML/raster access blocked.
- **Limitation:** Mask-accepted SCL water is not independent water truth or aquatic radiometry. Some retained visible/SWIR pixels are bright and negative decoded values are preserved. SCL coastal/shallow/turbid/mixed-pixel/cloud-shadow errors remain. No HAB, toxin, chlorophyll, water-safety/intake-risk/lead-time result; no pixel-equivalence claim; no exact network-byte measurement. Two transitive Affine deprecation warnings are reported, with no failures. Additional real cross-CRS smoke was not run; synthetic EPSG:32639 → 32640 alignment passed.
- **Lesson learned:** Successful pixel access is only a prerequisite. Product semantics, source identity, spatial alignment and contributor quality must all survive the transition to scientific inputs. Cache tests caught and corrected tuple/list serialization inequality; security tests check that transient URLs do not leak through transport/GDAL diagnostics.
- **Impact on next step:** Review the uncommitted AS-102 work; commit/push/PR requires separate instruction. AS-103 remains unauthorized. Capture a real mask/grid evidence visual and retain independent science-validation gaps.
- **Presentation takeaway:** “All nine bands aligned to one reproducible grid; conservative support retained 7,963 traceable water-class pixels.”
- **Recommended visual:** V15: AOI/candidate-water/retained-water/support-exclusion map; V16: XML→grid→PC lineage→verified offline cache result card. Captures pending; include exact acquisition/processing/experiment dates and attribution, with no SAS.
- **Candidate slide title:** “From catalog candidates to conservatively masked, traceable water pixels.”

### M16 — AS-102 code review, security hardening, merge and closeout

- **Date:** 8 October 2026 (Asia/Dubai). PR merged `2026-10-08T07:06:46Z` / `2026-10-08T11:06:46+04:00` Asia/Dubai; the merge timestamp is distinct from the earlier live experiment.
- **Task / milestone ID:** AS-102 final code review, publication, merge and documentation closeout; EV-018.
- **Status:** AS-102 COMPLETE AND MERGED. AS-103 remains NOT authorized and NOT started.
- **Problem / question:** Could the accepted preprocessing implementation pass security/provenance review and be published without losing historical evidence or overstating scientific progress?
- **Why it mattered:** Temporary access credentials and duplicated cache provenance require explicit containment/consistency checks; implementation acceptance, final review and main-branch merge are different stages.
- **Options considered:** Canonical HTTPS identity versus raw netloc equality; scoped logger suppression versus URL string redaction; explicit cache/provenance consistency checks versus trusting duplicated metadata. These were targeted review fixes, not a new provider or scientific decision.
- **Decision:** Complete the authorized review and merge of the existing Decisions 039–045 contract; no new technical decision and no AS-103 authorization.
- **Rationale:** Retain strict observation identity, bounded access, transient credentials, reproducible arrays and actual-product provenance before downstream science.
- **Implementation / experiment:** Review hardening covered canonical HTTPS/443 and redirect protections; SAS/transient URL containment; strict cross-provider observation matching; malformed STAC asset rejection; conservative interpolation-support validation; bounded raster reads; cache/provenance tamper consistency checks; and transient metadata signing cleanup. No new live-scene experiment is claimed by this closeout.
- **Evidence:** Feature commit `fe3d27046c40600010753957ee8921d57071ec48`; [PR #6](https://github.com/Omar-Aboulwafa/aquasentinel-813/pull/6); merge commit `627b6ae8a509509dbb2d5d43bbdc6d74e0ce2aac`; transport/assets/alignment/cache tests; [EV-018](evidence/PRESENTATION_EVIDENCE_INDEX.md). GitHub reported clean/mergeable before merge with no configured/reported CI/workflow checks.
- **Quantitative result:** Final reviewed suite **265 passed**, Ruff passed, `git diff --check` passed. Six Rasterio deprecation warnings remained non-blocking. Historical M15 remains 213 tests; no replacement experiment or change to the real-scene counts is claimed.
- **Limitation:** Preprocessing is implemented; HAB/anomaly/chlorophyll/toxin/water-safety/intake-risk/lead-time results are NOT established. BOA is not aquatic Rrs; coastal SCL/contributor limits and distinct PC/CDSE processing products remain. Local checks are not a GitHub CI pass.
- **Lesson learned:** A passing processing experiment needs separate security/provenance review and a verified publication trail; preserve earlier stages instead of rewriting them.
- **Impact on next step:** AS-102 is closed. Prepare/define AS-103 only after separate explicit authorization; scientific validation and sanitized presentation captures remain outstanding.
- **Presentation takeaway:** “Preprocessing merged with traceable review evidence; scientific conclusions remain a separate task.”
- **Recommended visual:** V17: sanitized PR #6 merge/commit and 265-test/Ruff/diff-check card, explicitly marked local checks; capture pending.
- **Candidate slide title:** “From tested pixels to reviewed, merged preprocessing.”

### M17 — AS-103: candidate spectral features, numerical diagnostics and parent lineage

- **Date:** 8 October 2026; cached experiment `2026-10-08T09:52:47.133486+00:00` UTC / `2026-10-08T13:52:47.133486+04:00` Asia/Dubai, completed `2026-10-08T09:52:47.209734+00:00` UTC.
- **Task / milestone ID:** AS-103 — Spectral Feature Extraction; EV-019/EV-020.
- **Status:** Explicitly authorized; implementation acceptance complete on uncommitted/unpushed/unmerged feature branch. AS-104 NOT authorized and NOT started.
- **Problem / question:** Can verified water reflectance become explainable candidate spectral signals without losing numeric support or parent-product lineage?
- **Why it mattered:** Signed BOA/denominator cancellation can create misleading extremes; mutable arrays can undermine parent-only identity; feature correlations can be overcounted scientifically.
- **Options considered:** Pure NumPy recomputation versus another disk cache; signed output/diagnostics versus clipping; immediate parent plus content fingerprint versus raw-source shortcut/parent-only hash; declared nominal wavelengths/k=1.0 versus claiming official SNAP MCI.
- **Decision:** Explicitly authorized Decision 046: six fixed candidate features, numerical-only guards, preserved parent support, finite metadata, consumed-content identity, immediate derived parent and no new cache/dependencies/config.
- **Rationale:** AS-104 may later use these per-scene signals; numerical support and scientific limits must remain visible before any temporal interpretation.
- **Implementation / experiment:** New features model/spectral modules and 83 offline cases; one existing-cache acceptance with no retrieval/raster writes; four independent scalar pixel checks and blocked-I/O repeated extraction.
- **Evidence:** [AS-103 plan](AS_103_SPECTRAL_FEATURES.md), [EV-019/EV-020 acceptance](evidence/AS_103_SPECTRAL_FEATURES_VALIDATION.md); branch `feature/as-103-spectral-features`, base main `642a469414f096b4ac7cd96de895aa38f7da42ec`.
- **Quantitative result:** 7,963 valid pixels per feature, all (228,310), float32; zero denominator/nonfinite exclusions in this scene; two NDCI-like outputs below −1 retained; 491 negative-input pixels for B06-inclusive features. Full suite 348 passed, Ruff/diff check passed; six existing Rasterio warnings. Input unchanged; repeat/identity/registry lineage exact.
- **Limitation:** Single cached scene, not temporal anomaly or HAB/chlorophyll/toxin/safety/risk/lead-time evidence. BOA is not Rrs; coastal/sediment/glint/correction/SCL limitations remain. Reference-page retrieval HTTP 403; no live literature-fetch success claimed.
- **Lesson learned:** Retaining negative and out-of-range values with explicit support/diagnostics preserves the evidence better than clipping; source lineage needs the actual processing parent.
- **Impact on next step:** Review uncommitted AS-103; separate authorization required for publication or AS-104. No temporal work started.
- **Presentation takeaway:** “Six traceable candidate signals, with numerical exclusions and scientific limits explicit.”
- **Recommended visual:** V18 candidate feature/support/diagnostic maps, V19 formula/fingerprint/PC→AS-102→AS-103 card; captures pending, no hazard interpretation.
- **Candidate slide title:** “Candidate spectral signals before temporal interpretation.”

### M18 — AS-103 code review, merge and closeout

- **Date:** 8 October 2026; merge `2026-10-08T10:43:24Z` UTC / `2026-10-08T14:43:24+04:00` Asia/Dubai.
- **Task / milestone ID:** AS-103 final code review, publication/merge and post-merge documentation closeout; EV-021.
- **Status:** AS-103 COMPLETE AND MERGED through PR #8. AS-103 development is closed; AS-104 NOT authorized and NOT started.
- **Problem / question:** Did the accepted candidate-feature implementation satisfy typed-model, numerical, identity and lineage contracts before publication?
- **Why it mattered:** A successful feature experiment and later code-review/merge checkpoint are distinct evidence stages; neither establishes a biological event or operational performance.
- **Options considered:** Preserve M17 / EV-019–EV-020 and add a later merge record versus retroactively rewriting acceptance; durable closed-development status versus a temporary current-branch label. This closeout changes no technical decision or algorithm.
- **Decision:** Record the approved final review and publication of Decision 046's existing AS-103 contract in M18 / EV-021; preserve historical acceptance and keep AS-104 separately unauthorized.
- **Rationale:** Future agents and presentation readers need accurate completion/lineage evidence without interpreting feature values as scientific validation or permission for temporal analysis.
- **Implementation / experiment:** Final implementation review PASS; `models.py` review PASS; `spectral.py` review PASS; numerical-policy tests PASS; identity/fingerprint tests PASS; immediate-parent lineage tests PASS; real-scene acceptance evidence review PASS. M17's cached experiment remains at `2026-10-08T09:52:47.133486+00:00` UTC / `2026-10-08T13:52:47.133486+04:00` Asia/Dubai, distinct from this later merge. No real scene was rerun during merge review or this closeout.
- **Evidence:** Implementation `5638bc8b4ab06f235f908642f714a7cc83b35709`; [PR #8](https://github.com/Omar-Aboulwafa/aquasentinel-813/pull/8); merge `b770d0561da9ac2b81ca2d4b8e784adff66ee231`; committed feature source/tests; [historical acceptance](evidence/AS_103_SPECTRAL_FEATURES_VALIDATION.md); [EV-021](evidence/PRESENTATION_EVIDENCE_INDEX.md#ev-021-final-as-103-review-and-merge).
- **Quantitative result:** Final reviewed suite **348 passed**, Ruff passed and `git diff --check` passed; six existing non-blocking Rasterio PendingDeprecationWarnings only, no new AS-103 warnings. Fourteen implementation files. No GitHub Actions/workflow CI run was configured/reported; no GitHub CI success is claimed. Historical M17 remains 348 tests and six candidate features, 7,963 pixels per feature / 100% parent-water support, two below-−1 NDCI-like values retained/diagnosed, signed BOA and exact PC→AS-102→AS-103 lineage.
- **Limitation:** Engineering review/merge only. BOA ≠ aquatic Rrs; ndci_like is not calibrated chlorophyll, mci_like is an analogue, and correlated NDCI-like/B05-red are not independent biological evidence. No event threshold, HAB/event classification, temporal baseline/anomaly, species/toxin identification, water-safety certification, autonomous plant action, intake exposure, risk/persistence/lead-time accuracy or scientific accuracy claim.
- **Lesson learned:** Preserve acceptance and publication as separate dated stages; a verified identity/lineage chain makes candidate features reproducible without validating their aquatic interpretation.
- **Impact on next step:** AS-103 is closed. AS-104 — Temporal Baseline is NEXT PLANNED only, NOT authorized and NOT started; require separate explicit authorization. Scientific validation and sanitized presentation captures remain outstanding.
- **Presentation takeaway:** “Candidate spectral features reviewed and merged, with parent lineage and scientific limits intact.”
- **Recommended visual:** V20 sanitized PR #8/commit/local-348-test review card, alongside V18/V19 candidate-feature/formula/lineage captures; all captures pending, no signed URLs or scientific-result claim.
- **Candidate slide title:** “From candidate signals to reviewed, merged feature engineering.”

### M19 — AS-104: causal temporal comparisons and a blocked real history gate

- **Date:** 8 October 2026 (Asia/Dubai); real attempt 12:28:07.712335–12:28:29.564367 UTC / 16:28:07.712335–16:28:29.564367 Asia/Dubai.
- **Task / milestone ID:** AS-104 — Temporal Baseline; E18/E19, EV-022/EV-023.
- **Status:** Explicitly authorized, pure implementation and offline gate PASS; real multi-scene acceptance BLOCKED. Uncommitted, unpushed, unmerged; no PR. AS-105+ unstarted.
- **Problem / question:** Can separate dated candidate features be compared causally on their exact target-supported pixels without future leakage or invalid standardized scores?
- **Why it mattered:** A temporal estimator must not manufacture history, numerical scale or biological conclusions from single-scene features.
- **Options considered:** Mean/std versus median/MAD; references+target versus target-ID collection; symmetric versus strictly-prior history; whole-reference versus consumed-support fingerprints; forced epsilon versus masked zero scale. Owner froze semantic reference fingerprints and excluded precision-noise-floor diagnostics.
- **Decision:** Decision 047: median/MAD/1.4826, signed deviation, standardized anomaly on positive scale and exact-tie midrank; explicit minimum (5 for P0), causal bounds, six separate feature families, immediate AS-103 parents.
- **Rationale:** Transparent NumPy math, strict support and provenance protect small-sample interpretation and deterministic recomputation.
- **Implementation / experiment:** Plan created first; temporal modules and initial 111 offline cases passed the 459-test gate before reusing April 28 target and querying fixed March history. Final inspection added one collection-iteration regression (112 temporal cases / 460 total). Unchanged AS-102 rejected two PC processing products for the first March 4 observation; experiment stopped before reference raster reads.
- **Evidence:** [AS-104 contract](AS_104_TEMPORAL_BASELINE.md), Decision 047, [EV-022/EV-023 evidence](evidence/AS_104_TEMPORAL_BASELINE_VALIDATION.md). Branch `feature/as-104-temporal-baseline`, base `c6accab2c5753734466a6375d1b3ce1762e99bed`.
- **Quantitative result:** 460 tests (348 retained +112 new), Ruff/diff PASS; six existing Rasterio warnings. CDSE 44 candidates, five March tile-40RBN/orbit-20 candidates; first has two exact PC matches (05.09/05.10). Zero processed historical scenes. Target 7,963 valid pixels/feature. No real temporal support/statistics/product ID.
- **Limitation:** Offline engineering success is not real multi-scene acceptance. Reprocessing-product ambiguity blocks unchanged upstream matching. No HAB/event, significance, confidence/probability, safety, risk, persistence or lead-time claim. March is not declared normal water.
- **Lesson learned:** Catalog availability and metadata-compatible dates do not guarantee an unambiguous raster product; strict matching exposes provider reprocessing rather than silently picking pixels.
- **Impact on next step:** Owner code/science review and separate authorization for any upstream delivered-product selection investigation. Preserve the fixed experiment and stop; no window/minimum/mask workaround and no AS-105+.
- **Presentation takeaway:** “Causal comparison passed offline; the real-data gate stopped honestly at provider-product ambiguity.”
- **Recommended visual:** V21 causal-window/support/MAD/rank/lineage diagram and a two-product March 4 ambiguity card; captures pending. No real anomaly map exists from this attempt.
- **Candidate slide title:** “Temporal evidence needs both a causal baseline and an unambiguous source.”

### M20 — Explicit PC processing baseline without a hidden heuristic

- **Date:** 8 October 2026 (Asia/Dubai); resolver smoke 13:38:26.730440–13:38:48.970146 UTC / 17:38:26.730440–17:38:48.970146 +04:00.
- **Task / milestone ID:** AS-102 required-PC-baseline upstream fix; Decision 048 / E20 / EV-024. M19 is reserved for preserved AS-104 work, not imported here.
- **Status:** Implemented and offline/metadata validated, uncommitted for review; not pushed/merged, no PR. AS-104 real acceptance BLOCKED.
- **Problem / question:** March observations each have 05.09 and 05.10 PC processing products; unchanged AS-102 correctly refused ambiguity before reference asset access.
- **Why it mattered:** Acquisition identity does not identify a processing product; temporal comparison must not silently mix delivered processing baselines.
- **Options considered:** Explicit required baseline; matching CDSE generation/baseline; arbitrary latest/earliest generation; mixed delivered baselines.
- **Decision:** Owner-authorized optional baseline constraint after validating structured exact-observation matches, still requiring exactly one product. No fallback; no new pixel/cache identity dimension.
- **Rationale:** The five predeclared March dates each have one complete 05.09 product, matching the accepted April PC target's baseline. CDSE 05.10 remains separate discovery context, as permitted by Decision 039.
- **Implementation / experiment:** Three keyword-only API additions, shared early selector validation, validated-match filtering, and checks on both cache-return paths. Separate worktree from exact main base c6accab; main's 348 tests retained. Then six metadata-only resolver calls with signing/XML/raster/preprocessing/cache entry points blocked; separate read-only accepted-April-cache verification.
- **Evidence:** [Fix plan/API](AS_102_REQUIRED_PC_BASELINE_FIX.md), [timestamped validation](evidence/AS_102_REQUIRED_PC_BASELINE_FIX_VALIDATION.md), Decision 048, source/tests on `fix/as-102-required-pc-baseline`.
- **Quantitative result:** **421 passed** (348 retained +73 new), Ruff/diff pass, same six Rasterio warnings. Fresh CDSE search 44 candidates; **5/5 March +1/1 target** uniquely resolved at 05.09; eleven required assets each; **0** forbidden smoke calls. Existing target cache accepts 05.09, rejects 05.10 and keeps exact identity/provenance/file hashes.
- **Limitation:** Metadata resolution only; March XML/raster readability, decoding/native-grid compatibility and per-pixel valid-water history are untested. No AS-104 temporal product or scientific/operational result; no GitHub CI claim.
- **Lesson learned:** Make ambiguity constraints explicit and test failure on zero/multiple; selecting the same actual product must not duplicate cache identity.
- **Impact on next step:** Review/merge the isolated fix before separately rerunning the unchanged AS-104 target/March-period/minimum-five experiment. Preserve its uncommitted work; do not resume it in this task or start AS-105+.
- **Presentation takeaway:** “One observation can have several processing products; choose explicitly and preserve lineage.”
- **Recommended visual:** Sanitized two-product table → explicit 05.09 constraint → exactly-one result; 421-test / 6-of-6 metadata card and unchanged-cache identity. Capture pending, never include signing material.
- **Candidate slide title:** “Resolve processing ambiguity without changing the science.”

### M21 — Decision 048 merged; AS-104 restored, signing blocks the frozen rerun

- **Date:** 9 October 2026 (Asia/Dubai); three attempts timestamped in EV-025, first started 2026-10-09T05:26:31.801976+00:00 UTC / 2026-10-09T09:26:31.801976+04:00 Dubai; last ended 2026-10-09T05:31:05.514348+00:00 UTC / 2026-10-09T09:31:05.514348+04:00 Dubai.
- **Task / milestone ID:** AS-104 resumed after PR #10 / Decision 048; E21 / EV-025.
- **Status:** Integration/preservation/offline PASS; real temporal acceptance BLOCKED by signing. AS-104 remains uncommitted; AS-105+ and the 05.10 P1 experiment unstarted.
- **Problem / question:** Can the preserved frozen temporal experiment run after explicit processing-product selection removes the original ambiguity?
- **Why it mattered:** Upstream publication must preserve reviewed temporal work and causal history; metadata resolution alone does not establish readable pixels or sufficient temporal support.
- **Options considered:** Verified backups + retained stash + ff-only versus replacing/rebuilding work; strict 05.09 versus silent generation/baseline selection; bounded same-asset signing retry versus relaxing data/mask/history rules.
- **Decision:** Apply retained stash onto exact merged main 39f2aee90c727fc151886efbdea44daec0e3f9b4; reconcile documentation only, keep algorithms/tests byte-identical and rerun the unchanged target/March/minimum-five contract. Stop on exhausted access failure.
- **Rationale:** Strict identity and processing comparability must precede temporal math; intermittent HTTP success is not a completed real acceptance.
- **Implementation / experiment:** External binary diff/untracked archive and SHA-256 inventories verified; safety stash applied without pop; four documentation conflicts resolved, both histories preserved in order. Three real attempts; third retries the same audited signer up to five times outside project source. Native SCL read succeeded, B02 signing exhausted retries.
- **Evidence:** [Timestamped integration and attempts](evidence/AS_104_TEMPORAL_BASELINE_VALIDATION.md#4-decision-048-integration-and-resumed-frozen-acceptance--9-october-2026), PR #10/39f2aee90c727fc151886efbdea44daec0e3f9b4, retained stash f93950aab6fdfb40bb100158915ef12692aa1665, recovery inventories. Original M19/E18–E19/EV-022–EV-023 and M20/E20/EV-024 remain historical.
- **Quantitative result:** Combined 533 tests PASS, Ruff/diff PASS; same six warnings. All ten restored AS-104 files initially hash-identical; eight source/test files still identical. Fresh 44-candidate searches; April target 7,963 pixels per feature. Exactly zero completed March references; no real temporal product. Diagnostic observed HTTP 504 alongside HTTP 200; final B02 call failed five attempts.
- **Limitation:** No real history-count distribution, sufficient/zero-MAD/anomaly/rank counts, temporal fingerprint/ID, scalar checks, future-scene check or repeatability result. Missing reference support is unmeasured, not zero. No hazard, scientific accuracy, operational or GitHub CI success claim.
- **Lesson learned:** Preserve both failure checkpoints: processing ambiguity was a source-selection issue; the later signing outage is an independent transport issue.
- **Impact on next step:** Await stable existing signing access, retry the identical frozen 05.09 experiment and report actual masks/history truth before real temporal acceptance. Retain stash; no commit/push/PR or AS-105+.
- **Presentation takeaway:** “An upstream fix removes one blocker; real-data gates still have to pass honestly.”
- **Recommended visual:** V22 chronological ambiguity → Decision 048 → restored hash/533-test gate → signing-blocked rerun card; capture pending. No anomaly map exists from this rerun; show only sanitized IDs/statuses.
- **Candidate slide title:** “Preserve the work, resolve the source, and report the next access gate.”
### M22 — Reuse authorization without changing scientific identity

- **Date:** 9 October 2026 (Asia/Dubai); live smoke 06:44:49.076690–06:44:51.406274 UTC / 10:44:49–10:44:51 +04:00.
- **Task / milestone ID:** AS-102 reusable PC SAS token transport; Decision 049 / E22 / EV-026.
- **Status:** Implemented and offline/bounded transport smoke PASS; uncommitted for review, no push/PR/merge.
- **Problem / question:** After Decision 048 merged, resumed AS-104 was blocked by intermittent per-asset `/sign` HTTP 504s; a cold scene used eleven authentication calls.
- **Why it mattered:** Repeated authorization increased external-service exposure before real temporal acceptance; transport credentials must remain outside reproducible scientific identity.
- **Options considered:** Keep per-asset `/sign`; reuse official account/container tokens; install full PC SDK; add subscription key; broaden raster retries.
- **Decision:** Explicitly authorized reusable anonymous issuer/account/container tokens, process memory only, existing `sign_asset` API, bounded acquisition retries only.
- **Rationale:** Official SDK/OpenAPI and the preceding corrected anonymous-token diagnostic support scoped reuse. Reduce authentication calls without adding dependencies/secrets or changing pixels/lineage.
- **Implementation / experiment:** Validate unsigned assets/scope/issuer and actual token/expiry schema; refresh at <=60 seconds; at most five attempts for 429/500/502/503/504 or typed transient failures, exponential 0.8/1.6/3.2/6.4-second delays. Offline fixtures then fresh March-4 05.09 eleven-asset signing, tiny XML/TIFF reads and three cache-reuse signs.
- **Evidence:** [Plan](AS_102_REUSABLE_PC_SAS_TOKEN_FIX.md), [EV-026 validation](evidence/AS_102_REUSABLE_PC_SAS_TOKEN_FIX_VALIDATION.md), Decision 049, transport source/tests. Original AS-104 blocker bodies remain only in their preserved worktree.
- **Quantitative result:** **531 passed** (421 main +110 net new); Ruff/diff PASS; six unchanged warnings. **1** anonymous HTTP 200 token attempt, **11/11** signs, XML **1,024 bytes** and B02 TIFF header **4,096 bytes**, both HTTP 206; **0** extra token requests for B03/SCL/XML reuse. **0** live-credential matches in repository scan; original 83 files/status/stash and accepted-cache hashes unchanged.
- **Limitation:** Header/transport evidence only; no full XML decoding/raster pixels/preprocessing or AS-104 acceptance. No induced live retry, availability guarantee, cross-process sharing or concurrent single-flight promise; no GitHub CI success.
- **Lesson learned:** Separate ephemeral authorization from stable assets and scientific identity. Do not infer rate limiting from observed 504s or impose undocumented `sp == r` restrictions.
- **Impact on next step:** Review/merge isolated transport fix before separately resuming AS-104 real acceptance. No AS-104 algorithm work, AS-105+ or P1 05.10 study here.
- **Presentation takeaway:** “Eleven assets, one scoped authorization, unchanged scientific identity.”
- **Recommended visual:** Safe issuer/account/container → private token → eleven unsigned assets diagram; one-request/eleven-signs card and 1,024/4,096-byte bounds. Capture pending; never show SAS material.
- **Candidate slide title:** “Make access reliable without changing the science.”

### M23 — Five real references completed; provenance casing stops temporal acceptance

- **Date:** 9 October 2026 (Asia/Dubai); 07:31:08.630215–07:31:57.353103 UTC / 11:31:08.630215–11:31:57.353103 +04:00.
- **Task / milestone ID:** AS-104 frozen five-reference 05.09 acceptance after merged Decision 049; E23 / EV-027.
- **Status:** Integration/preservation/offline and five-reference AS-102/103 PASS; AS-104 real acceptance BLOCKED at target provenance validation; uncommitted.
- **Problem / question:** Can the preserved frozen temporal experiment complete after reusable SAS transport removes repeated per-asset authorization?
- **Why it mattered:** Real delivered product metadata must satisfy temporal identity/lineage, not merely offline fixture assumptions; five scenes do not prove per-pixel history sufficiency.
- **Options considered:** Back up/stash/ff-only/restore versus rebuilding work; unchanged production transport versus custom retries; stop at the guard versus silently normalizing source metadata or relaxing contract checks.
- **Decision:** Execute the existing owner-authorized experiment, preserve source/tests and all historical records, stop and record the new validation failure. No new architectural/scientific decision is adopted.
- **Rationale:** Stable provenance and accepted cache identity must not be rewritten to bypass a real metadata mismatch.
- **Implementation / experiment:** Verified binary patch, ten-file archive, 83-file hashes and second retained stash; ff-only to PR #11, apply without pop, resolve four documentation conflicts. Eight temporal source/tests stay byte-identical. Run exactly five March references through normal AS-102 explicit 05.09 and unchanged AS-103; call unchanged AS-104 API.
- **Evidence:** [Validation §5](evidence/AS_104_TEMPORAL_BASELINE_VALIDATION.md#5-pr-11-integration-and-five-reference-0509-attempt--9-october-2026), PR #11 / 2006df7, retained backups/stashes and eight temporal hashes. Earlier M19–M22 retain original dated bodies/statuses.
- **Quantitative result:** **643 tests PASS**, Ruff/diff PASS, six existing warnings. **5/5** real reference scenes complete; valid water **8,674 / 2,092 / 7,350 / 3,834 / 6,156**; target **7,963**. Same 20 m EPSG:32640 310×228 grid. March-4 B04-denominator features exclude 52 pixels; March-14 green/blue excludes 20. Live in-memory credential scan: **0** matches; accepted target cache hashes unchanged.
- **Limitation:** AS-104 target guard compares `sentinel-2b` to actual source `Sentinel-2B` case-sensitively. Timestamps agree; corresponding reference mismatches also exist. No temporal reduction/product/fingerprint, history-count distributions, scalar validation, future-scene check or repeat result. These are unmeasured, not zero. No GitHub CI or scientific/operational success claim.
- **Lesson learned:** Use real provider/source representations in compatibility tests; upstream pixel success does not establish downstream temporal acceptance.
- **Impact on next step:** Owner review/authorization of a targeted platform-representation validation fix and realistic regression fixture; preserve existing lineage/cache identity and scientific rules. Do not repair it in this task.
- **Presentation takeaway:** “Real imagery exposed a metadata assumption that synthetic fixtures missed.”
- **Recommended visual:** Sanitized five-reference support table → target identity guard (`sentinel-2b` versus `Sentinel-2B`) → blocked temporal stage. Capture pending; no anomaly map exists.
- **Candidate slide title:** “Five scenes are ready; provenance still has to agree.”

### M24 — Case-only platform consistency, unchanged scientific identity

- **Date:** 9 October 2026 (Asia/Dubai), after the M23 blocked checkpoint and before the 12:01:50 +04:00 cached rerun.
- **Task / milestone ID:** AS-104 targeted platform representation fix; E24 / EV-028.
- **Status:** PASS — uncommitted bug fix and regression validation, not merged.
- **Problem / question:** Accepted upstream observations use `sentinel-2b` while actual PC source records preserve `Sentinel-2B`; strict raw equality rejected the same spacecraft before temporal reduction.
- **Why it mattered:** Real provider metadata must be accepted without rewriting scientific identity or weakening mismatches.
- **Options considered:** Case-only comparison versus alias/punctuation normalization or rewriting source/observation/cache records. Only case-only equality was authorized.
- **Decision:** Replace one equality predicate with `.casefold()` comparison under Decision 047; no Decision 050.
- **Rationale:** Case-equivalent strings denote the same platform for this check while different spacecraft, aliases, punctuation, spaces and invalid types must fail.
- **Implementation / experiment:** External binary patch/hash inventory before editing; one line in baseline.py and 20 regression cases in test_identity_lineage.py. No models, AS-102/103, transport, serializers, configuration, dependencies or temporal math changed.
- **Evidence:** [Validation §6](evidence/AS_104_TEMPORAL_BASELINE_VALIDATION.md#6-targeted-platform-case-representation-fix--9-october-2026), exact source delta, regression tests, retained pre-fix hashes/patch.
- **Quantitative result:** 132 temporal tests PASS; 663 full tests PASS, Ruff/diff PASS; six historical Rasterio warnings only.
- **Limitation:** The reverse-case example isolates the consistency predicate; the separate existing descriptor schema continues requiring lowercase observation identity. This is validation compatibility, not a new platform alias policy or science accuracy evidence.
- **Lesson learned:** Match case-equivalent provider representations at comparison time; preserve original serialized identity values.
- **Impact on next step:** Rerun exactly the frozen experiment from existing caches, without network or upstream reprocessing.
- **Presentation takeaway:** “Accept the same spacecraft without changing its provenance.”
- **Recommended visual:** One-line before/after predicate beside unchanged source/cache IDs; capture pending.
- **Candidate slide title:** “Fix the comparison, preserve the evidence.”

### M25 — Frozen real temporal acceptance from six verified caches

- **Date:** 9 October 2026; 08:01:50.383608–08:01:51.327507 UTC / 12:01:50.383608–12:01:51.327507 +04:00 Asia/Dubai.
- **Task / milestone ID:** AS-104 real five-reference 05.09 acceptance rerun; E25 / EV-029.
- **Status:** PASS — engineering acceptance; AS-104 remains uncommitted, unpushed, unmerged, no PR.
- **Problem / question:** Can the existing frozen median/MAD/midrank algorithm complete on the same six real inputs after the authorized representation correction?
- **Why it mattered:** Five scenes do not establish full history at every pixel; conservative sparse support must remain explicit.
- **Options considered:** Known-ID cache reload and deterministic unchanged AS-103 reconstruction versus unnecessary imagery retrieval; preserve minimum five versus relaxed support. Cache-only execution with the frozen contract was required.
- **Decision:** Execute Decision 047 unchanged except M24's equality predicate; no new architecture/scientific decision.
- **Rationale:** Isolate the validation fix and reuse independently verified real upstream evidence.
- **Implementation / experiment:** Reload exactly six 05.09 AS-102 caches, reconstruct matching AS-103 IDs, compute target plus R1–R5; check 18 deterministic first/middle/last eligible pixels, repeat, and add/mutate a clearly synthetic later scene.
- **Evidence:** [Validation §7](evidence/AS_104_TEMPORAL_BASELINE_VALIDATION.md#7-cached-five-reference-0509-real-acceptance-rerun--9-october-2026), complete JSON IDs/fingerprints/lineage/counts/summaries/scalar records and cache-file hashes.
- **Quantitative result:** Target support 7,963 per feature; baseline/z/rank support in approved order 792/802/801/801/801/797; insufficient 7,171/7,161/7,162/7,162/7,162/7,166. Zero MAD and numerical rejections: zero. 18/18 scalar checks, causal exclusion, repeat and input immutability PASS. Zero network attempts; all six AS-103 IDs and all 12 cache-file hashes unchanged. Offline 663 tests/Ruff/diff PASS.
- **Limitation:** Only about 10% of target support has five histories, and five observations are not statistical sufficiency. Extreme z values are retained with positive scale, not interpreted as hazard severity. Synthetic future exclusion proves selection, not real future availability. No HAB, concentration, toxins/species, water safety, risk, persistence, alert, lead-time or GitHub CI-success claim.
- **Lesson learned:** Missing temporal support is evidence; retain conservative masks instead of manufacturing a complete map.
- **Impact on next step:** Owner code/evidence review of the entire uncommitted AS-104 worktree. Publication requires separate authorization; AS-105+ and P1 05.10 remain unstarted.
- **Presentation takeaway:** “Five real dates support a measured subset, not the entire scene.”
- **Recommended visual:** History-count distribution and baseline-eligible support card; proposed spatial mask display, capture pending (no screenshot claimed).
- **Candidate slide title:** “A reproducible temporal baseline with honest coverage.”

### M26 — Reviewed AS-104 implementation and evidence published for PR review

- **Date:** 9 October 2026 (Asia/Dubai). Acceptance completed 12:01:51.327507 +04:00; later Git commit at 12:50:47 +04:00, remote publication confirmed by tracking-ref fetch at 12:52:09 +04:00. Exact push-completion second is not recorded; remote HEAD reconfirmed at 13:09:07 +04:00.
- **Task / milestone ID:** AS-104 implementation/evidence publication; E26 / EV-030.
- **Status:** COMMITTED AND PUSHED for PR review. Clean feature-publication worktree; PR NOT YET CREATED, NOT MERGED.
- **Problem / question:** How can reviewed AS-104 implementation and accepted evidence become an exact, externally reviewable Git artifact without losing history or recovery material?
- **Why it mattered:** Acceptance completion and publication are separate events; published identity, code/evidence scope and historical failures must be traceable.
- **Options considered:** Publish exactly the approved fifteen paths versus accidentally including runtime imagery/cache/recovery files; add a later publication checkpoint versus rewriting earlier blockers and uncommitted acceptance statuses.
- **Decision:** Owner-authorized commit and push on the existing feature branch. This is execution/publication under existing decisions, not Decision 050.
- **Rationale:** Make the approved implementation/evidence reviewable while preserving source identities, sparse-support limits and earlier factual checkpoints.
- **Implementation / experiment:** Final gates, exact staged-path/blob verification, one feature commit and upstream-tracked push; remote SHA equality, clean worktree, two stashes and five recovery artifacts verified. No new EO processing or scientific experiment.
- **Evidence:** Feature commit `09b38bd9c312470e948b1f17165ec5335cfc149d`, parent `2006df7a70a4f48c66933aed96f4464d8d03084e`, branch `feature/as-104-temporal-baseline`, upstream `origin/feature/as-104-temporal-baseline`; [publication validation §8](evidence/AS_104_TEMPORAL_BASELINE_VALIDATION.md#8-as-104-feature-publication--9-october-2026).
- **Quantitative result:** Exactly 15 committed paths; message `feat: implement AS-104 temporal baseline`. Pre-commit 663 tests PASS (17.49s), Ruff/diff and untracked whitespace PASS; six existing Rasterio warnings. Scientific engineering acceptance M25/E25/EV-029 PASS, scalar 18/18, synthetic causal/repeat PASS; all twelve cache hashes and six AS-103 IDs unchanged.
- **Limitation:** Publication is not merge or GitHub CI success, nor new detection/operational evidence. Roughly 10% of 7,963 target-valid pixels per feature have all five histories (792/802/801/801/801/797). Five observations are not statistical sufficiency; small positive scales can produce large robust-z magnitudes.
- **Lesson learned:** Record experiment time separately from commit/push verification, and publish only reviewed evidence-bearing paths.
- **Impact on next step:** Review the published AS-104 commit and open a PR if review passes and creation is authorized. No merge, AS-105+ or P1 05.10 study.
- **Presentation takeaway:** “The accepted result is now a reproducible, reviewable Git artifact.”
- **Recommended visual:** Acceptance → 15-path reviewed commit → pushed branch → pending PR/merge diagram; capture pending, no screenshot claimed.
- **Candidate slide title:** “Publish the evidence without rewriting its history.”

### M27 — AS-104 merged through PR #12 and formally closed

- **Date:** 9 October 2026 (Asia/Dubai). PR merged 13:26:08 +04:00 / 09:26:08Z; separate from M25 acceptance at 12:01:51.327507 +04:00 and M26 feature commit/publication verification at 12:50:47 / 12:52:09 +04:00.
- **Task / milestone ID:** AS-104 post-merge documentation closeout; E27 / EV-031.
- **Status:** AS-104 COMPLETE AND MERGED through PR #12; real acceptance PASS; no unresolved AS-104 P0 blocker. Known limitations retained.
- **Problem / question:** How should current project status close the merged temporal milestone while preserving earlier failures, accepted measurements and publication history?
- **Why it mattered:** A published branch and an accepted experiment are distinct from a merged milestone; the next agent needs accurate authorization and scientific boundaries.
- **Options considered:** Update current status with a later merge record while keeping M23–M26 intact; rewriting earlier pending/blocker states would lose chronology.
- **Decision:** Owner-authorized documentation-only closeout of the existing AS-104 implementation through PR #12. Execution/history event, not Decision 050.
- **Rationale:** Align handoff with verified main without altering algorithms, data, provenance identities or scientific claims.
- **Implementation / experiment:** Fetch and verify exact merged main; create isolated `docs/as-104-closeout`; inspect merged code/tests and case-only guard; reconcile seven authorized documents; preserve hashes/stashes/recovery material and run local quality gates. No EO experiment rerun.
- **Evidence:** [PR #12](https://github.com/Omar-Aboulwafa/aquasentinel-813/pull/12), title `feat: implement AS-104 temporal baseline`; main base `2006df7a70a4f48c66933aed96f4464d8d03084e`; feature head `703af1176aeaf9ba38d31c53648907c3b1792aec`; merge `472edc737847dc8581290a372c5da28f71fc48f0`. [Closeout evidence §9](evidence/AS_104_TEMPORAL_BASELINE_VALIDATION.md#9-pr-12-merge-and-as-104-closeout--9-october-2026).
- **Quantitative result:** Two commits (`09b38bd9c312470e948b1f17165ec5335cfc149d` implementation, `703af1176aeaf9ba38d31c53648907c3b1792aec` publication docs), fifteen PR paths. Final pre-merge 663 tests/Ruff/diff PASS, six existing Rasterio warnings. M25 scalar 18/18, causal check and repeat PASS; six AS-103 identities and twelve AS-102 cache-file hashes unchanged.
- **Limitation:** About 10% of 7,963 target-valid pixels per feature has five histories: 792/802/801/801/801/797. Five observations are not statistical sufficiency; small positive scales can produce large z. Rank is not probability/confidence/severity. Merge does not establish HAB/bloom, chlorophyll, species/toxins, safety, intake risk, persistence, alerts or warning lead time; no GitHub CI-success claim.
- **Lesson learned:** Record acceptance, publication and merge as distinct dated evidence-bearing checkpoints; close engineering work without overstating scientific validation.
- **Impact on next step:** Owner review of the next milestone/AS-105 design before implementation, with separate authorization. AS-105+ and P1 05.10 NOT STARTED. Retain both stashes and all external recovery artifacts.
- **Presentation takeaway:** “The reproducible temporal comparison is merged, with honest coverage and explicit scientific limits.”
- **Recommended visual:** M23 blocker → M24 fix → M25 accepted experiment → M26 publication → M27 merge timeline with sparse-support/guardrail card; capture pending, no screenshot claimed.
- **Candidate slide title:** “Close the temporal milestone without hiding its limits.”

### M28 — Frozen candidate policy and offline anomaly geometry

- **Date:** 9 October 2026 (Asia/Dubai); after merged AS-104 closeout and verified external handoff prerequisite.
- **Task / milestone ID:** AS-105 offline implementation; Decision 050 / E28 / EV-032.
- **Status:** PASS — synthetic implementation/adversarial validation; UNCOMMITTED / READY FOR OWNER REVIEW. Real geometry NOT RUN.
- **Problem / question:** How can causal spectral comparisons produce explainable spatial candidates without duplicate feature voting, hidden tuning or invented geometry?
- **Why it mattered:** Later reasoning needs exact spatial support and auditable lineage; early screening must not be mistaken for biological confirmation.
- **Options considered:** Rank/direction, z/direction or combined gates; feature/family voting; alternate rank/minimum/connectivity/filter policies. Comparisons are future predeclared work, not executed here.
- **Decision:** Owner-authorized Decision 050 freezes rank-valid, positive deviation and float32 0.90 evidence; two families including red-edge; independent availability denominator; eight-connected regions, no filter and exact pixel-edge geometry.
- **Rationale:** Count B05/red-related features once, preserve missing-support semantics and all candidates; expose the heuristic instead of optimizing on April 28. Families are not statistically independent.
- **Implementation / experiment:** Four new geometry modules, seven offline test files and seven documentation paths in an isolated worktree from `4e322df220f8cab2805fccf9a2b32dd825f29218`. Pure AS-104-parent extraction, canonical masks/identity/polygons, affine areas, output fingerprint and regeneration validation. No real handoff loaded into geometry.
- **Evidence:** [AS-105 contract](AS_105_HAB_ANOMALY_GEOMETRY.md), [M28 validation](evidence/AS_105_HAB_ANOMALY_GEOMETRY_VALIDATION.md), synthetic controls A–E and all 55 mandated adversarial requirements; protected upstream bytes/cache/handoff/stashes remain intact.
- **Quantitative result:** 136 new geometry cases PASS; 799 full tests PASS (663 retained), Ruff/diff/new-file whitespace PASS, six existing Rasterio warnings. Real candidate counts/fraction/area/regions/fragmentation/vote distribution UNKNOWN.
- **Limitation:** Engineering control results are not HAB accuracy. Rank is not probability/confidence/significance/severity; family agreement is not biological causation. Sparse five-history coverage and five-observation insufficiency remain. No real acceptance or comparative policy experiment.
- **Lesson learned:** Freeze the evidence denominator and binary threshold representation alongside the policy; prove exact geometry and reject rehashed tampering before interpreting real maps.
- **Impact on next step:** Owner review of uncommitted M28; separate authorization required for real geometry acceptance and bounded future policy validation. AS-106+ and P1 05.10 NOT STARTED.
- **Presentation takeaway:** “An explainable candidate map starts with an honest support denominator and a reproducible rule.”
- **Recommended visual:** Clearly labelled synthetic F1/F4 versus F4/F5 vote card, exact-threshold card and diagonal one-region/multipart round-trip diagram; capture pending. Do not substitute these fixtures for a real anomaly map.
- **Candidate slide title:** “From temporal signals to exact candidate geometry.”

### M28 owner-review reconciliation and feature publication authorization

10 October 2026 (Asia/Dubai), same M28/E28/EV-032 and Decision 050; no new
milestone. The 9 October implementation entry above preserves its historical
uncommitted stop state. Offline engineering review PASS; the owner requests a
five-history interpretation before authorizing publication. No-tie n=5 ranks
advance in 0.2 steps; the unchanged float32 0.90 screen requires five below,
or four below plus one exact tie. This is empirical upper-tail screening, not
a statistically estimated population percentile or probability/significance.
Four synthetic regression cases use unchanged AS-104 calculation; 140 geometry
and 803 full tests PASS, Ruff/diff PASS, six existing warnings. No algorithm,
upstream evidence or accepted-parent change. Feature commit/push is authorized;
this record accompanies publication, with exact Git/remote verification required.
PR not created; no merge. Future history-depth sensitivity is required where
valid EO allows deeper histories, with exact depths predeclared; NOT RUN.
Real geometry metrics UNKNOWN; future real checkpoint not created, AS-106+
and P1 05.10 NOT STARTED. Suggested visual: labelled five-history rank/tie ladder;
capture pending, not a real anomaly map or validation result.

### M29 — Frozen real temporal evidence to reproducible candidate geometry

- **Date:** 10 October 2026 (Asia/Dubai); first execution 05:45:15.046037–05:45:15.173566 UTC / 09:45:15.046037–09:45:15.173566 +04:00; acceptance completed 05:45:46.711968 UTC / 09:45:46.711968 +04:00. Owner review and this later publication are separate; no merge timestamp.
- **Task / milestone ID:** AS-105 real geometry engineering acceptance; M29 / E29 / EV-033.
- **Status:** REAL ENGINEERING ACCEPTANCE PASS; owner review PASS. M28 COMPLETE / COMMITTED / PUSHED; feature NOT YET PR-MERGED.
- **Problem / question:** Can the frozen reviewed extractor transform the accepted real AS-104 parent without tuning, upstream reruns or invented support/geometry?
- **Why it mattered:** Synthetic correctness needs a separately recorded real-parent engineering check before PR preparation; sparse support and empirical rank granularity must remain visible.
- **Options considered:** Execute the unchanged Decision 050 policy or stop on any verification mismatch. No alternate thresholds/family minima/connectivity/filtering were compared; zero or fragmented candidates would remain valid engineering outcomes.
- **Decision:** Owner-authorized real execution under unchanged Decision 050; execution/evidence checkpoint, not Decision 051.
- **Rationale:** Keep the predeclared policy independent of result appearance and separate reproducibility from scientific/event validation.
- **Implementation / experiment:** Verified handoff hashes/permissions; safely reconstructed 61-array parent; one initial extract and validation; independent literal masks/family OR/P/C, reference flood fill, determinant area and polygon round-trip; first metrics recorded, then one repeat; read-only 27-array external evidence bundle. No network, upstream processing or AS-102 cache loading.
- **Evidence:** Implementation `57100b2e53e941f3a7fdfdfc40b61d2b4043c0e5`, base `4e322df220f8cab2805fccf9a2b32dd825f29218`; [M29 validation](evidence/AS_105_HAB_ANOMALY_GEOMETRY_VALIDATION.md#m29--real-geometry-engineering-acceptance--10-october-2026); external `/workspace/aquasentinel-acceptance/as105/m29/` with recorded checksums, NOT tracked in Git. Product `hab_geometry:70876fbcb25e8a37abaa238a59e1da32fec9066792e6239db68e284b7bd18682`, input `c50d9f6300060ab9f194c1a0b8808de340eb53326268a52ef083ad7f994b2bc5`, output `ff976ec800ec2dfc966e4f373dd3f2442938a06a10254dd4ea7a86280dd0a765`.
- **Quantitative result:** P 802 / target water 7,963 = 10.071581% coverage; 7 candidates / P = 0.872818%; descriptive candidates/water 0.087907%; projected-grid candidate area 2,800 m² / 0.0028 km². One eight-connected region, three four-connected polygon parts; F2/F4 votes. All independent checks, repeat 27/27, parent immutability 61/61 and bundle audit PASS; 140 focused / 803 full tests, Ruff/diff PASS, six historical warnings.
- **Limitation:** P is not full AOI/ocean/risk coverage; sparse history remains material. No supported exact .90 rank; >=float32(.90) selected rank 1 only for this observed parent, while another exact-tie five-history pixel could attain .90. Five histories are not statistical sufficiency; families are not independent. No known-April-event comparison or HAB/bloom/concentration/species/toxin/accuracy/causation/persistence/risk/confidence/safety/intake/alert/lead-time inference.
- **Publication correction:** Owner confirmed the checksummed JSON's red_edge_red_ratio rank-.4/.6 counts **240/92**; the earlier chat's **238/93** was a transcription error. The artifact hash and measured result are unchanged; no rerun.
- **Lesson learned:** Separate evidence coverage from candidate fraction; one eight-connected region can honestly retain multiple polygon pieces. Real rank granularity needs future predeclared history-depth sensitivity, not retroactive tuning.
- **Impact on next step:** Owner review of M29 documentation/publication followed by PR preparation. Future comparative policy validation REQUIRED / NOT RUN; AS-106+ and P1 05.10 NOT STARTED.
- **Presentation takeaway:** “The frozen policy reproducibly produces seven candidate anomaly pixels on 802 evaluable pixels, with explicit limits.”
- **Recommended visual:** Capture pending: labelled P-versus-water support map, seven-pixel candidate/three-piece overlay, F2/F4 evidence card and five-history rank ladder. Do not present as HAB/event confirmation; no screenshot created by this documentation task.
- **Candidate slide title:** “Seven candidate pixels, an honest denominator, reproducible geometry.”

### M30 — AS-105 merged via PR #14 and formally closed

- **Date:** 10 October 2026; merge 06:24:09 UTC / 10:24:09+04:00 Asia/Dubai, after M29 acceptance and documentation publication.
- **Task / milestone ID:** AS-105 merge/publication closeout; M30 / E30 / EV-034.
- **Status:** COMPLETE AND MERGED; M28 offline/adversarial PASS and M29 real engineering PASS.
- **Problem / question:** How can the current handoff reflect official main without rewriting earlier blockers, publication states or scientific limitations?
- **Why it mattered:** Future agents need durable completed status and an explicit authorization boundary for the next milestone.
- **Options considered:** Update current status and append a separate merge checkpoint, or overwrite earlier pre-merge records. Preserve the original checkpoints.
- **Decision:** Record verified PR #14 merge/closeout as execution history; Decision 050 unchanged, no Decision 051.
- **Rationale:** A merge publishes reviewed evidence; it does not create new scientific validation or prove the policy optimal.
- **Implementation / experiment:** Fetched official main, verified GitHub merge metadata, created isolated documentation closeout worktree, reconciled current status and preserved historical entries. No real EO/geometry rerun or policy experiment.
- **Evidence:** [PR #14](https://github.com/Omar-Aboulwafa/aquasentinel-813/pull/14); [merge metadata and preservation](evidence/AS_105_HAB_ANOMALY_GEOMETRY_VALIDATION.md#m30--pr-14-merge-and-as-105-closeout--10-october-2026); merge `24a260cff130238c731f7cb62fc47eb74230b4dc`, previous main `4e322df220f8cab2805fccf9a2b32dd825f29218`, implementation `57100b2e53e941f3a7fdfdfc40b61d2b4043c0e5`, final head/M29 docs `1ac9fab9db48cca5625ead20e7133c79101a46d8`.
- **Quantitative result:** PR contained 2 commits, 18 files, 3,315 additions and 30 deletions. M29 unchanged: P=802/7,963, 7 candidates, 2,800 m² projected-grid candidate area, 1 MultiPolygon/3 parts; local baseline 803 tests PASS, Ruff/diff PASS, six existing Rasterio warnings.
- **Limitation:** Merge is not HAB/biological/accuracy/risk/confidence or CI validation. Five histories and ~10% support remain material limitations; future comparative policy validation REQUIRED / NOT RUN.
- **Lesson learned:** Preserve engineering acceptance, scientific validation and Git publication as separate evidence events.
- **Impact on next step:** Owner review of the next milestone / AS-106 design before implementation. AS-106+ is not authorized and NOT STARTED; P1 05.10 NOT STARTED.
- **Presentation takeaway:** Frozen-policy engineering evidence is now on official main with its scientific limits intact.
- **Recommended visual:** PR merge/timeline card beside evaluable-support and scientific-boundary cards; capture pending, no screenshot claimed.
- **Candidate slide title:** “Reviewed, reproducible, merged — with limits preserved.”

### AS-106 Decision 051 design freeze — planning only, 10 October 2026

- **Date / scope:** 10 October 2026 (Asia/Dubai); owner-approved documentation-only design freeze at base `b1b5147d9973d8cf23d575985319bf94a55a03d4`, branch `docs/as-106-design-freeze`.
- **Problem / why:** Distinguish recurrence from biological continuity, and make invalid-observation and sparse-history denominators explicit before implementation.
- **Options / decision:** Retain parent-aware validator rather than weaken validation or trust a mutable wrapper; exact-pixel recurrence rather than spatial matching; record real timing rather than invent a gap cutoff. Decision 051 freezes the accepted design; Decision 050 remains unchanged.
- **Rationale:** A valid non-candidate refutes the current streak; unsupported observations remain unknown. Temporal parents are integrity witnesses while AS-105 products are immediate provenance parents.
- **Implementation / experiment:** Design documentation only. No implementation, EO-service query, imagery read/download, new real processing or validation experiment. Existing AS-105 validator regeneration is explicitly allowed for future integrity checks.
- **Evidence / quantitative result:** [Frozen design](AS_106_PERSISTENCE.md), Decision 051 and owner authorization. Six accepted optical cache dates are March 4/9/14/24/29 and April 28; no verified earlier-April cache, exact earlier-April inventory unknown. These are prerequisite inventory facts, not recurrence results.
- **Limitation:** Real AS-106 acceptance BLOCKED ON FUTURE DATA PREPARATION. No observed recurrence result, biological inference, risk/confidence or statistical independence claim.
- **Lesson / next step:** Freeze comparison context and sequence-selection rules before outputs. Review published design, then explicitly authorize M31. M32–M35 are reserved future work, not executed milestone entries.
- **Presentation takeaway / candidate slide:** “Unknown is not absence: recurrence over valid observations.” Explain P/C/Q and honest candidate-history denominators; do not show fabricated real recurrence.
- **Recommended visual:** Conceptual timeline for candidate / unknown / valid non-candidate, labelled DESIGN ONLY; capture pending, no screenshot created.

### M31 — AS-106 offline observation recurrence — 10 October 2026

- **Date / task:** 10 October 2026 (Asia/Dubai); M31 / E31 / EV-035. Owner-authorized offline implementation and synthetic/adversarial validation at main `57185444f0cc963cc899a25cd8179d7a31f12119`; feature `feature/as-106-persistence`.
- **Problem / question:** Can repeated candidate observations be summarized causally without calling missing observations absence or implying continuous bloom duration?
- **Why it mattered:** Sparse observations require an explicit history denominator, exact timing and preserved source lineage before future real multi-date preparation.
- **Options considered / decision:** Frozen Decision 051: UNKNOWN skips; supported noncandidate breaks; exact same-grid pixels rather than motion/morphology; full AS-105 validation rather than weakened checks; existing NumPy/stdlib rather than a new dependency. No new decision.
- **Rationale:** Count every prior supported observation for Q but only the unbroken candidate streak for recurrence; keep witnesses separate from immediate provenance parents.
- **Implementation / experiment:** Pure persistence API and HABPersistenceScene, typed global/region evidence, canonical input/output fingerprints and regenerated validation. Synthetic/adversarial only; existing AS-105 regeneration is allowed integrity verification. No real handoff consumed, EO query/download, cache IO or upstream extraction by API.
- **Evidence:** [M31 validation](evidence/AS_106_PERSISTENCE_VALIDATION.md), `src/aquasentinel/persistence/`, `tests/persistence/`. 190 focused / 993 full tests PASS, Ruff/diff/whitespace PASS; six retained full-suite Rasterio warnings, no new/focused warnings.
- **Quantitative result:** Twelve seeded sequences independently checked over six pixels each. Synthetic two-date example has six target candidates, six history-evaluable candidates and six recurrent pixels (coverage/recurrence 1.0); this is a constructed test, NOT an EO observation.
- **Limitation:** Real recurrence NOT RUN / BLOCKED ON FUTURE DATA PREPARATION. No verified earlier-April cache or eligible inventory. Shared March histories are not independent confirmation; exact-pixel motion and long observation gaps remain limitations. No HAB/biology/accuracy/risk/confidence/safety claim.
- **Lesson learned / impact:** Output fingerprints alone cannot prove scientific integrity; regeneration from fully validated parents rejects rehashed tampering. Owner feature review is next; M32–M35 remain separately gated and NOT STARTED.
- **Presentation takeaway / recommended visual:** “Unknown is not absence.” A clearly labelled SYNTHETIC timeline comparing candidate→unknown→candidate versus candidate→supported-noncandidate→candidate, with Q/B/A denominator callouts. Visual capture pending; no screenshot created.
- **Candidate slide title:** “Recurrence over valid satellite observations — with honest gaps.”

### M32 — Predeclared metadata-only April sequence — 10 October 2026

- **Date / task:** 10 October 2026 (Asia/Dubai); M32 / E32 / EV-036, from PR #17 main `723e13a900dba30b73a8a2da39df1d984233a2f4`, branch `data/as-106-april-metadata-inventory`. Metadata query UTC 2026-10-10T08:23:54.186384+00:00 to 2026-10-10T08:24:00.344588+00:00; separate from later Git publication.
- **Problem / question:** Which April acquisitions satisfy the already-frozen recurrence-sequence contract, and what prerequisite stages actually exist?
- **Why it mattered:** Inventory must be frozen before inspecting anomalies; otherwise convenient dates or sparse-support outcomes could bias later recurrence evidence.
- **Options considered:** Reuse frozen CDSE/PC search and identity checks versus introduce a provider/helper; metadata-only key presence versus unauthorized raster/XML access; include every eligible date versus outcome-driven selection. Existing contracts and every eligible date were retained.
- **Decision / rationale:** Execute the owner-authorized Decision 051 inventory only; exactly one PC 05.09 match, tile/orbit/time/platform strict, no baseline substitution or anomaly filtering. No new architectural/scientific Decision.
- **Implementation / experiment:** External audit code, exact HTTPS metadata host/path and JSON-response guards, raster/signing entrypoints disabled, complete search pagination. Eligibility/digest frozen before read-only stage audit; no new production code.
- **Evidence:** [M32 metadata record](evidence/AS_106_APRIL_METADATA_INVENTORY.md), [normalized JSON](evidence/AS_106_APRIL_METADATA_INVENTORY.json), E32/EV-036. Digest `570792066c1997b9a403249d994c4e7367bf2f1dafc6473b6e30df20cd6481d5`.
- **Quantitative result:** 12 CDSE records across 2 pages; 2 pass metadata post-filter; 2 PC searches return 6 items with 2 exact 05.09 matches; 2 eligible dates (April 3 / April 28); all 11 required keys present. 10 metadata HTTP requests to only the 2 catalog hosts; ZERO asset requests / imagery bytes. 993 tests, Ruff/diff/whitespace/security checks PASS; six existing Rasterio warnings.
- **Limitation:** Key presence is not raster/XML/pixel suitability or usable support; only two dates qualify. Real recurrence NOT RUN; no biological persistence, HAB, risk/confidence or accuracy claim. Availability absence is limited to audited accepted artifacts/evidence.
- **Lesson learned:** Matching an acquisition does not make different processing products pixel-equivalent; PC 05.10 and adjacent-tile context must remain separate from the uniquely eligible 05.09 product.
- **Impact on next step:** April 3 needs AS-102→103→104→105; April 28 has verified accepted stage identities. Owner review and separate M33 authorization required; M33–M35 NOT STARTED. M31 is merged via PR #17; Decision 051 body unchanged.
- **Presentation takeaway:** Dates selected before seeing anomaly outcomes; no cherry-picking by support/candidate result and no imagery needed for inventory.
- **Recommended visual:** Two-date metadata timeline, tile/orbit exclusion funnel and stage-availability table with ZERO IMAGERY badge; visual capture pending, no screenshot created.
- **Candidate slide title:** “Choose dates before seeing anomaly outcomes.”

### M33 — Frozen April 3 upstream preparation and verified handoff — 10 October 2026

- **Date / task:** 10 October 2026 (Asia/Dubai); M33 / E33 / EV-037; base `200affdb7fb6f8801744a192511e4200cc0d100d`, branch `data/as-106-april3-upstream-preparation`. Preparation and later Git publication are separate events.
- **Problem / question:** Can the only missing predeclared April acquisition be prepared under unchanged production contracts and handed off offline for future recurrence?
- **Why it mattered:** Recurrence inputs must include every frozen eligible date, not only convenient anomaly results; metadata-key presence cannot prove usable native pixels.
- **Options considered:** Existing bounded production path versus custom downloader/full tile; exact PC 05.09 versus substitution; fixed references/policy versus tuning; typed verified bundle versus relying on scalar logs. Existing path and frozen identities/contracts retained.
- **Decision:** Execute owner-authorized M33 only; no new scientific/architectural Decision, no recurrence computation.
- **Rationale:** Establish real upstream availability and common-contract integrity before separately authorized M34; preserve accepted April 28 evidence.
- **Implementation / experiment:** Exact April 3 ingestion, XML decoding, AOI COG reads, AS-103/104/105; five March features reconstructed offline; real registry, repeated/scalar/causal/candidate/rasterization validations; external read-only 88-array handoff and fresh offline typed test.
- **Evidence:** [M33 record](evidence/AS_106_APRIL3_UPSTREAM_PREPARATION.md), [JSON](evidence/AS_106_APRIL3_UPSTREAM_PREPARATION.json), E33/EV-037; exact unchanged M32 digest.
- **Quantitative result:** 6,096 valid-water pixels; six feature supports 6,096; temporal eligible 784/794/793/793/793/789, zero MAD 0; P794, 88 candidates (11.083123% of P), 15 regions, 35,200 m². Common contract PASS; 18/18 scalar checks; 88/88 offline array checks; 408 focused / 993 full tests PASS, six existing warnings; Ruff/diff/credential PASS. Seven observed Python HTTP operations plus ten bounded native COG reads; internal GDAL HTTP counts/bytes not measured.
- **Limitation:** ~13% target-water policy support; five shared March references are not statistical sufficiency/independent confirmation; rank not probability/confidence/severity. No HAB/biology/recurrence/risk/accuracy claim; future policy validation NOT RUN.
- **Lesson learned:** JSON list/tuple coordinates and legacy display fields require canonical equality/explicit typed projection; initial external adapter assertions failed, then passed without source/scientific changes or new remote processing. Retained old logs/artifacts.
- **Impact on next step:** Both frozen April dates have compatible reconstructable typed inputs. M34 INPUTS READY, not M34 PASS; owner review and separate authorization required. M34/M35/AS-107+/P1 05.10 NOT STARTED.
- **Presentation takeaway:** Preserve dates and policy first, then report the observed support/result and prove offline reconstruction.
- **Recommended visual:** Two-date stage-readiness diagram with support denominators and handoff checksum card; capture pending, no screenshot claimed.
- **Candidate slide title:** “Two frozen observations, verified inputs — recurrence still gated.”

### M34 — Real exact-pixel recurrence engineering acceptance — 10 October 2026

- **Date / task:** 10 October 2026 (Asia/Dubai); M34 / E34 / EV-038; PR #19 main `4cde14ee448079163c2a08f3951f8dac294f8dac`; branch `data/as-106-real-acceptance`. Scientific execution, bundle sealing and later Git publication are distinct.
- **Problem / question:** What does the frozen two-observation sequence establish about exact-pixel recurrence at April 28 target candidates?
- **Why it mattered:** Valid prior support must define the fraction denominator; unknown must not become absence, and zero outcomes must not trigger tuning/date changes.
- **Options considered:** Verified offline typed handoffs versus unnecessary upstream reruns/network; exact-pixel frozen policy versus motion/region matching; retain zero result versus unauthorized tuning. Existing contract and complete sequence retained.
- **Decision:** Execute the owner-authorized real as106-v1 API and independent two-date oracle; no new architecture/science Decision.
- **Rationale:** Separate reproducible engineering recurrence from biological/event validation and prove actual support/identity/timing.
- **Implementation / experiment:** Four typed parents/hash/mode/policy/common-contract guards; first production recurrence, direct Boolean/scalar/time/global/region oracles, same/reversed caller repeats, seven in-memory tamper controls; read-only nine-array acceptance bundle/fresh typed offline audit. No public upstream processing.
- **Evidence:** [M34 acceptance](evidence/AS_106_REAL_ACCEPTANCE.md), [JSON](evidence/AS_106_REAL_ACCEPTANCE.json), E34/EV-038; unchanged M32 digest and M33/April 28 artifacts.
- **Quantitative result:** Target P802 / Q793 / A7 / B7 / C0; history coverage 7/7=100%; recurrence 0/7=0.0; all seven singleton streaks. Gap 25 days+8 seconds, exactly 2,160,008,000,000 µs; regional recurrent spans None. Nine arrays/dtypes PASS; 190 focused/993 full tests PASS, six existing warnings; Ruff/diff/security PASS; scientific network zero.
- **Limitation:** No same-pixel recurrence among seven history-supported targets does not establish absence of HAB. Long observation gap, movement, shared five March references, sparse upstream support and unvalidated screening policy remain limitations; no biology/risk/confidence/accuracy claim.
- **Lesson learned:** Recurrence evaluability and upstream policy coverage use different denominators: April 3 ~13% support cannot replace target candidate history 7/7. Empty recurrent-span summaries are None even when target singleton spans are zero.
- **Impact on next step:** M34 real engineering acceptance COMPLETE; AS-106 not fully closed. Owner review and separately gated M35 next, NOT STARTED; AS-107+/policy study/P1 05.10 NOT STARTED.
- **Presentation takeaway:** “Zero is a result, not a reason to tune.” Frozen dates/policy, honest support and independently reproducible recurrence.
- **Recommended visual:** Two-date seven-pixel P/C state table, Q/A/B/C denominator diagram and exact observation-gap timeline; capture pending, no screenshot claimed.
- **Candidate slide title:** “Seven supported candidates — no observed same-pixel recurrence.”

### M35 — AS-106 publication / formal closeout preparation — 10 October 2026

- **Date / task:** 10 October 2026 (Asia/Dubai); M35 / E35 / EV-039; PR #20 baseline `82e30c00a30ed893ad47c44c5a1e363661370d35`; prepared on `docs/as-106-closeout`. No new science.
- **Problem / question:** How do we publish accepted recurrence coherently, preserve limitations/history, and hand off a closed milestone without claiming biological truth?
- **Why it mattered:** A one-date spectral anomaly can mislead; an observational zero must not be relabelled absence of HAB or tuned into a stronger demonstration.
- **Options considered:** Consolidate accepted evidence versus unauthorized rerun/alternative recurrence; exact public statement versus biological overclaim; closure effective on merge versus another post-merge documentation loop. Accepted evidence and durable merge-effective closure retained.
- **Decision:** Owner-authorized publication/closeout only; no new scientific/architectural Decision. Decision 051 FINAL/FROZEN/MERGED; original scientific text unchanged, no Decision 052.
- **Rationale:** Separate measured acceptance, Git publication, merge and official closure, with one consistent forward handoff and explicit authorization boundaries.
- **Implementation / experiment:** Documentation reconciliation only; local Git ancestor/PR merge-subject verification through #20; read-only hashes/modes of accepted artifacts and bundle; eight documentation paths. No scientific experiment/reconstruction.
- **Evidence:** [M35 closeout](evidence/AS_106_CLOSEOUT.md), [JSON](evidence/AS_106_CLOSEOUT.json), E35/EV-039; unchanged M32/M33/M34 evidence.
- **Quantitative result:** Accepted P802/Q793/A7/B7/C0, history coverage 7/7=1.0, recurrence 0/7=0.0, streak1→7, exact 25-day+8-second gap. M34 9/9 array/dtype/oracle/repeat/tamper/bundle integrity PASS; measurements not rerun in M35. M35 final quality gates recorded in closeout evidence.
- **Limitation:** Exact-pixel observation only; two eligible dates, long gap, unknown support, shared five March histories, sparse upstream support and unvalidated screening policy. No biological persistence/absence, HAB, risk/confidence/probability/safety/accuracy or operational decision claim.
- **Lesson learned:** Preserve zero instead of changing dates, thresholds, family/connectivity rules or spatial tolerance; denominator clarity and reproducibility can be a presentation strength.
- **Impact on next step:** M35 closeout prepared/pending merge; its merge itself makes AS-106 COMPLETE/CLOSED. Owner review/authorized PR+merge next; AS-107 requires separate design/authorization, NOT STARTED.
- **Presentation takeaway:** Problem: one-date anomaly can mislead. Design: metadata-freeze every eligible date, compare only valid observations, UNKNOWN for missing support. Result: seven April 28 candidates had prior history, zero same-pixel prior candidates. Why: kept zero without tuning. Claim: reproducible observational recurrence; no biological/event truth.
- **Recommended visual:** Frozen-selection→April3(88 candidates)→April28(7)→supported7/recurrent0 story, with denominator/UNKNOWN and long-gap limits; capture pending, no screenshot claimed.
- **Candidate slide title:** “We kept zero recurrence — and its evidence.”

### M36 — AS-107 read-only feasibility/design audit — 10 October 2026

- **Date / task:** 10 October 2026 (Asia/Dubai); M36 / E36 / EV-040; prior audit, recorded retrospectively in M37.
- **Problem / question:** Can a scoring layer use current typed evidence while context/exposure are unavailable?
- **Why it mattered:** Missing inputs must not appear reassuring or create biological certainty.
- **Options considered:** Zero/neutral missing values, available-weight renormalization, full-input refusal and qualified provisional screening.
- **Decision:** Audit recommended revisions before freeze; owner later approved the explicit M37 policy.
- **Rationale:** Separate evidence strength, completeness, availability and scientific validation.
- **Implementation / experiment:** Read-only repository/interface audit, no real score or scientific product.
- **Evidence:** [M36 record](evidence/AS_107_DESIGN_FREEZE.md#m36--e36--ev-040--prior-read-only-audit-complete).
- **Quantitative result:** Five configured components; no real scoring result calculated. No new implementation test result claimed.
- **Limitation:** Heuristic weights, correlated families, unavailable context/exposure and observational upstream evidence.
- **Lesson learned:** Explicit regional denominators and typed integrity witnesses are needed before scoring.
- **Impact on next step:** M37 design freeze required owner review; audit did not authorize implementation.
- **Presentation takeaway:** Missing is unknown, not no risk; completeness is separate from score.
- **Recommended visual:** Availability versus evidence-strength diagram; capture pending, no visual claimed created.
- **Candidate slide title:** “Freeze the rules before looking at the score.”

### M37 — Decision 052 AS-107 policy freeze — 10 October 2026

- **Date / task:** 10 October 2026 (Asia/Dubai); M37 / E37 / EV-041; official base PR #21 merge `6b22d32f078ef80158b2f2d7aac4f3dd07925038`.
- **Problem / question:** How can provisional HAB-like screening stay deterministic, explainable and scientifically bounded?
- **Why it mattered:** Formula selection must precede real risk-band inspection; missing inputs cannot be zero or fabricated context.
- **Options considered:** M36 alternatives; owner approved pooled family-pixel breadth, availability-aware weighting and minimum-factor completeness.
- **Decision:** Decision 052 FINAL / FROZEN DESIGN — NOT IMPLEMENTED; primary evidence_completeness and provisional_observational_screening status.
- **Rationale:** Reuse frozen AS-105/106 evidence without new upstream thresholds; disclose correlated red-edge emphasis and unavailable inputs.
- **Implementation / experiment:** Documentation/policy only, typed API/provenance/identity and future acceptance matrix; no production scorer or real experiment.
- **Evidence:** [Decision 052](DECISIONS.md#decision-052--as-107-explainable-availability-aware-hab-risk-and-evidence-completeness), [contract](AS_107_HAB_RISK.md), [M37 record](evidence/AS_107_DESIGN_FREEZE.md#m37--e37--ev-041--frozen-policy).
- **Quantitative result:** Configured coverage ceiling 0.70, or 0.55 without persistence; 0.50 administrative interpretation flag. Policy consequences only, no real score/band. Actual M37 regression gates recorded separately in evidence.
- **Limitation:** No calibrated probability/confidence, biological confirmation, exposure completeness, event accuracy or warning lead time.
- **Lesson learned:** A High raw score can remain High while visibly qualified by limited evidence completeness.
- **Impact on next step:** Owner review/design PR+merge and separate M38 authorization; M38–M40 NOT STARTED, AS-108 NOT STARTED.
- **Presentation takeaway:** Rules, missing reasons and denominators make the future score reconstructable; outcome tuning is prohibited.
- **Recommended visual:** Five-driver contribution/availability layout beside completeness factors; proposed visual only, no real scoring graphic.
- **Candidate slide title:** “An explainable score — with its missing evidence visible.”

### M38 — AS-107 offline implementation and adversarial engineering validation — 10 October 2026

- **Date / task:** 10 October 2026 (Asia/Dubai); M38 / E38 / EV-042; PR #22 base `49f5276b1ad372725b21cdb2085815225c98eed4`.
- **Problem / question:** Implement the frozen availability-aware risk policy without inferring missing context or interpreting a real outcome.
- **Why it mattered:** Explanations, support denominators and provenance must remain auditable under manipulation.
- **Options considered:** Frozen M37 alternatives are unchanged; reuse parent validators and a pure scalar kernel rather than add IO/providers/cache or upstream refactors.
- **Decision:** Execute Decision 052 unchanged. No Decision 053; implementation authorization is not real-acceptance authorization.
- **Rationale:** Separate score/band from evidence completeness, retain unknown inputs, and validate from authoritative typed parents rather than trusting stored hashes.
- **Implementation / experiment:** Four risk modules; synthetic fixtures only; exact regional counting, drivers, site summary, identity/fingerprints and full regeneration validation.
- **Evidence:** [M38 validation](evidence/AS_107_IMPLEMENTATION_VALIDATION.md), `src/aquasentinel/risk/`, `tests/risk/`; E38 / EV-042.
- **Quantitative result:** 292 focused tests PASS; 1285 full tests PASS; six existing Rasterio warnings; Ruff/diff/preservation PASS. These counts are engineering results, not measured real risk.
- **Limitation:** No real AS-107 score/band, biological accuracy/calibration, missing context/exposure implementation or operational risk claim.
- **Lesson learned:** Rehashed attacker output still needs independent authoritative-parent regeneration; low completeness qualifies a High synthetic score without changing its stored band.
- **Impact on next step:** Owner implementation review; M39 real acceptance and M40 closeout remain separately gated/NOT STARTED.
- **Presentation takeaway:** “Explainable” includes missing reasons, exact denominators, correlated inputs and tamper-resistant lineage.
- **Recommended visual:** Synthetic-only five-driver/completeness and tamper-rejection diagram; proposed, capture pending, no real score graphic.
- **Candidate slide title:** “The score can explain itself — and prove where it came from.”

### M39 — First real provisional observational screening result — 10 October 2026

- **Date / task:** 10 October 2026 (Asia/Dubai); M39 / E39 / EV-043; PR #23 main `7f304bb44af93d2b3a1a3e6982fefad05fb8f452`. First call 2026-10-10T13:04:58.495566+00:00 → 2026-10-10T13:04:58.732346+00:00 UTC; later publication separate.
- **Problem / question:** Does the already frozen as107-v1 policy reproducibly consume accepted real AS105/106 evidence without tuning around its outcome?
- **Why it mattered:** A demo score needs auditable denominators, explicit missingness and engineering reproducibility; biological truth cannot be inferred from arithmetic success.
- **Options considered:** Only the frozen policy was authorized; no weight/band/threshold/source/date/recurrence alternatives were tried after result inspection.
- **Decision:** Execute Decision 052 unchanged, offline; no Decision 053. M39 acceptance is distinct from M40 closeout and AS108 biological calibration.
- **Rationale:** Preserve the first output and compare it with an independent oracle rather than optimize the band for presentation.
- **Implementation / experiment:** Fresh temporary sealed-schema typed reconstruction; pre-score policy digest; three public calls, independent counts/arithmetic/framing, full validators, 13 ordinary/3 attacker-rehashed controls and sealed fresh-process roundtrip.
- **Evidence:** [M39 report](evidence/AS_107_REAL_ACCEPTANCE.md), [JSON](evidence/AS_107_REAL_ACCEPTANCE.json), sealed external bundle `/workspace/aquasentinel-acceptance/as107/m39/113143700cb35ac9230d9c54b68b1b53e2573838a4913d4bc942e81c99903fdb`.
- **Quantitative result:** One seven-pixel region, a=(7,7,7,7,7), v=(0,7,0,7,0); S=40.0, E=33.333333333333336, T=0.0; score 29.52380952380953 / Watch; coverage/completeness 0.7/0.7; F_all/F_red/H=1/1/1. Independent exact binary64/IDs/fingerprints/repeats/tamper/preservation PASS; scientific requests/downloads zero.
- **Limitation:** Context/exposure unavailable; correlated red-edge emphasis and uncalibrated hypotheses; seven candidates within sparse five-history support; two dates/25-day gap, no biology/accuracy/water-safety/intake/lead-time validation.
- **Lesson learned:** Available persistence=0 is distinct from missing evidence; full regional availability cannot make missing context/exposure complete. Watch does not mean safe water.
- **Impact on next step:** Owner review of published M39 evidence; PR/M40 and AS108 separately gated, NOT STARTED. Future AS105 policy study NOT RUN; P1 05.10 NOT STARTED.
- **Presentation takeaway:** Under the frozen AS-107 observational screening policy, the April 28 validation AOI produced a Watch observational screening score of 29.52380952380953, with evidence completeness 0.7 and component coverage 0.7. Environmental context and intake exposure remain unavailable. The result is provisional observational screening, not confirmed HAB or operational water-safety determination.
- **Recommended visual:** Five-driver denominator/contribution table beside separate 29.52380952380953 / Watch and .7 completeness/coverage card; prominent provisional/context/exposure label. Proposed, capture pending; no screenshot created.
- **Candidate slide title:** “A real score with its missing evidence left visible.”

### M40 — Publish the accepted screening result without tuning its outcome — 10 October 2026

- **Date / task:** 10 October 2026 (Asia/Dubai); M40 / E40 / EV-044. Publication/closeout preparation only; experiment time remains the separate M39 record.
- **Problem / question:** A single satellite anomaly can be scientifically ambiguous and operationally misleading. How can the accepted result be handed off without hiding missingness or implying biological confirmation?
- **Why it mattered:** Presentation credibility requires a frozen policy, reconstructable evidence and clear limits, rather than a stronger-looking score.
- **Options considered:** Durable merge-effective closeout versus a further post-merge documentation loop; retain the observed Watch result versus unauthorized tuning. Only publication of existing accepted evidence was authorized.
- **Decision:** Prepare closeout on verified PR #24 main; future closeout merge is the closure event. No new architectural/scientific Decision; Decision 053 absent.
- **Rationale:** Distinguish policy freeze, implementation, real acceptance, publication and closure; preserve the accepted outcome and historical evidence.
- **Implementation / experiment:** Git parent/ancestor/tree checks for PRs #22/#23/#24; read-only M39 file/bundle rehash; documentation-only handoff; local engineering tests. No real scoring, parent reconstruction or EO retrieval.
- **Evidence:** [M40 closeout](evidence/AS_107_CLOSEOUT.md), [JSON](evidence/AS_107_CLOSEOUT.json), unchanged [M39 evidence](evidence/AS_107_REAL_ACCEPTANCE.md); M37–M39 historical records remain separate.
- **Quantitative result:** Accepted Watch = 29.52380952380953, completeness = 0.7, coverage = 0.7; spectral 14/35, red-edge 7/21, persistence A/B/C = 7/7/0. 1285 full tests PASS (104.18s), six existing Rasterio PendingDeprecationWarnings; Ruff/diff/new-file whitespace/credential/preservation PASS. No new scientific measurement.
- **Limitation:** Provisional observational screening only. Environmental context and intake exposure unavailable; exact-grid recurrence, long gap, sparse/shared references, BOA semantics and correlated evidence do not establish biological or operational truth.
- **Lesson learned:** Missing evidence must remain missing. A real result is credible when the policy preceded it and tampering is rejected, not because the band looks dramatic.
- **Impact on next step:** AS-107 CLOSEOUT READY before future closeout PR merge; COMPLETE / CLOSED after that merge. Owner authorization required for PR/merge and any AS-108 work; AS-108, future AS-105 policy validation and P1 05.10 NOT STARTED.
- **Presentation takeaway:** Freeze policy before real scoring; combine spectral anomaly, red-edge evidence breadth and observational persistence while separating risk score from completeness. Preserve the real Watch result, explain missing components, and recommend review on the next valid acquisition. Field verification remains the path to biological/operational confirmation.
- **Recommended visual:** Five-driver denominator/contribution table plus separate Watch/completeness/coverage cards and a freeze → implementation → acceptance → publication chain. Proposed visual only; no screenshot or figure is claimed to exist.
- **Candidate slide title:** “A Watch result we can explain — without pretending it proves a bloom.”

### M41 — Historical read-only validation feasibility / source audit — 10 October 2026

- **Date / task:** 10 October 2026 (Asia/Dubai); M41 / E41 / EV-045, retrospectively documented during M42. M41 changed no repository file and created no branch/commit.
- **Problem / question:** What could existing EO evidence legitimately establish about the documented Raha Beach April 2023 event?
- **Why it mattered:** Month-level reporting and analyst AOI context cannot support precise onset lead time or biological pixel accuracy.
- **Options considered:** Full before/event/after biological validation versus a narrow observational case; exact timing versus explicit unavailable lead time.
- **Decision:** Recommend REVISE before freeze, pending source verification and explicit POST/causal PRE scope. No Decision in M41.
- **Rationale:** Keep ground truth separate from reproducible satellite engineering and avoid fabricating missing May or negative labels.
- **Implementation / experiment:** Read-only Git/contracts/cache-manifest/stage inventory; six documentary source attempts blocked by proxy403. No EO query, array loading or science.
- **Evidence:** Historical M41 owner-reviewed chat audit; preserved local read-only audit; its facts transcribed in [M42 freeze](evidence/AS_108_DESIGN_FREEZE.md#historical-m41-and-numbering). No separate M41 repository publication existed.
- **Quantitative result:** Seven accepted AS-102 caches; five March AS-103 references; April 3 through AS-105, April 28 through AS-107; May summary metadata but no accepted May product; zero EO/scientific calls.
- **Limitation:** EAD PDF inaccessible inside Codex; title/report-year/location/time/toxin passage not independently verified there; complete March–May product inventory not retained.
- **Lesson learned:** PRE dates are not negatives, POST cannot be invented and available Watch output is not biological ground truth.
- **Impact on next step:** The project owner subsequently supplied externally verified EAD listing/PDF facts for M42; no personal owner inspection is claimed. This later resolution does not rewrite the M41 blocker.
- **Presentation takeaway:** Validate only the claim the reference can support.
- **Recommended visual:** Proposed source-precision and stage-availability matrix; no screenshot/visual claimed to exist.
- **Candidate slide title:** “What the historical reference can—and cannot—tell us.”

### M42 — Freeze the retrospective observational-consistency case — 10 October 2026

- **Date / task:** 10 October 2026 (Asia/Dubai); M42 / E42 / EV-046; Decision 053; base PR #25 `14149113e58788621d6aef91f039b95781c67434`.
- **Problem / question:** How can a one-event retrospective case be evaluated without outcome-dependent dates, policies or unsupported biological claims?
- **Why it mattered:** Credibility before the 11 October deadline requires a narrow, denominator-aware design and preservation of inconvenient results.
- **Options considered:** Broad accuracy/multi-event study versus minimum P0 case; independent PRE scoring versus descriptive fixed March context; chosen-looking May scene versus earliest compatible metadata-selected attempt.
- **Decision:** Decision 053 FINAL / FROZEN DESIGN — NOT EXECUTED; March descriptive, both April observations, one future May attempt, null/unavailable outcomes retained.
- **Rationale:** Freeze scene roles, eligibility and reporting before new outcomes; source month/area precision constrains claims, not policy tuning.
- **Implementation / experiment:** Documentation/schema only. Externally verified EAD facts supplied by the project owner resolve M41 source access blocker; no external research/EO/scientific execution here.
- **Evidence:** [Decision 053](DECISIONS.md#decision-053--as-108-historical-validation-contract), [AS-108 contract](AS_108_HAB_HISTORICAL_VALIDATION.md), [M42 evidence](evidence/AS_108_DESIGN_FREEZE.md), [JSON](evidence/AS_108_DESIGN_FREEZE.json).
- **Quantitative result:** One event, five PRE records, two EVENT records, one future attempted POST; EAD reports 23 incidents in 2023 but that count is not a labeled validation dataset. 1285 full tests PASS (115.87s), six existing Rasterio PendingDeprecationWarnings; Ruff PASS; diff/new-file whitespace PASS. No new validation outcome or score.
- **Limitation:** Month-only onset, area-only context, no incident toxin measurement, no biological negatives/accuracy/lead time; correlated features, sparse/shared histories, long gaps, missing operational components and possible POST unavailability remain.
- **Lesson learned:** A frozen limited study is stronger than a broad unsupported accuracy claim; missing evidence must stay visible.
- **Impact on next step:** Separate owner review/PR/merge approval, then separately authorize M43 metadata-only earliest-May selection before any pixels. AS-201 and validation execution NOT STARTED.
- **Presentation takeaway:** Freeze the evaluation before looking at new outcomes. EAD names the event/species/toxin association; AquaSentinel explains observational signals without pretending to identify species or toxin.
- **Recommended visual:** Proposed external-reference versus satellite-evidence lanes and PRE/EVENT/POST availability timeline. No screenshot/figure claimed to exist.
- **Candidate slide title:** “An honest historical case, designed before the next result.”

### M43 — Retain an unavailable POST scene instead of choosing a better-looking date — 10 October 2026

- **Date / task:** 10 October 2026 (Asia/Dubai); M43 / E43 / EV-047; metadata-only selection from PR #26 main `8bb56f12f2cd683d4a96f069c5d049bf4a39799e`.
- **Problem / question:** Does the frozen earliest May acquisition resolve uniquely to a compatible PC05.09 product before any pixel inspection?
- **Why it mattered:** Outcome-independent selection must remain auditable even when provider compatibility blocks the requested analytical phase.
- **Options considered:** Frozen chronological selection/no fallback versus querying later dates or relaxing the resolver; the latter options were not authorized.
- **Decision:** Execute unchanged Decision053; complete inventory, fix earliest eligible May3 identity, retain UNAVAILABLE after empty exact resolver query. No new Decision.
- **Rationale:** Preserve missing evidence rather than substitute a scientifically convenient date or infer absence from sparse metadata.
- **Implementation / experiment:** Existing STAC transport/strict metadata identities in an ephemeral external script; six full CDSE pages and one empty PC page; no assets or scientific processing.
- **Evidence:** [M43 metadata evidence](evidence/AS_108_POST_METADATA_SELECTION.md), [full inventory/digest](evidence/AS_108_POST_METADATA_SELECTION.json); `df487999defada56023a7e76be69c507b2b1ff11d81de1480737eca86a1ad4de`.
- **Quantitative result:** 26 provider records/26 timestamp-platform-tile-orbit keys/13 timestamps; four CDSE-eligible acquisitions; May3 cloud0.57%; zero PC matches; CDSE8/PC3 metadata requests; assets/bytes/science0. 1285 full tests PASS (106.24s), six existing Rasterio PendingDeprecationWarnings; Ruff PASS; diff/new-file whitespace PASS.
- **Limitation:** Empty resolver-window result does not establish global catalog absence or May biological state. PC compatibility of later dates unassessed; native headers/support/science unknown.
- **Lesson learned:** Metadata unavailability is a legitimate frozen-rule result; transparency includes retaining inconvenient failure without outcome-driven substitution.
- **Impact on next step:** Owner review, separate PR/merge approval and any separately authorized metadata investigation; no M44 pixels/science or AS-201.
- **Presentation takeaway:** POST was attempted using a rule frozen before inspecting May pixels; missing evidence was retained, not hidden.
- **Recommended visual:** Proposed six-page inventory/eligibility funnel with four dates, May3 empty PC response and zero-pixel boundary. No screenshot or visual claimed to exist.
- **Candidate slide title:** “The date we did not replace.”

### M44 — An honest result is useful when one phase is missing — 10 October 2026

- **Date:** 10 October 2026 (Asia/Dubai); reporting publication, not new experiment time.
- **Task:** AS-108 M44 / E44 / EV-048, retrospective historical case-study reporting.
- **Problem/question:** What does accepted evidence support about the documented Raha Beach April2023 event when POST is unavailable?
- **Why it mattered:** Deliver narrow credible P0 validation without hiding missing data or spending oil-pipeline time repairing POST.
- **Options considered:** Frozen accepted-evidence reporting; new May/April3 downstream science or fallback would require separate authorization and were excluded.
- **Decision:** Apply unchanged Decision053; no new scientific/architectural decision.
- **Rationale:** Both accepted EVENT endpoints are evaluable/positive; required POST context is missing, yielding PARTIALLY_CONSISTENT.
- **Implementation/experiment:** Scalar/count reconstruction and deterministic reporting only; no EO or scientific experiment.
- **Evidence:** [M44 report](evidence/AS_108_HISTORICAL_CASE_STUDY.md), [JSON](evidence/AS_108_HISTORICAL_CASE_STUDY.json), accepted M33/M29/M34/M39, frozen M42 and merged M43.
- **Quantitative result:** PRE5/5 descriptive evaluable; EVENT2/2 candidate-positive; April3 88/P794, April28 7/P802; Watch1/1 scored,1/2 retained with one unscored; POST0/1 required slot evaluable. Accepted Watch29.52380952380953, completeness/coverage0.7/0.7 unchanged.
- **Limitation:** One retrospective month/area case; April outputs known before freeze; no biological accuracy, exact lead time, independent validation or recovery claim.
- **Lesson learned:** Retain inconvenient missingness and keep reporting integrity distinct from predictive accuracy.
- **Impact on next step:** Owner review/PR/merge separately authorized; then separate AS-201 authorization. No POST repair in M44.
- **Presentation takeaway:** Documented event. Observable signal. Missing POST retained.
- **Recommended visual:** PRE/EVENT/POST availability strip with POST missing; proposed only, no screenshot claimed.
- **Candidate slide title:** Validation without hiding missing evidence.

### M45 — Historical read-only Sentinel-1 feasibility audit — historical predecessor or design checkpoint

- **Date / task:** Pre-M47 read-only audit; exact audit timestamp not recorded here; AS-201 M45/E45/EV-049, recorded during M47 on 11 October 2026.
- **Problem / question:** Which metadata-compatible source sequence can support a Kharg surface-slick demonstration?
- **Why it mattered:** Scientific representation and defensible selection precede oil-candidate inference.
- **Options considered:** CDSE source discovery; PC GRD/RTC; Sentinel Hub; multiple documentary radar dates.
- **Decision:** Recommend same S1A ascending orbit101 Apr24/May6/May18; two slices per date.
- **Rationale:** Documentary timing and metadata compatibility before SAR output inspection.
- **Implementation / experiment:** Read-only metadata feasibility; no repository writes or pixel/science execution.
- **Evidence:** [M47 accepted predecessor/design record](evidence/AS_201_DESIGN_FREEZE.md) and [JSON](evidence/AS_201_DESIGN_FREEZE.json); prior temporary files are not repository artifacts.
- **Quantitative result:** Three-role sequence recommended; six exact source products retained for later audit.
- **Limitation:** Envelope is analyst geometry; no petroleum polygon/truth or raster suitability claim.
- **Lesson learned:** Choose dates before scientific output.
- **Impact on next step:** M46 provider/access/representation gate; not executed by this entry.
- **Presentation takeaway:** Before looking for dark pixels, freeze the same-track sequence and raw-data contract.
- **Recommended visual:** Metadata-only three-date timeline; proposed, no screenshot/figure claimed to exist.
- **Candidate slide title:** “Before looking for dark pixels.”

### M46 — Historical provider/access/header/XML gate — historical predecessor or design checkpoint

- **Date / task:** Pre-M47 read-only audit; exact audit timestamp not recorded here; AS-201 M46/E46/EV-050, recorded during M47 on 11 October 2026.
- **Problem / question:** Can credential-free raw GRD provide the metadata needed for later local SAR preprocessing?
- **Why it mattered:** Scientific representation and defensible selection precede oil-candidate inference.
- **Options considered:** PC GRD local preprocessing vs RTC vs Sentinel Hub; asset keys vs validated XML roles.
- **Decision:** PC GRD access PASS; raw amplitude and representative noise/calibration structures verified.
- **Rationale:** Bounded access avoids full scenes; headers/XML resolve misleading STAC metadata.
- **Implementation / experiment:** Six VV and one VH header; representative VV manifest/product/calibration/noise XML; retained allowlist blocker, RFI and 404 failures.
- **Evidence:** [M47 accepted predecessor/design record](evidence/AS_201_DESIGN_FREEZE.md) and [JSON](evidence/AS_201_DESIGN_FREEZE.json); prior temporary files are not repository artifacts.
- **Quantitative result:** 7 headers / 224 ranges / 115,563 header bytes; 3,298,504 XML bytes; zero pixels.
- **Limitation:** No calibration/noise removal; representative VV only; no VH LUT proof or guaranteed future access.
- **Lesson learned:** COG packaging and asset labels do not establish scientific representation.
- **Impact on next step:** M47 source contract freeze; not executed by this entry.
- **Presentation takeaway:** Before looking for dark pixels, freeze the same-track sequence and raw-data contract.
- **Recommended visual:** Header/XML defect-to-validation card; proposed, no screenshot/figure claimed to exist.
- **Candidate slide title:** “Before looking for dark pixels.”

### M47 — Freeze sources before looking for dark pixels — historical predecessor or design checkpoint

- **Date / task:** 11 October 2026 (Asia/Dubai); AS-201 M47/E47/EV-051, recorded during M47 on 11 October 2026.
- **Problem / question:** How can future retrieval avoid outcome-driven date/provider/AOI choices?
- **Why it mattered:** Scientific representation and defensible selection precede oil-candidate inference.
- **Options considered:** Broad vs narrowed envelope; raw GRD vs alternate representation; scientific preprocessing now vs later dedicated design.
- **Decision:** Decision054 as201-v1 exact six-source raw GRD contract; broad envelope, explicit gaps, no fallback.
- **Rationale:** Preserve southern documentary geography and same-track reproducibility; separate access proof from science.
- **Implementation / experiment:** Documentation/policy only; canonical design digest, strict JSON, engineering and preservation checks.
- **Evidence:** [M47 accepted predecessor/design record](evidence/AS_201_DESIGN_FREEZE.md) and [JSON](evidence/AS_201_DESIGN_FREEZE.json); prior temporary files are not repository artifacts.
- **Quantitative result:** 3 roles; 2 mandatory slices/date; exact PC cardinality1 each; 1,285 tests PASS (36.40s), six existing Rasterio warnings, Ruff/diff/strict JSON/digest/security/preservation PASS; zero M47 EO/pixels/science.
- **Limitation:** AS201 not implemented; AS202 numerics/coefficient/grid/downstream thresholds not frozen.
- **Lesson learned:** Freeze source and representation before anomaly strength can influence selection.
- **Impact on next step:** Owner review then separate PR/merge and AS201 implementation authorization; not executed by this entry.
- **Presentation takeaway:** Before looking for dark pixels, freeze the same-track sequence and raw-data contract.
- **Recommended visual:** Three-role timeline plus envelope/support diagram; proposed, no screenshot/figure claimed to exist.
- **Candidate slide title:** “Before looking for dark pixels.”

### M48 — Review and complete raw Sentinel-1 source engineering — 11 October 2026

- **Date:** 11 October 2026 (Asia/Dubai); implementation, not a new scientific decision.
- **Task / ID:** AS-201 M48 / E48 / EV-052 under merged Decision 054.
- **Problem:** existing twelve-path WIP lacked coverage, group/set provenance and
  robust native header/XML checks; its existence did not constitute acceptance.
- **Why it mattered:** unknown support and provider packaging defects must not
  become false scientific evidence downstream.
- **Options:** rewrite WIP, accept it as-is, or preserve/review/complete it. Owner
  authorized the third; d6f89ce remains intact.
- **Decision:** implement frozen raw-GRD handoff only; no Decision 055 or SAR science.
- **Rationale:** strict source engineering precedes numerical interpretation.
- **Implementation:** exact six slots, defensive XML, chained TIFF directories,
  footprint support/gaps, immutable hashes and source/derived registry lineage.
- **Evidence:** EV-052 MD/JSON; offline catalog/header/XML/provenance/security tests.
- **Quantitative result:** all six synthetic slots retain identity and order; real
  provider requests, SAR pixel reads/bytes and scientific compute are all zero.
  Actual test totals are recorded in EV-052, separately from historical M47 gates.
- **Limitation:** no M48 live six-source acceptance or oil result; metadata footprint
  overlap is not valid-pixel support. M46 representative access remains historical.
- **Lesson:** a COG packaging label cannot establish radiometric representation;
  metadata roles and native identity must be checked explicitly.
- **Next step:** owner code review → separate PR/merge authorization; AS-202 needs
  its own design authorization.
- **Presentation takeaway:** provenance and honest missingness before dark pixels.
- **Recommended visual:** source → header/XML → three metadata support groups →
  derived retrieval lineage; proposed only, no screenshot created.
- **Candidate slide title:** “Know the source before interpreting the signal.”

### M49 — A stopped live gate is not a scientific pass — 11 October 2026

- **Task / ID:** AS-201 M49 / E49 / EV-053, new live acceptance after merged M48.
- **Problem / question:** Do the offline-validated contracts succeed against today's six real sources?
- **Why it mattered:** Synthetic success cannot replace live source availability proof.
- **Options considered:** Run the unchanged public path; silently patch/substitute; or retain failures.
- **Decision:** Execute once, stop on failure, retain exact observed evidence; no new policy decision.
- **Rationale:** Source freeze and honest missingness precede any SAR science.
- **Implementation / experiment:** External transport observers; merged `search_sentinel1` aborted with `CatalogMetadataError`; access validator not reached.
- **Evidence:** [EV-053 MD](evidence/AS_201_LIVE_ACCEPTANCE.md) and [JSON](evidence/AS_201_LIVE_ACCEPTANCE.json), status/path/body hashes.
- **Quantitative result:** 2 CDSE requests / 15,659 response-body bytes; zero PC/signing/TIFF/XML/image blocks/pixels/scientific SAR calls; 1432 engineering tests PASS.
- **Limitation:** Six sources not validated; observer did not retain raw bodies/exception text, so exact offending field and cause remain unlocalized.
- **Lesson learned:** Retain sanitized structured diagnostics without confusing HTTP200, offline tests or an initial coarse error label with live readiness.
- **Impact on next step:** Owner review and separately authorized failure localization; no AS-202.
- **Presentation takeaway:** A failed gate protects against treating incomplete source access as scientific evidence.
- **Recommended visual:** Stopped discovery → six untested slots diagram, proposed only; no screenshot created.
- **Candidate slide title:** “Live readiness must be earned.”

### M50 — Keep scientific policy frozen; adapt the client boundary — 11 October 2026

- **Task / ID:** AS-201 M50 / E50 / EV-054, offline interoperability correction.
- **Problem / question:** Can an immutable envelope safely cross a client that deep-copies dicts?
- **Why it mattered:** M49 failed before search traffic; live readiness remained unproved.
- **Options considered:** Weaken FrozenJSON; change shared STAC/dependencies; or convert only at the SAR boundary.
- **Decision / rationale:** Local JSON conversion preserves scientific immutability and isolates library compatibility; no new scientific decision.
- **Implementation / experiment:** Resolver-only conversion; real pystac-client constructor and pagination exercised with synthetic HTTP responses.
- **Evidence:** [EV-054 MD](evidence/AS_201_STAC_GEOMETRY_BOUNDARY_FIX.md) and [JSON](evidence/AS_201_STAC_GEOMETRY_BOUNDARY_FIX.json).
- **Quantitative result:** 2 new regressions; 136 focused / 1434 full tests PASS, 6 historical warnings; 3 pages/provider; provider/pixel/science access zero.
- **Limitation:** Offline success does not prove current six-source access; M49 FAIL unchanged, live retry not run.
- **Lesson learned:** An immutable domain model may need an explicit mutable-library boundary representation.
- **Impact on next step:** Review the fix before separately authorized publication and live retry.
- **Presentation takeaway:** Preserve a failed gate and correct its cause without changing the scientific contract.
- **Recommended visual:** Conceptual frozen-policy → plain JSON → client diagram; no screenshot created.
- **Candidate slide title:** “Fix the boundary, preserve the evidence.”

### M51 — A corrected boundary is not a completed live gate — 11 October 2026

- **Task / ID:** AS-201 M51 / E51 / EV-055; one controlled public-path live retry.
- **Problem / question:** Does merged M50 permit all six real sources to pass retrieval acceptance?
- **Why it mattered:** Offline interoperability does not establish source/asset readiness.
- **Options considered:** Preserve exact policy and outcome; patch while probing; or substitute sources.
- **Decision / rationale:** One unchanged run, no repair/restart; retain all unavailable slots and exact stage diagnosis.
- **Implementation / experiment:** Public search and access validator, delegated stage/request instrumentation; both catalogs paginated completely.
- **Evidence:** [EV-055 MD](evidence/AS_201_LIVE_ACCEPTANCE_RETRY.md) and [JSON](evidence/AS_201_LIVE_ACCEPTANCE_RETRY.json).
- **Quantitative result:** 8 HTTP200 requests / 671,449 body bytes; 3 CDSE + 1 PC pages; 6/6 slots discovery-identity invalid; zero assets/pixels/science.
- **Limitation:** CDSE product:type IW_GRDH_1S rejected by GRD/GRDH literal check; header/XML/PC identity not accepted; retrieval not ready.
- **Lesson learned:** Crossing one library boundary does not prove provider metadata normalization or live access.
- **Impact on next step:** Separate owner review and authorization for the localized SAR-only metadata correction.
- **Presentation takeaway:** Preserve each failed gate rather than claiming readiness from catalog success.
- **Recommended visual:** Catalog success → six identity rejections → zero asset access; proposed, no screenshot created.
- **Candidate slide title:** “Catalog access is not source acceptance.”

### M52 — Exact provider semantics without relaxed source identity — 11 October 2026 (Asia/Dubai)

- **Task / ID:** AS-201 M52 / E52 / EV-056; offline product-type interoperability correction.
- **Problem / question:** M51 rejected all six exact CDSE sources because product:type IW_GRDH_1S was not in the GRD/GRDH literal set.
- **Why it mattered:** An authentic provider representation must cross the metadata boundary before live access can be evaluated.
- **Options considered:** Exact documented alias; broad substring acceptance; changing providers or sources.
- **Decision / rationale:** Add only IW_GRDH_1S, retaining field precedence and every frozen invariant; no scientific-policy change.
- **Implementation / experiment:** One SAR resolver membership correction; 41 new offline regression cases; no provider request or live retry.
- **Evidence:** [EV-056 MD](evidence/AS_201_CDSE_PRODUCT_TYPE_FIX.md) and [JSON](evidence/AS_201_CDSE_PRODUCT_TYPE_FIX.json).
- **Quantitative result:** Six exact synthetic CDSE normalizations pass; six-source normalized identities stay identical to GRD fixture; zero pixels/science.
- **Limitation:** Offline normalization does not establish six-source header/XML readiness; M51 remains historical FAIL.
- **Lesson learned:** Normalize exact provider semantics at the narrow boundary while rejecting incompatible metadata.
- **Impact on next step:** Owner review; separate fix publication/merge and controlled live acceptance authorization.
- **Presentation takeaway:** A minimal tested compatibility correction preserves scientific restraint and failed-gate history.
- **Recommended visual:** M51 literal mismatch → exact alias + conflict guards → offline pass → live gate still pending; proposed, no screenshot created.
- **Candidate slide title:** “Provider compatibility without weakened evidence.”

### M53 — Access success still requires metadata identity — 11 October 2026 (Asia/Dubai)

- **Task / ID:** AS-201 M53 / E53 / EV-057; one controlled post-M52 public live gate.
- **Problem / question:** Does the merged exact product-type correction permit complete six-source access validation?
- **Why it mattered:** Catalog and offline identity acceptance are necessary but insufficient for a trustworthy raw-source handoff.
- **Options considered:** Preserve one exact run; patch/restart; substitute a source or relax metadata.
- **Decision / rationale:** Original public workflow once, all six slots retained, no fix or manual retry.
- **Implementation / experiment:** Complete catalog pagination, six exact source matches, VV structural ranges and existing four XMLs per slice.
- **Evidence:** [EV-057 MD](evidence/AS_201_LIVE_ACCEPTANCE_AFTER_M52.md) and [JSON](evidence/AS_201_LIVE_ACCEPTANCE_AFTER_M52.json).
- **Quantitative result:** 195 requests / 20,261,621 body bytes; 6/6 VV headers PASS; 6/6 manifest-time rejections; 30 sign operations / 1 transient token; zero pixels/science.
- **Limitation:** Provider manifest/startTime lacks an explicit timezone required by the existing parser; later XML identity/LUT checks not reached; ready=false.
- **Lesson learned:** A readable file and valid TIFF structure do not establish validated metadata identity.
- **Impact on next step:** Owner review; any subsequent investigation/correction/live retry requires separate authorization.
- **Presentation takeaway:** Show engineering progress while retaining the actual failed gate rather than claiming oil-pipeline readiness.
- **Recommended visual:** Catalog/identity PASS → VV headers PASS → manifest time FAIL → explicit unavailable handoff; proposed only, no screenshot created.
- **Candidate slide title:** “Readable is not yet validated.”

### M54 — Normalize serialization without weakening identity — 11 October 2026 (Asia/Dubai)

- **Task / ID:** AS-201 M54 / E54 / EV-058; offline manifest UTC-time interoperability correction.
- **Problem / question:** All six M53 sources expose naive acquisition times that the generic parser rejects before later XML validation.
- **Why it mattered:** The exact UTC acquisition identity must survive provider serialization differences without relaxing source matching.
- **Options considered:** Manifest-only UTC interpretation; loosen generic parsing; tolerate interval mismatch; retry live immediately.
- **Decision / rationale:** Owner-authorized manifest-only boundary; exact interval equality and generic strictness retained.
- **Implementation / experiment:** Two manifest call sites use a dedicated parser; existing six-source synthetic fixtures and fail-closed controls exercise the complete XML validator.
- **Evidence:** [EV-058 MD](evidence/AS_201_MANIFEST_UTC_TIME_FIX.md) / [JSON](evidence/AS_201_MANIFEST_UTC_TIME_FIX.json).
- **Quantitative result:** 73 new cases; 250 focused / 1548 full tests PASS; six historical Rasterio warnings; provider requests/pixels/scientific compute zero.
- **Limitation:** Offline serialization acceptance does not prove later live XML identity/LUT success; M53 remains FAIL and live readiness is UNPROVED.
- **Lesson learned:** Normalize provider serialization at its smallest boundary while keeping exact identity checks intact.
- **Impact on next step:** Owner review; any publication/merge or live retry requires separate authorization. AS-202 remains NOT STARTED.
- **Presentation takeaway:** Keep the failed live gate visible and show the narrow, independently tested correction.
- **Recommended visual:** Naive manifest time → scoped UTC interpretation → exact microsecond equality → unchanged later guards; proposed only, no new visual exists.
- **Candidate slide title:** “Fix the boundary, preserve the contract.”

### M55 — A passed time boundary exposes the next identity gate — 11 October 2026 (Asia/Dubai)

- **Task / ID:** AS-201 M55 / E55 / EV-059; controlled post-M54 live engineering gate.
- **Problem / question:** Does manifest-only UTC normalization allow the complete frozen six-source access contract to pass?
- **Why it mattered:** Offline correction must be distinguished from actual provider metadata readiness.
- **Options considered:** One unchanged public run; patch/restart; substitute another slice; preserve exact unavailable states.
- **Decision / rationale:** Owner-authorized single run; retain all six sources and the actual failing boundary without repair.
- **Implementation / experiment:** Complete catalogs/identities, original VV structural ranges and four XMLs/slice; passive same-run trace only.
- **Evidence:** [EV-059 MD](evidence/AS_201_LIVE_ACCEPTANCE_AFTER_M54.md) / [JSON](evidence/AS_201_LIVE_ACCEPTANCE_AFTER_M54.json).
- **Quantitative result:** 195 requests / 20,261,623 bytes; 6/6 VV headers and exact manifest intervals pass; 6/6 familyName checks fail; 250 focused / 1548 full tests PASS; zero pixels/science.
- **Limitation:** Entire manifest remains FAIL; later native-measurement/XML/LUT/geolocation/thermal gates NOT_REACHED; live readiness UNPROVED.
- **Lesson learned:** Preserve each gate's evidence; passing one representation boundary may expose a separate identity requirement.
- **Impact on next step:** Owner review; no fix/retry or AS-202 inside M55. Further action requires separate authorization.
- **Presentation takeaway:** Honest unavailable handoffs preserve progress without claiming scientific readiness.
- **Recommended visual:** Catalog/identity/header PASS → exact manifest time PASS → familyName FAIL → later checks NOT_REACHED; proposed only, no new visual exists.
- **Candidate slide title:** “Progress is not yet readiness.”

### M56 — Platform identity is not instrument identity — 11 October 2026 (Asia/Dubai)

- **Task / ID:** AS-201 M56 / E56 / EV-060; manifest-only representation diagnostic.
- **Problem / question:** Why does recursive platform familyName lookup reject all six manifests?
- **Why it mattered:** The live failure needs exact field-level evidence before any correction.
- **Options considered:** Repeat full acceptance; inspect six preserved manifest references only; patch the parser before observing the structure.
- **Decision / rationale:** Owner-authorized manifest-only diagnostic; preserve M55 FAIL and avoid all other assets.
- **Implementation / experiment:** Existing transient signer, bounded XML fetch/parser; unmodified recursive helper reproduction and direct-child hypotheses.
- **Evidence:** [EV-060 MD](evidence/AS_201_MANIFEST_PLATFORM_DIAGNOSTIC.md) / [JSON](evidence/AS_201_MANIFEST_PLATFORM_DIAGNOSTIC.json).
- **Quantitative result:** 6/6 identical platform structures; two distinct family texts each; 6 GETs / 151,650 manifest bytes, six body hashes matching M55; zero pixels/science.
- **Limitation:** Direct family is uppercase SENTINEL-1; scoping alone does not satisfy the later exact literal. Later validators/readiness remain unproved.
- **Lesson learned:** XML local names can recur at different identity levels; preserve structural scope and distinguish representation from semantics.
- **Impact on next step:** Owner review; separate correction/test/retry authorization required. No source edit, M55 rerun or AS-202.
- **Presentation takeaway:** Diagnose the exact mismatch before changing a frozen contract.
- **Recommended visual:** platform → familyName SENTINEL-1 vs instrument → familyName Synthetic Aperture Radar; proposed only, no screenshot/figure created.
- **Candidate slide title:** “Platform identity is not instrument identity.”

### M57 — Separate platform identity from instrument identity — 11 October 2026 (Asia/Dubai)

- **Task / ID:** AS-201 M57 / E57 / EV-061; minimal offline scope/casing correction.
- **Problem / question:** M56 proved recursive familyName lookup mixes platform and nested instrument identities, followed by a separate case-literal mismatch.
- **Why it mattered:** Metadata interoperability must not weaken exact frozen source matching or later scientific-metadata guards.
- **Options considered:** Manifest-only direct-child/case boundary; change shared recursive helpers; introduce mission aliases; immediately retry live.
- **Decision / rationale:** Owner-authorized direct-child cardinality plus case-only identity; all other boundaries preserved.
- **Implementation / experiment:** One manifest block changed; exact six-source synthetic fixtures, nested-family isolation and fail-closed regressions through complete metadata validation.
- **Evidence:** [EV-061 MD](evidence/AS_201_MANIFEST_PLATFORM_FIX.md) / [JSON](evidence/AS_201_MANIFEST_PLATFORM_FIX.json).
- **Quantitative result:** 69 added cases; 330 focused / 1617 full tests PASS, six existing Rasterio warnings; provider requests/pixels/SAR science zero.
- **Limitation:** Complete offline metadata success does not establish later live XML readiness; M55 remains FAIL and M56 historical diagnostic remains intact.
- **Lesson learned:** Fix the smallest proven representation boundary and retain fail-closed cardinality and mission identity.
- **Impact on next step:** Owner review; publication/merge/live retry each require separate authorization. AS-202 remains NOT STARTED.
- **Presentation takeaway:** A measured, narrow correction preserves the original scientific contract.
- **Recommended visual:** Direct platform family identity separated from nested instrument family; proposed only, no new visual exists.
- **Candidate slide title:** “Correct the representation, preserve the guards.”

### M58 — Live manifest success exposes the next strict metadata boundary — 11 October 2026 (Asia/Dubai)

- Goal: one unchanged six-source live acceptance after M57, no patch or science.
- Result: **LIVE FAIL**. Catalogs/identities/assets/VV headers and all complete
  manifests PASS; calibration-vector azimuthTime is rejected as timezone-naive.
  Six UNAVAILABLE / METADATA_INVALID; final ready=false. Later guards NOT_REACHED.
- 195 requests / 20,261,623 bytes; 30 signs / 1 token; zero pixels/SAR science.
  330 focused / 1617 full tests PASS, six existing Rasterio warnings; quality/
  preservation PASS. Evidence: EV-062 MD/JSON, full trace and exact identities.
- Presentation: “Each real gate is reported honestly; an offline fix is not live
  readiness.” No backscatter/oil/AS-202 claim; no new visual or screenshot claimed.
- Next: owner review only. M55 FAIL/M56 diagnostic/M57 offline PASS retained.

### M59 — Establish timestamp facts before changing their meaning — 11 October 2026 (Asia/Dubai)

- Goal: diagnose only consumed SAFE product/calibration/noise timestamps from
  M58's exact stable references; no production fix or full live acceptance.
- 18 single XML GETs, all hashes equal M58. All 360 values share naive ISO /
  six-digit precision / no offset or whitespace; all strict-parser calls reject.
  ADS wall-clock correspondence does not establish UTC semantics.
- 18 signs / 1 token; 19 requests / 19,339,930 bytes; catalogs/TIFF/manifest/
  pixels/science zero. M58 not rerun. 330 focused / 1617 full tests PASS,
  six existing Rasterio warnings; quality/security/digest/preservation PASS.
- Presentation: “Diagnose the representation before assigning timezone meaning.”
  No new screenshot/figure claimed. UTC_SEMANTICS_REQUIRES_OWNER/SPEC REVIEW.
- Next: owner/spec review; M58 FAIL preserved, live readiness UNPROVED.
  Evidence: EV-063 MD/JSON. AS-202 NOT STARTED; Decision 055 ABSENT.

### M60 — Apply specified UTC semantics at the smallest boundary — 11 October 2026 (Asia/Dubai)

- Specification establishes SAFE timeType UTC; M59 establishes the actual naive
  six-digit serialization. The two sources of knowledge are kept distinct.
- One local helper/four calls; generic and manifest time parsing, platform scope
  and all later identity/LUT/geolocation/native/thermal guards preserved.
- All six synthetic sources pass complete metadata validation in four equivalent
  representations. 80 malformed / 18 exact interval / 41 later guard cases reject.
  493 focused / 1780 full tests PASS; six existing Rasterio warnings; all gates PASS.
- Provider/sign/token/TIFF/XML/pixel/science zero. Historical M58 FAIL and M59
  diagnostic remain untouched; live/scientific readiness UNPROVED. No figure claimed.
- Presentation: “Resolve representation from the specification, then prove the
  narrow boundary offline.” Next is owner review; no live-readiness/oil claim.
  Evidence EV-064 MD/JSON. AS-202 NOT STARTED; Decision 055 ABSENT.

### M61 — Prove the complete metadata handoff without reading pixels — 11 October 2026 (Asia/Dubai)

- One controlled unchanged live run after M60: all six frozen sources finish
  AVAILABLE, all three groups and final retrieval ready, provenance validates.
- Complete manifest/LUT/noise/geolocation/spacing/ADS/dimension/thermal guards PASS.
  360 SAFE times pass. All 18 noise-azimuth vectors have matching lengths and all
  four bounds; passive observation reuses original XML with no extra request.
- 195 requests / 20,261,623 bytes / 30 signs / 1 token; VH/ZIP/image-block/pixel/
  SAR science zero. 493 focused / 1780 full PASS; six existing Rasterio warnings;
  quality/digest/security/preservation PASS. No new visual claimed.
- Presentation: “Same source bytes. Specified UTC semantics. Complete metadata
  readiness.” This proves AS-201 access/metadata, not calibrated backscatter or oil.
- M58 historical FAIL / M59 diagnostic / M60 offline PASS remain intact.
  LIVE_READINESS PROVED_AT_AS201_METADATA_ACCESS_BOUNDARY; SAR science UNPROVED.
  Owner review next; AS-202 NOT STARTED; Decision 055 ABSENT. EV-065 MD/JSON.

## 3. Decision timeline

The decision log is authoritative. Decisions 039–045 are explicitly dated 6 October 2026. Except Decision 038's explicit 2 October selection date, earlier per-decision dates are not recorded. Decisions 001–037 were documented with continuity setup on 2 October; do not imply that numerical order supplies precise event times.

| Recorded period | Decisions | Choice / alternative | Rationale and consequence | Evidence / status |
|---|---|---|---|---|
| 2 Oct continuity record | 001–006 | Track 03 and a defined operator; multi-hazard product with HAB first, oil second | Operational decision drives scope, rather than a generic map or detector | Decision log; current product commitments |
| 2 Oct continuity record | 007–010 | S2 optical, S1 SAR; hyperspectral P1, no native-813 requirement | Sensor suitability and a P0 path independent of enhancement availability | Decision log; future hazard capabilities |
| 2 Oct continuity record | 011–015 | Explainable baseline before complex ML; independent hazards; human verification | Weak labels and scientific uncertainty preclude confirmatory or autonomous claims | Decision log; current guardrails |
| 2 Oct continuity record | 016–018 | Historical validation; study AOI distinct from operational intake | External event reports and EO findings must remain separate | Decision log; planned validation |
| 2 Oct engineering / continuity record | 019–024 | Provenance first; Python 3.11; `src/`, TOML, GeoJSON | Traceable outputs and reproducible validated inputs | AS-001/002/003 commits; implemented foundations |
| 2 Oct continuity record | 025–029, 035–037 | Repository continuity, multi-machine workflow, isolated accounts, branches, read-only onboarding | Recoverable state and reviewed authorization before development | AS-000C history; completed setup |
| 2 Oct continuity record | 030–034 | Minimal dependencies; catalog before imagery; preferred future Streamlit; cache fallback; protect P0 | Delivery reliability and evidence precede sophistication | Decision log; UI/cache remain plans |
| Explicitly 2 Oct | 038 | Configurable CDSE catalog; `pystac-client==0.9.0` only new direct dependency | Owner selection and tested real discovery without raster scope | AS-101 report and commits; implemented |
| 3 Oct merge record | No new technical decision | Close AS-101 status after PR #2; preserve AS-102 authorization boundary | Documents must match merged engineering state | `cf1ed23`, PR #3 / `acbe2c1`; completed docs |
| Investigations recorded 6 Oct; original probe timestamps missing | None adopted | CDSE scale/offset/access blocker, PC catalog/advertised COGs, cross-provider product distinction | Metadata and access findings are documented; backend/processing decisions remain pending | M09–M13; [evidence index](evidence/PRESENTATION_EVIDENCE_INDEX.md); no technical decision changed |
| Later experiment FG-01 recorded 6 Oct; original timestamp missing | None adopted | Actual PC bounded access and product-XML decoding | Access prerequisite is READY for tested path; no provider switch, canonical-grid/mask approval, or implementation authorization | M14; [final gate](evidence/AS_102_PLANETARY_COMPUTER_RASTER_GATE.md); existing decisions preserved |
| 6 Oct implementation authorization / timestamped acceptance | 039–045 | CDSE discovery + actual PC pixels; XML; fixed 20 m grid; conservative SCL/support; NumPy/Rasterio; transient SAS and verified AOI cache | Pixel meaning, attribution, spatial alignment and quality are prerequisites for future science | M15; EV-016/EV-017; historical 6 Oct feature-branch acceptance (213 tests); later review/merge in M16 / EV-018 |
| 8 Oct final review / merge | No new technical decision | Targeted security/cache/provenance hardening; merge existing AS-102 contract | Verified publication closes preprocessing while preserving scientific/authorization limits | M16 / EV-018; PR #6, merge `627b6ae`; 265 tests, local Ruff/diff checks; no GitHub CI reported |
| 8 Oct AS-103 authorization/acceptance | 046 | Six candidate features, declared wavelengths, signed numeric guards and fingerprinted immediate-parent lineage; no extra cache/dependency | Per-scene signals precede future temporal science | M17; EV-019/EV-020; uncommitted feature-branch acceptance |
| 8 Oct AS-103 final review / merge | No new technical decision | Final model/arithmetic/numerical/identity/lineage and real-evidence review; publish existing Decision 046 contract | Separate reviewed publication from the earlier experiment without extending scientific scope | M18 / EV-021; PR #8, merge `b770d056`; 348 tests, local Ruff/diff checks; no configured/reported GitHub CI |
| 8 Oct AS-104 authorization | Decision 047 | Strictly-prior median/MAD/midrank; semantic target-support fingerprints; zero-scale masking; no noise floor | Independent support/identity/lineage; no event inference | M19 / EV-022–EV-023 |

| 8 Oct isolated upstream authorization | 048 | Optional explicit PC baseline after validated exact matching; zero/multiple fail; selector is not a cache identity dimension | Homogeneous delivered processing without generation heuristics or changed pixel processing | M20/E20/EV-024; Decision 047 remains in preserved AS-104 worktree |
| 9 Oct isolated upstream transport authorization | 049 | Reusable anonymous account/container SAS, memory-only expiry-aware cache and bounded token-only retries; retain public API | Fewer authentication calls without dependency/key/identity changes | M22/E22/EV-026; 531 tests and fresh one-request/eleven-signs smoke; uncommitted for review |
| 9 Oct AS-104 merge / closeout | No new decision | PR #12 merges the existing temporal contract and accepted evidence; close current status while retaining M23–M26 | Acceptance, publication and merge remain separate; no Decision 050 or future-stage authorization | M27/E27/EV-031; merge `472edc7` |
| 9 Oct AS-105 offline authorization | 050 | Frozen rank/direction family-aware P0 candidate geometry; explicit support denominator, exact pixel polygons and parent lineage | Explainable heuristic before separately authorized real acceptance/policy comparison | M28/E28/EV-032; synthetic-only PASS, uncommitted |
| 10 Oct owner-approved design freeze | 051 | Consecutive-valid exact-pixel recurrence; invalid UNKNOWN, noncandidate breaks; no gap cutoff | Preserve AS-105 integrity validation, immediate geometry lineage, explicit history denominators and predeclared fixed-March April selection | [Frozen AS-106 design](AS_106_PERSISTENCE.md); DESIGN ONLY, implementation and M31–M35 NOT STARTED |
| 10 Oct owner-approved design freeze | 052 | Availability-aware provisional HAB-like screening; evidence completeness separate from score/band | Missing is unavailable, correlated evidence disclosed; freeze before any real score | M37/E37/EV-041; FINAL / FROZEN DESIGN, NOT IMPLEMENTED |
| 10 Oct AS-108 M42 | Decision 053 | Freeze one-event observational consistency, externally verified EAD month/area facts supplied by the owner, descriptive PRE, retained EVENT and earliest metadata-selected POST | No biological accuracy/exact lead time or new science; protect minimum P0 and oil/demo deadline | M42/E42/EV-046 |

Remaining pending decisions include other task-required geospatial frameworks (NumPy/Rasterio now adopted), final operational demo site, usable hyperspectral event/site, and fitted ML selection. The PRD's broad stack is a suggested future stack, not the installed dependency inventory.


### M47 decision timeline addition

| Date | Decision | Contract | Boundary | Evidence |
|---|---|---|---|---|
| 11 Oct AS-201 M47 | Decision 054 | Freeze exact raw-GRD sources, broad envelope/gaps and secure typed handoff before SAR science | AS-202 algorithm and downstream thresholds remain unfrozen | M47/E47/EV-051 |

## 4. Engineering evidence index

| ID | Evidence location | What it supports | What it does not support |
|---|---|---|---|
| E01 | [pyproject.toml](../pyproject.toml), [README](../README.md), `f878acc` | Python range `>=3.11,<3.12`, package/test/lint foundation | Fully locked environment or an implemented application UI |
| E02 | [config](../src/aquasentinel/config/), [runtime](../src/aquasentinel/runtime.py), [tests](../tests/config/), `f606ac5` / `113ca44` | Validated config/AOI and runtime inputs | A real intake geometry or validated risk weights |
| E03 | [provenance](../src/aquasentinel/provenance/), [tests](../tests/provenance/), `e2baedc` / `db79260` | Schema 1.0, validation, serialization, registry, lineage persistence | Real derived hazard/risk/alert products |
| E04 | [AGENTS](../AGENTS.md), state/handoff/decisions, [plans](../.agent/PLANS.md), AS-000C commits | Recoverable project context and recorded onboarding completion | A tracked copy of the original full audit report |
| E05 | [catalog/stac.py](../src/aquasentinel/catalog/stac.py), [catalog tests](../tests/catalog/test_stac.py) | Real client logic with offline HTTP fixtures; complete pagination and explicit errors | A raster data-access implementation |
| E06 | [ingestion/sentinel2.py](../src/aquasentinel/ingestion/sentinel2.py), [tests](../tests/ingestion/test_sentinel2.py) | Candidate normalization, sorting, duplicates, filters, source mapping | Pixel scale/offset, native grid, mask policy |
| E07 | [AS-101 report](AS_101_STAC_SEARCH.md), Decision 038 | Dated live CDSE query and reproduction instructions | Permanent catalog count or asset-read success |
| E08 | [loader](../src/aquasentinel/config/loader.py), [test_catalog.py](../tests/config/test_catalog.py), `f57f6bf` | Strict TOML cloud typing before network requests | A general refactor of all config coercions |
| E09 | AS-101 report; history `b3f0e9f` → `35caa90` → `cf1ed23` | Historical AS-101 92 and reviewed 97 passing-test baselines; preserved 17 original tests | Detection accuracy, coverage percentage, or service SLA |
| E10 | PR #2 / `1b83a73`; PR #3 / `acbe2c1` | Implementation merge and post-merge closeout on main | AS-102 authorization or completion |
| E11 | [.gitignore](../.gitignore), config cache path, Decision 033 | Large EO/cache/secret exclusions and demo-fallback requirement | A completed cached raster demo |
| E12 | [CDSE report](evidence/AS_102_CDSE_ACCESS_PROBE.md), [PC report](evidence/AS_102_PLANETARY_COMPUTER_PROBE.md), [EV-009–EV-014](evidence/PRESENTATION_EVIDENCE_INDEX.md) | Owner-supplied record of metadata/blocked access/catalog success and product-identity comparison | Successful raster reads/signing/decoding at the documented pre-read checkpoint; later final-gate result |
| E13 | [Final PC gate](evidence/AS_102_PLANETARY_COMPUTER_RASTER_GATE.md), EV-014 later stage / EV-015 | Reported 4 credential-free signings, 3 GDAL bounded reads, XML and B02/B05 decoding; 8/8 gates passed | All-band preprocessing, measured transfer efficiency, aquatic suitability, HAB results, or CDSE pixel equivalence |
| E14 | [AS-102 implementation/validation](evidence/AS_102_OPTICAL_PREPROCESSING_VALIDATION.md), [plan](AS_102_OPTICAL_PREPROCESSING.md), new source/tests | Nine-band real AOI alignment, XML/masks, actual-PC provenance, 213-test baseline and verified offline cache | Aquatic radiometric validation, HAB/operational performance or merged release |
| E15 | PR #6; feature `fe3d270`; merge `627b6ae`; M16 / EV-018 | Final reviewed AS-102 publication; 265 tests, Ruff/diff checks and targeted security/cache/provenance review | GitHub CI pass, HAB/scientific/operational performance |
| E16 | [AS-103 contract](AS_103_SPECTRAL_FEATURES.md), [validation](evidence/AS_103_SPECTRAL_FEATURES_VALIDATION.md), feature source/tests; M17 / EV-019–EV-020 | Six deterministic candidate features, guarded support, fingerprinted identity, immediate-parent lineage and 348-test branch baseline | Merged release, temporal anomalies, HAB/scientific/operational validation |
| E17 | Implementation `5638bc8`; [PR #8](https://github.com/Omar-Aboulwafa/aquasentinel-813/pull/8); merge `b770d056`; M18 / EV-021 | Final reviewed/merged AS-103 engineering, deterministic per-scene features and reproducible identity/immediate-parent lineage; 348 tests, Ruff/diff checks | GitHub CI success, temporal anomaly, HAB/chlorophyll/species/toxins, water safety, exposure/risk/lead-time or scientific accuracy |
| E18 | AS-104 modules/tests; Decision 047; EV-022 | Offline causal math, semantic identity, exact multi-parent lineage; 460 tests/Ruff/diff | Real multi-scene or biological/operational validation |
| E19 | EV-023 real attempt, March 4 metadata diagnosis | Two exact processing-product matches; unchanged AS-102 correctly stops ambiguity | Usable history, real temporal maps/ID, HAB/risk/lead-time |
| E20 | [Required-PC-baseline plan](AS_102_REQUIRED_PC_BASELINE_FIX.md), [validation](evidence/AS_102_REQUIRED_PC_BASELINE_FIX_VALIDATION.md); M20/EV-024 | Strict optional selector, constrained cache returns, unchanged actual-product identity, 421 tests, 6/6 real metadata resolutions and zero forbidden calls | Merged fix, March asset/decoding/support success, AS-104 acceptance, scientific hazard or operational accuracy |
| E21 | PR #10 / `39f2aee`; retained stash/hash backups; [resumed AS-104 evidence](evidence/AS_104_TEMPORAL_BASELINE_VALIDATION.md); M21/EV-025 | Verified preserved integration, combined 533-test gate and timestamped real signing failures under unchanged 05.09 contract | Real temporal product/support/scalar/causality/repeat acceptance, HAB/accuracy/operational claims |
| E22 | [Reusable-token plan](AS_102_REUSABLE_PC_SAS_TOKEN_FIX.md), [transport validation](evidence/AS_102_REUSABLE_PC_SAS_TOKEN_FIX_VALIDATION.md); M22/EV-026 | 531 tests, one anonymous token HTTP request/eleven signs, bounded XML/TIFF reads and zero additional reuse requests; unchanged cache/files/identity | Full processing, AS-104 acceptance, five usable histories, scientific/operational accuracy, perpetual availability or GitHub CI success |
| E23 | [AS-104 validation §5](evidence/AS_104_TEMPORAL_BASELINE_VALIDATION.md#5-pr-11-integration-and-five-reference-0509-attempt--9-october-2026); M23/EV-027; PR #11/2006df7 | Preserved integration; 643 offline tests; five real AS-102/103 references; same grid/05.09; target platform-casing provenance blocker; safe IDs/support/feature summaries | Real temporal output/history/scalar/causal/repeat acceptance, HAB/scientific/operational accuracy or GitHub CI success |
| E24 | [Platform fix validation §6](evidence/AS_104_TEMPORAL_BASELINE_VALIDATION.md#6-targeted-platform-case-representation-fix--9-october-2026); M24/EV-028 | Case-only consistency predicate; 20 regressions; 132 temporal/663 full tests; unchanged stored identity/math | Alias normalization, rewritten products, new scientific decision or merged release |
| E25 | [Cached real validation §7](evidence/AS_104_TEMPORAL_BASELINE_VALIDATION.md#7-cached-five-reference-0509-real-acceptance-rerun--9-october-2026); M25/EV-029 | Six verified real caches/AS-103 IDs; sparse five-history support; 18 scalar checks; synthetic causal exclusion/repeat; no network | Detection accuracy, statistical sufficiency, real future availability, hazard/operational claims or GitHub CI success |
| E26 | Feature `09b38bd`; parent `2006df7`; [publication §8](evidence/AS_104_TEMPORAL_BASELINE_VALIDATION.md#8-as-104-feature-publication--9-october-2026); M26/EV-030 | Exactly 15 reviewed paths committed/pushed, 663-test pre-commit gate, clean worktree and remote SHA equality; preserves M23–M25 | Merge, PR creation, new scientific experiment, detection accuracy or GitHub CI success |
| E27 | [PR #12](https://github.com/Omar-Aboulwafa/aquasentinel-813/pull/12); merge `472edc7`; [closeout §9](evidence/AS_104_TEMPORAL_BASELINE_VALIDATION.md#9-pr-12-merge-and-as-104-closeout--9-october-2026); M27/EV-031 | AS-104 complete/merged; two commits/fifteen paths, 663-test reviewed baseline; source/test and accepted-evidence preservation, explicit next-stage authorization | New EO experiment, biological/operational validation, statistical sufficiency or GitHub CI success |
| E28 | [AS-105 contract](AS_105_HAB_ANOMALY_GEOMETRY.md), [offline validation](evidence/AS_105_HAB_ANOMALY_GEOMETRY_VALIDATION.md); M28/EV-032; Decision 050 | Frozen family policy, exact support/components/polygons/area, consumed-bit identity, immediate lineage; 140 geometry/803 total tests and controls A–E PASS | Real geometry metrics, HAB accuracy/biological causation, probability/confidence/risk, persistence, alerts, lead time or GitHub CI success |
| E29 | [M29 real acceptance](evidence/AS_105_HAB_ANOMALY_GEOMETRY_VALIDATION.md#m29--real-geometry-engineering-acceptance--10-october-2026); M29/EV-033; external checksummed bundle, NOT tracked | Frozen real-parent masks/components/areas/polygons, 27/27 repeat, 61/61 parent immutability, 140 focused/803 full tests and zero real network/upstream/cache-load attempts PASS | HAB/event/accuracy/causation/probability/confidence/risk/persistence/alert/lead-time validation; policy comparison, merge or GitHub CI success |
| E30 | PR #14; M30/EV-034; [merge closeout](evidence/AS_105_HAB_ANOMALY_GEOMETRY_VALIDATION.md#m30--pr-14-merge-and-as-105-closeout--10-october-2026) | AS-105 implementation and accepted real engineering evidence merged at `24a260cff130238c731f7cb62fc47eb74230b4dc`; original source/tests, external artifacts and historical records preserved | New scientific validation, optimized policy, HAB detection, CI success or next-milestone authorization |
| E31 | [M31 offline validation](evidence/AS_106_PERSISTENCE_VALIDATION.md); Decision 051; M31/EV-035 | Pure exact-pixel consecutive-valid recurrence; typed timing/denominators/regions, parent-aware integrity and AS-105-only lineage; 190 focused/993 full tests PASS | Real recurrence/April acceptance, biological continuity/HAB, accuracy, risk/confidence, CI success or M32–M35 authorization |
| E32 | [M32 metadata evidence](evidence/AS_106_APRIL_METADATA_INVENTORY.md); [normalized inventory](evidence/AS_106_APRIL_METADATA_INVENTORY.json); Decision 051; M32/EV-036 | Metadata-first April 3/28 sequence frozen before anomaly inspection; 12 CDSE records, 2 eligible PC 05.09 products, zero imagery; April 3 upstream stages missing | Raster/pixel usability, real recurrence, biological persistence/HAB, risk/confidence, CI or M33–M35 authorization |
| E33 | [M33 upstream record](evidence/AS_106_APRIL3_UPSTREAM_PREPARATION.md); [JSON](evidence/AS_106_APRIL3_UPSTREAM_PREPARATION.json); M33/EV-037 | Exact April 3 AS-102→103→104→105; typed offline handoff and common contract PASS; 408 focused/993 full tests | Frozen sequence preserved; M34 inputs ready, recurrence NOT RUN; no scientific/architectural Decision |
| E34 | [M34 real acceptance](evidence/AS_106_REAL_ACCEPTANCE.md); [JSON](evidence/AS_106_REAL_ACCEPTANCE.json); M34/EV-038 | Real as106-v1 P802/Q793/A7/B7/C0; 9/9 array/time/region oracles, repeat/tamper/offline bundle PASS; 190 focused/993 full tests | Observational engineering acceptance, not biological validation; zero retained without tuning; M35 NOT STARTED |
| E35 | [M35 closeout](evidence/AS_106_CLOSEOUT.md); [JSON](evidence/AS_106_CLOSEOUT.json); M35/EV-039; PR #16–#20 chain | Accepted AS-106 result consolidated; publication/closeout prepared, official closure effective on merge | No new science/Decision; zero retained, engineering versus biological claims separated; AS-107 separately authorized |
| E36 | [Prior M36 audit](evidence/AS_107_DESIGN_FREEZE.md#m36--e36--ev-040--prior-read-only-audit-complete); M36/EV-040 | Typed AS-105/106 feasibility and missing-component alternatives reviewed; owner-approved revisions followed in M37 | Prior read-only audit recorded retrospectively, no real score/implementation |
| E37 | [M37 freeze](evidence/AS_107_DESIGN_FREEZE.md); [Decision 052](DECISIONS.md#decision-052--as-107-explainable-availability-aware-hab-risk-and-evidence-completeness); EV-041 | Owner-approved scoring/completeness/qualification/lineage/test contract frozen before real scoring | Design only; M38–M40/AS-108 NOT STARTED; no scientific result or calibrated confidence |
| E38 | [M38 evidence](evidence/AS_107_IMPLEMENTATION_VALIDATION.md); EV-042 | Frozen as107-v1 implementation; 292 focused/1285 full tests; exact scalar/identity/lineage/tamper/side-effect controls PASS | Synthetic engineering only; no real score or M39/M40/AS-108; Decision 052 unchanged |
| E39 | [M39 real acceptance](evidence/AS_107_REAL_ACCEPTANCE.md); [JSON](evidence/AS_107_REAL_ACCEPTANCE.json); EV-043 | First real frozen-policy score 29.52380952380953 / Watch; completeness/coverage .7/.7; independent arithmetic/hash/repeat/tamper/fresh sealed roundtrip PASS | Provisional screening, not biology; context/exposure unavailable; M40/AS108 not started |
| E40 | [M40 closeout](evidence/AS_107_CLOSEOUT.md); [JSON](evidence/AS_107_CLOSEOUT.json); EV-044 | Verified PR #22–#24 merge chain, unchanged accepted Watch .7/.7 result and protected hashes/modes; durable closeout effective on future merge; 1285 full tests PASS (104.18s), six existing Rasterio PendingDeprecationWarnings; Ruff/diff/new-file whitespace/credential/preservation PASS | Documentation/engineering only, no new biology or scoring; AS-107 CLOSEOUT READY before closeout merge; AS-108 NOT STARTED |
| E41 | Historical read-only M41 audit, recorded during M42; EV-045 | Existing metadata/product feasibility; source access blocked, missing POST and causal PRE limitations surfaced | No repository edits in M41, no independently retrieved EAD passage, no EO/scientific execution |
| E42 | [Decision 053](DECISIONS.md#decision-053--as-108-historical-validation-contract); [M42 freeze](evidence/AS_108_DESIGN_FREEZE.md); EV-046 | Externally verified documentary facts supplied by the owner and deterministic phase/eligibility/denominator/claim contract; 1285 full tests PASS (115.87s), six existing Rasterio PendingDeprecationWarnings; Ruff PASS; diff/new-file whitespace PASS | Frozen design only, no case classification/science or PR/merge; AS-201 NOT STARTED |
| E44 | [M44 case](evidence/AS_108_HISTORICAL_CASE_STUDY.md); [JSON](evidence/AS_108_HISTORICAL_CASE_STUDY.json); EV-048 | Accepted-only reconstruction; both EVENT positive; missing POST retained; frozen category PARTIALLY_CONSISTENT; deterministic case digest | Reporting integrity, not new science, predictive accuracy or biological validation; AS-201 NOT STARTED |
| E43 | [M43 metadata selection](evidence/AS_108_POST_METADATA_SELECTION.md); [JSON](evidence/AS_108_POST_METADATA_SELECTION.json); EV-047 | Complete 26-record/6-page CDSE inventory; four eligible dates; earliest May3, exact PC query0; UNAVAILABLE; digest frozen; 1285 full tests PASS (106.24s), six existing Rasterio PendingDeprecationWarnings; Ruff PASS; diff/new-file whitespace PASS | No pixels/scoring/category or fallback; later PC compatibility unassessed; M44/AS-201 NOT STARTED |

Integration note (9 October 2026): E18–E19 and E20 are now reunited in chronological order. Their original bodies and historical statuses remain unchanged; E01–E17 remain preserved.

Reproduce the engineering quality gate with `git diff --check`, `python -m pytest -v`, and `python -m ruff check .` in the Python 3.11 environment. Record fresh results separately from historical results. Do not rerun a live probe and silently rewrite the original 44-scene observation.

Journal-task validation on 6 October 2026: the existing `.venv` used Python 3.11.16; `python -m pytest -v` reported **97 passed in 0.20s**, and `python -m ruff check .` reported **All checks passed!** No live catalog or raster experiment was rerun. Whitespace validation also checks the new untracked file with `git diff --no-index --check /dev/null docs/PRESENTATION_JOURNAL.md`, because plain `git diff --check` does not include untracked files.


### M45–M47 engineering evidence additions

| Entry | Source | Demonstrates | Limitation |
|---|---|---|---|
| E45 | M47 historical predecessor record; EV-049 | Metadata-only Kharg feasibility, no repository writing at M45 | No pixel or petroleum claim |
| E46 | M47 historical predecessor record; EV-050 | GRD header/XML/access PASS without pixels; defects/failures retained | No SAR calibration/detection |
| E47 | [Design freeze](evidence/AS_201_DESIGN_FREEZE.md); EV-051; Decision054 | Exact six-source policy, coverage and security/digest/preservation contract | Not implemented; no scientific result or CI claim |

### E48 — Raw-GRD source implementation, offline validation

[EV-052](evidence/AS_201_IMPLEMENTATION_VALIDATION.md): review of preserved WIP,
strict matching/header/XML, source/group/set support identities and registry lineage.
No SAR scientific result, live provider probe or CI success claim.

### E49 — Live acceptance stopped before six-source resolution

[EV-053](evidence/AS_201_LIVE_ACCEPTANCE.md): actual public-path catalog metadata
failure; CDSE HTTP200 status/body hashes retained. No PC/source/header/XML readiness
claim, no SAR science. Exact error field remains unlocalized; no hidden retry/patch.

### E50 — Real client construction, offline provider fixtures

[EV-054](evidence/AS_201_STAC_GEOMETRY_BOUNDARY_FIX.md): immutable policy retained;
only the SAR boundary receives ordinary JSON. Original deepcopy failure reproduced,
corrected constructor and complete synthetic pagination pass. M49 historical FAIL
unchanged; zero real provider/pixel/scientific work; no live-readiness claim.

### E51 — Controlled retry reaches the next strict identity gate

[EV-055](evidence/AS_201_LIVE_ACCEPTANCE_RETRY.md): M50 construction now succeeds
live; both catalogs complete. Six CDSE product-type representation failures leave
all slots UNAVAILABLE, readiness false, no normalized sources/derived provenance.
No signing/header/XML/pixel/science request and no production correction.

### E52 — Exact CDSE product-type interoperability, offline only

[EV-056](evidence/AS_201_CDSE_PRODUCT_TYPE_FIX.md): accepts IW_GRDH_1S exactly,
preserves GRD/GRDH and strict field/identity guards. All six synthetic CDSE sources
normalize; 41 new regression cases; shared STAC/optical and frozen policy unchanged.
M49/M51 FAIL records retained; no live retry, pixels or SAR science. Live readiness unproved.

### E53 — Single public run crosses identity/header gates, fails manifest time

[EV-057](evidence/AS_201_LIVE_ACCEPTANCE_AFTER_M52.md): exact six-source resolution
and all VV headers pass; 24 XMLs fetched, all six manifest/startTime timezone checks
fail. Final retrieval remains unavailable/ready=false with normalized lineage and
deterministic metadata support. No provider retry, production fix, pixels or SAR science.

### E54 — Manifest-only UTC interpretation, exact matching retained

[EV-058](evidence/AS_201_MANIFEST_UTC_TIME_FIX.md): 24 six-source serialization cases,
49 fail-closed/guard controls; 250 focused / 1548 full tests PASS. Generic parser,
resolver and later XML guards unchanged; zero provider requests and SAR science.
M53 stays historical FAIL; no live-readiness claim.

### E55 — Single live run passes manifest time, fails platform family text

[EV-059](evidence/AS_201_LIVE_ACCEPTANCE_AFTER_M54.md): all six exact sources,
VV headers and manifest acquisition intervals pass; platform familyName cardinality
fails. Later validators are NOT_REACHED; all final slots unavailable, ready=false.
One search/validation, no patch/restart/extra requests/pixels or SAR science.

### E56 — Six unchanged manifests expose a recursive XML scope collision

[EV-060](evidence/AS_201_MANIFEST_PLATFORM_DIAGNOSTIC.md): direct platform family
SENTINEL-1 and nested instrument family Synthetic Aperture Radar are conflated by
recursive lookup. Two distinct values reproduce the exact exception in every source;
uppercase direct text also differs from the later literal. No production fix or
acceptance retry, catalog/TIFF/other XML/pixels/scientific compute. M55 remains FAIL.

### E57 — Manifest-only direct identity and case normalization, offline validated

[EV-061](evidence/AS_201_MANIFEST_PLATFORM_FIX.md): exactly one nonempty direct familyName,
case-only Sentinel-1 equality; nested instrument cannot contaminate or rescue identity.
69 added offline cases; earlier/time/shared/later guards preserved. No provider requests,
production behavior beyond this manifest block, live retry, pixels or SAR science.
M55 remains historical FAIL; M56 diagnostic preserved; readiness UNPROVED.

### E58 — One unchanged public live run, passively accounted

One search + one access-validation call; no monkeypatch, manual retry, restart,
production edit or additional diagnostic request. Complete manifest PASS in each
source; strict calibration.azimuthTime failure preserved before later XML guards.
Final failure-state identity/provenance valid with 12 immediate sources; ready=false.
Zero pixels/science. Offline engineering tests cannot override live failure.

### E59 — In-memory timestamp audit with exact body-hash continuity

Exactly 18 existing XMLs fetched once; every body hash/length equals M58.
Only consumed ADS and calibration/noise-range timestamp fields inspected.
360 unchanged generic parser calls reproduce strict timezone rejection; minimal
raw/stripped ADS facts and vector first/last/counts/digests retained, not raw XML.
Passive accounting, no monkeypatch/full validator; no inferred UTC or code change.

### E60 — SAFE-local UTC parsing with exact identity and guard preservation

- Four calls/eight field paths use specified UTC interpretation for naive SAFE
  timeType text; unpadded/microsecond validation occurs before text normalization.
- Byte comparison preserves generic parser, M54/M57, all unrelated functions;
  exact ADS mismatch/metadata tamper regressions retain fail-closed behavior.
- 163 new cases; eight reviewed expectation changes; 493 focused / 1780 full PASS,
  six existing warnings. No provider traffic or scientific application. EV-064.

### E61 — Complete unchanged production validators with passive noise structure

- Source-line tracing records successful guards, without replacement functions,
  added requests or validator reruns. Six slices, 35 required stages each PASS.
- Noise-azimuth summaries retain counts/booleans only; no raw XML or credentials.
  Original TIFF reader validates zero metadata/image-block overlap.
- Twelve source IDs/common support remain identical; accepted-access metadata
  changes fingerprints appropriately. 493 focused / 1780 full PASS; six warnings.
- Six documentation/evidence paths only. No SAR scientific processing. EV-065.

## 5. Scientific evidence index

| ID | Evidence | Scientific meaning / permitted claim | Boundary |
|---|---|---|---|
| S01 | Decisions 014–015; PRD §5 | Intended outputs support awareness and field verification | No toxin/species/petroleum confirmation, definitive safe/unsafe certification, or automatic shutdown |
| S02 | [AOI GeoJSON](../data/aoi/demo_site.geojson); Decisions 017–018 | Explicit analyst-defined Al Raha study area | Not an official boundary or operational intake |
| S03 | AS-101 live-result record | Candidate L2A metadata is available in the chosen AOI/window | Cloud metadata is scene-wide; usable water pixels not demonstrated |
| S04 | Provenance schema/tests and AS-101 conversion record | Observations retain source/product/time/catalog identity | Traceability does not itself validate reflectance or a hazard |
| S05 | Decision 016; PRD §11 | Al Raha April 2023 and Kharg May 2026 are historical validation candidates | No completed event analysis, labelled dataset, or laboratory confirmation in tracked evidence |
| S06 | Decisions 011–013; configured weights | Explainable, separately interpretable hazards and tunable PoC hypotheses | No fitted classifier, validated weights, or measured risk calibration |
| S07 | Decision 008 | SAR roughness anomalies can motivate slick-candidate analysis | Low-wind and natural-film look-alikes must be reviewed; no implemented oil result yet |
| S08 | [CDSE reflectance metadata](evidence/AS_102_CDSE_ACCESS_PROBE.md#reflectance-scaleoffset-discovery); M09 | Advertised scale 0.0001/offset -0.1 imply `DN * 0.0001 - 0.1`; mask DN=0 first, do not automatically clamp valid negatives | No decoded pixel verification; L2A BOA reflectance is not automatically aquatic remote-sensing reflectance |
| S09 | [PC identity comparison](evidence/AS_102_PLANETARY_COMPUTER_PROBE.md#cross-provider-identity-finding); M12 | Metadata supports same acquisition but different baseline/product identity | No pixel equivalence; actual raster product needs its own provenance |
| S10 | [CDSE quality assets](evidence/AS_102_CDSE_ACCESS_PROBE.md#advertised-assets-format-and-grid); [PC inventory](evidence/AS_102_PLANETARY_COMPUTER_PROBE.md#asset-inventory-and-advertised-delivery-path) | SCL available in both; `CLD_20m` observed in CDSE; no separate cloud-probability asset observed in the inspected PC item | No quality-mask performance, usable-water fraction, or collection-wide absence claim |
| S11 | [Final PC XML / decoding](evidence/AS_102_PLANETARY_COMPUTER_RASTER_GATE.md#product-xml-and-metadata-driven-interpretation); EV-015 | Retrieved PC baseline-05.09 XML quantification 10000 and offset -1000 map B02/B05 DN to BOA reflectance | Access/decoding mechanics only; BOA is not automatically aquatic remote-sensing reflectance or chlorophyll concentration |
| S12 | [Final SCL window](evidence/AS_102_PLANETARY_COMPUTER_RASTER_GATE.md#observed-bounded-window-reads) | Raw 32×32 SCL sample has 353 water-class pixels out of 1024 | Not final usable water after masks; no valid-water fraction or HAB evidence |
| S13 | [AS-102 full-AOI evidence](evidence/AS_102_OPTICAL_PREPROCESSING_VALIDATION.md); EV-016 | Actual XML-decoded BOA, nine aligned bands, conservative mask statistics and retained negative reflectance | Mask-accepted water is not independent coastal-water truth, aquatic Rrs, HAB/chlorophyll/toxin or safety evidence |
| S14 | [AS-103 candidate-feature evidence](evidence/AS_103_SPECTRAL_FEATURES_VALIDATION.md); Decision 046; EV-019 | Six signed-BOA spectral features with declared nominal wavelengths, numerical guards and retained out-of-range diagnostics | BOA is not aquatic Rrs; no calibrated chlorophyll, event/HAB threshold or independent evidence from correlated NDCI-like/B05:red features |
| S15 | M29 / E29 / EV-033; unchanged Decision 050 | Real reproducible seven-pixel candidate anomaly geometry, F2/F4 agreement, 2,800 m² projected-grid candidate area on P=802; observed coarse ranks | No known-event comparison, biological causation, HAB/bloom/concentration, accuracy/false positives, risk/confidence or operational inference; sparse support and five-history limitations remain |

No measured HAB accuracy, false-positive rate, temporal lead time, intake exposure, or avoided loss is available in the repository. The presentation must distinguish motivation, planned method, measured engineering evidence, and future scientific validation.

M39 / E39 / EV-043 adds reproducible real provisional observational screening: Watch 29.52380952380953, completeness/coverage .7/.7, context/exposure unavailable. It adds no biological/event accuracy evidence and does not replace historical S01–S15.

## 6. Failures / blockers / pivots

| Topic | Classification | Repository-supported observation | Response / lesson | Presentation restriction |
|---|---|---|---|---|
| TOML boolean becomes `1.0` through coercion | Fixed review defect | `f57f6bf` changes the loader and adds numeric/invalid-input tests | Reject invalid types before converting or requesting the catalog | May show the actual before/after diff; not a measured environmental failure |
| Pagination cycles, malformed pages, conflicting duplicates | Tested failure modes | AS-101 code/tests explicitly reject these cases | Explicit failure is safer than silently returning partial evidence | Do not claim the live provider exhibited all fixture failure modes |
| Raster access after catalog search | Recorded environmental blocker | [CDSE report](evidence/AS_102_CDSE_ACCESS_PROBE.md): proxy blocked raster/header/window attempts; S3/OIDC route advertised | Separate catalog success, runtime blocking, and provider access requirements | No successful bounded CDSE read or universal provider-denial claim |
| Reflectance offset discovery | Advertised metadata finding; pixel verification pending | CDSE scale 0.0001/offset -0.1 recorded for selected baseline-05.10 product | Use product-specific metadata; capture sanitized per-band excerpts | Formula is metadata-derived, not an observed decoded-pixel result |
| Planetary Computer / allowlist / signing | Recorded catalog success and historical asset-host blocker | [PC report](evidence/AS_102_PLANETARY_COMPUTER_PROBE.md): HTTP 200; additional blob-host allowlist needed | Advertised COG path remains viable; signing/decoding/read still pending at this stage | No provider pivot, successful signing, or successful raster read claimed |
| PC final access gate — later stage | Reported successful access/decoding experiment | [FG-01](evidence/AS_102_PLANETARY_COMPUTER_RASTER_GATE.md): 4 HTTP 200 credential-free signings, 3 windows, XML read, 8/8 gates passed | Preserve the earlier blocker/PENDING history; use actual PC product identity | Not all-band preprocessing, scientific validation, a provider decision, or exact byte-efficiency evidence |
| Same observation, different processing product | Metadata-supported finding | Acquisition/platform/tile/orbit match; CDSE 05.10/Aug 2024 versus PC 05.09/Apr 2023 | Preserve actual product identity if provider supplies pixels | Same acquisition does not imply pixel equivalence |
| Live services, cloud, labels, SAR look-alikes | Anticipated risks, not necessarily observed failures | PRD risk register and Project State §18 | Cached fallback, conservative claims, transparent baselines, false-positive review | Keep planned mitigations distinct from completed work |
| PRD calendar versus current delivery | Schedule plan versus actual state | Planned 3 Oct preprocessing did not override the historical not-started checkpoint; actual M15 acceptance is dated 6 Oct | Use commits and state docs for the completed timeline | Do not present the entire planned calendar as achieved |

No provider pivot was adopted by the historical probe/evidence tasks. The separately authorized M15 implementation now adopts CDSE discovery plus actual-PC raster delivery (Decisions 039–045). Historical reports preserve their earlier boundaries; FG-01 access success alone did not establish preprocessing. EV-016/EV-017 separately establishes AS-102 mechanics, not scientific performance. Original historical transcripts/timestamps/screenshots remain capture gaps.

## 7. Metrics and quantitative results

| Metric | Recorded value | Date / source | Interpretation |
|---|---|---|---|
| AS-003 quality baseline | 17 tests passed; Ruff passed | 2 Oct; Project State §9 | Historical whole-project baseline; preserve as history |
| Initial AS-101 quality baseline | 92 tests passed; Ruff/diff check passed | 2 Oct documentation at `b3f0e9f` | Superseded by review fixes; not current baseline |
| AS-101 reviewed baseline | 97 tests passed; Ruff/diff check passed | Review docs `35caa90`; current AS-101 report | Engineering validation, not scientific accuracy |
| Added cloud-type cases | 5: 2 accepted numeric, 3 rejected literals | `f57f6bf`; config tests | Explains 92 → 97; invalid cases make zero catalog calls |
| Live catalog result | 44 unique candidate products | 2 Oct; AS-101 report | Not 44 independent dates, water-valid scenes, or detections |
| Provenance conversion/serialization | 44/44 successful | Same recorded live experiment | Valid source records for all candidates |
| Acquisition span | 4 Mar 06:47:51.024Z – 28 May 06:46:29.024Z, 2023 | AS-101 report | Returned temporal coverage only |
| Observed scene cloud cover | 0.12–24.96% | AS-101 report | Not AOI-specific clear-water fraction |
| Query settings | 1 Mar–31 May 2023; <= 30% scene cloud | Config/report | Input constraints, not performance results |
| First candidate asset references | 47 | AS-101 report | Inventory count; no raster access implied |
| Metadata request timeout | 30 seconds default | Config/Decision 038 | Per request; not total duration or measured latency |
| New direct AS-101 dependency | 1: `pystac-client==0.9.0` | pyproject / Decision 038 | No raster-processing stack adopted |
| Provenance schema | 1.0 | Provenance serialization / Project State | Schema version, not product maturity score |
| Selected CDSE item's assets | 47 | [CDSE probe record](evidence/AS_102_CDSE_ACCESS_PROBE.md) | Separate from the first March candidate's 47 references |
| CDSE advertised raster conversion | Scale 0.0001; offset -0.1 | CDSE probe metadata record; original probe date not supplied | Metadata-derived formula; no read DN/decoded sample |
| PC anonymous STAC | READY / HTTP 200 | [PC historical checkpoint](evidence/AS_102_PLANETARY_COMPUTER_PROBE.md) | Catalog access, not successful raster access |
| PC advertised probe assets | B02 10 m; B05 and SCL 20 m COG; nine reflectance bands available | PC item-inspection record | No native header or bounded read verified at this point |
| Cross-provider processing versions | CDSE 05.10/Aug 2024; PC 05.09/Apr 2023 | PC identity comparison | Same acquisition/platform/tile/orbit; different processed product |
| Bounded PC raster read | PENDING | EV-014; pre-read evidence point | No window/DN result; any later gate requires a separate dated record |
| Later PC final access gate | PASS / READY; 8/8 gates passed | [FG-01 record](evidence/AS_102_PLANETARY_COMPUTER_RASTER_GATE.md); original experiment timestamp missing | Later stage; historical PENDING row retained |
| Credential-free signing | 4 HTTP 200 operations: B02, B05, SCL, product-metadata | FG-01 | No user credentials/subscription key; tokens transient, not recorded |
| Successful bounded reads | 3: B02 64×64; B05/SCL 32×32 | FG-01, GDAL 3.10.3 | Shared approximately 640×640 m; no full-scene download |
| Raw SCL sample | Class 4=58, 5=540, 6=353, 7=73; total 1024 | FG-01 | 353 water-class pixels are not final usable-water pixels |
| Product XML / PC decoding | 53,347 bytes; baseline 05.09; quantification 10000; offset -1000 | FG-01 / EV-015 | XML size, not raster-transfer bytes; formula `(DN - 1000) / 10000`; B02/B05 mapping from XML |
| PoC deadline | 11 October 2026 | PRD | Delivery target, not evidence of readiness |

| Metric | Observed result | Evidence | Limitation |
|---|---|---|---|
| AS-102 full-AOI arrays | 9 float32 bands, aligned SCL/masks; (228,310), 20 m EPSG:32640 | M15 / EV-016, exact 6 Oct timestamp | Processing geometry, not aquatic validity |
| AS-102 mask counts | AOI 67,449; valid data 65,166; candidate water 10,211; valid water 7,963 | M15 / EV-016 | Mask-accepted water, not verified water/HAB |
| AS-102 fractions/loss | AOI 11.805957%; retention 77.984526%; excluded water 2,248 | M15 / EV-016 | Explicit denominators and conservative loss |
| Historical 6 Oct AS-102 quality/cache | 213 tests passed (97 retained +116 added); Ruff/diff check passed; checksum/offline replay equivalent | M15 / EV-017 | No accuracy/lead-time/service-availability claim |
| AS-102 final reviewed/merged baseline | 265 tests passed; Ruff/diff check passed; six non-blocking Rasterio warnings | M16 / EV-018; 8 Oct; PR #6 / `627b6ae` | Local checks; no configured/reported GitHub CI, no scientific accuracy claim |
| AS-103 candidate feature acceptance | 6 arrays; 7,963 valid pixels each; 2 NDCI-like out-of-range values; repeat/lineage exact; 348 tests | M17 / EV-019–EV-020; 8 Oct cached experiment | No anomaly/event or scientific validation claim |
| AS-103 final reviewed/merged baseline | 348 tests passed; Ruff/diff checks passed; six existing non-blocking Rasterio warnings, no new AS-103 warnings | M18 / EV-021; PR #8 / `b770d056`; merge 8 Oct 10:43:24 UTC / 14:43:24 Asia/Dubai | Local engineering/review evidence; no configured/reported GitHub CI or replacement real-scene experiment; no scientific accuracy claim |

Unavailable metrics: exact raster-transfer bytes, aquatic radiometric validation, accuracy/false positives, warning lead time, buyer validation or avoided operating cost. AS-102 preprocessing and valid-water mask statistics are now observed for one real scene. The exact experiment start/completion interval is recorded, but it is not a standalone preprocessing benchmark or network-throughput measure.

| AS-104 branch offline baseline | 460 tests; six historical warnings; Ruff/diff PASS | M19 / EV-022 | Not merged; no CI-success claim |
| AS-104 real history gate | Five March discovery dates; two first-date PC matches; zero processed references | M19 / EV-023 | Real multi-scene acceptance BLOCKED; no temporal product |

| Metric | Observed result | Evidence | Limitation |
|---|---|---|---|
| AS-105 real evaluable support | P=802 / target water=7,963 = 10.071581% | M29 / EV-033 | Coverage diagnostic only, not full AOI/ocean/risk coverage or candidate fraction |
| AS-105 real candidates | 7 / P=802 = 0.872818%; descriptive 7/7,963 = 0.087907% | M29 / EV-033 | Frozen heuristic candidates, not detections or probability |
| AS-105 projected-grid candidate area | 2,800 m² / 0.0028 km²; pixel 400 m² | M29 / EV-033 | Not confirmed bloom extent |
| AS-105 real geometry | One eight-connected region; one MultiPolygon, three four-connected parts; F2/F4 votes | M29 / EV-033 | Parts are not three independent regions; no biological confirmation |
| AS-105 real rank granularity | No supported exact .90; observed threshold passers all rank 1 | M29 / EV-033 | This parent only; exact ties can yield .90 elsewhere; history-depth sensitivity required / NOT RUN |
| AS-105 real engineering quality | 140 focused / 803 full tests, Ruff/diff PASS, six historical warnings; repeat 27/27, parent 61/61 unchanged | M29 / EV-033 | Local engineering acceptance only; no CI, accuracy, event or comparative-policy validation |

| M39 real observational screening | 29.52380952380953 / Watch; completeness .7, coverage .7; S40/E33.333333333333336/T0 | M39 / E39 / EV-043 | Provisional, context/exposure unavailable; zero recurrence not biological absence/safety; no calibration |

## 8. Presentation visual / screenshot inventory

No presentation screenshot/image assets are tracked in the inspected repository. The PRD contains a text architecture diagram; source documents, tests, and Git history are available to capture. The following are **recommended future visuals**, not existing screenshots or generated artifacts.

| Visual ID | Proposed visual | Evidence basis | Capture status / constraint |
|---|---|---|---|
| V01 | Operator, offshore concern, verification decision | PRD §§1–5; Decisions 001–004 | Planned diagram; label product value as intended, not measured |
| V02 | Implemented versus planned architecture | PRD §9; tracked source tree | Text diagram exists; slide rendering pending; mark AS-102 as complete/merged through PR #6 and hazards/UI as future |
| V03 | Foundation/continuity/AS-101 timeline | Git history; M02–M08 | Capture pending; distinguish source dates and timezones |
| V04 | Al Raha study polygon and public reference point | GeoJSON; Decisions 017–018 | Map pending; explicitly “analyst-defined validation AOI,” not intake |
| V05 | Source/derived lineage example | Provenance tests/models; Decisions 019–020 | Capture pending; use a labelled fixture, not an invented real alert |
| V06 | Search constraints and 44/44 evidence card | AS-101 recorded result | Layout pending; state observation date and scene-count caveats |
| V07 | Tiny candidate metadata table | Five real example rows in AS-101 report | Capture pending; retain exact IDs/cloud values; no complete timeline inference |
| V08 | Cloud-type review diff and 97-test summary | `f57f6bf`; tests; quality record | Capture pending; show actual run result and interpreter when captured |
| V09 | CDSE reflectance metadata and formula | M09; [CDSE report](evidence/AS_102_CDSE_ACCESS_PROBE.md) | Report available; sanitized original metadata capture pending; label as advertised, not pixel-verified |
| V10 | CDSE/PC access and product-identity comparison | M10–M12; [PC report](evidence/AS_102_PLANETARY_COMPUTER_PROBE.md) | Comparison table available; rendered visual/original response capture pending; raster read still pending at this checkpoint; never show SAS URLs/tokens |
| V11 | Before/event/after water evidence and mask map | PRD §§11, 17; AS-108 plan | Future scientific validation; no actual result available |
| V12 | Separate HAB/oil evidence and monitoring-priority panels | PRD §§13, 17 | Future dashboard/demo; do not present mockups as implemented software |
| V13 | PC STAC → temporary SAS → COG windows → XML → decoding → future masks/alignment | M14; [final gate](evidence/AS_102_PLANETARY_COMPUTER_RASTER_GATE.md) | Pipeline visual and sanitized signing/GDAL/XML/decoding captures still needed; no signed URLs/tokens; last step explicitly future |
| V14 | 32×32 SCL raw class distribution and shared probe footprint | M14 / S12 | Visual pending; show 353/1024 as raw water-class pixels, never final usable-water count |
| V15 | Al Raha AOI, SCL candidate water, retained water and support exclusions | M15 / EV-016 | Real arrays exist in ignored AOI cache; map/screenshot still pending; label mask eligibility, not HAB |
| V16 | XML decoding, actual-PC lineage and offline-cache validation card | M15 / EV-017; Decisions 039–045 | Capture pending; no SAS; separate CDSE discovery product and actual PC pixel product |
| V17 | Final review/merge and local 265-test quality card | M16 / EV-018; PR #6 / `627b6ae` | Capture pending; distinguish local checks from absent GitHub CI; no scientific-result claim |
| V18 | Six candidate feature maps, support and numeric diagnostics | M17 / EV-019 | Capture pending; label candidate signed-BOA signals, not HAB/anomaly |
| V19 | Formula, input fingerprint and PC→AS-102→AS-103 lineage | M17 / EV-020; Decision 046 | Capture pending; show immediate parent and numerical-only epsilon |
| V20 | Final AS-103 review/PR #8 merge and local 348-test quality card | M18 / EV-021; implementation `5638bc8`, merge `b770d056` | Capture pending; distinguish review/merge from M17 experiment and local checks from absent GitHub CI; no scientific-result claim |
| V21 | Causal window/support/MAD/rank/lineage and March 4 two-product blocker | M19 / EV-022–EV-023 | Capture pending; no real temporal anomaly map or biological interpretation |
| V22 | Preserved integration and three signing-blocked reruns | M21 / EV-025 | Capture pending; sanitized timeline/hash/533-test/HTTP status card; no signed URLs or temporal anomaly map |
| V23 | P-versus-target-water map, seven candidates/three polygon parts, F2/F4 votes and empirical-rank ladder | M29 / E29 / EV-033; external checksummed bundle | Capture pending; no screenshot created; label candidate geometry and 802/7,963 sparse support, never confirmed HAB/event or comprehensive ocean assessment |

For every captured visual, record its path, date, evidence IDs, source/product identity where relevant, caption, licence/attribution, and limitations. Large rasters and runtime caches remain excluded from Git; screenshots must contain no credentials or private operational information.


## 9. Lessons learned

These are interpretations supported by the reconstructed evidence, not new technical decisions.

1. **Define the operational question first.** Decisions 001–004 link sensors to monitoring priority for a specific user; no demonstrated commercial impact yet.
2. **Separate validation geometry from deployment claims.** Decisions 017–018 prevent an accessible study polygon from becoming a falsely implied intake.
3. **Build traceability before live ingestion.** AS-003 enabled AS-101 to validate every candidate as a source record without changing provenance.
4. **Make handoffs recoverable.** AS-000C records context and authorization in Git; the new M09–M13 reports preserve prior investigations while exposing remaining timestamp/transcript/capture gaps.
5. **Catalog completeness is a correctness concern.** AS-101 consumes pagination and rejects malformed/incomplete results rather than returning quiet partial success.
6. **Validate input meaning before conversion.** The cloud boolean fix preserves the user's configured threshold and adds explicit pre-network evidence.
7. **Software evidence and scientific evidence answer different questions.** 97 passing tests and 44 catalog candidates do not establish water-pixel usability or hazard performance.
8. **Minimal dependencies protect scope.** AS-101 adds a STAC client only; the broader PRD tool list is not a mandate to install everything.
9. **A presentation needs an evidence trail too.** Historical probes and later FG-01 now preserve separate evidence stages. Bounded PC reads and XML-driven decoding are established for tested assets; original commands/timestamps and visuals still need capture. Access mechanics do not establish aquatic suitability or pixel equivalence.
10. **Plans are not completion records.** AS-101's merge is evidenced; M15 preserves historical AS-102 feature-branch acceptance, and M16 / EV-018 separately establishes final review/merge. M17 / EV-019–EV-020 records separately authorized AS-103 feature-branch acceptance; M18 / EV-021 establishes its later final review/merge through PR #8. Temporal/anomaly, hazard/risk and UI milestones remain future work; AS-104 remains unauthorized.
11. **Use the actual product's metadata.** PC decoding came from retrieved baseline-05.09 XML and band mapping, not an assumed DN/10000 formula or borrowed CDSE offset; the successful mechanism needed masking/alignment (now addressed separately by M15); independent scientific validation remains future.

12. **Track interpolation contributors, not just target labels.** M15 rejects land/cloud/nodata support across all nine bands and quantifies lost candidate water instead of quietly retaining mixed pixels.
13. **Test cached evidence as part of the product.** M15 verifies checksums, grid, statistics and actual-PC lineage; a known-ID replay succeeds with external access blocked. Scientific validation remains separate.

14. **Real engineering acceptance preserves scientific limits.** M29 independently checks the frozen policy and exact geometry without tuning; seven candidates on 802 evaluable pixels are not confirmed HAB or event agreement. Separate sparse support, candidate fraction and projected-grid candidate area.

## 10. Final-presentation slide candidates

This is a proposed 7-slide spine, consistent with the PRD's 5–7-slide target. It is not a final deck or a claim that the full PoC is submission-ready. Detailed milestone titles above can become appendix material.

| Slide | Candidate title / story | Evidence / visual | Readiness |
|---|---|---|---|
| 1 | “Watch the sea before a threat reaches the intake” — user, problem, verification decision | M01, S01; V01 | Thesis supported; operational benefit remains intended |
| 2 | “The right sensor for each hazard” — S2 biology, S1 slick candidates, optional hyperspectral | Decisions 005–015; V02 | Scope supported; hazard results not built |
| 3 | “Build the evidence trail first” — config/AOI, provenance, recoverable handoffs | M02–M05; V03–V05 | Engineering supported; visuals pending |
| 4 | “44 real candidates, every source traceable” — real CDSE query and its limits | M06–M07; E05–E07; V06–V07 | Live metadata evidence supported |
| 5 | “From catalog metadata to real satellite pixels” — historical blockers/PENDING → credential-free signing, bounded COG windows, product XML decoding | M09–M14; EV-009–EV-015; V09–V10, V13–V14 | Later gate PASS / READY for tested product/path; capture visuals pending; M15 separately records later masks/alignment |
| 6 | “7,963 conservatively masked water pixels, every source traceable” — XML, fixed grid, contributor support and cached replay | M15–M16; EV-016–EV-018; V15–V17 | AS-102 complete/merged through PR #6; AS-103 complete/merged through PR #8 (M18 / EV-021); AS-104 temporal comparisons passed real acceptance (M25 / EV-029), were published (M26 / EV-030) and are COMPLETE AND MERGED through PR #12 (M27 / EV-031) |
| 7 | “Monitoring priority with evidence and limits” — intended workflow, AS-101 97 / AS-102 final 265 test baselines (historical M15: 213), reproducibility, next steps | M08/M15/M16; S01–S08; V08/V16/V17 | Engineering supported; end-to-end demo and impact evidence outstanding |

For a presentation made from this evidence pack, slide 5 must label observed versus metadata-derived/inferred findings and show EV-014's historical PENDING → later PASS / READY progression. Do not show 353 raw SCL water-class pixels as a valid-water count or claim exact transferred-byte efficiency. Slide 6 may show the separately validated AS-102 mask/lineage/cache result and AS-103 candidate features complete/merged through PR #8. Distinguish M17 historical acceptance from M18 final review/merge; AS-104 temporal comparisons passed real acceptance (M25 / EV-029), were published (M26 / EV-030) and are COMPLETE AND MERGED through PR #12 (M27 / EV-031). Event/scientific validation remains future work. Never replace missing real scientific evidence with an unlabelled simulation. Business subscriptions/licences in PRD §23 are hypotheses, not validated pricing or revenue.

M29 appendix slide candidate: “Seven candidate pixels, an honest denominator, reproducible geometry”; use V23 / EV-033 and label engineering acceptance, sparse coverage, no event comparison and future policy validation NOT RUN. Capture pending.

## 11. Outstanding evidence still needed

AS-105 M28 COMPLETE / COMMITTED / PUSHED; M29 real engineering acceptance and
owner review PASS. Exact real metrics and canonical geometry are now recorded
in EV-033 and the external local bundle, NOT tracked in Git. Sanitized map/slide
capture remains pending. AS-105 is COMPLETE AND MERGED through PR #14;
Decision 051 is merged and unchanged. AS-106 M31 offline implementation and
synthetic/adversarial validation PASS; owner feature review is next. Real April
preparation and M32–M35 remain NOT STARTED.
Future comparative policy validation, including
predeclared history-depth sensitivity, is REQUIRED / NOT RUN. No known-April-event
comparison or accuracy/biological claim. Synthetic visuals remain labelled;
AS-107+ and P1 05.10 NOT STARTED.

| Priority / category | Missing evidence | Required record before a presentation claim |
|---|---|---|
| Immediate capture | CDSE reflectance metadata verification | Formula/baseline now in [CDSE report](evidence/AS_102_CDSE_ACCESS_PROBE.md); still need original per-band metadata excerpt, timestamp, and actual decoded sample verification |
| Access verification / capture | CDSE raster investigation follow-up | Proxy blocker and advertised route recorded; still need original commands/hosts/tool context and bounded transport/header/window result |
| Historical capture / later validation | Planetary Computer final gate | FG-01 now records signing, three raster reads, XML and B02/B05 decoding; original timestamp/command/8-gate checklist and metadata screenshots still needed; M15 separately supplies new all-band implementation evidence |
| Identity capture | Same acquisition / different processing product | Comparison now in [PC report](evidence/AS_102_PLANETARY_COMPUTER_PROBE.md#cross-provider-identity-finding); original metadata excerpts/rendered comparison pending; pixel equivalence unverified |
| Historical gate capture | Later AS-102 final access gate | EV-014 historical PENDING and later FG-01 PASS/READY retained unchanged; M15 separately supplies all-band arrays/mask counts. Original FG-01 timestamps/captures and exact transfer bytes remain missing; scientific performance unverified |
| AS-102 presentation capture | Optical preprocessing implementation | M15 / EV-016–EV-017 preserve the 213-test/full-AOI acceptance; M16 / EV-018 records final review/merge with 265 tests. Sanitized map, merge and quality captures remain pending |
| AS-103 presentation capture / future science | Candidate spectral features and final review/merge | M17 / EV-019–EV-020 preserve acceptance; M18 / EV-021 records final code-review/merge through PR #8. Sanitized V18–V20 captures and independent scientific validation remain pending; later AS-104 acceptance/publication/merge is separately recorded by M25–M27 / EV-029–EV-031 |
| P0 scientific evidence | HAB and oil historical validation | Cited event references, usable observations, before/during/after, false-positive review, uncertainty, temporally separated evaluation |
| P0 product evidence | Operational site and decision demo | Defensible public site/intake source; clearly separated validation AOI; working hazard-specific evidence/priority workflow |
| P0 reproducibility | Clean-environment/full-product demo | AS-102 AOI cache replay verified by EV-017; second-machine cache provisioning and full hazard/decision demo remain future; no raw scenes or secrets in Git |
| P0 presentation | Captured visuals, demo recording, attribution | Real screenshots/figures linked to evidence IDs, metadata/licences, limitations, dated 90–180-second recording |
| Scientific/impact claim | Lead time, accuracy, operational benefit | Measurement method, reference labels/timing, limitations; omit claims until supported |
| P1 only | Hyperspectral/environmental enhancement | Demonstrated usable data and measurable contribution; must not block core P0 |
| AS-104 acceptance/publication capture and future science | Temporal observational comparisons | Earlier provider/transport/platform blockers remain historical (M19/M21/M23); M25 / EV-029 acceptance PASS, M26 / EV-030 publication and M27 / EV-031 merge/closeout recorded. Sanitized support/lineage/merge visuals and independent scientific validation remain pending; AS-104 COMPLETE AND MERGED through PR #12 |

The historical probe records and separate later FG-01 record transcribe the owner's supplied evidence. The later report was created before this journal update; it resolves access/decoding outcome gaps only for the tested product/path/assets. Original historical entries remain intact. Remaining capture/scientific gaps do not assert that experiments failed or never happened. Those historical documentation tasks changed no source/tests/configuration/decisions. The separately authorized M15 implementation now adds source/tests/configuration and Decisions 039–045, with its own dated evidence and scope.


## 12. Reusable milestone-entry template

Copy the following for each meaningful milestone, major review, data probe, failure, or decision. Write “not recorded,” “not measured,” or “pending” when evidence is missing.

```markdown
### Mxx — Milestone name

- **Date:** Event date/timezone; separately record report/commit date if different.
- **Task / milestone ID:** Existing task ID or clearly labelled investigation.
- **Status:** Completed fact / current decision / recorded experiment / blocker / evidence gap / future plan.
- **Problem / question:** What uncertainty or user need was addressed?
- **Why it mattered:** Product, engineering, scientific, or delivery consequence.
- **Options considered:** Only recorded alternatives; say if none are recorded.
- **Decision:** Existing approved decision ID, or pending; this entry alone is not approval.
- **Rationale:** Evidence supporting the choice and its tradeoffs.
- **Implementation / experiment:** Exact bounded work performed, environment/tools, inputs.
- **Evidence:** Relative repository paths, section/evidence IDs, full commit SHA/PR,
  sanitized provider records and reproduction method where relevant.
- **Quantitative result:** Values, units, denominator, observation date, and uncertainty;
  distinguish measured results from settings and planned targets.
- **Limitation:** What the evidence cannot establish; missing ground truth or access.
- **Lesson learned:** Interpretation supported by the evidence, not invented impact.
- **Impact on next step:** Prerequisites, remaining gaps, and authorization boundary.
- **Presentation takeaway:** A defensible sentence with an appropriate status label.
- **Recommended visual:** Existing artifact path or planned capture; caption/attribution.
- **Candidate slide title:** A title that does not overclaim the result.
```

For external data, also record provider, collection, item/product ID, observation identity, processing version, stable unsigned source references, metadata origin, licence, and lineage impact. If a result changes, preserve the old dated result and add the new one with its cause; do not silently replace history. Never store credentials, SAS tokens, private keys, full raw scenes, or runtime caches as evidence.

## Presentation Update Rule

Future agents must update this journal after every meaningful milestone or major decision, within the authorized documentation scope. Add a dated milestone entry with all template fields and repository evidence; update the timeline, evidence indexes, metrics, blocker state, visual inventory, and slide candidates affected by it.

Record successful and failed experiments, options considered, reasons, quantitative outcomes, limitations, and lessons while the evidence is available. Preserve historical baselines and prior decision rationale. Label proposed work and missing evidence explicitly; never promote chat memory, intended work, synthetic examples, or an access probe into completed implementation or scientific validation.

Cross-check new entries against Project State, Handoff, Decisions, the PRD, tests/code, and Git history. An approved technical change belongs in the decision log through a separately authorized task; this journal only records and explains it. Keep feasibility, authorization, implementation, merge status, and validation distinct. Do not mark AS-102 implemented or start AS-103 through a presentation update. Capture sanitized visual references and exact reproduction evidence without secrets or large EO files.
