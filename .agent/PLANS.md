# AquaSentinel 813 — Agent Execution Plans

**Purpose:** Define how Codex or any coding agent should plan, execute, validate, and report multi-step work in this repository.

This file is intentionally operational. It is not a product specification and does not replace:

- `AGENTS.md`
- `docs/PROJECT_STATE.md`
- `docs/DECISIONS.md`
- `docs/HANDOFF.md`
- `docs/AquaSentinel_813_PRD_v1.0.md`

---

## 1. When to Use a Plan

Use an explicit execution plan when a task:

- spans multiple files,
- adds or changes dependencies,
- introduces a new data source,
- changes architecture,
- changes scientific logic,
- requires multiple implementation stages,
- may take more than one focused coding pass,
- may need partial progress to be resumed later.

Examples:

- AS-101 — Sentinel-2 STAC Search
- AS-102 — Optical Preprocessing
- AS-201 — Sentinel-1 ingestion
- dashboard integration
- environmental context integration
- validation pipelines

For very small fixes, a full plan is optional.

---

## 2. Required Plan Structure

Before implementing a non-trivial task, produce a plan with these sections.

### Task

State the exact task ID and name.

Example:

`AS-101 — Sentinel-2 STAC Search`

### Goal

Describe the user-visible or system-level result in one or two sentences.

### Inputs

List required inputs such as:

- config values,
- AOI,
- date window,
- credentials,
- external catalog,
- existing modules.

### Outputs

List concrete outputs such as:

- Python module,
- data model,
- provenance record,
- test fixtures,
- documentation update.

### Files Likely to Change

List expected files before editing.

Example:

- `pyproject.toml`
- `src/aquasentinel/catalog/stac.py`
- `src/aquasentinel/ingestion/sentinel2.py`
- `tests/catalog/test_stac.py`
- `docs/PROJECT_STATE.md`

### Dependencies

List:

- new dependencies,
- why each is needed,
- whether the standard library is insufficient,
- version constraints if relevant.

Do not add dependencies without justification.

### Acceptance Criteria

Write objective completion criteria.

Each item must be testable.

### Scientific Guardrails

List any scientific or operational constraints relevant to the task.

### Risks

List likely technical, scientific, or delivery risks.

### Validation

State exactly how the task will be validated:

- tests,
- Ruff,
- live smoke test,
- fixture-based test,
- provenance check,
- manual inspection.

### Non-Goals

State what is explicitly excluded from the task.

This prevents scope creep.

---

## 3. Implementation Rules

During execution:

1. Read `AGENTS.md`.
2. Read `docs/PROJECT_STATE.md`.
3. Read relevant decisions.
4. Inspect current branch and `git status`.
5. Inspect existing code/tests.
6. Implement the smallest complete solution.
7. Add tests as implementation proceeds.
8. Keep provenance integration intact.
9. Do not hide errors behind broad exception handling.
10. Do not silently change scientific assumptions.
11. Do not introduce unrelated refactors.
12. Do not commit secrets or large EO files.

---

## 4. Progress Tracking

For a longer task, report progress using this format:

### Completed

- item
- item

### In Progress

- item

### Blocked

- item
- reason

### Remaining

- item
- item

### Validation So Far

- tests run
- lint status
- live checks

Do not claim completion while acceptance criteria remain unmet.

---

## 5. Required Completion Report

At the end of a task, report:

### What Changed

Summarize implementation.

### Files Changed

List files.

### Dependencies Added or Changed

List exact dependency changes.

### Tests Added or Updated

List test files and key cases.

### Validation Results

Include:

```text
python -m pytest -v
python -m ruff check .
```

and any additional live/data checks.

### Scientific / Operational Limitations

State what the implementation does not prove.

### Provenance Impact

Explain whether and how data lineage is preserved.

### Known Issues

List unresolved issues.

### Recommended Next Task

State the next milestone, but do not start it unless requested.

---

## 6. Stop-and-Ask Conditions

Stop and ask the project owner before proceeding if:

- a requirement conflicts with `DECISIONS.md`,
- a scientific claim would need to be weakened or strengthened materially,
- a new external provider becomes a hard dependency,
- a new paid service is required,
- credentials or private data are required,
- the proposed change affects P0 scope,
- the task requires changing Python major/minor version,
- the task requires changing the main product user or core decision,
- a validation event appears unsuitable or unsupported,
- the task risks missing the PoC deadline.

---

## 7. Quality Gate

Before considering a coding task complete, run:

```text
python -m pytest -v
python -m ruff check .
```

Also inspect:

```text
git status
git diff
```

For external-data tasks, also perform at least one real-data smoke test unless the task is explicitly fixture-only.

---

## 8. Branching Rule

Do not implement planned work directly on `main`.

Use a task-specific branch.

Examples:

- `feature/as-101-sentinel2-stac`
- `feature/as-102-optical-preprocessing`
- `feature/as-201-sentinel1-retrieval`
- `fix/stac-timeout-handling`

The branch should contain only work relevant to the task.

---

## 9. Data-Task Rule

For satellite/environmental integrations:

1. search metadata first,
2. validate item identity,
3. preserve provenance,
4. retrieve only what is required,
5. cache safely,
6. avoid committing raw large files,
7. separate external-source facts from derived conclusions.

---

## 10. Scientific Modelling Rule

Before introducing a fitted ML model:

1. define baseline,
2. define labels,
3. define leakage controls,
4. define validation split,
5. define evaluation metrics,
6. define explanation method,
7. document limitations.

If labels are weak or sparse, prefer a transparent anomaly model over an overfit classifier.

---

## 11. P0 Protection Rule

When schedule pressure exists, protect:

1. real EO-derived output,
2. scientific credibility,
3. validation,
4. explainability,
5. provenance,
6. reproducibility,
7. working demo.

Cut or delay:

- advanced ML,
- hyperspectral extras,
- complex drift modelling,
- nonessential exports,
- visual polish,

before weakening P0.

---

## 12. AS-101 Plan Template

Use the following structure when AS-101 begins.

### Task

AS-101 — Sentinel-2 STAC Search

### Goal

Given the configured AOI, date range, and cloud-cover limit, return real Sentinel-2 observations suitable for downstream water analysis and convert them into AquaSentinel provenance records.

### Likely Inputs

- `config/default.toml`
- `data/aoi/demo_site.geojson`
- runtime context
- selected STAC endpoint

### Likely Outputs

- STAC catalog client module
- Sentinel-2 search service
- deterministic result model
- provenance mapping
- tests
- project-state update

### Non-Goals

- full image download
- atmospheric correction
- spectral indices
- HAB detection
- ML risk model
- dashboard

### Acceptance Criteria

- search uses configured AOI
- search uses configured date range
- search applies cloud-cover filtering
- results are deterministic and typed
- each returned scene can produce a `SourceRecord`
- invalid/missing metadata is handled explicitly
- tests pass
- Ruff passes
- at least one real-data smoke test succeeds
- no raw imagery is committed

### Expected Validation

```text
python -m pytest -v
python -m ruff check .
```

Plus a real Sentinel-2 catalog query against the chosen STAC provider.

---

## 13. Continuity Rule

If an agent or session stops mid-task:

1. do not rely on memory,
2. preserve progress in Git where safe,
3. update `docs/PROJECT_STATE.md` if meaningful state changed,
4. document blockers,
5. leave the branch in a recoverable state,
6. record the next exact step.

The next agent should be able to resume from repository evidence.

---

## 14. Final Planning Principle

A good plan should reduce uncertainty before code is changed.

The agent should never use planning as an excuse to over-design the system.

Plan only enough to:

- protect scope,
- protect scientific credibility,
- preserve provenance,
- make implementation testable,
- make handoff reliable.
