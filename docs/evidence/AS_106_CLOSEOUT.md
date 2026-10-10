# AS-106 M35 — Publication / closeout preparation

## 1. Scope and durable closure semantics

**M35 / E35 / EV-039: PUBLICATION / CLOSEOUT PASS — READY FOR PR.** This is documentation/evidence only, using merged M34 as authoritative. **Before closeout merge: AS-106 CLOSEOUT READY.** `closeout_effective_on_merge = true`: when this branch is merged, that merge itself makes AS-106 **COMPLETE / CLOSED** and M35 **COMPLETE / MERGED / PUBLICATION-CLOSEOUT**. No additional post-merge edit solely to record a merge SHA is required. Official main is not claimed closed before that merge.

Prepared on `docs/as-106-closeout`, from official acceptance baseline `82e30c00a30ed893ad47c44c5a1e363661370d35`, in `/workspace/aquasentinel-813-as106-m35`. Current active development branch: none; AS-107+ NOT STARTED / NOT AUTHORIZED. No new scientific result, recurrence run, upstream extraction, EO/network research, policy change, PR or merge.

## 2. Verified publication / merge chain

| Milestone | PR | Merge SHA | Git commit time (Asia/Dubai) |
| --- | --- | --- | --- |
| Decision 051 design freeze | 16 | 57185444f0cc963cc899a25cd8179d7a31f12119 | 2026-10-10T11:21:58+04:00 |
| M31 implementation | 17 | 723e13a900dba30b73a8a2da39df1d984233a2f4 | 2026-10-10T12:13:05+04:00 |
| M32 metadata inventory | 18 | 200affdb7fb6f8801744a192511e4200cc0d100d | 2026-10-10T13:35:36+04:00 |
| M33 April 3 preparation | 19 | 4cde14ee448079163c2a08f3951f8dac294f8dac | 2026-10-10T14:22:32+04:00 |
| M34 real engineering acceptance | 20 | 82e30c00a30ed893ad47c44c5a1e363661370d35 | 2026-10-10T14:52:49+04:00 |

All five commits verified as ancestors of official base, with matching Git merge subjects and two-parent records. Times are Git commit timestamps; no separate GitHub API timestamp claim. M31 implementation, M32 selection, M33 upstream preparation and M34 real acceptance are COMPLETE / MERGED. Decision 051 original body unchanged, FINAL / FROZEN / MERGED via PR #16. No Decision 052 for administrative closure.

## 3. Authoritative accepted real result

- **Version:** `as106-v1`
- **Product:** `hab_persistence:c576478b6b6d85894e5317e65a1d0fd6cee38ed1c406d452b10f97712d2cc3bb`
- **Input fingerprint:** `2f8f6f1c37bd9f8a236109ab821e6e426f222840c4a74f623d2e78bd76529ab7`
- **Output fingerprint:** `7739a3f97c0e88113a17629678a0ef31bdb14594400f0568c0dfdfdb5dabafef`
- **M32 selection digest:** `570792066c1997b9a403249d994c4e7367bf2f1dafc6473b6e30df20cd6481d5`

Frozen acquisition sequence UTC: **2023-04-03T06:46:21.024000Z → 2023-04-28T06:46:29.024000Z**.

| Population / metric | Accepted value |
| --- | --- |
| P: target AS-105 policy support | 802 |
| Q: target P with valid prior support | 793 |
| A: target candidates | 7 |
| B: target candidates with valid prior support | 7 |
| C: recurrent target candidates | 0 |
| Candidate-history coverage B/A | 7/7 = 1.0 |
| Recurrence C/B | 0/7 = 0.0 |
| Streak histogram on A | 1 → 7 |
| Observation gap | 2,160,008,000,000 µs = 25 days + 8 seconds |

No measured count, timestamp, identity, denominator or interpretation changed. The single authoritative target region remains seven pixels, history-evaluable 7, recurrent 0, maximum/median streak 1/1.0; recurrent-span summaries None.

## 4. Final scientific statement and limitations

> No same-pixel candidate recurrence was observed among the 7 target candidate pixels with valid prior observational history.

- Exact same-grid pixel recurrence only; no neighborhood, motion or current compensation.
- Unsupported earlier observations are UNKNOWN, not negative.
- Only two April observations were eligible under the frozen contract; both retained.
- Gap is 25 days + 8 seconds; it does not imply continuous biological presence or absence.
- Shared five March references are not independent confirmation; five histories are not statistical sufficiency.
- April 3 ~13% upstream policy coverage is a separate denominator from 7/7 target-candidate history coverage.
- Zero observational recurrence is not absence-of-HAB evidence.
- Spectral candidate geometry does not identify species/toxins.
- AS-106 supplies no operational risk/confidence/probability/water-safety decision.
- Decision 050 comparative policy validation remains REQUIRED / NOT RUN.

No claim that HAB was absent/disappeared, bloom ended, water was safe, an event was false/disproved, biological persistence was zero, risk/confidence was low, or operational concern disappeared. Candidate recurrence is an observational statistic, not biological truth, severity, accuracy, false-positive rate or warning lead time.

## 5. Anti-cherry-picking audit / presentation story

1. Metadata froze the sequence before recurrence inspection.
2. Every eligible April acquisition was retained: April 3 and April 28.
3. Both dates shared the same frozen temporal comparison contract.
4. April 3 produced 88 AS-105 candidates.
5. April 28 produced 7 AS-105 candidates.
6. Real AS-106 produced zero same-pixel recurrence.
7. Zero was retained without tuning.
8. No date, threshold, family rule, connectivity or spatial tolerance changed.

**Problem:** a one-date spectral anomaly can mislead. **Design:** freeze eligible dates first, use valid-observation-aware exact-pixel recurrence and keep unavailable history UNKNOWN. **Real result:** all seven April 28 candidates had valid April 3 history, but none was a candidate at the same pixel on April 3. **Why it matters:** zero was preserved instead of adjusting policy to produce a stronger demo. **Claim:** reproducible observational recurrence logic. **Not established:** biological persistence/absence or HAB confirmation. No visual/screenshot is claimed created.

## 6. Accepted M34 engineering integrity — not rerun in M35

- Four accepted typed AS-104/105 parent reconstructions and common comparison contract: PASS.
- Independent scientific array and dtype reproduction: **9/9 + 9/9 PASS**.
- Boolean/global/time/region and exact observation-gap oracles: PASS.
- Product scene.validate(), same/reversed-order repeats and caller-order independence: PASS.
- Product identity, input/output fingerprints and created_at exclusion: PASS.
- Parent immutability and output non-aliasing: PASS.
- Seven tamper controls, including altered science with recomputed output fingerprint: REJECTED / PASS.
- Sealed typed acceptance-bundle fresh offline roundtrip: PASS.
- M34 scientific network requests/downloads/signing: ZERO.

These statements reference immutable [M34 JSON](AS_106_REAL_ACCEPTANCE.json)/[M34 record](AS_106_REAL_ACCEPTANCE.md), not new M35 computations or biological accuracy claims. Historical M34 gates: 190 focused/993 full tests, six existing Rasterio warnings; Ruff/diff/security PASS.

## 7. Acceptance bundle reference / local read-only verification

- **Directory:** `/workspace/aquasentinel-acceptance/as106/m34/c576478b6b6d85894e5317e65a1d0fd6cee38ed1c406d452b10f97712d2cc3bb`

| File | Bytes | Accepted SHA-256 | Mode |
| --- | --- | --- | --- |
| SHA256SUMS.txt | 255 | 793f29341bbdc057b9198ffd65c7714829e8373c901ea39fd5a7c773584c674d | 0444 |
| execution.log | 1335 | f8ed67c9198c6b415a9369a4659ec5527dc18a2f262a92f7087f44bdaf4c80c7 | 0444 |
| real_acceptance.json | 58486 | feb7b974126b2e5ad518febc053494db6d1824badf2fe0db04103e83ecb72d90 | 0444 |
| scientific_arrays.npz | 6527 | 6ba3d54f056717e9fe4f11f8c58ef649555d781792edd9ac49a40571b442fc19 | 0444 |

Directory **0555**. All four files locally rehashed and SHA256SUMS entries checked read-only during M35: **PASS**. No NPZ loading, array reconstruction, science/validator execution, rewriting or chmod. Bundle not in Git and unchanged.

## 8. Preservation and change scope

Before editing: 115 tracked-file hashes; 41 protected external-file hashes and 53 mode records. All existing source/tests/config/dependencies, seven accepted AS-102 caches, AS-104 handoff/M29/M33 handoff/M34 bundle, M32/M33/M34 evidence and recovery artifacts preserved. Only the eight authorized closeout documentation/evidence paths change.

Safety stashes untouched: `f93950aab6fdfb40bb100158915ef12692aa1665` and `d979a433a5ab8ae600282048f184eb5fd06a8f17`. Decisions 050/051 full scientific sections byte-identical; no Decision 052. Historical M31–M34/E31–E34/EV-035–EV-038 bodies retained; current-status header relabelled historical where needed. No accepted evidence rewritten to imply advance knowledge of later results.

## 9. M35 quality gates and network audit

M35 final engineering gates: **PASS**.

- `python -m pytest -v`: **993 passed**, six existing Rasterio PendingDeprecationWarnings, 64.16 seconds.
- `python -m ruff check .`: **PASS**.
- `git diff --check` and both new-file whitespace checks: **PASS**.
- Credential scan of all eight authorized files: **PASS**, no live SAS/signed URL/Authorization header/secret.
- Current-status consistency and historical preservation audit: **PASS**.
- Source/test/config changes: **0**; dependency changes: **NONE**.
- 109 untouched tracked-file hashes, 41 external hashes, 53 mode records and the stash inventory: unchanged.

Only initial Git fetch and final authorized closeout branch push. Scientific/external-data requests **0**, EO/metadata/raster/XML downloads **0**, signing/token requests **0**, new real recurrence/upstream executions **0**. The explicitly authorized existing pytest suite is a separate engineering gate, not a real M34 rerun. No dependency setup change or web research.

## 10. Forward handoff and publication stop

AS-106 provides **observational recurrence evidence, target candidate history coverage, exact streak/timing evidence and provenance**. It provides **no risk, confidence, probability, HAB confirmation, biological persistence or operational decision**. Future AS-107 must consume evidence with its denominators/UNKNOWN/time/spatial limits intact and must not reinterpret recurrence as biological truth. Separate owner design review and implementation authorization required; no AS-107 design/implementation begins here.

Before merge: **AS-106 CLOSEOUT READY**, M35 preparation complete/pending merge. After future closeout merge: **AS-106 COMPLETE / CLOSED**, M35 complete/merged/publication-closeout. No future merge SHA placeholder or extra documentation loop required. Stop after this task’s commit/push: no PR or merge. AS-107+ **NOT STARTED**; future AS-105 policy validation **NOT RUN**; P1 05.10 **NOT STARTED**.
