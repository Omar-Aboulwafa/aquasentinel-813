# AS-201 M54 — Manifest UTC-time interoperability correction

**M54 / E54 / EV-058: OFFLINE MANIFEST UTC-TIME INTEROPERABILITY CORRECTION PASS.**
Date: 11 October 2026 (Asia/Dubai). Offline correction only; no live retry.

## Baseline and preserved failure

Official main: `9403faf7f7bd8c0a71e5d262338974647831ad93` (PR #33 merge).
Parent M53 evidence commit: `42855ac22844ede60e37c5136944de879a0a9080`; its sole parent is official main.
Prepared on `fix/as-201-manifest-utc-time-normalization`. M53 changes six documentation/evidence files only.
History is main → M53 historical live FAIL → M54 offline correction; no amend or rewrite.

M53 complete catalogs resolved all six CDSE identities, six PC identities and six stable
asset sets. All six VV structural headers passed and all four required XMLs per slice
were fetched. Every source then became `UNAVAILABLE / METADATA_INVALID` at
`_validate_manifest` → generic `_parse_time` for timezone-naive `manifest.startTime`.
Example: `2026-04-24T14:42:05.150515` versus the frozen
`2026-04-24T14:42:05.150515+00:00`. Sanitized error:
`Sentinel-1 item manifest.startTime must be timezone-aware.`
Later live XML identity/LUT checks were not reached. M53 remains historical FAIL.

Historical evidence remains byte-identical:
[M53 MD](AS_201_LIVE_ACCEPTANCE_AFTER_M52.md) /
[JSON](AS_201_LIVE_ACCEPTANCE_AFTER_M52.json), semantic SHA-256
`984cdb35b7364150d687d86f4a3478f2e93ca7015843b58425f109687ab0078d`.

## Smallest local correction

Only production path: `src/aquasentinel/ingestion/sentinel1_metadata.py`.
New `_parse_manifest_time` is called only for manifest acquisition `startTime` and
`stopTime`. Explicit offsets normalize to UTC; a naive value receives UTC at this
boundary alone. The existing exact start/stop tuple comparison is unchanged.
Microseconds remain significant; no tolerance, rounding, truncation, filename-derived
correction, STAC substitution or provider fallback.

Raw text is checked before `_unique_text` can strip it, so padded/empty values remain
fail-closed. Fractional precision beyond six digits is rejected because Python's
`datetime.fromisoformat` would otherwise silently truncate it. Invalid dates/times,
wrong/swapped intervals and one-microsecond mismatches fail.

`sentinel1_policy._parse_time` is byte-identical and continues rejecting naive time.
Product/calibration/noise ADS and calibration/noise LUT time boundaries remain strict.
Manifest platform, IW, ascending orbit, relative orbit 101, product, ADS identity,
dimensions, geolocation/incidence, calibration/noise LUTs and thermal-noise metadata
guards are unchanged. Reversing only the new imports/helper and its two calls restores
the entire original production file byte-for-byte.

## Offline regression matrix

| Coverage | Cases | Result |
| --- | ---: | --- |
| six frozen sources times four serializations | 24 | PASS |
| start stop one microsecond or one second mismatch | 4 | PASS |
| swapped interval | 1 | PASS |
| start stop times eight invalid serializations | 16 | PASS |
| generic parser naive start stop rejection | 2 | PASS |
| three ADS roles times naive start stop rejection | 6 | PASS |
| calibration noise LUT naive time rejection | 2 | PASS |
| later XML identity dimensions geolocation LUT thermal guards | 18 | PASS |
| **Total new cases** | **73** | **PASS** |

Existing six-source XML/header fixtures exercise naive/Z/+00:00/+04:00 equivalent
serialization; the complete returned metadata summary equals the original aware
fixture summary. Negative controls keep XML syntactically valid to reach the relevant
guard. Public errors stay sanitized. Existing tests are unchanged; the autouse
`no_network` fixture rejects network connections in these contract tests.

## Engineering quality gates

- Focused Sentinel-1 metadata/contract/non-optical catalog suite: **250 passed**, 1.02 s.
- Full repository suite: **1548 passed**, 36.86 s; **6 existing Rasterio PendingDeprecationWarnings**.
- Ruff: **PASS**. Diff/new-file whitespace, strict finite JSON, independent semantic
  digest reconstruction/repeat, credential scan and preservation: **PASS**.
- These are local engineering gates; no GitHub CI success is claimed.

## Preservation

Snapshot covered 165 tracked files, frozen Decisions 050–054,
44 protected external file hashes, 57 modes and all three
safety stashes. Only the eight authorized paths change. Resolver, shared STAC, optical,
config/dependencies and entire DECISIONS file remain byte-identical. M49–M53 MD/JSON
evidence remains byte-identical; historical failure checkpoints are not rewritten.
Protected bundles/caches/handoffs/recovery artifacts, modes and stash inventory are
unchanged; no new scientific raster/cache product or credential/signed href is persisted.

## External execution boundary

CDSE / PC / signing / token / TIFF / XML provider / ZIP requests or operations: **0** each.
SAR pixel reads/bytes: **0/0**. Scientific SAR compute: **0**. Live retries: **0**.
Git fetch/push are branch-publication operations, not provider requests.
Offline synthetic tests do not constitute real scientific processing.

## Deterministic evidence

Schema: `as201-m54-manifest-utc-time-fix-v1`. Semantic SHA-256: `6c2f7b00534cb1e58e50739ea199e602248476699d40df8ee695fe3fa3f8df1f`.
Hash UTF-8 JSON of `semantic` only, sorted keys, compact separators,
`ensure_ascii=False`, `allow_nan=False`. Quality timing and the new commit SHA are
excluded. Independent reversed-key reconstruction and repeat must match the digest.
[Machine-readable evidence](AS_201_MANIFEST_UTC_TIME_FIX.json).

## Limitation and next action

M54 establishes only offline acceptance of the M53-observed manifest serialization.
It does not establish later live XML identity/LUT/geolocation success or six-source
provider readiness. **LIVE_READINESS = UNPROVED.** No SAR calibration, thermal-noise
correction, dB conversion, reprojection, mosaicking, filtering or oil detection.
**AS-202 NOT STARTED. Decision 055 ABSENT.** No PR, merge or live acceptance retry.
Next: owner review of this correction; publication/merge and any controlled live retry
require separate authorization.
