# AquaSentinel 813 — Architecture & Product Decisions

## Current AS-105 M29 status — 10 October 2026 (Asia/Dubai)

**M28: COMPLETE / COMMITTED / PUSHED**, implementation `57100b2e53e941f3a7fdfdfc40b61d2b4043c0e5`,
branch `feature/as-105-hab-anomaly-geometry`, remote
`origin/feature/as-105-hab-anomaly-geometry`, base main `4e322df220f8cab2805fccf9a2b32dd825f29218`.
**M29 / E29 / EV-033: REAL ENGINEERING ACCEPTANCE PASS; OWNER REVIEW PASS.**
Decision 050 remains unchanged; M29 is an execution/evidence checkpoint, not
Decision 051. The accepted AS-104 handoff was the only real input; no network,
upstream reprocessing or AS-102 cache loading, and no policy tuning.

Foundation/continuity complete → AS-101/102/103 merged → Decisions 048/049 merged → AS-104 COMPLETE AND MERGED → AS-105 M28 COMPLETE / COMMITTED / PUSHED → AS-105 M29 REAL ENGINEERING ACCEPTANCE PASS → owner review of M29 documentation/publication followed by PR preparation → AS-105 FEATURE NOT YET PR-MERGED → AS-106+ NOT STARTED; P1 05.10 NOT STARTED.

Target valid water **7,963**; policy-evaluable support P **802** (**10.071581%**
coverage diagnostic); candidates **7**, fraction **7/802 = 0.872818%** of P.
**Projected-grid candidate area: 2,800 m² / 0.0028 km².** One eight-connected
region, one MultiPolygon with three four-connected pieces; F2/F4 agreement.
P is not full AOI/ocean/risk coverage, and its coverage is not candidate fraction.
Sparse-history support remains material; no masks were relaxed.

Frozen real product: `hab_geometry:70876fbcb25e8a37abaa238a59e1da32fec9066792e6239db68e284b7bd18682`.
First extraction **2026-10-10T05:45:15.046037+00:00–05:45:15.173566+00:00** /
**09:45:15.046037–09:45:15.173566 +04:00 Asia/Dubai**;
acceptance completed **05:45:46.711968 UTC / 09:45:46.711968 +04:00**.
Execution/acceptance precede owner review and this later documentation publication;
no PR or merge timestamp exists. **PR NOT CREATED; FEATURE NOT YET MERGED.**

Independent masks/families/P/C, components, area and polygon round-trip PASS;
repeat **27/27 arrays**, parent immutability **61/61**, bundle read-back PASS.
M29 gates: **140 focused / 803 full tests PASS**, Ruff/diff PASS;
only six existing Rasterio PendingDeprecationWarnings. These are local checks,
not GitHub CI or scientific accuracy. External local evidence bundle:
`/workspace/aquasentinel-acceptance/as105/m29/`, **NOT tracked in Git**.

M29 establishes reproducible real candidate spectral anomaly geometry only. It does NOT establish confirmed HAB/bloom, chlorophyll concentration, species/toxins, biological causation, sensitivity/specificity/accuracy/false-positive rate, event agreement, persistence, risk/confidence, water safety, intake exposure, alert or warning lead time. No comparison with the historical April event was performed. Rank is not probability/confidence/significance/severity; policy families are not statistically independent. Five observations are not statistical sufficiency.
Future comparative policy validation: **REQUIRED / NOT RUN**, including
predeclared history-depth sensitivity; AS-106+ and P1 05.10 **NOT STARTED**.
Immediate next step: **owner review of M29 documentation/publication followed by
PR preparation**; no PR creation or merge in this task. All earlier M01–M28,
E01–E28, EV-001–EV-032 and Decisions 001–050 remain historical and preserved.
The old M28 status below describes its earlier checkpoint, not current status.
See [AS-105 contract](AS_105_HAB_ANOMALY_GEOMETRY.md) and [M29 validation](evidence/AS_105_HAB_ANOMALY_GEOMETRY_VALIDATION.md#m29--real-geometry-engineering-acceptance--10-october-2026).

## Historical AS-105 M28 status — before M29, 10 October 2026 (Asia/Dubai)

Owner-authorized **offline implementation only**; Decision 050 / M28 / E28 / EV-032.
**PASS — OWNER-REVIEWED / FEATURE PUBLICATION AUTHORIZED** on
`feature/as-105-hab-anomaly-geometry`, isolated worktree
`/workspace/aquasentinel-813-as105`, verified base
`4e322df220f8cab2805fccf9a2b32dd825f29218`.
Foundation/continuity complete → AS-101/102/103 merged → Decisions 048/049 merged
→ AS-104 COMPLETE AND MERGED → AS-105 frozen-policy offline implementation PASS
→ owner rank-granularity clarification accepted → feature publication
→ PR code review next after publication verification.

140 synthetic geometry cases PASS; full **803 passed**, Ruff/diff/whitespace
PASS; only six existing Rasterio warnings. No upstream algorithms, tests,
configuration, dependencies, provenance schema or cache format changed.
All 55 mandated adversarial requirements and controls A–E pass; this is
engineering evidence, not HAB accuracy. Rank is not probability/confidence/
significance/severity and evidence families are not independent measurements.

Real AS-105 geometry acceptance: **NOT RUN**; real counts/fraction/area/regions
remain **UNKNOWN**. Its future checkpoint is reserved and has **not been created**.
Future predeclared comparative policy validation: **REQUIRED / NOT RUN**;
AS-106+ and P1 homogeneous 05.10: **NOT STARTED**.
The owner authorized feature commit/push on 10 October 2026 after the final
quality/preservation gates. This record accompanies that feature publication;
verify the exact Git SHA/remote before PR review. **PR NOT CREATED; NOT MERGED.**
Real acceptance and future studies remain separately gated. The verified external
AS-104 handoff, twelve accepted cache hashes, both safety stashes and recovery
artifacts remain intact; the handoff is read-only and not tracked.

Earlier dated checkpoint status statements below retain their historical
meaning, including earlier AS-105 non-authorization and absence of Decision 050.
This M28 block governs current status; M01–M27/E01–E27/EV-001–EV-031 stay intact.

Owner-review clarification (same M28/Decision 050): with five histories,
no-tie empirical ranks are 0.0/0.2/0.4/0.6/0.8/1.0; the frozen 0.90 screen
requires all five below, or four below plus one exact tie. It is not a population
90th-percentile estimator or significance. Four synthetic regression cases pass.
Future predeclared history-depth sensitivity is required where valid EO permits;
choose exact depths before running it. M29 retains the accepted minimum-five
parent. No real geometry execution or new checkpoint.

See [AS-105 contract](AS_105_HAB_ANOMALY_GEOMETRY.md) and [M28 validation](evidence/AS_105_HAB_ANOMALY_GEOMETRY_VALIDATION.md).

**Historical AS-104 closeout status — 9 October 2026 (Asia/Dubai), M27/E27/EV-031:**
**AS-104: COMPLETE AND MERGED** through [PR #12](https://github.com/Omar-Aboulwafa/aquasentinel-813/pull/12).
**AS-104 implementation merge commit:** `472edc737847dc8581290a372c5da28f71fc48f0`.
Feature implementation commit: `09b38bd9c312470e948b1f17165ec5335cfc149d`.
Publication documentation commit / final PR head: `703af1176aeaf9ba38d31c53648907c3b1792aec`.
Merged **2026-10-09T09:26:08Z** / **2026-10-09T13:26:08+04:00 Asia/Dubai**.
Real acceptance **PASS**; no unresolved AS-104 P0 blocker. Known scientific and
coverage limitations remain documented. Current active development branch: **none**;
AS-104 development is closed. This closeout was prepared on `docs/as-104-closeout`.
Next step: owner review of the next milestone/AS-105 design before implementation;
separate authorization is required. AS-105+ and P1 homogeneous 05.10 **NOT STARTED**.
M23–M26/E23–E26/EV-027–EV-030 retain their dated historical blocker, fix, acceptance
and publication states, including then-pending PR/merge language. M27/E27/EV-031
records the later merge/closeout; it is an execution/history event, not Decision 050.
Both safety stashes and external recovery artifacts are retained historical recovery
material. No EO experiment rerun or source/test/math/cache changes in this closeout.
See [merge/closeout evidence §9](evidence/AS_104_TEMPORAL_BASELINE_VALIDATION.md#9-pr-12-merge-and-as-104-closeout--9-october-2026).

**Historical AS-104 publication status — before PR #12 merge, 9 October 2026 (Asia/Dubai), M26/E26/EV-030:**
Implementation and real acceptance **PASS**; feature commit
`09b38bd9c312470e948b1f17165ec5335cfc149d` is **COMMITTED AND PUSHED**,
parent/base `2006df7a70a4f48c66933aed96f4464d8d03084e`.
Branch `feature/as-104-temporal-baseline`; remote/upstream
`origin/feature/as-104-temporal-baseline`. Feature publication verified equal
local/remote SHA and a **clean worktree**. This reconciliation is documentation only.
**PR NOT YET CREATED; merge NOT YET PERFORMED.** Review the published commit and
open a PR if review passes and creation is authorized; this task creates no PR.
M23/E23/EV-027 remains historically BLOCKED; M24–M25/E24–E25/EV-028–EV-029 remain
acceptance-time PASS. Their earlier stop states below are historical, not current
Git status. M26/E26/EV-030 separates later publication from acceptance completion.
No Decision 050; both stashes/recovery artifacts retained; AS-105+ and P1 05.10
**NOT STARTED**. No science, source/tests, caches or experiment timestamps changed.
Exact publication metadata/times and unchanged acceptance evidence are in
[validation §8](evidence/AS_104_TEMPORAL_BASELINE_VALIDATION.md#8-as-104-feature-publication--9-october-2026).

The original planning/dated execution records below retain their then-current
stop-state instructions unchanged. Their uncommitted/no-push language is historical.

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

## Decision 046 — AS-103 Candidate Spectral Features with Signed BOA and Parent Lineage

**Date:** 8 October 2026 (Asia/Dubai). **Status:** Explicitly authorized for AS-103;
implemented on uncommitted feature branch for review.

### Decision

Freeze exactly ndci_like, mci_like, B05/B04, B06/B04, B03/B04 and B03/B02 in the
canonical order defined by the AS-103 contract. Candidate signals only; no event
threshold/classification or temporal baseline. Preserve authoritative AS-102
valid-water support and signed BOA. Float64 arithmetic returns float32; numerical
rejection is inclusive `abs(d) <= max(1e-4,1e-6*(|a|+|b|))`; nonfinite intermediate
or float32 results are masked NaN. Record per-feature diagnostics and finite
JSON-safe summaries, including unclipped NDCI-like out-of-range counts.

Use nominal MCI B04/B05/B06 at 665/705/740 nm with k=1.0 (not SNAP's 1.005),
coefficient 8/15, metadata-declared convention rather than provider XML wavelengths.
BOA is not aquatic Rrs. NDCI-like and B05/red ratio share an evidence family and
must not later be treated as independent biological evidence.

### Why and consequence

Pure NumPy feature extraction from verified AS-102 output is cheap and explainable;
no new dependency, configuration, disk cache, retrieval, signing or resampling is
needed. The AS-103 identity includes canonical formulas/policies/grid/parent and a
versioned fingerprint of the full mask plus five consumed bands on water support,
because frozen dataclasses do not make NumPy arrays immutable. Creation time and
feature summaries do not define identity. Registry lineage is actual PC source →
AS-102 derived product → AS-103 derived product; no raw-source shortcut or generic
schema change. AS-104 remains separately unauthorized and not started.

Contract/references: [AS-103 plan/API](AS_103_SPECTRAL_FEATURES.md).
Observed acceptance: [AS-103 evidence](evidence/AS_103_SPECTRAL_FEATURES_VALIDATION.md).

---

## Decision 047 — AS-104 Causal Per-Pixel Temporal Feature Baselines

**Date:** 8 October 2026 (Asia/Dubai).
**Status:** Explicitly authorized for AS-104.

### Decision

AS-104 is a causal, target-specific, per-feature, per-pixel temporal comparison
over validated AS-103 SpectralFeatureScene objects. For one target observation,
use explicitly bounded strictly-prior observations only. No target self-inclusion.
No future observations. No symmetric before/after baseline in as104-v1.

For every feature/pixel:

- historical centre = median
- MAD = median(abs(history - median))
- scale = 1.4826 * MAD
- signed deviation = target - centre
- standardized anomaly = deviation / scale when scale > 0
- empirical rank uses exact-tie midrank

Minimum history is an explicit API parameter. For P0 real acceptance use
`minimum_observations = 5`. Five is a P0 engineering/scientific starting rule,
not a claim of statistical sufficiency.

Zero MAD:

- centre remains valid
- scale = 0 remains valid
- signed deviation remains valid
- empirical rank remains valid
- standardized anomaly is invalid / NaN
- no epsilon
- no fallback scale estimator
- no clipping

AS-104 never combines features. Preserve feature-family metadata, including the
shared `red_edge_b5_vs_red` family for `ndci_like` and `red_edge_red_ratio`.
These must not later be interpreted as independent biological evidence.

AS-104 outputs are temporal spectral anomalies, candidate feature deviations,
observational anomalies and baseline-relative signals. They are NOT HAB detections,
bloom detections, calibrated chlorophyll, species/toxin evidence, water-safety
evidence, intake exposure, persistence, risk score, alert level, monitoring
recommendation or warning lead-time proof.

### Frozen owner modifications and implementation contract

Use semantic `as104-input-v1` fingerprints. Target: full valid-water mask, all six
feature masks, supported feature values. Selected references: feature validity
restricted to target feature support and values only on the target/reference
support intersection. Exclude reference pixels outside target support, invalid
NaN payloads, future and out-of-period scenes. Use length-delimited canonical
headers, C-order masks and little-endian float32 payloads. Copy relevant inputs;
no concurrent-copy guarantee. Selected parent IDs/times remain in identity and
provenance even when a parent contributes no valid values. Do not implement
`precision_limited_scale_count` or any float32-epsilon pseudo noise floor.

Primary API: `compute_temporal_anomaly(scenes, *, target_product_id,
reference_start, reference_end=None, minimum_observations, registry)`.
Use start <= reference acquisition < effective end <= target acquisition;
normalize UTC, default effective end to target time, sort selected references by
acquisition then product ID. Reject duplicate products/times/observations,
malformed inputs, incompatible selected grids/feature/processing contracts and
unresolved/inconsistent upstream lineage. P0 uses the same tile, relative orbit
and delivered PC processing baseline; Sentinel-2A/B may coexist. Generation
times differ and are recorded. Minimum is an integer 3 through uint32 maximum;
booleans are rejected and there is no hidden default. Sparse/empty support is a
valid empty result, not an exception.

Float64 arithmetic, centre, scale and deviation; float32 standardized anomaly and
rank; uint32 counts, zero outside target feature support; boolean masks, all
subsets of target feature support. Positive scale is used directly; mask nonfinite
or non-representable float32 standardized results. Exact rank is
`(count(history < target) + 0.5*count(history == target))/n`, range [0,1], same
minimum; rank is not probability, p-value, confidence or severity. No interpolation,
trend fitting, seasonality correction, pooling, winsorization or outlier deletion.

Identity `temporal:<SHA-256(canonical identity)>`, version `as104-v1`, includes
selected parents/times, semantic fingerprints, grid, feature/family/compatibility
contracts, effective bounds, minimum, numerical/support/statistics/dtype policies
and Python/NumPy versions. Creation time and calculated summaries are excluded.
Immediate provenance parents are target AS-103 first, then chronological selected
references: PC -> AS-102 -> AS-103 -> AS-104. Registry is read-only during
computation; caller may register the result afterward. No generic schema change,
new dependency, config field or disk cache.

### Validation and scope

Pass offline independent arithmetic, support, numerical, causality, semantic
identity, model corruption, exact multi-parent lineage and blocked-IO tests before
real work. Predeclare April 28 target, March 1–April 1 UTC reference period and
minimum 5. Use unchanged AS-101/102/103 and ignored AS-102 caches; record actual
support and blockers without widening dates, lowering minimum, relaxing masks,
mixing processing or selecting by anomalies. Preserve all historical evidence.

No AS-105/106/107/108, ML, environmental/oil context, exposure, risk/alerts,
recommendations or dashboard. Positive is not dangerous; negative is not safe;
BOA is not aquatic Rrs. Acquisition-causal retrospective comparison does not
establish historical operational availability or warning lead time. Contract:
[AS-104 plan/API](AS_104_TEMPORAL_BASELINE.md).

---

## Decision 048 — Explicit Planetary Computer Processing-Baseline Selection

**Date:** 8 October 2026 (Asia/Dubai).
**Status:** Explicitly authorized.

### Decision

AS-102 may optionally receive an explicitly required Planetary Computer
processing baseline when resolving a known Sentinel-2 observation.

Resolution order is:

1. Validate each returned Planetary Computer item's existing structured
   metadata and processing metadata.
2. Identify items matching the expected observation exactly by acquisition
   timestamp, platform, MGRS tile and relative orbit.
3. If no required processing baseline is supplied, preserve the existing
   behavior exactly: require exactly one observation match.
4. If a required processing baseline IS supplied, filter the exact observation
   matches by that baseline.
5. Require EXACTLY ONE remaining product.
6. Zero remaining products: explicit failure.
7. More than one remaining product: explicit failure.

There is NO earliest-generation fallback, latest-generation fallback, implicit
preference for CDSE generation, automatic baseline preference or mixed-baseline
fallback. The constraint is explicit and caller-controlled.

The actual selected Planetary Computer product remains authoritative for pixels.
The selected actual PC source ID, processing baseline, generation time, provider
metadata and unsigned asset references remain recorded through the existing
AS-102 identity/provenance. The separate CDSE discovery product remains
discovery/matching context.

The required-baseline selector itself is a SOURCE-RESOLUTION CONSTRAINT, not a
new pixel-processing identity dimension. Therefore, if the same actual PC product
is selected, product/cache identity remains the existing identity of that actual
product. Do not create a second cache identity merely because the caller supplied
the selector explicitly. Do not change cache schema or rewrite old cache manifests.

However, all cache-return paths MUST enforce a supplied constraint: a cached
AS-102 scene must not be returned when its recorded `pc_processing_baseline`
conflicts with `required_processing_baseline`.

This extends Decision 039. It does not change reflectance decoding, grid
construction, masks, resampling, actual-source provenance, AS-103 or AS-104
algorithms.

### Cross-worktree coordination and evidence

At base `c6accab2c5753734466a6375d1b3ce1762e99bed`, merged main ends at Decision
046. Decision 047 remains only in the separately authorized, uncommitted AS-104
worktree on `feature/as-104-temporal-baseline`; it is deliberately not copied or
renumbered here, as explicitly instructed by the owner. Decision 048 keeps its
assigned number. M19 / E18–E19 / EV-022–EV-023 are reserved for that preserved
work; this separate fix uses M20 / E20 / EV-024.

AS-104 exposed the two-product ambiguity before reference XML/raster access.
Metadata investigation found one complete 05.09 product for each of the five
frozen March observations. The fix is a source-resolution extension only, left
uncommitted for review. AS-104 remains uncommitted and its real acceptance BLOCKED
until this upstream fix is reviewed/merged and acceptance is separately rerun.
See [fix plan/API](AS_102_REQUIRED_PC_BASELINE_FIX.md) and
[validation evidence](evidence/AS_102_REQUIRED_PC_BASELINE_FIX_VALIDATION.md).

### Post-merge integration checkpoint — 9 October 2026 (Asia/Dubai)

PR #10 merged the source-selection fix at
`39f2aee90c727fc151886efbdea44daec0e3f9b4` (feature fix
`c9a415b65a101319e9c9f2fef21ad0dcd44c9347`). Decision 047 and 048 now coexist
in order; the preceding cross-worktree/pending-review text is the original
8 October fix checkpoint, preserved verbatim. AS-104 source/tests were restored
byte-identically and the combined gate passed 533 tests, Ruff/diff checks and
six existing warnings. Frozen 05.09 real acceptance was resumed but stopped at
March 4 signing (HTTP 504 observed), not observation ambiguity. No selector,
processing/cache identity, numerical rule or scientific decision changed.
See M21/E21/EV-025 and the separately dated AS-104 validation evidence.

---

## Decision 049 — Reusable Planetary Computer Account/Container SAS Token Transport

**Date:** 9 October 2026 (Asia/Dubai)
**Status:** Explicitly authorized.

AquaSentinel shall replace repeated per-asset Planetary Computer `/sign`
authentication for supported Azure Blob assets with transient reusable
SAS tokens scoped to the validated Planetary Computer storage
account/container.

The actual stable unsigned asset HREF remains authoritative for:

- source metadata
- provenance
- processing identity
- cache identity
- cache manifests
- reproducibility records

SAS tokens and signed URLs are TRANSPORT-ONLY ephemeral credentials.

They MUST NEVER be written into:

- provenance
- product identity
- processing parameters
- cache manifests
- repository files
- logs
- exception messages
- evidence documents

The public `sign_asset(href, settings)` behavior remains:

unsigned stable HREF in
→ transient signed HREF out

The caller must not need to know whether authorization used a cached or
newly acquired token.

No AS-102 caller API change is required.

### Cross-worktree coordination and implementation boundary

Decision 048 was merged via PR #10 at
`39f2aee90c727fc151886efbdea44daec0e3f9b4`. Resumed AS-104 then encountered
intermittent per-asset authentication HTTP 504s; Decision 049 follows that failure.
Decision 047/M19/E18–E19/EV-022–EV-023 and M21/E21/EV-025 remain only in the
preserved, uncommitted AS-104 worktree; their bodies are not copied or renumbered.
This separate fix uses M22/E22/EV-026. Decision 048/M20/E20/EV-024 retain their
historical meanings.

Use the configured HTTPS issuer, official account/container token route and
actual `token` / `msft:expiry` response schema. Refresh at remaining lifetime
<=60 seconds. Token acquisition alone permits at most five attempts with
0.8/1.6/3.2/6.4-second backoffs for HTTP 429/500/502/503/504 or typed transient
connection/timeouts. No subscription key, SDK, dependency/config change, caller
change, pixel-processing change, provenance change or cache-schema change.
AS-104 real acceptance remains blocked pending fix review/merge.
See [plan](AS_102_REUSABLE_PC_SAS_TOKEN_FIX.md) and
[validation](evidence/AS_102_REUSABLE_PC_SAS_TOKEN_FIX_VALIDATION.md).

---

## Decision 050 — AS-105 Predeclared Family-Aware Candidate Anomaly Geometry

**Date:** 9 October 2026 (Asia/Dubai).
**Status:** Owner-approved v1 scientific policy; M28 offline engineering review
PASS and five-history clarification accepted 10 October 2026. Feature publication
authorized; PR code review is next after publication verification. Real geometry acceptance and comparative
policy validation are separately gated and NOT RUN.

**Decision:** Freeze `as105-v1` as a predeclared P0 screening heuristic on a
validated AS-104 parent, not a fitted/validated HAB classifier. For each feature,
use rank-valid support and evidence `deviation > 0 AND rank >= float32(0.90)`.
Record nominal 0.90, actual 0.8999999761581421 and threshold bits `3f666666`.
No robust-z gate or summary, epsilon, clipping, fallback or imputation.

**Owner-review clarification — 10 October 2026 (Asia/Dubai):** Nominal 0.90 and
the frozen float32 comparison remain unchanged. This is a predeclared
empirical-rank screening threshold whose effective granularity depends on the
available historical sample count, not a statistically estimated population
90th percentile, significance, probability, confidence or severity.
AS-104's exact-tie midrank is
`(count(history < target) + 0.5 * count(history == target)) / n`.
For the accepted five-history parent, no-tie ranks are spaced by 0.2:
0.0, 0.2, 0.4, 0.6, 0.8, 1.0. Thus the unchanged threshold requires the
target to exceed all five values in a no-tie pixel. Rank 0.90 is attained only
with four values below and one exact tie; three below and two ties yields 0.80.
These decimal ranks are stored as float32 before the frozen comparison.
This is an upper-tail screening rule, not a smooth percentile estimator.
Five observations are not statistical sufficiency; future comparative validation
remains required. M29 must use the already accepted parent with minimum five;
no AS-104 math, minimum or accepted evidence is changed.

F1 `red_edge_b5_vs_red` = ndci_like + red_edge_red_ratio;
F2 `red_edge_line_height` = mci_like;
F3 `red_edge_b6_vs_red` = red_edge2_red_ratio;
F4 `visible_green_vs_red` = green_red_ratio;
F5 `visible_green_vs_blue` = green_blue_ratio.
OR member evidence gives at most one family vote. Candidates require at least
two families and a vote from F1/F2/F3. Policy support independently requires at
least two available families and available F1/F2/F3, using OR of member rank
support. Fraction uses that support denominator, not AOI/water/all-six intersection.

Use deterministic row-major int32 eight-connected components with no morphology
or size filter. Polygonize four-connected pieces, group by label, preserve exact
pixel edges and canonical winding/start/holes/parts. Geometry stays in projected
AnalysisGrid CRS; exact raster round-trip is mandatory. Area derives from affine
determinant on supported north-up square projected metre grids, not hardcoded 400.

**Options considered:** rank + direction, z + direction or combined evidence;
feature counting versus family counting; alternate thresholds/family minima;
red-edge requirement; four/eight connectivity; region filtering. Owner freezes
one explainable policy now and requires a later bounded comparative study,
without tuning against the accepted April 28 observation. F1 grouping avoids
counting two related B05/red signals twice; distinct policy families do not imply
statistical independence or proof of biological causation.

**Integrity/lineage:** pure one-parent API; defensive array copies; canonical
consumed-mask/deviation/rank fingerprint, separate complete output fingerprint,
full policy/software/grid identity and parent-aware regeneration. Existing
DerivedProductRecord references exactly the AS-104 product, preserving actual
PC → AS-102 → AS-103 → AS-104 → AS-105 without schema/cache/dependency changes.
Rehashed alternate policy is invalid under v1.

**Scientific limits:** candidate spectral anomaly geometry only. Rank is not
probability, confidence, significance or severity. No HAB/bloom confirmation,
chlorophyll, species, toxins, water safety, intake risk, persistence, confidence,
alert or lead time. BOA is not aquatic reflectance. Roughly 10% five-history
support and the absence of statistical sufficiency from five observations remain
explicit; large z from small scales is not a geometry vote.

**Required future validation — NOT RUN:** bounded predeclared comparisons of
rank + direction, z + direction and combined rank/z; rank 0.80/0.90/0.95;
family minimum 1/2/3; red-edge required/optional; connectivity 4/8; no filtering
versus separately labelled region-filter sensitivity. Add **history-depth
sensitivity** where valid EO availability permits: predeclare support around
five, moderately deeper and substantially deeper histories. Select exact depths
from valid EO availability before running the study, to assess dependence on
coarse five-history rank resolution. Do not run it now or change the accepted
AS-104 parent/minimum for M29. April 28 cannot be both
tuning data and the sole proof of superiority. This task authorizes neither
that study nor real geometry acceptance, persistence/risk/alerting or P1 05.10.

**Evidence:** [contract/plan](AS_105_HAB_ANOMALY_GEOMETRY.md),
[offline validation](evidence/AS_105_HAB_ANOMALY_GEOMETRY_VALIDATION.md),
M28/E28/EV-032; 140 geometry and 803 full tests PASS with six existing warnings.

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

## Historical AS-104 Execution Note — Case Representation and Cached Acceptance

9 October 2026 (Asia/Dubai): the owner-authorized M24/E24/EV-028 bug fix changes
one AS-104 provenance consistency equality to `.casefold()` comparison only.
It introduces no aliases, stored platform normalization or identity rewrite;
all other validation and Decision 047's scientific contract remain unchanged.
No Decision 050 is created. Decisions 047–049 and historical M23/E23/EV-027
remain preserved. M25/E25/EV-029 records the frozen cached 05.09 real acceptance
PASS, with minimum five, sparse support, scalar/causal/repeat verification and
unchanged AS-102/AS-103 identity. See the AS-104 validation §§6–7 for evidence.
These are execution checkpoints, not a new architectural/scientific decision.
AS-104 remains uncommitted for review; no AS-105+ or P1 05.10 study.

## Historical AS-104 Publication Execution Note — M26 / E26 / EV-030 (before PR #12 merge)

AS-104 feature commit `09b38bd9c312470e948b1f17165ec5335cfc149d` is committed
and pushed on the existing feature branch from parent `2006df7a70a4f48c66933aed96f4464d8d03084e`.
This publishes the already accepted implementation/evidence; it is not a new
scientific/architectural decision and does not create Decision 050. Current
publication status supersedes the earlier execution stop state above, while
Decisions 047–049 and M23–M25 remain historically intact. PR not yet created;
not merged. Review published commit next; no AS-105+ or P1 05.10 study.

## AS-104 Merge/Closeout Execution Note — M27 / E27 / EV-031

AS-104 is COMPLETE AND MERGED via PR #12 at `472edc737847dc8581290a372c5da28f71fc48f0`,
merged **2026-10-09T13:26:08+04:00 Asia/Dubai** / **2026-10-09T09:26:08Z**.
The two reviewed commits are implementation `09b38bd9c312470e948b1f17165ec5335cfc149d` and publication
documentation/final feature head `703af1176aeaf9ba38d31c53648907c3b1792aec`. Real acceptance PASS;
accepted math, identities, measurements and scientific guardrails are unchanged.
M23–M26 and Decisions 001–049 remain historical records. This is an execution/
history event under the existing decisions, not a new Decision 050.
No unresolved AS-104 P0 blocker; known coverage/scientific limits remain. Owner
review of the next milestone/AS-105 design before implementation requires separate
authorization. Both stashes/recovery artifacts retained; no EO rerun, new merge,
AS-105+ or P1 homogeneous-05.10 experiment.
