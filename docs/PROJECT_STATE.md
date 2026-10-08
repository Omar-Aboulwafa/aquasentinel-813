# AquaSentinel 813 — Project State

**Last updated:** 6 October 2026 (Asia/Dubai)
**Repository:** `Omar-Aboulwafa/aquasentinel-813`
**Default branch:** `main`
**Current development branch:** `feature/as-102-optical-preprocessing` (uncommitted implementation for review).
**Latest approved base:** `0867708ea62676dcbcd0f5f83577cc120d633f26` (`origin/main`, merged PR #5).
**PoC deadline:** 11 October 2026
**Challenge:** Arab Youth Space Hackathon 2026 — Track 03: Water Security & Marine Environments

---

## 1. Current Status

AquaSentinel 813 is at the following stage:

**Foundation complete → continuity complete → Codex development handoff complete → AS-101 complete and merged → AS-102 implemented and validated on its feature branch (uncommitted, unpushed, not merged) → AS-103 next planned, NOT authorized and NOT started.**

Completed engineering foundations:

- AS-001 — Repository Scaffold.
- AS-002 — Configuration & AOI Model.
- AS-003 — Provenance Model.

Continuity setup and Codex read-only onboarding are complete:

- AS-000C.1 — `AGENTS.md` completed and merged into `main`.
- AS-000C.2 — `docs/PROJECT_STATE.md` completed and merged into `main`.
- AS-000C.3–AS-000C.6 — PRD, decisions, handoff, and execution-plan documentation completed and merged into `main`.
- AS-000C.7 — Codex read-only onboarding **COMPLETED** on 2 October 2026 at `779069d`.
- AS-000C.8 — Codex development handoff **COMPLETED** with explicit AS-101 implementation authorization on 2 October 2026.

Completed AS-101 implementation and next milestone:

- AS-101 — Sentinel-2 STAC Search: completed on `feature/as-101-sentinel2-stac`, based on `origin/main` at `51f4ede`. Implementation is committed at `41a0b0b217cace909c906b7aedcb9cc6d0026f53` and documentation at `b3f0e9f878375f5fbfccb35519eeac5cc8fa48af`. AS-101, including the approved review fixes, is merged into `main` via [PR #2](https://github.com/Omar-Aboulwafa/aquasentinel-813/pull/2) at merge commit `1b83a732155ee01c01b7d33cb50115725cfb08c3`.
- Quality gate: **97 tests passed**, Ruff passed, and `git diff --check` passed.
- Real CDSE query returned **44 scenes** for the configured Al Raha AOI, 1 March–31 May 2023, cloud cover <= 30%; all converted to valid provenance records.
- AS-102 was explicitly authorized on 6 October 2026 and is implemented/validated on `feature/as-102-optical-preprocessing`, based on merged PR #5 / `0867708ea62676dcbcd0f5f83577cc120d633f26`. Changes remain uncommitted, unpushed and unmerged; no PR was created. AS-103 is next planned but NOT authorized and NOT started. See §23 and `docs/AS_102_OPTICAL_PREPROCESSING.md`.

---

## 2. Product Definition

### Working product name

**AquaSentinel 813**

### Product vision

AquaSentinel 813 is an explainable, multi-hazard marine-intake intelligence system that combines Earth observation and environmental context to identify marine hazards offshore, assess their relevance to monitored desalination intake zones, and prioritize earlier field verification.

### Core principle

> AquaSentinel watches the sea before a threat reaches the intake.

### Primary user

Desalination Plant Water Quality / Operations Manager.

### Primary operational decision

> Where and when should monitoring or field verification be prioritized?

### PoC hazard scope

**Primary hazard:**
- HAB / biological water-quality anomaly.

**Secondary hazard:**
- Oil-slick / marine surface-pollution candidate.

### Product logic

Observation
→ Detection
→ Explanation
→ Exposure
→ Risk
→ Monitoring Priority
→ Human Decision

---

## 3. Scientific Guardrails

The product must avoid overclaiming what satellite observations prove.

Preferred language:

- HAB-like spectral anomaly.
- Elevated biological water-quality risk.
- Oil-slick candidate.
- Observational risk.
- Monitoring priority.
- Field verification recommended.
- Confidence.

The product must not claim that satellite data alone has:

- confirmed toxic algae,
- confirmed algal toxins,
- confirmed petroleum composition,
- certified water as safe or unsafe,
- justified autonomous desalination-plant shutdown.

Remote sensing supports earlier operational awareness and prioritization. Field and laboratory verification remain necessary.

---

## 4. Sensor Strategy

### Sentinel-2

Primary use:

- water colour,
- chlorophyll-related signals,
- red-edge features,
- biological/spectral anomaly detection,
- temporal comparison.

### Sentinel-1 SAR

Primary use:

- marine surface-slick candidates,
- oil-related surface anomalies,
- cloud-independent observation.

### EnMAP / future hyperspectral data

Primary use:

- detailed spectral characterization,
- confidence enhancement,
- multispectral-vs-hyperspectral comparison.

Hyperspectral data is a P1 enhancement, not a P0 dependency.

### Supporting environmental data

Potential P1 context:

- sea-surface temperature,
- currents,
- ERA5 wind,
- historical environmental conditions.

---

## 5. Current Technical Baseline

### Runtime

- Python: `3.11.17`
- Conda environment: `aquasentinel813`
- Project directory on office PC: `D:\aquasentinel-813`

### Development tools

- pytest
- Ruff
- Git
- GitHub
- VS Code

### Package layout

Python package:

`src/aquasentinel`

### Configuration

Main config:

`config/default.toml`

Current configuration includes:

- app metadata,
- AOI path,
- cache path,
- analysis date window,
- maximum cloud cover,
- risk bands,
- HAB PoC weights,
- oil PoC weights.

The current risk weights are PoC hypotheses, not validated scientific constants.

### AOI

Current validation GeoJSON:

`data/aoi/demo_site.geojson`

Current validation AOI:

- Al Raha Bay / Al Raha Beach validation area.
- Analyst-defined polygon.
- Includes a public geographic reference point.
- Does not represent a desalination intake.
- Must not be presented as an official environmental or administrative boundary.

---

## 6. AS-001 — Repository Scaffold — COMPLETE

Implemented:

- Git repository initialized.
- Default branch is `main`.
- Personal Git identity configured locally for the repository.
- Personal GitHub SSH alias configured separately from company access.
- GitHub personal repository created:
  - `Omar-Aboulwafa/aquasentinel-813`
- Python 3.11 Conda environment created.
- Editable package installation works.
- `pyproject.toml` created.
- `.gitignore` created.
- `.env.example` created.
- README created.
- Initial package created.
- Initial smoke test created.
- pytest and Ruff configured.

Initial foundation commit:

`f878acc chore: scaffold AquaSentinel 813 project`

---

## 7. AS-002 — Configuration & AOI Model — COMPLETE

Implemented modules:

- `src/aquasentinel/config/models.py`
- `src/aquasentinel/config/loader.py`
- `src/aquasentinel/config/aoi.py`
- `src/aquasentinel/config/__init__.py`
- `src/aquasentinel/runtime.py`

Implemented capabilities:

- TOML config loading.
- Analysis-date validation.
- Cloud-cover validation.
- Risk-band validation.
- Risk-weight normalization validation.
- AOI file-path validation.
- GeoJSON FeatureCollection loading.
- Point validation.
- Polygon validation.
- Longitude/latitude range validation.
- Polygon closure validation.
- Duplicate feature-ID rejection.
- Role lookup.
- Runtime context combining config and AOI.

Current demo AOI:

`data/aoi/demo_site.geojson`

AS-002 feature commit:

`f606ac5 feat: add configuration and AOI runtime model`

AS-002 merge commit:

`113ca44 merge: complete AS-002 configuration and AOI model`

---

## 8. AS-003 — Provenance Model — COMPLETE

Implemented package:

`src/aquasentinel/provenance/`

Implemented modules:

- `models.py`
- `serialization.py`
- `registry.py`
- `persistence.py`
- `__init__.py`

Implemented capabilities:

### Source records

Tracks:

- source ID,
- platform,
- source product ID,
- acquisition timestamp,
- catalog,
- collection,
- source URL when available,
- licence when available.

### Derived product records

Tracks:

- derived product ID,
- product type,
- creation timestamp,
- processing version,
- upstream source IDs,
- processing parameters.

### Validation

Implemented:

- non-empty identifiers,
- timezone-aware timestamps,
- source-reference requirements,
- duplicate-ID protection,
- JSON-serializable processing-parameter validation.

### Serialization

Implemented:

- source record → dictionary,
- derived record → dictionary,
- dictionary → source record,
- dictionary → derived record,
- JSON writing,
- UTC timestamp normalization,
- provenance schema version.

Current provenance schema version:

`1.0`

### Provenance registry

Implemented:

- add source,
- add derived product,
- reject duplicate records,
- reject unknown upstream references,
- retrieve source,
- retrieve derived product,
- recursively resolve lineage.

Expected lineage:

Source observation
→ derived feature
→ hazard layer
→ risk product
→ operational alert

### Registry persistence

Implemented:

- save full provenance registry to JSON manifest,
- restore registry from manifest,
- resolve multi-step derived dependencies while loading.

AS-003 feature commit:

`e2baedc feat: add provenance tracking and lineage registry`

AS-003 merge commit:

`db79260 merge: complete AS-003 provenance model`

`db79260` is the known `main` state immediately before Codex/continuity setup began.

---

## 9. Current Test / Quality Status

Current AS-102 branch quality baseline: **213 tests passed**, Ruff passed, and `git diff --check` passed. See §23 for the live acceptance and cache evidence. This is separate from the historical baselines below.

At the completion of AS-003:

- pytest: **17 passed**
- Ruff: **All checks passed**
- `main` working tree: clean
- `main` synchronized with `origin/main`

Standard quality gate:

```text
python -m pytest -v
python -m ruff check .
```

These commands must continue to pass before merge.

---

## 10. Git / Account Setup

This office computer is also used with company systems.

The AquaSentinel repository must use the user's personal GitHub account without changing company Git configuration.

Personal GitHub account:

`Omar-Aboulwafa`

Personal repository SSH remote pattern:

`git@github.com-omar-personal:Omar-Aboulwafa/aquasentinel-813.git`

Current `origin` should remain:

`git@github.com-omar-personal:Omar-Aboulwafa/aquasentinel-813.git`

Personal SSH alias:

`github.com-omar-personal`

Do not modify machine-global Git identity or the company's GitHub configuration without explicit approval.

---

## 11. Multi-Machine Strategy

The project must be usable from:

- office PC,
- personal PC,
- Codex/cloud environments.

The repository is the source of truth.

### Before switching machines

Run:

1. tests,
2. Ruff,
3. commit,
4. push.

### On the other machine

Run:

1. pull/fetch,
2. activate or recreate the Python 3.11 environment,
3. install the project and development dependencies,
4. run tests,
5. continue from a task-specific branch.

Do not use Git to transfer:

- `.env`,
- passwords,
- tokens,
- SSH private keys,
- machine-specific secrets.

---

## 12. Codex / Continuity Strategy

Reason for AS-000C:

The project must not depend on one ChatGPT conversation or one agent context window.

Repository documentation must allow a new ChatGPT session, Codex task, another computer, or another developer to recover current project state.

### Required continuity files

- `AGENTS.md`
- `docs/PROJECT_STATE.md`
- `docs/DECISIONS.md`
- `docs/HANDOFF.md`
- `.agent/PLANS.md`

All required continuity files are committed and merged into `main`.

### Agent startup sequence

A new coding agent should:

1. Read `AGENTS.md`.
2. Read `docs/PROJECT_STATE.md`.
3. Read relevant decision/architecture documentation.
4. Inspect the current branch.
5. Run `git status`.
6. Inspect relevant tests/code.
7. Run the current test suite before making meaningful changes when practical.

Do not rely on chat memory for critical project decisions.

---

## 13. AS-000C — Codex & Continuity Setup — COMPLETE

### AS-000C.1 — AGENTS.md

Status:

**Completed and merged into `main`.**

Purpose:

- repository-level coding-agent instructions,
- scope protection,
- scientific guardrails,
- Git rules,
- dependency rules,
- testing rules,
- agent workflow.

### AS-000C.2 — PROJECT_STATE.md

Status:

**Completed and merged into `main`.**

### AS-000C.3 — PRD / scope reference

Status:

**Completed and merged into `main`.**

The approved AquaSentinel PRD is available at `docs/AquaSentinel_813_PRD_v1.0.md`.

### AS-000C.4 — DECISIONS.md

Status:

**Completed and merged into `main`.**

Must capture major decisions and reasons, including:

- why Track 03,
- why multi-hazard vision,
- why HAB is the primary PoC hazard,
- why oil is secondary,
- why Sentinel-2 for biological anomaly,
- why Sentinel-1 for oil,
- why hyperspectral is P1,
- why satellite outputs remain observational,
- why Python 3.11,
- why provenance was built before data ingestion,
- why the repo is the source of truth.

### AS-000C.5 — HANDOFF.md

Status:

**Completed and merged into `main`.**

Must enable a fresh human or agent to continue with minimal context.

### AS-000C.6 — `.agent/PLANS.md`

Status:

**Completed and merged into `main`.**

Defines how longer Codex tasks should be planned and reported.

### AS-000C.7 — Codex read-only onboarding

Status:

**COMPLETED.**

Completed on 2 October 2026 at `779069d`. Codex inspected the repository documentation, architecture, configuration/AOI, provenance, and tests, and returned a structured onboarding report without modifying repository files. Repository understanding has been verified.

### AS-000C.8 — Codex development handoff

Status:

**COMPLETED.**

AS-101 was explicitly authorized on 2 October 2026 as the first development task after onboarding. The handoff specified CDSE as the default provider, catalog-only scope, minimal dependencies, provenance integration, offline tests, a real-data smoke test, and initial review before committing. Onboarding alone did not authorize implementation; the separate development instruction did.

---

## 14. AS-101 — Sentinel-2 STAC Search — COMPLETE AND MERGED

### Name

**AS-101 — Sentinel-2 STAC Search**

### Goal

Given:

- configured AOI,
- configured date window,
- configured cloud-cover limit,

return real Sentinel-2 observations suitable for downstream water analysis.

### Initial task scope

AS-101 should focus on:

- selecting a stable STAC catalog/endpoint,
- catalog search,
- AOI intersection,
- time-range filtering,
- cloud-cover filtering,
- deterministic result representation,
- conversion of returned observations into AquaSentinel provenance records,
- tests.

### Explicit non-goals for AS-101

Do not yet:

- download full Sentinel-2 imagery,
- implement atmospheric correction,
- compute HAB indices,
- build the dashboard,
- build the ML risk model.

Search/catalog integration comes first.

### Implementation and validation

- Configurable CDSE STAC endpoint, collection, and per-request timeout.
- Primary validation Polygon passed as `intersects`; inclusive UTC date window and `eo:cloud_cover <= threshold` query.
- Full pagination without a result cap; explicit errors for incomplete/cyclic pagination, catalog failures, and missing/malformed item metadata.
- Typed metadata candidates sorted by acquisition time and item ID; identical duplicates collapsed and conflicting duplicates rejected.
- Provider-qualified `SourceRecord` mapping; upstream provenance models remain unchanged.
- Only new direct dependency: `pystac-client==0.9.0`.
- **97 tests passed**, including all 17 original tests; Ruff and `git diff --check` passed.
- Live CDSE smoke test on 2 October 2026 returned **44 scenes**, from `2023-03-04T06:47:51.024Z` through `2023-05-28T06:46:29.024Z`; provenance conversion succeeded for every scene.

Implementation and smoke-test details: `docs/AS_101_STAC_SEARCH.md`.

AS-101 is complete and merged into `main` via PR #2 at merge commit `1b83a732155ee01c01b7d33cb50115725cfb08c3`. No raster imagery was downloaded, and catalog availability does not demonstrate HAB detection or usable water pixels. AS-102 is now independently authorized and validated on its uncommitted feature branch; see §23.

---

## 15. Planned Milestones After AS-101

Expected sequence:

- AS-101 — Sentinel-2 STAC Search (complete and merged via PR #2).
- AS-102 — Optical Preprocessing (implemented/validated on feature branch; not merged).
- AS-103 — Spectral Feature Extraction (next planned; unauthorized, not started).
- AS-104 — Temporal Baseline.
- AS-105 — HAB Anomaly Geometry.
- AS-106 — Persistence.
- AS-107 — HAB Risk & Confidence.
- AS-108 — HAB Historical Validation.

Then oil pipeline work:

- AS-201 — Sentinel-1 retrieval.
- AS-202 — SAR preprocessing.
- AS-203 — Low-backscatter candidate detection.
- AS-204 — Candidate filtering.
- AS-205 — Temporal/reference comparison.
- AS-206 — Oil risk & confidence.
- AS-207 — Historical oil validation.

P1 environmental/hyperspectral work should not block P0.

---

## 16. Validation Strategy

### HAB validation

Primary candidate:

**Al Raha Beach / Al Raha Bay, Abu Dhabi — April 2023**

Target analysis:

- pre-event,
- event,
- post-event/recovery.

Questions:

- was there a meaningful satellite-observable anomaly,
- which features changed,
- did the anomaly persist,
- could an earlier monitoring signal have been raised?

### Oil validation

Primary candidate:

**Kharg Island / Persian Gulf — May 2026**

Target analysis:

- Sentinel-1 slick-like anomaly,
- multi-date persistence/change,
- optical/context support when available,
- exposure demonstration.

Historical event reports and EO-derived observations must remain clearly distinguished.

---

## 17. PoC Scope Protection

P0 must be protected.

If schedule pressure increases, simplify or remove P1 work before weakening:

1. real EO-derived results,
2. scientific credibility,
3. validation,
4. explainability,
5. provenance,
6. reproducibility,
7. working demo.

Possible P1 cuts include:

- advanced drift simulation,
- hyperspectral integration,
- fitted ML classifier,
- advanced exports,
- visual polish.

---

## 18. Known Risks

### Technical

- cloud cover may prevent optical validation on ideal dates,
- Sentinel-1 oil detection has natural/low-wind look-alikes,
- hyperspectral scenes may not coincide with historical events,
- public external services may require credentials or become temporarily unavailable.

### Scientific

- water-colour anomaly is not equivalent to toxic HAB confirmation,
- low SAR backscatter is not equivalent to confirmed petroleum,
- risk weights remain PoC hypotheses until properly validated,
- limited labelled Gulf data may make anomaly detection preferable to overfit classification.

### Delivery

- deadline is close,
- scope expansion is a major risk,
- live API dependence during demo is risky.

Mitigation:

- maintain cached validated demo assets,
- preserve provenance,
- keep P0 independent of P1 external data where possible,
- record limitations explicitly.

---

## 19. Important Repository Rules

Never commit:

- `.env`,
- API credentials,
- SSH private keys,
- passwords,
- proprietary company credentials,
- large raw EO scenes,
- runtime caches.

Use:

- `.env.example`,
- STAC/product references,
- provenance manifests,
- reproducible scripts,
- small fixtures.

All meaningful code changes require tests where appropriate.

---

## 20. How to Resume the Project in a Fresh Session

Use the following recovery procedure:

1. Open the repository.
2. Read `AGENTS.md`.
3. Read this file.
4. Run:
   - `git status`
   - `git branch --show-current`
   - `git log --oneline --graph --decorate -8`
5. Activate the `aquasentinel813` Python 3.11 environment.
6. Run:
   - `python -m pytest -v`
   - `python -m ruff check .`
7. Read `docs/DECISIONS.md` and `docs/HANDOFF.md` when available.
8. Continue the next incomplete task listed in this document.

Do not reconstruct important project state from memory when repository evidence exists.

---

## 21. Immediate Next Action

AS-102 was explicitly authorized on 6 October 2026 and is implemented/validated on `feature/as-102-optical-preprocessing`, based on merged PR #5 / `0867708ea62676dcbcd0f5f83577cc120d633f26`. Changes remain uncommitted, unpushed and unmerged; no PR was created. AS-103 is next planned but NOT authorized and NOT started.

Immediate sequence:

1. Review the uncommitted AS-102 implementation, tests, Decisions 039–045 and EV-016/EV-017 evidence.
2. Preserve the passing quality gates, signed-material exclusion and ignored AOI cache. Commit/push/PR work requires explicit authorization.
3. AS-103 remains a separate future authorization; do not start feature extraction or hazard analysis.

---

## 22. Definition of Current Success

At the current point, the project is healthy if:

- `main` remains clean and synchronized,
- the test suite passes,
- Ruff passes,
- continuity documentation is committed,
- a new session/agent can understand the project without chat history,
- AS-101 is complete and merged into `main` via PR #2, with passing offline checks and a successful real catalog smoke test,
- AS-102 meets its authorized implementation acceptance on the isolated feature branch; its changes are explicitly uncommitted/unmerged and AS-103 has not started.


## 23. AS-102 — Optical Preprocessing Implementation Acceptance

AS-102 was explicitly authorized on 6 October 2026 and is implemented/validated on `feature/as-102-optical-preprocessing`, based on merged PR #5 / `0867708ea62676dcbcd0f5f83577cc120d633f26`. Changes remain uncommitted, unpushed and unmerged; no PR was created. AS-103 is next planned but NOT authorized and NOT started.

- CDSE discovery is preserved; Planetary Computer supplies the actual raster product, with strict time/platform/tile/orbit matching and independent product provenance.
- Nine native reflectance bands plus SCL and product XML; XML-driven offsets/quantification, bounded COG reads, fixed 20 m EPSG:32640 AOI grid (310 × 228), bilinear reflectance/nearest SCL, and all-band conservative interpolation/water support.
- Fresh real acceptance began `2026-10-06T10:07:14.660936+00:00` / `2026-10-06T14:07:14.660936+04:00` Asia/Dubai. CDSE returned 44 candidates; known April 28 observation matched PC baseline 05.09 separately from CDSE 05.10.
- AOI 67,449 pixels; valid data 65,166; candidate water 10,211; retained valid water 7,963; AOI water fraction 0.11805957093507688 (11.805957%); water retention 0.7798452649103907 (77.984526%). Excluded candidate water: 2,248. These are mask outcomes, not confirmed water/HAB or aquatic suitability.
- AOI cache/checksum reload is equivalent and uses no network/signing/raster work when the cache ID is known. Runtime cache material remains ignored.
- Current quality baseline: **213 tests passed** (all prior 97 retained), Ruff passed, `git diff --check` passed. Python 3.11.16 / NumPy 2.2.6 / Rasterio 1.4.3 / GDAL 3.9.3 in this cloud run. Two transitive Affine deprecation warnings are reported, with no failures.
- Decisions 039–045 record the newly authorized contract. EV-016/EV-017 and journal M15 record real implementation evidence; historical EV-014 PENDING and later FG-01 PASS/READY plus EV-015 remain preserved.
- L2A BOA reflectance is not aquatic Rrs; coastal/turbid/mixed-water SCL errors remain. No indices, chlorophyll, HAB/toxin/water-safety/intake-risk or lead-time conclusions were computed.

Plan/API/limits: `docs/AS_102_OPTICAL_PREPROCESSING.md`. Real evidence: `docs/evidence/AS_102_OPTICAL_PREPROCESSING_VALIDATION.md`. No source cache, raw scene or signing credentials belong in Git.
