# AS-201 M61 — Controlled live acceptance after M60

## Result and scope

**M61 / E61 / EV-065: AS201_LIVE_ACCEPTANCE_AFTER_M60 = PASS.**
Official main/base: `23887f0d4782ea8711b06e5566e66f4a3839a7fa`, PR #37 merge with exact parents
`225efc896bf74d87f62741e05a4251ac86d07395` and
`505336537683f4a23b2fe4b3c206b768328f829f`.
Fresh branch: `validation/as-201-live-acceptance-after-safe-utc-fix`.
M61/E61/EV-065 were unused before allocation. Decisions 050–054 preserved;
Decision 055 absent. Source/tests/config/dependencies unchanged.

Exactly one `search_sentinel1(SARConfig())` and one
`validate_retrieval_access(...)` call. No manual retry, restart, alternate date,
source substitution, patching, diagnostic GET or complete-validator rerun.
Passive tracing does not replace production functions or modify provider behavior.

Execution time (UTC): 2026-10-11T15:03:54.725111+00:00 → 2026-10-11T15:05:24.672631+00:00.
This is live metadata/access engineering acceptance, not calibrated SAR science.

## Actual stage matrix

Each cell records the original unchanged guard/validator's successful completion,
not successful HTTP retrieval alone. R1/R2 = REFERENCE slices; E1/E2 =
DOCUMENTARY_EVENT slices; L1/L2 = LATE_FOLLOW_UP slices. The JSON records exact
source identities, original checkpoints, scalar summaries and this expanded matrix.

| Stage | R1 | R2 | E1 | E2 | L1 | L2 |
|---|---|---|---|---|---|---|
| CDSE_discovery_identity | PASS | PASS | PASS | PASS | PASS | PASS |
| PC_source_identity | PASS | PASS | PASS | PASS | PASS | PASS |
| asset_resolution | PASS | PASS | PASS | PASS | PASS | PASS |
| VV_TIFF_structural_validation | PASS | PASS | PASS | PASS | PASS | PASS |
| manifest_interval | PASS | PASS | PASS | PASS | PASS | PASS |
| manifest_mode | PASS | PASS | PASS | PASS | PASS | PASS |
| ascending_orbit_direction | PASS | PASS | PASS | PASS | PASS | PASS |
| relative_orbit | PASS | PASS | PASS | PASS | PASS | PASS |
| GRD_product | PASS | PASS | PASS | PASS | PASS | PASS |
| platform_number | PASS | PASS | PASS | PASS | PASS | PASS |
| direct_platform_familyName | PASS | PASS | PASS | PASS | PASS | PASS |
| native_VV_measurement_witness | PASS | PASS | PASS | PASS | PASS | PASS |
| calibration_vector_structure | PASS | PASS | PASS | PASS | PASS | PASS |
| calibration_SAFE_timestamps | PASS | PASS | PASS | PASS | PASS | PASS |
| betaNought_LUT | PASS | PASS | PASS | PASS | PASS | PASS |
| sigmaNought_LUT | PASS | PASS | PASS | PASS | PASS | PASS |
| gamma_LUT | PASS | PASS | PASS | PASS | PASS | PASS |
| DN_LUT | PASS | PASS | PASS | PASS | PASS | PASS |
| noise_range_vector_structure | PASS | PASS | PASS | PASS | PASS | PASS |
| noise_range_SAFE_timestamps | PASS | PASS | PASS | PASS | PASS | PASS |
| noise_range_LUT | PASS | PASS | PASS | PASS | PASS | PASS |
| noise_azimuth_vector_structure | PASS | PASS | PASS | PASS | PASS | PASS |
| product_geolocation_structure | PASS | PASS | PASS | PASS | PASS | PASS |
| WGS84_coordinate_bounds | PASS | PASS | PASS | PASS | PASS | PASS |
| incidence_angle_scalar_structure | PASS | PASS | PASS | PASS | PASS | PASS |
| native_range_spacing | PASS | PASS | PASS | PASS | PASS | PASS |
| native_azimuth_spacing | PASS | PASS | PASS | PASS | PASS | PASS |
| product_ADS_identity_interval | PASS | PASS | PASS | PASS | PASS | PASS |
| calibration_ADS_identity_interval | PASS | PASS | PASS | PASS | PASS | PASS |
| noise_ADS_identity_interval | PASS | PASS | PASS | PASS | PASS | PASS |
| TIFF_XML_dimensions_agreement | PASS | PASS | PASS | PASS | PASS | PASS |
| thermalNoiseCorrectionPerformed | PASS | PASS | PASS | PASS | PASS | PASS |
| required_calibration_structures | PASS | PASS | PASS | PASS | PASS | PASS |
| required_noise_structures | PASS | PASS | PASS | PASS | PASS | PASS |
| final_slice_availability | PASS | PASS | PASS | PASS | PASS | PASS |

All six complete metadata validators PASS, finishing AVAILABLE with no failure
reason. All three groups ready=true; final retrieval ready=true; deepest stage K
(final assembly). No first new failure, affected failure slice or NOT_REACHED
required stage. There were no captured validator exceptions or observer errors.

M54 manifest intervals and M57 direct platform/case-only/native VV witness pass
live. M60 SAFE parser passes all 360 reviewed fields live: six ADS times + 27
calibration and 27 noise-range times per source. Generic `_parse_time` is unchanged
and strict. All later LUT/noise/geolocation/spacing/ADS/dimension/thermal/required
structure guards pass under the existing contract. All six summaries report
thermalNoiseCorrectionPerformed=false; metadata validation did not apply correction.

## Special passive noiseAzimuthVector observation

This observation reads only the ET root already returned by production parsing of
the same fetched noise XML. No extra GET, XML parse, validator call or optionality
interpretation. Only counts/booleans/summary facts are persisted; no raw XML.

| Source | List exists / declared / actual | Line coordinates = LUT values by vector | Four bounds present | Any bound absent | Production |
|---|---|---|---|---|---|
| REFERENCE/1 | true / 3 / 3 | 1692=1692, 1690=1690, 1691=1691 | 3 | 0 | PASS |
| REFERENCE/2 | true / 3 / 3 | 1693=1693, 1689=1689, 1690=1690 | 3 | 0 | PASS |
| DOCUMENTARY_EVENT/1 | true / 3 / 3 | 1691=1691, 1691=1691, 1689=1689 | 3 | 0 | PASS |
| DOCUMENTARY_EVENT/2 | true / 3 / 3 | 1691=1691, 1691=1691, 1690=1690 | 3 | 0 | PASS |
| LATE_FOLLOW_UP/1 | true / 3 / 3 | 1691=1691, 1692=1692, 1693=1693 | 3 | 0 | PASS |
| LATE_FOLLOW_UP/2 | true / 3 / 3 | 1691=1691, 1691=1691, 1691=1691 | 3 | 0 | PASS |

All six noise files contain one list and three vectors. All 18 vectors have a line
element, matching parsed line/LUT lengths and all four direct bounds:
firstAzimuthLine, lastAzimuthLine, firstRangeSample, lastRangeSample. No vector has
an absent bound. Existing production structure validation PASSes all six files.
This does not assert that bounds are universally mandatory or optional in a schema.

## Actual request/byte accounting

Counts and application response-body bytes measured in M61, not copied from M58.
Git operations are separate. Response-body bytes exclude TLS/wire overhead.

| Category | Requests | Response-body bytes | HTTP status counts |
|---|---:|---:|---|
| CALIBRATION | 6 | 6,093,708 | {'200': 6} |
| CDSE_COLLECTION | 1 | 11,989 | {'200': 1} |
| CDSE_ROOT | 1 | 3,670 | {'200': 1} |
| CDSE_SEARCH_PAGE | 3 | 436,326 | {'200': 3} |
| MANIFEST | 6 | 151,650 | {'200': 6} |
| NOISE | 6 | 2,560,801 | {'200': 6} |
| PC_COLLECTION | 1 | 11,147 | {'200': 1} |
| PC_ROOT | 1 | 2,135 | {'200': 1} |
| PC_SEARCH_PAGE | 1 | 206,182 | {'200': 1} |
| PRODUCT | 6 | 10,685,021 | {'200': 6} |
| TIFF | 162 | 98,592 | {'206': 162} |
| TOKEN | 1 | 402 | {'200': 1} |

**Total: 195 HTTP requests / 20,261,623 response-body bytes.**
**30 signing operations / 1 token HTTP acquisition.**

CDSE pagination: 3 pages (10 + 10 + 6 records), terminating without next link;
PC: 1 page (24 records), no next link. Exact six frozen sources retained.
162 VV metadata ranges are header/IFD/index metadata only. The unchanged TIFF
reader checks all requested spans against image-block offsets and rejects overlap;
all six structural validations PASS. All 24 XML bodies were fetched once per role
per source; every body hash and length matches M58.

VH TIFF requests/bytes: 0/0. ZIP downloads/bytes: 0/0. Image-block requests/bytes:
0/0. SAR pixel reads/bytes: 0/0. Calibration/noise application, sigma0/gamma0/dB,
reprojection/mosaicking/filtering, surface-slick/oil detection, persistence/risk
scoring, scientific SAR compute and AS-202 execution: all 0.

Trace/profile/logging state restored; transient token cache discarded. No token,
signed URL/SAS parameters, Authorization header/cookie or raw XML persisted.

## Deterministic identity and provenance

The original `to_dict()` validates retrieval records, support, deterministic
identity and provenance. No complete XML validator was rerun for reporting.
All 12 immediate source IDs are unchanged from M58: six distinct CDSE discovery
sources and six actual PC pixel-source records. Exact IDs are in the JSON.

### Slice fingerprints

| Frozen source | Actual fingerprint |
|---|---|
| REFERENCE/1 | `2ec6829642ea8e51b45c2aaeecf4d41985702b68445361d2abe4a85da431eb4f` |
| REFERENCE/2 | `cd952a1fd6c33807a0af9341f1753c4d2a517992277a13b9fd2424134ae77c08` |
| DOCUMENTARY_EVENT/1 | `27c77c39535bf833102dca57bf3d44f694dfecd2ab3eeb17e57abfd23016f36e` |
| DOCUMENTARY_EVENT/2 | `0b8aef219e40be84fc87e54810d426542eb1a24bf9834aaf9bc9a377d1063375` |
| LATE_FOLLOW_UP/1 | `a18146833f4028db481b800c6e5e40807b40eed9126e065b82bc1ed10af156a0` |
| LATE_FOLLOW_UP/2 | `ad9a98f3939a9f7761159641ff838ae9c6705eca949492918b4c74c40408cf2c` |

### Group fingerprints and readiness

| Group | Actual fingerprint | Ready |
|---|---|---|
| REFERENCE | `939aa61d624ca2a4f1b726b9d2ee988c4771e172b285cb836cbf54b0acd46ef9` | true |
| DOCUMENTARY_EVENT | `807567e519815cb0a4b98919ae81a9974da01194e3a3bfa2a3808a292e75455d` | true |
| LATE_FOLLOW_UP | `afe9db9ecb0b8a4137f7fda8748083e86434caf857cbb952e3c7dba1964ecb41` | true |

Retrieval product: `sentinel1_retrieval:de51027c6daa0f2812c0f2e43a041619ca1f290d16773e68c2da9f673bdbcc6e`.
Retrieval fingerprint: `de51027c6daa0f2812c0f2e43a041619ca1f290d16773e68c2da9f673bdbcc6e`. Final ready: true.

M58 product was `sentinel1_retrieval:b2d9afb757d3551dcee8c6ae79624cbb33a03b1b8207cc025ade79ce22076a08`.

The change is expected: M58 was UNAVAILABLE/METADATA_INVALID without accepted
header/metadata; M61 is AVAILABLE with validated headers, XML metadata summaries
and metadata_SHA256. Those fingerprinted state fields change slice identities,
which propagate to group/retrieval identity. Equality was not forced. Same source
IDs, XML bytes and footprint support do not imply the same accepted-access state.

Common support remains COMMON_THREE_DATE_METADATA_SUPPORT, exactly unchanged from
M58. Footprint inventory complete=true; is_lower_bound=false. Coverage gaps remain
explicit NODATA_OR_UNAVAILABLE_NEVER_ZERO_ANOMALY. Exact geometries retained in
production parameters. Footprint support is not raster pixel evaluability or oil area.

## Engineering quality gates and preservation

Focused pytest: 493 passed. Full pytest: 1780 passed,
6 existing Rasterio PendingDeprecationWarnings. External socket attempts in both
suites: 0. Ruff/diff/new-file whitespace/strict finite JSON/independent digest
reconstruction and repeat/credential scan/preservation audit: PASS. No GitHub CI claim.

All unauthorized tracked files retain pre-edit SHA-256: source/tests/config/deps,
Decisions 050–054, M49–M60 historical evidence and accepted scientific artifacts.
61 protected external hashes / 74 modes / all three safety stashes and recovery
material unchanged. Data inventory unchanged; no new raster/cache scientific product.

Schema `as201-m61-live-acceptance-after-m60-v1`. Semantic SHA-256:
`7525894e32308d55b88ff677158de2fed1d8fe71870a1731bd0280c76e08ce97`. Canonical UTF-8 JSON uses sorted keys, compact separators, stable
arrays and finite numbers. Execution timestamps, gate timings, preservation
summaries and the new commit SHA are excluded. Independent reconstruction/repeat agree.

## Chronology and current boundary

M58: HISTORICAL LIVE FAIL. M59: DIAGNOSTIC COMPLETE.
M60: OFFLINE CORRECTION PASS. These records remain byte-identical.
M61: AS201_LIVE_ACCEPTANCE_AFTER_M60 = PASS.
LIVE_READINESS: PROVED_AT_AS201_METADATA_ACCESS_BOUNDARY.
SAR_SCIENTIFIC_READINESS: UNPROVED. OIL_DETECTION: NOT STARTED.
AS-202: NOT STARTED. Decision 055: ABSENT.

No calibrated backscatter, noise-removal validity, oil/source/chemical
identification, water safety, shutdown advice or AS-202 readiness is established.
No second live attempt/diagnostic/fix occurred. Only the six authorized docs/evidence
paths change. Next: owner review; PR/merge and any new scientific milestone require
separate authorization. No PR created; no merge performed in M61.
