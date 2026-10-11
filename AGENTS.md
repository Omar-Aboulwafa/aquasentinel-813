# AquaSentinel 813 — Agent Instructions

## Mission

AquaSentinel 813 is an explainable multi-hazard marine-intake intelligence system for the Arab Youth Space Hackathon 2026.

Core principle:

> AquaSentinel watches the sea before a threat reaches the intake.

Primary user:

> Desalination Plant Water Quality / Operations Manager.

Primary decision:

> Where and when should monitoring or field verification be prioritized?

---

## PoC Scope

### P0 — Must work

- Sentinel-2 HAB / biological-water-anomaly pipeline.
- Sentinel-1 oil-slick candidate pipeline.
- Explainable hazard-specific risk.
- AOI/configuration.
- Provenance and lineage.
- Historical validation.
- Working demo.
- Reproducible tests and documentation.

### P1 — Only when P0 is safe

- EnMAP hyperspectral enhancement.
- Sea-surface temperature.
- Ocean currents.
- ERA5 wind.
- Simple exposure/advection logic.
- Additional model explainability.

Do not add major features outside this scope without explicit approval.

---

## Scientific Guardrails

Use language such as:

- HAB-like spectral anomaly.
- Elevated biological water-quality risk.
- Oil-slick candidate.
- Observational risk.
- Field verification recommended.
- Monitoring priority.
- Confidence.

Do not claim satellite observations alone have:

- confirmed toxic algae,
- confirmed toxins,
- confirmed petroleum composition,
- certified water as safe or unsafe,
- justified automatic plant shutdown.

Remote sensing supports operational awareness and prioritization. Field and laboratory verification remain necessary.

---

## Sensor Roles

### Sentinel-2

Primary roles:

- water colour,
- chlorophyll-related signals,
- red-edge features,
- temporal and spectral biological anomalies,
- historical water-quality comparison.

### Sentinel-1 SAR

Primary roles:

- marine surface-slick candidates,
- oil-related surface anomalies,
- cloud-independent marine observation.

### EnMAP / Future Hyperspectral Data

Primary roles:

- detailed spectral characterization,
- confidence enhancement,
- comparison with multispectral observations.

Hyperspectral data is an enhancement layer, not a P0 dependency.

### Environmental Context

Potential supporting data:

- sea-surface temperature,
- ocean currents,
- wind,
- historical environmental conditions.

---

## Architecture Principle

Preserve this reasoning chain:

Observation
→ Detection
→ Explanation
→ Exposure
→ Risk
→ Monitoring Priority
→ Human Decision

AI is a component of the system, not the product definition.

Prefer explainable, reproducible, and scientifically defensible methods over unnecessary model complexity.

---

## Technical Baseline

- Python: 3.11.
- Conda environment: `aquasentinel813`.
- Python package: `src/aquasentinel`.
- Tests: pytest.
- Linting: Ruff.
- Configuration: TOML.
- AOI format: GeoJSON.
- GitHub repository: `Omar-Aboulwafa/aquasentinel-813`.
- Default branch: `main`.

---

## Repository Is the Source of Truth

Do not rely on chat history, Codex memory, or agent memory.

For hackathon registration, submission, judging, official program-data, and submission-readiness facts, read [docs/HACKATHON_SUBMISSION.md](docs/HACKATHON_SUBMISSION.md).

Before any non-trivial work:

1. Read `AGENTS.md`.
2. Read `docs/PROJECT_STATE.md`.
3. Read the relevant files in `docs/`.
4. Inspect the current Git branch.
5. Inspect `git status`.
6. Inspect affected code and tests.
7. Understand the current architecture before adding dependencies or changing interfaces.
8. Implement only the requested scope.

If conversation history conflicts with the repository, treat the repository and current approved project documentation as authoritative unless the user explicitly changes a decision.

---

## Git Workflow

Do not develop directly on `main` unless explicitly instructed.

Use task-specific branches such as:

- `feature/as-101-sentinel2-stac`
- `feature/as-102-optical-preprocessing`
- `feature/as-201-sentinel1-oil`
- `fix/...`
- `docs/...`
- `chore/...`

Before commit or merge, run:

```text
python -m pytest -v
python -m ruff check .
```

Also inspect:

```text
git status
git diff
```

Never commit:

- `.env`,
- credentials,
- API tokens,
- passwords,
- SSH keys,
- private account data,
- runtime caches,
- large Earth-observation files,
- proprietary company data.

---

## Data and Provenance

Prefer reproducible catalog references, item IDs, product IDs, and manifests over committing raw imagery.

Every real Earth-observation source used by the system should eventually retain:

- platform,
- product or STAC item ID,
- acquisition timestamp,
- source catalog,
- collection,
- source URL when available,
- licence when relevant.

Derived products must preserve lineage to upstream observations.

Expected conceptual lineage:

Source observation
→ derived feature
→ hazard layer
→ risk product
→ operational alert

Do not create derived products that silently lose source lineage.

---

## Configuration Rules

Do not hard-code values that belong in configuration, including:

- AOI paths,
- analysis date windows,
- cloud thresholds,
- data directories,
- PoC risk weights,
- external-service configuration.

Current default configuration:

`config/default.toml`

Risk weights are PoC hypotheses, not validated scientific constants.

Any material change to risk logic should be documented.

---

## Coding Rules

Prefer:

- small focused modules,
- explicit typing,
- validation,
- deterministic processing,
- pure functions where practical,
- unit tests,
- readable scientific code,
- minimal dependencies.

Avoid:

- unrelated refactors,
- hidden global state,
- unexplained magic numbers,
- unnecessary frameworks,
- premature abstraction,
- multiple overlapping libraries for the same task,
- black-box modelling without a baseline,
- broad architectural changes unrelated to the current task.

---

## Dependency Policy

Before adding a dependency:

1. Confirm the standard library cannot reasonably satisfy the need.
2. Confirm the dependency directly supports the active task.
3. Prefer mature and widely used scientific/geospatial packages.
4. Avoid adding overlapping packages for the same function.
5. Update project metadata consistently.
6. Do not upgrade unrelated dependencies during feature work.

---

## Testing Expectations

Every meaningful new module should have tests.

Tests should cover:

- normal behaviour,
- invalid input,
- edge cases,
- scientific guardrails where relevant,
- provenance integrity where applicable.

Never delete or weaken a failing test merely to make the test suite pass unless the underlying requirement has explicitly changed.

---

## Agent Execution

For meaningful tasks:

1. Read the repository instructions and project state.
2. Inspect the existing implementation.
3. State which files will likely change.
4. Implement the smallest complete solution.
5. Add or update tests.
6. Run pytest.
7. Run Ruff.
8. Review the diff.
9. Summarize:
   - what changed,
   - validation performed,
   - limitations,
   - unresolved issues,
   - recommended next step.

If ambiguity could materially affect scientific validity, architecture, data interpretation, or product claims, ask instead of inventing assumptions.

---

## Long-Running Work

For multi-step or multi-hour work:

- follow `.agent/PLANS.md` when available,
- keep progress explicit,
- record major architectural decisions in `docs/DECISIONS.md`,
- update `docs/PROJECT_STATE.md` whenever project state materially changes,
- keep important knowledge in the repository rather than relying on agent memory.

---

## Current Completed Foundations

Completed:

- AS-001 — Repository Scaffold.
- AS-002 — Configuration & AOI Model.
- AS-003 — Provenance Model.

Current engineering baseline:

- Python 3.11 environment is working.
- `main` is synchronized with GitHub.
- Configuration and AOI loading are implemented.
- GeoJSON validation is implemented.
- Runtime context is implemented.
- Provenance models are implemented.
- Provenance JSON serialization is implemented.
- Provenance lineage registry is implemented.
- Provenance registry persistence is implemented.
- Test suite currently passes.
- Ruff currently passes.

Next engineering milestone:

- AS-101 — Sentinel-2 STAC Search.

Always check `docs/PROJECT_STATE.md` for the latest state.

---

## Product Priority Under Deadline

Protect in this order:

1. Real EO-derived results.
2. Scientific credibility.
3. Validation.
4. Explainability.
5. Provenance.
6. Reproducibility.
7. Working demo.
8. Advanced modelling.
9. Visual polish.

Do not sacrifice P0 reliability for P1 features.

---

## Final Agent Principle

The goal is not to produce the most complicated satellite-AI system.

The goal is to produce a credible, explainable, reproducible, and demonstrable system that helps a real desalination operator make an earlier and better monitoring decision.
