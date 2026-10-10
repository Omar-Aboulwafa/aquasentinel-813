# AS-108 M43 — POST Metadata Inventory and Deterministic Selection

## Result and boundary

**M43 / E43 / EV-047: COMPLETE — metadata selection UNAVAILABLE.**
Reason: **ZERO_EXACT_PC_05_09_MATCHES**. No PC item or compatible product selected.
Earliest CDSE-eligible observation is frozen as a provisional identity, not a usable
processed scene: **2023-05-03T06:46:21.024000Z / sentinel-2a / 40RBN / orbit20**,
CDSE cloud **0.57%**. The sole existing resolver query returned zero items.
No later date queried on PC or substituted; no raster/signing/HEAD/range/COG request,
no XML asset retrieval, no pixel/support inspection and no AS-102–107 science.
`UNAVAILABLE` here is a **metadata-selection status**, not an AS-108 case category.

Official main/base `8bb56f12f2cd683d4a96f069c5d049bf4a39799e` is PR #26, with verified parents
`14149113e58788621d6aef91f039b95781c67434` and
`9e7254edc7680c5da31e796f82be2b8537833b9b`. Decision 053 FINAL / FROZEN DESIGN /
MERGED; AS-107 COMPLETE / CLOSED. Isolated clean branch before work:
`data/as-108-post-selection` in `/workspace/aquasentinel-813-as108-m43`.
M43/E43/EV-047 were unassigned; prior M43 references were forward plans only.
Metadata execution finished **2026-10-10T16:17:21.657015Z UTC**;
**2026-10-10T20:17:21.657015+04:00 Asia/Dubai**.
This time is not part of the semantic digest.

## Fixed analytical window, AOI and providers

POST is exactly **[2023-05-01T00:00:00Z,2023-06-01T00:00:00Z)**, an analytical
calendar phase, not a biological recovery boundary. The STAC interval uses those
bounds; returned dates are independently checked with the exclusive end.
AOI: `raha_validation_aoi`, unchanged `data/aoi/demo_site.geojson` Al Raha polygon,
geometry SHA-256 `a0fdb745672b246f569400574aa299ae4e233b8012ef54e970cdacba56687c2a`.
Analyst-defined context, not EAD incident geometry or a confirmed intake.

CDSE: `https://stac.dataspace.copernicus.eu/v1/`, collection `sentinel-2-l2a`.
PC: `https://planetarycomputer.microsoft.com/api/stac/v1/`, collection `sentinel-2-l2a`.
Existing `pystac-client` transport and repository `_SearchIO` page validation were
used from an ephemeral external orchestration script. No production helper added.
CDSE inventory applied **no server-side cloud restriction**, to retain high-cloud,
wrong-tile/orbit and missing/invalid metadata dispositions rather than censor the
inventory. This broad inventory does **not** change frozen eligibility **<=30%**.
Sentinel-2 L2A, S2A/B, AOI catalog match, fixed May dates, tile40RBN/orbit20 and strict
internally consistent identity are independently checked before selection.
Cloud is provider scene metadata, not AOI cloud fraction or usable-water evidence.

## Pagination and accounting

Requested page size 5, `max_items=None`. Complete CDSE page sizes:
**5 + 5 + 5 + 5 + 5 + 1 = 26**. First five pages each advertise exactly one next
link; terminal page advertises none. All 26 item IDs unique; page membership and
reported numberReturned captured in the JSON. No numberMatched was supplied, so
completeness is established by fully consumed validated pagination, not invented
provider totals. Every request returned HTTP200 JSON/GeoJSON.

**N_provider_records=26; N_distinct_acquisitions=26** using the frozen key
(timestamp, platform, tile, orbit), comprising **13 unique timestamps × 2 tiles**.
These are catalog observation keys, not 26 independent biological samples. No
reprocessing duplicate key occurred; all records remain individually retained.
**N_metadata_eligible_before_pc=4**; 22 fail CDSE-level criteria. PC compatibility
was checked only for the frozen earliest observation. **0 selected compatible
products**; full-contract N_metadata_eligible is **null/unknown**, because the
three unselected CDSE-eligible observations were deliberately not PC-queried.
Do not present four CDSE-eligible dates as four confirmed PC-compatible products,
or the three unassessed dates as incompatibility failures.

## Full CDSE provider/acquisition inventory

All rows are within May, query-matched to the AOI and strict-ID L2A/S2A-or-B.
Processing baseline, generation time, provider fields, record hashes and grouping
are fully retained in the [JSON inventory](AS_108_POST_METADATA_SELECTION.json).
PRE/POST temporal roles do not confer biological-negative labels.

| UTC acquisition | CDSE item ID | Platform | Tile | Orbit | Scene cloud % | Disposition | Reason |
|---|---|---|---|---|---|---|---|
| 2023-05-01T06:56:29.024000Z | S2B_MSIL2A_20230501T065629_N0510_R063_T39RZH_20240831T132114 | sentinel-2b | 39RZH | 63 | 18.32 | REJECTED_METADATA | MGRS_TILE_NOT_40RBN, RELATIVE_ORBIT_NOT_20 |
| 2023-05-01T06:56:29.024000Z | S2B_MSIL2A_20230501T065629_N0510_R063_T40RBN_20240831T132114 | sentinel-2b | 40RBN | 63 | 20.78 | REJECTED_METADATA | RELATIVE_ORBIT_NOT_20 |
| 2023-05-03T06:46:21.024000Z | S2A_MSIL2A_20230503T064621_N0510_R020_T39RZH_20240903T135841 | sentinel-2a | 39RZH | 20 | 0.73 | REJECTED_METADATA | MGRS_TILE_NOT_40RBN |
| 2023-05-03T06:46:21.024000Z | S2A_MSIL2A_20230503T064621_N0510_R020_T40RBN_20240903T135841 | sentinel-2a | 40RBN | 20 | 0.57 | UNAVAILABLE_PC_COMPATIBILITY | Zero PC matches for fixed query |
| 2023-05-06T06:56:21.024000Z | S2A_MSIL2A_20230506T065621_N0510_R063_T39RZH_20240901T194431 | sentinel-2a | 39RZH | 63 | 71.05 | REJECTED_METADATA | CDSE_CLOUD_METADATA_GT_30_PERCENT, MGRS_TILE_NOT_40RBN, RELATIVE_ORBIT_NOT_20 |
| 2023-05-06T06:56:21.024000Z | S2A_MSIL2A_20230506T065621_N0510_R063_T40RBN_20240901T194431 | sentinel-2a | 40RBN | 63 | 73.13 | REJECTED_METADATA | CDSE_CLOUD_METADATA_GT_30_PERCENT, RELATIVE_ORBIT_NOT_20 |
| 2023-05-08T06:46:29.024000Z | S2B_MSIL2A_20230508T064629_N0510_R020_T39RZH_20240908T033402 | sentinel-2b | 39RZH | 20 | 16.21 | REJECTED_METADATA | MGRS_TILE_NOT_40RBN |
| 2023-05-08T06:46:29.024000Z | S2B_MSIL2A_20230508T064629_N0510_R020_T40RBN_20240908T033402 | sentinel-2b | 40RBN | 20 | 15.6 | NOT_SELECTED_METADATA_RULE | Later eligible acquisition; not selected |
| 2023-05-11T06:56:29.024000Z | S2B_MSIL2A_20230511T065629_N0510_R063_T39RZH_20240905T131833 | sentinel-2b | 39RZH | 63 | 18.68 | REJECTED_METADATA | MGRS_TILE_NOT_40RBN, RELATIVE_ORBIT_NOT_20 |
| 2023-05-11T06:56:29.024000Z | S2B_MSIL2A_20230511T065629_N0510_R063_T40RBN_20240905T131833 | sentinel-2b | 40RBN | 63 | 19.74 | REJECTED_METADATA | RELATIVE_ORBIT_NOT_20 |
| 2023-05-13T06:46:21.024000Z | S2A_MSIL2A_20230513T064621_N0510_R020_T39RZH_20240907T025331 | sentinel-2a | 39RZH | 20 | 0.23 | REJECTED_METADATA | MGRS_TILE_NOT_40RBN |
| 2023-05-13T06:46:21.024000Z | S2A_MSIL2A_20230513T064621_N0510_R020_T40RBN_20240907T025331 | sentinel-2a | 40RBN | 20 | 0.19 | NOT_SELECTED_METADATA_RULE | Later eligible acquisition; not selected |
| 2023-05-16T06:56:21.024000Z | S2A_MSIL2A_20230516T065621_N0510_R063_T39RZH_20240905T075051 | sentinel-2a | 39RZH | 63 | 70.65 | REJECTED_METADATA | CDSE_CLOUD_METADATA_GT_30_PERCENT, MGRS_TILE_NOT_40RBN, RELATIVE_ORBIT_NOT_20 |
| 2023-05-16T06:56:21.024000Z | S2A_MSIL2A_20230516T065621_N0510_R063_T40RBN_20240905T075051 | sentinel-2a | 40RBN | 63 | 71.39 | REJECTED_METADATA | CDSE_CLOUD_METADATA_GT_30_PERCENT, RELATIVE_ORBIT_NOT_20 |
| 2023-05-18T06:46:29.024000Z | S2B_MSIL2A_20230518T064629_N0510_R020_T39RZH_20240905T010301 | sentinel-2b | 39RZH | 20 | 89.62 | REJECTED_METADATA | CDSE_CLOUD_METADATA_GT_30_PERCENT, MGRS_TILE_NOT_40RBN |
| 2023-05-18T06:46:29.024000Z | S2B_MSIL2A_20230518T064629_N0510_R020_T40RBN_20240905T010301 | sentinel-2b | 40RBN | 20 | 89.77 | REJECTED_METADATA | CDSE_CLOUD_METADATA_GT_30_PERCENT |
| 2023-05-21T06:56:29.024000Z | S2B_MSIL2A_20230521T065629_N0510_R063_T39RZH_20240904T210158 | sentinel-2b | 39RZH | 63 | 90.96 | REJECTED_METADATA | CDSE_CLOUD_METADATA_GT_30_PERCENT, MGRS_TILE_NOT_40RBN, RELATIVE_ORBIT_NOT_20 |
| 2023-05-21T06:56:29.024000Z | S2B_MSIL2A_20230521T065629_N0510_R063_T40RBN_20240904T210158 | sentinel-2b | 40RBN | 63 | 92.12 | REJECTED_METADATA | CDSE_CLOUD_METADATA_GT_30_PERCENT, RELATIVE_ORBIT_NOT_20 |
| 2023-05-23T06:46:31.024000Z | S2A_MSIL2A_20230523T064631_N0510_R020_T39RZH_20240907T084524 | sentinel-2a | 39RZH | 20 | 39.95 | REJECTED_METADATA | CDSE_CLOUD_METADATA_GT_30_PERCENT, MGRS_TILE_NOT_40RBN |
| 2023-05-23T06:46:31.024000Z | S2A_MSIL2A_20230523T064631_N0510_R020_T40RBN_20240907T084524 | sentinel-2a | 40RBN | 20 | 38.79 | REJECTED_METADATA | CDSE_CLOUD_METADATA_GT_30_PERCENT |
| 2023-05-26T06:56:21.024000Z | S2A_MSIL2A_20230526T065621_N0510_R063_T39RZH_20240907T073145 | sentinel-2a | 39RZH | 63 | 12.89 | REJECTED_METADATA | MGRS_TILE_NOT_40RBN, RELATIVE_ORBIT_NOT_20 |
| 2023-05-26T06:56:21.024000Z | S2A_MSIL2A_20230526T065621_N0510_R063_T40RBN_20240907T073145 | sentinel-2a | 40RBN | 63 | 13.41 | REJECTED_METADATA | RELATIVE_ORBIT_NOT_20 |
| 2023-05-28T06:46:29.024000Z | S2B_MSIL2A_20230528T064629_N0510_R020_T39RZH_20240908T011647 | sentinel-2b | 39RZH | 20 | 19.3 | REJECTED_METADATA | MGRS_TILE_NOT_40RBN |
| 2023-05-28T06:46:29.024000Z | S2B_MSIL2A_20230528T064629_N0510_R020_T40RBN_20240908T011647 | sentinel-2b | 40RBN | 20 | 19.46 | NOT_SELECTED_METADATA_RULE | Later eligible acquisition; not selected |
| 2023-05-31T06:56:29.024000Z | S2B_MSIL2A_20230531T065629_N0510_R063_T39RZH_20240908T012259 | sentinel-2b | 39RZH | 63 | 31.9 | REJECTED_METADATA | CDSE_CLOUD_METADATA_GT_30_PERCENT, MGRS_TILE_NOT_40RBN, RELATIVE_ORBIT_NOT_20 |
| 2023-05-31T06:56:29.024000Z | S2B_MSIL2A_20230531T065629_N0510_R063_T40RBN_20240908T012259 | sentinel-2b | 40RBN | 63 | 33.7 | REJECTED_METADATA | CDSE_CLOUD_METADATA_GT_30_PERCENT, RELATIVE_ORBIT_NOT_20 |

## Frozen sequence and exact PC query

Canonical order: UTC acquisition ascending, then CDSE item ID. CDSE metadata-
eligible sequence: **May 3, May 8, May 13, May 28**, all 40RBN/orbit20.
The earliest provisional CDSE identity is:
`S2A_MSIL2A_20230503T064621_N0510_R020_T40RBN_20240903T135841`,
CDSE processing baseline **05.10**, generation **2024-09-03T13:58:41Z**.

Decision 053 makes PC compatibility mandatory before a final selected product.
M43 first fixes the earliest CDSE-eligible identity, then evaluates that identity's
exact PC compatibility. It does **not** reinterpret compatibility as permission
to skip an inconvenient earliest candidate and query a later scene. Zero matches
therefore yields UNAVAILABLE under the frozen no-fallback rule, consistent with
the owner-authorized M43 execution sequence. No new eligibility or fallback policy.

Use the existing resolver's **+/-1 second** acquisition query:
`2023-05-03T06:46:20.024000Z/2023-05-03T06:46:22.024000Z`, same AOI,
Sentinel-2 L2A, broad matching cloud<=100 as already implemented. This PC matching
query never replaces CDSE<=30 eligibility. One terminal empty PC page, with
numberReturned **0**, no next link: **pre-filter=0; strict identity=0; strict
identity+05.09=0**. Exact acquisition/platform/tile/orbit and baseline05.09 remain
mandatory; no raw-ID string equality, aliases, date widening or relaxed matching.
Selected PC item ID, baseline and generation: **null**. No signing or asset-key
validation needed for an empty result. This does not prove no corresponding
observation exists anywhere in PC; it records the exact frozen query's outcome.

## Accepted grid/upstream reference — not recomputed

Copied only from accepted
`docs/evidence/AS_106_APRIL3_UPSTREAM_PREPARATION.json#/as102/grid`:
EPSG:32640, **20 m**, width×height **310×228**, bounds
**[249020,2702860,255220,2707420]**, grid ID
`88d76cf6265d9e0fa2802ed26324c02275e74721d4eb5b597cc9884a6d27aeec`.
May native headers, decoding and pixel support **NOT VERIFIED**.
Required B02/B03/B04/B05/B06/B07/B08/B8A/B11 + SCL/product XML, unchanged AOI,
XML-driven decoding, invalid SCL classes {0,1,2,3,7,8,9,10,11}/unknowns, water6,
bilinear reflectance/nearest categorical alignment and conservative all-contributor
support remain references to accepted AS-102 policy. AS-103–107 identities/numerics,
March reference history, Decisions050/051/052 and scoring policy are unchanged;
no scientific stage executed or cache created.

## Deterministic metadata-only digest

Schema **as108-m43-post-selection-v1**. SHA-256:
**`df487999defada56023a7e76be69c507b2b1ff11d81de1480737eca86a1ad4de`**.
Reproduce `sha256(canonical_json(JSON["selection_payload"]))` using existing
`canonical_json`: sorted keys, compact comma/colon separators, `allow_nan=False`,
default `ensure_ascii=True`, UTF-8 and **one trailing newline**. Records/acquisitions
ordered by timestamp+ID; eligible identities likewise; pagination in page order.
Selected identities, zero PC cardinality, unavailable reason, complete inventory,
exact query scopes/filters, fixed window/AOI/provider/grid/contract references and
Decision053 body hash are all committed. Stable provider metadata hashes use the
explicit JSON `provider_record_hash_fields`; final dispositions are separately
covered by the overall selection digest. No pixels, scores, signed hrefs, tokens
or volatile execution/request times enter the selection payload.

## Network and scientific boundary

Actual metadata requests: **CDSE8** (root+collection+6 pages), **PC3**
(root+collection+1 empty search page). **EO asset requests0, EO raster bytes0,
scientific compute calls0, signing0, COG HEAD/range/open0**.
Guard allowed only HTTPS catalog metadata routes on these two provider hosts;
blocked attempts0, no unexpected contact. Item assets, if returned, stayed in
memory and were not dereferenced; durable evidence uses stable metadata only.
Initial Git fetch1 at metadata freeze; authorized later push/remote verification
are administrative Git operations, reported separately from EO metadata.
Engineering tests use local/synthetic fixtures with external network blocked.

## Preservation and engineering gates

Before provider requests/edits: **137 tracked hashes**, four frozen-decision body
hashes, accepted AS-107 and M42 evidence hashes, **44 protected external hashes**,
**57 modes** and exact safety-stash inventory snapshotted. No source/tests/config/
dependency/cache changes; no accepted scientific evidence or M42 MD/JSON rewrites.
Decisions050/051/052/**053** bodies remain byte-identical. Both safety stashes
retained untouched. Historical M41/M42 records remain intact, relabelled historical
only where dated current headers need separation from M43.
Engineering gates: **1285 full tests PASS (106.24s), six existing Rasterio PendingDeprecationWarnings; Ruff PASS; diff/new-file whitespace PASS**. Preservation/security: **PASS — eight authorized docs/evidence paths only; Decisions050–053, source/tests/config/dependencies, accepted AS-107/M42 evidence, 44 external hashes, 57 modes and both safety stashes unchanged; digest/credential scan PASS; no scientific cache created**.
No GitHub CI success claimed.

## Interpretation and forward boundary

“The frozen metadata rule did not yield a uniquely compatible POST observation;
the missing POST evidence was retained rather than substituted.” This is not
recovery, a May biological-negative label, successful scientific validation or
an observational-consistency classification. April outputs were already known;
Decision053 retrospective reporting semantics remain unchanged. Future May output
cannot revise categories. Accepted April28 Watch result is immutable and not rerun.

Stop after M43 evidence commit/push; PR/merge require separate authorization.
Next: **owner review of this UNAVAILABLE evidence**, then separately authorize
**M44 case-study reporting from accepted PRE/EVENT evidence with POST explicitly
UNAVAILABLE**. An unavailable POST is permitted by the minimum P0 contract; further
metadata-only compatibility investigation is optional and needs separate authorization. No automatic query widening,
fallback, pixel retrieval or M44 science. **M44 NOT STARTED; AS-108 scientific
validation execution NOT STARTED; AS-201 NOT STARTED; Decision054 ABSENT.**
