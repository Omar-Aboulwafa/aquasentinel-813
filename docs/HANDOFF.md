# AquaSentinel 813 — Handoff Guide

**Last updated:** 9 October 2026 (Asia/Dubai)
**Repository:** `Omar-Aboulwafa/aquasentinel-813`
**Default branch:** `main`
**Current fix branch:** `fix/as-102-reusable-pc-sas-token`, in separate worktree `/workspace/aquasentinel-813-pc-sas-token-fix`; uncommitted for review.
**Decision 048 implementation merge commit:** `39f2aee90c727fc151886efbdea44daec0e3f9b4` (PR #10); exact Decision 049 fix base.
**Preserved development branch:** `feature/as-104-temporal-baseline`; AS-104 explicitly authorized, uncommitted and real acceptance BLOCKED. AS-105+ NOT authorized and NOT started.
**Closeout preparation branch:** This closeout was prepared on `docs/as-103-post-merge-closeout`.
**AS-103 implementation merge commit:** `b770d0561da9ac2b81ca2d4b8e784adff66ee231` (merged via PR #8).
**AS-102 closeout preparation branch:** The AS-102 closeout was prepared on `docs/as-102-post-merge-closeout`.
**AS-102 implementation merge commit:** `627b6ae8a509509dbb2d5d43bbdc6d74e0ce2aac` (merged via PR #6).

**Current-state update — Decision 049 (9 October 2026, Asia/Dubai):** Decision
048 is merged via PR #10. Resumed AS-104 then encountered intermittent PC `/sign`
HTTP 504s. Only the separate reusable-account/container-token transport fix is
active here; no AS-104 algorithm work or real acceptance was resumed in this task.
Fix gate: **531 tests passed** (421 main baseline +110 net new transport cases),
Ruff/diff PASS, same six historical Rasterio warnings. Fresh March-4 smoke:
**1** anonymous token HTTP attempt/acquisition, **11/11** signed assets, bounded
XML/TIFF reads **1,024/4,096 bytes** via HTTP **206**, and **0** additional token
requests for B03/SCL/XML reuse. This is transport evidence only.
Original AS-104 status, 83 file hashes, accepted cache hashes and retained safety
stash remain unchanged. Decision 047/M19/E18–E19/EV-022–EV-023 and M21/E21/EV-025
remain only there; their bodies are not copied here. Decision 049/M22/E22/EV-026
belong to this isolated fix. Earlier Decision 048/AS-103 status wording below is
historical; this update governs current state. AS-104 real acceptance remains
BLOCKED pending Decision 049 review/merge. No commit/push/PR/merge; AS-105+ and
P1 homogeneous-05.10 robustness study NOT started.

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

Completed continuity setup and Codex read-only onboarding:

- AS-000C.1 — `AGENTS.md` completed and merged into `main`.
- AS-000C.2 — `PROJECT_STATE.md` completed and merged into `main`.
- AS-000C.3 — PRD completed and merged under `docs/`.
- AS-000C.4 — `DECISIONS.md` completed and merged into `main`.
- AS-000C.5 — `HANDOFF.md` completed and merged into `main`.
- AS-000C.6 — `.agent/PLANS.md` completed and merged into `main`.
- AS-000C.7 — Codex read-only onboarding **COMPLETED** on 2 October 2026 at `779069d`.
- AS-000C.8 — Codex development handoff **COMPLETED** with explicit AS-101 implementation authorization on 2 October 2026.

Current project phase:

**Foundation complete → continuity complete → AS-101/AS-102/AS-103 complete and merged → Decision 048 merged via PR #10 → AS-104 resumed, uncommitted/preserved and real acceptance BLOCKED by SAS transport → Decision 049 transport fix uncommitted for review → AS-105+ unauthorized and unstarted.**

Current implementation and next milestone:

- AS-101 — Sentinel-2 STAC Search was completed on `feature/as-101-sentinel2-stac` from base `51f4ede`. Implementation commit `41a0b0b`, documentation commit `b3f0e9f`, and the approved review fixes are merged into `main` via [PR #2](https://github.com/Omar-Aboulwafa/aquasentinel-813/pull/2) at merge commit `1b83a732155ee01c01b7d33cb50115725cfb08c3`.
- **97 tests passed**, Ruff passed, and `git diff --check` passed. A real CDSE query returned 44 scenes and every scene converted to valid provenance.
- See `docs/AS_101_STAC_SEARCH.md` for usage, semantics, and smoke-test evidence.
- AS-102 was explicitly authorized on 6 October 2026 and is **COMPLETE AND MERGED** through [PR #6](https://github.com/Omar-Aboulwafa/aquasentinel-813/pull/6). Implementation commit: `fe3d27046c40600010753957ee8921d57071ec48`. Merge commit: `627b6ae8a509509dbb2d5d43bbdc6d74e0ce2aac`, merged `2026-10-08T07:06:46Z` / `2026-10-08T11:06:46+04:00` Asia/Dubai. AS-103 is complete and merged through PR #8; AS-104 remains NOT authorized and NOT started. See §22 for usage and validation evidence.
- AS-103 is **COMPLETE AND MERGED** through [PR #8](https://github.com/Omar-Aboulwafa/aquasentinel-813/pull/8). Implementation commit: `5638bc8b4ab06f235f908642f714a7cc83b35709`. AS-103 implementation merge commit: `b770d0561da9ac2b81ca2d4b8e784adff66ee231`, merged `2026-10-08T10:43:24Z` / `2026-10-08T14:43:24+04:00` Asia/Dubai. See §23 and journal M18 / EV-021 for final review/merge and preserved acceptance evidence.

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

Existing implemented foundations (including AS-102 merged through PR #6):

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

## 15. AS-101 Implementation and Next Engineering Task

AS-101 was explicitly authorized and is now complete and merged into `main` via PR #2 at merge commit `1b83a732155ee01c01b7d33cb50115725cfb08c3`. AS-102 was explicitly authorized on 6 October 2026 and is **COMPLETE AND MERGED** through [PR #6](https://github.com/Omar-Aboulwafa/aquasentinel-813/pull/6). Implementation commit: `fe3d27046c40600010753957ee8921d57071ec48`. Merge commit: `627b6ae8a509509dbb2d5d43bbdc6d74e0ce2aac`, merged `2026-10-08T07:06:46Z` / `2026-10-08T11:06:46+04:00` Asia/Dubai. AS-103 is complete and merged through PR #8; AS-104 remains NOT authorized and NOT started.

### AS-101 — Sentinel-2 STAC Search

Goal:

Given:

- configured AOI,
- configured date window,
- configured cloud-cover threshold,

return real Sentinel-2 observations suitable for downstream analysis.

Implemented AS-101 scope:

- use the explicitly selected CDSE default endpoint/provider, with configurable endpoint and collection,
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

## 16. First Codex Task — COMPLETED

The first Codex task was read-only and completed successfully on 2 October 2026 at `779069d`. Repository documentation, architecture, configuration/AOI, provenance, and tests were inspected, and Codex's understanding was verified without modifying repository files.

Read-only onboarding prompt reference:

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

Codex onboarding is complete. AS-000C.8 was completed by the separate explicit AS-101 development authorization on 2 October 2026.

---

## 17. AS-101 Codex Handoff Rule

Read-only onboarding was accepted, and AS-101 subsequently received explicit implementation authorization. Onboarding completion alone did not authorize code changes. Future milestones require separate authorization.

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

**Foundation complete → continuity complete → AS-101/AS-102/AS-103 complete and merged → AS-104 authorized, uncommitted/preserved and real acceptance BLOCKED → Decision 048 upstream fix uncommitted for review → AS-105+ unauthorized and unstarted.**

Immediate priority:

**Review the uncommitted Decision 048 fix in its separate worktree. AS-104 remains preserved and real acceptance BLOCKED pending upstream review/merge and a separate frozen-contract rerun. Do not resume AS-104 or start AS-105+.**

Core constraint:

**Protect scientific credibility and P0 delivery before sophistication.**


## 22. AS-102 Merged Implementation Handoff

AS-102 was explicitly authorized on 6 October 2026 and is **COMPLETE AND MERGED** through [PR #6](https://github.com/Omar-Aboulwafa/aquasentinel-813/pull/6). Implementation commit: `fe3d27046c40600010753957ee8921d57071ec48`. Merge commit: `627b6ae8a509509dbb2d5d43bbdc6d74e0ce2aac`, merged `2026-10-08T07:06:46Z` / `2026-10-08T11:06:46+04:00` Asia/Dubai. AS-103 is complete and merged through PR #8; AS-104 remains NOT authorized and NOT started.

- CDSE discovery is preserved; Planetary Computer supplies the actual raster product, with strict time/platform/tile/orbit matching and independent product provenance.
- Nine native reflectance bands plus SCL and product XML; XML-driven offsets/quantification, bounded COG reads, fixed 20 m EPSG:32640 AOI grid (310 × 228), bilinear reflectance/nearest SCL, and all-band conservative interpolation/water support.
- Fresh real acceptance began `2026-10-06T10:07:14.660936+00:00` / `2026-10-06T14:07:14.660936+04:00` Asia/Dubai. CDSE returned 44 candidates; known April 28 observation matched PC baseline 05.09 separately from CDSE 05.10.
- AOI 67,449 pixels; valid data 65,166; candidate water 10,211; retained valid water 7,963; AOI water fraction 0.11805957093507688 (11.805957%); water retention 0.7798452649103907 (77.984526%). Excluded candidate water: 2,248. These are mask outcomes, not confirmed water/HAB or aquatic suitability.
- AOI cache/checksum reload is equivalent and uses no network/signing/raster work when the cache ID is known. Runtime cache material remains ignored.
- AS-102 final reviewed quality baseline: **265 tests passed**, Ruff passed, `git diff --check` passed. Six Rasterio deprecation warnings remain non-blocking. The historical 6 October implementation acceptance was **213 tests passed** (all prior 97 retained), with two transitive Affine warnings. Python 3.11.16 / NumPy 2.2.6 / Rasterio 1.4.3 / GDAL 3.9.3 in that cloud run. GitHub reported clean/mergeable before merge and no configured/reported CI/workflow checks; no GitHub CI pass is claimed.
- Decisions 039–045 record the newly authorized contract. EV-016/EV-017 and journal M15 preserve the 6 October implementation evidence; EV-018 and journal M16 record final review/merge. Historical EV-014 PENDING and later FG-01 PASS/READY plus EV-015 remain preserved.
- L2A BOA reflectance is not aquatic Rrs; coastal/turbid/mixed-water SCL errors remain. No indices, chlorophyll, HAB/toxin/water-safety/intake-risk or lead-time conclusions were computed.

### Resume/reproduce

Read `docs/AS_102_OPTICAL_PREPROCESSING.md` and `docs/evidence/AS_102_OPTICAL_PREPROCESSING_VALIDATION.md` before changing code. On this cloud checkout, use `source .venv/bin/activate` (Python 3.11); existing office/home Conda guidance above remains valid. Reinstall the updated project dependencies in the relevant Python 3.11 environment before testing on another machine; do not assume runtime caches are shared by Git.

Public entry point: `aquasentinel.preprocessing.optical.preprocess_optical_scene(context, candidate)`. The candidate comes from existing `search_sentinel2(context)`. Offline replay: `preprocess_optical_scene(context, known_cache_id=cache_id)` validates cache/AOI/grid and performs no external-data work. Canonical default cache ID from the real acceptance:

`0725a908d21cd655e83f70d2bb11247dc0f1516f0c00ea275efc3239113ee4a6`

Cache is local under `data/cache/as102/<cache_id>/`, containing AOI arrays and unsigned manifest/provenance. If absent, follow the documented strict live workflow; if corrupt, fail and investigate rather than silently reuse it. All water consumers must apply `valid_water_mask`; a finite band value alone is not eligibility. Zero retained water is a valid outcome. Captured presentation screenshots/maps and independent aquatic/HAB validation remain outstanding.


## 23. AS-103 — Spectral Feature Extraction — COMPLETE AND MERGED

AS-103 is **COMPLETE AND MERGED** through [PR #8](https://github.com/Omar-Aboulwafa/aquasentinel-813/pull/8). Implementation commit: `5638bc8b4ab06f235f908642f714a7cc83b35709`. AS-103 implementation merge commit: `b770d0561da9ac2b81ca2d4b8e784adff66ee231`, merged `2026-10-08T10:43:24Z` / `2026-10-08T14:43:24+04:00` Asia/Dubai.

Final reviewed baseline: **348 tests passed**, Ruff passed and `git diff --check` passed; six existing non-blocking Rasterio PendingDeprecationWarnings only, with no new AS-103 warnings. No GitHub Actions/workflow CI run was configured/reported; no GitHub CI success is claimed.

AS-103 development is closed. AS-104 — Temporal Baseline is NEXT PLANNED only, NOT authorized and NOT started; a future agent must obtain separate explicit authorization before implementing it. The completed stage produces candidate per-scene BOA spectral signals only, not temporal anomalies, HAB presence, chlorophyll concentration, species, toxins, water safety, intake exposure, operational risk, persistence or warning lead time.

### Historical implementation/acceptance checkpoint — M17 / EV-019–EV-020

The following records the initial feature-branch acceptance state. Its uncommitted/unpushed/unmerged wording is historical; the later review/publication stage is M18 / EV-021. The cached real-scene experiment was not rerun during merge review or this documentation closeout.

AS-103 was explicitly authorized on 8 October 2026 and is implemented/validated on `feature/as-103-spectral-features`, based on main `642a469414f096b4ac7cd96de895aa38f7da42ec`. Changes remain uncommitted, unpushed and unmerged for code review; no PR. AS-104 is next planned but NOT authorized and NOT started.

- Execution plan was written before implementation; Decision 046 freezes the accepted contract.
- Pure `extract_spectral_features(scene)` with six canonical signed-BOA candidate features;
  nominal MCI 665/705/740 nm, k=1.0, no threshold or event inference.
- Float64 arithmetic, float32 arrays, feature-specific masks within unchanged AS-102 water;
  fixed 1e-4/1e-6 denominator guards, NaN outside support, typed statistics/diagnostics.
- Versioned SHA-256 mask/five-band input fingerprint and canonical deterministic identity;
  immediate AS-102 derived parent lineage, not a raw-source shortcut. No AS-103 disk cache.
- Cached acceptance at `2026-10-08T09:52:47.133486+00:00` UTC / `2026-10-08T13:52:47.133486+04:00`
  Asia/Dubai: same EPSG:32640 310×228 grid, 7,963 parent pixels and 7,963 valid pixels
  for each feature; no denominator/nonfinite exclusions. Two unclipped NDCI-like values
  outside [-1,1]; negative-input counts 2 for B05/red and 491 for B06-inclusive features.
- Repeated arrays/masks/summaries/identity and PC→AS-102→AS-103 lineage verified;
  four independent scalar pixel checks; external access/write entry points blocked.
- **348 tests passed** (265 retained +83 new), Ruff and diff checks passed.
  Six existing Rasterio PendingDeprecationWarnings; no new AS-103 warnings.
- AS-102 source/config/dependencies/cache format and generic provenance were preserved.
- BOA is not aquatic Rrs; features are not HAB, chlorophyll concentration, species,
  toxins, safety, shutdown, risk or lead-time evidence. Temporal/event validation remains
  future. Reference-page retrieval HTTP 403 is recorded without claiming a live fetch.

Read [AS-103 execution plan/API](AS_103_SPECTRAL_FEATURES.md) and
[acceptance evidence](evidence/AS_103_SPECTRAL_FEATURES_VALIDATION.md).
Use `extract_spectral_features(parent)` after the existing verified AS-102 cache reload;
no feature cache or network is required. AS-103 implementation is complete and merged; see journal M18 / EV-021 for final review/publication.
AS-104 — Temporal Baseline remains NEXT PLANNED only, NOT authorized and NOT started.

## 24. Decision 048 Upstream Fix Handoff — IN REVIEW

Read [fix plan/API](AS_102_REQUIRED_PC_BASELINE_FIX.md), Decision 048 and
[EV-024 validation](evidence/AS_102_REQUIRED_PC_BASELINE_FIX_VALIDATION.md).
Branch `fix/as-102-required-pc-baseline`; worktree
`/workspace/aquasentinel-813-as102-baseline-fix`; exact base
`c6accab2c5753734466a6375d1b3ce1762e99bed`. No dependency/config/schema changes.

Three existing APIs now accept optional keyword-only `required_processing_baseline`.
None retains exactly-one observation matching; an explicit NN.NN baseline filters
validated exact matches and still fails on zero/multiple products. No generation
fallback or CDSE-processing preference. Actual PC lineage and separate discovery
context remain recorded in existing identity. Same actual product means same
cache/product identity. Known-cache reload checks the constraint without access
or writes, and regular cache reuse checks it before returning.

Real metadata smoke on March 4/9/14/24/29 and April 28 resolved all expected 05.09
products, full eleven-asset set, tile 40RBN/orbit 20; **6/6 PASS**, **0** forbidden
signing/XML/raster/preprocessing/cache calls. Existing April cache ID
`0725a908d21cd655e83f70d2bb11247dc0f1516f0c00ea275efc3239113ee4a6` is unchanged,
accepts 05.09 and rejects 05.10. Local fix gate **421 passed**, Ruff/diff pass,
six unchanged historical Rasterio warnings; no GitHub CI claim.

The original `/workspace/aquasentinel-813` stays on
`feature/as-104-temporal-baseline` at the same base with all AS-104 changes intact.
Never stash, stage, reset, clean, switch, move, delete or edit it for this fix.
Decision 047 remains there; M19/E18–E19/EV-022–EV-023 are reserved there, while this
fix uses owner-approved M20/E20/EV-024. No original AS-104 docs are imported.
All earlier decisions/milestone/evidence records retain their historical wording.

Stop state: upstream fix uncommitted for review, no commit/push/PR/merge. AS-104
real acceptance BLOCKED until this fix is reviewed/merged and the unchanged
target/March period/minimum-five experiment separately rerun. Metadata success
does not prove XML, raster, water support, temporal acceptance or a hazard.
AS-105+ NOT authorized and NOT started.

## 25. Decision 049 — Reusable PC SAS Transport Fix — IN REVIEW

Plan: [AS-102 reusable-token fix](AS_102_REUSABLE_PC_SAS_TOKEN_FIX.md).
Evidence: [EV-026 validation](evidence/AS_102_REUSABLE_PC_SAS_TOKEN_FIX_VALIDATION.md).
Branch/worktree/base are recorded in the header. Decision 049 is explicitly
owner-authorized; implementation and documentation remain uncommitted for review.

`sign_asset(href, settings)` preserves its public API and strict unsigned-HREF
allowlist. Derive validated Azure account/container and official token route from
the configured HTTPS SAS issuer; no hardcoded asset scope, API key, SDK, new
config or dependency. Private process-memory tokens are reused across assets/
scenes while >60 seconds remain and refreshed at <=60 seconds. At most five
acquisition attempts for HTTP 429/500/502/503/504 or typed transient connection/
timeouts, with 0.8/1.6/3.2/6.4-second delays. Invalid payload/security/type errors
and other HTTP statuses are terminal. Never persist/log token or signed HREF.

Stable unsigned source/provenance/cache identity remains unchanged. Existing
bounded HTTP reader/redirect/security checks and all XML/raster callers remain
unchanged, with no generic provenance/schema/decoding/grid/mask/resampling or
AS-103/AS-104 algorithm change. No new raster/cache product was created.

**531 passed**, Ruff/diff PASS, six unchanged Rasterio warnings. Real March-4
05.09 smoke at 06:44:49–06:44:51 UTC / 10:44:49–10:44:51 Asia/Dubai on 9 October:
one anonymous token HTTP 200, eleven transient signs from one scope, XML 1,024
bytes and B02 TIFF header 4,096 bytes (both 206), three reuse signs with zero
additional token requests. No full processing or AS-104 acceptance claim.

Preserve original `/workspace/aquasentinel-813` on
`feature/as-104-temporal-baseline` at `39f2aee90c727fc151886efbdea44daec0e3f9b4`:
never switch/stash/apply/drop/reset/clean/stage/commit/format/edit it for this fix.
Safety stash `f93950aab6fdfb40bb100158915ef12692aa1665` stays intact. Cross-worktree
history belongs to its existing owner; this fix uses only Decision 049/M22/E22/
EV-026, preserving Decision 048/M20/E20/EV-024 history. Next gate is owner review
and merge of this fix before separately rerunning AS-104 real acceptance.
No AS-105+, P1 05.10 study or GitHub CI-success claim.
