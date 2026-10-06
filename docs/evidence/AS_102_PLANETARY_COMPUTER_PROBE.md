# AS-102 research evidence — Planetary Computer probe

**Record created:** 6 October 2026 (Asia/Dubai).

**Evidence point:** Anonymous STAC/item inspection after Planetary Computer became reachable, before the additional raster-host allowlist update and before a bounded raster read. This is a historical checkpoint, not a claim about every later experiment or today's service status.

**Record basis:** The project owner's supplied reconstruction of experiments already performed. No network probe, signing, product-metadata read, or raster read was rerun for this documentation task. The original experiment date/time and raw command/provider transcripts were not supplied; they remain capture gaps. Reported direct observations and provider-advertised properties are separated below.

**Evidence IDs:** EV-011, EV-012, EV-013, EV-014; see the [presentation evidence index](PRESENTATION_EVIDENCE_INDEX.md).

## Purpose and scope

Evaluate Planetary Computer as a possible future raster-access path for the same Sentinel-2 observation previously inspected in CDSE. Discovery must use acquisition/platform/tile identity rather than identical item ID strings. This record does not select a backend, alter Decision 038, authorize AS-102, or implement AS-102/AS-103.

## Evidence classification

| Category | Meaning in this report |
|---|---|
| Directly observed evidence | Reported anonymous STAC response and inspected item/asset inventory from the earlier probe |
| Provider/STAC-advertised metadata | Item fields and advertised raster properties; no raster header/pixels confirm them at this checkpoint |
| Inference | Observation matching or feasibility assessment derived from the reported fields |
| Blocker | Additional runtime hostname allowlisting required before raster access |
| Recommendation | Further verification or provenance handling; not an adopted implementation decision |
| Unverified claim | Signing, reflectance decoding, raster access, or equivalence not established at this checkpoint |

## Directly observed catalog result

- Planetary Computer STAC anonymous access was **READY / HTTP 200** at the reported checkpoint.
- Endpoint: `https://planetarycomputer.microsoft.com/api/stac/v1/`.
- Collection: `sentinel-2-l2a`.
- Item identified for the Al Raha/tile/time investigation: `S2B_MSIL2A_20230428T064629_R020_T40RBN_20230428T122311`.
- The inspected item supplied the proposed nine reflectance bands and SCL. No separate cloud-probability asset was observed in this item.
- Raster hrefs pointed to **`sentinel2l2a01.blob.core.windows.net`**, requiring an additional Codex environment allowlist update. Raster access stopped at that boundary.

Anonymous catalog success does not establish signed asset access. The supplied record contains no exact search command/request body, retry counts, total item count, request timestamp, signing response, or raster byte count; none is invented here.

## Provider/STAC-advertised item identity

| Field | Recorded value |
|---|---|
| Item ID | `S2B_MSIL2A_20230428T064629_R020_T40RBN_20230428T122311` |
| Acquisition timestamp | `2023-04-28T06:46:29.024000Z` |
| Platform | `Sentinel-2B` in the supplied record; normalized comparison identity `sentinel-2b` |
| MGRS tile | `40RBN` |
| Relative orbit | `20` |
| Processing baseline | `05.09` |
| Generation | `2023-04-28T12:23:11.362052Z` |
| CRS | `EPSG:32640` |

These metadata fields support the cross-provider comparison below. They are not a claim that a raster header was read.

## Asset inventory and advertised delivery path

| Band / quality asset | Available in inspected item? | Advertised format / resolution retained in the supplied record |
|---|---|---|
| B02 / blue | Yes | 10 m COG / GeoTIFF |
| B03 / green | Yes | Exact per-asset format/resolution detail not retained in this summary |
| B04 / red | Yes | Exact per-asset format/resolution detail not retained in this summary |
| B05 / red edge | Yes | 20 m COG / GeoTIFF |
| B06 / red edge | Yes | Exact per-asset format/resolution detail not retained in this summary |
| B07 / red edge | Yes | Exact per-asset format/resolution detail not retained in this summary |
| B08 / NIR | Yes | Exact per-asset format/resolution detail not retained in this summary |
| B8A / narrow NIR | Yes | Exact per-asset format/resolution detail not retained in this summary |
| B11 / SWIR | Yes | Exact per-asset format/resolution detail not retained in this summary |
| SCL | Yes | 20 m COG / GeoTIFF |
| Separate cloud probability | Not observed in this item | Do not generalize absence to the collection or all providers |

The complete original asset-key list, exact media-type strings/roles, unsigned per-asset hrefs, dimensions, transforms, dtype, and nodata fields are not reproduced in the supplied summary. This table records semantic band availability without inventing a complete asset inventory. The reported raster host is `sentinel2l2a01.blob.core.windows.net`; no additional raster hostname is supplied.

**Inference:** Advertised COG assets provide a plausible remote-window delivery path. **Unverified:** Actual driver/layout, range support, header properties, tiny window shapes/DN values, and successful reads were not measured at this checkpoint. An advertised COG is not itself evidence of a working bounded read.

## Authentication, signing, and environment boundary

| Question | Status at this evidence point | Classification |
|---|---|---|
| Anonymous STAC search/item access | READY; HTTP 200 | Directly observed catalog evidence |
| Additional asset hostname | `sentinel2l2a01.blob.core.windows.net` | Observed href hostname |
| Additional environment allowlist update | Required before continuing raster access | Blocker |
| Raw href anonymous readability | Not established | Unverified claim |
| SAS signing without user credentials | Not established by the supplied checkpoint | Unverified claim |
| PC account/API key requirement for intended raster use | Not established by this checkpoint | Unverified claim |
| Bounded raster/header/window read | **PENDING**; had not yet been performed | EV-014 |

Do not persist credentials, SAS tokens, or signed URLs. This document stores only the stable STAC endpoint, collection, product IDs, and asset hostname. It contains no claim of successful signing or raster authentication.

## Reflectance semantics

The inspected Planetary Computer item **did not advertise explicit per-band raster scale/offset metadata**. At this checkpoint, product metadata had not been read to establish DN decoding.

- **Unverified:** The correct scale, offset, quantification value, nodata interpretation, and decoded sample values for this PC product.
- **Recommendation:** Inspect the actual product metadata, including the baseline-specific BOA offset/quantification, before decoding pixels. Record the exact metadata origin and band mapping.
- **Prohibited inference:** Do not assume DN / 10000, and do not copy CDSE's advertised `0.0001` / `-0.1` into this differently processed PC product without its own evidence.
- **Scientific limitation:** L2A BOA surface reflectance is not automatically aquatic remote-sensing reflectance or HAB evidence. Band availability and advertised SCL do not establish usable coastal water pixels.

## Cross-provider identity finding

| Identity field | CDSE | Planetary Computer | Finding / category |
|---|---|---|---|
| Product / item | `S2B_MSIL2A_20230428T064629_N0510_R020_T40RBN_20240831T052931` | `S2B_MSIL2A_20230428T064629_R020_T40RBN_20230428T122311` | Different product identities; observed metadata |
| Acquisition | `2023-04-28T06:46:29.024Z` | `2023-04-28T06:46:29.024000Z` | Same instant after timestamp normalization |
| Platform | `sentinel-2b` | `Sentinel-2B` / normalized `sentinel-2b` | Same spacecraft identity |
| MGRS tile | `40RBN` | `40RBN` | Match |
| Relative orbit | `20` | `20` | Match |
| Processing baseline | `05.10` | `05.09` | Different |
| Processing / generation | August 2024; ID suffix `20240831T052931` | `2023-04-28T12:23:11.362052Z` | Different processing/generation time |

**Inference supported by the identity fields:** These represent the **same underlying acquisition**, but **not the same processed product**. The match uses acquisition, platform, tile, and relative orbit; it does not rely on item ID equality. Different processing baselines and generation times prevent treating the products as interchangeable processed raster data.

**Unverified:** Pixel equivalence was **not established**. No cross-provider raster comparison or equality metric was performed at this checkpoint. Refer to the [CDSE report](AS_102_CDSE_ACCESS_PROBE.md) for its advertised metadata and blocked raster access.

**Provenance recommendation:** If Planetary Computer later supplies AS-102 pixels, preserve a provider-qualified `SourceRecord` for the **actual PC raster product**, with its PC catalog/collection/item identity. Do not label those pixels as the CDSE baseline-05.10 product. Preserve the discovery/matching context separately and ensure any derived provenance references the actual upstream raster source. Existing source/derived models and Decision 038 are unchanged by this documentation task.

## Readiness and next evidence

At this historical stage, **Planetary Computer remained viable, but was NOT READY for AS-102 raster implementation**: anonymous STAC worked and the required assets were advertised, while asset-host access, signing, product-metadata decoding, and bounded reads still needed verification.

EV-014 remains **PENDING** in this evidence pack. A later result must be added as a separately dated stage with actual command/tool context and observations; do not silently promote this earlier metadata-only checkpoint into a successful raster gate.

Recommended next verification, if separately authorized: allow the reported asset hostname, establish access/signing behavior without persisting tokens, inspect product metadata, and record tiny bounded B02/B05/SCL header/window results using existing tooling. No full-scene download, dependency installation, or implementation is part of this record.

Remaining capture gaps: original experiment timestamp/search transcript, sanitized STAC asset excerpts, signing/access evidence, product metadata fields and band mapping, bounded window samples, and any later final-gate report.

Suggested visuals still needed: anonymous catalog response summary, sanitized B02/B05/SCL delivery-path diagram, and the same-acquisition/different-product comparison table. Caption every figure with this checkpoint's pending raster status.
