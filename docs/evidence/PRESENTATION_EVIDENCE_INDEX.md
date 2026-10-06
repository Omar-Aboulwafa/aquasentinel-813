# AquaSentinel 813 — Presentation Evidence Index

**Created:** 6 October 2026 (Asia/Dubai).

**Purpose:** Compact claim-to-evidence index for the [presentation journal](../PRESENTATION_JOURNAL.md). This pack preserves the CDSE investigation, the **historical Planetary Computer metadata-only checkpoint**, and the [later successful final raster gate](AS_102_PLANETARY_COMPUTER_RASTER_GATE.md). It does not certify perpetual external-service availability, adopt a provider, or authorize/implement AS-102 or AS-103.

**Later evidence stage recorded:** 6 October 2026 (Asia/Dubai), FG-01. Original experiment timestamp not supplied; this is a later experiment than the preserved metadata-only checkpoint, not a new probe run by this documentation task.

## Evidence standard and temporal boundary

The historical probe reports and later raster-gate report transcribe the project owner's supplied factual reconstruction of completed investigations. “Directly observed” refers to those reported observations, not a new live probe performed when writing these documents. Original command logs, full STAC responses, exact experiment timestamps, and screenshots are not attached. Their absence is explicitly retained as a capture limitation.

Use these classifications: **directly observed evidence**, **provider/STAC-advertised metadata**, **inference**, **blocker**, **recommendation**, and **unverified claim**. An advertised format or grid does not prove a successful raster read. A provider recommendation is not an approved technical decision. A pending result must remain pending until a separately recorded experiment supports it.

EV-001–EV-008 index existing repository evidence. EV-009–EV-013 preserve the historical investigations. **EV-014 progresses from historical PENDING to later FG-01 PASS / READY**; both stages appear below, and the original PENDING row is preserved. EV-015 separates metadata-driven PC decoding from raster-access success. Record creation date, acquisition date, processing date, and experiment date must remain distinct.

## Claim index

| Evidence ID | Claim | Status | Metric/result | Source document | Suggested presentation use | Visual still needed? | Final validation needed? |
|---|---|---|---|---|---|---|---|
| EV-001 | Product thesis / Track 03 | Current approved product decisions | Water-quality/operations manager; monitoring/field-verification priority; two planned P0 hazards | [Decisions 001–015](../DECISIONS.md); [PRD §§1–5](../AquaSentinel_813_PRD_v1.0.md) | Problem/user/decision opening | Yes: operator-to-decision diagram | Yes for claimed operational impact; not for recorded thesis |
| EV-002 | AS-001 repository foundation | Completed engineering fact | Python 3.11, `src/` packaging, pytest/Ruff; `f878acc` | [Project State §6](../PROJECT_STATE.md); [pyproject](../../pyproject.toml) | Reproducible engineering foundation | Yes: package/setup capture | Fresh clean-environment reproduction before demo |
| EV-003 | AS-002 config/AOI | Completed engineering fact | TOML/GeoJSON validation and runtime context; `f606ac5`, `113ca44` | [Project State §7](../PROJECT_STATE.md); [runtime](../../src/aquasentinel/runtime.py) | Explicit geographic/scientific inputs | Yes: labelled Al Raha study map | Operational intake geometry remains separate/pending |
| EV-004 | AS-003 provenance | Completed engineering fact | Schema 1.0; historical 17-test project baseline; `e2baedc`, `db79260` | [Project State §§8–9](../PROJECT_STATE.md); [provenance](../../src/aquasentinel/provenance/) | Trace a future result to its source | Yes: labelled source/derived example | Real end-to-end derived hazard lineage remains future |
| EV-005 | Codex continuity | Completed recorded onboarding/handoff | AS-000C.1–8 completed; read-only audit at `779069d`; separate AS-101 authorization | [Project State §13](../PROJECT_STATE.md); [Handoff §§16–19](../HANDOFF.md) | Recoverable multi-machine/agent workflow | Yes: continuity sequence | Original full audit artifact not retained in tracked snapshot |
| EV-006 | AS-101 real Sentinel-2 search | Completed implementation and recorded experiment | AOI/date/cloud search, full pagination, deterministic candidates/provenance; PR #2 merge `1b83a73` | [AS-101 report](../AS_101_STAC_SEARCH.md) | Connect the use case to real catalog data | Yes: query-to-source diagram | Live services can change; raster usability not established |
| EV-007 | 44 candidate scenes | Directly observed catalog experiment | 44 unique products; 44/44 provenance conversions; 0.12–24.96% scene cloud; recorded 2 Oct 2026 | [AS-101 live result](../AS_101_STAC_SEARCH.md); [CDSE probe](AS_102_CDSE_ACCESS_PROBE.md) | First live-data evidence card | Yes: dated result card | Not a fixed future count; usable-water analysis pending |
| EV-008 | 97-test quality baseline | Recorded engineering validation | 97 tests passed, Ruff passed, diff check passed; 17 original tests retained | [AS-101 validation](../AS_101_STAC_SEARCH.md); [journal E09](../PRESENTATION_JOURNAL.md) | Quality/review evidence | Yes: dated test summary | Rerun before release; not scientific accuracy |
| EV-009 | CDSE reflectance offset discovery | Provider/STAC-advertised metadata; decoding inference | Scale `0.0001`, offset `-0.1`; valid DN decoding `DN * 0.0001 - 0.1` | [CDSE reflectance record](AS_102_CDSE_ACCESS_PROBE.md#reflectance-scaleoffset-discovery) | Explain why raw stored values need product semantics | Yes: sanitized metadata fields and formula | Yes: per-band metadata excerpts and decoded real sample |
| EV-010 | CDSE raster-access blocker | Observed environmental blocker; S3/OIDC route advertised | Proxy blocked live raster/header/window attempts; no full download; bounded access unverified | [CDSE access record](AS_102_CDSE_ACCESS_PROBE.md#access-route-and-blocker) | Catalog-versus-pixel-access distinction | Yes: access-boundary diagram | Yes: runtime transport and bounded read; do not infer universal provider denial |
| EV-011 | Planetary Computer STAC accessibility | Directly observed catalog evidence | Anonymous STAC READY / HTTP 200; corresponding item identified | [PC catalog result](AS_102_PLANETARY_COMPUTER_PROBE.md#directly-observed-catalog-result) | Evidence that an alternative catalog was reachable | Yes: sanitized catalog response | Raster signing/access still pending at this checkpoint |
| EV-012 | Same acquisition / different processed product | Metadata-supported inference; pixel equivalence unverified | Acquisition/platform/tile/orbit match; CDSE baseline 05.10/Aug 2024 versus PC 05.09/Apr 2023 | [Identity comparison](AS_102_PLANETARY_COMPUTER_PROBE.md#cross-provider-identity-finding) | Explain provenance during provider evaluation | Yes: comparison table | Metadata capture still needed; no pixel-equivalence claim |
| EV-013 | Planetary Computer COG delivery path | Provider/STAC-advertised metadata; viable-path inference | Nine proposed reflectance bands + SCL; B02 10 m, B05/SCL 20 m COG; host `sentinel2l2a01.blob.core.windows.net` | [PC assets/access](AS_102_PLANETARY_COMPUTER_PROBE.md#asset-inventory-and-advertised-delivery-path) | Potential route to bounded raster access | Yes: host-to-window diagram | Yes: allowlist/access, signing, header/window support, decoding |
| EV-014 | AS-102 bounded raster read | **PENDING — unverified at this evidence point** | No bounded read had yet been performed in the recorded PC stage; no DN/window result | [PC readiness](AS_102_PLANETARY_COMPUTER_PROBE.md#readiness-and-next-evidence) | Explicit remaining feasibility gate | Yes: actual tiny-window evidence after verification | **Yes; do not mark successful from catalog/COG metadata** |
| EV-014 · FG-01 | AS-102 bounded raster read — later final gate | **PASS / READY for tested PC product/path** | 3 successful bounded raster reads; 4 credential-free HTTP 200 signing operations; product XML read; metadata-driven B02/B05 decoding; **8/8 readiness gates passed** | [Later raster-gate record](AS_102_PLANETARY_COMPUTER_RASTER_GATE.md) | Show progression from catalog metadata to real bounded pixels | Yes: sanitized header/window/signing captures | Historical result reported; complete-band preprocessing, scientific suitability, and repeatability captures remain future |
| EV-015 | Metadata-driven PC reflectance decoding | Observed XML and DN samples; metadata-derived interpretation | XML 53,347 bytes; baseline 05.09; quantification 10000; offset -1000; B02 bandId 1/B05 bandId 4; `(DN - 1000) / 10000` | [XML and decoding evidence](AS_102_PLANETARY_COMPUTER_RASTER_GATE.md#product-xml-and-metadata-driven-interpretation) | Explain modern-baseline offsets with actual product metadata | Yes: XML field/band-map excerpt and sample table | Mechanics established for tested bands; aquatic suitability, quality masking, and pixel equivalence not established |

### EV-014 evidence progression

| Stage / record date | Status | Evidence boundary |
|---|---|---|
| Historical checkpoint, recorded 6 Oct 2026 | **PENDING** | Anonymous catalog/advertised COGs only; [original report](AS_102_PLANETARY_COMPUTER_PROBE.md) remains unchanged |
| Later experiment FG-01, recorded 6 Oct 2026 | **PASS / READY** | GDAL 3.10.3 B02 64×64, B05 32×32, SCL 32×32 reads; signed XML and metadata-driven decoding; [new report](AS_102_PLANETARY_COMPUTER_RASTER_GATE.md) |

Original experiment timestamps were not supplied; report dates do not imply the experiments happened simultaneously. **AS-102 raster-access prerequisite READY; AS-102 NOT YET IMPLEMENTED; AS-103 NOT STARTED.** The SCL sample contains 353/1024 raw water-class pixels, not a final usable-water count. Exact transferred raster bytes were not measured.

No visual is claimed to exist merely because it is suggested here. A metadata inventory, 44 catalog products, and 97 passing software tests do not establish HAB detection, aquatic reflectance suitability, a safe/unsafe water decision, or operational warning lead time.

## Remaining evidence and presentation gaps

- Original probe task/command transcripts, dates/times, tool versions, sanitized STAC/asset metadata excerpts, and actual screenshots.
- CDSE raster transport/authentication and bounded range/window access; no provider-global access conclusion from the environment proxy blocker.
- The later FG-01 report now records credential-free signing, B02/B05/SCL headers/windows, and XML-based decoding. Original timestamps/commands/8-gate checklist, sanitized XML/header/status captures, and untested reflectance-band reads still need evidence; do not relabel the earlier checkpoint as successful.
- Complete per-provider inventories and field provenance; no cross-provider pixel-equivalence result.
- Exact raster-transfer bytes were not measured; compressed blocks may exceed the requested pixel window. No byte-efficiency claim is supported.
- Valid-water fractions, aligned optical products, historical HAB/oil validation, false positives, operational demo site, cached demo fallback, and measured impact. These remain future evidence, not delivered capabilities.
- Approved AS-102 contract/provider choice and separate implementation authorization; no AS-103 work is authorized by this pack.

## Presentation capture rule

For every important experiment, future agents must record:

- Command/task purpose and the exact bounded method used.
- Experiment timestamp/date and timezone, separately from the report-creation date and product dates.
- Source/provider and stable catalog/collection references.
- Item/product identity, acquisition context, and processing baseline/version where relevant.
- Quantitative result, units/denominator, and whether it is observed, advertised, inferred, or unverified.
- Limitation, failure/blocker, remaining uncertainty, and authorization boundary.
- Screenshot/visual requirement, caption, capture status, and attribution/licence.
- Repository evidence file and relevant commit/PR reference when available.

Do **not** store credentials, SAS tokens, signed URLs, or secrets. Use sanitized unsigned references and metadata excerpts. Do not commit full EO scenes or runtime caches as presentation evidence.

After an evidence record exists, update the journal and affected EV entries. Preserve the old dated checkpoint when adding a later successful or failed gate; never rewrite a metadata-only stage as if it already contained pixel evidence. Scientific/provider decisions continue to be governed by the existing decision log and explicit authorization.
