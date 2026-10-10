# AS-106 M34 — Real recurrence engineering acceptance

## 1. M34 / E34 / EV-038 scope

**REAL ENGINEERING ACCEPTANCE PASS**, using the first real production `as106-v1` recurrence over the frozen two-date April sequence. This is not biological/event validation. No scientific algorithm/policy/source/test/config/dependency changes or new EO access. M35 remains NOT STARTED; no PR or merge.

## 2. Official base

- **Official main / PR #19 merge / branch base:** `4cde14ee448079163c2a08f3951f8dac294f8dac`

Branch `data/as-106-real-acceptance`; isolated worktree `/workspace/aquasentinel-813-as106-m34`. Initial `git fetch origin main` verified the exact base; clean worktree before execution. Final authorized branch push is separate Git access, not EO access.

## 3. Frozen M32 sequence / digest

- **M32 selection SHA-256:** `570792066c1997b9a403249d994c4e7367bf2f1dafc6473b6e30df20cd6481d5`

1. April 3: `2023-04-03T06:46:21.024000Z`.
2. April 28 explicit/latest target: `2023-04-28T06:46:29.024000Z`.

No date added, removed or replaced. Inventory and M33 evidence byte-identical; no selection/metadata query or upstream rerun.

## 4. Accepted April 3 / April 28 parent IDs

| Date | Typed temporal integrity witness | Immediate geometry parent |
| --- | --- | --- |
| April 3 | temporal:71f6be2d8437e91f7cf213df0bd876897febebe630a02a20bb151a5d852edb11 | hab_geometry:7e3a4ba3ba8fb394ca874415c62f7fed7a160609c6dee458d59b35ea0c12cd52 |
| April 28 target | temporal:e814b0574ab30d1841778ee3c5005ffcb313ab42473c41acc028f0a9f7804a8b | hab_geometry:70876fbcb25e8a37abaa238a59e1da32fec9066792e6239db68e284b7bd18682 |

April 3 P794 / C88 / 15 regions; April 28 P802 / C7 / one region / 2,800 m². These input guards matched before AS-106.

## 5. Offline reconstruction verification

All ten owner-required input artifact hashes and read-only file/directory modes verified before computation. Fresh independent temporary adapter rebuilt directly from accepted manifest/report schemas, with no import/dependency on earlier /tmp scripts. Real AnalysisGrid, TemporalFeatureScene, HABAnomalyGeometryScene and DerivedProductRecord reconstructed; no dictionary substitutes.

Temporal validators and both `geometry.validate(temporal_parent)` calls PASS; exact IDs/fingerprints/counts/grid and frozen Decision 050 policy PASS; common AS-104 contract identical, SHA-256 `8e13d83acf214e35465077d893178f6998f9a1976cd01582d4d468601f2513fc`. Chronological timestamps/latest target PASS; no cross-scene array aliasing. M33 88-array semantic hash/dtype/shape inventory PASS. Historical M29 display fields explicitly projected outside typed region fields; coordinates canonicalized as existing acceptance convention.

Socket/DNS/connect, requests/httpx/urllib/HTTP, STAC, Rasterio-open, signing/transport/cache and public AS-102/103/104/105 entrypoints were blocked. Observed attempts **0**, scientific metadata/assets/XML/signing requests **0**, downloaded EO bytes **0**. Existing parent validators internally regenerate AS-105 only as approved integrity verification. A temporary immutability serializer needed AnalysisGrid.to_dict() to represent Affine before the first production call; diagnostic corrected outside Git, not a scientific input/algorithm change.

## 6. Exact AS-106 product identity

- **Product ID:** `hab_persistence:c576478b6b6d85894e5317e65a1d0fd6cee38ed1c406d452b10f97712d2cc3bb`
- **Identity SHA-256:** `c576478b6b6d85894e5317e65a1d0fd6cee38ed1c406d452b10f97712d2cc3bb`
- **Input content fingerprint:** `2f8f6f1c37bd9f8a236109ab821e6e426f222840c4a74f623d2e78bd76529ab7`
- **Output content fingerprint:** `7739a3f97c0e88113a17629678a0ef31bdb14594400f0568c0dfdfdb5dabafef`

Version `as106-v1`; input `as106-input-v1`; output `as106-output-v1`. Canonical identity JSON SHA-256 independently recomputed PASS. Input/output fingerprints separately recomputed with production helper contracts PASS. Full identity/common temporal contract/policy/software/provenance retained in normalized JSON. Creation timestamp excluded from product identity; changed provenance time validates with identical product ID.

## 7. Q / A / B / C definitions and actual counts

| Population | Definition | Actual count |
| --- | --- | --- |
| Target P | April 28 policy-evaluable pixels | 802 |
| Q | P28 AND P03 | 793 |
| A | C28 | 7 |
| B | C28 AND P03 | 7 |
| C | C28 AND P03 AND C03 | 0 |
| No prior candidate history | A − B | 0 |

Nine target-P pixels have no prior support; no target candidate lies in those nine. Unsupported means UNKNOWN, not candidate absence. April 3 supported noncandidate breaks the target streak. No neighborhood/region/motion matching.

## 8. Candidate history coverage

**B/A = 7/7 = 1.0 (100%)**. This is the target-candidate history denominator. Global Q/P is 793/802; April 3 P/valid-water (~13%) is a separate upstream statistic and must not replace B/A.

## 9. Recurrence fraction

**C/B = 0/7 = 0.0**, not None because the denominator is nonempty. All seven target candidates had prior observational support; none was a same-pixel April 3 candidate. Zero recurrence was retained without tuning, changing dates or policy.

## 10. Streak histogram

On A only: **streak 1 → 7 pixels**; streak 2 → 0; histogram sums to 7. Outside target C, streak 0. No streak >2 is possible. Prior-count histogram on target P: **0 → 9; 1 → 793**.

## 11. Exact timing results

Interval **25 days + 8 seconds = 2,160,008 seconds = 2,160,008,000,000 µs**. Direct integer UTC arithmetic verified.

| Array / support | Exact distribution |
| --- | --- |
| current_streak_span_distribution_full_grid | {'-1': 70673, '0': 7} |
| current_streak_span_distribution_on_target_C | {'0': 7} |
| previous_valid_gap_distribution_full_grid | {'-1': 69887, '2160008000000': 793} |
| previous_valid_gap_distribution_on_target_P | {'-1': 9, '2160008000000': 793} |

Previous-valid gap is the exact interval at Q, -1 otherwise. Current span is 0 for all seven singleton target candidates, -1 outside C28. None for regional recurrent-span maximum/median, since no recurrent pixels exist; do not replace those empty-support summaries with zero. Gaps/spans are observation timing, not continuous bloom duration.

## 12. Recurrent pixel count

**0**. `recurrent_candidate_mask` is false everywhere. This supports the specific observational statement below, not absence of HAB or continuous biological presence/absence.

## 13. Target-region recurrence summary

Authoritative AS-105 target region ID: `hab_geometry:70876fbcb25e8a37abaa238a59e1da32fec9066792e6239db68e284b7bd18682:region:1`. Component label 1 and all seven target pixels/geometry retained; no new recurrence regions.

| Region field | Value |
| --- | --- |
| candidate_history_coverage | 1.0 |
| component_label | 1 |
| maximum_current_streak_span_us | None |
| maximum_streak_count | 1 |
| median_current_streak_span_us | None |
| median_streak_count | 1.0 |
| persistence_evaluable_target_candidate_count | 7 |
| recurrence_fraction | 0.0 |
| recurrent_candidate_count | 0 |
| target_pixel_count | 7 |

| Prior observation field | Value |
| --- | --- |
| acquired_at | 2023-04-03T06:46:21.024000+00:00 |
| candidate_overlap_fraction_of_supported | 0.0 |
| candidate_overlap_pixel_count | 0 |
| geometry_product_id | hab_geometry:7e3a4ba3ba8fb394ca874415c62f7fed7a160609c6dee458d59b35ea0c12cd52 |
| supported_target_region_pixel_count | 7 |

Regional B/C reconcile exactly to global B=7/C=0. Streak maxima/medians use B; recurrent-span summaries use recurrent pixels. Prior support 7 / overlap 0 / overlap-support fraction 0.0.

## 14. Independent Boolean oracle

With exactly one prior observation, direct oracle (not copied recurrence implementation): `Q=P28&P03`; prior count = Q as uint32; `B=C28&Q`; recurrent = `C28&P03&C03`; streak 2 at recurrent candidates, 1 at other target candidates, 0 elsewhere. Gap = exact interval at Q / -1 elsewhere. Span = exact interval at recurrent candidates / 0 at other target candidates / -1 elsewhere. Global denominators, exact histogram and every regional/prior-observation field independently reproduced. **PASS**.

## 15. Nine-array reproduction

| Field | Required dtype | Shape | Oracle |
| --- | --- | --- | --- |
| current_streak_count | uint32 | [228, 310] | PASS |
| current_streak_span_us | int64 | [228, 310] | PASS |
| persistence_evaluable_mask | bool | [228, 310] | PASS |
| previous_valid_observation_gap_us | int64 | [228, 310] | PASS |
| prior_valid_observation_count | uint32 | [228, 310] | PASS |
| recurrent_candidate_mask | bool | [228, 310] | PASS |
| target_candidate_analysis_support_mask | bool | [228, 310] | PASS |
| target_candidate_mask | bool | [228, 310] | PASS |
| target_component_labels | int32 | [228, 310] | PASS |

**9/9 arrays exact PASS; 9/9 dtypes PASS**. Semantic SHA-256 per array retained in JSON; no huge raw array dump. NPZ uses exactly these nine named numeric arrays, no pickle.

## 16. Deterministic repeat / permutation

Same-order repeat PASS; reverse caller order PASS. Product ID, input/output fingerprints, all arrays/dtypes, statistics, region summaries/parameters and chronological provenance source order identical. Created_at exclusion PASS using altered provenance timing and unchanged product identity with successful validation. Three authorized public real calls total (first plus two repeats); fresh bundle audit blocks further public recurrence calls. Internal validator regeneration is distinct.

## 17. Parent-aware validation

`real_scene.validate([april3_geometry, april28_geometry], temporal_parents=...)` **PASS**. Both temporal witnesses and complete geometry parents validated normally. Parent array/metadata immutability PASS; all returned arrays do not alias any parent. Fresh bundle roundtrip reconstructs typed scene and calls the same validator, with all upstream/public recurrence entrypoints blocked.

## 18. Tamper rejection

| In-memory mutation | Validation result |
| --- | --- |
| gap | REJECTED / PASS |
| provenance | REJECTED / PASS |
| recurrent_mask | REJECTED / PASS |
| region | REJECTED / PASS |
| rehashed_recurrent_mask | REJECTED / PASS |
| statistics | REJECTED / PASS |
| streak | REJECTED / PASS |

Seven controls rejected: recurrent mask, streak, gap, global statistics, region summary, provenance shortcut and recurrent mask with recomputed output fingerprint/consistent provenance parameter copy. No accepted persisted artifact was modified.

## 19. Provenance

Immediate AS-106 source_ids are exactly chronological April 3 AS-105 then April 28 AS-105, including target. AS-104 IDs are integrity witnesses, not immediate source shortcuts. Typed provenance matches identity/processing parameters and preserves PC → AS-102 → AS-103 → AS-104 → AS-105 → AS-106. Full DerivedProductRecord in JSON; generic schema unchanged.

## 20. Acceptance bundle hashes and roundtrip

- **External bundle directory:** `/workspace/aquasentinel-acceptance/as106/m34/c576478b6b6d85894e5317e65a1d0fd6cee38ed1c406d452b10f97712d2cc3bb`

| File | Bytes | SHA-256 | Mode |
| --- | --- | --- | --- |
| SHA256SUMS.txt | 255 | 793f29341bbdc057b9198ffd65c7714829e8373c901ea39fd5a7c773584c674d | 0444 |
| execution.log | 1335 | f8ed67c9198c6b415a9369a4659ec5527dc18a2f262a92f7087f44bdaf4c80c7 | 0444 |
| real_acceptance.json | 58486 | feb7b974126b2e5ad518febc053494db6d1824badf2fe0db04103e83ecb72d90 | 0444 |
| scientific_arrays.npz | 6527 | 6ba3d54f056717e9fe4f11f8c58ef649555d781792edd9ac49a40571b442fc19 | 0444 |

Directory **0555**, all files **0444**. SHA256SUMS covers the other three files; tracked JSON records all four hashes. Bundle remains outside Git.

Fresh process verified checksums and all nine array semantic hashes/dtypes/shapes using `numpy.load(..., allow_pickle=False)`, reconstructed the four accepted parents and typed HABPersistenceScene, compared exact IDs/fingerprints/statistics/regions/provenance, and validated against parents **PASS**, both before and after final sealing. No network/public upstream/public recurrence calls. Bundle JSON has sufficient typed metadata for future audit without rerunning public M34; existing validator internal regeneration is permitted.

## 21. Preservation

Snapshot before real computation: **113 tracked files / 37 protected external files / 48 permission records** plus exact safety stash inventory. All pre-existing tracked files unchanged during science; only eight authorized docs paths subsequently change. Six historical accepted AS-102 caches, new M33 April 3 cache/handoff, April 28 AS-104 handoff, M29 bundle, M32/M33 evidence and recovery files remain byte-/permission-identical. M32 selection digest unchanged.

Both safety stashes untouched: `f93950aab6fdfb40bb100158915ef12692aa1665`, `d979a433a5ab8ae600282048f184eb5fd06a8f17`. New M34 bundle is the only new scientific artifact. Protected hashes/modes in JSON; no cache/handoff/log/NPZ or generated script staged.

## 22. Tests / Ruff / diff / security

- `python -m pytest tests/persistence -v`: **190 passed**, no warnings, 46.36 s.
- `python -m pytest -v`: **993 passed**, six existing Rasterio PendingDeprecationWarnings, 64.61 s.
- `python -m ruff check .`: **PASS**.
- `git diff --check`, staged and both new-file whitespace checks: **PASS before commit**.
- Credential scan of all changed docs/evidence and bundle metadata: **PASS before commit**; no live token/SAS query/signed URL/Authorization header/secret.
- Source/test/config/dependency changes: **0 / 0 / 0 / NONE**. No new decision; Decisions 050/051 scientific bodies identical. These are local results, not CI-success claims.

Scientific network attempts, metadata requests, asset/XML retrieval, signing/token requests and EO bytes downloaded **0**. Only authorized Git initial fetch/final branch push.

## 23. Scientific interpretation / boundary

**No same-pixel candidate recurrence was observed among the 7 target candidate pixels with valid prior observational history.**

7 of 7 target candidates have valid prior observational support; 0 are unevaluable for recurrence. This denominator is distinct from April 3 P/valid-water coverage.

Observed candidate recurrence only, not continuous biological persistence, HAB confirmation, bloom duration, accuracy, risk, confidence, water safety or warning lead time. Shared reference histories are not independent confirmation. No absence-of-HAB, probability/severity/exposure/species/toxin/alert or policy accuracy claim. 25-day gap is not continuous bloom duration; exact-pixel recurrence cannot track motion. Five shared March histories are not statistical sufficiency.

This is engineering acceptance of the frozen observational recurrence product, not biological/event validation. No accuracy, false-positive rate, warning lead time, exposure, species/toxins, water safety or absence-of-HAB claim. UNKNOWN support is not false absence; exact-pixel semantics miss moved/adjacent candidates. Five shared March histories and sparse upstream support remain known limitations; Decision 050 comparative policy validation is REQUIRED / NOT RUN. No thresholds, windows, reference counts, baselines or date choices adjusted.

## 24. M35 NOT STARTED

M31/M32/M33 COMPLETE / MERGED; M34 REAL ENGINEERING ACCEPTANCE COMPLETE. AS-106 is not yet fully closed; M35 owner review/publication/merge/closeout remains **NOT STARTED** and separately gated. AS-107+ **NOT STARTED**; future AS-105 policy validation **NOT RUN**; P1 05.10 **NOT STARTED**. No PR/merge. This task’s authorized M34 evidence commit/push is not M35 closeout.

Execution: 2026-10-10T14:40:31.682184+04:00 → 2026-10-10T14:40:35.235165+04:00 (Asia/Dubai); acceptance bundle finalized 2026-10-10T14:42:10.034770+04:00. Later documentation/Git publication is separate from real execution and does not change its measured result.
