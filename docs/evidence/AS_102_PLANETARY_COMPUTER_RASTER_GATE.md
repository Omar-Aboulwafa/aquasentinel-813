# AS-102 research evidence — final Planetary Computer raster-access gate

**Stage:** FG-01 — later successful raster-access experiment.

**Stage recorded:** 6 October 2026 (Asia/Dubai). The original experiment timestamp was not supplied. This experiment occurred after the [historical metadata-only checkpoint](AS_102_PLANETARY_COMPUTER_PROBE.md), where EV-014 was PENDING; that earlier report remains unchanged.

**Record basis:** The project owner's supplied results of an already performed final gate. This documentation task did not repeat signing, network requests, XML retrieval, or raster reads. Reported observations are transcribed below; original command logs, metadata excerpts, and screenshots remain capture gaps. Acquisition/generation dates are product dates, not the date of this record or an invented experiment timestamp.

**Evidence:** EV-014 later stage — **PASS / READY**, and EV-015 — metadata-driven reflectance decoding. See the [evidence index](PRESENTATION_EVIDENCE_INDEX.md).

## Purpose, classification, and result

**Question:** Can AquaSentinel retrieve real Sentinel-2 pixels without downloading the full scene or providing user credentials?

**Observed result:** Yes, for the tested Planetary Computer product/path: **3 bounded raster reads**, **4 credential-free signing operations**, a product XML read, and XML-driven B02/B05 decoding. The supplied final-gate result is **8/8 readiness gates passed**; the original gate checklist/command transcript is not attached, so individual criterion names are not reconstructed here.

“Observed” means an outcome reported from that completed experiment. “Metadata-derived interpretation” means decoding derived from retrieved XML fields. “Inference” means a conclusion limited to the tested path. Remaining limitations and future provenance requirements are labelled separately. No provider or scientific decision is changed by this evidence record.

## Confirmed product identity

| Field | Recorded value |
|---|---|
| STAC provider | `https://planetarycomputer.microsoft.com/api/stac/v1/` |
| Collection | `sentinel-2-l2a` |
| Item / product | `S2B_MSIL2A_20230428T064629_R020_T40RBN_20230428T122311` |
| Acquisition | `2023-04-28T06:46:29.024000Z` |
| Platform | `Sentinel-2B` |
| MGRS tile | `40RBN` |
| Relative orbit | `20` |
| Processing baseline | `05.09` |
| Generation | `2023-04-28T12:23:11.362052Z` |
| CRS | `EPSG:32640` |
| Asset hostname | `sentinel2l2a01.blob.core.windows.net` |

Identity fields come from the inspected product/provider metadata; CRS was also observed through GDAL raster headers. The product XML confirmed baseline 05.09.

## Credential-free signing evidence

Official signing endpoint: `https://planetarycomputer.microsoft.com/api/sas/v1/sign`.

| Asset signed | Observed response | User credentials / subscription key |
|---|---|---|
| B02 | HTTP 200 | None used |
| B05 | HTTP 200 | None used |
| SCL | HTTP 200 | None used |
| product-metadata | HTTP 200 | None used |

SAS material remained transient in memory. No SAS token or signed URL was persisted or printed. The four successful operations establish credential-free signing for these tested assets; they are not a permanent guarantee of service availability or a claim about every product/account policy. No raw unsigned-href anonymity result is inferred from successful signed access.

## Observed raster headers and native grids

GDAL **3.10.3** inspected the remote assets via `/vsicurl/`.

| Property | B02 | B05 | SCL |
|---|---|---|---|
| Driver / layout | GTiff / COG | GTiff / COG | GTiff / COG |
| Dimensions (width × height) | 10980 × 10980 | 5490 × 5490 | 5490 × 5490 |
| Native pixel size | 10 m | 20 m | 20 m |
| CRS | EPSG:32640 | EPSG:32640 | EPSG:32640 |
| Dtype | UInt16 | UInt16 | UInt8 / uint8 |
| Nodata | 0 | 0 | 0 |
| Blocks | 512 × 512 | 512 × 512 | 512 × 512 |
| Compression | DEFLATE | DEFLATE | DEFLATE |
| Overview dimensions | 5490², 2745², 1373², 687², 344² | 2745², 1373², 687², 344², 172² | 2745², 1373², 687², 344², 172² |

Affine coefficients below use `[a, b, c, d, e, f]`, where `x = a*column + b*row + c` and `y = d*column + e*row + f`, in projected metres. This is matrix coefficient order, not GDAL's six-element geotransform ordering.

```text
B02:     [10, 0, 199980, 0, -10, 2800020]
B05/SCL: [20, 0, 199980, 0, -20, 2800020]
```

B05 and SCL share the same native transform/grid. This verifies the tested native grids; it is not an implemented canonical 20 m analysis grid or evidence that all nine reflectance bands were read/aligned.

## Observed bounded window reads

The configured Al Raha AOI was transformed to EPSG:32640. A shared tested footprint inside it was:

```text
[xmin, ymin, xmax, ymax] = [251780, 2704820, 252420, 2705460]
Approximate physical footprint: 640 × 640 m
```

The Al Raha polygon remains an analyst-defined validation AOI, not an operational desalination intake.

| Read | Pixel window `(xoff, yoff, width, height)` | Array shape / dtype | Nodata count | Valid DN range | Example DN values |
|---|---|---|---:|---|---|
| B02 | `(5180, 9456, 64, 64)` | 64 × 64 / uint16 | 0 | 1284–4836 | 1284, 1286, 1288, 1289, 1291, 1292 |
| B05 | `(2590, 4728, 32, 32)` | 32 × 32 / uint16 | 0 | 1017–6301 | 1017, 1024, 1028, 1032, 1033, 1038 |
| SCL | Same window/physical footprint as B05 | 32 × 32 / uint8 | 0 inferred from the complete nonzero-class distribution below | Categorical classes, not reflectance DN | 4, 5, 6, 7 |

Raw SCL classification distribution:

| Class | Label | Pixel count |
|---:|---|---:|
| 4 | Vegetation | 58 |
| 5 | Not vegetated | 540 |
| 6 | Water | 353 |
| 7 | Unclassified | 73 |
| Total | All sampled pixels | 1024 |

These are **raw SCL classifications inside the probe window**. **353 water-class pixels do not equal final usable-water pixels after AS-102 masking.** No valid-water mask/count/fraction was produced. Reflectance samples above are not necessarily quality-masked water pixels.

## Product XML and metadata-driven interpretation

The signed **product-metadata XML was successfully read: 53,347 bytes**. This is the XML document size, not a raster-transfer measurement.

Observed XML values:

| Field | Value |
|---|---|
| `PROCESSING_BASELINE` | `05.09` |
| `BOA_QUANTIFICATION_VALUE` | `10000` |
| `BOA_ADD_OFFSET` | `-1000` for declared band IDs 0–12 |

The mapping came from XML `Spectral_Information` metadata:

| Raster band | XML `physicalBand` | XML `bandId` | Additive offset |
|---|---|---:|---:|
| B02 | B2 | 1 | -1000 |
| B05 | B5 | 4 | -1000 |

STAC/TIFF did not supply assigned scale/offset values for this PC item. **The retrieved product XML is the decoding source.** The offset was established for the actual PC baseline-05.09 product rather than copied from CDSE baseline-05.10 metadata or assumed from the acquisition year.

Metadata-derived reflectance decoding for valid B02/B05 values:

```text
rho_BOA = (DN - 1000) / 10000
        = DN * 0.0001 - 0.1
```

| Band | Observed DN | Metadata-derived BOA reflectance |
|---|---:|---:|
| B02 | 1284 | 0.0284 |
| B02 | 1286 | 0.0286 |
| B02 | 1288 | 0.0288 |
| B05 | 1017 | 0.0017 |
| B05 | 1024 | 0.0024 |
| B05 | 1028 | 0.0028 |

Nodata was masked before decoding; the sampled B02/B05 windows contained no nodata values. Decoding used **no clipping to 0..1**; valid negative reflectance must not be automatically clamped. The arithmetic demonstrates metadata-driven decoding mechanics, not radiometric accuracy, aquatic atmospheric suitability, or final water-pixel quality. SCL is categorical and does not use this reflectance formula.

## Remote-access boundary and efficiency limitation

Observed: GDAL `/vsicurl/` remote access, header inspection, and bounded pixel-window reads succeeded. No full raster download, SAFE ZIP, full-product fallback, or full-scene statistics were used. Signed material was transient; no raw scene or probe pixel arrays are added to this documentation pack.

**Exact transferred bytes were not measured.** COG/GDAL may fetch compressed blocks larger than the requested pixel window. Successful bounded reads establish the tested remote window path; they do not establish exact HTTP request/range sizes, a precise bandwidth saving, an all-band runtime benchmark, or complete-scene accessibility under all conditions.

## Cross-provider distinction

| Field | CDSE | Planetary Computer |
|---|---|---|
| Product | `S2B_MSIL2A_20230428T064629_N0510_R020_T40RBN_20240831T052931` | `S2B_MSIL2A_20230428T064629_R020_T40RBN_20230428T122311` |
| Processing baseline | 05.10 | 05.09 |
| Processing / generation | August 2024 | `2023-04-28T12:23:11.362052Z` |

**Same underlying acquisition: YES**, supported by acquisition timestamp, platform, tile, and relative orbit. **Same processed product: NO. Pixel equivalence: NOT ESTABLISHED.** The successful PC reads do not validate access to or pixel equivalence with the CDSE product. See the unchanged [historical comparison](AS_102_PLANETARY_COMPUTER_PROBE.md#cross-provider-identity-finding) and [CDSE report](AS_102_CDSE_ACCESS_PROBE.md).

## Provenance implication for future AS-102 products

Future products using PC pixels must reference a **distinct provider-qualified Planetary Computer `SourceRecord` for the actual raster product**, not the CDSE source identity. The logical source/provenance record must retain:

- Provider/catalog and collection.
- Item/product identity, acquisition, and platform.
- MGRS tile, relative orbit, processing baseline, and generation time.
- Unsigned asset identities and source grids.
- Nodata and XML decoding metadata, including the quantification, offsets, and band mapping.

The current typed `SourceRecord` directly holds core identity/catalog fields; it does not declare all of the additional grid/processing/asset fields above. Future implementation design must specify how associated source metadata and derived processing parameters retain them. No schema extension, manifest, or preprocessing product is implemented by this record.

SAS tokens and signed URLs must **never** enter provenance, cache identity, manifests, or logs. Use stable unsigned asset identity and preserve the actual PC product lineage. This is an evidence/provenance requirement, not an approved provider switch.

## Readiness and scientific limits

| State | Recorded result |
|---|---|
| Historical EV-014 metadata-only checkpoint | PENDING; preserved in the earlier report/index stage |
| Later final raster-access gate | **PASS / READY — 8/8 gates passed** |
| AS-102 raster-access prerequisite | **READY for the tested PC product/path** |
| AS-102 implementation | **NOT YET IMPLEMENTED**; separate authorization required |
| AS-103 | **NOT STARTED** |

This experiment establishes **data access and decoding mechanics**. It does **not** establish aquatic atmospheric suitability, final valid-water count, HAB detection, chlorophyll concentration, toxic algae, warning lead time, or operational intake risk. It does not approve a masking policy, canonical grid, provider architecture, or scientific model. Only B02, B05, and SCL were raster-tested; a full AS-102 band set and preprocessing acceptance remain future work.

## Presentation takeaway and capture gaps

> From catalog metadata to real satellite pixels — reproducibly, remotely, and without downloading the full scene.

Use that takeaway with the tested product/path and bounded-window scope stated. Evidence supports a reproducible method; the exact original command transcript and experiment timestamp still need capture, and no rerun was performed when writing this record.

Recommended future visual:

```text
Planetary Computer STAC
→ temporary SAS signing
→ COG range/window access
→ product XML
→ reflectance decoding
→ future AS-102 masks/alignment
```

Label masks/alignment as future work. Still-needed sanitized captures: original dated task/command and 8-gate checklist; four HTTP-status results without tokens; GDAL header/window summary; SCL distribution labelled raw classes; XML baseline/quantification/offset and `Spectral_Information` excerpts; decoding example table; same-acquisition/different-product figure. No signed URL, SAS token, credentials, or full EO raster belongs in screenshots or repository evidence.
