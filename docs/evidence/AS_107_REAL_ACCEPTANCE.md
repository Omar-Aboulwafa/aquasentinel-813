# AS-107 M39 — First Real Observational Screening Engineering Acceptance

## 1. Authority, task plan and exact baseline

M39 / E39 / EV-043: **REAL ENGINEERING ACCEPTANCE PASS**. Owner-authorized M39 only; no M40/AS-108 or new Decision 053. Fetch verified official main `7f304bb44af93d2b3a1a3e6982fefad05fb8f452` and both PR #23 parents exactly. Clean isolated `data/as-107-real-acceptance` in `/workspace/aquasentinel-813-as107-m39`; 130 tracked files initially clean. Source/tests/config/dependencies are immutable.

Goal: consume sealed accepted typed AS-104/105/106 evidence using merged as107-v1, independently verify arithmetic/identity/lineage, seal a reconstructable result, document/publish evidence only. Inputs: frozen April sequence and policy; outputs: scalar typed HABRiskScene and small external JSON/log/checksums, no risk raster/cache. Dependencies: existing Python/NumPy only. Risks: corrupted reconstruction, outcome tuning, incomplete/context-free evidence and overclaim. Validation: pre-score tests/preservation, strict parent validators, literal Python/NumPy oracle, repeats/permutation, tamper/regeneration, sealed fresh-process roundtrip and final regression gates. Non-goals: EO retrieval, public upstream science, policy/code changes, biology calibration, PR/merge/closeout.

## 2. Accepted inputs and sealed verification

M34 bundle: `/workspace/aquasentinel-acceptance/as106/m34/c576478b6b6d85894e5317e65a1d0fd6cee38ed1c406d452b10f97712d2cc3bb`. Directory 0555, four files 0444; hashes matched both authoritative AS-106 real-acceptance/closeout records, historical preservation snapshot and SHA256SUMS. Existing M29/M33/AS-104 bundles were likewise verified before loading. All NPZ opens use allow_pickle=False; no object arrays.

| M34 file | SHA-256 | Mode |
|---|---|---|
| SHA256SUMS.txt | `793f29341bbdc057b9198ffd65c7714829e8373c901ea39fd5a7c773584c674d` | 0444 |
| execution.log | `f8ed67c9198c6b415a9369a4659ec5527dc18a2f262a92f7087f44bdaf4c80c7` | 0444 |
| real_acceptance.json | `feb7b974126b2e5ad518febc053494db6d1824badf2fe0db04103e83ecb72d90` | 0444 |
| scientific_arrays.npz | `6ba3d54f056717e9fe4f11f8c58ef649555d781792edd9ac49a40571b442fc19` | 0444 |

M32 selection digest: `570792066c1997b9a403249d994c4e7367bf2f1dafc6473b6e30df20cd6481d5`. Frozen times: 2023-04-03T06:46:21.024000Z → 2023-04-28T06:46:29.024000Z. No scene substitution.

| Typed accepted parent | Product ID |
|---|---|
| April 3 temporal | `temporal:71f6be2d8437e91f7cf213df0bd876897febebe630a02a20bb151a5d852edb11` |
| April 3 geometry | `hab_geometry:7e3a4ba3ba8fb394ca874415c62f7fed7a160609c6dee458d59b35ea0c12cd52` |
| April 28 temporal | `temporal:e814b0574ab30d1841778ee3c5005ffcb313ab42473c41acc028f0a9f7804a8b` |
| April 28 geometry | `hab_geometry:70876fbcb25e8a37abaa238a59e1da32fec9066792e6239db68e284b7bd18682` |
| Accepted persistence | `hab_persistence:c576478b6b6d85894e5317e65a1d0fd6cee38ed1c406d452b10f97712d2cc3bb` |

Persistence input `2f8f6f1c37bd9f8a236109ab821e6e426f222840c4a74f623d2e78bd76529ab7`; output `7739a3f97c0e88113a17629678a0ef31bdb14594400f0568c0dfdfdb5dabafef` unchanged.

## 3. Offline typed reconstruction and guards

A fresh temporary adapter outside Git reconstructs documented dataclasses/arrays, not scientific output. April 3: 88 array members with exact shape/dtype/semantic checks; April 28 temporal: 61 members with shape/dtype; target geometry: 27 arrays; accepted persistence: 9 arrays with exact semantic checks. Typed temporal validate, geometry.validate(temporal) for both dates and persistence.validate(full sequence, witnesses) PASS before first score. Grid, times, masks/labels, regions/counts/area, A/B/C, fingerprints/provenance/version and frozen policy validated. Existing internal integrity regeneration is allowed; public extraction is blocked.

Before any real scoring: socket DNS/connect/send guards, urllib/HTTP/requests/httpx, STAC/Rasterio open, catalog, signing/asset/XML, cache load/write, registry mutation and public AS-102/103/104/105/106 entrypoints blocked. All guarded attempt counts stayed zero, including fresh process. No EO bytes downloaded; Git fetch/push are separate administrative network. Temporary adapter preflight corrections (canonical JSON newline and display-only region field filtering) occurred before the first scoring call; no production/policy/input edits.

## 4. Pre-score freeze and first-result preservation

Canonical exact typed binary64 policy serialization SHA-256: `f1a9291ba47250a66283a0d352496cc7e60fbdb853ad197b0e56bd3192123c07`. Serialized before scoring, then verified unchanged in first call, repeats/control and fresh process. Full policy in JSON retains raw/canonical weights, mandatory components, bands, minimum-factor completeness, administrative .50, recommendations, status, definitions and None/not_implemented semantics.

First real call began `2026-10-10T13:04:58.495566+00:00` and completed `2026-10-10T13:04:58.732346+00:00` UTC; provenance created_at is `2026-10-10T13:04:58.725725+00:00`. First typed result was written immediately before inspection/oracle and made 0444. File SHA-256 `2bd6c2b10cdca85114ecb63011fbeab684cb173e3b61096dbc51fbb7598a5474`. Parent byte/semantic snapshot before/after `b5401a7219d9d58090d8aefa71dade8ff45e81e7bcd98e406f26c215c2696e52`. The first actual result was accepted unchanged; zero policy/code tuning. These experiment times are separate from later bundle/documentation/Git publication.

## 5. Actual authoritative region and family denominators

Region `hab_geometry:70876fbcb25e8a37abaa238a59e1da32fec9066792e6239db68e284b7bd18682:region:1`; label 1; 7 pixels; 2800.0 m² / 0.0028 km². Projected bbox `[249120.0, 2704160.0, 249200.0, 2704240.0]`, first row/column 159/5; participating `['red_edge_line_height', 'visible_green_vs_red']`. One unchanged authoritative region; no filtering/merging/geometry edits.

| Family | Available a_j | Evidence v_j |
|---|---:|---:|
| red_edge_b5_vs_red | 7 | 0 |
| red_edge_line_height | 7 | 7 |
| red_edge_b6_vs_red | 7 | 0 |
| visible_green_vs_red | 7 | 7 |
| visible_green_vs_blue | 7 | 0 |

## 6. Components, weights and contributions

| Component | Numerator/denominator | Value (unrounded) | Configured = canonical weight | Effective weight | Contribution | Availability |
|---|---|---|---|---|---|---|
| spectral_anomaly | 14/35 | 40.0 | 0.35 | 0.5 | 20.0 | available; None |
| chlorophyll_red_edge_signal | 7/21 | 33.333333333333336 | 0.2 | 0.28571428571428575 | 9.523809523809526 | available; None |
| persistence | 0/7 | 0.0 | 0.15 | 0.2142857142857143 | 0.0 | available; None |
| environmental_context | None/None | None | 0.15 | 0.0 | None | unavailable; not_implemented |
| intake_exposure | None/None | None | 0.15 | 0.0 | None | unavailable; not_implemented |

Spectral: 14/35 → 40.0 (`0x1.4000000000000p+5`). Red-edge family evidence breadth: 7/21 → 33.333333333333336 (`0x1.0aaaaaaaaaaabp+5`), not chlorophyll concentration. Persistence A/B/C=7/7/0: 0/7 → 0.0 (`0x0.0p+0`); AVAILABLE because B>0. Context/exposure are None/unavailable/not_implemented with zero effective weights, None contributions and no fictional source IDs.

Canonical available set: spectral_anomaly, chlorophyll_red_edge_signal, persistence. W0=1.0; raw/canonical weights = .35/.20/.15/.15/.15. K=0.7 (`0x1.6666666666666p-1`). Available renormalization and exact math.fsum in canonical order, no imputation/clipping/epsilon or score multiplication by completeness. Contributions are explanatory separate binary64 operations; their rounded display sum is not the authoritative equation.

## 7. Raw score, completeness and interpretation

Exact raw score **29.52380952380953**, float.hex() `0x1.d861861861863p+4`; **Watch** under frozen continuous [25,50) interval. F_all=35/35=1.0, F_red=21/21=1.0, H=7/7=1.0; completeness=min(K,F_all,F_red,H)=**0.7**, hex `0x1.6666666666666p-1`. Flag incomplete_evidence; no limited_evidence_completeness flag (.7 >= .50). Completeness is not probability/calibrated confidence/biological sufficiency.

Storage/explanation order: `['spectral_anomaly', 'chlorophyll_red_edge_signal', 'persistence', 'environmental_context', 'intake_exposure']`. Highest contribution is spectral_anomaly 20.0, then red-edge 9.523809523809526, then available persistence 0.0, then unavailable context/exposure. Assessment `provisional_observational_screening`; recommendation **Review on the next valid acquisition**. Full limitations and persistence streak/gap/region explanations remain in typed JSON.

## 8. Site summary

Selected region `hab_geometry:70876fbcb25e8a37abaa238a59e1da32fec9066792e6239db68e284b7bd18682:region:1`, label 1; score/band/completeness/coverage/drivers/factors/flags/recommendation/limitations copied together. Sole authoritative scored region; frozen selection is maximum raw score, descending completeness, ascending label. No averaging or whole-site biological/operational estimator. Site status None; provisional assessment explicit. Policy support count 802 versus seven candidates.

## 9. Independent arithmetic and fingerprints

Independent Python/NumPy oracle imports no AS-107 arithmetic/fingerprint/ID helpers: counts all a/v and A/B/C directly from accepted masks, reproduces all numerators/denominators, components, W0/weights/K/fsum score/bands, factor denominators/minimum, flags, effective weights/contributions, ordering, recommendations and copied site evidence. Every binary64 comparison uses exact float.hex(); no display-round acceptance. PASS in original and fresh process.

Independent framing reconstructed `as107-input-v1`: **084790273118f50f6c8eaf0ed380dbce730c6dbbd7e4fa0f757c5d145e894d91** and `as107-output-v1`: **25cccf8e8b550a76f28ebb01a2249060de5b1cd3114a7c531ef4775adbc87dae**. Input consumes full target P/C/labels, candidate-supported family bits/recurrence/timing/streak and typed authoritative/regional persistence explanations; excludes unrelated raw features and witness payloads. Eight-byte big-endian canonical-header length, newline-terminated sorted compact JSON, byte_count and C-order bytes. Exact binary64/container/UTC typed serialization. Output includes all semantic region/site/policy/statistics/diagnostics and excludes resulting ID/created_at. Identity independently reconstructed from accepted parents/contracts/time/grid/input hash/full policy/software, then SHA-256 = **hab_risk:113143700cb35ac9230d9c54b68b1b53e2573838a4913d4bc942e81c99903fdb**.

## 10. Repeats, parent-aware validation and tamper controls

Exactly three real public compute calls: first, same logical order, then reversed geometry sequence/witness insertion/policy mapping order. Every semantic field, ID, fingerprints/parameters and immediate source order identical; only provenance created_at differs. A separate altered-created_at copy passed validator with unchanged identity/output fingerprint. Full authoritative parent-aware validation PASS, also from sealed bundle in fresh process (zero additional public risk calls).

| Tamper on copy | Outcome |
|---|---|
| assessment_status | REJECTED / PASS |
| attacker_rehashed_driver_identity_parameters | REJECTED / PASS |
| attacker_rehashed_recommendation_assessment | REJECTED / PASS |
| attacker_rehashed_region | REJECTED / PASS |
| completeness_factor | REJECTED / PASS |
| driver_contribution | REJECTED / PASS |
| driver_effective_weight | REJECTED / PASS |
| driver_value | REJECTED / PASS |
| evidence_completeness | REJECTED / PASS |
| output_fingerprint | REJECTED / PASS |
| product_id | REJECTED / PASS |
| provenance_source | REJECTED / PASS |
| recommendation | REJECTED / PASS |
| risk_band | REJECTED / PASS |
| risk_score | REJECTED / PASS |
| selected_region | REJECTED / PASS |

Attacker controls recomputed output hashes/parameters/provenance and, for driver and recommendation/assessment mutations, recomputed identity/product ID too. Full authoritative-parent regeneration rejected all; locally consistent hashes are not authority. No tampered scene persisted as accepted.

## 11. Provenance, immutability and side effects

Immediate source_ids exactly `(
hab_geometry:70876fbcb25e8a37abaa238a59e1da32fec9066792e6239db68e284b7bd18682,
hab_persistence:c576478b6b6d85894e5317e65a1d0fd6cee38ed1c406d452b10f97712d2cc3bb
)` in target-geometry then persistence order. Temporal witnesses are integrity-only, no PC/AS102/AS103/AS104 shortcut. Read-only sealed registry/M33 provenance metadata verified recursive PC→AS102→AS103→AS104→AS105→AS106→AS107 plus direct target AS105→AS107 edge. No registry instantiated/mutated.

All parent array bytes/dtypes/shapes, metadata/provenance unchanged through first/repeat/control/fresh processes; result has no arrays and all mutable-object identities disjoint from parents. Original sealed bundles/caches/handoffs/recovery files and modes unchanged. No cache/registry writes or upstream calls. Decisions 050/051/052 full-section SHA-256 and byte snapshots retained; zero production/test/dependency/config diffs.

## 12. Sealed M39 bundle and fresh-process roundtrip

External directory `/workspace/aquasentinel-acceptance/as107/m39/113143700cb35ac9230d9c54b68b1b53e2573838a4913d4bc942e81c99903fdb`, mode 0555. No upstream array duplication or risk raster. JSON contains typed exact scene, plain audit fields, parent/policy hashes, denominators/weights/hex values, provenance, software, validation/tamper/preservation/security and scientific limits.

| File | Bytes | SHA-256 | Mode |
|---|---:|---|---|
| SHA256SUMS.txt | 167 | `b71ca40555544202df9a735984901377bd373f625eeb36332807455ce61aa1ab` | 0444 |
| execution.log | 660 | `d77c6307df5363cf43fa62b86e7cc4e6fa224cce4fac7bbe9dda02e34457d54c` | 0444 |
| real_acceptance.json | 121988 | `4473db7e589ee80b2e62209d59a7e16c2381a3f4783e5ebba166ccc778af0133` | 0444 |

SHA256SUMS covers JSON/log; its own SHA separately inventoried. Hashes checked before/after chmod. Fresh Python process reverified checksums/modes, reconstructed full typed result/accepted parents, compared exact first-result bytes/provenance/ID/fingerprints/all fields, ran full parent-aware validation and independent arithmetic/hash reproduction. PASS; zero new public risk/upstream/network calls.

## 13. Actual quality gates

Pre-score focused: **292 passed in 45.89s**, no warnings. Pre-score full: **1285 passed in 112.89s**, six existing Rasterio PendingDeprecationWarnings. Ruff/diff PASS. Existing Python 3.11.16/NumPy 2.2.6 environment, this worktree src path, disabled bytecode/pytest/Ruff caches; no install. Local tests, no GitHub CI-success claim.

Final M39 engineering quality gate: **292 focused tests PASS (43.61s); 1285 full tests PASS (103.96s), six existing Rasterio PendingDeprecationWarnings; Ruff/diff/credential/preservation PASS.** Local engineering checks, no GitHub CI-success claim.

## 14. Scientific interpretation and retained limitations

Under the frozen AS-107 observational screening policy, the April 28 validation AOI produced a **Watch observational screening score of 29.52380952380953**, with evidence completeness **0.7** and component coverage **0.7**. Environmental context and intake exposure remain unavailable. The result is provisional observational screening, not confirmed HAB or operational water-safety determination.

**No same-pixel candidate recurrence was observed among the 7 target candidate pixels with valid prior observational history.** This is only accepted C/B=0/7; not biological nonpersistence, no HAB, safe water or zero risk. Observation gap remains 25 days + 8 seconds, streak 1 at all seven candidates. Context/exposure unavailable explains K/completeness .7; full local family/history availability is not full scientific evidence. F1–F3 overlap spectral/red-edge components; no independent corroboration or calibrated weight claim.

BOA is not aquatic Rrs or measured chlorophyll. Sparse (~10%) five-history support, five shared March references, two April observations, exact-pixel/no-motion limitations, candidate-conditioning/site maximum and pending Decision050 comparison remain visible. Five observations are not statistical sufficiency. No confirmed HAB/bloom/species/toxins, water safety/shutdown, HAB probability/calibrated confidence, accuracy/sensitivity/specificity/false-positive rate/lead-time or complete intake-risk claim. Al Raha is an analyst-defined validation AOI, not a confirmed desalination intake boundary.

## 15. Publication / stop boundary

M39/E39/EV-043 real engineering acceptance PASS; evidence-only authorized commit/push for owner review. No PR/merge, no M40/AS108, no new Decision053, environmental/intake implementation, EO retrieval, public AS105/106 rerun, policy tuning or 05.10 robustness. Scientific execution/bundle/documentation/publication are separate timestamps. The already merged M38 and historical M36/M37/M38 evidence remain unchanged; current status is additive, not a rewrite of earlier absent-score checkpoints.
