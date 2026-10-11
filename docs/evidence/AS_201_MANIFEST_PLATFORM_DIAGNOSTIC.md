# AS-201 M56 — Manifest Platform / familyName Representation Diagnostic

## Result, scope and chronology

**M56 / E56 / EV-060: MANIFEST_PLATFORM_REPRESENTATION_DIAGNOSTIC_COMPLETE.**
Official main: `cea91ab8b7fa8dbf4618a32c0a51ea1b2356f721`.
Exact branch parent M55: `ff00aafed870b0f427532159c4eb4ac3d08691d9`.
Branch: `diagnostic/as-201-manifest-platform-familyname`.
Chronology: main → published M55 live FAIL → M56 manifest-only diagnostic.
M56/E56/EV-060 were unused before allocation. M55 evidence has exactly six docs-only
paths and the required sole parent; its FAIL state and original body remain unchanged.

Goal: localize the platform familyName representation without a production fix or
full live acceptance. Inputs: six stable, unsigned, query-free allowlisted manifest
references from M55 JSON `/semantic/retrieval/parameters/source_records`.
Exact CDSE/PC/source/native-product identities were checked before any request.
All six references have purpose `manifest`, hostname
`sentinel1euwest.blob.core.windows.net`, and the exact frozen native-product path.
No catalog search or source rediscovery occurred. No new dependencies or tests.

Execution UTC: `2026-10-11T11:01:39.926964+00:00` → `2026-10-11T11:01:44.622924+00:00`.
The existing signer and bounded `read_bytes` were used, with the existing **2 MiB
manifest budget**. The existing `_parse_xml` rejects DTD/entities and caps XML at
4 MiB; the stricter manifest transport budget applies here. XML was parsed in
memory, unmodified; no raw XML, signed URL, SAS query, token, headers or cookies
were persisted. Only minimal benign structural facts and body hash/size survive.
Token state was cleared and scoped logging suppression restored afterward.

## Six-manifest structure matrix

| Role / slice | Platforms | Number | Descendant familyName count | Recursive text list | Unique cardinality / result | XML bytes | Matches M55 hash |
|---|---:|---|---:|---|---|---:|---|
| REFERENCE / 1 | 1 | `A` | 2 | `SENTINEL-1`; `Synthetic Aperture Radar` | 2 / RAISES | 25,275 | Yes |
| REFERENCE / 2 | 1 | `A` | 2 | `SENTINEL-1`; `Synthetic Aperture Radar` | 2 / RAISES | 25,275 | Yes |
| DOCUMENTARY_EVENT / 1 | 1 | `A` | 2 | `SENTINEL-1`; `Synthetic Aperture Radar` | 2 / RAISES | 25,275 | Yes |
| DOCUMENTARY_EVENT / 2 | 1 | `A` | 2 | `SENTINEL-1`; `Synthetic Aperture Radar` | 2 / RAISES | 25,275 | Yes |
| LATE_FOLLOW_UP / 1 | 1 | `A` | 2 | `SENTINEL-1`; `Synthetic Aperture Radar` | 2 / RAISES | 25,275 | Yes |
| LATE_FOLLOW_UP / 2 | 1 | `A` | 2 | `SENTINEL-1`; `Synthetic Aperture Radar` | 2 / RAISES | 25,275 | Yes |

All six platform subtrees have identical recorded structure, text, attributes and
parser results. Each manifest has exactly one platform element. The direct-child
local-name order is `nssdcIdentifier`, `familyName`, `number`, `instrument`.

## Exact minimal structural extraction (common to all six)

| Relative local-name path | Exact text | Stripped text | None / empty after strip | Benign attributes |
|---|---|---|---|---|
| `platform/familyName` | `SENTINEL-1` | `SENTINEL-1` | false / false | none |
| `platform/number` | `A` | `A` | false / false | none |
| `platform/instrument/familyName` | `Synthetic Aperture Radar` | `Synthetic Aperture Radar` | false / false | `abbreviation="SAR"` |

The JSON retains these facts separately for every frozen manifest, exact stable
unsigned reference/source identity, and each body's SHA-256. All six body hashes
match the M55 manifest hashes; this diagnostic localizes the same captured inputs.

## Current-parser reproduction and exact cause

Unchanged `_texts(platform, "familyName")` returns, in order:
`["SENTINEL-1", "Synthetic Aperture Radar"]`.
The unique-value set is `{"SENTINEL-1", "Synthetic Aperture Radar"}`, cardinality **2**.
Unchanged `_unique_text(platform, "familyName")` raises:
**`Sentinel1MetadataError: XML requires one consistent familyName value.`**
Platform number recursion returns `["A"]`; `_unique_text(platform, "number")` returns `A`.

**Classification: application XML element-scope interoperability defect.**
Recursive local-name matching mixes the platform's family identity and its nested
instrument's family identity. It is neither zero text values nor repeated identical
values: there are two different valid-looking benign descriptions at different
structural levels. A provider-data defect is not established; no formal schema
validation was performed. M56 does not certify standards compliance.

The direct-child familyName unambiguously identifies Sentinel-1. However its exact
uppercase value differs from the later current literal `Sentinel-1`. That comparison
was NOT_REACHED in M55 and is not executed as full validation in M56.

## Local hypotheses — no implementation

- Current recursive selection: two distinct values, raises the observed exception.
- Direct-child-only selection: exactly one nonempty value, `SENTINEL-1`.
- That value compared to the current exact `Sentinel-1` literal: false.
- Exact case-only comparison of those two strings: true.

Smallest justified correction for separate owner authorization: a manifest-specific
direct-child familyName cardinality/text reader and exact case-only Sentinel-1
comparison, with offline nested-instrument, absent/duplicate/direct-conflict/wrong-family
regressions. Proposed production scope: `sentinel1_metadata.py` only, preserving
shared `_texts`/`_unique_text`, optical code, exact platform number/source/time guards
and all later native witness/XML/LUT/geolocation/thermal validation. No alias or broad
substring acceptance is justified. **Nothing was implemented or monkeypatched to
produce an acceptance PASS.** A production fix and any acceptance retry need separate
owner authorization. No Decision 055.

## Actual network / execution accounting

| Activity | Actual |
|---|---:|
| Manifest signing operations | 6 |
| Token HTTP acquisitions | 1 |
| Token response-body bytes | 404 |
| Manifest GET requests | 6 |
| Manifest response-body bytes | 151,650 |
| Total provider HTTP requests | 7 |
| Total response-body bytes | 152,054 |
| All HTTP statuses | 200 |
| Ordinary internal / custom retries | 0 / 0 |
| CDSE / PC STAC / catalog requests | 0 / 0 / 0 |
| TIFF / VH / product / calibration / noise XML | 0 / 0 / 0 / 0 / 0 |
| ZIP / image-block / SAR pixel reads and bytes | 0 / 0 |
| Scientific SAR compute | 0 |
| search_sentinel1 / validate_retrieval_access / M55 reruns | 0 / 0 / 0 |

Byte counts are response bodies, excluding wire framing/headers. Passive HTTP
observation delegates the original opener and never records signed URLs or token
body/hash. Engineering tests are offline synthetic execution, separate from live
provider activity; real socket connections were blocked and zero were attempted.
The exclusive diagnostic marker remains outside the repository; no automatic rerun.

## Evidence integrity / engineering gates

Semantic SHA-256: **`1c4da094b1845f1862d6c39cd173f8d66ad1e935c5dcf34d532ea9fbd6a5b6eb`**.
Canonical UTF-8 JSON uses sorted keys, compact separators, stable list order,
`ensure_ascii=False`, `allow_nan=False`; hashes only the JSON `semantic` object.
Execution times, engineering results and preservation summaries are outside this
digest. Strict finite JSON, independent digest reconstruction with reversed object
insertion order, deterministic repeat and credential/signed-URL scans PASS.

**261 focused tests PASS (0.98 s); 1548 full tests PASS
(37.33 s); six existing Rasterio PendingDeprecationWarnings.**
Ruff PASS; tracked/new-file whitespace PASS. No GitHub CI success claimed.
All non-authorized tracked hashes unchanged; source/tests/config/dependencies,
entire Decisions 050–054 file, accepted upstream/M49–M55 evidence byte-identical.
**44 protected external hashes / 57 modes / three stashes unchanged**;
recovery material retained; no new scientific raster/cache product.

## Boundary and handoff

**M55 = HISTORICAL LIVE FAIL. LIVE_READINESS = UNPROVED.**
M56 diagnoses representation; later XML/native witness/LUT/geolocation/thermal
checks remain unproved. No SAR calibration/noise application, backscatter/dB,
reprojection/mosaicking/filtering or oil detection. **AS-202 NOT STARTED; Decision 055
ABSENT.** No PR or merge. Next: owner review of diagnostic facts, then separate
minimal manifest-boundary fix authorization, followed only by a separately authorized
live engineering gate. No production correction or M55 rerun in this task.
