# AS-201 M59 — SAFE XML Timestamp Representation Diagnostic

## Scope, baseline and chronology

**M59 / E59 / EV-063: SAFE_XML_TIME_REPRESENTATION_DIAGNOSTIC_COMPLETE.**
Official main: `225efc896bf74d87f62741e05a4251ac86d07395` (PR #36 merge, exact expected parents verified).
Parent: published M58 `376754bed59eedbe9cbce47978ae5a52ae481410`, whose sole parent is official main.
Fresh clean branch: `diagnostic/as-201-safe-xml-time-representation`. M59/E59/EV-063 unused before allocation.
Chronology: **main → M58 historical live FAIL → M59 diagnostic**. M58 unchanged.

M58 passed all six complete manifests including native VV witness, then failed
`_validate_luts` → `calibrationVector/azimuthTime` → generic `_parse_time` with
`Sentinel-1 item calibration.azimuthTime must be timezone-aware.`
Raw offending timestamp text was not retained in M58; later checks NOT_REACHED.
M59 inspects only existing consumed product/calibration/noise XML timestamps.
No production/test/config/dependency change, full live acceptance, complete
metadata validator or scientific SAR processing. No parser correction.

Inputs: M58's exact six frozen source policies and 18 stable unsigned references,
with purpose/PC/native identity, HTTPS, existing host allowlist, no query/userinfo
verified before any request. Exactly one GET per existing product_vv,
calibration_vv and noise_vv asset; no substitution or manual retry.
All **18/18 body SHA-256 and lengths match M58** before interpretation.
XML exists in memory only; no raw XML, signed URL/query/token/header/cookie saved.
Minimal benign timestamp facts, body SHA/length and safe request accounting saved.

## Six-source ADS start/stop matrix

Each product, calibration and noise document has exactly one adsHeader.
Within each source, all three roles have the **identical exact start/stop text**:

| Frozen source | Exact raw startTime (all 3 roles) | Exact raw stopTime (all 3 roles) | Product / calibration / noise timezone | Frozen field correspondence |
|---|---|---|---|---|
| REFERENCE / 1 | `2026-04-24T14:42:05.150515` | `2026-04-24T14:42:30.148548` | NAIVE / NAIVE / NAIVE | PASS (wall-clock only) |
| REFERENCE / 2 | `2026-04-24T14:42:30.150042` | `2026-04-24T14:42:55.148075` | NAIVE / NAIVE / NAIVE | PASS (wall-clock only) |
| DOCUMENTARY_EVENT / 1 | `2026-05-06T14:42:04.538690` | `2026-05-06T14:42:29.536703` | NAIVE / NAIVE / NAIVE | PASS (wall-clock only) |
| DOCUMENTARY_EVENT / 2 | `2026-05-06T14:42:29.538209` | `2026-05-06T14:42:54.536224` | NAIVE / NAIVE / NAIVE | PASS (wall-clock only) |
| LATE_FOLLOW_UP / 1 | `2026-05-18T14:42:04.240283` | `2026-05-18T14:42:29.238414` | NAIVE / NAIVE / NAIVE | PASS (wall-clock only) |
| LATE_FOLLOW_UP / 2 | `2026-05-18T14:42:29.239908` | `2026-05-18T14:42:54.239534` | NAIVE / NAIVE / NAIVE | PASS (wall-clock only) |

All 36 ADS fields: raw text equals stripped text, no surrounding whitespace,
`datetime.fromisoformat()` accepts as timezone-naive, explicit offset absent,
**six fractional-second digits**, generic strict `_parse_time` RAISES.
For product/calibration/noise respectively, reproduce role-specific `.startTime`
and `.stopTime` calls using existing `_unique_text` consumption. All 36 wall-clock
field comparisons and exact ISO text comparisons against the frozen acquisition
representation with timezone annotation removed PASS. This compares displayed
calendar/time fields only; no timezone is invented or converted for this comparison.
**Text/field correspondence is NOT UTC semantic equivalence.**
JSON retains all requested raw/stripped/precision/offset/parser facts per ADS field.

## Calibration and noise-range timestamp summaries

| Source / family | Vectors and timestamps | Aware / naive | First exact text | Last exact text |
|---|---:|---:|---|---|
| REFERENCE / 1 / CALIBRATION | 27 | 0 / 27 | `2026-04-24T14:42:05.150515` | `2026-04-24T14:42:31.150515` |
| REFERENCE / 1 / NOISE | 27 | 0 / 27 | `2026-04-24T14:42:05.150515` | `2026-04-24T14:42:30.148548` |
| REFERENCE / 2 / CALIBRATION | 27 | 0 / 27 | `2026-04-24T14:42:30.150042` | `2026-04-24T14:42:56.150042` |
| REFERENCE / 2 / NOISE | 27 | 0 / 27 | `2026-04-24T14:42:30.150042` | `2026-04-24T14:42:55.148075` |
| DOCUMENTARY_EVENT / 1 / CALIBRATION | 27 | 0 / 27 | `2026-05-06T14:42:04.538690` | `2026-05-06T14:42:30.538690` |
| DOCUMENTARY_EVENT / 1 / NOISE | 27 | 0 / 27 | `2026-05-06T14:42:04.538690` | `2026-05-06T14:42:29.536703` |
| DOCUMENTARY_EVENT / 2 / CALIBRATION | 27 | 0 / 27 | `2026-05-06T14:42:29.538209` | `2026-05-06T14:42:55.538209` |
| DOCUMENTARY_EVENT / 2 / NOISE | 27 | 0 / 27 | `2026-05-06T14:42:29.538209` | `2026-05-06T14:42:54.536223` |
| LATE_FOLLOW_UP / 1 / CALIBRATION | 27 | 0 / 27 | `2026-05-18T14:42:04.240283` | `2026-05-18T14:42:30.240283` |
| LATE_FOLLOW_UP / 1 / NOISE | 27 | 0 / 27 | `2026-05-18T14:42:04.240283` | `2026-05-18T14:42:29.238414` |
| LATE_FOLLOW_UP / 2 / CALIBRATION | 27 | 0 / 27 | `2026-05-18T14:42:29.239908` | `2026-05-18T14:42:55.239908` |
| LATE_FOLLOW_UP / 2 / NOISE | 27 | 0 / 27 | `2026-05-18T14:42:29.239908` | `2026-05-18T14:42:54.239534` |

Each of twelve collections: vector_count=27, azimuthTime_count=27,
missing=0, empty=0, malformed=0, aware=0, naive=27, whitespace=0;
offset representations={NONE}, fractional precision={6}. Each collection's
format is homogeneous; all collections share the same representation class.
Total: **162 calibration + 162 noise-range values**. Timestamp values themselves
vary by position/source; homogeneous serialization does not mean identical values.
Vector first/last values are reported verbatim, without enforcing ADS endpoints,
rounding microseconds or inventing a vector-acquisition equality rule.

Ordered-list SHA-256 values:

- REFERENCE / 1 / CALIBRATION: `cc5c0a56c847953a7ac45d30afb21a1b0aaddcd6e68650df4291282055539192`
- REFERENCE / 1 / NOISE: `895ec105c56aee0d0e47055f3596e242461a95aa031c6b261dc30be25d3ca995`
- REFERENCE / 2 / CALIBRATION: `008fa60b734f585f467c25ff9d56ed6281758c352ef03c06afcb328855225940`
- REFERENCE / 2 / NOISE: `683b5eb4a54616bdd40b0df0471356201974556ef304782b655ecbb7d322beff`
- DOCUMENTARY_EVENT / 1 / CALIBRATION: `7165ee18a90df907a8c01f10ffd2658e8f26a06f9098a2f080f7349ec3a9dee0`
- DOCUMENTARY_EVENT / 1 / NOISE: `e97bd185ef7103c015f0784f07c58c0c04603353e0fca267139a49d784c10fca`
- DOCUMENTARY_EVENT / 2 / CALIBRATION: `0c257f3172cc537daa84b6a8e6b7251d4bbfca5ddb79c72fb2f1e6ac30af47ec`
- DOCUMENTARY_EVENT / 2 / NOISE: `2e52192128099d53f0c91274062ecde4187e0cf2aefaec0c5000773ee4bfdaef`
- LATE_FOLLOW_UP / 1 / CALIBRATION: `0f21e8654858fd31a6f54f3259e372698460c040894a63bfbd52d27990d472f4`
- LATE_FOLLOW_UP / 1 / NOISE: `cce64dc423e99b015d6d06e0f51bb4172ef3788d2bd37adef9fb994f22dc73b3`
- LATE_FOLLOW_UP / 2 / CALIBRATION: `f426037b416d11786ccbb1a36772775ddca40864bec49abbe79037e65d6fb0f6`
- LATE_FOLLOW_UP / 2 / NOISE: `65fc262d6619774d3ba70186aff50d8feec0c821907188746b85cb67d8e00eca`

Each digest hashes the UTF-8 compact JSON array of exact raw timestamp texts in
XML vector order (null only for a missing element; none encountered). Every value
was inspected in memory. Evidence retains counts/representation/first/last/digest,
not all 324 vector values or raw XML. JSON stores these facts per source/family.

## Exact current parser reproduction

No monkeypatch. Only the consumed `_parse_time` calls were reproduced locally:

| Field family | Calls | PASS | RAISE |
|---|---:|---:|---:|
| product.startTime / stopTime | 12 | 0 | 12 |
| calibration.startTime / stopTime | 12 | 0 | 12 |
| noise.startTime / stopTime | 12 | 0 | 12 |
| calibration.azimuthTime | 162 | 0 | 162 |
| noise.azimuthTime | 162 | 0 | 162 |
| TOTAL | 360 | 0 | 360 |

Exception: `Sentinel1RetrievalError`.
Exact sanitized family messages: `Sentinel-1 item <field> must be timezone-aware.`
JSON provides exact `.startTime`, `.stopTime`, and `.azimuthTime` error text.
The original parser accepts ISO syntax but requires an explicit timezone.

## Ten diagnostic questions and answers

1. M58 failed on the unzoned text 2026-04-24T14:42:05.150515 at the first reference calibrationVector/azimuthTime. Format YYYY-MM-DDTHH:MM:SS.ffffff without Z/offset; fromisoformat accepts it as naive; generic _parse_time raises Sentinel1RetrievalError.

2. All 162 calibration-vector timestamps across six sources have the same serialization class: naive, six fractional digits, no surrounding whitespace or explicit offset. The values themselves differ; they are not identical timestamp strings.

3. All 162 noise-range azimuthTime values have the same serialization class and identical strict-parser rejection. Each of the six ordered lists is summarized and hashed separately.

4. All twelve product ADS start/stop values are naive.

5. All twelve calibration ADS start/stop values are naive.

6. All twelve noise ADS start/stop values are naive.

7. All 360 inspected consumed values parse as ISO datetimes, carry exactly six fractional digits, have no surrounding whitespace and no offset. No missing/empty/malformed vector timestamp found.

8. All 18 retrieved product/calibration/noise bodies match their M58 SHA-256 and lengths: 3 documents for each of 6 sources.

9. Calibration-only handling leaves the same proven rejection at noise.azimuthTime and all six ADS role/start-stop boundaries. Noise range is the next timestamp family in production order if intervening calibration guards pass. M59 does not prove those intervening guards or run the complete validator.

10. Observed serialization is uniform across the inspected SAFE XML timestamp families, supporting review of a single narrowly scoped metadata-time boundary rather than unrelated format exceptions. UTC meaning is not established by formatting; owner/spec review is required before any UTC interpretation rule. ADS exact frozen interval guards and vector semantics must remain distinct; generic parser must not be globally relaxed.

**UTC_SEMANTICS_REQUIRES_OWNER/SPEC REVIEW.** No authoritative standards review
or external documentary request occurred here. This diagnostic proves serialization,
not implicit UTC meaning. It makes no provider-defect or formal XML-schema
compliance/noncompliance claim. A future owner/spec-reviewed rule could be scoped
to explicitly reviewed SAFE metadata time fields; this diagnostic does not authorize
it. Generic parser, exact ADS frozen intervals, microsecond significance and all
later native/XML/LUT/geolocation/thermal guards remain unchanged.

## Actual network and execution accounting

| Role | HTTP requests | Response-body bytes | HTTP status counts |
|---|---:|---:|---|
| TOKEN | 1 | 400 | 200: 1 |
| PRODUCT | 6 | 10,685,021 | 200: 6 |
| CALIBRATION | 6 | 6,093,708 | 200: 6 |
| NOISE | 6 | 2,560,801 | 200: 6 |
| TOTAL | 19 | 19,339,930 | All HTTP200 |

**18 signing operations / 1 token HTTP acquisition**. XML asset bodies total
**19,339,530 bytes** across 18 GETs, each once. Token response-body accounting
400 bytes; no token value/body/hash retained. Bytes exclude TLS/HTTP wire overhead.
Safe accounting: role/source identity/host/status/count/length only; exact stable
unsigned references remain in JSON. No signed query/header persisted.

CDSE, PC STAC, manifest, TIFF, VH, ZIP, image-block requests: **zero**.
SAR pixel reads/bytes: **0/0**. Scientific SAR compute: **0**.
`search_sentinel1`, `validate_retrieval_access`, complete metadata/manifest/ADS/LUT
validators and TIFF reader: **zero calls**, passively checked. M58 was not rerun.
No custom additional request, manual retry, source substitution or science.
Trace/logging restored; transient token state discarded.

## Engineering quality, preservation and digest

Focused AS-201/Sentinel-1: **330 passed in 1.08s**.
Full repository: **1617 passed, 6 existing Rasterio PendingDeprecationWarnings in 36.07s**.
Offline test processes denied external socket connections; **0 attempts** in each.
Ruff, tracked/new-file whitespace, strict finite JSON, independent semantic digest
reconstruction/repeat, credential/signed-URL scan and preservation audit: **PASS**.
No GitHub CI success claim.

Only six authorized documentation/evidence paths change. Source/tests/config/
dependencies, Decisions 050–054 entire file/frozen bodies, M58 MD/JSON and all
prior accepted upstream evidence remain byte-identical. **49 protected external
hashes / 62 modes / all three stashes** unchanged; recovery retained;
data inventory unchanged; no scientific products created.

Semantic SHA-256: `0550fd44fc8a6f6e4a8f1746240587dd108a2faca83b7d41229fd366f16d5fa6`.
Canonicalization: sorted keys, compact comma/colon separators, UTF-8,
ensure_ascii=false, allow_nan=false; array order retained. Execution timestamps,
quality/preservation summaries and new commit SHA excluded. Independent reparse/
key-order reversal gives the same digest. Execution time is recorded separately
in JSON: `2026-10-11T14:00:10.366177+00:00` to `2026-10-11T14:00:22.888376+00:00` UTC.

## Owner handoff

**M58 HISTORICAL LIVE FAIL; M57 OFFLINE CORRECTION PASS; LIVE_READINESS UNPROVED.
AS-202 NOT STARTED. Decision 055 ABSENT.** No PR/merge.
Next: owner/spec review of UTC semantics and diagnostic facts; any narrow parser
correction/offline regression work, publication/merge or live acceptance requires
separate authorization. No correction or full live rerun in M59.
