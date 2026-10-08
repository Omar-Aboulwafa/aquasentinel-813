# AS-102 — Optical Preprocessing

## Task

Authorized implementation on 6 October 2026, branch `feature/as-102-optical-preprocessing`, base `0867708ea62676dcbcd0f5f83577cc120d633f26` (merged PR #5). No commit, push, or AS-103 work is authorized.

## Goal

Transform CDSE-discovered Sentinel-2 L2A candidates into AOI-sized, XML-decoded, aligned surface-reflectance arrays with conservative water-quality masks and reproducible Planetary Computer pixel lineage.

## Inputs

Existing runtime/AOI and AS-101 candidates; Planetary Computer anonymous STAC and transient SAS signing; native B02/B03/B04/B05/B06/B07/B08/B8A/B11, SCL and product XML. No user credentials.

## Outputs

Typed `PreprocessedOpticalScene`, fixed AOI grid, masks/statistics, actual-PC `SourceRecord`, `DerivedProductRecord`, checksum-verified AOI cache, offline tests and separately recorded live validation.

## Files Likely to Change

- `pyproject.toml`, `config/default.toml`, `src/aquasentinel/config/{models,loader,__init__}.py`.
- New `src/aquasentinel/ingestion/sentinel2_assets.py` and `planetary_computer.py`.
- New `src/aquasentinel/preprocessing/{__init__,models,metadata,alignment,masks,optical,cache}.py`.
- New focused configuration, ingestion and preprocessing tests.
- This plan, `docs/DECISIONS.md`, `docs/PROJECT_STATE.md`, `docs/HANDOFF.md`, presentation journal/index and a new validation evidence report. Historical probe reports remain intact.

## Dependencies

Only new direct dependencies: `numpy==2.2.6` (array arithmetic/masking without SciPy) and `rasterio==1.4.3` (bounded COG reads, CRS transformation, rasterization/reprojection). Both support Python 3.11. Standard-library urllib, JSON and ElementTree handle signing/XML; existing `pystac-client==0.9.0` handles catalogs. No unrelated dependency upgrades.

## Acceptance Criteria

Strict same acquisition/platform/MGRS/orbit match; independently retained processing identity; all nine native bands and SCL; complete XML quantification and band-specific offsets; no full-scene fallback or persisted SAS; deterministic EPSG:32640 20 m AOI grid (Al Raha bounds `[249020,2702860,255220,2707420]`, 310 × 228); float32 reflectance and uint8 SCL; bilinear reflectance/nearest categorical resampling; all-band conservative water support; explicit zero-water outcome and fraction denominators; PC-only pixel-source lineage; deterministic atomic cache with SHA-256 and offline known-ID reload. Existing 97 tests plus new offline coverage, Ruff and diff check pass. Full-AOI real acceptance and cache equivalence must succeed before completion.

## Scientific Guardrails

BOA surface reflectance is not automatically aquatic remote-sensing reflectance. Decode `(DN + band_offset) / quantification` using the actual PC XML; mask nodata first, preserve negative/zero/>1 values, never assume DN/10000. SCL 2 means dark-area pixels. Invalid classes `{0,1,2,3,7,8,9,10,11}` and unknowns are excluded; only class 6 is candidate water. No HAB, toxins, chlorophyll, water-safety or operational lead-time claims.

## Risks

Different provider processing products; missing/conflicting XML; transient network/signing failures; token leakage through GDAL diagnostics; coastal SCL errors; bilinear contamination; conservative loss of shoreline water; cache corruption; cross-CRS overlap. Fail explicitly, sanitize transport errors and retain processing/masking evidence.

## Validation

Offline synthetic tests for config, strict matching/assets, signing security, XML, decoding, canonical/cross-CRS alignment, every SCL class, contamination safeguards, zero-water statistics, provenance and cache corruption/offline reuse. Run `.venv/bin/python -m pytest -v`, `.venv/bin/python -m ruff check .`, `git diff --check`. After tests, capture exact UTC/Dubai timestamp before a live CDSE→PC full-AOI run; report all grids, shapes, SCL counts, masks/fractions, valid-water ranges, provenance and cache reload with network/signing disabled. Inspect full diff, secret-marker counts and ignored caches.

## Non-Goals

AS-103, spectral indices, atmospheric/aquatic correction, hazard/risk/dashboard work, full-tile downloads, cloud-probability P0, additional geospatial frameworks, commits or pushes.

## Execution Status

Plan persisted before source changes. Implementation acceptance COMPLETE on the uncommitted feature branch: 213 offline tests passed, Ruff/diff check passed, fresh full-AOI real acceptance passed, and known-ID cache reload was equivalent with external access blocked. No commit/push/PR/merge occurred; AS-103 remains unauthorized and unimplemented.


## Final Implemented Contract and API

`preprocess_optical_scene(context, candidate)` resolves the strict PC observation, signs bounded XML/native COG reads, decodes float32 BOA arrays, aligns to the fixed grid, computes masks/statistics/provenance and writes the AOI cache. `preprocess_optical_scene(context, known_cache_id=cache_id)` reloads locally without catalog, signing, XML or raster access and checks the configured AOI/grid. The normal pytest suite is offline.

Focused modules are configuration, `ingestion/planetary_computer.py` (bounded HTTPS/signing), `ingestion/sentinel2_assets.py` (identity/assets), and `preprocessing/{models,metadata,alignment,masks,optical,cache}.py`. Splitting XML and transport from orchestration keeps semantic/security responsibilities testable. Existing AS-101, runtime and generic provenance modules remain unchanged.

`PreprocessedOpticalScene` exposes the actual-PC and CDSE-context identities, typed fixed grid, nine float32 arrays in explicit band order, uint8 SCL, five boolean masks, fraction/count statistics, JSON processing parameters, deterministic cache ID and derived provenance. The resolved source carries provider processing identifiers, unsigned assets, native observed grids/nodata and decoding metadata. The returned arrays cover the snapped AOI envelope; use the masks to select polygon/quality-eligible pixels. Finite reflectance alone is not water eligibility.

Source quality is nearest-mapped to each native band. Invalid SCL/nodata contributors become NaN before bilinear reprojection. Conservative water support erodes the native water-and-nodata-valid boolean grid by 3×3, then bilinearly reprojects it with zero treated as bad support (not nodata) and accepts only exactly 1. Final water intersects support across all nine bands with target SCL, AOI membership and finite data. This extra erosion is conservative and deliberately discards some otherwise classified water. It is not a calibrated coastal-water classifier.

The target uses an outward-snapped, densified transformed AOI envelope and centre-based polygon mask. Native reads have a four-pixel halo, expected 10/20 m numeric grids, explicit nodata and bounded-size/full-scene rejection; no provider 20 m substituted visible-band assets or fallback downloads. B02/B03/B04/B08 remain native 10 m; B05/B06/B07/B8A/B11/SCL are 20 m. Cross-CRS tests use source EPSG:32639 against the same EPSG:32640 target.

Cache format is AOI-sized compressed NumPy `arrays.npz` plus grid/lineage `manifest.json`, rather than extra GeoTIFF writes. It preserves exact arrays/dtypes and avoids any raster-driver work on reload. Identity includes actual PC/CDSE match and processing, unsigned assets, XML coefficients, geometry digest, target grid, band order, mask/resampling/support policies, processing and software versions. An atomic temporary-directory rename publishes the cache; SHA-256, schema, key, grid/shape/dtype, statistics and lineage checks reject corruption. Manifests serialize canonically; creation time is evidence, not part of the stable cache key.

## Validation and Limitations

See [EV-016/EV-017 real acceptance](evidence/AS_102_OPTICAL_PREPROCESSING_VALIDATION.md) and journal M15 for exact timestamps, product IDs, native windows, XML mapping, grid, SCL distribution, valid-water ranges, provenance and cache identity. Finalized fresh run: 6 October 2026, `10:07:14.660936+00:00` / `14:07:14.660936+04:00` Asia/Dubai. AOI 67,449; valid data 65,166; candidate water 10,211; valid water 7,963; AOI fraction 0.11805957093507688; retained fraction 0.7798452649103907. Excluded water 2,248. All nine band shapes are (228,310), float32; SCL/masks align.

All prior 97 tests plus 116 new offline cases pass: **213 passed**. NumPy 2.2.6, Rasterio 1.4.3, Python 3.11.16 and bundled GDAL 3.9.3 were actually used. Two PendingDeprecationWarnings come from Rasterio's calls into its transitive Affine package; no test/data-access failure resulted. Installation used the existing Python 3.11 virtual environment and `uv --cache-dir /tmp/as102-uv-cache pip install --python .venv/bin/python numpy==2.2.6 rasterio==1.4.3`; `pystac-client` was retained. Project pins make the two added direct dependencies reproducible on another Python 3.11 machine.

Live all-band/source-window acceptance and a second fresh read succeeded. Cache equivalence was checked with network-related and raster entry points replaced by failing sentinels. An additional real EPSG:32639 scene was not required/run; synthetic cross-CRS coverage is present. Exact transferred bytes were not measured; remote COG block reads can exceed requested windows.

SCL is imperfect over coastal/mixed/shallow/turbid water and cloud shadows. Bright visible/SWIR values can survive this classification/support policy; the mask is eligibility evidence, not validated aquatic radiometry. Preserve negative reflectance, do not silently relax masks, and accept zero-water outcomes. L2A BOA reflectance is not aquatic Rrs and does not establish any biological hazard, chlorophyll concentration, toxins, water safety, intake danger or lead time. Provider-reported licence labels and external-service availability require their own presentation/release review. Presentation captures and independent science validation remain pending; neither blocks the specifically authorized AS-102 mechanics acceptance.

## Completion Gate

All authorized implementation gates are satisfied: approved clean base/task branch/plan; only NumPy/Rasterio added; strict identity/assets; bounded transient access; XML semantics; all nine aligned bands and SCL; fixed grid/cross-CRS test; conservative masks/statistics/zero-water behavior; actual-PC lineage; deterministic atomic cache/checksum/corruption/offline reload; 213 tests/Ruff/diff check; fresh full-AOI acceptance and cache equivalence; scientific limits; Decisions 039–045; state/handoff/journal/evidence updates; no tracked raw/cache/signing material. **AS-102 COMPLETE for feature-branch implementation review, not complete/merged on main.** No AS-103 work, commit or push.
