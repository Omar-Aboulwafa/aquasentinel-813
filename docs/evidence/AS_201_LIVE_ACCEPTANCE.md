# AS-201 M49 — Live Six-Source Provider Acceptance

## Result and scope

**M49 / E49 / EV-053: AS201_LIVE_ACCEPTANCE = FAIL.** This is the terminal
failed acceptance attempt, not a completed six-source validation or AS-202.
Failure classification: **CATALOG_METADATA_CONTRACT_REJECTION_UNLOCALIZED**.
The unchanged merged public `search_sentinel1(...)` was called once and raised
`CatalogMetadataError` before returning a retrieval set. `validate_retrieval_access(...)`
was **not reached**. The failure is retained, not repaired or converted to PASS.

Baseline: `392603b5b074d515eb6c137e33395c7f0b1256ac`, PR **#30 MERGED / CLOSED**,
parents `1d2d994c7a04cca712485ce53dc9132db50615a8` and
`d9ff882a6ff0727a91d1a54240c12d8c61920725`. Decision 054 remains merged/frozen.
Branch: `validation/as-201-live-acceptance`, created clean from exact main.
M49/E49/EV-053 were confirmed unused before allocation. M48 implementation/offline
validation and historical M46 provider access remain distinct.

Live attempt: **2026-10-10T21:53:31.697726+00:00 → 2026-10-10T21:53:34.600932+00:00** (UTC).
An external observer delegated to the merged HTTP functions and public path;
it counted response bytes/requests, suppressed diagnostics in its process and
restored instrumentation/logging state. No production source or test was edited.
Existing Python 3.11 virtual environment was reused; no dependency installation.

## Exact failure evidence and uncertainty

| Request | Host / stable path | HTTP | Response-body bytes | Body SHA-256 |
|---|---|---|---:|---|
| CDSE root GET | stac.dataspace.copernicus.eu `/v1/` | 200 | 3,670 | `2665e1c0ebd3bd0a47ecc82902237d5797abcfcd95dab73eaa024fc4db3890d4` |
| CDSE collection GET | stac.dataspace.copernicus.eu `/v1/collections/sentinel-1-grd` | 200 | 11,989 | `d0f82ec0a132ebc0c48543f25e1fa0a0de4d6f8c5279936a7907c90160806246` |

No search-page HTTP request occurred. Neither PC metadata nor signing, TIFF/XML
access was reached. HTTP 200 is not proof of a valid normalized catalog contract.
Because the raised exception is a catalog metadata rejection and there is no
demonstrated transport denial, this gate is **FAIL**, not a provider-availability PASS.

**Diagnostic limitation:** the observer retained the exception class, request
status/path/body hashes and counts, but not the response bodies, exception text
or traceback. The precise offending field and whether it reflects a code defect
or provider schema drift are therefore **not established**. No fabricated cause
is assigned. Its initial coarse fatal-error diagnostic said BLOCKED; this record
explicitly distinguishes that diagnostic from the durable metadata-failure gate.
There was no further provider request or retry after failure and no production patch.

## Six frozen slots — unknown is not a failed individual header

All six exact Decision-054 slots remain in this evidence, in frozen order.
None reached an actual AS-201 availability state because public discovery aborted.
Do not translate the null state into six measured ACCESS_BLOCKED outcomes.

| Role / slice | Required PC identity | Live outcome |
|---|---|---|
| REFERENCE / 1 | `S1A_IW_GRDH_1SDV_20260424T144205_20260424T144230_064223_08158E` | NOT EVALUATED: discovery aborted |
| REFERENCE / 2 | `S1A_IW_GRDH_1SDV_20260424T144230_20260424T144255_064223_08158E` | NOT EVALUATED: discovery aborted |
| DOCUMENTARY_EVENT / 1 | `S1A_IW_GRDH_1SDV_20260506T144204_20260506T144229_064398_081C09` | NOT EVALUATED: discovery aborted |
| DOCUMENTARY_EVENT / 2 | `S1A_IW_GRDH_1SDV_20260506T144229_20260506T144254_064398_081C09` | NOT EVALUATED: discovery aborted |
| LATE_FOLLOW_UP / 1 | `S1A_IW_GRDH_1SDV_20260518T144204_20260518T144229_064573_082235` | NOT EVALUATED: discovery aborted |
| LATE_FOLLOW_UP / 2 | `S1A_IW_GRDH_1SDV_20260518T144229_20260518T144254_064573_082235` | NOT EVALUATED: discovery aborted |

The [JSON](AS_201_LIVE_ACCEPTANCE.json) records all exact CDSE/native IDs,
microsecond intervals, absolute orbit and **expected**, not observed, dimensions.
All slices remain S1A IW GRDH, ascending relative orbit101, VV+VH by frozen policy.
No slice/date was removed, substituted or normalized to an alternate representation.
REFERENCE is not an oil-free label; DOCUMENTARY_EVENT is not a proven peak;
LATE_FOLLOW_UP is not a recovery claim.

## TIFF/XML contracts and thermal-noise state

**NOT EVALUATED for every slot:** CDSE/PC exact identity, platform/mode/product/
orbit/polarizations, start/end interval, VV/VH asset identity, manifest, product
annotation, calibration/noise XML and TIFF structural contract. Width/height,
uint16/single-band, nodata, compression, tile size, overview count, WGS84 tiepoints,
absence of native affine and `thermalNoiseCorrectionPerformed` are all **unknown**
in this live attempt. No historical or synthetic values fill these fields.

## Request and byte accounting

| Category | Requests | Response-body bytes received |
|---|---:|---:|
| CDSE STAC metadata (root + collection) | 2 | 15,659 |
| CDSE search pages | 0 | 0 |
| Planetary Computer STAC metadata | 0 | 0 |
| Signing/token | 0 | 0 |
| TIFF header/IFD/tag ranges | 0 | 0 |
| Manifest XML | 0 | 0 |
| VV product annotation XML | 0 | 0 |
| VV calibration XML | 0 | 0 |
| VV noise XML | 0 | 0 |
| **Total provider retrieval** | **2** | **15,659** |

Bytes are response-body bytes delivered to the HTTP client, not wire framing,
HTTP headers or compressed-transfer size. Git operations are excluded.
Full product ZIP downloads **0**; image-block payload requests **0**;
SAR pixel read calls/bytes **0/0**; real scientific SAR compute calls **0**.
No `rasterio.open()` on measurement assets, TIFF image blocks, calibration,
noise correction, power/backscatter/dB conversion, reprojection, common grid,
resampling, mosaic, speckle, masks, detection, geometry, temporal SAR or risk.

## Coverage, identity and provenance

Each date's live metadata support, common three-date support and coverage gaps:
**UNAVAILABLE — discovery did not return any frozen footprint inventory**.
No synthetic/old support geometry or area is presented as M49 measurement.
No lower-bound footprint geometry was constructed. Metadata support would not
prove pixel evaluability even if available.

Retrieval fingerprint: **null**; six slice fingerprints: **null**;
three group fingerprints: **null**; derived retrieval provenance source count:
**null / no derived product constructed**, not an accepted zero-source retrieval.
Evidence semantic SHA-256: `ad4d6422a1280cb730f43952a20bd5bf4992d53b9bfe7627862d6715ab22cc7c`.
Canonicalization hashes JSON `semantic` only with sorted keys, compact UTF-8,
finite JSON and fixed frozen slot order; execution timestamps are excluded.
The external observation record hash is recorded separately in JSON.

## Engineering, security and preservation

- Full repository pytest: **1,432 passed, six existing Rasterio
  PendingDeprecationWarnings, 36.39s**. These offline fixtures do not establish
  live six-source availability.
- Ruff, diff/new-file whitespace, strict finite JSON, independent digest/repeat,
  credential/signed-URL scan and preservation checks: **PASS**. No CI claim.
- All non-authorized tracked files, source/tests/configuration/dependencies,
  Decisions 050–054 bodies and prior accepted evidence remain byte-identical.
- **44 protected external hashes / 57 modes** unchanged; sealed caches/handoffs,
  recovery artifacts and the complete three-stash inventory retained, including
  both historical AS-104 safety stashes and the M48 recovery stash.
- No scientific cache/raster product created. No token was requested, printed
  or persisted; no signed href, Authorization header or cookie persisted.

## Owner handoff

**AS-202 NOT STARTED. Decision 055 ABSENT. No PR created or merge performed.**
Only this failed acceptance record and continuity documentation are published.
Next: owner review of the stopped M49 failure; separately authorize catalog
failure localization and any subsequent correction/retry. Do not proceed to
AS-202 or relax source/policy checks on the basis of offline tests alone.
No calibrated backscatter, oil candidate, petroleum/source confirmation,
water safety or shutdown conclusion follows from this attempt.
