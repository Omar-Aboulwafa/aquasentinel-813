# AquaSentinel 813 — Project State

**Last updated:** 2 October 2026
**Repository:** `Omar-Aboulwafa/aquasentinel-813`
**Default branch:** `main`
**Current branch:** `main`
**PoC deadline:** 11 October 2026
**Challenge:** Arab Youth Space Hackathon 2026 — Track 03: Water Security & Marine Environments

---

## 1. Current Status

AquaSentinel 813 is at the following stage:

**Foundation complete → continuity setup complete → Codex onboarding complete → AS-101 Sentinel-2 STAC Search is next.**

Completed engineering foundations:

- AS-001 — Repository Scaffold.
- AS-002 — Configuration & AOI Model.
- AS-003 — Provenance Model.

Continuity setup and Codex read-only onboarding are complete:

- AS-000C.1 — `AGENTS.md` completed and merged into `main`.
- AS-000C.2 — `docs/PROJECT_STATE.md` completed and merged into `main`.
- AS-000C.3–AS-000C.6 — PRD, decisions, handoff, and execution-plan documentation completed and merged into `main`.
- AS-000C.7 — Codex read-only onboarding **COMPLETED** on 2 October 2026 at `779069d`.
- AS-000C.8 — Codex development handoff **PENDING** until AS-101 implementation is explicitly authorized.

Next satellite engineering milestone, pending explicit implementation authorization:

- AS-101 — Sentinel-2 STAC Search.

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

## 13. AS-000C — Continuity & Onboarding COMPLETE; Development Handoff PENDING

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

**PENDING.**

AS-101 will be the first planned engineering task delegated to Codex. The development handoff remains pending until AS-101 implementation is explicitly authorized; completed onboarding does not authorize implementation.

---

## 14. Next Engineering Milestone — AS-101

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

---

## 15. Planned Milestones After AS-101

Expected sequence:

- AS-101 — Sentinel-2 STAC Search.
- AS-102 — Optical Preprocessing.
- AS-103 — Spectral Feature Extraction.
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

Continuity setup and Codex read-only onboarding are complete. AS-101 — Sentinel-2 STAC Search is the next engineering milestone.

Immediate sequence:

1. Obtain explicit authorization for AS-101 implementation; AS-000C.8 remains pending until then.
2. Once authorized, hand off AS-101 with explicit acceptance criteria, minimal dependencies, provenance integration, and test expectations.
3. Begin AS-101 on a dedicated feature branch and follow the existing quality gate.

---

## 22. Definition of Current Success

At the current point, the project is healthy if:

- `main` remains clean and synchronized,
- the test suite passes,
- Ruff passes,
- continuity documentation is committed,
- a new session/agent can understand the project without chat history,
- AS-101 can begin without revisiting completed foundation work.
