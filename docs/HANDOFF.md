# AquaSentinel 813 — Handoff Guide

**Last updated:** 2 October 2026
**Repository:** `Omar-Aboulwafa/aquasentinel-813`
**Default branch:** `main`
**Current continuity branch:** `chore/as-000c-codex-continuity`

This file is the fast handoff document for a new ChatGPT session, Codex task, developer, or second machine.

---

## 1. What This Project Is

AquaSentinel 813 is an explainable, multi-hazard marine-intake intelligence system being developed for the Arab Youth Space Hackathon 2026 — Track 03: Water Security & Marine Environments.

Core product principle:

> AquaSentinel watches the sea before a threat reaches the intake.

Primary user:

> Desalination Plant Water Quality / Operations Manager.

Primary operational decision:

> Where and when should monitoring or field verification be prioritized?

The PoC currently focuses on:

- HAB / biological water anomaly as the primary hazard.
- Oil-slick candidate detection as the secondary hazard.

The product is decision support, not autonomous plant control.

---

## 2. Read These Files First

A new agent or developer should read these in order:

1. `AGENTS.md`
2. `docs/PROJECT_STATE.md`
3. `docs/DECISIONS.md`
4. `docs/AquaSentinel_813_PRD_v1.0.md`
5. `.agent/PLANS.md` when available

These files together contain the project scope, scientific guardrails, architecture, completed work, and next steps.

---

## 3. Current Engineering State

Completed:

- AS-001 — Repository Scaffold.
- AS-002 — Configuration & AOI Model.
- AS-003 — Provenance Model.

Current continuity work:

- AS-000C.1 — `AGENTS.md` completed locally.
- AS-000C.2 — `PROJECT_STATE.md` added locally.
- AS-000C.3 — PRD moved into `docs/`.
- AS-000C.4 — `DECISIONS.md` added locally.
- AS-000C.4B — this `HANDOFF.md`.
- AS-000C.5 — `.agent/PLANS.md` still pending.
- AS-000C.7 — Codex read-only onboarding still pending.
- AS-000C.8 — AS-101 delegation still pending.

Next engineering milestone after continuity setup:

- AS-101 — Sentinel-2 STAC Search.

---

## 4. Known Good Git State Before Continuity Setup

Known `main` merge commit before AS-000C work:

`db79260 merge: complete AS-003 provenance model`

Known feature commit for AS-003:

`e2baedc feat: add provenance tracking and lineage registry`

Known AS-002 merge commit:

`113ca44 merge: complete AS-002 configuration and AOI model`

Known AS-001 initial commit:

`f878acc chore: scaffold AquaSentinel 813 project`

Do not assume these remain the latest commits after this handoff file is merged. Always inspect Git.

---

## 5. Required Startup Checks

When resuming the project, run:

```text
git branch --show-current
git status
git log --oneline --graph --decorate -8
```

Then activate the Python environment:

```text
conda activate aquasentinel813
```

Then run:

```text
python --version
python -m pytest -v
python -m ruff check .
```

Expected Python major/minor:

`3.11`

At the completion of AS-003, the known test baseline was:

`17 passed`

and Ruff reported:

`All checks passed!`

A higher test count later is normal.

---

## 6. Office-PC Setup

Current office-PC project path:

`D:\aquasentinel-813`

Current Conda environment:

`aquasentinel813`

Personal GitHub account:

`Omar-Aboulwafa`

Personal GitHub SSH alias:

`github.com-omar-personal`

Expected origin:

`git@github.com-omar-personal:Omar-Aboulwafa/aquasentinel-813.git`

This machine also has company Git/GitHub usage.

Do not alter global Git identity or company SSH settings unless explicitly requested.

---

## 7. Personal-PC Setup Strategy

On the personal machine, use the same personal GitHub repository.

Recommended sequence:

1. Configure personal GitHub authentication.
2. Clone the repository.
3. Create a Python 3.11 environment.
4. Install the project:

```text
python -m pip install -e ".[dev]"
```

5. Run:

```text
python -m pytest -v
python -m ruff check .
```

6. Continue from a task-specific branch.

Do not manually copy code folders between machines when Git can synchronize them.

---

## 8. Multi-Machine Working Rule

Before leaving one machine:

1. run tests,
2. run Ruff,
3. inspect `git status`,
4. commit meaningful work,
5. push.

On the next machine:

1. fetch/pull,
2. activate/recreate the environment,
3. install updated dependencies if needed,
4. run tests,
5. continue.

Do not move secrets through Git.

---

## 9. Scientific Guardrails

Preferred wording:

- HAB-like spectral anomaly.
- Elevated biological water-quality risk.
- Oil-slick candidate.
- Observational risk.
- Confidence.
- Field verification recommended.
- Monitoring priority.

Do not claim that satellite observations alone have:

- confirmed toxic algae,
- confirmed algal toxins,
- confirmed petroleum composition,
- certified water as safe or unsafe,
- justified autonomous plant shutdown.

The system supports earlier awareness and human verification.

---

## 10. Current Sensor Strategy

### Sentinel-2

Primary P0 source for:

- water colour,
- chlorophyll-related signals,
- red-edge features,
- biological/spectral anomaly detection,
- temporal monitoring.

### Sentinel-1 SAR

Primary P0 source for:

- surface-slick candidates,
- oil-related surface anomalies,
- cloud-independent marine observation.

### EnMAP / future hyperspectral data

P1 enhancement for:

- detailed spectral characterization,
- confidence enhancement,
- multispectral-vs-hyperspectral comparison.

Hyperspectral is not a P0 dependency.

---

## 11. Current Validation Strategy

### HAB / biological anomaly

Primary candidate:

**Al Raha Beach / Al Raha Bay, Abu Dhabi — April 2023**

Current validation AOI:

`data/aoi/demo_site.geojson`

Important:

- the AOI polygon is analyst-defined,
- it is not an official boundary,
- it is not a desalination intake.

### Oil

Primary candidate:

**Kharg Island / Persian Gulf — May 2026**

Historical reports and EO-derived evidence must remain clearly separated.

---

## 12. Current Architecture

Core reasoning chain:

Observation
→ Detection
→ Explanation
→ Exposure
→ Risk
→ Monitoring Priority
→ Human Decision

Existing implemented foundations:

### Configuration and AOI

`src/aquasentinel/config/`

Includes:

- configuration models,
- TOML loading,
- AOI GeoJSON loading,
- validation,
- runtime context.

### Provenance

`src/aquasentinel/provenance/`

Includes:

- source records,
- derived product records,
- JSON serialization,
- registry,
- lineage tracking,
- persistence.

Expected lineage:

Source observation
→ derived feature
→ hazard layer
→ risk product
→ operational alert

---

## 13. Configuration

Current default config:

`config/default.toml`

Current configuration includes:

- application metadata,
- AOI path,
- cache path,
- analysis date window,
- maximum cloud cover,
- risk bands,
- HAB PoC weights,
- oil PoC weights.

Risk weights are PoC hypotheses, not validated scientific constants.

---

## 14. What Not to Do

Do not:

- begin major refactors unrelated to the active task,
- develop directly on `main` unless explicitly approved,
- introduce large dependency stacks preemptively,
- commit `.env`,
- commit SSH keys,
- commit credentials,
- commit raw large EO scenes,
- claim confirmed toxic algae from satellite evidence,
- claim confirmed oil from a low-backscatter SAR feature alone,
- make hyperspectral data a hard dependency,
- average unrelated hazards into one scientific score,
- bypass provenance for convenience.

---

## 15. Immediate Next Engineering Task

After continuity setup and Codex onboarding:

### AS-101 — Sentinel-2 STAC Search

Goal:

Given:

- configured AOI,
- configured date window,
- configured cloud-cover threshold,

return real Sentinel-2 observations suitable for downstream analysis.

Expected AS-101 scope:

- select stable STAC endpoint/provider,
- search by AOI,
- search by date interval,
- filter by cloud cover,
- deterministic result representation,
- map results into AquaSentinel provenance records,
- add tests.

Do not yet:

- download full imagery,
- run atmospheric correction,
- compute HAB indices,
- build ML risk models,
- build the dashboard.

---

## 16. First Codex Task

The first Codex task should be read-only.

Suggested prompt:

```text
Read AGENTS.md, docs/PROJECT_STATE.md, docs/DECISIONS.md, docs/HANDOFF.md, and docs/AquaSentinel_813_PRD_v1.0.md.

Then inspect the repository structure, current Git branch/status, pyproject.toml, existing tests, config/AOI implementation, runtime context, and provenance implementation.

Do not modify any file.

Return:
1. your understanding of the product,
2. completed engineering milestones,
3. current architecture,
4. scientific guardrails,
5. current test/quality expectations,
6. what AS-101 should accomplish,
7. likely files/modules AS-101 should add or modify,
8. dependencies you think AS-101 actually needs,
9. any ambiguity, risk, or contradiction you detect.

Do not implement AS-101 yet.
```

Review Codex's understanding before allowing code changes.

---

## 17. AS-101 Codex Handoff Rule

Only after the read-only onboarding is accepted should Codex implement AS-101.

The AS-101 task should include:

- explicit acceptance criteria,
- a dedicated feature branch,
- test expectations,
- provenance integration,
- minimal dependencies,
- no full imagery processing.

Codex should report:

- files changed,
- dependency changes,
- tests added,
- test results,
- Ruff results,
- limitations,
- next recommended task.

---

## 18. Definition of a Healthy Handoff

A new agent/developer should be able to answer, without chat history:

- What is AquaSentinel?
- Who is the primary user?
- What decision does it support?
- Which hazards are P0?
- Which sensors serve which hazards?
- What scientific claims are prohibited?
- What has already been implemented?
- What is the known-good quality baseline?
- What is the next task?
- What must not be changed casually?

If those answers are unclear, repository documentation is incomplete.

---

## 19. Recovery From Context Loss

If a ChatGPT/Codex context window is lost:

1. reopen the repository,
2. read `AGENTS.md`,
3. read `docs/PROJECT_STATE.md`,
4. read `docs/DECISIONS.md`,
5. read this file,
6. inspect Git history,
7. run tests/Ruff,
8. continue from the next incomplete task.

Do not recreate prior decisions from memory when repository documentation exists.

---

## 20. Human Owner Checkpoint

Before a major scope or architecture change, ask the project owner when the change affects:

- primary product positioning,
- hazard scope,
- scientific interpretation,
- validation strategy,
- dependency architecture,
- deadline-critical P0 functionality,
- external service/provider commitment,
- model claims,
- operational recommendations.

Small implementation details inside approved acceptance criteria do not require constant re-approval.

---

## 21. Final Handoff Summary

Current project phase:

**Foundation complete → continuity setup → Codex onboarding → Sentinel-2 integration**

Immediate priority:

**Finish repository continuity, validate Codex understanding, then begin AS-101.**

Core constraint:

**Protect scientific credibility and P0 delivery before sophistication.**
