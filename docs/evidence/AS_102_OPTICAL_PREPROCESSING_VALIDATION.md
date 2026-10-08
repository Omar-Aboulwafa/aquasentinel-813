# AS-102 — Optical Preprocessing Real-Data Validation

**Evidence:** EV-016 (full-AOI preprocessing), EV-017 (cache/provenance/quality); journal M15.
**Status:** COMPLETE for authorized AS-102 acceptance on the feature branch; uncommitted, unpushed, not merged into main. AS-103 is unauthorized and not started.
**Base origin/main:** `0867708ea62676dcbcd0f5f83577cc120d633f26` (merged PR #5).
**Branch:** `feature/as-102-optical-preprocessing`.
**Experiment started:** `2026-10-06T10:07:14.660936+00:00` UTC / `2026-10-06T14:07:14.660936+04:00` Asia/Dubai.
**Experiment completed:** `2026-10-06T10:07:43.753204+00:00` UTC.

## Method and observation identity

This is a new implementation experiment, not a transcription of FG-01. Before network access, the runner captured its exact start timestamp. It used the existing configured Al Raha validation AOI and current AS-101 CDSE search, which returned **44 candidates**. The selected product had 0.12% scene cloud cover. PC matching used full timestamp, normalized platform, tile and relative orbit; structured product identities and independent PC generation/baseline metadata were checked.

| Field | CDSE discovery context | Actual PC pixel source |
|---|---|---|
| Item | `S2B_MSIL2A_20230428T064629_N0510_R020_T40RBN_20240831T052931` | `S2B_MSIL2A_20230428T064629_R020_T40RBN_20230428T122311` |
| Acquisition | 2023-04-28T06:46:29.024000+00:00 | 2023-04-28T06:46:29.024000+00:00 |
| Platform | sentinel-2b | sentinel-2b (provider spelling Sentinel-2B) |
| MGRS tile | 40RBN | 40RBN |
| Relative orbit | 20 | 20 |
| Processing baseline | 05.10 | 05.09 |
| Generation | 2024-08-31T05:29:31+00:00 | 2023-04-28T12:23:11.362052Z |


Same acquisition: established by observation metadata. Same processed product: **no**. Pixel equivalence: **not established**. PC provider identifiers (SAFE URI, datatake, granule, datastrip, CRS and orbit state) are retained in processing evidence. Licences retain provider-reported values: CDSE `other`, PC `proprietary`; do not replace these labels with an invented licence or claim they establish unrestricted redistribution. Attribution/licence review remains a presentation requirement.

## Resolved assets and bounded source reads

All 11 required keys came from the actual PC item, with unsigned references retained. Reflectance/SCL assets advertise COG GeoTIFF; observed raster driver is GTiff. XML uses `application/xml`. All selected hrefs use HTTPS on `sentinel2l2a01.blob.core.windows.net`. Reflectance/SCL roles are data; XML role is metadata. No SDK, account, API key, full-scene fallback, SAFE ZIP, or full-scene statistics were used. Signing material remained in memory; neither the runner log nor this report contains it.

| Key | Native metres | Observed native shape (height × width) | dtype | nodata | Read window [col,row,width,height] |
|---|---|---|---|---|---|
| B02 | 10 | 10980 × 10980 | uint16 | 0.0 | [4900, 9256, 628, 464] |
| B03 | 10 | 10980 × 10980 | uint16 | 0.0 | [4900, 9256, 628, 464] |
| B04 | 10 | 10980 × 10980 | uint16 | 0.0 | [4900, 9256, 628, 464] |
| B05 | 20 | 5490 × 5490 | uint16 | 0.0 | [2448, 4626, 318, 236] |
| B06 | 20 | 5490 × 5490 | uint16 | 0.0 | [2448, 4626, 318, 236] |
| B07 | 20 | 5490 × 5490 | uint16 | 0.0 | [2448, 4626, 318, 236] |
| B08 | 10 | 10980 × 10980 | uint16 | 0.0 | [4900, 9256, 628, 464] |
| B11 | 20 | 5490 × 5490 | uint16 | 0.0 | [2448, 4626, 318, 236] |
| B8A | 20 | 5490 × 5490 | uint16 | 0.0 | [2448, 4626, 318, 236] |
| SCL | 20 | 5490 × 5490 | uint8 | 0.0 | [2448, 4626, 318, 236] |


The four 10 m assets use native affine `[10,0,199980,0,-10,2800020]`; 20 m assets use `[20,0,199980,0,-20,2800020]`. Source CRS is EPSG:32640. A four-native-pixel halo bounds interpolation support; only these AOI windows were requested. COG blocks can exceed requested pixel windows; transferred bytes were not measured. An additional real EPSG:32639 experiment was not run; offline cross-CRS tests exercise that source CRS against the fixed EPSG:32640 target.

## XML-driven reflectance

The signed product XML established baseline **05.09**, positive finite BOA quantification **10000**, and additive offsets **-1000 for all nine bands**. Unique physicalBand/bandId mapping was parsed independently of STAC/TIFF scale defaults:

| Band | XML bandId | Parsed offset |
|---|---|---|
| B02 | 1 | -1000.0 |
| B03 | 2 | -1000.0 |
| B04 | 3 | -1000.0 |
| B05 | 4 | -1000.0 |
| B06 | 5 | -1000.0 |
| B07 | 6 | -1000.0 |
| B08 | 7 | -1000.0 |
| B8A | 8 | -1000.0 |
| B11 | 11 | -1000.0 |


Decode `rho_BOA = (DN + offset) / quantification`; for this actual product, `(DN - 1000) / 10000`. Native nodata 0 is excluded before offset arithmetic. Output is float32 without clipping; negative values survive. No DN/10000 assumption, acquisition-date inference, or copied CDSE coefficient is used. XML is namespace-tolerant and capped at 2,000,000 bytes; malformed, incomplete, duplicate, nonfinite and conflicting semantics fail explicitly.

## Canonical grid and outputs

- CRS: `EPSG:32640`; resolution: 20 m.
- Bounds: `[249020.0, 2702860.0, 255220.0, 2707420.0]`.
- Affine: `[20.0, 0.0, 249020.0, 0.0, -20.0, 2707420.0]`.
- Width: 310; height: 228.
- Grid ID: `88d76cf6265d9e0fa2802ed26324c02275e74721d4eb5b597cc9884a6d27aeec`.
- AOI geometry SHA-256: `a0fdb745672b246f569400574aa299ae4e233b8012ef54e970cdacba56687c2a`.
- Bands in processing order: `B02, B03, B04, B05, B06, B07, B08, B8A, B11`.
- **Every band has shape (228, 310), dtype float32**; aligned SCL has shape (228, 310), dtype uint8. All five masks have that shape and boolean dtype.

The output covers the snapped AOI envelope; the separate centre-rasterized `aoi_mask` identifies the polygon interior. Reflectance arrays must be used with `valid_data_mask` or, for future water features, `valid_water_mask`; finite values alone are not evidence of water eligibility. Reflectance is bilinear, categorical SCL nearest-neighbour. Bilinear downsampling is not an area average.

## SCL and measured mask statistics

Counts below are **inside the AOI**, not over the bounding rectangle or full scene. Classes absent from the table have count zero.

| SCL class | AOI pixel count |
|---|---|
| 2 | 8 |
| 3 | 341 |
| 4 | 818 |
| 5 | 54139 |
| 6 | 10211 |
| 7 | 1772 |
| 8 | 75 |
| 9 | 85 |


Class 2 retains the provider meaning dark-area pixels. Invalid classes are 0/1/2/3/7/8/9/10/11 and unknown classes. Class 6 is candidate water; 4/5 remain valid non-water.

| Metric | Observed result |
|---|---|
| aoi_pixel_count | 67449 |
| candidate_water_count | 10211 |
| valid_data_count | 65166 |
| valid_water_count | 7963 |
| valid_water_fraction_of_aoi | 0.11805957093507688 |
| water_retained_fraction | 0.7798452649103907 |


Valid-water fraction = **7963 / 67449 = 0.118059570935 (11.8060%)**.
Water-retained fraction = **7963 / 10211 = 0.779845264910 (77.9845%)**.
**2248 candidate-water pixels were excluded** (22.0155%); the conservative loss is reported, not silently compensated. Zero candidate/usable water remains a valid outcome, with a `None` retention denominator when no candidate water exists.

For each band, source SCL/nodata is mapped to its native grid; invalid contributors are removed before bilinear interpolation. A 3×3 native-water erosion plus a bilinear binary-support test requiring exactly 1 protects target water from land/cloud/shadow/nodata support. Zero support is actual bad support, never nodata that could be renormalized away. The final mask intersects acceptable support across all nine bands with finite data, target water and AOI membership.

| Band | Candidate-water pixels passing that band support |
|---|---|
| B02 | 7996 |
| B03 | 7996 |
| B04 | 7996 |
| B05 | 7996 |
| B06 | 7996 |
| B07 | 7996 |
| B08 | 7963 |
| B11 | 7996 |
| B8A | 7996 |


B08 is the limiting support in this observation; all-band intersection retains 7,963 pixels. This is a reproducible mask-accepted-water count, not independent confirmation of water or aquatic radiometric suitability.

## Finite valid-water reflectance ranges

Computed only where `valid_water_mask` is true; no indices, chlorophyll, anomaly score or HAB interpretation was computed.

| Band | Minimum BOA reflectance | Maximum BOA reflectance |
|---|---|---|
| B02 | 0.01939687505364418 | 0.3334999978542328 |
| B03 | 0.027904687449336052 | 0.39173126220703125 |
| B04 | 0.003068750025704503 | 0.4461812376976013 |
| B05 | -0.0015999999595806003 | 0.4860000014305115 |
| B06 | -0.0044999998062849045 | 0.482699990272522 |
| B07 | -0.00279999990016222 | 0.48510000109672546 |
| B08 | -0.0013562500244006515 | 0.4926687479019165 |
| B11 | 0.008100000210106373 | 0.5462999939918518 |
| B8A | -0.002899999963119626 | 0.49230000376701355 |


The preserved negative values demonstrate unclipped decoding. Some SCL-water pixels have bright visible/SWIR reflectance; SCL and conservative interpolation safeguards do not certify that every retained pixel is optically pure coastal water. Mixed/shallow/turbid-water misclassification and aquatic correction remain scientific limitations rather than reasons to alter masks silently.

## Provenance and cache verification

Actual PC source ID:
`stac:ef177b34b0fa3cabbb6d613d65f1c55d8ea4c5959326bb8896ec51d111792740:sentinel-2-l2a:S2B_MSIL2A_20230428T064629_R020_T40RBN_20230428T122311`

CDSE discovery source ID (context only):
`stac:727c9c270e50361fad55ba968c9f8e618dea21f690ff8ae24cfb77374ae151f7:sentinel-2-l2a:S2B_MSIL2A_20230428T064629_N0510_R020_T40RBN_20240831T052931`

Derived product ID:
`optical:0725a908d21cd655e83f70d2bb11247dc0f1516f0c00ea275efc3239113ee4a6`

Cache ID:
`0725a908d21cd655e83f70d2bb11247dc0f1516f0c00ea275efc3239113ee4a6`

Processing version: `as102-v1`. The derived record references **only the actual PC source ID** as its pixel source; observation match, distinct processing products, unsigned XML/native assets, decoding, AOI/grid, native windows/nodata, resampling, mask/support policies, statistics and software versions remain JSON-only parameters.

The cache is `data/cache/as102/<cache_id>/`: AOI-sized `arrays.npz` and canonical `manifest.json`, published by an atomic directory rename. File SHA-256 is verified, then cache identity/schema/grid/shapes/dtypes/mask statistics/provenance are validated. Offline corruption tests cover file bytes, grid, statistics, malformed JSON and source identity.

The real runner reloaded the known cache ID with catalog resolution, signing, XML, native raster access and `rasterio.open` replaced by failing sentinels. Every band and mask was array-equal (including NaNs), statistics/source/provenance were equal, and no sentinel fired. **Cache equivalence PASS; second known-ID load required zero raster/signing work and no network access.** Cache/raw EO files are ignored and excluded from Git.

A first fresh run at `2026-10-06T10:02:33.238907+00:00` obtained identical grid/counts/key. Its generated cache was preserved outside the repository while a second fresh bounded read verified the finalized typed-source/security implementation at the timestamp above. Neither run was a full-tile download.

## Software, tests and reproducibility

Validated Python 3.11.16; new direct pins NumPy 2.2.6 and Rasterio 1.4.3 (bundled GDAL 3.9.3); retained pystac-client 0.9.0. No other direct dependency was added. **213 offline tests passed**, retaining all existing 97; Ruff and diff check passed. Two PendingDeprecationWarnings originate from Rasterio calling its transitive Affine package; they are reported and do not fail processing/tests. Historical AS-003 17 and AS-101 97 baselines remain separate.

Reproduce in the configured Python 3.11 environment:

```python
from aquasentinel.runtime import build_runtime_context
from aquasentinel.ingestion.sentinel2 import search_sentinel2
from aquasentinel.preprocessing.optical import preprocess_optical_scene

context = build_runtime_context()
candidates = search_sentinel2(context)
candidate = next(c for c in candidates if c.item_id ==
    "S2B_MSIL2A_20230428T064629_N0510_R020_T40RBN_20240831T052931")
scene = preprocess_optical_scene(context, candidate)
cached = preprocess_optical_scene(context, known_cache_id=scene.cache_id)
```

Catalogs/signing/network rules are external and can change. If the known product disappears or metadata changes, fail explicitly and record a new matched experiment; do not invent equivalence or silently update this evidence.

## Scientific limits, remaining evidence and presentation use

L2A BOA surface reflectance is **not automatically aquatic remote-sensing reflectance**. SCL can misclassify coastal, mixed, shallow and turbid water and cloud-shadow-over-water. The support policy deliberately removes shoreline/uncertain water; it is not an empirically calibrated ecological validity test. This observation does not establish HABs, toxic algae, toxins, chlorophyll concentration, safe/unsafe water, intake danger, accuracy, or warning lead time. Field/laboratory validation remains necessary. AS-103 is not authorized or started.

EV-014's historical PENDING checkpoint, later FG-01 PASS/READY and EV-015 XML finding remain unchanged. EV-016/EV-017 add implementation evidence; they do not retroactively turn the original probe into preprocessing.

Recommended captures (still pending): dated nine-band/grid/count result card; AOI/candidate-water/retained-water/support-exclusion map; PC-versus-CDSE lineage diagram; product-XML decoding table; checksum/cache-hit test summary. Include acquisition/processing/experiment dates and licence/attribution context. Never show SAS/signing material or present masks as confirmed biological evidence.

Candidate slide: **“From 44 catalog candidates to 7,963 traceable, conservatively masked water pixels.”**
