# AS-106 M33 — April 3 upstream preparation and verified handoff

## 1. M33 / E33 / EV-037 scope

PASS — APRIL-3 UPSTREAM PREPARATION + VERIFIED HANDOFF COMPLETE; M34 INPUTS READY / NOT RUN.

Only the owner-frozen April 3 observation was newly processed through unchanged production AS-102→103→104→105. No AS-106 recurrence was computed. No alternate dates, threshold tuning, new provider, dependency, source or test change. External adapter code served execution, instrumentation and typed reconstruction only.

## 2. Official base

- **Official main / branch base:** `200affdb7fb6f8801744a192511e4200cc0d100d`

Branch: `data/as-106-april3-upstream-preparation`; worktree `/workspace/aquasentinel-813-as106-m33`. M31 merged via PR #17; M32 via PR #18. Initial fetch verified exact base and clean worktree. Git publication follows preparation and local gates; no PR/merge is part of M33.

## 3. Frozen M32 sequence and digest

- **Selection inventory SHA-256:** `570792066c1997b9a403249d994c4e7367bf2f1dafc6473b6e30df20cd6481d5`

1. `2023-04-03T06:46:21.024000Z` — newly prepared by M33.
2. `2023-04-28T06:46:29.024000Z` — already accepted; read-only comparison/reconstruction.

Both M32 inventory files are byte-identical. No selection rerun or outcome-based exclusion.

## 4. Exact April 3 CDSE / PC identity

- **acquired_at:** `2023-04-03T06:46:21.024000+00:00`
- **cdse_item_id:** `S2A_MSIL2A_20230403T064621_N0510_R020_T40RBN_20240824T175307`
- **mgrs_tile:** `40RBN`
- **pc_item_id:** `S2A_MSIL2A_20230403T064621_R020_T40RBN_20230403T115452`
- **platform:** `sentinel-2a`
- **relative_orbit:** `20`
- **required_pc_processing_baseline:** `05.09`
- **Actual PC generation time:** `2023-04-03T11:54:52.560526Z`

Matching preserves acquisition/platform/tile/orbit and requires the unique exact 05.09 product. CDSE discovery and PC pixel products have different processing histories; pixel equivalence is not claimed.

## 5. Actual network / data access

Only existing allowed hosts: `stac.dataspace.copernicus.eu`, `planetarycomputer.microsoft.com`, `sentinel2l2a01.blob.core.windows.net`. **7 observed Python HTTP operations**, all successful: 2 CDSE metadata GETs (collection/exact item); PC root/collection GETs and existing resolver POST search; 1 existing reusable account/container token GET; 1 bounded product XML GET. Signing is credential-free, transient and reused for selected assets; token state cleared after access. No token, signed URL or raw STAC response persisted.

The resolver query reconciles only the exact acquisition (±1-second existing resolver bounds), not alternative date selection. **10 native COG window reads**, required assets `B02/B03/B04/B05/B06/B07/B08/B8A/B11/SCL`; product-metadata XML uses the production 2,000,000-byte bound.

| Native assets | Resolution | Full dimensions | Window [col,row,width,height] | Returned shape |
| --- | --- | --- | --- | --- |
| B02/B03/B04/B08 | 10 m | 10980 × 10980 | [4900, 9256, 628, 464] | 464 × 628 |
| B05/B06/B07/B8A/B11/SCL | 20 m | 5490 × 5490 | [2448, 4626, 318, 236] | 236 × 318 |

Production Rasterio/GDAL COG window/range access succeeded, with bounded native headers and existing halo/read settings. Internal GDAL HTTP request counts and transferred bytes are **not measured / not exposed** by this Python audit; ten reads are not ten HTTP requests. Unexpected hosts / unrelated asset attempts / full SAFE, ZIP or tile downloads: **0** at observed boundaries. No preview, thumbnail, unrelated scene or new March request. After ingestion all processing/reconstruction was offline. Initial Git fetch and final authorized branch push are separate from EO access.

## 6. AS-102 April 3 result

- **Product ID:** `optical:441badc774727bcff001ccb02e8e936988b819db8cecc3a247d5d80572ec6499`
- **Cache ID:** `441badc774727bcff001ccb02e8e936988b819db8cecc3a247d5d80572ec6499`
- **Cache path:** `/workspace/aquasentinel-813-as106-m33/data/cache/as102/441badc774727bcff001ccb02e8e936988b819db8cecc3a247d5d80572ec6499`
- **Grid ID:** `88d76cf6265d9e0fa2802ed26324c02275e74721d4eb5b597cc9884a6d27aeec`

Grid: EPSG:32640, 20 m, 310 × 228, bounds [249020, 2702860, 255220, 2707420]. Source ID: `stac:ef177b34b0fa3cabbb6d613d65f1c55d8ea4c5959326bb8896ec51d111792740:sentinel-2-l2a:S2A_MSIL2A_20230403T064621_R020_T40RBN_20230403T115452`. XML baseline 05.09; BOA quantification 10000; all nine band offsets −1000. Production decoding `(DN + band_offset) / quantification`, negative reflectance preserved. No reflectance/grid/mask/resampling change.

| Statistic | Count/fraction |
| --- | --- |
| aoi_pixel_count | 67449 |
| candidate_water_count | 8501 |
| valid_data_count | 63166 |
| valid_water_count | 6096 |
| valid_water_fraction_of_aoi | 0.09037939776720189 |
| water_retained_fraction | 0.7170921068109635 |

Interpolation support and each of nine per-band water-support counts: **6,096**; 2,405 candidate-water pixels excluded by existing support safeguards. Cache typed reload, identity/parameters/provenance/arrays and masks match **PASS**.

| Cache file | Bytes | SHA-256 |
| --- | --- | --- |
| arrays.npz | 1647851 | 350e4ce5fe117942c26d54e611db6daff2bef9eda7bc80da810338ae530bcb22 |
| manifest.json | 28211 | 23c024f8a002aad8ecaf1b930b6acf01c55a6404b25f67b70b3c8ac9c19e4b67 |

Local ignored cache only; not committed.

## 7. AS-103 April 3 result

- **Product ID:** `spectral:6bb1ee8db74f19f7fd03e1fd72c99d1c6fee88c6367b970913e341b55fa8a73c`
- **AS-102 parent:** `optical:441badc774727bcff001ccb02e8e936988b819db8cecc3a247d5d80572ec6499`
- **Input semantic fingerprint:** `3514eae5b3356531d40357feade7f1c1b1e6728451a9bd19b2920d23ea3f99ce`

Version `as103-v1`; all six canonical feature valid counts **6,096** (100% parent valid water). Negative-input, denominator-rejection and nonfinite-result counts 0; NDCI-like out-of-nominal-range count 0. Full feature summaries/diagnostics retained in JSON. Parent-aware validation, deterministic repeat and input immutability **PASS**. Lineage: actual PC SourceRecord → AS-102 → AS-103. No chlorophyll/HAB interpretation.

## 8. Fixed March references

| Acquired at | Frozen spectral product ID | Offline reconstruction |
| --- | --- | --- |
| 2023-03-04T06:47:51.024000+00:00 | spectral:6409add4aef5c95cfe773bfabfa1f554bdda2968241712bda4debefa34b57130 | PASS |
| 2023-03-09T06:47:19.025000+00:00 | spectral:dafde3d3a2a94d44b62a9d5605bce497b03021e517b7dd6b081607719f37efa1 | PASS |
| 2023-03-14T06:46:41.024000+00:00 | spectral:721d847a7ed032426c8124e42507b60c3f9a6ae86a4e9ad406176646c35abff7 | PASS |
| 2023-03-24T06:46:21.024000+00:00 | spectral:1002b083b3d7637abd67446ef171e0746fe3bd839706cadff18571ac1c51af66 | PASS |
| 2023-03-29T06:46:29.024000+00:00 | spectral:c4de2a86bb7b15a6a8bc49373823bb944be7e6787db383b0959c93c51f3464d5 | PASS |

March references were reconstructed offline from already accepted caches; all five frozen IDs and fingerprints match. No cache mutation or new March network access. Real SourceRecord/AS-102/AS-103 records registered normally; descriptor validation and registry immutability PASS. Reference interval `[2023-03-01T00:00:00Z, 2023-04-01T00:00:00Z)`; minimum observations 5; no extra March/April reference.

## 9. AS-104 April 3 result

- **Product ID:** `temporal:71f6be2d8437e91f7cf213df0bd876897febebe630a02a20bb151a5d852edb11`
- **Target AS-103:** `spectral:6bb1ee8db74f19f7fd03e1fd72c99d1c6fee88c6367b970913e341b55fa8a73c`
- **Identity digest:** `71f6be2d8437e91f7cf213df0bd876897febebe630a02a20bb151a5d852edb11`
- **Target semantic input fingerprint:** `d4b8b7352650a8636437547999da747571d194aa21adfaa06019d6120f8b666a`
- **Output content fingerprint:** `949d75aa4642dd2680e0428265da423a8cb855f6965ed30f831b3c91ddf80a92`

| Feature | Target valid | Eligible / valid rank / anomaly | Zero MAD | Above / below baseline |
| --- | --- | --- | --- | --- |
| green_blue_ratio | 6096 | 789 | 0 | 662 / 127 |
| green_red_ratio | 6096 | 793 | 0 | 170 / 623 |
| mci_like | 6096 | 794 | 0 | 646 / 148 |
| ndci_like | 6096 | 784 | 0 | 667 / 117 |
| red_edge2_red_ratio | 6096 | 793 | 0 | 642 / 151 |
| red_edge_red_ratio | 6096 | 793 | 0 | 703 / 90 |

Equal-baseline and numeric-rejection counts 0. Full rank/deviation/centre/scale/observation summaries and reference fingerprints are preserved in JSON. Median centre; scale 1.4826×MAD; deviation target−centre; robust z only positive scale; exact-tie empirical midrank. No epsilon/fallback/clipping/imputation/mask relaxation. Independent scalar checks **18/18 PASS**; deterministic reverse-caller-order repeat **PASS**; synthetic future observation exclusion **PASS**; causality and exact references **PASS**. Parent/registry contracts validated normally. Lineage includes target plus ordered five March AS-103 derived products.

## 10. Common-contract comparison with April 28

**PASS before AS-105 execution.** Existing `comparison_contract` projection canonical JSON identical, SHA-256 `8e13d83acf214e35465077d893178f6998f9a1976cd01582d4d468601f2513fc`.

| Field | Result |
| --- | --- |
| algorithm | PASS |
| feature_order | PASS |
| formulas | PASS |
| grid | PASS |
| mgrs_tile | PASS |
| minimum_observations | PASS |
| pc_processing_baseline | PASS |
| processing_version | PASS |
| reference_acquired_at | PASS |
| reference_period | PASS |
| reference_product_ids | PASS |
| relative_orbit | PASS |
| upstream_contract | PASS |

| Upstream field | Result |
| --- | --- |
| aoi_geometry_digest | PASS |
| as102_version | PASS |
| as103_version | PASS |
| bands | PASS |
| catalog | PASS |
| collection | PASS |
| decoding | PASS |
| interpolation_support_policy | PASS |
| mask_policy | PASS |
| resampling | PASS |

Target-specific IDs/acquisition/satellite/generation/pixel support may differ and are excluded by the existing common contract. No weakened compatibility check.

## 11. AS-105 April 3 result

- **Product ID:** `hab_geometry:7e3a4ba3ba8fb394ca874415c62f7fed7a160609c6dee458d59b35ea0c12cd52`
- **AS-104 parent:** `temporal:71f6be2d8437e91f7cf213df0bd876897febebe630a02a20bb151a5d852edb11`
- **Input fingerprint:** `b8bbe965ed3b57e8abbbaa5560784b274b89e9657e3cffb9b378c805f1021a24`
- **Output fingerprint:** `ecea6b13cded3553b5d4e8e373e9b8749e3584aba943e808cee4b057b8b731c9`

Frozen Decision 050 unchanged. P **794**; target valid water **6,096**; candidates **88**; candidate/P **0.11083123425692695 (11.083123%)**; candidate/target-water **0.014435695538057743 (1.443570%)**, descriptive only. **15 regions**, **35,200 m² / 0.0352 km²**; largest 66 pixels; ten one-pixel regions. No morphology/minimum-area/minimum-pixel change.

| Family | Available | Evidence |
| --- | --- | --- |
| red_edge_b5_vs_red | 794 | 5 |
| red_edge_b6_vs_red | 793 | 0 |
| red_edge_line_height | 794 | 272 |
| visible_green_vs_blue | 789 | 151 |
| visible_green_vs_red | 793 | 1 |

| Feature | Eligible | Evidence |
| --- | --- | --- |
| green_blue_ratio | 789 | 151 |
| green_red_ratio | 793 | 1 |
| mci_like | 794 | 272 |
| ndci_like | 784 | 5 |
| red_edge2_red_ratio | 793 | 0 |
| red_edge_red_ratio | 793 | 5 |

Vote histogram on P: 0→453, 1→253, 2→88, 3–5→0. All 88 candidates have two family votes.

| Region ID | Pixels | Area m² | Participating families | Projected bbox |
| --- | --- | --- | --- | --- |
| hab_geometry:7e3a4ba3ba8fb394ca874415c62f7fed7a160609c6dee458d59b35ea0c12cd52:region:1 | 1 | 400.0 | red_edge_line_height, visible_green_vs_blue | [253380.0, 2706540.0, 253400.0, 2706560.0] |
| hab_geometry:7e3a4ba3ba8fb394ca874415c62f7fed7a160609c6dee458d59b35ea0c12cd52:region:2 | 1 | 400.0 | red_edge_line_height, visible_green_vs_blue | [253660.0, 2706500.0, 253680.0, 2706520.0] |
| hab_geometry:7e3a4ba3ba8fb394ca874415c62f7fed7a160609c6dee458d59b35ea0c12cd52:region:3 | 1 | 400.0 | red_edge_line_height, visible_green_vs_blue | [253560.0, 2706480.0, 253580.0, 2706500.0] |
| hab_geometry:7e3a4ba3ba8fb394ca874415c62f7fed7a160609c6dee458d59b35ea0c12cd52:region:4 | 1 | 400.0 | red_edge_line_height, visible_green_vs_blue | [253620.0, 2706480.0, 253640.0, 2706500.0] |
| hab_geometry:7e3a4ba3ba8fb394ca874415c62f7fed7a160609c6dee458d59b35ea0c12cd52:region:5 | 66 | 26400.0 | red_edge_line_height, visible_green_vs_blue | [253520.0, 2706200.0, 253680.0, 2706480.0] |
| hab_geometry:7e3a4ba3ba8fb394ca874415c62f7fed7a160609c6dee458d59b35ea0c12cd52:region:6 | 2 | 800.0 | red_edge_line_height, visible_green_vs_blue | [253600.0, 2706120.0, 253620.0, 2706160.0] |
| hab_geometry:7e3a4ba3ba8fb394ca874415c62f7fed7a160609c6dee458d59b35ea0c12cd52:region:7 | 1 | 400.0 | red_edge_line_height, visible_green_vs_blue | [253660.0, 2706060.0, 253680.0, 2706080.0] |
| hab_geometry:7e3a4ba3ba8fb394ca874415c62f7fed7a160609c6dee458d59b35ea0c12cd52:region:8 | 1 | 400.0 | red_edge_line_height, visible_green_vs_blue | [253880.0, 2705700.0, 253900.0, 2705720.0] |
| hab_geometry:7e3a4ba3ba8fb394ca874415c62f7fed7a160609c6dee458d59b35ea0c12cd52:region:9 | 1 | 400.0 | red_edge_line_height, visible_green_vs_blue | [253540.0, 2705680.0, 253560.0, 2705700.0] |
| hab_geometry:7e3a4ba3ba8fb394ca874415c62f7fed7a160609c6dee458d59b35ea0c12cd52:region:10 | 4 | 1600.0 | red_edge_line_height, visible_green_vs_blue | [252640.0, 2705280.0, 252700.0, 2705340.0] |
| hab_geometry:7e3a4ba3ba8fb394ca874415c62f7fed7a160609c6dee458d59b35ea0c12cd52:region:11 | 1 | 400.0 | red_edge_line_height, visible_green_vs_blue | [252360.0, 2705200.0, 252380.0, 2705220.0] |
| hab_geometry:7e3a4ba3ba8fb394ca874415c62f7fed7a160609c6dee458d59b35ea0c12cd52:region:12 | 2 | 800.0 | red_edge_line_height, visible_green_vs_blue | [252320.0, 2705160.0, 252340.0, 2705200.0] |
| hab_geometry:7e3a4ba3ba8fb394ca874415c62f7fed7a160609c6dee458d59b35ea0c12cd52:region:13 | 4 | 1600.0 | red_edge_line_height, visible_green_vs_blue | [251360.0, 2704920.0, 251400.0, 2704960.0] |
| hab_geometry:7e3a4ba3ba8fb394ca874415c62f7fed7a160609c6dee458d59b35ea0c12cd52:region:14 | 1 | 400.0 | red_edge_b5_vs_red, red_edge_line_height | [253100.0, 2704920.0, 253120.0, 2704940.0] |
| hab_geometry:7e3a4ba3ba8fb394ca874415c62f7fed7a160609c6dee458d59b35ea0c12cd52:region:15 | 1 | 400.0 | red_edge_line_height, visible_green_vs_blue | [251240.0, 2704820.0, 251260.0, 2704840.0] |


Full per-region family evidence counts, projected polygons and feature summaries are in JSON. Typed parent-aware validation, independent candidate/family-mask reproduction, rasterization-to-label roundtrip and deterministic repeat **PASS**. Result is frozen observational anomaly geometry, not a bloom or biological validation.

## 12. Handoff construction

- **Directory:** `/workspace/aquasentinel-handoffs/as106/m33/april3/7e3a4ba3ba8fb394ca874415c62f7fed7a160609c6dee458d59b35ea0c12cd52`
- **Format:** `as106-m33-handoff-v1`

**88 scientific arrays: 61 AS-104 + 27 AS-105**, with stage prefixes, numeric dtypes/no pickle. Typed metadata includes grid, IDs/parents/times, all temporal maps/masks/statistics/diagnostics/parameters/provenance, geometry labels/masks/votes/regions/statistics/parameters/provenance, fixed reference metadata, software, frozen selection and per-array semantic hashes/dtypes/shapes. No remote asset href or credentials. Existing AS-104/M29 conventions combined with explicit stage prefixes; external adapter only.

| File | Bytes | SHA-256 | Mode |
| --- | --- | --- | --- |
| SHA256SUMS.txt | 157 | ea33a3aee348a30b006ceaa17fb4685b351a13f9812cb14ad01f2e4c63c19d90 | 0444 |
| arrays.npz | 212461 | c7ca935af29f760623f13dc2350302521de5847390e699a405882f472ed92e21 | 0444 |
| manifest.json | 123984 | add610b9c52fd94a46f5b118dbe9bddec9dae9b11420e65798b748ce03b94475 | 0444 |

Directory **0555**; files **0444** after validation. SHA256SUMS lists NPZ/manifest; JSON records the sums-file hash too. Cache and handoff are different local artifacts, both out of Git.

Initial external adapter assertions failed on (1) JSON coordinate lists versus live tuples and (2) historical M29 display-only `geometry_type` / `polygon_part_count` keys outside the typed region model. Corrected only the temporary adapter: canonical serialization for region equality and explicit projection of those two display fields. All scientific arrays/accepted products stayed unchanged; no AS-102/104/105 public rerun or additional network. Offline AS-103 identity reverification was authorized and identical. Historical failed log is retained outside Git; final typed tests passed.

## 13. Fresh offline typed reconstruction PASS

Fresh process disables socket/HTTP/raster network, cache load, public AS-102/103/104/105 extraction and recurrence. Read checksum-verified manifest and `numpy.load(..., allow_pickle=False)`; verify all array inventory hashes/dtypes/shapes; rebuild AnalysisGrid and DerivedProductRecords; instantiate TemporalFeatureScene then HABAnomalyGeometryScene with explicit typed regions; call parent-aware geometry validation. External recipe: `/tmp/as106-m33-handoff.py` and `/tmp/as106-m33-offline.py`; handoff retains all typed metadata and stage-prefixed arrays needed to reproduce it without those scripts.

April 3 typed temporal **PASS**, typed geometry **PASS**, **88/88 array checks PASS**, exact IDs/fingerprints/statistics/regions **PASS**, parent-aware validation **PASS**. Separately reconstruct existing accepted April 28 AS-104/M29 artifacts **PASS**, accepted identities and common contract preserved. Network/public extraction/cache-load/recurrence attempts **0**. Existing validator internal integrity regeneration is permitted; no public extraction or real recurrence executed. **M34 INPUTS READY**, not M34 PASS.

## 14. Protected-artifact preservation

Before processing: 111 tracked-file hashes, 32 protected external-file hashes, nine permission records and exact stash inventory captured. After scientific work all pre-existing tracked files were identical; only the eight authorized documentation paths subsequently change. Twelve files in six accepted AS-102 caches, three AS-104 April 28 handoff files, four M29 bundle files and thirteen external recovery files remain byte-identical; permission records unchanged. Both M32 evidence files and selection digest unchanged. JSON includes individual protected-file hashes.

Safety stashes retained untouched:

- `f93950aab6fdfb40bb100158915ef12692aa1665`
- `d979a433a5ab8ae600282048f184eb5fd06a8f17`

April 28 accepted AS-102/103/104/105 identities remain unchanged. New April 3 cache (two files) and handoff (three files) are separately reported above; no accepted artifact overwritten.

## 15. Quality gates

- Focused preprocessing cache/features/temporal/geometry: **408 passed**, no warnings, 31.27 s.
- Full `python -m pytest -v`: **993 passed, 6 existing Rasterio PendingDeprecationWarnings**, 74.74 s.
- `python -m ruff check .`: **PASS**.
- `git diff --check` plus both new-file whitespace checks: **PASS**.
- Credential scan of new evidence/handoff/cache and changed documentation: **PASS**; no live SAS, signed URL/query, Authorization value, password or secret persisted.
- Source/test/config/dependency changes **0 / 0 / 0 / NONE**; eight documentation/evidence paths only. Local engineering results, not GitHub CI claims.

## 16. Scientific limitations

April 3 frozen BOA-derived observational anomaly preparation only; no recurrence, HAB confirmation, biological continuity, species/toxins, accuracy, risk/confidence, safety/exposure or warning claim.

Only ~13% (794/6096) of April 3 target-valid water is policy-evaluable with the fixed five-history support. Five historical observations are not statistical sufficiency; shared March references do not provide independent confirmation. Small positive MAD scales can yield large robust-z magnitudes. Rank is not probability, confidence or severity. L2A BOA is observational input, not aquatic Rrs; masks/coastal support limitations remain. Frozen AS-105 policy has not undergone comparative sensitivity/accuracy/false-positive validation. Sparse support is reported honestly, not relaxed. No threshold/date changes, recurrence, biological continuity, exposure, safety, operational warning or lead-time claim.

## 17. M34 readiness

April 3 + April 28 have reconstructable typed AS-104/AS-105 artifacts under the identical frozen common comparison contract. **M34 INPUTS READY**. Owner review and separate authorization are required before real AS-106 recurrence acceptance; no guarantee of its future outcome. Decisions 050/051 unchanged, Decision 052 absent.

## 18. M34 explicitly NOT RUN

`compute_hab_persistence()` calls **0**. Real AS-106 acceptance **NOT RUN**; M34/M35 **NOT STARTED**; AS-107+ **NOT STARTED**; future AS-105 policy validation **NOT RUN**; P1 05.10 **NOT STARTED**. No PR or merge. M33 preparation execution began 2026-10-10T13:52:12.884792+04:00; recovery verification completed 2026-10-10T13:56:23.011397+04:00. Later documentation/Git publication is distinct from scientific execution; it does not rerun the experiment or constitute M35.
