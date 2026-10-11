# AquaSentinel 813 — Presentation Evidence Index

## Current AS-201 M60 — SAFE XML UTC time interoperability correction — OFFLINE PASS

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
Evidence: [EV-064 MD](AS_201_SAFE_XML_UTC_TIME_FIX.md) /
[JSON](AS_201_SAFE_XML_UTC_TIME_FIX.json).

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
Evidence: [EV-061 MD](AS_201_MANIFEST_PLATFORM_FIX.md) /
[JSON](AS_201_MANIFEST_PLATFORM_FIX.json).

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
Evidence: [EV-060 MD](AS_201_MANIFEST_PLATFORM_DIAGNOSTIC.md) /
[JSON](AS_201_MANIFEST_PLATFORM_DIAGNOSTIC.json).

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
Evidence: [EV-059 MD](AS_201_LIVE_ACCEPTANCE_AFTER_M54.md) and
[JSON](AS_201_LIVE_ACCEPTANCE_AFTER_M54.json).

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
Evidence: [EV-058 MD](AS_201_MANIFEST_UTC_TIME_FIX.md) and
[JSON](AS_201_MANIFEST_UTC_TIME_FIX.json).

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
Evidence: [EV-057 MD](AS_201_LIVE_ACCEPTANCE_AFTER_M52.md) and
[JSON](AS_201_LIVE_ACCEPTANCE_AFTER_M52.json).

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
Evidence: [EV-056 MD](AS_201_CDSE_PRODUCT_TYPE_FIX.md) and
[JSON](AS_201_CDSE_PRODUCT_TYPE_FIX.json).

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
Evidence: [EV-055 MD](AS_201_LIVE_ACCEPTANCE_RETRY.md) and
[JSON](AS_201_LIVE_ACCEPTANCE_RETRY.json).

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
Evidence: [EV-054 MD](AS_201_STAC_GEOMETRY_BOUNDARY_FIX.md) and
[JSON](AS_201_STAC_GEOMETRY_BOUNDARY_FIX.json).

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
See [EV-053 MD](AS_201_LIVE_ACCEPTANCE.md) and
[JSON](AS_201_LIVE_ACCEPTANCE.json).

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
[EV-052 implementation evidence](AS_201_IMPLEMENTATION_VALIDATION.md) and [JSON](AS_201_IMPLEMENTATION_VALIDATION.json).
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
See [contract](../AS_201_SENTINEL1_RETRIEVAL.md), [freeze evidence](AS_201_DESIGN_FREEZE.md)
and [JSON](AS_201_DESIGN_FREEZE.json). Engineering results are recorded in
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
See [case report](AS_108_HISTORICAL_CASE_STUDY.md) and [JSON](AS_108_HISTORICAL_CASE_STUDY.json). Earlier checkpoints retain their original historical facts.

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
See [M43 evidence](AS_108_POST_METADATA_SELECTION.md) and
[complete inventory/selection digest](AS_108_POST_METADATA_SELECTION.json).
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

See [AS-108 contract](../AS_108_HAB_HISTORICAL_VALIDATION.md), [freeze evidence](AS_108_DESIGN_FREEZE.md),
and [machine-readable design](AS_108_DESIGN_FREEZE.json). Earlier dated status/milestone bodies
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

See [M40 closeout](AS_107_CLOSEOUT.md) and [machine-readable closeout](AS_107_CLOSEOUT.json).
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

See [M39 evidence](AS_107_REAL_ACCEPTANCE.md) and
[machine-readable audit](AS_107_REAL_ACCEPTANCE.json).
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
See [M38 evidence](AS_107_IMPLEMENTATION_VALIDATION.md).
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

See [frozen contract](../AS_107_HAB_RISK.md), Decision 052 and
[M36/M37 evidence](AS_107_DESIGN_FREEZE.md). Existing dated checkpoints
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

See [M35 closeout](AS_106_CLOSEOUT.md) and
[normalized closeout](AS_106_CLOSEOUT.json).
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

See [M34 evidence](AS_106_REAL_ACCEPTANCE.md) and
[normalized evidence](AS_106_REAL_ACCEPTANCE.json).
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

See [M33 evidence](AS_106_APRIL3_UPSTREAM_PREPARATION.md) and
[normalized evidence](AS_106_APRIL3_UPSTREAM_PREPARATION.json).
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

See [M32 evidence](AS_106_APRIL_METADATA_INVENTORY.md) and
[normalized inventory](AS_106_APRIL_METADATA_INVENTORY.json).
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
See [AS-106 specification](../AS_106_PERSISTENCE.md) and [M31 validation](AS_106_PERSISTENCE_VALIDATION.md).

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
See [AS-106 frozen design](../AS_106_PERSISTENCE.md) and [Decision 051](../DECISIONS.md#decision-051--as-106-causal-consecutive-valid-observation-recurrence).

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
See [AS-105 contract](../AS_105_HAB_ANOMALY_GEOMETRY.md) and [M29 validation](AS_105_HAB_ANOMALY_GEOMETRY_VALIDATION.md#m29--real-geometry-engineering-acceptance--10-october-2026).

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

See [AS-105 contract](../AS_105_HAB_ANOMALY_GEOMETRY.md) and [M28 validation](AS_105_HAB_ANOMALY_GEOMETRY_VALIDATION.md).

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
See [merge/closeout evidence §9](AS_104_TEMPORAL_BASELINE_VALIDATION.md#9-pr-12-merge-and-as-104-closeout--9-october-2026).

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
[validation §8](AS_104_TEMPORAL_BASELINE_VALIDATION.md#8-as-104-feature-publication--9-october-2026).

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
[validation §§6–7](AS_104_TEMPORAL_BASELINE_VALIDATION.md).

M23/E23/EV-027 remains the earlier **BLOCKED** platform-casing attempt; its body
and all prior checkpoint/decision bodies remain preserved. No Decision 050.
Both retained stashes and old/new external recovery artifacts remain available.
AS-104 stays **UNCOMMITTED / READY FOR REVIEW**. Owner review is the next gate;
no commit/push/PR/merge, AS-105+, or P1 homogeneous-05.10 experiment. PASS is
engineering acceptance of temporal candidate BOA signals, not biological or
operational accuracy, risk, persistence, alert or warning-lead-time validation.
Earlier dated checkpoint statements below are historical; this update governs
current state. Final quality/security verification is recorded in validation §7.

**Created:** 6 October 2026 (Asia/Dubai).

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
[resumed evidence](AS_104_TEMPORAL_BASELINE_VALIDATION.md) / M21/E21/EV-025.
**P1 Processing Baseline Robustness Experiment — NOT STARTED**: homogeneous
05.09 versus homogeneous 05.10 requires separate authorization and is not
accuracy validation. AS-105+ is NOT authorized and NOT started. No commit,
push or PR in this integration task; retain the verified safety stash.

**Purpose:** Compact claim-to-evidence index for the [presentation journal](../PRESENTATION_JOURNAL.md). This pack preserves the CDSE investigation, the **historical Planetary Computer metadata-only checkpoint**, and the [later successful final raster gate](AS_102_PLANETARY_COMPUTER_RASTER_GATE.md). Historical records do not themselves certify perpetual external-service availability or authorize implementation. The separately authorized M15 update adds actual AS-102 implementation evidence EV-016/EV-017 and Decisions 039–045; AS-103 is COMPLETE AND MERGED through PR #8; EV-019/EV-020 preserve its earlier feature-branch acceptance stage, and EV-021 records the later final code-review/publication stage. AS-102 is COMPLETE AND MERGED through PR #6; EV-018 records the final reviewed/merged stage while EV-016/EV-017 preserve their historical acceptance checkpoint.

**Later evidence stage recorded:** 6 October 2026 (Asia/Dubai), FG-01. Original experiment timestamp not supplied; this is a later experiment than the preserved metadata-only checkpoint, not a new probe run by this documentation task.

**New implementation evidence:** EV-016/EV-017, fresh experiment started `2026-10-06T10:07:14.660936+00:00` UTC / `2026-10-06T14:07:14.660936+04:00` Asia/Dubai. Base `0867708ea62676dcbcd0f5f83577cc120d633f26`, branch `feature/as-102-optical-preprocessing`. This new experiment has exact timestamps, typed processing evidence and offline tests, unlike the original supplied historical reconstructions.

**Final review/merge update:** 8 October 2026 (Asia/Dubai), EV-018. Feature `fe3d27046c40600010753957ee8921d57071ec48`; [PR #6](https://github.com/Omar-Aboulwafa/aquasentinel-813/pull/6); merge `627b6ae8a509509dbb2d5d43bbdc6d74e0ce2aac` at `2026-10-08T07:06:46Z` / `2026-10-08T11:06:46+04:00`. Final reviewed baseline: 265 tests passed, Ruff/diff checks passed; six non-blocking Rasterio warnings. No configured/reported GitHub CI/workflow checks. At the AS-102 merge checkpoint AS-103 was NOT authorized and NOT started; the later AS-103 authorization/acceptance is recorded separately below.

**Historical AS-103 acceptance checkpoint:** 8 October 2026, EV-019/EV-020; explicitly authorized candidate-feature implementation, uncommitted/unpushed/unmerged. Six features, 7,963 valid pixels each; 348-test branch baseline. AS-104 NOT authorized and NOT started.

**Historical AS-103 final review/merge update:** 8 October 2026 (Asia/Dubai), M18 / EV-021. AS-103 is **COMPLETE AND MERGED** through [PR #8](https://github.com/Omar-Aboulwafa/aquasentinel-813/pull/8). Implementation `5638bc8b4ab06f235f908642f714a7cc83b35709`; AS-103 implementation merge commit `b770d0561da9ac2b81ca2d4b8e784adff66ee231`, merged `2026-10-08T10:43:24Z` / `2026-10-08T14:43:24+04:00` Asia/Dubai. Final reviewed baseline: 348 tests passed, Ruff/diff checks passed; six existing non-blocking Rasterio PendingDeprecationWarnings only, no new AS-103 warnings. No GitHub Actions/workflow CI run was configured/reported; no GitHub CI success is claimed. AS-103 development is closed. AS-104 — Temporal Baseline is NEXT PLANNED only, NOT authorized and NOT started. No real-scene experiment was rerun during merge review or this documentation closeout.

**Historical AS-104 checkpoint — 8 October 2026 (Asia/Dubai):** Decision 047 explicitly
authorized implementation; M19 / E18–E19 / EV-022–EV-023 records an uncommitted
offline PASS and BLOCKED real multi-scene attempt. This supersedes older AS-104
status wording while preserving EV-001–EV-021 as historical records. No new merge,
GitHub CI, HAB/event or operational-performance claim. AS-105+ remains unstarted.

## Evidence standard and temporal boundary

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
[AS-104 validation](AS_104_TEMPORAL_BASELINE_VALIDATION.md#5-pr-11-integration-and-five-reference-0509-attempt--9-october-2026).
Owner review/authorization of a targeted platform-representation fix and realistic
metadata tests is the next gate; do not mutate source records or accepted caches
to bypass it. AS-104 remains uncommitted for review. No new Decision 050, commit,
push, PR or GitHub merge; only the required local ff-only integration occurred.
AS-105+ and P1 homogeneous-05.10 study NOT started. No hazard, science accuracy,
operational risk, persistence, alert or warning-lead-time claim.

**Historical upstream fix checkpoint — 8 October 2026:** Decision 048 / M20 / E20 /
EV-024 adds separately authorized source disambiguation, uncommitted for review.
AS-104 was explicitly authorized and remains uncommitted/preserved in its original
worktree; real acceptance is still BLOCKED pending upstream review/merge and a
separate rerun. Decision 047 and M19/E18–E19/EV-022–EV-023 remain there only, per
owner clarification; their numbers are reserved, not reused. Earlier AS-103
closeout authorization statements retain their historical checkpoint meaning.

**Historical Decision 049 fix checkpoint — 9 October 2026:** Decision 048 is merged via PR
#10 at `39f2aee90c727fc151886efbdea44daec0e3f9b4`. AS-104 resumed and then hit
intermittent per-asset SAS HTTP 504s. Decision 049/M22/E22/EV-026 now records a
separate, uncommitted reusable-token transport fix and fresh bounded smoke.
Decision 047/M19/E18–E19/EV-022–EV-023 and M21/E21/EV-025 stay only in the
preserved uncommitted AS-104 worktree; their bodies are not copied. Historical
EV-001–EV-024 rows remain unchanged. AS-104 acceptance is still BLOCKED pending
Decision 049 review/merge. AS-105+ and P1 homogeneous-05.10 study NOT started.

The historical probe reports and later raster-gate report transcribe the project owner's supplied factual reconstruction of completed investigations. “Directly observed” refers to those reported observations, not a new live probe performed when writing these documents. Original command logs, full STAC responses, exact experiment timestamps, and screenshots are not attached. Their absence is explicitly retained as a capture limitation.

Use these classifications: **directly observed evidence**, **provider/STAC-advertised metadata**, **inference**, **blocker**, **recommendation**, and **unverified claim**. An advertised format or grid does not prove a successful raster read. A provider recommendation is not an approved technical decision. A pending result must remain pending until a separately recorded experiment supports it.

EV-001–EV-008 index existing repository evidence. EV-009–EV-013 preserve the historical investigations. **EV-014 progresses from historical PENDING to later FG-01 PASS / READY**; both stages appear below, and the original PENDING row is preserved. EV-015 separates metadata-driven PC decoding from raster-access success. Record creation date, acquisition date, processing date, and experiment date must remain distinct.

EV-016/EV-017 retain the 6 October experiment and feature-branch status at that date. Their uncommitted/unmerged/review-pending wording is historical; **EV-018 supersedes that Git status** without changing the original experiment or its 213-test baseline.

EV-019/EV-020 and journal M17 retain the original AS-103 feature-branch acceptance state and experiment timestamp. Their uncommitted/not-merged statuses are intentional historical truth; **EV-021 / M18 supersedes that Git status** with a separately dated final review/merge checkpoint, preserving the 348-test baseline and all real-scene evidence.

## Claim index

Earlier evidence rows retain their recorded checkpoint statuses. EV-030 records
publication; EV-031 records the later PR #12 merge/closeout without rewriting
EV-027–EV-030. Their pending PR/merge instructions are historical.

| Evidence ID | Claim | Status | Metric/result | Source document | Suggested presentation use | Visual still needed? | Final validation needed? |
|---|---|---|---|---|---|---|---|
| EV-001 | Product thesis / Track 03 | Current approved product decisions | Water-quality/operations manager; monitoring/field-verification priority; two planned P0 hazards | [Decisions 001–015](../DECISIONS.md); [PRD §§1–5](../AquaSentinel_813_PRD_v1.0.md) | Problem/user/decision opening | Yes: operator-to-decision diagram | Yes for claimed operational impact; not for recorded thesis |
| EV-002 | AS-001 repository foundation | Completed engineering fact | Python 3.11, `src/` packaging, pytest/Ruff; `f878acc` | [Project State §6](../PROJECT_STATE.md); [pyproject](../../pyproject.toml) | Reproducible engineering foundation | Yes: package/setup capture | Fresh clean-environment reproduction before demo |
| EV-003 | AS-002 config/AOI | Completed engineering fact | TOML/GeoJSON validation and runtime context; `f606ac5`, `113ca44` | [Project State §7](../PROJECT_STATE.md); [runtime](../../src/aquasentinel/runtime.py) | Explicit geographic/scientific inputs | Yes: labelled Al Raha study map | Operational intake geometry remains separate/pending |
| EV-004 | AS-003 provenance | Completed engineering fact | Schema 1.0; historical 17-test project baseline; `e2baedc`, `db79260` | [Project State §§8–9](../PROJECT_STATE.md); [provenance](../../src/aquasentinel/provenance/) | Trace a future result to its source | Yes: labelled source/derived example | Real end-to-end derived hazard lineage remains future |
| EV-005 | Codex continuity | Completed recorded onboarding/handoff | AS-000C.1–8 completed; read-only audit at `779069d`; separate AS-101 authorization | [Project State §13](../PROJECT_STATE.md); [Handoff §§16–19](../HANDOFF.md) | Recoverable multi-machine/agent workflow | Yes: continuity sequence | Original full audit artifact not retained in tracked snapshot |
| EV-006 | AS-101 real Sentinel-2 search | Completed implementation and recorded experiment | AOI/date/cloud search, full pagination, deterministic candidates/provenance; PR #2 merge `1b83a73` | [AS-101 report](../AS_101_STAC_SEARCH.md) | Connect the use case to real catalog data | Yes: query-to-source diagram | Live services can change; raster usability not established |
| EV-007 | 44 candidate scenes | Directly observed catalog experiment | 44 unique products; 44/44 provenance conversions; 0.12–24.96% scene cloud; recorded 2 Oct 2026 | [AS-101 live result](../AS_101_STAC_SEARCH.md); [CDSE probe](AS_102_CDSE_ACCESS_PROBE.md) | First live-data evidence card | Yes: dated result card | Not a fixed future count; usable-water analysis pending |
| EV-008 | 97-test quality baseline | Recorded engineering validation | 97 tests passed, Ruff passed, diff check passed; 17 original tests retained | [AS-101 validation](../AS_101_STAC_SEARCH.md); [journal E09](../PRESENTATION_JOURNAL.md) | Quality/review evidence | Yes: dated test summary | Rerun before release; not scientific accuracy |
| EV-009 | CDSE reflectance offset discovery | Provider/STAC-advertised metadata; decoding inference | Scale `0.0001`, offset `-0.1`; valid DN decoding `DN * 0.0001 - 0.1` | [CDSE reflectance record](AS_102_CDSE_ACCESS_PROBE.md#reflectance-scaleoffset-discovery) | Explain why raw stored values need product semantics | Yes: sanitized metadata fields and formula | Yes: per-band metadata excerpts and decoded real sample |
| EV-010 | CDSE raster-access blocker | Observed environmental blocker; S3/OIDC route advertised | Proxy blocked live raster/header/window attempts; no full download; bounded access unverified | [CDSE access record](AS_102_CDSE_ACCESS_PROBE.md#access-route-and-blocker) | Catalog-versus-pixel-access distinction | Yes: access-boundary diagram | Yes: runtime transport and bounded read; do not infer universal provider denial |
| EV-011 | Planetary Computer STAC accessibility | Directly observed catalog evidence | Anonymous STAC READY / HTTP 200; corresponding item identified | [PC catalog result](AS_102_PLANETARY_COMPUTER_PROBE.md#directly-observed-catalog-result) | Evidence that an alternative catalog was reachable | Yes: sanitized catalog response | Raster signing/access still pending at this checkpoint |
| EV-012 | Same acquisition / different processed product | Metadata-supported inference; pixel equivalence unverified | Acquisition/platform/tile/orbit match; CDSE baseline 05.10/Aug 2024 versus PC 05.09/Apr 2023 | [Identity comparison](AS_102_PLANETARY_COMPUTER_PROBE.md#cross-provider-identity-finding) | Explain provenance during provider evaluation | Yes: comparison table | Metadata capture still needed; no pixel-equivalence claim |
| EV-013 | Planetary Computer COG delivery path | Provider/STAC-advertised metadata; viable-path inference | Nine proposed reflectance bands + SCL; B02 10 m, B05/SCL 20 m COG; host `sentinel2l2a01.blob.core.windows.net` | [PC assets/access](AS_102_PLANETARY_COMPUTER_PROBE.md#asset-inventory-and-advertised-delivery-path) | Potential route to bounded raster access | Yes: host-to-window diagram | Yes: allowlist/access, signing, header/window support, decoding |
| EV-014 | AS-102 bounded raster read | **PENDING — unverified at this evidence point** | No bounded read had yet been performed in the recorded PC stage; no DN/window result | [PC readiness](AS_102_PLANETARY_COMPUTER_PROBE.md#readiness-and-next-evidence) | Explicit remaining feasibility gate | Yes: actual tiny-window evidence after verification | **Yes; do not mark successful from catalog/COG metadata** |
| EV-014 · FG-01 | AS-102 bounded raster read — later final gate | **PASS / READY for tested PC product/path** | 3 successful bounded raster reads; 4 credential-free HTTP 200 signing operations; product XML read; metadata-driven B02/B05 decoding; **8/8 readiness gates passed** | [Later raster-gate record](AS_102_PLANETARY_COMPUTER_RASTER_GATE.md) | Show progression from catalog metadata to real bounded pixels | Yes: sanitized header/window/signing captures | Historical result reported; complete-band preprocessing, scientific suitability, and repeatability captures remain future |
| EV-015 | Metadata-driven PC reflectance decoding | Observed XML and DN samples; metadata-derived interpretation | XML 53,347 bytes; baseline 05.09; quantification 10000; offset -1000; B02 bandId 1/B05 bandId 4; `(DN - 1000) / 10000` | [XML and decoding evidence](AS_102_PLANETARY_COMPUTER_RASTER_GATE.md#product-xml-and-metadata-driven-interpretation) | Explain modern-baseline offsets with actual product metadata | Yes: XML field/band-map excerpt and sample table | Mechanics established for tested bands; aquatic suitability, quality masking, and pixel equivalence not established |
| EV-016 | Full-AOI AS-102 optical preprocessing | **PASS — implemented/validated on uncommitted feature branch** | 9 float32 bands + uint8 SCL/masks, (228,310), 20 m EPSG:32640; AOI 67,449; valid data 65,166; candidate water 10,211; valid water 7,963; AOI fraction 11.805957%, retention 77.984526%, excluded 2,248 | [Timestamped real validation](AS_102_OPTICAL_PREPROCESSING_VALIDATION.md); journal M15 | Real pixel/grid/mask evidence without hazard claims | Yes: AOI/candidate/retained/excluded map | Independent aquatic/HAB scientific validation remains future |
| EV-017 | Actual-PC lineage, verified AOI cache and quality gate | **PASS — implementation acceptance; not merged** | PC-only pixel lineage; CDSE discovery separate; SHA-256/canonical atomic cache; array/source/provenance-equivalent known-ID reload with catalog/signing/XML/raster calls blocked; 213 tests passed (97 retained), Ruff/diff check passed | [Cache/quality evidence](AS_102_OPTICAL_PREPROCESSING_VALIDATION.md); Decisions 039–045 | Reproducible, traceable inputs for future features | Yes: lineage/checksum/test card | Clean-machine/full-product demo and Git review remain pending |
| EV-018 | AS-102 final security/cache/provenance review and merge | **COMPLETE AND MERGED — 8 October 2026** | Final reviewed implementation `fe3d27046c40600010753957ee8921d57071ec48`; PR #6; merge `627b6ae8a509509dbb2d5d43bbdc6d74e0ce2aac`; 265 tests passed, Ruff/diff checks passed; canonical HTTPS/redirect protections, transient SAS containment, strict matching/asset rejection, bounded reads, conservative support and cache/provenance tamper checks; six non-blocking Rasterio warnings | [PR #6](https://github.com/Omar-Aboulwafa/aquasentinel-813/pull/6); [journal M16](../PRESENTATION_JOURNAL.md#m16--as-102-code-review-security-hardening-merge-and-closeout); committed source/tests | Reviewed/merged preprocessing and engineering reproducibility only; does NOT support HAB confirmation, chlorophyll concentration, toxin detection, water safety, desalination shutdown, warning lead time or operational risk accuracy | Yes: sanitized merge/commit/local-quality card | No configured/reported GitHub CI checks; independent science and full-product validation remain outstanding |
| EV-019 | Per-scene AS-103 candidate spectral features and numerical diagnostics | **PASS — authorized feature-branch acceptance, uncommitted** | 6 float32 arrays/masks (228,310); 7,963 valid pixels each; no denominator/nonfinite exclusions; two NDCI-like outputs below −1 retained; 491 negative-input pixels for B06 features | [Timestamped AS-103 evidence](AS_103_SPECTRAL_FEATURES_VALIDATION.md); journal M17 | Explain candidate signals and numerical support before temporal science | Yes: V18 sanitized maps | No HAB, chlorophyll concentration, toxins, species, safety, risk or lead-time claim; independent science remains future |
| EV-020 | AS-103 content identity, immediate-parent lineage and offline quality | **PASS — authorized feature-branch acceptance, not merged** | Versioned mask/five-band fingerprint; deterministic repeat; exact PC→AS-102→AS-103 registry chain; four scalar pixel checks; no access/write calls; 348 tests (265 retained +83 new), Ruff/diff pass, six existing Rasterio warnings | [AS-103 validation](AS_103_SPECTRAL_FEATURES_VALIDATION.md); [contract](../AS_103_SPECTRAL_FEATURES.md); Decision 046 | Reproducible candidate inputs for future AS-104 | Yes: V19 lineage/formula card | Code review/publication pending; no AS-104 authorization or GitHub CI/science claim |
| EV-021 | AS-103 final code review and merge | **COMPLETE AND MERGED — 8 October 2026** | Implementation `5638bc8b4ab06f235f908642f714a7cc83b35709`; PR #8; merge `b770d0561da9ac2b81ca2d4b8e784adff66ee231` at `2026-10-08T10:43:24Z` / `2026-10-08T14:43:24+04:00` Asia/Dubai; 348 tests passed, Ruff/diff checks passed; six existing non-blocking Rasterio warnings only, no new AS-103 warnings; typed model/arithmetic, inclusive denominator guards, NaN/support, consumed-content fingerprint/identity and immediate-parent lineage reviewed; real-scene evidence independently reviewed | [PR #8](https://github.com/Omar-Aboulwafa/aquasentinel-813/pull/8); [journal M18](../PRESENTATION_JOURNAL.md#m18--as-103-code-review-merge-and-closeout); committed source/tests and historical AS-103 acceptance evidence | Reviewed/merged spectral feature engineering, deterministic per-scene feature generation and reproducible lineage/identity only; does NOT support temporal anomaly, HAB confirmation, chlorophyll concentration, species/toxin identification, water safety, intake exposure, operational risk accuracy or warning lead time | Yes: V20 sanitized merge/local-quality card | No configured/reported GitHub Actions/workflow CI run or CI-success claim; independent science remains future; AS-104 NOT authorized and NOT started |
| EV-024 | Explicit PC processing-baseline source resolution and unchanged cache identity | **PASS — isolated fix offline/metadata gates; uncommitted, not merged** | 421 tests (348 retained +73 added), Ruff/diff pass, same six warnings; 5/5 frozen March references plus April target resolve at 05.09 with all eleven required assets and 0 forbidden signing/XML/raster/preprocessing/cache calls; accepted target cache retains identity/provenance/bytes and rejects 05.10 | [Timestamped fix validation](AS_102_REQUIRED_PC_BASELINE_FIX_VALIDATION.md); [plan/API](../AS_102_REQUIRED_PC_BASELINE_FIX.md); Decision 048; M20/E20 | Explain acquisition versus processing-product ambiguity and explicit failure-safe selection | Yes: sanitized ambiguity/constraint/quality card, pending | Upstream code review/merge and separate frozen AS-104 acceptance rerun; no March asset/decoding/support, temporal/HAB, operational accuracy or GitHub CI-success claim |
| EV-026 | Reusable transient PC account/container SAS transport | **PASS — offline/bounded transport smoke; UNCOMMITTED / READY FOR REVIEW** | 531 tests (421 main +110 net new), Ruff/diff PASS, six unchanged warnings; fresh March-4 05.09 all-eleven same-scope signs with 1 anonymous HTTP 200 token attempt, XML 1,024 bytes/B02 4,096 bytes via 206, zero additional acquisition for reuse; original worktree/cache hashes and stash preserved | [Timestamped validation](AS_102_REUSABLE_PC_SAS_TOKEN_FIX_VALIDATION.md); [plan](../AS_102_REUSABLE_PC_SAS_TOKEN_FIX.md); Decision 049; M22/E22 | Scoped credential reuse without changing scientific source identity | Yes: sanitized one-request/eleven-assets card; capture pending | No full processing, AS-104 acceptance, five usable histories, science/operational accuracy, availability guarantee or GitHub CI-success claim; review/merge remains next |
| EV-028 | AS-104 case-only platform consistency fix | **PASS — UNCOMMITTED / READY FOR REVIEW** | One equality predicate, 20 regression cases, 132 temporal and 663 full tests/Ruff/diff PASS; stored values/identities unchanged | [Validation §6](AS_104_TEMPORAL_BASELINE_VALIDATION.md#6-targeted-platform-case-representation-fix--9-october-2026); M24/E24 | Fix representation compatibility while preserving scientific identity | Yes: before/after predicate card; capture pending | No aliases, science change, Decision 050, publication or accuracy claim |
| EV-029 | AS-104 cached five-reference 05.09 acceptance rerun | **PASS — UNCOMMITTED / READY FOR REVIEW** | Six known-ID cache reloads/unchanged AS-103 IDs; 792–802 eligible pixels from 7,963 target support; 18 scalar checks, synthetic causal exclusion, repeat PASS; zero network | [Validation §7](AS_104_TEMPORAL_BASELINE_VALIDATION.md#7-cached-five-reference-0509-real-acceptance-rerun--9-october-2026); M25/E25 | Honest sparse temporal support and reproducible lineage | Yes: history-count/support card; capture pending | Five scenes are not statistical sufficiency; no HAB, concentration, safety, operational risk, persistence, alerts/lead time or CI-success claim |
| EV-030 | AS-104 reviewed implementation/evidence publication | **COMMITTED AND PUSHED — PR NOT YET CREATED, NOT MERGED** | Feature `09b38bd`, parent `2006df7`, 15 paths; pre-commit 663 tests/Ruff/diff PASS, six warnings; remote SHA equality/clean worktree, accepted identities/hashes/history preserved | [Publication §8](AS_104_TEMPORAL_BASELINE_VALIDATION.md#8-as-104-feature-publication--9-october-2026); M26/E26 | Separate measured acceptance from reviewable Git publication | Yes: acceptance → commit → branch → pending review diagram; capture pending | No new EO experiment, merge, GitHub CI success, statistical sufficiency or hazard/operational validation |
| EV-031 | AS-104 merged through PR #12 and formally closed | **COMPLETE AND MERGED — REAL ACCEPTANCE PASS** | Merge `472edc7`, final head `703af11`, two commits/fifteen paths, 663-test reviewed baseline, six historical warnings; preserved 18/18 scalar/causal/repeat evidence, identities/hashes and recovery | [Closeout §9](AS_104_TEMPORAL_BASELINE_VALIDATION.md#9-pr-12-merge-and-as-104-closeout--9-october-2026); M27/E27; PR #12 | Distinguish acceptance/publication/merge; disclose sparse support and authorization boundaries | Yes: milestone timeline/support/merge card; capture pending | No new scientific experiment, HAB/operational claim, statistical sufficiency or GitHub CI success; future design requires authorization |
| EV-032 | AS-105 frozen-policy offline candidate anomaly geometry | **PASS — SYNTHETIC / OWNER-RECONCILED / PUBLICATION AUTHORIZED** | 140 geometry/803 total tests, all 55 adversarial requirements and controls A–E; Ruff/diff/whitespace PASS, six existing warnings; exact threshold/family/support/polygons/lineage and protected hashes | [M28 validation](AS_105_HAB_ANOMALY_GEOMETRY_VALIDATION.md); [contract](../AS_105_HAB_ANOMALY_GEOMETRY.md); Decision 050; M28/E28 | Explainable predeclared rule, honest support and exact candidate geometry | Yes: labelled synthetic vote/threshold/round-trip card, capture pending | Real geometry metrics UNKNOWN; no real acceptance, future policy comparison, HAB accuracy, biological causation, probability/confidence/risk, alerts, persistence or CI-success claim |
| EV-033 | AS-105 M29 real geometry engineering acceptance | **PASS — OWNER-REVIEWED; NOT YET PR-MERGED** | P 802 / water 7,963; 7 candidates, 7/802=0.872818%; projected-grid candidate area 2,800 m²; one eight-connected MultiPolygon region/three pieces, F2/F4 votes; independent checks/repeat/immutability/bundle PASS; 140 focused/803 full tests | [M29 validation](AS_105_HAB_ANOMALY_GEOMETRY_VALIDATION.md#m29--real-geometry-engineering-acceptance--10-october-2026); M29/E29; external local checksummed bundle NOT tracked | Reproducible frozen candidate anomaly geometry with explicit sparse support | V23 capture pending; no screenshot claimed | No HAB/event/biological/accuracy/risk/confidence/persistence/alert/lead-time or CI-success claim; future comparative policy validation REQUIRED / NOT RUN |
| EV-034 | AS-105 PR #14 merge and formal closeout | **COMPLETE AND MERGED** | Actual merge `24a260cff130238c731f7cb62fc47eb74230b4dc`, 10 Oct 2026 06:24:09 UTC / 10:24:09 Dubai; 2 commits / 18 files; M28/M29 PASS unchanged | [PR #14](https://github.com/Omar-Aboulwafa/aquasentinel-813/pull/14); [merge closeout](AS_105_HAB_ANOMALY_GEOMETRY_VALIDATION.md#m30--pr-14-merge-and-as-105-closeout--10-october-2026); M30/E30 | Reviewed frozen-policy engineering evidence on official main | Merge/timeline/support card capture pending | Publication event only; no new scientific validation/CI claim; future policy validation REQUIRED / NOT RUN; AS-106+ and P1 05.10 NOT STARTED |
| EV-035 | AS-106 M31 offline implementation + synthetic/adversarial validation | **OFFLINE PASS; REAL NOT RUN** | 190 focused/993 full tests; six retained full-suite warnings; Ruff/diff/whitespace PASS; no EO/service network/download | [M31 validation](AS_106_PERSISTENCE_VALIDATION.md); M31/E31; Decision 051 | Reproducible recurrence, timing/denominators/regions, canonical identity, parent integrity and lineage on synthetic inputs | Synthetic timeline/denominator visual pending | No real recurrence, biological persistence, HAB/accuracy/risk/confidence or CI claim; M32–M35 NOT STARTED |
| EV-036 | AS-106 M32 predeclared metadata-only April inventory | **METADATA-ONLY PASS / COMPLETE** | 12 CDSE records / 2 post-filter / 2 exact PC 05.09 products; April 3 and April 28; 10 metadata HTTP requests, ZERO imagery | [M32 evidence](AS_106_APRIL_METADATA_INVENTORY.md); [JSON](AS_106_APRIL_METADATA_INVENTORY.json); M32/E32; Decision 051 | Every eligible date frozen before anomaly inspection; all exclusions retained; April 3 prerequisite stage gap explicit | Metadata timeline/funnel/stage card pending | Key presence is not pixel suitability; real recurrence NOT RUN; M33–M35/AS-107+/P1 05.10 NOT STARTED; future policy validation NOT RUN |
| EV-037 | AS-106 M33 exact April 3 upstream preparation + verified handoff | **PASS / COMPLETE; M34 INPUTS READY, NOT RUN** | P794 / 88 candidates / 15 regions; 88-array offline typed handoff; common contract PASS; 18/18 scalar checks; 408 focused/993 full tests | [M33 evidence](AS_106_APRIL3_UPSTREAM_PREPARATION.md); [JSON](AS_106_APRIL3_UPSTREAM_PREPARATION.json); M33/E33 | Freeze dates/policy before outcomes; prove inputs without computing recurrence | Two-date readiness/support/checksum card capture pending | No recurrence/HAB/biology/accuracy/risk/confidence/CI claim; sparse support remains; M34/M35/AS-107+/P1 05.10 NOT STARTED; future policy validation NOT RUN |
| EV-038 | AS-106 M34 frozen real recurrence engineering acceptance | **REAL ENGINEERING PASS / COMPLETE; M35 NOT STARTED** | P802/Q793/A7/B7/C0; coverage 7/7=1.0, recurrence 0/7=0.0; nine arrays/dtypes, exact timing/region/repeat/tamper/typed offline bundle PASS; 190 focused/993 full tests | [M34 evidence](AS_106_REAL_ACCEPTANCE.md); [JSON](AS_106_REAL_ACCEPTANCE.json); M34/E34 | Frozen sequence/policy and honest denominator; zero outcome retained without tuning | Seven-pixel state/denominator/timing diagram capture pending | No absence-of-HAB/biology/risk/confidence/accuracy/CI claim; M35/AS-107+/P1 05.10 NOT STARTED; future policy study NOT RUN |
| EV-039 | AS-106 M35 publication / formal closeout preparation | **PASS — CLOSEOUT READY; OFFICIAL CLOSURE EFFECTIVE ON MERGE** | PR #16–#20 verified; accepted P802/Q793/A7/B7/C0, coverage1.0/recurrence0.0; preserved IDs/fingerprints/bundle/history | [M35 record](AS_106_CLOSEOUT.md); [JSON](AS_106_CLOSEOUT.json); M35/E35 | Frozen eligible dates and zero retained without tuning; durable official closure | Final selection/support/recurrence/limits slide capture pending | Documentation only, no new science/biological/risk/confidence/CI claim; no PR/merge; AS-107+/P1 05.10 NOT STARTED; future policy validation NOT RUN |
| EV-040 | M36 AS-107 feasibility/design audit | **COMPLETE — READ ONLY** | Config/interfaces/missing policies reviewed; no real score or code | [Prior audit record](AS_107_DESIGN_FREEZE.md#m36--e36--ev-040--prior-read-only-audit-complete); M36/E36 | Freeze policy before inspecting score | Availability/evidence-strength visual proposed | Recorded retrospectively in M37; no scientific result or implementation |
| EV-041 | M37 Decision 052 design freeze | **FINAL / FROZEN DESIGN — NOT IMPLEMENTED** | Owner-approved formulas, completeness, qualification, identity/lineage and future tests | [M37 record](AS_107_DESIGN_FREEZE.md); [contract](../AS_107_HAB_RISK.md); M37/E37 | Missing is not zero; score is separate from evidence completeness | Driver/completeness layout proposed, no real-score visual | Documentation only; no real score/product/PR/merge/AS-108; M38–M40 NOT STARTED |
| EV-042 | M38 AS-107 offline implementation and synthetic/adversarial validation | **IMPLEMENTED / SYNTHETIC-ADVERSARIAL PASS** | 292 focused/1285 full tests; six existing Rasterio warnings; Ruff/diff/security/preservation PASS | [M38 evidence](AS_107_IMPLEMENTATION_VALIDATION.md); M38/E38; frozen Decision 052 | Availability and completeness are explicit; rehashed tampering rejected by regeneration | Synthetic-only driver/completeness diagram proposed, capture pending | No real score/band, biological validation, operational risk or CI-success claim; M39/M40/AS-108 NOT STARTED |
| EV-043 | M39 first real AS-107 engineering acceptance | **REAL ENGINEERING ACCEPTANCE PASS** | Watch 29.52380952380953; completeness/coverage .7/.7; exact oracle/hash/repeats/16 tamper controls/fresh sealed roundtrip/preservation PASS | [M39 report](AS_107_REAL_ACCEPTANCE.md); [JSON](AS_107_REAL_ACCEPTANCE.json); M39/E39 | Retain actual band and missing context/exposure; zero recurrence is not safe water | Driver/contribution/completeness card proposed, capture pending | Provisional only, no biological calibration/accuracy/intake completeness; M40/AS108/05.10 not started |
| EV-044 | M40 AS-107 publication / closeout preparation | **PUBLICATION / CLOSEOUT PASS — READY FOR PR** | Verified PR #22/#23/#24 ancestry/parents/trees; immutable Watch .7/.7 result; 1285 full tests PASS (104.18s), six existing Rasterio PendingDeprecationWarnings; Ruff/diff/new-file whitespace/credential/preservation PASS | [Closeout](AS_107_CLOSEOUT.md); [JSON](AS_107_CLOSEOUT.json); M40/E40 | Policy frozen before outcome; missing components explicit; closure effective on future closeout merge | Driver cards and publication-chain figure proposed, capture pending | AS-107 CLOSEOUT READY before merge, COMPLETE / CLOSED after future merge; no new science; AS-108 NOT STARTED |
| EV-045 | Historical M41 read-only feasibility/source audit | **COMPLETE; historical source-access blocker** | Seven caches and stage inventory; six blocked documentary attempts; zero EO/science | [M42 historical record](AS_108_DESIGN_FREEZE.md#historical-m41-and-numbering); M41/E41 | Source precision and missingness bound validation | Proposed audit matrix only | Recorded retrospectively during M42; M41 made no repository edits; externally verified source facts subsequently supplied by the owner |
| EV-046 | Decision 053 / M42 AS-108 historical-validation design | **FINAL / FROZEN DESIGN — NOT EXECUTED** | Fixed 5 PRE/2 EVENT/1 future POST attempt, month/area reference, explicit denominators/categories; 1285 full tests PASS (115.87s), six existing Rasterio PendingDeprecationWarnings; Ruff PASS; diff/new-file whitespace PASS | [M42 freeze](AS_108_DESIGN_FREEZE.md); [JSON](AS_108_DESIGN_FREEZE.json); M42/E42 | Freeze evaluation before new outcomes; external species/toxin separated from EO inference | Proposed two-lane timeline only | No new score/May selection/validation execution; PR/merge and M43 separately authorized; AS-201 NOT STARTED |
| EV-048 | M44 retrospective historical case study | COMPLETE WITH POST UNAVAILABLE | PRE5/5; EVENT2/2 positive; Watch1/1 scored and1/2 retained; missing POST; frozen PARTIALLY_CONSISTENT; case digest | [Report](AS_108_HISTORICAL_CASE_STUDY.md); [JSON](AS_108_HISTORICAL_CASE_STUDY.json); M44/E44 | Documented event. Observable signal. Missing POST retained. | Proposed phase strip, not captured | One retrospective month/area case; no biology/accuracy/recovery/lead-time claim; zero new EO science |
| EV-047 | M43 POST metadata inventory/deterministic selection | **COMPLETE — SELECTION UNAVAILABLE** | Six CDSE pages/26 records/four CDSE-eligible dates; earliest May3 cloud0.57%; exact PC query0; metadata digest frozen; 1285 full tests PASS (106.24s), six existing Rasterio PendingDeprecationWarnings; Ruff PASS; diff/new-file whitespace PASS | [M43 evidence](AS_108_POST_METADATA_SELECTION.md); [JSON](AS_108_POST_METADATA_SELECTION.json); M43/E43 | Keep frozen date and missingness instead of substituting a convenient scene | Proposed inventory funnel, capture pending | Metadata only; no recovery, biology, score, category, pixels or fallback; M44/AS-201 NOT STARTED |

### EV-021 final AS-103 review and merge

This later checkpoint records the owner-approved final implementation and real-scene
acceptance review, followed by verified publication/PR #8 merge. Review evidence:

- Typed model invariants (`models.py`) and feature arithmetic (`spectral.py`): PASS.
- Inclusive denominator epsilon guards and NaN/feature-support behavior: reviewed/tested PASS.
- Input fingerprint and consumed B02–B06 identity sensitivity: reviewed/tested PASS.
- Unconsumed B07/B08/B8A/B11 identity independence and timestamp-independent identity: reviewed/tested PASS.
- Exact PC→AS-102→AS-103 immediate-parent lineage and direct raw-source shortcut rejection: reviewed/tested PASS.
- M17 real-scene acceptance evidence, including independent scalar checks: review PASS.

M17's experiment began `2026-10-08T09:52:47.133486+00:00` UTC /
`2026-10-08T13:52:47.133486+04:00` Asia/Dubai. The later merge occurred at
`2026-10-08T10:43:24Z` / `2026-10-08T14:43:24+04:00` Asia/Dubai.
The scene was not rerun during merge review or this documentation closeout.
EV-019/EV-020 remain unchanged, including their historical statuses and 348-test baseline.
The preserved scene has six candidate features, 7,963 pixels each (100% parent water),
two below-−1 NDCI-like values retained/diagnosed and signed BOA preserved.

BOA is not aquatic Rrs; ndci_like is not calibrated chlorophyll; mci_like is an
analogue. Correlated NDCI-like/B05-red features are not independent biological
evidence. No event threshold, HAB/event classification, temporal baseline/anomaly,
species/toxins, safe/unsafe certification, autonomous plant action, intake exposure,
operational risk, persistence, warning lead-time accuracy or scientific accuracy is
established. AS-104 is NEXT PLANNED only, NOT authorized and NOT started.
No GitHub Actions/workflow CI run was configured/reported; local quality checks do
not imply GitHub CI success.

### EV-022 — AS-104 offline temporal engineering

**Status:** PASS — authorized implementation, uncommitted for review.
**Date:** 8 October 2026 (Asia/Dubai).
**Claim:** Causal target-ID selection, per-feature/pixel median/MAD/signed deviation,
positive-scale standardized anomaly, exact midrank, semantic target-support input
fingerprints, typed masks/counts/summaries, immediate-AS-103 multi-parent provenance
and blocked IO/immutability. 460 tests passed (348 +112), Ruff/diff PASS; six existing
Rasterio warnings. No dependency/config/cache-format/provenance-schema changes.
**Evidence:** [AS-104 plan/API](../AS_104_TEMPORAL_BASELINE.md), Decision 047,
[validation](AS_104_TEMPORAL_BASELINE_VALIDATION.md), journal M19 / E18.
**Limits:** Offline math/provenance evidence, not real multi-scene acceptance,
biological/event validation, risk, confidence/probability or warning lead time.
No commit/push/PR; AS-105+ unauthorized/unstarted.

### EV-023 — AS-104 fixed-window real acceptance blocked by provider ambiguity

**Status:** BLOCKED — real multi-scene acceptance NOT complete.
**Date:** 8 October 2026 (Asia/Dubai); actual attempt UTC
12:28:07.712335–12:28:29.564367 / Dubai 16:28:07.712335–16:28:29.564367.
**Claim:** Existing April 28 cache/AS-103 target reused (7,963 valid pixels/feature).
AS-101 returned 44 candidates; five March dates match tile 40RBN/orbit 20. The first
reference, March 4, has two PC products with the exact same acquisition/platform/
tile/orbit but baselines 05.09 and 05.10. Unchanged AS-102 exactly-one matching
raises ObservationMatchError; experiment stops before reference raster reads.
**Evidence:** [Timestamped AS-104 validation/blocker](AS_104_TEMPORAL_BASELINE_VALIDATION.md),
journal M19 / E19; stable product IDs, fixed bounds and metadata-only diagnosis.
**Limits:** Zero processed references; real support/summaries, temporal fingerprints/
ID/lineage, scalar checks and future-real-scene check NOT produced/run. No silent
selection workaround, window widening, minimum lowering, baseline mixing or mask
relaxation. Separately authorize any upstream selection-policy investigation.
No HAB/event, science accuracy or operational availability/lead-time claim.
**Visual:** V21 blocker/causal-contract card planned, no screenshot/anomaly map exists.

### EV-024 required-PC-baseline upstream fix

New metadata smoke: `2026-10-08T13:38:26.730440+00:00`–
`2026-10-08T13:38:48.970146+00:00` UTC, or
`2026-10-08T17:38:26.730440+04:00`–`2026-10-08T17:38:48.970146+04:00`
Asia/Dubai. The exact predeclared March products and accepted April product resolve
at 05.09 using the new optional constraint; no XML/rasters were accessed and no
cache was created. Separate offline loading of the accepted April cache verified
matching/contradicting constraints without altering its files or provenance.
This fixes ambiguity at metadata level only, not AS-104 real acceptance.
EV-022–EV-023 remain reserved in the untouched AS-104 worktree. All historical
EV-001–EV-021 rows remain unchanged, including EV-014 PENDING/later PASS progression.

### EV-025 — PR #10 integration and frozen AS-104 signing-access blocker

**Status:** Integration/preservation/offline PASS; real acceptance BLOCKED.
**Date:** 9 October 2026 (Asia/Dubai); exact three attempt times in validation §4.
**Claim:** Exact merged main `39f2aee90c727fc151886efbdea44daec0e3f9b4` integrated
ff-only; retained verified stash restored; four documentation conflicts reconciled;
Decision 047→048, M19→M20, E18–E20 and EV-022–EV-024 preserved without renumbering
or rewriting historical statuses. Eight temporal source/test files byte-identical;
533 tests, Ruff/diff PASS; six existing warnings. Frozen delivered-05.09 attempts
resolved March 4 product, read XML/SCL, then signing prevented completion;
last B02 signing exhausted five bounded attempts. Diagnostic observed intermittent
HTTP 504/200. Zero completed March references; accepted target 7,963 pixels/feature.
**Evidence:** [Timestamped resumed validation](AS_104_TEMPORAL_BASELINE_VALIDATION.md#4-decision-048-integration-and-resumed-frozen-acceptance--9-october-2026),
PR #10, journal M21 / E21, retained recovery/hash inventories and safety stash.
**Limits:** No real temporal support/counts/statistics/fingerprints/product/lineage,
scalar, future-scene or repeat result. Support is unknown, not measured zero;
not HAB, calibrated chlorophyll, biological/operational accuracy or GitHub CI.
**Next:** Retry identical 05.09 contract when signing is available; do not widen
bounds, reduce minimum, mix processing or relax masks. Keep changes uncommitted;
stash retained. P1 05.10 comparison and AS-105+ NOT STARTED.
**Visual:** V22 sanitized gate chronology/HTTP status card planned, no anomaly map.

### EV-026 reusable-token transport — later stage

Fresh transport experiment: `2026-10-09T06:44:49.076690+00:00`–
`2026-10-09T06:44:51.406274+00:00` UTC / 10:44:49–10:44:51 Asia/Dubai.
One token HTTP 200, eleven signs on the actual March-4 05.09 account/container,
two tiny HTTP 206 prefix/header reads, then zero extra acquisition requests for
three cache-reuse signs. Report contains safe counters/status/latency/bytes only.
No SAS credentials, product cache or full preprocessing created. EV-026 does not
supersede EV-024's historical metadata experiment; it records a new transport
stage after PR #10. EV-025 remains only in the preserved AS-104 worktree.

### EV-027 — PR #11 integration and real five-reference 05.09 acceptance attempt

**Status:** Integration/preservation/offline and AS-102/103 references PASS;
AS-104 real acceptance **BLOCKED**. Uncommitted for review.
**Date:** 9 October 2026; exact experiment UTC 07:31:08.630215–07:31:57.353103 /
Dubai 11:31:08.630215–11:31:57.353103 +04:00.
**Claim:** Exact ff-only PR #11 integration; second retained stash and external
recovery artifacts; eight temporal source/test hashes preserved. Combined suite
643 passed, Ruff/diff PASS, six existing warnings. Normal production transport
completed five predeclared actual 05.09 March AS-102/103 scenes, identical target
grid, and retained target cache identity/bytes. AS-104 target provenance guard
rejects lower-case observation `sentinel-2b` against source label `Sentinel-2B`.
Timestamps match; no temporal reduction occurred.
**Evidence:** [Validation §5](AS_104_TEMPORAL_BASELINE_VALIDATION.md#5-pr-11-integration-and-five-reference-0509-attempt--9-october-2026), M23/E23, PR #11 / 2006df7;
full safe per-scene IDs/fingerprints/statistics/support and diagnosis.
**Limits:** No real temporal distributions/arrays/masks/statistics, semantic
fingerprints/ID/lineage, scalar checks, causal future control or repeat result;
missing outputs are unmeasured, not zero. No new Decision 050, algorithm change,
cache rewrite, contract relaxation, hazard/accuracy/operational or GitHub CI claim.
**Visual:** Five-reference support table and sanitized platform-label guard card;
capture pending, no temporal anomaly screenshot.

### EV-014 evidence progression

| Stage / record date | Status | Evidence boundary |
|---|---|---|
| Historical checkpoint, recorded 6 Oct 2026 | **PENDING** | Anonymous catalog/advertised COGs only; [original report](AS_102_PLANETARY_COMPUTER_PROBE.md) remains unchanged |
| Later experiment FG-01, recorded 6 Oct 2026 | **PASS / READY** | GDAL 3.10.3 B02 64×64, B05 32×32, SCL 32×32 reads; signed XML and metadata-driven decoding; [new report](AS_102_PLANETARY_COMPUTER_RASTER_GATE.md) |

Original experiment timestamps were not supplied; report dates do not imply the experiments happened simultaneously. **At FG-01: AS-102 raster-access prerequisite READY; AS-102 NOT YET IMPLEMENTED; AS-103 NOT STARTED.** This historical state is preserved; the later EV-016/EV-017 record supports AS-102 feature-branch implementation acceptance, with AS-103 still not started at that checkpoint. EV-019/EV-020 records the subsequent separately authorized AS-103 acceptance. The SCL sample contains 353/1024 raw water-class pixels, not a final usable-water count. Exact transferred raster bytes were not measured.

No visual is claimed to exist merely because it is suggested here. A metadata inventory, 44 catalog products, and 97 passing software tests do not establish HAB detection, aquatic reflectance suitability, a safe/unsafe water decision, or operational warning lead time.

## Remaining evidence and presentation gaps

- Original probe task/command transcripts, dates/times, tool versions, sanitized STAC/asset metadata excerpts, and actual screenshots.
- CDSE raster transport/authentication and bounded range/window access; no provider-global access conclusion from the environment proxy blocker.
- The later FG-01 report now records credential-free signing, B02/B05/SCL headers/windows, and XML-based decoding. Original timestamps/commands/8-gate checklist, sanitized original XML/header/status captures still need evidence; EV-016 independently records later all-band preprocessing; do not relabel the earlier checkpoint as successful.
- Complete per-provider inventories and field provenance; no cross-provider pixel-equivalence result.
- Exact raster-transfer bytes were not measured; compressed blocks may exceed the requested pixel window. No byte-efficiency claim is supported.
- EV-016/EV-017 now records one real scene’s aligned optical arrays, mask/fraction statistics, actual-PC lineage and offline cache replay. Historical HAB/oil validation, false positives, operational demo site, full product/demo fallback and measured impact remain future evidence. EV-019/EV-020 adds candidate features only, not temporal/scientific interpretation.
- AS-102 contract/provider choice and implementation were separately authorized and recorded by Decisions 039–045 / M15. Final Git review/publication is recorded separately by EV-018 / M16 and PR #6. Presentation captures remain pending; the separate AS-103 authorization is recorded in Decision 046 / M17, not granted by this pack. EV-021 / M18 and PR #8 separately record AS-103 final review/merge. AS-104 remains NOT authorized and NOT started.

## Presentation capture rule

For every important experiment, future agents must record:

- Command/task purpose and the exact bounded method used.
- Experiment timestamp/date and timezone, separately from the report-creation date and product dates.
- Source/provider and stable catalog/collection references.
- Item/product identity, acquisition context, and processing baseline/version where relevant.
- Quantitative result, units/denominator, and whether it is observed, advertised, inferred, or unverified.
- Limitation, failure/blocker, remaining uncertainty, and authorization boundary.
- Screenshot/visual requirement, caption, capture status, and attribution/licence.
- Repository evidence file and relevant commit/PR reference when available.

Do **not** store credentials, SAS tokens, signed URLs, or secrets. Use sanitized unsigned references and metadata excerpts. Do not commit full EO scenes or runtime caches as presentation evidence.

After an evidence record exists, update the journal and affected EV entries. Preserve the old dated checkpoint when adding a later successful or failed gate; never rewrite a metadata-only stage as if it already contained pixel evidence. Scientific/provider decisions continue to be governed by the existing decision log and explicit authorization.

### EV-028 — Targeted platform case-representation consistency fix

**Status:** PASS — uncommitted for owner review. Date: 9 October 2026 (Asia/Dubai).
**Finding:** Only `_descriptor`'s platform equality changes to `.casefold()`.
No aliases, punctuation/space stripping, stored value normalization or identity
rewrite. Acquisition, lineage and every other compatibility rule are unchanged.
**Validation:** 20 added regressions; 132 temporal / 663 full tests, Ruff/diff PASS;
six historical Rasterio warnings. Reverse-case unit test isolates the predicate;
the existing lowercase observation descriptor schema remains unchanged.
**Evidence:** [Validation §6](AS_104_TEMPORAL_BASELINE_VALIDATION.md#6-targeted-platform-case-representation-fix--9-october-2026), M24/E24, source/test delta and external pre-fix patch/hash inventory.
**Limit:** Bug fix under Decision 047; no Decision 050 or new scientific result.

### EV-029 — Cached real five-reference 05.09 temporal acceptance rerun

**Status:** PASS — uncommitted for owner review. Date: 9 October 2026 (Asia/Dubai).
**Experiment:** 08:01:50.383608–08:01:51.327507 UTC /
12:01:50.383608–12:01:51.327507 +04:00. Exactly five fixed March references and
accepted April-28 target, March half-open window and minimum five. Six existing
known-ID 05.09 caches reused; unchanged AS-103 reconstruction reproduced exact
IDs; all 12 cache-file hashes preserved. Zero network attempts or raster writes.
**Result:** Six features each have target support 7,963. Baseline/z/rank counts
792/802/801/801/801/797; insufficient counts 7,171/7,161/7,162/7,162/7,162/7,166.
Zero MAD/numerical rejection counts zero. 18/18 independent scalar checks,
synthetic future addition/mutation exclusion, deterministic repeat and input
immutability PASS. Target-first/R1–R5 immediate parents and full upstream lineage.
**Product:** `temporal:e814b0574ab30d1841778ee3c5005ffcb313ab42473c41acc028f0a9f7804a8b`.
**Evidence:** [Validation §7](AS_104_TEMPORAL_BASELINE_VALIDATION.md#7-cached-five-reference-0509-real-acceptance-rerun--9-october-2026), M25/E25, complete safe JSON distributions/summaries/fingerprints/parents/scalar records.
**Limit:** Engineering acceptance only; rank is not probability/confidence/
severity and five observations are not statistical sufficiency. No aquatic Rrs,
HAB, concentration, species/toxins, safety, intake risk, persistence, alert,
warning lead-time or GitHub CI-success claim. Synthetic control is not a real
future observation. M23/E23/EV-027 remains historically BLOCKED; no publication,
AS-105+ or P1 homogeneous-05.10 experiment.

### EV-030 — AS-104 implementation and accepted evidence committed and pushed

**Status:** COMMITTED AND PUSHED for PR review; PR NOT YET CREATED, NOT MERGED.
**Date:** 9 October 2026 (Asia/Dubai), after M25 acceptance. Git commit
12:50:47 +04:00; remote publication verified by tracking-ref fetch at
12:52:09 +04:00. Exact push-completion second is not recorded.
**Publication:** Branch `feature/as-104-temporal-baseline`; feature commit
`09b38bd9c312470e948b1f17165ec5335cfc149d`, parent/base
`2006df7a70a4f48c66933aed96f4464d8d03084e`, message
`feat: implement AS-104 temporal baseline`, exactly **15 paths**. Pushed to
`origin/feature/as-104-temporal-baseline`; SHA equality/upstream/clean worktree
verified. No cache, credentials, external recovery or temporary scripts committed.
**Validation:** Before feature commit, 663 tests/Ruff/diff PASS with six existing
Rasterio warnings. M25/E25/EV-029 real acceptance, scalar 18/18, synthetic causal
and repeat checks PASS; all twelve cache hashes and six AS-103 IDs unchanged.
**Evidence:** [Publication §8](AS_104_TEMPORAL_BASELINE_VALIDATION.md#8-as-104-feature-publication--9-october-2026), M26/E26 and exact Git commit/remote metadata.
**Limit:** No new EO processing or scientific values. M23/E23/EV-027 remains
BLOCKED, M24–M25/E24–E25/EV-028–EV-029 remain acceptance-time PASS with original
stop states. Roughly 10% support is not failure/statistical sufficiency; small
positive scales can yield large z. No Decision 050, merge, GitHub CI success,
AS-105+ or P1 05.10 study. Review published commit and open PR only when authorized.

### EV-031 — AS-104 PR #12 merge and formal closeout

**Status:** AS-104 COMPLETE AND MERGED; real acceptance PASS; no unresolved AS-104
P0 blocker. Known scientific/coverage limitations remain documented.
**Date:** 9 October 2026, **2026-10-09T13:26:08+04:00 Asia/Dubai** /
**2026-10-09T09:26:08Z** merge; distinct from M25 acceptance and M26 publication.
**Merge:** PR #12, title `feat: implement AS-104 temporal baseline`; base `main`
at `2006df7a70a4f48c66933aed96f4464d8d03084e`, head `feature/as-104-temporal-baseline` at
`703af1176aeaf9ba38d31c53648907c3b1792aec`, merge `472edc737847dc8581290a372c5da28f71fc48f0`. Two commits/fifteen changed
paths: implementation `09b38bd9c312470e948b1f17165ec5335cfc149d` plus publication docs `703af1176aeaf9ba38d31c53648907c3b1792aec`.
**Evidence:** [Merge/closeout §9](AS_104_TEMPORAL_BASELINE_VALIDATION.md#9-pr-12-merge-and-as-104-closeout--9-october-2026), M27/E27 and verified Git merge metadata.
**Validation:** Final pre-merge 663 tests, Ruff/diff PASS, six existing Rasterio
warnings; accepted scalar 18/18, synthetic causal and repeat PASS. Temporal
product/fingerprint, eligible counts and all accepted AS-102 cache hashes /
AS-103 identities are preserved. This docs-only closeout does not rerun EO.
**Limit:** About 10% five-history support is retained, not hidden or relaxed.
Five observations are not statistical sufficiency; small positive scales can
yield large z. Rank is not probability/confidence/severity. No HAB/bloom,
chlorophyll, species/toxins, safety, intake risk, persistence, alerts, lead-time
or GitHub CI-success claim. EV-027 blocker, EV-028 fix, EV-029 acceptance and
EV-030 PR-pending publication remain historical. No Decision 050.
**Next:** Owner review of next milestone/AS-105 design before implementation;
separate authorization required. Both safety stashes/recovery artifacts retained;
AS-105+ and P1 homogeneous 05.10 NOT STARTED. No closeout PR or new merge in this task.

### EV-032 — AS-105 M28 offline geometry implementation

**Date/status:** Offline implementation 9 October 2026; owner-review clarification
10 October 2026 (Asia/Dubai), same Decision 050 / M28 / E28. PASS, synthetic only;
feature publication authorized, PR review follows Git/remote verification. Base `4e322df`.

**Observed engineering evidence:** 140 geometry cases/803 full tests PASS,
Ruff/diff and new-file whitespace PASS; six historical Rasterio warnings only.
Controls A–E cover deterministic repeat, valid irrelevant mutation, consumed-bit
identity/classification changes, eight-neighbour components and exact polygons.
All 55 mandated adversarial requirements pass, including output/provenance/policy
tampering and blocked IO/upstream paths. Protected source/tests/cache/handoff
hashes and safety stashes/recovery material remain unchanged.

**Evidence:** [offline validation](AS_105_HAB_ANOMALY_GEOMETRY_VALIDATION.md) and
[frozen contract](../AS_105_HAB_ANOMALY_GEOMETRY.md). Verified external AS-104
handoff is prerequisite evidence only, not a real geometry experiment.

**Limit:** Real candidate counts/fraction/area/regions/fragmentation/votes UNKNOWN;
real acceptance and future policy comparison NOT RUN, future checkpoint not
created. Rank is not probability/confidence/significance/severity; families are
not independent or biological proof. No HAB/concentration/species/toxins/safety/
intake-risk/persistence/alert/lead-time or GitHub CI-success claim. AS-106+ and
P1 05.10 NOT STARTED. EV-001–EV-031 remain historical and unchanged.

EV-032 owner-review addendum, 10 October: unchanged float32 0.90 policy has
coarse n=5 empirical-rank granularity; four new synthetic regressions PASS.
No smooth population-percentile, significance/probability/confidence/severity
claim. Predeclared future history-depth sensitivity is required and NOT RUN;
M29 retains the accepted minimum-five parent. This is the same checkpoint,
not new real geometry evidence.

### EV-033 — AS-105 M29 real geometry engineering acceptance

**Date/status:** 10 October 2026 (Asia/Dubai); first execution
05:45:15.046037–05:45:15.173566 UTC / 09:45:15.046037–09:45:15.173566 +04:00;
acceptance completed 05:45:46.711968 UTC / 09:45:46.711968 +04:00.
Owner review PASS; later documentation publication is separate. M28 implementation
`57100b2e53e941f3a7fdfdfc40b61d2b4043c0e5` is COMMITTED / PUSHED; no PR/merge timestamp, feature NOT YET PR-MERGED.

**Identity:** `hab_geometry:70876fbcb25e8a37abaa238a59e1da32fec9066792e6239db68e284b7bd18682`, input `c50d9f6300060ab9f194c1a0b8808de340eb53326268a52ef083ad7f994b2bc5`, output `ff976ec800ec2dfc966e4f373dd3f2442938a06a10254dd4ea7a86280dd0a765`,
version as105-v1; immediate parent `temporal:e814b0574ab30d1841778ee3c5005ffcb313ab42473c41acc028f0a9f7804a8b`. Grid EPSG:32640, 20 m, 310×228,
ID `88d76cf6265d9e0fa2802ed26324c02275e74721d4eb5b597cc9884a6d27aeec`.
**Result:** P **802** / target water **7,963**, coverage **10.071581%**;
C **7**, fraction **7/802 = 0.872818%**; descriptive C/water **0.087907%**;
**projected-grid candidate area 2,800 m² / 0.0028 km²**. One eight-connected
region, one MultiPolygon, three four-connected pieces; F2/F4 agreement,
family pixel counts **0,7,0,7,0**. Not three independent regions or biological proof.
**Granularity:** no supported float32(.90); observed .0/.2/.4/.6/.8/1 ranks made
>=float32(.90) equivalent to rank==1 for this parent only. Another four-below/
one-exact-tie five-history pixel can attain .90; unchanged algorithm/threshold.
Future history-depth sensitivity REQUIRED / NOT RUN.

**Engineering evidence:** exact handoff/parent/scene validation; independent
literal feature/family/P/C masks, labels/seeds/count, determinant area and exact
polygon rasterization PASS; repeat **27/27**, parent immutability **61/61**, external
bundle read-back/checksum audit PASS; zero real connection/HTTP/upstream/cache-load
attempts, no tuning/repository edits during execution. Focused **140**, full **803**
tests PASS, Ruff/diff PASS, six existing Rasterio warnings only. Protected handoff,
12 caches, both safety stashes and 13 recovery artifacts unchanged.
**Evidence:** [full M29 tables, region, timestamps and hashes](AS_105_HAB_ANOMALY_GEOMETRY_VALIDATION.md#m29--real-geometry-engineering-acceptance--10-october-2026);
M29/E29; `/workspace/aquasentinel-acceptance/as105/m29/`, external local evidence
artifact **NOT tracked in Git**, four read-only files with exact recorded hashes.
**Limits:** M29 establishes reproducible real candidate spectral anomaly geometry only. It does NOT establish confirmed HAB/bloom, chlorophyll concentration, species/toxins, biological causation, sensitivity/specificity/accuracy/false-positive rate, event agreement, persistence, risk/confidence, water safety, intake exposure, alert or warning lead time. No comparison with the historical April event was performed. Rank is not probability/confidence/significance/severity; policy families are not statistically independent. Five observations are not statistical sufficiency.
**Publication correction:** Owner confirmed verified red_edge_red_ratio rank-.4/.6 counts **240/92**, correcting the earlier chat transcription **238/93**; acceptance JSON hash unchanged, no rerun.
**Next:** Owner review of M29 documentation/publication followed by PR preparation;
future comparative policy validation REQUIRED / NOT RUN; no PR/merge, AS-106+
or P1 05.10. Decision 050 unchanged, no Decision 051. EV-001–EV-032 retained.

### EV-034 — AS-105 PR #14 merge and formal closeout

**Date/status:** 10 October 2026; **AS-105 COMPLETE AND MERGED**, M30 / E30 / EV-034.
PR #14 “feat: implement AS-105 HAB anomaly geometry” merged into `main` at
**2026-10-10T06:24:09Z / 2026-10-10T10:24:09+04:00 Asia/Dubai**.
Actual merge `24a260cff130238c731f7cb62fc47eb74230b4dc`; base before merge
`4e322df220f8cab2805fccf9a2b32dd825f29218`; head
`feature/as-105-hab-anomaly-geometry`, final head/M29 documentation commit
`1ac9fab9db48cca5625ead20e7133c79101a46d8`; implementation
`57100b2e53e941f3a7fdfdfc40b61d2b4043c0e5`. Two commits, 18 files,
3,315 additions / 30 deletions. No provisional merge SHA is used.

**Evidence:** [verified merge record](AS_105_HAB_ANOMALY_GEOMETRY_VALIDATION.md#m30--pr-14-merge-and-as-105-closeout--10-october-2026)
and [PR #14](https://github.com/Omar-Aboulwafa/aquasentinel-813/pull/14).
M28 synthetic/adversarial PASS and M29 real engineering PASS remain separate
historical records. EV-033 retains its original pre-merge checkpoint text.
Decision 050 is merged and unchanged; no Decision 051. The accepted product,
input/output fingerprints, 802/7,963 support, seven candidates, projected-grid
2,800 m² / 0.0028 km² area, one region/three parts and corrected rank counts
240/92 remain unchanged. No real processing rerun.

**Preservation/limits:** Source/tests byte-identical to official main; external
handoff/M29 bundle remain read-only, twelve accepted cache hashes unchanged,
both safety stashes and recovery artifacts retained. Local 803-test baseline,
Ruff/diff PASS and six existing Rasterio warnings do not establish CI success
or scientific accuracy. Scientific guardrails, sparse support and empirical
rank limitations remain intact; no HAB/event/biological/risk/operational claim.
Future comparative policy validation **REQUIRED / NOT RUN** across the original
predeclared dimensions. Merge/support-boundary visual capture pending.

**Next:** Owner review of the next milestone / AS-106 design before implementation.
AS-106+ is not authorized and **NOT STARTED**; P1 05.10 **NOT STARTED**.
This documentation closeout creates no PR and performs no merge.

## Historical AS-106 design freeze and future evidence reservations — 10 October 2026

Decision 051 is owner-approved/frozen design only; [specification](../AS_106_PERSISTENCE.md).
This is not AS-106 implementation or real validation evidence. Historical
EV-001–EV-034 retain their original bodies and dates. No completed EV-035–EV-039
evidence record or implementation-validation placeholder document is created.

| Reserved future IDs | Scope | Current status |
|---|---|---|
| M31 / E31 / EV-035 | Offline implementation + synthetic/adversarial validation | NOT STARTED; separate implementation authorization |
| M32 / E32 / EV-036 | Metadata-only April inventory; network metadata only, NO imagery | NOT STARTED |
| M33 / E33 / EV-037 | Separately authorized missing April AS-102→103→104→105 preparation/handoffs | NOT STARTED |
| M34 / E34 / EV-038 | Offline real AS-106 engineering acceptance | BLOCKED ON FUTURE DATA PREPARATION / NOT STARTED |
| M35 / E35 / EV-039 | Owner review/publication/merge/closeout | NOT STARTED |

Existing accepted dates are March 4/9/14/24/29 and April 28; no verified earlier-
April cache or complete eligible inventory. Freeze every eligible April acquisition
before anomaly inspection, unchanged 05.09/grid/tile/orbit/cloud contracts and
the same accepted March references. Sparse/zero-candidate dates are not removed.
No recurrence measurement or biological/risk/confidence claim is supplied here.
AS-107+ / P1 05.10 NOT STARTED; AS-105 policy validation REQUIRED / NOT RUN.

### EV-035 — AS-106 M31 offline implementation and synthetic/adversarial validation

**Date:** 10 October 2026 (Asia/Dubai). **Status:** OFFLINE ENGINEERING PASS.
**Branch/base:** `feature/as-106-persistence` / `57185444f0cc963cc899a25cd8179d7a31f12119`.
**Evidence:** [M31 validation](AS_106_PERSISTENCE_VALIDATION.md); M31/E31;
Decision 051 unchanged. 190 focused / 993 full tests, Ruff/diff/new-file whitespace
PASS. No focused/new warnings; six retained Rasterio warnings in full suite.
Twelve randomized synthetic sequences have independent per-pixel scalar checks;
rehashed tampering, immutable parents, exact timing/medians, canonical identity,
AS-105-only immediate lineage and no-IO/upstream-extraction guards PASS.
No accepted real artifacts consumed for recurrence; hashes/modes retained.
No EO network/download, real April output, biological/risk/confidence/accuracy,
GitHub CI success, PR or merge claim. Real acceptance BLOCKED ON FUTURE DATA
PREPARATION; M32/E32/EV-036 through M35/E35/EV-039 NOT STARTED. Their original
historical design reservations above remain preserved. Future AS-105 policy
validation NOT RUN; AS-107+ / P1 05.10 NOT STARTED. Synthetic visual capture pending.

### EV-036 — AS-106 M32 predeclared metadata-only April inventory

**Date:** 10 October 2026 (Asia/Dubai). **Status:** METADATA-ONLY PASS / COMPLETE.
**Branch/base:** `data/as-106-april-metadata-inventory` / `723e13a900dba30b73a8a2da39df1d984233a2f4`
(PR #17 merged M31). **Evidence:** [normalized JSON](AS_106_APRIL_METADATA_INVENTORY.json)
and [M32 record](AS_106_APRIL_METADATA_INVENTORY.md); M32/E32; Decision 051 unchanged.
12 CDSE records/2 pages → 2 post-filter candidates → 2 unique exact PC 05.09
products with all 11 required keys → April 3 and April 28 sequence, chronologically.
Ten excluded CDSE records retain exact tile/orbit reasons. Two PC searches return
six context items; no ambiguous 05.09 match. April 28 reconciles to accepted target.
Selection SHA-256: `570792066c1997b9a403249d994c4e7367bf2f1dafc6473b6e30df20cd6481d5`; operational timestamps and local stage availability
excluded. Selection completed before outcome-independent availability audit.

Only `stac.dataspace.copernicus.eu` and `planetarycomputer.microsoft.com`
contacted: 10 metadata HTTP requests, 3 logical searches, 4 complete search pages;
ZERO asset requests / imagery bytes, no signing, href persistence or EO processing.
April 3 all AS-102/103/104/105 missing; April 28 all present through accepted
identities/evidence. Missing-stage audit is local, not provider-wide absence;
accepted AS-103 descriptors do not imply a new disk cache. Future April 3 M33
work is separate; M33/M34/M35 NOT STARTED, real AS-106 acceptance NOT RUN.
993 tests PASS, Ruff/diff/new-file whitespace/credential checks PASS; six retained
Rasterio warnings. Protected source/tests, caches/handoff/M29, both safety stashes
and external recovery files retained byte-identical with modes unchanged.
No raster usability, biological persistence/HAB/accuracy/risk/confidence or CI
claim. AS-107+ / P1 05.10 NOT STARTED; future AS-105 policy validation NOT RUN.
Recommended metadata-only timeline/exclusion funnel/stage card capture pending.
No new Decision 052, PR or merge; M32 evidence publication is not M35.

### EV-037 — AS-106 M33 April 3 upstream preparation and verified handoff

**Date:** 10 October 2026 (Asia/Dubai). **Status:** UPSTREAM PREPARATION + VERIFIED
HANDOFF PASS / COMPLETE. Base `200affdb7fb6f8801744a192511e4200cc0d100d`; branch
`data/as-106-april3-upstream-preparation`. M31/M32 merged; Decisions 050/051 frozen.
Only exact April 3 at PC 05.09 newly prepared through unchanged AS-102→103→104→105.
M32 selection/digest preserved; five accepted March spectral IDs reproduced offline.
April 28 common-contract comparison PASS before AS-105; accepted artifacts intact.

Valid water 6,096; temporal support 784/794/793/793/793/789, zero MAD 0; AS-105 P794,
88 candidates (11.083123% of P), 15 regions / 35,200 m². Independent scalar 18/18,
causal/repeat/candidate/rasterization/parent integrity checks PASS. External typed
88-array bundle files 0444/directory 0555, checksum verified. Fresh offline April 3
and historical April 28 reconstruction PASS with zero network/public extraction/
recurrence. Temporary adapter list/tuple and historical display-field mismatches
corrected without production changes; failed checkpoint preserved outside Git.

[M33 evidence](AS_106_APRIL3_UPSTREAM_PREPARATION.md) and
[JSON](AS_106_APRIL3_UPSTREAM_PREPARATION.json) contain exact IDs/fingerprints/region
statistics, bounded-network audit, file hashes/modes, quality and preservation.
408 focused/993 full tests, Ruff/diff/whitespace/credentials PASS; six existing
Rasterio warnings. No source/test/config/dependency change or CI success claim.
M34 INPUTS READY is not M34 acceptance; recurrence NOT RUN. M34/M35/AS-107+/P1
05.10 NOT STARTED; future AS-105 policy validation NOT RUN. ~13% support/shared
five-history limits retained; no HAB/biology/accuracy/risk/confidence/alert claim.
No Decision 052, PR or merge. Recommended readiness/support/checksum visual
capture pending, no screenshot created. Historical EV-001–EV-036 bodies retained.

### EV-038 — AS-106 M34 first real recurrence engineering acceptance

**Date:** 10 October 2026 (Asia/Dubai). **Status:** REAL ENGINEERING ACCEPTANCE
PASS / COMPLETE; AS-106 not fully closed; M35 NOT STARTED. Base PR #19 merge
`4cde14ee448079163c2a08f3951f8dac294f8dac`, branch `data/as-106-real-acceptance`.
Four accepted typed parents verified from immutable local artifacts; exactly
April 3→April 28 target; common grid/context/frozen policy PASS before production.

**P802 / Q793 / A7 / B7 / C0**; candidate-history coverage 1.0; recurrence fraction
0.0; seven streak-one pixels; exact previous-valid gap 2,160,008,000,000 µs at Q.
One unchanged target region: support7 / overlap0, recurrent spans None. No observed
same-pixel recurrence at history-supported target candidates; no tuning/date change.

[M34 evidence](AS_106_REAL_ACCEPTANCE.md)/[JSON](AS_106_REAL_ACCEPTANCE.json) record
exact product/fingerprints/provenance, direct nine-array/dtype/time/global/region
oracles, creation-time exclusion, same/reverse repeats, immutability/non-aliasing,
seven tamper controls including rehash, and four-file read-only bundle hashes.
Fresh typed offline bundle roundtrip PASS; zero scientific network/public upstream
attempts. Existing validator internal regeneration is integrity only.
190 persistence/993 full tests PASS, six existing Rasterio warnings; Ruff/diff/
whitespace/credentials PASS. All prior caches/handoffs/M29/M32/M33/stashes/recovery
hashes/modes intact; source/test/config/dependencies unchanged. Decisions 050/051
scientific bodies unchanged, no Decision 052, PR, merge or GitHub CI claim.

History coverage 7/7 is distinct from sparse April 3 upstream coverage; long gap,
exact-pixel movement sensitivity and shared five March histories remain limitations.
No biological/event/absence-of-HAB/probability/confidence/risk/safety/accuracy claim.
M35/AS-107+/P1 05.10 NOT STARTED; future AS-105 policy validation NOT RUN. State/
denominator/timing visual capture pending, no screenshot created. EV-001–EV-037
historical bodies preserved. M34 evidence commit/push is not M35 formal closeout.

### EV-039 — AS-106 M35 publication / closeout preparation

**Date:** 10 October 2026 (Asia/Dubai). **Status:** PUBLICATION / CLOSEOUT PASS —
READY FOR PR; official closure pending this branch's merge. Prepared on
`docs/as-106-closeout`, baseline PR #20 merge
`82e30c00a30ed893ad47c44c5a1e363661370d35`. M31–M34 COMPLETE/MERGED; Decision 051
FINAL/FROZEN/MERGED via PR #16, original scientific text unchanged, no Decision 052.

[M35 record](AS_106_CLOSEOUT.md)/[JSON](AS_106_CLOSEOUT.json) consolidate exact
accepted product/fingerprints/digest, April3→April28 sequence, P802/Q793/A7/B7/C0,
7/7 history coverage, 0/7 recurrence, seven singleton streaks and exact observation
gap. “No same-pixel candidate recurrence was observed among the 7 target candidate
pixels with valid prior observational history.” M34 engineering integrity PASS
referenced, not rerun; local bundle hashes/modes checked read-only and unchanged.

Metadata froze every eligible date before recurrence inspection; April 3 had 88
candidates, April 28 had 7, recurrence0 retained without changing dates/thresholds/
family/connectivity/spatial rules. Biological absence/persistence/HAB/risk/confidence/
probability/water-safety/accuracy claims remain unsupported. Exact pixels/two dates/
long gap/shared five histories/sparse upstream support limits disclosed.

Only eight docs paths change; accepted artifacts/evidence, source/tests/config/
dependencies, stashes and recovery preserved. Final M35 quality/security gates in
closeout evidence; no new science/data network, PR, merge or GitHub CI success.
The future merge itself makes AS-106 COMPLETE/CLOSED and M35 COMPLETE/MERGED;
no extra post-merge SHA edit required. AS-107 separately designed/authorized,
NOT STARTED; future AS-105 policy validation NOT RUN; P1 05.10 NOT STARTED.
Historical EV-001–EV-038 bodies retained; presentation visual capture pending.

### EV-040 — M36 prior AS-107 read-only feasibility/design audit

10 October 2026 (Asia/Dubai); M36/E36 COMPLETE. Recorded retrospectively from the
completed owner-reviewed audit in [M36 record](AS_107_DESIGN_FREEZE.md#m36--e36--ev-040--prior-read-only-audit-complete).
Current typed AS-105 family availability/evidence and AS-106 regional recurrence
can support future scoring; AS-104 remains an integrity witness. Audit compared
missing policies and recommended explicit regional/completeness/qualification rules.
No real score, outcome-based formula selection, implementation or scientific product.

### EV-041 — M37 AS-107 Decision 052 owner-approved design freeze

10 October 2026 (Asia/Dubai); M37/E37 FINAL / FROZEN DESIGN — NOT IMPLEMENTED.
[Contract](../AS_107_HAB_RISK.md), Decision 052 and [M37 evidence](AS_107_DESIGN_FREEZE.md)
freeze formulas, weights/availability, evidence_completeness, provisional status,
continuous bands, 0.50 administrative interpretation, regions/site/drivers,
monitoring/witness/provenance/identity/serialization and future adversarial gates.
No real score or expected band; 0.70/0.55 coverage are config consequences only.
Correlation/missing-input/scientific boundaries remain explicit. Actual regression
and preservation gates are in M37 evidence, not proof of unimplemented risk science.
Earlier evidence bodies preserved; M38/E38/EV-042, M39/E39/EV-043 and M40/E40/EV-044
are future reservations only. No PR/merge/implementation/scientific product or
AS-108 work; policy validation/05.10 remain unrun. Proposed visuals are not created.

### EV-042 — M38 AS-107 offline implementation / synthetic-adversarial validation

10 October 2026 (Asia/Dubai); M38/E38 IMPLEMENTED / SYNTHETIC-ADVERSARIAL PASS.
[M38 record](AS_107_IMPLEMENTATION_VALIDATION.md) contains actual quality results,
frozen-policy implementation, exact denominators, explanation/qualification, typed
parent-chain/provenance/identity, adversarial rehash and no-side-effect evidence.
No real AS-105/106 handoff was loaded or scored; no real score/band/prediction.
Historical M36/M37 / EV-040/041 remain unchanged. Decision 052 scientific body
preserved; no Decision 053. M39/EV-043 and M40/EV-044 remain future reservations,
NOT STARTED; AS-108, policy study and 05.10 NOT STARTED/NOT RUN. Publication on
feature/as-107-hab-risk is for owner review; M38 creates no PR and performs no merge.

### EV-043 — M39 first real frozen-policy observational screening

Under the frozen AS-107 observational screening policy, the April 28 validation AOI produced a **Watch observational screening score of 29.52380952380953**, with evidence completeness **0.7** and component coverage **0.7**. Environmental context and intake exposure remain unavailable. The result is provisional observational screening, not confirmed HAB or operational water-safety determination.

Full integer denominators, binary64 values, explanations, lineage, hashes/modes and independent controls are in [M39 MD](AS_107_REAL_ACCEPTANCE.md) / [JSON](AS_107_REAL_ACCEPTANCE.json). One unchanged seven-pixel region, F2/F4 evidence, persistence 0/7 available; no outcome tuning or EO retrieval. First immutable result, exactly three public calls, 13 ordinary/3 rehashed rejection controls and fresh-process sealed roundtrip PASS. M40/AS108 separately authorized only; no PR/merge or 05.10 experiment. Historical EV-001–EV-042 bodies remain intact.

### EV-044 — AS-107 M40 publication / closeout preparation

M40 / E40 verifies the merged freeze → implementation → accepted-real-evidence chain
and publishes the unchanged Watch = 29.52380952380953, completeness/coverage .7/.7
result. [Closeout MD](AS_107_CLOSEOUT.md) and [JSON](AS_107_CLOSEOUT.json) record
exact denominators, immutable fingerprints, the anti-outcome-tuning chronology,
protected hashes/modes/stashes and 1285 full tests PASS (104.18s), six existing Rasterio PendingDeprecationWarnings; Ruff/diff/new-file whitespace/credential/preservation PASS.
M39 / EV-043 remains historical and byte-identical. No scientific rerun/retrieval.
Before future closeout merge: AS-107 CLOSEOUT READY. The future closeout merge
itself establishes AS-107 COMPLETE / CLOSED; no future merge SHA is invented.
AS-108, future AS-105 policy validation and P1 05.10 are NOT STARTED. No Decision 053.

### EV-045 — Historical M41 read-only feasibility/source audit

Recorded retrospectively during M42 to preserve chronological journal continuity.
M41 changed no repository files, froze no design and ran no EO science. Its source
requests were blocked and recommendation was REVISE pending verification/scope.
Owner-supplied outside-Codex verification subsequently resolved that blocker for
M42; do not rewrite the original checkpoint as if access succeeded.

### EV-046 — Decision 053 / M42 design freeze

[AS-108 contract](../AS_108_HAB_HISTORICAL_VALIDATION.md), [freeze evidence](AS_108_DESIGN_FREEZE.md)
and [machine-readable contract](AS_108_DESIGN_FREEZE.json) freeze a retrospective
observational-consistency case only: month/area reference, descriptive PRE, both
April observations and one future earliest metadata-compatible May attempt.
1285 full tests PASS (115.87s), six existing Rasterio PendingDeprecationWarnings; Ruff PASS; diff/new-file whitespace PASS. No execution, present consistency classification, new score or
biological accuracy result. Owner review is next; PR/merge and M43 need separate
authorization. Decision 054 absent; AS-201 NOT STARTED.

### EV-047 — M43 POST metadata inventory and selection

Six validated CDSE pages retain all 26 May AOI records and distinct keys; four pass
CDSE eligibility. Frozen earliest May3 `S2A_MSIL2A_20230503T064621_N0510_R020_T40RBN_20240903T135841` yields zero items in
the unchanged exact PC resolver query. Selection **UNAVAILABLE**, PC ID/baseline
null; later May dates not substituted or PC-queried. Digest `df487999defada56023a7e76be69c507b2b1ff11d81de1480737eca86a1ad4de`.
[M43 evidence](AS_108_POST_METADATA_SELECTION.md) and [JSON](AS_108_POST_METADATA_SELECTION.json)
retain page membership, eligibility, cardinality and request accounting.
1285 full tests PASS (106.24s), six existing Rasterio PendingDeprecationWarnings; Ruff PASS; diff/new-file whitespace PASS. Source/tests/config/dependencies, frozen Decisions050–053, accepted
AS-107/M42 evidence and protected artifacts remain unchanged. No new pixels/science
or observational-consistency category. Owner review and separate authorization
required; M44 and AS-201 NOT STARTED.

### EV-048 — M44 retrospective case-study reporting over accepted evidence

Both accepted event-month observations have frozen-policy candidate evidence;
April28 retains its accepted Watch result. POST no exact compatible PC05.09 match
is preserved without substitution. Frozen Decision053 evaluates to
PARTIALLY_CONSISTENT; required context is incomplete. Five PRE descriptive records
are not biological negatives; April3 scoring remains unavailable.
M44 is reporting arithmetic over accepted artifacts only; no EO/provider/documentary
requests or scientific rerun. Case JSON retains exact identities, fingerprints,
source locators, denominators, predicate trace and semantic digest. No new Decision054.
AS-108 P0 retrospective case study complete with POST unavailable; publication
requires owner review, separate PR/merge authorization. AS-201 NOT STARTED.

## AS-201 historical audit and design-freeze evidence — recorded at M47

| ID | Checkpoint | Status | Evidence / presentation use | Limitation |
|---|---|---|---|---|
| EV-049 | M45/E45 read-only feasibility predecessor | COMPLETE — HISTORICAL | [Accepted predecessor facts](AS_201_DESIGN_FREEZE.md); documentary/metadata same-track sequence | Did not write repository; no pixels/petroleum/detection |
| EV-050 | M46/E46 access/representation predecessor | COMPLETE / PASS — HISTORICAL | [Header/XML gate summary](AS_201_DESIGN_FREEZE.md); raw GRD access, provider defects and failed approaches | No SAR processing; representative VV XML and one VH header, not universal metadata/VH LUT proof |
| EV-051 | M47/E47 Decision054 | FINAL / FROZEN DESIGN / NOT IMPLEMENTED | [Contract](../AS_201_SENTINEL1_RETRIEVAL.md); [MD](AS_201_DESIGN_FREEZE.md); [JSON](AS_201_DESIGN_FREEZE.json); exact source/coverage/security digest | No candidate detected; AS201 implementation/AS202 NOT STARTED; proposed visuals only |

### EV-052 — AS-201 M48 raw-GRD implementation / offline engineering validation

- **M48 / E48**, Decision 054 implementation; Decision 055 absent.
- Sources: [MD](AS_201_IMPLEMENTATION_VALIDATION.md) and
  [JSON](AS_201_IMPLEMENTATION_VALIDATION.json), preserved WIP and follow-up Git diff.
- Proves: exact frozen source engineering, metadata support/missingness,
  deterministic identities/provenance, bounded header/XML and transport controls.
- Does not prove: live six-source availability, pixel validity, calibrated
  backscatter, oil candidate detection, petroleum composition or operational safety.
- Scientific requests/compute/pixel reads/bytes: zero. AS-202 NOT STARTED.
- Publication: feature branch for owner review; no M48 PR/merge performed.

### EV-053 — AS-201 M49 live six-source acceptance attempt

- **M49 / E49**; Decision 054 unchanged, Decision 055 absent.
- Sources: [MD](AS_201_LIVE_ACCEPTANCE.md) / [JSON](AS_201_LIVE_ACCEPTANCE.json).
- **FAIL:** public discovery raised `CatalogMetadataError`; six required slots
  NOT EVALUATED, access validator not reached, field/cause unlocalized.
- Actual metadata: 2 CDSE requests / 15,659 response-body bytes; no PC/token/
  TIFF/XML request, image block, SAR pixel or scientific processing.
- Historical M48 offline tests and M46 access proof retained; no live PASS,
  coverage/product fingerprint, oil detection or calibrated backscatter claimed.
- Owner review and separate diagnostic authorization next; AS-202 NOT STARTED.

### EV-054 — AS-201 M50 SAR STAC geometry boundary correction

- **M50 / E50**; no new scientific decision; Decisions 050–054 unchanged.
- [MD](AS_201_STAC_GEOMETRY_BOUNDARY_FIX.md) and [JSON](AS_201_STAC_GEOMETRY_BOUNDARY_FIX.json).
- Frozen envelope remains immutable; independent built-in JSON enters both providers.
- Real client deepcopy and 3-page/provider pagination pass offline; 136 focused / 1434 full tests PASS.
- M49 FAIL and localization evidence byte-identical; full live retry NOT RUN.
- Provider requests 0; SAR pixels/bytes 0/0; scientific SAR compute 0.
- AS-202 NOT STARTED; Decision 055 ABSENT. Offline interoperability, not live readiness.

### EV-055 — AS-201 M51 one controlled six-source live retry

- **M51 / E51**; evidence ID only; Decision 055 remains absent.
- [MD](AS_201_LIVE_ACCEPTANCE_RETRY.md) and [JSON](AS_201_LIVE_ACCEPTANCE_RETRY.json).
- **FAIL:** stage I CDSE product:type IW_GRDH_1S rejected by GRD/GRDH contract.
- Both catalogs/pagination pass; 8 requests / 671,449 body bytes; six UNAVAILABLE slots.
- Assets/header/XML not accessed; SAR pixel reads/bytes 0/0; scientific SAR compute 0.
- M49 FAIL and M50 correction evidence unchanged; no fix, restart, AS-202 or CI claim.

### EV-056 — AS-201 M52 exact CDSE product-type interoperability correction

- **M52 / E52**; Decision 055 remains absent.
- [MD](AS_201_CDSE_PRODUCT_TYPE_FIX.md) and [JSON](AS_201_CDSE_PRODUCT_TYPE_FIX.json).
- Exact IW_GRDH_1S alias alongside GRD/GRDH; incompatible higher-priority metadata still rejects.
- 41 new offline cases; six exact synthetic sources normalize; unchanged normalized retrieval identities.
- M49/M50/M51 evidence preserved; M51 remains FAIL; live readiness unproved.
- No provider request, live retry, SAR pixels/science, AS-202, new decision or CI-success claim.

### EV-057 — AS-201 M53 controlled live acceptance after M52

- **M53 / E53**; Decision 055 remains absent.
- [MD](AS_201_LIVE_ACCEPTANCE_AFTER_M52.md) and [JSON](AS_201_LIVE_ACCEPTANCE_AFTER_M52.json).
- **FAIL:** six UNAVAILABLE / METADATA_INVALID; manifest/startTime timezone rejection; ready=false.
- Both catalogs and 6/6 exact identities pass; 162 HTTP206 VV structural ranges pass; 24 XMLs fetched.
- 195 requests / 20,261,621 body bytes; 30 sign operations / 1 token request; no signed material persisted.
- Complete footprint metadata and 12-source derived provenance are not access readiness.
- M49/M50/M51/M52 evidence byte-identical; no fix, restart, extra provider traffic, pixels, science, AS-202 or CI-success claim.

### EV-058 — AS-201 M54 manifest UTC-time interoperability correction

- **M54 / E54**; OFFLINE MANIFEST UTC-TIME INTEROPERABILITY CORRECTION PASS.
- [MD](AS_201_MANIFEST_UTC_TIME_FIX.md) / [JSON](AS_201_MANIFEST_UTC_TIME_FIX.json).
- Semantic SHA-256: `6c2f7b00534cb1e58e50739ea199e602248476699d40df8ee695fe3fa3f8df1f`.
- 73 new offline cases; 250 focused / 1548 full tests PASS, six existing Rasterio warnings; Ruff PASS.
- Only manifest acquisition times may assume UTC; exact microseconds and every later XML guard retained. Generic parser unchanged.
- M49–M53 evidence preserved; M53 remains historical LIVE FAIL. No provider requests/pixels/scientific compute or live retry.
- LIVE_READINESS UNPROVED; AS-202 NOT STARTED; Decision 055 ABSENT. Proposed visual only; no screenshot created.

### EV-059 — AS-201 M55 controlled live acceptance after M54

- **M55 / E55**; AS201_LIVE_ACCEPTANCE_AFTER_M54 = FAIL; all six UNAVAILABLE / METADATA_INVALID, ready=false.
- [MD](AS_201_LIVE_ACCEPTANCE_AFTER_M54.md) / [JSON](AS_201_LIVE_ACCEPTANCE_AFTER_M54.json).
- Semantic SHA-256: `875eb97e3b48c6ff99d2ea819466a852ca424880ef56b469e773be1992765e5e`.
- Both catalogs/exact identities/assets/VV headers and exact manifest UTC intervals pass; manifest familyName text-cardinality fails.
- Native witness/product/calibration/noise/geolocation/thermal validations NOT_REACHED; no PASS invented for fetched XML.
- 195 requests / 20,261,623 bytes; 30 signing operations / 1 transient token acquisition; no signed material persisted.
- 250 focused / 1548 full tests PASS, six historical Rasterio warnings; offline tests do not override live FAIL.
- M49–M54 evidence and Decisions 050–054 unchanged; no production fix/restart/retry, pixels or science.
- LIVE_READINESS UNPROVED; AS-202 NOT STARTED; Decision 055 ABSENT. Proposed visual only, no screenshot created.

### EV-060 — AS-201 M56 manifest platform representation diagnostic

- **Artifacts:** [MD](AS_201_MANIFEST_PLATFORM_DIAGNOSTIC.md) / [JSON](AS_201_MANIFEST_PLATFORM_DIAGNOSTIC.json).
- **Milestone / engineering:** M56 / E56; diagnostic complete, no production fix.
- **Evidence:** six manifests have one platform/number A; direct family SENTINEL-1 and nested instrument family Synthetic Aperture Radar produce two recursive values and the exact M55 failure. Each body hash matches M55.
- **Accounting:** six signs, one token HTTP acquisition, six HTTP200 manifest GETs / 151,650 bytes; all other provider assets/pixels/science zero.
- **Meaning:** exact application XML-scope mismatch plus separate case-literal mismatch; no schema-defect assertion or live-readiness claim.
- **Boundary:** M55 HISTORICAL LIVE FAIL; LIVE_READINESS UNPROVED; AS-202 NOT STARTED; Decision 055 ABSENT. No PR/merge/correction/retry.

### EV-061 — AS-201 M57 offline manifest platform familyName correction

- **Artifacts:** [MD](AS_201_MANIFEST_PLATFORM_FIX.md) / [JSON](AS_201_MANIFEST_PLATFORM_FIX.json).
- **Milestone / engineering:** M57 / E57; OFFLINE MANIFEST PLATFORM FAMILYNAME INTEROPERABILITY CORRECTION PASS.
- **Evidence:** exact six-source observed scope/casing representation passes complete synthetic metadata validation; nested family isolation and invalid direct/cardinality cases fail closed.
- **Quantitative result:** 69 added cases; 330 focused / 1617 full tests PASS; six existing Rasterio warnings. Provider/signing/pixels/science zero.
- **Preservation:** shared XML/time helpers, platform number A, earlier/later guards, prior evidence, Decisions 050–054 and protected material unchanged.
- **Boundary:** M55 HISTORICAL LIVE FAIL; M56 DIAGNOSTIC COMPLETE; LIVE_READINESS UNPROVED; AS-202 NOT STARTED; Decision 055 ABSENT. No retry/PR/merge.

### EV-062 — M58 controlled six-source live acceptance after M57 — FAIL

- Sources: [MD](AS_201_LIVE_ACCEPTANCE_AFTER_M57.md) / [JSON](AS_201_LIVE_ACCEPTANCE_AFTER_M57.json).
- M58/E58: catalogs, identities, assets, VV headers and complete manifests PASS;
  all six calibration-vector azimuthTime checks FAIL; later guards NOT_REACHED.
- Six UNAVAILABLE / METADATA_INVALID; all groups/final ready=false.
- One unchanged public run, passive tracing; 195 requests / 20,261,623 bytes;
  30 signs / 1 token; zero SAR pixels/science; no repair or second diagnostic.
- 330 focused / 1617 full tests PASS; six existing Rasterio warnings; quality,
  digest/security/preservation PASS. No GitHub CI claim.
- M55 FAIL / M56 diagnostic / M57 offline PASS remain historical; live readiness
  UNPROVED. AS-202 NOT STARTED; Decision 055 ABSENT. No PR/merge.

### EV-063 — M59 SAFE XML timestamp representation diagnostic — COMPLETE

- Sources: [MD](AS_201_SAFE_XML_TIME_DIAGNOSTIC.md) / [JSON](AS_201_SAFE_XML_TIME_DIAGNOSTIC.json).
- M59/E59: all 18 XML bodies hash-identical to M58; all 360 consumed timestamps
  naive ISO / six fractional digits / no whitespace/offset; generic parser rejects.
- 36 ADS wall-clock comparisons PASS; semantic UTC remains unestablished.
  UTC_SEMANTICS_REQUIRES_OWNER/SPEC REVIEW. Vector counts/first/last/digests recorded.
- 18 signs / 1 token; 19 HTTP200 requests / 19,339,930 bytes; no catalog/manifest/
  TIFF/pixel/science access; no raw XML or signed reference persisted.
- 330 focused / 1617 full tests PASS, six existing Rasterio warnings; quality,
  digest/security/preservation PASS. No GitHub CI claim.
- M58 remains HISTORICAL LIVE FAIL; M57 OFFLINE CORRECTION PASS; live readiness
  UNPROVED. No production fix/full rerun/PR/merge. AS-202 NOT STARTED; Decision 055 ABSENT.

### EV-064 — M60 SAFE XML UTC time interoperability correction — OFFLINE PASS

- Sources: [MD](AS_201_SAFE_XML_UTC_TIME_FIX.md) / [JSON](AS_201_SAFE_XML_UTC_TIME_FIX.json).
- M60/E60: official specification timeType UTC semantics supplied in authorization;
  immutable M59 360 naive timestamps provide separate serialization evidence.
- One local helper/four authorized calls; exact ADS identity, M54/M57/generic
  parsing and all later guards preserved. Six-source complete synthetic matrix PASS.
- 80 malformed / 18 exact mismatch / 41 later-guard cases reject; 493 focused /
  1780 full PASS; six existing Rasterio warnings; all offline quality gates PASS.
- Provider/sign/token/TIFF/XML/pixel/science zero; no M58/M59 rerun, PR or merge.
- M58 HISTORICAL LIVE FAIL; M59 DIAGNOSTIC COMPLETE; LIVE_READINESS and
  SAR_SCIENTIFIC_READINESS UNPROVED; AS-202 NOT STARTED; Decision 055 ABSENT.
