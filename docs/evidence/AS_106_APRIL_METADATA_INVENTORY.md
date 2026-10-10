# AS-106 — M32 Metadata-Only April Acquisition Inventory

## 1. Scope: M32 / E32 / EV-036

**METADATA-ONLY PASS / COMPLETE.** This freezes the future real sequence before
anomaly-dependent selection. No imagery or scientific computation was performed.
M31 offline persistence is COMPLETE AND MERGED via PR #17; M32 is not M33–M35.

## 2. Official main and isolated branch

Verified `origin/main` and initial worktree HEAD:
`723e13a900dba30b73a8a2da39df1d984233a2f4`. Branch: `data/as-106-april-metadata-inventory`;
isolated worktree `/workspace/aquasentinel-813-as106-m32`, initially clean.
Git network authorized for the initial `git fetch origin main` and final branch
push only. No PR or merge is part of M32.

## 3. Query time

Metadata transport started **2026-10-10T08:23:54.186384+00:00** and completed
**2026-10-10T08:24:00.344588+00:00** (UTC). These are inventory execution times, not acquisition,
scientific acceptance or Git publication timestamps. Manifest `created_at` is
operational and excluded from the selection digest.

## 4. Exact services, hosts and request audit

- CDSE endpoint: `https://stac.dataspace.copernicus.eu/v1/`.
- PC endpoint: `https://planetarycomputer.microsoft.com/api/stac/v1/`.
- Both collections: `sentinel-2-l2a`.
- Allowed hosts printed before requests: `stac.dataspace.copernicus.eu` and
  `planetarycomputer.microsoft.com`; these were the **only service hosts contacted**.

| Operation | Host | Method / metadata path | HTTP requests | Search pages / features | Pagination |
|---|---|---|---|---|---|
| CDSE discovery | stac.dataspace.copernicus.eu | GET `/v1/`; GET collection; POST search | 4 | 2 pages: 10 + 2 = 12 | next then terminal; complete |
| PC April 3 match | planetarycomputer.microsoft.com | GET root; GET collection; POST search | 3 | 1 page / 4 items | terminal; complete |
| PC April 28 match | planetarycomputer.microsoft.com | GET root; GET collection; POST search | 3 | 1 page / 2 items | terminal; complete |

**10 metadata HTTP requests; 3 logical searches; 4 complete search pages.**
Every response was successful JSON/GeoJSON. No retries, credential/session
authentication, redirects, unexpected-host contact or blocked operation occurred.
An external audit script used the repository `search_catalog` transport, with
an exact HTTPS host/path guard before every request, including any redirect;
streaming response headers were checked before reading JSON bodies. Rasterio
open, signing/asset-byte entrypoints and asset-resolving entrypoints were disabled.
No asset domain was contacted. Detailed method/host/path/page counts are in the
normalized JSON; no raw provider responses or hrefs were persisted.

## 5. Exact frozen interval and AOI

Inclusive **[2023-04-01T00:00:00Z, 2023-04-28T06:46:29.024000Z]**.
AOI: `raha_validation_aoi`, **Al Raha Bay Validation AOI**, role
`validation_aoi`, from unchanged `data/aoi/demo_site.geojson`.
WGS84 Polygon ring: `[54.525,24.42]`, `[54.585,24.42]`, `[54.585,24.46]`,
`[54.525,24.46]`, `[54.525,24.42]`.
Repository `geometry_digest` SHA-256: `a0fdb745672b246f569400574aa299ae4e233b8012ef54e970cdacba56687c2a`.
This is the analyst-defined validation AOI, not an operational intake location.

## 6. Frozen inclusion criteria and reused contracts

Sentinel-2 L2A; configured AOI; exact inclusive interval; CDSE metadata cloud
**<=30%**; **40RBN / relative orbit 20**; **Sentinel-2A or Sentinel-2B**;
strict cross-provider acquisition/platform/tile/orbit identity; exactly one PC
**05.09** product; all required asset keys present. No alternative baseline.

Required keys, derived directly from `sentinel2_assets.REQUIRED_ASSETS`:
`B02`, `B03`, `B04`, `B05`, `B06`, `B07`, `B08`, `B8A`, `B11`, `SCL`, `product-metadata`. Each presence is an explicit boolean in JSON. PC asset hrefs, media
types, bodies and raster/decoding metadata were not inspected or recorded.

Used frozen `search_catalog`, `normalize_item`, `discovery_identity` and
`_pc_identity`. No production helper or rule was changed. CDSE ID/metadata and
PC ID/property identity checks retain their original strictness. Matching uses
full timezone-aware UTC acquisition precision, not ID string equality or fuzzy
time/alias fallback. No duplicate records or ambiguous exact 05.09 matches occurred.

The existing resolver's PC query is each exact CDSE acquisition **+/-1 second**,
AOI intersects, collection `sentinel-2-l2a`, cloud query **<=100%**. That broad
PC query is existing discovery/matching behavior, not a replacement for CDSE's
**<=30% eligibility gate**. All returned PC identities were validated before
exact-match/baseline selection. No PC cloud threshold was newly invented.

Frozen EPSG:32640 20 m grid, March reference IDs/period, minimum_observations=5,
BOA/XML decoding, masking and AS-102/103/104/105 contracts remain requirements
for separately authorized M33. Metadata-only key presence does **not** establish
raster readability, XML safety, decoded-pixel compatibility or usable-water
support. Any future preparation failure is a blocker, not an outcome-driven
exclusion or permission to weaken these contracts.

## 7. CDSE discovery count and pagination

**12 returned CDSE product records**, at **6 distinct acquisition timestamps**.
Pages contained **10 then 2** features; the second page had no next link.
`max_items=None` and the existing malformed/repeated-pagination safeguards
were retained. This is complete for the frozen AOI/interval/cloud query;
products not returned because of the declared cloud gate are not fabricated
as discovered exclusions. Record count is not acquisition count.

## 8. Deterministic metadata post-filter

Canonical order: UTC acquisition then CDSE item ID. **2 records pass** tile/orbit,
platform, exact interval and cloud rechecks; **10 records excluded**. Every raw
returned record remains in `candidate_records` with eligibility and exact reasons.
No source anomaly, support fraction, candidate count or scientific outcome was
consulted to make any disposition.

## 9. Planetary Computer matching results

**2 logical PC searches / 6 returned items / 3 exact observation matches across
all baselines / 2 exact observation matches at 05.09.** April 3 returned the
40RBN products at 05.09 and 05.10 plus two adjacent 39RZH products. April 28
returned one 40RBN 05.09 product plus an adjacent 39RZH 05.09 product.
Adjacent tile products do not match; April 3 05.10 is context only.

| CDSE acquisition | PC product | Tile / orbit | Baseline | Generation UTC | Exact observation match | All required keys | Disposition |
|---|---|---|---|---|---|---|---|
| 2023-04-03T06:46:21.024000+00:00 | `S2A_MSIL2A_20230403T064621_R020_T39RZH_20230403T120124` | 39RZH / 20 | 05.09 | 2023-04-03T12:01:24.779706Z | false | yes | wrong tile; not an observation match |
| 2023-04-03T06:46:21.024000+00:00 | `S2A_MSIL2A_20230403T064621_R020_T39RZH_20240824T175307` | 39RZH / 20 | 05.10 | 2024-08-24T17:53:07.000000Z | false | yes | wrong tile; not an observation match |
| 2023-04-03T06:46:21.024000+00:00 | `S2A_MSIL2A_20230403T064621_R020_T40RBN_20230403T115452` | 40RBN / 20 | 05.09 | 2023-04-03T11:54:52.560526Z | true | yes | eligible selected product |
| 2023-04-03T06:46:21.024000+00:00 | `S2A_MSIL2A_20230403T064621_R020_T40RBN_20240824T175307` | 40RBN / 20 | 05.10 | 2024-08-24T17:53:07.000000Z | true | yes | other baseline; not eligible |
| 2023-04-28T06:46:29.024000+00:00 | `S2B_MSIL2A_20230428T064629_R020_T39RZH_20230428T123202` | 39RZH / 20 | 05.09 | 2023-04-28T12:32:02.636260Z | false | yes | wrong tile; not an observation match |
| 2023-04-28T06:46:29.024000+00:00 | `S2B_MSIL2A_20230428T064629_R020_T40RBN_20230428T122311` | 40RBN / 20 | 05.09 | 2023-04-28T12:23:11.362052Z | true | yes | eligible selected product |

No zero-match, multiple-05.09-match or missing-required-key exclusion occurred.
No baseline substitution or imagery comparison was attempted.

## 10. Final eligible acquisition count

**2 unique acquisitions**, chronologically April 3 then April 28.
The original Decision 051 eligibility rule is unchanged. Every eligible date is
included; sparse support and zero-candidate outcomes cannot remove a date.

## 11. Chronological eligible inventory

| # | Acquisition UTC | Platform | Tile / orbit | CDSE cloud % | CDSE product | Exact PC 05.09 product | All 11 keys | AS-102 | AS-103 | AS-104 | AS-105 | Future M33 status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 2023-04-03T06:46:21.024000+00:00 | sentinel-2a | 40RBN / 20 | 0.68 | `S2A_MSIL2A_20230403T064621_N0510_R020_T40RBN_20240824T175307` | `S2A_MSIL2A_20230403T064621_R020_T40RBN_20230403T115452` | yes | missing | missing | missing | missing | `needs_as102_as103_as104_as105` |
| 2 | 2023-04-28T06:46:29.024000+00:00 | sentinel-2b | 40RBN / 20 | 0.12 | `S2B_MSIL2A_20230428T064629_N0510_R020_T40RBN_20240831T052931` | `S2B_MSIL2A_20230428T064629_R020_T40RBN_20230428T122311` | yes | present | present | present | present | `already_complete_for_sequence` |

## 12. Every excluded returned record

| Acquisition UTC | CDSE product | Platform | Cloud % | Tile / orbit | Exact deterministic exclusion reasons |
|---|---|---|---|---|---|
| 2023-04-01T06:56:29.024000+00:00 | `S2B_MSIL2A_20230401T065629_N0510_R063_T39RZH_20240828T022548` | sentinel-2b | 6.05 | 39RZH / 63 | wrong MGRS tile; requires 40RBN; wrong relative orbit; requires 20 |
| 2023-04-01T06:56:29.024000+00:00 | `S2B_MSIL2A_20230401T065629_N0510_R063_T40RBN_20240828T022548` | sentinel-2b | 4.73 | 40RBN / 63 | wrong relative orbit; requires 20 |
| 2023-04-03T06:46:21.024000+00:00 | `S2A_MSIL2A_20230403T064621_N0510_R020_T39RZH_20240824T175307` | sentinel-2a | 0.74 | 39RZH / 20 | wrong MGRS tile; requires 40RBN |
| 2023-04-06T06:56:21.024000+00:00 | `S2A_MSIL2A_20230406T065621_N0510_R063_T39RZH_20240827T062705` | sentinel-2a | 0.3 | 39RZH / 63 | wrong MGRS tile; requires 40RBN; wrong relative orbit; requires 20 |
| 2023-04-06T06:56:21.024000+00:00 | `S2A_MSIL2A_20230406T065621_N0510_R063_T40RBN_20240827T062705` | sentinel-2a | 0.31 | 40RBN / 63 | wrong relative orbit; requires 20 |
| 2023-04-16T06:56:21.024000+00:00 | `S2A_MSIL2A_20230416T065621_N0510_R063_T39RZH_20240901T165132` | sentinel-2a | 16.16 | 39RZH / 63 | wrong MGRS tile; requires 40RBN; wrong relative orbit; requires 20 |
| 2023-04-16T06:56:21.024000+00:00 | `S2A_MSIL2A_20230416T065621_N0510_R063_T40RBN_20240901T165132` | sentinel-2a | 15.23 | 40RBN / 63 | wrong relative orbit; requires 20 |
| 2023-04-21T06:56:29.024000+00:00 | `S2B_MSIL2A_20230421T065629_N0510_R063_T39RZH_20240902T093328` | sentinel-2b | 9.32 | 39RZH / 63 | wrong MGRS tile; requires 40RBN; wrong relative orbit; requires 20 |
| 2023-04-21T06:56:29.024000+00:00 | `S2B_MSIL2A_20230421T065629_N0510_R063_T40RBN_20240902T093328` | sentinel-2b | 10.56 | 40RBN / 63 | wrong relative orbit; requires 20 |
| 2023-04-28T06:46:29.024000+00:00 | `S2B_MSIL2A_20230428T064629_N0510_R020_T39RZH_20240831T052931` | sentinel-2b | 0.14 | 39RZH / 20 | wrong MGRS tile; requires 40RBN |

Both exclusion reasons are retained where both apply. A wrong-tile record on
April 3 or 28 does not exclude its separate eligible 40RBN record. The fully
excluded acquisition timestamps are April 1, 6, 16 and 21; exclusion is strictly
metadata-driven, not a statement about water conditions.

## 13. Accepted April 28 target reconciliation

**PASS**, exact acquisition `2023-04-28T06:46:29.024000Z`, Sentinel-2B,
40RBN, relative orbit 20; exactly one PC **05.09** product:
`S2B_MSIL2A_20230428T064629_R020_T40RBN_20230428T122311`.
CDSE discovery: `S2B_MSIL2A_20230428T064629_N0510_R020_T40RBN_20240831T052931`.
Actual PC generation: `2023-04-28T12:23:11.362052Z`; CDSE reprocessing generation
`2024-08-31T05:29:31Z`, baseline **05.10**. Observation identity matches, while
processing products differ. **Pixel equivalence is not claimed.** Accepted
target artifacts and historical evidence were not overwritten.

## 14. Existing stage availability — audited after selection

| Acquisition UTC | AS-102 | AS-103 | AS-104 | AS-105 | Required future stages |
|---|---|---|---|---|---|
| 2023-04-03T06:46:21.024000+00:00 | missing | missing | missing | missing | as102, as103, as104, as105 |
| 2023-04-28T06:46:29.024000+00:00 | present | present | present | present | none; reuse accepted evidence after required integrity verification |

Read-only scope: six cache manifests under
`/workspace/aquasentinel-813/data/cache/as102/`; six accepted AS-103 PASS identity
descriptors in the existing AS-104 handoff manifest; the one AS-104 handoff;
the one M29 accepted geometry bundle; repository evidence at the verified base.
No April 3 stage identity/evidence is present in this audited scope. Missing
means no verified accepted/available artifact here, not provider-wide nonexistence.
No NPZ arrays were loaded or scientific values computed for this availability
audit. Hashing protected files is preservation verification, not scene processing.

April 28 identities, with evidence paths/hashes in JSON:

- AS-102: `optical:0725a908d21cd655e83f70d2bb11247dc0f1516f0c00ea275efc3239113ee4a6`;
  actual PC source/baseline and observation identity verified in accepted cache.
- AS-103: `spectral:dae91b4dda0131ca2d2987321abd2ffd5c4b5ffb2e95a44880b7a5f9a67ea64b`;
  accepted PASS descriptor and correct AS-102 parent, not a new persisted spectral cache.
- AS-104: `temporal:e814b0574ab30d1841778ee3c5005ffcb313ab42473c41acc028f0a9f7804a8b`;
  accepted handoff target points to that AS-103 product.
- AS-105: `hab_geometry:70876fbcb25e8a37abaa238a59e1da32fec9066792e6239db68e284b7bd18682`;
  M29 accepted identity has that exact AS-104 parent and target acquisition.

The March 4/9/14/24/29 cache/AS-103 identities are existing historical references,
outside the frozen April sequence. Nothing was regenerated; witness/integrity
validation at future scientific consumption remains required.

## 15. Exact future M33 requirements

**Only `2023-04-03T06:46:21.024000Z` needs AS-102→AS-103→AS-104→AS-105**.
Status: `needs_as102_as103_as104_as105`. April 28 status:
`already_complete_for_sequence`, using existing accepted artifacts/evidence;
no new April 28 extraction is authorized. The fixed five March references and
target-specific AS-104 comparison remain frozen. This stage-derived classification
does not authorize downloads, reconstruction, extraction or M33 execution.

## 16. Canonical selection digest and reproducibility

**selection_inventory_sha256:** `570792066c1997b9a403249d994c4e7367bf2f1dafc6473b6e30df20cd6481d5`.

Normalized artifact: [AS_106_APRIL_METADATA_INVENTORY.json](AS_106_APRIL_METADATA_INVENTORY.json).
Reconstruct the hash payload exactly as follows: `frozen_interval`, `aoi_identity`,
`selection_policy`; `candidate_dispositions` = each ordered `candidate_records`
entry with only `pc_query` removed; `ordered_eligible_acquisitions` = those
dispositions with `eligible=true`, unchanged and in order. Serialize using
UTF-8 `json.dumps(sort_keys=True, separators=(",", ":"), allow_nan=False)`
plus one newline, then SHA-256. This reuses repository canonical JSON conventions.
Includes all dispositions, ordered exact PC 05.09 identities and required-key
presence; excludes operational creation/query times/counts, stage availability,
local paths/hashes and publication/quality-gate metadata. Identical normalized
provider metadata produces the same digest; no second network run was performed.

CDSE normalized query: collection `sentinel-2-l2a`, AOI intersects above, interval
`2023-04-01T00:00:00+00:00/2023-04-28T06:46:29.024000+00:00`,
`eo:cloud_cover <=30`, no item cap. Exact PC query intervals and matching
dispositions are in JSON. Pagination completion was verified for every search.

## 17. Zero downloads, security, quality and preservation

**Asset/binary request count: 0. Imagery/data bytes downloaded: 0.** Only JSON
metadata was retrieved. No signing/token request, bearer credentials, remote
raster open, thumbnail/quicklook/ZIP/SAFE/JP2/TIFF body or new-date processing.
JSON has only normalized identities, selection/disposition/key-presence and
availability metadata; no asset hrefs, SAS queries or raw STAC bodies.

Existing tests: **993 passed / six retained Rasterio PendingDeprecationWarnings**.
Ruff PASS; diff/new-file whitespace PASS; credential/URL scan PASS. No source,
test, config or dependency change. These are local checks, not GitHub CI claims.
Before/after SHA-256 and mode checks preserve all protected tracked files,
12 accepted AS-102 cache files, three AS-104 handoff files, four M29 bundle
files and 13 external recovery artifacts. Both safety stashes remain untouched:
`f93950aab6fdfb40bb100158915ef12692aa1665` and
`d979a433a5ab8ae600282048f184eb5fd06a8f17`. No protected file or mode changed.

## 18. Scientific boundary and presentation value

Predeclared metadata-first selection is anti-cherry-picking evidence, not
scientific recurrence acceptance. Metadata cloud cover is scene-level; asset
presence cannot establish water usability. Only two dates meet this frozen query;
unobserved/unsupported intervals cannot become candidate absence or continuous
biological duration. No BOA, masks, features, baselines, ranks, deviation, families,
candidate pixels, recurrence, areas or regions were computed.
No HAB/bloom/biology/concentration/species/toxins, continuous persistence,
accuracy/false-positive rate, risk/confidence, exposure/safety, alert or lead-time
claim. Shared March references are not independent confirmation. Decision 051
and Decision 050 scientific limitations remain intact.

Presentation takeaway: **“Choose dates before seeing anomaly outcomes.”**
Recommended visual: metadata-only two-date timeline, tile/orbit exclusion funnel,
and stage-availability card with a ZERO IMAGERY callout. No screenshot was created.

## 19. Authorization boundary and next gate

M32 / E32 / EV-036: **COMPLETE / METADATA-ONLY PASS**.
M31 COMPLETE AND MERGED via PR #17; Decision 051 unchanged; Decision 052 absent.
**M33 upstream preparation NOT STARTED; M34 real AS-106 acceptance NOT STARTED;
M35 publication/closeout NOT STARTED; real AS-106 acceptance NOT RUN.**
Owner review and separate April 3 preparation authorization are next.
AS-107+ / P1 05.10 NOT STARTED; future AS-105 policy validation NOT RUN.
This inventory branch publication is not M35; no PR or merge is authorized here.
