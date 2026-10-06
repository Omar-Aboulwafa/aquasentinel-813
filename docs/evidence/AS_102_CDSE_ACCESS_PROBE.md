# AS-102 research evidence — CDSE access probe

**Record created:** 6 October 2026 (Asia/Dubai).

**Evidence point:** Completed CDSE metadata/access investigation, before any successful bounded raster read. The original probe date/time was not supplied; acquisition and processing dates below are product dates, not experiment dates.

**Record basis:** The project owner's supplied reconstruction of experiments already performed, plus the existing [AS-101 report](../AS_101_STAC_SEARCH.md). This documentation task did not repeat network requests or read rasters. Raw provider responses, command transcripts, and screenshots are not attached; their capture remains an evidence gap. “Observed” below means reported direct observation during that earlier probe, not a new observation on the record-creation date.

**Evidence IDs:** EV-006, EV-007, EV-009, EV-010; see the [presentation evidence index](PRESENTATION_EVIDENCE_INDEX.md).

## Purpose and scope

Determine whether real CDSE Sentinel-2 L2A candidates provide the bands, reflectance metadata, and raster-access route needed for future optical preprocessing. The investigation inspected catalog metadata and attempted bounded access. AS-102 was not implemented, AS-103 was not started, and no scientific/provider decision is changed by this record.

The configured Al Raha polygon is an analyst-defined validation AOI, not an official boundary or a desalination intake. AS-101's recorded query used 1 March–31 May 2023 and scene cloud cover <= 30%.

## Evidence classification

| Category | Meaning in this report |
|---|---|
| Directly observed evidence | Outcome reported from the earlier query, item inspection, or access attempt |
| Provider/STAC-advertised metadata | A value or capability described by provider metadata, without a raster header/pixel read verifying it |
| Inference | A conclusion derived from supplied metadata, with its assumptions stated |
| Blocker | An observed environmental obstacle preventing verification |
| Recommendation | A future handling requirement or next verification step; not implemented here |
| Unverified claim | An outcome that the probe did not establish |

## Directly observed evidence

- The Al Raha AS-101 search returned **44 unique candidate scenes**. The existing report dates that search to **2 October 2026**, with **44/44** successful provenance conversions and serializations. This is a catalog result, not a count of usable water scenes.
- The investigation selected the CDSE item `S2B_MSIL2A_20230428T064629_N0510_R020_T40RBN_20240831T052931` and observed **47 assets** in its metadata. The AS-101 report separately records 47 references for its first March candidate; these refer to different items and must not be conflated.
- The Codex environment proxy blocked attempted live raster/header/window access. No successful bounded remote raster read was established.
- No full raster or product was downloaded during the investigation.

The supplied reconstruction does not include exact commands, attempted raster hostnames, request timestamps, HTTP response codes, byte counts, tool versions, or screenshots. Do not invent them or turn the proxy block into an observed provider-side rejection.

## Provider/STAC-advertised identity

| Field | Recorded value | Evidence classification |
|---|---|---|
| Catalog | `https://stac.dataspace.copernicus.eu/v1/` | Existing AS-101 provider configuration |
| Collection | `sentinel-2-l2a` | Provider metadata / configuration |
| Item / product ID | `S2B_MSIL2A_20230428T064629_N0510_R020_T40RBN_20240831T052931` | Inspected item identity |
| Acquisition | `2023-04-28T06:46:29.024Z` | Provider metadata |
| Platform | `sentinel-2b` | Provider metadata |
| MGRS tile | `40RBN` | Provider metadata |
| Relative orbit | `20` | Supplied cross-provider identity record; also encoded as `R020` |
| Processing baseline | `05.10` | Provider metadata; also encoded as `N0510` |
| Generation / reprocessing | August 2024 | Supplied processing metadata record |
| Generation suffix | `20240831T052931` | Product ID text; an encoded timestamp, not an independently verified header field |
| Asset count | `47` | Observed metadata inventory count |

The 2023 observation date and August 2024 reprocessing belong to different events. Do not describe the product as acquired in August 2024.

## Advertised assets, format, and grid

| Asset group | Recorded availability | Advertised resolution | Verification limit |
|---|---|---|---|
| B02, B03, B04, B08 reflectance | Available | 10 m native reflectance assets | Metadata only; no native raster header/pixels read |
| B05, B06, B07, B8A, B11 reflectance | Available | 20 m native reflectance assets | Metadata only; no alignment or reflectance values verified |
| SCL scene classification | Available | 20 m asset advertised | No class distribution or water-mask performance measured |
| `CLD_20m` cloud-quality asset | Available | 20 m | No probability values, calibration, or threshold effectiveness verified |

The proposed nine-band set is B02, B03, B04, B05, B06, B07, B08, B8A, and B11, plus SCL. Listing availability does not approve an AS-102 implementation contract. The complete 47-key inventory, exact per-key hrefs/media types/roles, and any additional resolutions are not retained in the supplied summary.

Provider metadata advertises **JP2** rasters, **EPSG:32640**, and **10 m / 20 m** resolutions. These are advertised properties, not successful GDAL/Rasterio header observations. Dimensions, transforms, driver behavior, compression, dtype, and range/window support remain unverified by this access probe.

## Reflectance scale/offset discovery

The inspected CDSE STAC raster metadata explicitly advertised:

| Field | Value | Classification |
|---|---:|---|
| Scale | `0.0001` | Provider/STAC-advertised raster metadata |
| Offset | `-0.1` | Provider/STAC-advertised raster metadata |

**Inference from those fields:** For this advertised product representation, decode valid stored values as:

```text
reflectance = DN * 0.0001 - 0.1
```

This includes the advertised additive offset; assuming DN / 10000 alone would omit it. The discovery is metadata evidence, not a decoded-pixel experiment, and the values must not be applied automatically to another provider or differently processed product.

**Recommended handling:** Mask **DN=0 before decoding**; do not automatically clamp valid negative reflectance. These are recorded decoding constraints for future work, not implemented behavior. Preserve the provider metadata origin and product baseline when later validating the conversion.

**Unverified:** No successfully read DN sample, decoded reflectance sample, cross-band consistency result, or independent product-metadata comparison was established by this CDSE access attempt. A full sanitized STAC excerpt with per-band field provenance is still needed for a presentation screenshot.

## Access route and blocker

| Question | Recorded finding | Classification |
|---|---|---|
| Can catalog metadata be searched? | Yes; AS-101 returned 44 candidates without credentials | Directly observed catalog evidence |
| What route does the asset metadata describe? | S3/OIDC-authenticated asset routes | Provider/STAC-advertised access description |
| Were live raster/header/window reads successful? | No verified read; the environment proxy blocked the attempts | Environmental blocker |
| Was a full scene downloaded? | No full raster/product download | Reported experiment boundary |
| Does this prove the provider universally denies anonymous access? | No | Unverified; do not infer from a proxy block |
| Does this prove authenticated S3 works in the intended runtime? | No | Unverified |
| Does this prove remote range/window support? | No; bounded remote access remained unverified | Unverified |

The blocker prevented the probe from separating provider access requirements from actual runtime transport behavior. Do not report successful authentication, header inspection, native-grid verification, or usable pixels.

## Scientific limitation

Sentinel-2 L2A **BOA surface reflectance is not automatically aquatic remote-sensing reflectance**. Atmospheric correction, coastal adjacency, turbidity, cloud/shadow contamination, and aquatic suitability still require evaluation. Advertised scale/offset, SCL, and a cloud-quality asset do not establish HAB detection, toxic species/toxins, water safety, or validated monitoring lead time.

## Implications and remaining evidence

- **Inference:** CDSE metadata supplies an explicit reflectance conversion for this product representation; pixel access remains a separate question.
- **Recommendation:** Preserve a sanitized asset inventory and raster metadata excerpt, then document a genuinely bounded access result if separately authorized. Do not download a full tile to bypass the probe boundary.
- **Recommendation:** Keep the actual product identity in provenance. See the [cross-provider comparison](AS_102_PLANETARY_COMPUTER_PROBE.md#cross-provider-identity-finding) before substituting another provider's pixels.
- **Pending evidence:** Original experiment timestamp/commands, metadata excerpts, exact access route/hosts, authenticated transport feasibility, bounded window result, and decoded sample verification.
- **Presentation use:** EV-009 explains why scale/offset matters; EV-010 explains the separation between searchable metadata and readable pixels. A proxy blocker is engineering evidence, not a finding about water conditions.

Suggested visuals still needed: sanitized scale/offset metadata excerpt, selected-product identity card, and catalog-versus-raster access diagram with the environmental blocker explicitly labelled.
