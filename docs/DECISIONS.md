# AquaSentinel 813 — Architecture & Product Decisions

**Last updated:** 2 October 2026
**Status:** Active decision log
**Repository:** `Omar-Aboulwafa/aquasentinel-813`

This document records important project decisions and the reasoning behind them so that future ChatGPT sessions, Codex tasks, developers, or collaborators can continue the project without relying on conversation history.

---

## Decision 001 — Choose Track 03: Water Security & Marine Environments

### Decision

AquaSentinel 813 will compete under:

**Track 03 — Water Security & Marine Environments**

### Why

The track offers a strong intersection of:

- real UAE/Gulf operational relevance,
- Earth-observation suitability,
- hyperspectral relevance,
- clear public-sector / utility users,
- measurable operational impact,
- commercial potential beyond the hackathon.

Marine threats can directly affect desalination infrastructure, making the problem operational rather than purely academic.

### Consequence

The PoC is designed around seawater-intake monitoring and early-warning intelligence.

---

## Decision 002 — Focus on Desalination Intake Intelligence

### Decision

The primary product user is:

**Desalination Plant Water Quality / Operations Manager**

The primary decision supported is:

> Where and when should monitoring or field verification be prioritized?

### Why

A narrowly defined operational user is stronger than building a generic “marine monitoring platform.”

The product must support a real decision, not merely visualize satellite data.

### Consequence

AquaSentinel outputs must be translated into:

- risk level,
- evidence,
- confidence,
- exposure,
- monitoring priority,
- recommended verification.

---

## Decision 003 — Product Positioning Is Early-Warning Intelligence, Not Detection Alone

### Decision

AquaSentinel is not positioned as:

> an AI algae detector

or:

> an oil-spill map

It is positioned as:

> an explainable marine-intake early-warning and monitoring-prioritization system.

### Why

Detection alone does not create sufficient operational value.

The stronger product chain is:

Observation
→ Detection
→ Explanation
→ Exposure
→ Risk
→ Monitoring Priority
→ Human Decision

### Consequence

Every hazard module must eventually connect to an operational monitoring decision.

---

## Decision 004 — Adopt a Multi-Hazard Product Vision

### Decision

The long-term product vision is multi-hazard marine-intake intelligence.

The PoC includes:

- HAB / biological anomaly as the primary hazard.
- Oil-slick candidate detection as the secondary hazard.

### Why

A desalination operator cares about any offshore event that could affect intake conditions, not only one environmental phenomenon.

Recent Gulf-region events demonstrate that both biological anomalies and marine pollution are operationally relevant.

### Consequence

The architecture must support multiple independent hazard modules without forcing unrelated hazards into one scientific model.

---

## Decision 005 — HAB Is the Primary PoC Hazard

### Decision

The biological-anomaly / HAB pipeline is the primary and most complete PoC hazard module.

### Why

It provides:

- strong fit with Track 03,
- natural Sentinel-2 use,
- strong hyperspectral relevance,
- clear water-security value,
- historical UAE validation opportunities,
- a strong early-warning narrative.

### Consequence

The HAB pipeline receives implementation priority before advanced oil, environmental, or hyperspectral features.

---

## Decision 006 — Oil Is the Secondary PoC Hazard

### Decision

Oil-slick candidate detection is the second hazard module.

### Why

It demonstrates that AquaSentinel is a platform for intake protection rather than a single-purpose algae product.

Sentinel-1 SAR also provides a technically distinct sensing modality and cloud-independent observation.

### Consequence

The oil module should remain smaller than the HAB module during the PoC.

---

## Decision 007 — Use Sentinel-2 as the Main Biological-Anomaly Sensor

### Decision

Sentinel-2 is the P0 optical data source for HAB-related and biological water-quality anomaly analysis.

### Intended uses

- water colour,
- chlorophyll-related signals,
- red-edge features,
- temporal change,
- spectral anomaly detection.

### Why

Sentinel-2 offers:

- suitable spectral bands,
- strong public availability,
- repeat observations,
- regional coverage,
- compatibility with STAC-based workflows.

### Consequence

AS-101 begins with Sentinel-2 STAC search before any full-image processing.

---

## Decision 008 — Use Sentinel-1 SAR for Oil-Slick Candidates

### Decision

Sentinel-1 is the primary P0 source for oil-slick candidate detection.

### Why

SAR can detect surface roughness changes that may correspond to oil slicks and remains usable through cloud cover.

### Scientific constraint

Low SAR backscatter does **not** uniquely prove petroleum.

Look-alikes can include:

- low-wind areas,
- natural films,
- biological surface films,
- other surface effects.

### Consequence

Product wording must use:

> oil-slick candidate

and include confidence/context rather than claiming confirmed oil.

---

## Decision 009 — Hyperspectral Is P1, Not a P0 Dependency

### Decision

EnMAP / Satellite 813-style hyperspectral analysis is an enhancement layer.

P0 must work without it.

### Why

Hyperspectral data is valuable for:

- detailed spectral characterization,
- increased confidence,
- comparison with multispectral observations.

However, tying the entire PoC to scene availability or restricted data access creates delivery risk.

### Consequence

The baseline must work with Sentinel-2 / Sentinel-1 first.

Hyperspectral work is added only after P0 is stable.

---

## Decision 010 — Do Not Depend on Native Satellite 813 Data for the PoC

### Decision

The PoC architecture must not require direct Satellite 813 imagery to function.

### Why

Access and availability may be limited or staged by the hackathon.

### Consequence

The system must be demonstrable with openly accessible EO sources first.

Satellite 813 can later be positioned as a high-value enhancement.

---

## Decision 011 — Use Explainable Risk Before Complex ML

### Decision

Start with transparent anomaly/risk logic and simple models.

Do not start with deep learning merely for sophistication.

### Why

The PoC must be:

- explainable,
- reproducible,
- defensible to judges,
- implementable before the deadline.

### Consequence

Initial risk scoring may use configurable heuristic weights or simple baseline models.

More advanced ML is permitted only when labels, validation quality, and time justify it.

---

## Decision 012 — Risk Weights Are Hypotheses, Not Scientific Constants

### Decision

Current HAB and oil risk weights are configurable PoC assumptions.

### Why

They have not been scientifically validated as universal operational weights.

### Consequence

The product and documentation must not represent them as validated constants.

Changes to risk weighting should be documented.

---

## Decision 013 — Never Average Unrelated Hazards Into One Scientific Score

### Decision

HAB risk and oil risk remain separately interpretable.

### Why

They are scientifically different phenomena with different evidence and uncertainty.

### Consequence

If an overall site status is needed, it should reflect the highest credible active hazard rather than mathematically averaging unrelated hazard classes.

---

## Decision 014 — Remote Sensing Outputs Are Observational, Not Confirmatory

### Decision

AquaSentinel must use conservative scientific language.

Allowed wording includes:

- HAB-like spectral anomaly,
- elevated biological water-quality risk,
- oil-slick candidate,
- field verification recommended,
- observational risk,
- confidence.

### Prohibited overclaims

Do not claim satellite observations alone have:

- confirmed toxic algae,
- confirmed algal toxin,
- confirmed petroleum composition,
- certified water safe/unsafe,
- justified autonomous plant shutdown.

### Consequence

The product is decision support, not laboratory confirmation.

---

## Decision 015 — Keep Human Verification in the Loop

### Decision

AquaSentinel recommends monitoring and verification actions.

It does not autonomously shut down plant operations.

### Why

Desalination operations are safety-critical and require qualified human decision-making.

### Consequence

The primary action language is:

> prioritize field verification / increase monitoring

rather than:

> stop intake / shut down plant.

---

## Decision 016 — Use Historical Events for Validation

### Decision

The PoC will validate against documented historical events instead of showing only synthetic or random examples.

### Current candidates

Biological anomaly:

**Al Raha Beach / Al Raha Bay, Abu Dhabi — April 2023**

Oil:

**Kharg Island / Persian Gulf — May 2026**

### Why

A known event gives the judges a credible reference point.

### Consequence

The system must clearly distinguish:

- what an external report says happened,
- what the satellite-derived analysis shows.

---

## Decision 017 — Separate Validation AOI From Operational Demo Site

### Decision

The current Al Raha AOI is a validation AOI.

It must not be presented as a desalination intake.

### Why

Scientific validation and operational product demonstration serve different purposes.

### Consequence

A future operational demo AOI/intake zone should be represented separately and clearly labelled.

---

## Decision 018 — Use Analyst-Defined AOIs Transparently

### Decision

The current AOI polygon is an analyst-defined study area, not an official administrative or environmental boundary.

### Consequence

The code and product metadata must preserve this distinction.

---

## Decision 019 — Build Provenance Before Satellite Ingestion

### Decision

Provenance and lineage infrastructure was implemented before connecting to live EO catalogs.

### Why

Once real scenes begin flowing through the system, losing source identity would create technical debt and scientific credibility problems.

### Consequence

Every real EO observation and derived product should integrate with the existing provenance layer.

---

## Decision 020 — Preserve End-to-End Lineage

### Decision

Expected lineage:

Source observation
→ derived feature
→ hazard layer
→ risk product
→ operational alert

### Why

Judges and future customers should be able to trace a result back to its input data and processing version.

### Consequence

Derived data must not silently lose references to upstream sources.

---

## Decision 021 — Use Python 3.11 for the PoC

### Decision

The project uses Python 3.11.

Current environment:

`aquasentinel813`

### Why

Python 3.11 provides strong compatibility with the scientific/geospatial ecosystem required by the project.

The office machine also had newer Python versions, but the project environment was intentionally isolated.

### Consequence

Do not migrate the project to Python 3.13/3.14 during the PoC without a strong reason and explicit approval.

---

## Decision 022 — Use a `src/` Package Layout

### Decision

Application code lives under:

`src/aquasentinel`

### Why

This provides clean package isolation and reduces accidental imports from the project root.

### Consequence

New core modules should normally be added under this package.

---

## Decision 023 — Use TOML for Project Configuration

### Decision

Runtime/project defaults live in:

`config/default.toml`

### Current configurable items include

- AOI path,
- cache directory,
- date range,
- cloud-cover limit,
- risk bands,
- risk weights.

### Why

Operational/scientific parameters should not be buried in source code.

### Consequence

Avoid hard-coding configuration values when they belong in TOML.

---

## Decision 024 — Use GeoJSON for AOI Representation

### Decision

AOIs are stored in GeoJSON.

### Why

GeoJSON is:

- interoperable,
- human-readable,
- easy to map,
- compatible with future geospatial tooling.

### Consequence

Coordinate validation is part of the config/AOI layer.

---

## Decision 025 — Repository Is the Source of Truth

### Decision

Project state must live in GitHub/repository documentation, not in ChatGPT conversation memory.

### Why

The user may:

- change computers,
- start a new ChatGPT conversation,
- start a new Codex task,
- hit a context-window limit,
- involve another developer.

### Consequence

Important project state belongs in:

- `AGENTS.md`,
- `docs/PROJECT_STATE.md`,
- `docs/DECISIONS.md`,
- `docs/HANDOFF.md`,
- `.agent/PLANS.md`,
- code,
- tests,
- Git history.

---

## Decision 026 — Use a Cloud/GitHub-First Multi-Machine Workflow

### Decision

Office PC, personal PC, and Codex/cloud environments should all work from the same GitHub repository.

### Workflow

Before changing machine:

- test,
- lint,
- commit,
- push.

On the destination machine:

- pull,
- recreate/activate environment,
- install dependencies,
- test,
- continue.

### Consequence

Machine-specific state should be minimized.

---

## Decision 027 — Keep Personal GitHub Separate From Company GitHub

### Decision

The office machine uses a dedicated personal SSH alias:

`github.com-omar-personal`

Current personal repo remote:

`git@github.com-omar-personal:Omar-Aboulwafa/aquasentinel-813.git`

### Why

The machine is also connected to company systems.

### Consequence

Do not modify global Git identity or company SSH settings unless explicitly approved.

---

## Decision 028 — Use Feature Branches, Not Direct Development on `main`

### Decision

Each engineering task should use a task-specific branch.

Examples:

- `feature/as-101-sentinel2-stac`
- `feature/as-102-optical-preprocessing`
- `fix/...`
- `docs/...`
- `chore/...`

### Consequence

`main` should remain stable and merge-ready.

---

## Decision 029 — Require Tests and Ruff Before Merge

### Decision

Standard quality gate:

```text
python -m pytest -v
python -m ruff check .
```

### Consequence

Do not merge code with failing tests or lint issues.

---

## Decision 030 — Keep Dependencies Minimal

### Decision

Do not add libraries simply because they may be useful later.

### Before adding a dependency

Confirm:

1. the standard library is insufficient,
2. the dependency is needed for the current task,
3. it is mature and appropriate,
4. it does not unnecessarily duplicate another library.

### Consequence

AS-101 should add only what is required for robust STAC integration.

---

## Decision 031 — STAC Search Comes Before Image Download

### Decision

AS-101 will search/catalog Sentinel-2 observations first.

It will not yet download/process full imagery.

### Why

The correct order is:

catalog discovery
→ deterministic scene selection
→ provenance
→ retrieval
→ preprocessing

### Consequence

AS-101 acceptance criteria should focus on real scene discovery and metadata/provenance.

---

## Decision 032 — Streamlit Is the Preferred PoC UI Direction

### Decision

When the dashboard phase begins, Streamlit is the preferred first implementation unless project needs change.

### Why

It offers a fast route to:

- maps,
- controls,
- charts,
- evidence panels,
- Python-native integration.

### Consequence

Do not spend early PoC time building a complex frontend framework.

---

## Decision 033 — Live APIs Must Not Be the Only Demo Path

### Decision

The final demo should have cached/validated fallback data.

### Why

External EO and environmental services can fail, rate-limit, or require re-authentication.

### Consequence

A live API failure must not make the hackathon demo unusable.

---

## Decision 034 — P0 Reliability Beats P1 Sophistication

### Decision

When time is limited, protect:

1. real EO-derived results,
2. scientific credibility,
3. validation,
4. explainability,
5. provenance,
6. reproducibility,
7. working demo.

before protecting:

- advanced modelling,
- advanced UI,
- hyperspectral extras,
- complex drift simulation,
- visual polish.

### Consequence

P1 features may be cut without changing the core product thesis.

---

## Decision 035 — Codex Is Introduced Before AS-101

### Decision

Codex onboarding/continuity setup occurs before satellite-data engineering begins.

### Why

AS-101 is the point where implementation complexity and file count begin to increase materially.

### Consequence

Before delegating AS-101, the repository must contain enough context for Codex to work without relying on the current ChatGPT conversation.

---

## Decision 036 — First Codex Task Is Read-Only

### Decision

The first Codex task should inspect the repository and summarize its understanding without modifying code.

### Why

This validates that:

- `AGENTS.md` is effective,
- project state is understandable,
- important decisions are recoverable,
- agent assumptions can be corrected before code changes.

### Consequence

AS-101 should only be delegated after the read-only onboarding is reviewed.

---

## Decision 037 — Keep Decision History, Do Not Rewrite It Silently

### Decision

If a major project decision changes, update this file rather than deleting the old rationale without explanation.

### Preferred pattern

Add:

- changed decision,
- date,
- reason,
- impact.

### Why

Architecture history matters for understanding why the current system exists.

---

## Decision 038 — Use Configurable CDSE STAC for AS-101

### Decision

On 2 October 2026, the project owner explicitly selected Copernicus Data Space Ecosystem as the default Sentinel-2 Level-2A catalog for AS-101:

- Endpoint: `https://stac.dataspace.copernicus.eu/v1/`
- Collection: `sentinel-2-l2a`

Both are configurable. `pystac-client==0.9.0` is the only new direct dependency; it provides STAC discovery/search and pagination without introducing raster processing libraries.

### Evidence and consequences

- A real query for the configured Al Raha validation AOI and 1 March–31 May 2023 window returned 44 scenes with cloud cover <= 30%; every candidate converted to valid provenance.
- A configurable 30-second request timeout bounds network waits. No result cap is imposed; all pagination is consumed or an explicit error is raised.
- Missing required metadata fails explicitly. Platform is required because the existing `SourceRecord` requires it; platform values are never invented. Optional self URLs and licence metadata remain absent when unavailable.
- Candidate IDs include a full SHA-256 digest of the catalog endpoint plus escaped collection/item IDs to avoid provider and separator collisions.
- Only metadata and asset references are retrieved. Catalog availability is not evidence of HABs or usable water pixels, and asset accessibility has not been verified.

Reproduction and detailed evidence: `docs/AS_101_STAC_SEARCH.md`.

---

## Decision 039 — Preserve CDSE Discovery; Use Planetary Computer Raster Delivery

**Date:** 6 October 2026. **Status:** Explicitly authorized for AS-102.

### Decision

AS-101 remains the CDSE metadata workflow. AS-102 strictly matches its candidate to Planetary Computer and uses the anonymous STAC / credential-free HREF-signing / native COG path. Do not rewrite AS-101 or fall back to whole products.

### Why and consequence

FG-01 established bounded access where the prior CDSE environment probe was blocked. Match full acquisition timestamp, normalized platform, MGRS tile and relative orbit; reject zero/ambiguous/conflicting matches. Parse the structured CDSE ID when provider-specific fields are absent. PC `s2:mgrs_tile`, `s2:generation_time`, processing baseline and optional SAFE product identity are independently checked. Current PC and CDSE products have different baselines/generation dates; no pixel equivalence is asserted.

---

## Decision 040 — Attribute Pixels to the Actual PC Product

**Date:** 6 October 2026. **Status:** Explicitly authorized for AS-102.

### Decision

The actual PC raster product receives the existing provider-qualified STAC `SourceRecord` pattern. `ResolvedOpticalSource` retains observation/processing identity, unsigned assets, observed native grids/nodata and XML decoding. The preprocessed `DerivedProductRecord.source_ids` contains only this PC source; CDSE is retained as discovery/matching context in parameters.

### Why and consequence

Same acquisition is not the same processed product. Generic source/provenance models and AS-101 remain unchanged. Deterministic processing identity and JSON-only parameters preserve reproducibility without arrays or signing credentials.

---

## Decision 041 — Decode BOA Reflectance from the Delivered Product XML

**Date:** 6 October 2026. **Status:** Explicitly authorized for AS-102.

### Decision

Read bounded `product-metadata` XML and validate baseline, quantification, unique physicalBand/bandId mapping and every required additive offset. Decode `(DN + band_offset) / quantification`; mask source nodata before decoding, output float32, and retain negative/zero/unclipped values. Missing, malformed, duplicate, nonfinite or conflicting metadata fails explicitly.

### Why and consequence

Modern Sentinel-2 processing baselines make DN/10000 unsafe. The observed PC baseline-05.09 XML establishes quantification 10000 and offset -1000 for all nine required bands, including B8A; these values are parsed, not constants copied from CDSE. BOA reflectance is not automatically aquatic remote-sensing reflectance.

---

## Decision 042 — Use One Fixed 20 m Analysis Grid per AOI

**Date:** 6 October 2026. **Status:** Explicitly authorized for AS-102.

### Decision

Transform the configured WGS84 polygon envelope to a configured metric CRS, densify bounds, and snap outward to a stable 20 m lattice. The Al Raha default is EPSG:32640: bounds `[249020,2702860,255220,2707420]`, width 310, height 228, affine `[20,0,249020,0,-20,2707420]`. Polygon membership uses pixel centres.

### Why and consequence

Native 10/20 m bands and scenes from different UTM zones must share a single analysis grid. Read native assets with a bounded four-pixel halo; reflectance uses bilinear, SCL nearest. Bilinear downsampling is not an area average. Cross-CRS synthetic coverage includes EPSG:32639 → EPSG:32640; no per-tile target-grid fallback.

---

## Decision 043 — Conservative SCL and All-Band Water Support

**Date:** 6 October 2026. **Status:** Explicitly authorized for AS-102.

### Decision

Invalid classes are `{0,1,2,3,7,8,9,10,11}` plus unknowns; class 2 retains the provider meaning dark-area pixels. Classes 4/5 are valid non-water, class 6 candidate water. Export separate AOI, valid-data, water, valid-water and interpolation-support masks.

Map SCL to each native reflectance grid and remove invalid/nodata contributors before bilinear reprojection. Erode native water/nodata support by a 3×3 NumPy neighbourhood, bilinearly project the resulting binary support with zero treated as actual invalid support, and require a support value exactly 1 across all nine bands. Do not renormalize bad support away. Final water also requires AOI membership, valid target SCL and finite reflectance in every band.

### Why and consequence

Land/cloud/shadow/nodata interpolation must not manufacture usable water. The extra neighbourhood is deliberately conservative, particularly near shorelines. Report excluded counts and retention. Zero surviving water is valid; no silent mask relaxation. SCL is imperfect coastal/shallow/turbid-water truth, and separate cloud-probability assets remain outside AS-102 P0.

---

## Decision 044 — Add Only NumPy and Rasterio for AS-102

**Date:** 6 October 2026. **Status:** Explicitly authorized for AS-102.

### Decision

Add direct pins `numpy==2.2.6` and `rasterio==1.4.3`, compatible with Python 3.11; retain `pystac-client==0.9.0`. NumPy handles masks/arrays and Rasterio/GDAL handles bounded COG access, CRS transformation and resampling. Standard-library urllib/JSON/ElementTree handles signing and XML.

### Why and consequence

No SciPy, SDK, additional direct HTTP library or overlapping geospatial stack is needed. The validated environment resolves Python 3.11.16, NumPy 2.2.6, Rasterio 1.4.3 and bundled GDAL 3.9.3. Transitive wheel dependencies are not a new direct project stack. The earlier GDAL 3.10.3 access probe remains a separate historical environment/result.

---

## Decision 045 — Keep SAS Material Transient and Stable Cache Evidence Unsigned

**Date:** 6 October 2026. **Status:** Explicitly authorized for AS-102.

### Decision

Use the official configured HREF signing endpoint immediately before access. Permit only exact configured HTTPS asset hosts, validate the signed response points to the same object, reject cross-host metadata redirects, suppress/sanitize Rasterio diagnostics and exception chains, and never persist signed URLs/SAS/credentials. Stable JSON serialization rejects credentialled/query-bearing URLs.

### Why and consequence

Temporary access credentials must not become product identity or presentation evidence. Cache only AOI-sized arrays/masks under `data/cache/as102/<cache_id>/`, with deterministic identity, atomic directory publication, canonical manifest JSON and SHA-256 verification. Corrupt caches fail explicitly. Known-ID reload uses no catalog/signing/XML/raster work; it validates the configured AOI/grid and retains original processing lineage.

---

## Pending Decisions

The following decisions are intentionally not final yet:

### Full geospatial dependency stack

Packages such as:

- `rioxarray`,
- `xarray`,
- `geopandas`,
- `stackstac`

should be introduced only when their task requires them.

### Final operational demo site

A future desalination/intake demonstration location must be chosen from a defensible public source.

### Hyperspectral event/site

Depends on usable EnMAP/813 data availability.

### Final fitted ML model

Only select after determining label availability and baseline performance.

---

## Decision Review Rule

Before making a change that contradicts one of these decisions:

1. identify the affected decision,
2. explain why it should change,
3. evaluate impact on scope/deadline/scientific validity,
4. update this document if the change is approved.

The purpose of this file is to prevent accidental architectural drift and loss of project reasoning.
