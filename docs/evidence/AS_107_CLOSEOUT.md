# AS-107 M40 — Publication / Closeout Preparation

## Scope and durable closure semantics

M40 / E40 / EV-044, prepared 10 October 2026 (Asia/Dubai), is documentation and
accepted-evidence publication only. No real scoring, upstream processing, parent
reconstruction or scientific-data retrieval occurred. This is not a new policy
or scientific Decision; Decision 053 is absent.

**Current pre-merge state: AS-107 CLOSEOUT READY.**
**M40: PUBLICATION / CLOSEOUT PASS — READY FOR PR.**
The **future closeout PR merge itself** is the durable closure event. After that
merge: **AS-107 COMPLETE / CLOSED; M40 COMPLETE / MERGED / PUBLICATION-CLOSEOUT**.
`closeout_effective_on_merge = true`; no future merge SHA is invented and no
additional documentation loop is needed merely to record that SHA. No M40 PR
or merge was performed here. Owner authorization is required separately.

## Official baseline and verified merged publication chain

Implementation/acceptance baseline:
`2bfbbd63cb5fee8e1d18a0b1099335b924e5ed9d`.
Clean isolated branch `docs/as-107-closeout`, worktree `/workspace/aquasentinel-813-as107-m40`,
created directly from verified origin/main. Active development branch: none.

| PR | Merge commit | Parents, in order | Actual Git committer timestamp |
|---|---|---|---|
| #22 | `49f5276b1ad372725b21cdb2085815225c98eed4` | `6b22d32f078ef80158b2f2d7aac4f3dd07925038` / `5430383611437e939cebce89608c001889eea487` | 2026-10-10T16:15:17+04:00 |
| #23 | `7f304bb44af93d2b3a1a3e6982fefad05fb8f452` | `49f5276b1ad372725b21cdb2085815225c98eed4` / `55533467393f394d6cb3f856b439f41fde4b0148` | 2026-10-10T16:55:09+04:00 |
| #24 | `2bfbbd63cb5fee8e1d18a0b1099335b924e5ed9d` | `7f304bb44af93d2b3a1a3e6982fefad05fb8f452` / `6f2d3d88df6d395f2f2da69a33e30e8163196ca3` | 2026-10-10T17:26:55+04:00 |

All three merges are ancestors of official main. Each has the exact recorded
parents and the same tree as its second-parent PR head. Subjects record PRs
#22/#23/#24; these are verified Git relationships. Timestamps above are Git
committer timestamps, not invented GitHub API merge timestamps.
Decision 052 / M37 is FINAL / FROZEN / MERGED; M38 implementation and
synthetic/adversarial validation are MERGED; M39 real engineering acceptance
is PASS / MERGED. AS-106 remains COMPLETE / CLOSED.
M40/E40/EV-044 were reserved and unused before this task; previous M36–M39
facts remain explicitly historical, not rewritten as though they knew later results.

## Immutable accepted M39 result

Transcribed from committed M39 evidence and its accepted independent oracle,
not recalculated through AS-107 production code.

- Version: `as107-v1`.
- Product: `hab_risk:113143700cb35ac9230d9c54b68b1b53e2573838a4913d4bc942e81c99903fdb`.
- Input fingerprint: `084790273118f50f6c8eaf0ed380dbce730c6dbbd7e4fa0f757c5d145e894d91`.
- Output fingerprint: `25cccf8e8b550a76f28ebb01a2249060de5b1cd3114a7c531ef4775adbc87dae`.
- Score: **29.52380952380953**, exact binary64 hex `0x1.d861861861863p+4`.
- Band: **Watch** under frozen continuous `[25,50)` semantics.
- Evidence completeness: **0.7**; component coverage: **0.7**.
- Assessment: `provisional_observational_screening`.
- Recommendation: **Review on the next valid acquisition**.
- Authoritative region: `hab_geometry:70876fbcb25e8a37abaa238a59e1da32fec9066792e6239db68e284b7bd18682:region:1`.
- Region: **7 pixels; 2,800 m²; 0.0028 km²**.
- Family availability a: **(7, 7, 7, 7, 7)**; family evidence v: **(0, 7, 0, 7, 0)**.

| Driver | Accepted numerator / denominator | Value | Configured weight | Effective available weight | Contribution |
|---|---|---|---|---|---|
| spectral_anomaly | 14 / 35 | 40.0 | 0.35 | 0.5 | 20.0 |
| chlorophyll_red_edge_signal | 7 / 21 | 33.333333333333336 | 0.20 | 0.28571428571428575 | 9.523809523809526 |
| persistence | C/B = 0 / 7; A/B/C = 7/7/0 | 0.0, available | 0.15 | 0.2142857142857143 | 0.0 |
| environmental_context | None | None / unavailable / not_implemented | 0.15 | 0.0 | None |
| intake_exposure | None | None / unavailable / not_implemented | 0.15 | 0.0 | None |

`chlorophyll_red_edge_signal` is the fixed schema name for **red-edge family
evidence breadth**, not measured chlorophyll concentration. Unavailable drivers
remain None, not invented zero-valued scientific measurements.

F_all = 35/35 = 1.0; F_red = 21/21 = 1.0; H = 7/7 = 1.0.
Evidence completeness = **min(0.7, 1.0, 1.0, 1.0) = 0.7**.
Flag: **incomplete_evidence**. Do not add `limited_evidence_completeness`:
0.7 is above the frozen administrative 0.50 threshold.
The site summary selects this sole candidate region; the candidate-conditioned
maximum is not complete operational/intake risk.

## Scientific interpretation and limitations

AquaSentinel produced a **Watch observational screening result** under frozen
AS-107 policy. It remains `provisional_observational_screening`.

**No same-pixel candidate recurrence was observed among the 7 target candidate
pixels with valid prior observational history.** This does not mean no HAB, no
biological persistence, zero environmental risk or safe water.

- Provisional observational screening only; no HAB confirmation or HAB absence confirmation.
- No species/toxin identification, measured chlorophyll concentration, biological probability, calibrated confidence or clinical/environmental truth.
- No water-safety certification, desalination operational safety determination, intake shutdown instruction or complete operational risk.
- No historical accuracy, sensitivity, specificity, false-positive-rate or warning-lead-time validation.
- Exact same-grid persistence only; no motion/current compensation; only the frozen April eligible observations.
- Long observation gap of 25 days + 8 seconds; two observations do not establish continuous biological persistence.
- Five shared historical references are not independent confirmation; sparse/shared historical support is not statistical sufficiency.
- BOA reflectance is not aquatic Rrs; correlated red-edge evidence is not independent corroboration.
- Environmental context and intake exposure are not implemented; only 70% of configured component weight is available.
- Candidate-conditioned site maximum is an observational screening summary, not a complete intake assessment.
- Al Raha is an analyst-defined validation AOI, NOT a confirmed desalination intake.

Evidence completeness and coverage are not biological probability or calibrated
confidence. No sensitivity/specificity/FPR, historical accuracy, confirmed
biological outcome or warning lead time is established by this closeout.

## Anti-outcome-tuning record

1. Decision 052 was frozen before M38 implementation and before M39 real scoring.
2. M38 implemented and synthetic/adversarially validated that unchanged frozen policy.
3. M39 consumed unchanged accepted AS-104/AS-105/AS-106 evidence.
4. The first real result was preserved before inspection and independent oracle validation.
5. The accepted real outcome was Watch = 29.52380952380953.
6. No weight, band, threshold, family definition, candidate policy, recurrence rule or recommendation was changed after seeing the result.
7. Environmental context and intake exposure remained unavailable, rather than being fabricated as zero-valued scientific evidence.
8. The actual outcome was retained, not tuned to create a stronger hackathon demo; reproducibility and scientific restraint are part of the product.

The verified publication order is freeze → implementation/synthetic validation
→ accepted real result → publication → closeout preparation. M39 first call
was 2026-10-10T13:04:58.495566+00:00 to 2026-10-10T13:04:58.732346+00:00
(UTC); the original first-result SHA-256 is
`2bd6c2b10cdca85114ecb63011fbeab684cb173e3b61096dbc51fbb7598a5474`. That record and its pre-score
policy comparison remain historical evidence. M40 only rehashes accepted files;
it does not reconstruct parents or rerun the oracle/scientific calculation.

## Historical M39 engineering integrity

Independent integer/binary64 arithmetic and input/output/product reconstruction:
PASS. Deterministic repeat, caller-order permutation, creation-time exclusion,
full parent-aware validation, immutability/non-aliasing and sealed fresh-process
reconstruction: PASS. Ordinary tamper controls: **13/13 rejected**;
attacker-rehashed controls: **3/3 rejected**. Registry/cache mutation and
scientific network/metadata/asset/EO retrieval: **zero**.
Historical final engineering gate: **292 focused tests, 1,285 full tests**, six
existing Rasterio PendingDeprecationWarnings; Ruff/diff/security/preservation PASS.
These are accepted M39 results, not M40 scientific reruns or GitHub CI claims.

## Read-only external bundle verification

Directory: `/workspace/aquasentinel-acceptance/as107/m39/113143700cb35ac9230d9c54b68b1b53e2573838a4913d4bc942e81c99903fdb`.
Locally verified read-only against accepted hashes; directory mode **0555**,
all three files **0444**. No chmod, rewrite or acceptance regeneration.

| File | SHA-256 | Bytes | Mode |
|---|---|---|---|
| SHA256SUMS.txt | `b71ca40555544202df9a735984901377bd373f625eeb36332807455ce61aa1ab` | 167 | 0444 |
| execution.log | `d77c6307df5363cf43fa62b86e7cc4e6fa224cce4fac7bbe9dda02e34457d54c` | 660 | 0444 |
| real_acceptance.json | `4473db7e589ee80b2e62209d59a7e16c2381a3f4783e5ebba166ccc778af0133` | 121988 | 0444 |

The external accepted result matches the committed accepted result. Existing
sealed bundles, caches, handoffs and recovery artifacts are retained unchanged.

## Preservation evidence

Pre-edit snapshot: **132 tracked files**, **44 protected external file hashes**,
**57 permission records**, and the exact safety-stash inventory. Only the eight
authorized documentation/evidence paths may change; production source, tests,
configuration and dependencies remain byte-identical.

| Frozen scientific/policy section | SHA-256, unchanged |
|---|---|
| Decision 050 | `d3623a363868a57609f50488679ad01ac9df0554b638c489731eab994ae04773` |
| Decision 051 | `4c279549a1c9bd132febcc6fe4cdbd53346cbf8c8cb98a08c3253eb453c02eea` |
| Decision 052 | `a871997701eb5c0069c848f55e45d7d15f2a2e606c712d68a60a1ee54b47cdf5` |

M39 repository MD SHA-256: `344da2c7b9b1ee521dcde273b167a39d4e452f435dfe80036a8af196ff3b3f3f`.
M39 repository JSON SHA-256: `dc97694a9fb1090e30add0d697431bfa9c1eaead783eed7a94050713967cd4c2`.
Both bodies remain byte-identical. Historical sections remain intact apart from
labelling the former current M39 header historical.
Retained safety stashes, unapplied/undropped:
`f93950aab6fdfb40bb100158915ef12692aa1665` and
`d979a433a5ab8ae600282048f184eb5fd06a8f17`.

Final preservation/security audit: **PASS; all 126 untouched tracked files, 44 protected external hashes, 57 modes and both safety stashes unchanged; no signed href/SAS/credentials**.

## M40 engineering quality gates and execution boundary

**1285 full tests PASS (104.18s), six existing Rasterio PendingDeprecationWarnings; Ruff/diff/new-file whitespace/credential/preservation PASS**.
Commands: `python -m pytest -v`, `python -m ruff check .`, `git diff --check`;
new-file whitespace and all-eight-file credential/stable-metadata scans included.
These are repository-local engineering gates; no GitHub CI success is claimed.
Scientific/external-data requests **0**, EO bytes downloaded **0**, real scoring
calls **0**, upstream reruns **0**, parent reconstructions **0**.
Administrative network is limited to initial Git fetch and authorized final push.

## Final presentation handoff

**Problem:** A single satellite anomaly can be scientifically ambiguous and
operationally misleading.

**Design:** Freeze policy before real scoring; combine spectral anomaly evidence,
red-edge evidence breadth and observational persistence; explicitly represent
missing operational components; keep evidence completeness separate from risk score.

**Real result:** Watch = 29.52380952380953; evidence completeness = 0.7;
component coverage = 0.7.

**Why credible:** Policy preceded the result, evidence lineage is reconstructable,
tampering is rejected, and missing components are not fabricated.

**Operational meaning:** Review on the next valid acquisition.

**Scientific restraint:** Provisional observational screening only; field
verification remains the path for biological/operational confirmation.

AS-107 delivers deterministic availability-aware regional/site screening, a
continuous band, reconstructable five-driver explanation, unavailable components,
completeness, coverage, observational persistence, deterministic fingerprints and
provenance, tamper-detectable parent-aware validation, and the accepted Watch example.
It does not establish biological truth, calibrated probabilities, measured
chlorophyll, species/toxins, accuracy, water safety, shutdown criteria or lead time.
Suggested visual: five-driver table, separate screening/completeness/coverage cards
and verified publication chain. **Proposed only; no screenshot/visual claimed to exist.**

## Forward boundary and publication status

**AS-108 NOT STARTED.** Any AS-108 validation requires separate owner authorization.
Future AS-105 policy validation and P1 homogeneous 05.10 robustness NOT STARTED.
No Decision 053. Owner review of this closeout is next; no automatic next-stage start.

AS-107 before future closeout merge: **CLOSEOUT READY**.
AS-107 after future closeout merge: **COMPLETE / CLOSED**.
M40: **PUBLICATION / CLOSEOUT PASS — READY FOR PR**.
M40 PR: **NONE CREATED**. M40 merge: **NONE PERFORMED**.
