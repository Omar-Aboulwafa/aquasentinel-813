# AS-201 — Sentinel-1 Retrieval / Source Contract

## M47 scope, plan and status

Decision 054 / M47 / E47 / EV-051: **FINAL / FROZEN DESIGN / NOT IMPLEMENTED**.
Prepared 11 October 2026 (Asia/Dubai) on `docs/as-201-design-freeze`, from PR #28
main `9a8a15c489a6aa3e678b642d2ccf5160affc56bd`. AS-107 COMPLETE / CLOSED. AS-108 P0 retrospective case
study COMPLETE / MERGED with POST UNAVAILABLE; PARTIALLY_CONSISTENT is unchanged.
AS-201 implementation and AS-202 **NOT STARTED**. No Decision 055, PR or merge.

**Task/goal:** Freeze the reproducible P0 raw Sentinel-1 source contract before
looking for dark pixels. Inputs are the approved M45/M46 documentary/metadata/
header/XML audit facts. Outputs are this contract, Decision 054 and durable MD/JSON
design evidence, plus continuity/presentation records. Exactly eight documentation
paths change; no source, tests, configuration or dependency changes. No new package.
Acceptance requires exact six-source mapping, explicit coverage/missingness,
typed provenance/security semantics, unfrozen numerical preprocessing, strict
JSON/digest/security/preservation gates and existing pytest/Ruff/diff checks.
Non-goals: pixels, SAR processing, detection, risk, downstream policy freezes.

## External event, separate from satellite inference

Data Desk, **May 2026 Kharg oil slick**, published **2026-05-19**:
https://research.datadesk.eco/kharg-slick/ . Verification provenance:
`EXTERNALLY_VERIFIED_PUBLIC_SOURCE_FACTS_SUPPLIED_IN_AUTHORIZATION`.
Codex records the supplied facts; it did not independently retrieve this source
in M47. Outside access time is not supplied; null, never invented.

External interpretation: Kharg Island/Persian Gulf; first documented radar witness
May 6 about 14:42 UTC, S1A; progression south/southwest; May 11 displaced visible
sheen around 28.75 N/~55 km south; May 13 SAR context about 28.75–28.95 N;
May 18 remaining dark patches roughly 45 km southwest. These are documentary
interpretations, not AquaSentinel results or petroleum pixel ground truth.
No Data Desk polygon is imported as truth. The objective is a historical
surface-slick **candidate** demonstration, not petroleum/source confirmation.

## Frozen envelope and observed source support

`KHARG_P0_VALIDATION_ENVELOPE`, EPSG:4326, **[49.60, 28.60, 50.70, 29.60]**,
selected before AquaSentinel SAR pixels. Broad geography retains southern context.
The proposed [49.60,28.92,50.70,29.60] is **rejected** because it can exclude 28.75 N.
The envelope is not a spill polygon, intake, shutdown zone or Data Desk polygon.

For each date, source support is envelope intersect union of **both frozen slice
footprints**. Common support is intersection of the three date supports. Date
products retain date support; direct temporal/reference comparison uses common
three-date support unless a later frozen algorithm explicitly defines pair support.
No gap filling, extrapolation or anomaly-derived envelope edit. Missing is nodata/
unavailable, never Normal or zero anomaly. Metadata geometry is distinct from
pixel evaluability. M46 approximate coverage: envelope 11,868.26 km², common support
11,865.19 km², uncovered 3.07 km²; these are **not petroleum-area measurements**.
Geometry arithmetic was not repeated in M47; future retrieval validates footprints.

## Exact sequence and source mapping

All sources: **S1A, IW, GRDH, ascending, relative orbit 101, VV+VH**.
REFERENCE Apr 24: pre-event observational reference, not oil-free/negative.
DOCUMENTARY_EVENT May 6: first documentary radar witness, not a proven peak.
LATE_FOLLOW_UP May 18: late observational witness, not recovery.

| Role / slice | Exact CDSE identity | Exact PC identity |
|---|---|---|
| REFERENCE / 1 | `S1A_IW_GRDH_1SDV_20260424T144205_20260424T144230_064223_08158E_4192_COG` | `S1A_IW_GRDH_1SDV_20260424T144205_20260424T144230_064223_08158E` |
| REFERENCE / 2 | `S1A_IW_GRDH_1SDV_20260424T144230_20260424T144255_064223_08158E_BA3A_COG` | `S1A_IW_GRDH_1SDV_20260424T144230_20260424T144255_064223_08158E` |
| DOCUMENTARY_EVENT / 1 | `S1A_IW_GRDH_1SDV_20260506T144204_20260506T144229_064398_081C09_BF44_COG` | `S1A_IW_GRDH_1SDV_20260506T144204_20260506T144229_064398_081C09` |
| DOCUMENTARY_EVENT / 2 | `S1A_IW_GRDH_1SDV_20260506T144229_20260506T144254_064398_081C09_A43B_COG` | `S1A_IW_GRDH_1SDV_20260506T144229_20260506T144254_064398_081C09` |
| LATE_FOLLOW_UP / 1 | `S1A_IW_GRDH_1SDV_20260518T144204_20260518T144229_064573_082235_34DC_COG` | `S1A_IW_GRDH_1SDV_20260518T144204_20260518T144229_064573_082235` |
| LATE_FOLLOW_UP / 2 | `S1A_IW_GRDH_1SDV_20260518T144229_20260518T144254_064573_082235_E298_COG` | `S1A_IW_GRDH_1SDV_20260518T144229_20260518T144254_064573_082235` |

Each PC product must represent the exact native source product (CDSE `_COG`
discovery representation retained distinctly); **exactly one** match per slice.
Validate native identifier, acquisition **start/end interval**, platform, mode,
product, orbit and polarizations. PC midpoint datetime alone is insufficient.
Exact microsecond intervals and native product IDs are in the [JSON](evidence/AS_201_DESIGN_FREEZE.json).
No string-ID-only equivalence, nearest-date fallback or silent provider replacement.

Two slices/date are mandatory. Order acquisition-start UTC ascending then stable
provider item ID. Preserve each interval/footprint/source/access/provenance and
date union. AS-201 does **not** mosaic pixels or choose darkest/brightest overlaps.
No May 8/9/13/14 substitution or dropped inconvenient slice/date.

## Provider, representation and defensive metadata contract

Discovery: CDSE https://stac.dataspace.copernicus.eu/v1/ , `sentinel-1-grd`.
Raster/XML: PC https://planetarycomputer.microsoft.com/api/stac/v1/ ,
`sentinel-1-grd`; exact storage host **sentinel1euwest.blob.core.windows.net**,
container `s1-grd`. Anonymous short-lived token access was verified by M46, not
retested here. Access failure becomes **UNAVAILABLE / ACCESS_BLOCKED**; neither
RTC nor Sentinel Hub is a P0 fallback. A fallback needs a separate advance freeze.

Representation: **RAW_GRD_AMPLITUDE**, Level-1 IW GRDH detected multi-look ground
range, uint16, one band/polarization, nodata 0, 10 m range/azimuth sample spacing.
Independent resolution is coarser than 10 m (M46 PC metadata 20 m range/22 m azimuth).
No calibrated backscatter, denoising or RTC inferred from COG packaging.

M46 headers: classic little-endian TIFF, ZSTD, 1024² tiles, six reduced overview
levels, header-only range access, geographic tiepoints/geolocation. No native
affine pixel-scale/model-transform contract can be inferred from STAC transforms.
Use actual headers/geolocation for later preprocessing, not approximate STAC affine.
Inspected `proj:shape` was [width,height], reversed from usual semantics; headers
govern dimensions. Contradictory asset prose cannot redefine raw representation:
collection/source-product contract plus actual header/XML identity govern.

The `schema-product-vv` asset returned RFI XML. Old SAFE manifest names and an
rfi-prefixed normalized candidate returned 404; actual same-product
`annotation/iw-vv.xml` returned validated **product** XML. Resolver must validate
root/schema role, native product, polarization, acquisition, platform/mode/orbit
and measurement dimensions. The known provider normalized path is not a license
for arbitrary URL/date guesses. Incorrect/missing metadata makes slice unavailable.

Required per VV slice: measurement, SAFE manifest, main product annotation,
calibration and noise XML. Representative May 6 A43B metadata verified 27
calibration vectors (beta0/sigma0/gamma/DN LUT structures), 27 range-noise vectors,
3 azimuth-noise vectors, geolocation and incidence structures; counts are **not
universal requirements**. Every future slice validates its own applicable schema
and identity. Representative `thermalNoiseCorrectionPerformed=false`: never assume
already denoised; record per-slice true/false/unknown explicitly. Required metadata
missing/mismatched is unavailable, not another date. VH identity/access metadata
is retained as auxiliary; no first-implementation dependence on VH scientific use.
M46 tested one VH header, **not VH calibration/noise XML contents**.

## AS-201 API, identity, lineage and cache

Responsibility: discover → normalize → apply frozen policy → resolve exact IDs
→ validate access/representation metadata → group slices → stable provenance and
asset references → handoff **without scientific pixel transformation**.
Sentinel-1-specific search is required: no Sentinel-2 cloud query. Reuse suitable
HTTP/page validation, UTC/canonical hash, SourceRecord/registry and sanitised error
patterns. Complete generic pagination remains mandatory. No production helper
is written in M47. Existing S2 host/config/BOA/SCL/grid/cache assumptions are not SAR
contracts; do not introduce an unrelated generic refactor.

Immutable conceptual APIs (implementation names may follow existing style):

- **Sentinel1SliceSource:** SourceRecord, provider/collection/stable ID, platform,
  start/end, mode/polarizations, orbit direction/relative/absolute orbit, product/
  resolution/sampling, footprint/role, stable unsigned measurement and manifest/
  product/calibration/noise references, representation/noise state, fingerprint.
- **Sentinel1AcquisitionGroup:** role/canonical acquisition, required ordered slices,
  date union support, missingness diagnostics, fingerprint.
- **Sentinel1RetrievalSet:** policy/envelope, three role groups, common support,
  discovery/access provenance, limitations, fingerprint.

Coverage output includes envelope geometry, slice footprints, per-date source
support, common support and gap diagnostics. Actual future geometry must be retained
canonically, not approximated from scalar area summaries. Never persist SAS in types.
Use **as201-v1**, derived namespace **sentinel1_retrieval**. Register distinct CDSE
discovery and actual PC access SourceRecords, preserving their explicit one-to-one
association; retrieval DerivedProductRecord references registered sources in stable
slice order. Do not modify generic provenance schema or falsely equate provider IDs.
SourceRecord acquired_at uses start; SAR wrapper retains end and full SAR metadata.

Fingerprint commits policy/version, envelope, six CDSE/six PC IDs, roles/order,
orbit/mode/pols, provider collections, representation, coverage geometries and
metadata availability. Exclude SAS, signed query, expiry, request/creation time,
cache paths/mtimes. Existing canonical sorted compact finite JSON/SHA-256 conventions
are reusable; no disk cache schema is implemented now.

Cache future stable STAC/source metadata, appropriate XML and canonical retrieval
evidence. Runtime token-only access; never persist cookies/Authorization/signed URL.
Large rasters are not committed. Bounded range access preferred; no P0 full Product
ZIP. HTTPS only, exact allowlisted host, effective port443, no userinfo/fragment/
malformed URL; unexpected-host redirect rejected. Query values absent from errors/
logs/provenance; scoped logging suppression where needed. Stable unsigned path only.

## AS-202 ownership and explicitly unfrozen items

AS-202 owns scientific preprocessing: raw amplitude + product annotation +
calibration/noise LUT + geolocation/incidence + support. Noise/calibration is
explicit and documented **exactly once**. RAW_GRD_AMPLITUDE is eligible;
PROVIDER_CALIBRATED_BACKSCATTER must not be recalibrated as raw DN; RTC_GAMMA0 must
not receive second calibration/RTC; UNKNOWN_REPRESENTATION rejected/unavailable.
Official Sentinel-1 product specifications and actual XML schema/version define
LUT semantics, including modern **range AND azimuth** noise. No invented 1-D model.
This records a processing-specification requirement, not new official-document
retrieval/verification or executable equations in M47.

**SIGMA0_ELLIPSOID: CURRENT RECOMMENDED CANDIDATE / NOT YET FROZEN**: transparent
ellipsoid-area same-track open-water contract, avoiding unnecessary terrain
normalization complexity. Dedicated AS-202 pre-science design must freeze coefficient.
Not frozen: 2-D noise interpolation, clipping details, calibration equation,
coefficient, target CRS/grid, output resolution, resampling, speckle, mask source,
pixel overlap/mosaic. AS-203 threshold/spatial/polarization detection; AS-204
lookalike filters; AS-205 comparison/persistence; AS-206 scoring and AS-207 validation
classification also **NOT FROZEN**. Existing oil weights .45/.15/.20/.10/.10 remain
unchanged configuration hypotheses, not validated scientific constants.

## Missingness, claims and downstream acceptance requirements

Absent frozen CDSE product, zero/multiple unresolved PC matches, identity/polarization
mismatch, missing VV/required XML, unknown representation or blocked access:
explicit unavailable with reason; retain source/date/required slice slot, never
silently drop it or invent a fallback. Full retrieval-set readiness requires all
six required slices; partial support/availability remains visible.

Sequence/envelope frozen before SAR pixels: no date/provider/orbit/polarization
or threshold adjustment based on future output. Primary unit **documented_event_case**;
acquisition/region/pixel support secondary, pixels not petroleum truth samples.
One event does not establish sensitivity/specificity/FPR/precision/recall/ROC-AUC
or population accuracy. Low backscatter != petroleum: calm/low-wind/wind shadows,
rain, biological surfactants, fronts, wakes, coasts/infrastructure, thermal/border
noise, incidence and speckle remain lookalikes, **not already filtered**.
No real intake invented; later user-defined monitoring zone must be labelled demo.

Allowed: oil-slick candidate, low-backscatter surface anomaly, surface-slick
observational evidence, observational risk, monitoring priority, field verification
recommended. Forbidden: confirmed petroleum/chemistry, source attribution,
responsible vessel/infrastructure, oil probability, safe/unsafe water or shutdown.
M47 detects no candidate, computes no area/persistence/risk, and validates no biology.

Future AS-201 tests should cover complete pagination/no cloud query, exact six
mapping/cardinality, intervals/platform/orbit/mode/pols rejection, both slices/order,
support/gap preservation, raw-vs-calibrated/RTC/unknown classification, header-shape
defect, RFI-vs-product XML/404 normalization with strict identity, per-slice metadata,
VV-required/VH-auxiliary behavior, deterministic identity/time/token exclusion,
registry lineage, unavailable/no-substitution, URL/redirect/token/error/cache security
and defensive immutable metadata. Future metadata/access acceptance must produce
the exact fixed set with zero scientific pixel transformation. These tests/probes
are a future authorized task, not M47 execution.

## Design evidence and next authorization

Schema **as201-m47-design-freeze-v1**. Semantic SHA-256 **`11ce3efc96f62a539be899162b418718cd5ece9a8438cb44a1a4dce356a6f7f2`**.
Canonical input: JSON `design` only, sorted keys, compact separators, UTF-8,
ensure_ascii=false, allow_nan=false, fixed semantic array order. No request times,
future commit SHA, temporary path, SAS or display prose. The JSON carries exact
identity intervals/API semantics; historical audit facts are separate evidence.
See [M47 MD](evidence/AS_201_DESIGN_FREEZE.md) and [JSON](evidence/AS_201_DESIGN_FREEZE.json).
Next: owner review → separately authorized design PR/merge → separately authorized
AS-201 offline retrieval/source implementation. AS-202 needs its own pre-science
numerical design; no Decision 055 or implementation is authorized here.
