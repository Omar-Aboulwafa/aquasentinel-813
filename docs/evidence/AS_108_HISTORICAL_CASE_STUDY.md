# AS-108 M44 — Retrospective HAB Historical Case Study

## Result and scope

**M44 / E44 / EV-048: retrospective case-study reporting COMPLETE.**
**AS-108 P0: RETROSPECTIVE OBSERVATIONAL-CONSISTENCY CASE STUDY COMPLETE WITH POST UNAVAILABLE.**
Frozen Decision 053 category: **PARTIALLY_CONSISTENT**.
Both retained EVENT observations are evaluable and have positive candidate evidence.
Required POST geometry context is unavailable; it is retained without substitution.
This is qualified month/area observational correspondence, not biological validation.

Reporting uses **REUSED_ACCEPTED_EVIDENCE** only. **M44_REPORTING_DERIVATION** is
limited to denominators, scalar/count proportions, frozen predicate evaluation,
PRD answer statuses and the semantic digest. No scientific module was invoked on
accepted scenes; no new score, pixels, XML, geometry or persistence product.
Engineering tests exercise the existing synthetic/local fixtures separately.

Official main/base: `865cd14398c6bcdbeaed6a19210f5615beb638e6`, PR #27 merge; exact parents
`8bb56f12f2cd683d4a96f069c5d049bf4a39799e` and
`e76d042d1ddefe4c2d78b6fc585f8b65a5a4fff0` verified from Git.
Decision 053/M42 merged through PR #26; M43 complete/merged through PR #27;
AS-107 COMPLETE / CLOSED. Isolated branch `data/as-108-case-study`, worktree
`/workspace/aquasentinel-813-as108-m44`, clean before work. M44/E44/EV-048 were
unused; earlier M44 references were future plans. No Decision 054.

## Documentary reference, separate from satellite inference

Reuse [M42 event reference](AS_108_DESIGN_FREEZE.json), `/event_reference`, exactly.
EAD **Marine Water Quality Report 2023**, official Marine Water Quality category,
listing publication **21 November 2024** (reporting year 2023, not publication year).
The supplied verified summary records 23 Abu Dhabi algal bloom incidents in 2023
and one Raha Beach Red Tide incident in April. The 23 incidents are documentary
context, not a labeled validation dataset.

Verification status **EXTERNALLY_VERIFIED_FACTS_SUPPLIED_BY_OWNER**: the project
owner supplied externally verified official listing/PDF facts in M42; Codex did
not independently retrieve or inspect the source during M42 or M44. The record
does not claim the owner personally conducted inspection. Outside access timestamp,
page/section, event start/end and precise geometry remain null, not invented.

Event reference ID: `ead-raha-beach-red-tide-2023-04`.
Timing **MONTH_LEVEL**, documented month **2023-04**, biological onset unknown.
Lead-time status **MONTH_LEVEL_ONLY**; exact warning lead time **NOT ESTIMABLE**.
Location **Raha Beach**, spatial precision **AREA_LEVEL_ONLY**. AOI relationship
**AREA_LEVEL_CONTEXTUAL_ALIGNMENT**; unchanged analyst Al Raha AOI is not the
EAD incident/sampling footprint or a confirmed desalination intake.

**Pseudo-nitzschia multistriata** is EAD's external species reference, never a
satellite inference. **Domoic acid** is the externally reported species-associated
toxin; incident-specific measured concentration **NOT ESTABLISHED**. AquaSentinel
species and toxin inference **NONE**. No documentary request made in M44.

## Fixed phases and units

| Phase | Inclusive start UTC | Exclusive end UTC | Interpretation |
|---|---|---|---|
| PRE | 2023-03-01 | 2023-04-01 | Descriptive pre-month March references |
| EVENT | 2023-04-01 | 2023-05-01 | Both retained event-month observations |
| POST | 2023-05-01 | 2023-06-01 | Required analytical phase; unavailable metadata outcome |

One `event_case` is the primary unit. Acquisition, region and pixel support are
secondary reporting units. PRE/POST are calendar roles, not biological-negative
labels. Pixels are not independent biological samples or accuracy denominators.
Shared grid is the accepted EPSG:32640, 20 m, 310x228 contract; no grid recreated.
AOI identity/digest and grid reference remain those frozen in M43.

## PRE reconstruction — five descriptive records

All five accepted AS-103 records have nonempty feature support and accepted
reconstruction PASS. Highest observation-target stage is **AS-103**; later temporal
products consume these records as reference parents, not as independently scored
March targets. No PRE Normal, candidate, risk or biological-negative result inferred.

Feature-count order: ndci_like / mci_like / red_edge_red_ratio /
red_edge2_red_ratio / green_red_ratio / green_blue_ratio.

| UTC acquisition | AS-102 valid water | Six feature-valid counts | Evaluable |
|---|---:|---|---|
| 2023-03-04T06:47:51.024000Z | 8674 | 8622 / 8674 / 8622 / 8622 / 8622 / 8674 | yes |
| 2023-03-09T06:47:19.025000Z | 2092 | 2092 / 2092 / 2092 / 2092 / 2092 / 2092 | yes |
| 2023-03-14T06:46:41.024000Z | 7350 | 7350 / 7350 / 7350 / 7350 / 7350 / 7330 | yes |
| 2023-03-24T06:46:21.024000Z | 3834 | 3834 / 3834 / 3834 / 3834 / 3834 / 3834 | yes |
| 2023-03-29T06:46:29.024000Z | 6156 | 6156 / 6156 / 6156 / 6156 / 6156 / 6156 | yes |

Support counts come from AS-104 acceptance's second JSON fence (index 1),
`/references/<index>/as102_statistics` and `/feature_statistics`; exact AS-102 /
AS-103 IDs and AS-103 input fingerprints agree with M33
`AS_106_APRIL3_UPSTREAM_PREPARATION.json`, `/march_reference_reconstruction`.
The [case JSON](AS_108_HISTORICAL_CASE_STUDY.json) copies identities, counts,
source/discovery distinctions, lineage edges and per-record source locators.

- **2023-03-04**: AS-102 `optical:038a425d46eead247826c4e1e735851a50325d896f1c95b99258840285bf31e1`; AS-103 `spectral:6409add4aef5c95cfe773bfabfa1f554bdda2968241712bda4debefa34b57130`; accepted AS-103 input fingerprint `187251ea126ffdf774b5d347d2af23f7b693b5d947a7ed49e5d6c3cf694c0166`.
- **2023-03-09**: AS-102 `optical:a412b51188a9c47a0f121a5882fbf464490a66d19a96d3f682c0955398193644`; AS-103 `spectral:dafde3d3a2a94d44b62a9d5605bce497b03021e517b7dd6b081607719f37efa1`; accepted AS-103 input fingerprint `0a61a0afa5254da8959d38135d967d664debfa45b8aea4f3070608dd8dd198b8`.
- **2023-03-14**: AS-102 `optical:91cd94459703fb64b6c982d0d61403dcea8e766a99796b01d591d9ab6b9a67c2`; AS-103 `spectral:721d847a7ed032426c8124e42507b60c3f9a6ae86a4e9ad406176646c35abff7`; accepted AS-103 input fingerprint `89311bd86000b4c7a60e1839040022d64c5a45715e3c5fc3a5392c6bc9592462`.
- **2023-03-24**: AS-102 `optical:f812d226e81f482d912b0f0450ec3623e8a707f3a1774aaeaba2b27080b03ad2`; AS-103 `spectral:1002b083b3d7637abd67446ef171e0746fe3bd839706cadff18571ac1c51af66`; accepted AS-103 input fingerprint `2d56879067af2cf99a854725edd38627fdbbcee56345f422e2ba477e509d1898`.
- **2023-03-29**: AS-102 `optical:45360cce80a32aba72c755a3110b865575cc65d45eb96a27922f2dbc93d3aeee`; AS-103 `spectral:c4de2a86bb7b15a6a8bc49373823bb944be7e6787db383b0959c93c51f3464d5`; accepted AS-103 input fingerprint `02e8cbea849befda080e04d63bb8dd37ebb89ecd16b0fc5d4aef92976c9757bd`.

## EVENT reconstruction and immutable lineage

### 2023-04-03 — accepted through AS-105

- AS102: `optical:441badc774727bcff001ccb02e8e936988b819db8cecc3a247d5d80572ec6499`.
- AS103: `spectral:6bb1ee8db74f19f7fd03e1fd72c99d1c6fee88c6367b970913e341b55fa8a73c`.
  input_content_fingerprint: `3514eae5b3356531d40357feade7f1c1b1e6728451a9bd19b2920d23ea3f99ce`.
- AS104: `temporal:71f6be2d8437e91f7cf213df0bd876897febebe630a02a20bb151a5d852edb11`.
  output_content_fingerprint: `949d75aa4642dd2680e0428265da423a8cb855f6965ed30f831b3c91ddf80a92`.
- AS105: `hab_geometry:7e3a4ba3ba8fb394ca874415c62f7fed7a160609c6dee458d59b35ea0c12cd52`.
  input_content_fingerprint: `b8bbe965ed3b57e8abbbaa5560784b274b89e9657e3cffb9b378c805f1021a24`.
  output_content_fingerprint: `ecea6b13cded3553b5d4e8e373e9b8749e3584aba943e808cee4b057b8b731c9`.

Accepted AS-105 **P = 794**, **candidates = 88**, **regions = 15**.
Target valid water 6096; P/water **794/6096**; candidates/P **88/794**. These are support diagnostics, not biological sample sizes.
Total projected-grid candidate area **35200.0 m² / 0.0352 km²**; not confirmed bloom extent.
AS-105 valid parent-aware accepted evidence and P>0: **True**. Candidate count>0: **True**.

| Family | Available policy support | Evidence pixels | Evidence/support |
|---|---:|---:|---|
| red_edge_b5_vs_red | 794 | 5 | 5/794 |
| red_edge_b6_vs_red | 793 | 0 | 0/793 |
| red_edge_line_height | 794 | 272 | 272/794 |
| visible_green_vs_blue | 789 | 151 | 151/789 |
| visible_green_vs_red | 793 | 1 | 1/793 |

Largest region: 66 pixels / 26,400 m². Ten one-pixel regions are retained, not
filtered away. Four other small regions plus the largest and single pixels total
15 regions / 88 pixels / 35,200 m². Most regions are F2/F5; one is F1/F2.
Immediate lineage: actual PC → AS-102 → AS-103 → AS-104 → AS-105; chronological
March AS-103 references also parent the AS-104 product. Exact source IDs,
fingerprints, family counts and regional deviation/rank summaries are copied from
M33 JSON `/as102`–`/as105`, with typed-parent validation PASS. No AS-106 or AS-107
April 3 result exists in accepted evidence; score/band remain null, not zero/Normal.
### 2023-04-28 — accepted through AS-107

- AS102: `optical:0725a908d21cd655e83f70d2bb11247dc0f1516f0c00ea275efc3239113ee4a6`.
- AS103: `spectral:dae91b4dda0131ca2d2987321abd2ffd5c4b5ffb2e95a44880b7a5f9a67ea64b`.
  input_content_fingerprint: `e76edf08917ef02cfdb544d811fe6df79ea29f014842be5d29fbb03645d475d7`.
- AS104: `temporal:e814b0574ab30d1841778ee3c5005ffcb313ab42473c41acc028f0a9f7804a8b`.
  output_content_fingerprint: `2a2902f946d49487f1416d0bd6ad73c7976910fe72060f03503540a49e2678dd`.
- AS105: `hab_geometry:70876fbcb25e8a37abaa238a59e1da32fec9066792e6239db68e284b7bd18682`.
  input_content_fingerprint: `c50d9f6300060ab9f194c1a0b8808de340eb53326268a52ef083ad7f994b2bc5`.
  output_content_fingerprint: `ff976ec800ec2dfc966e4f373dd3f2442938a06a10254dd4ea7a86280dd0a765`.
- AS106: `hab_persistence:c576478b6b6d85894e5317e65a1d0fd6cee38ed1c406d452b10f97712d2cc3bb`.
  input_content_fingerprint: `2f8f6f1c37bd9f8a236109ab821e6e426f222840c4a74f623d2e78bd76529ab7`.
  output_content_fingerprint: `7739a3f97c0e88113a17629678a0ef31bdb14594400f0568c0dfdfdb5dabafef`.
- AS107: `hab_risk:113143700cb35ac9230d9c54b68b1b53e2573838a4913d4bc942e81c99903fdb`.
  input_content_fingerprint: `084790273118f50f6c8eaf0ed380dbce730c6dbbd7e4fa0f757c5d145e894d91`.
  output_content_fingerprint: `25cccf8e8b550a76f28ebb01a2249060de5b1cd3114a7c531ef4775adbc87dae`.

Accepted AS-105 **P = 802**, **candidates = 7**, **regions = 1**.
Target valid water 7963; P/water **802/7963**; candidates/P **7/802**. These are support diagnostics, not biological sample sizes.
Total projected-grid candidate area **2800.0 m² / 0.0028 km²**; not confirmed bloom extent.
AS-105 valid parent-aware accepted evidence and P>0: **True**. Candidate count>0: **True**.

| Family | Available policy support | Evidence pixels | Evidence/support |
|---|---:|---:|---|
| red_edge_b5_vs_red | 802 | 3 | 3/802 |
| red_edge_b6_vs_red | 801 | 0 | 0/801 |
| red_edge_line_height | 802 | 37 | 37/802 |
| visible_green_vs_blue | 797 | 1 | 1/797 |
| visible_green_vs_red | 801 | 47 | 47/801 |

One eight-connected region, a MultiPolygon with three four-connected parts,
7 pixels / 2,800 m² / 0.0028 km²; no one-pixel region. F2/F4 evidence agreement.
The locally verified accepted M29 `real_acceptance.json` supplies the complete
geometry statistics, family and regional feature summaries. SHA-256:
`4ee7496b9537e80523d1e92ecee0b9cccce98fb5b3f293d7db279479076aec6a`.
Committed M29 MD, M34 JSON and M39 parent-reconstruction evidence corroborate the
same product/witness relationships. This file is read-only; no geometry recomputed.

Accepted AS-106 immediate parents are April3 AS-105 then April28 AS-105;
AS-107 immediate parents are target April28 AS-105 and accepted AS-106. No lineage
shortcut to raw source. Exact IDs/fingerprints remain in the case JSON.

Accepted Watch score **29.52380952380953**, evidence completeness **0.7**,
component coverage **0.7**, `provisional_observational_screening`, recommendation
**Review on the next valid acquisition**. Reused, not rescored.

| Driver | Evidence numerator/denominator | Accepted value | Accepted contribution |
|---|---|---:|---:|
| Spectral anomaly | 14/35 family-pixel evidence | 40.0 | 20.0 |
| Red-edge family evidence breadth | 7/21 | 33.333333333333336 | 9.523809523809526 |
| Persistence | C/B = 0/7 | 0.0 | 0.0 |
| Environmental context | unavailable / not_implemented | null | null |
| Intake exposure | unavailable / not_implemented | null | null |

Frozen raw weights 0.35/0.20/0.15/0.15/0.15; available configured weight
0.7/1.0, effective weights 0.5/0.28571428571428575/0.2142857142857143/0/0.
F_all=35/35=1, F_red=21/21=1, H=7/7=1; completeness
min(0.7,1,1,1)=0.7. `incomplete_evidence` remains; no invented limited-completeness
flag. Red-edge and spectral drivers overlap/correlate, not independent corroboration
or measured chlorophyll.

Persistence **A/B/C = 7/7/0**: seven target candidate pixels, all seven prior-history
evaluable, none with exact-grid candidate recurrence. B/A=7/7; C/B=0/7.
**No same-pixel candidate recurrence was observed among the 7 target candidate
pixels with valid prior observational history.** This does not imply no HAB,
no biological persistence, safe water or zero environmental risk. Exact-grid
recurrence has no motion/current compensation; 25-day+8-second gap is sparse
sampling, not continuous biological monitoring. Candidate presence on both April
acquisitions is different from same-pixel recurrence or biological persistence.

## POST reconstruction — retain the inconvenient missing phase

M43 merged evidence: provisional CDSE identity
`S2A_MSIL2A_20230503T064621_N0510_R020_T40RBN_20240903T135841`,
**2023-05-03T06:46:21.024000Z**, sentinel-2a, tile40RBN/orbit20,
CDSE cloud metadata **0.57%** (not AOI cloud fraction).
PC ID/baseline null; selection **UNAVAILABLE**, **ZERO_EXACT_PC_05_09_MATCHES**.
Selection SHA-256:
`df487999defada56023a7e76be69c507b2b1ff11d81de1480737eca86a1ad4de`.

M43 six-page inventory: 26 provider records / 26 distinct acquisition keys /
13 timestamps; four pass CDSE eligibility, only earliest queried on PC, zero exact
PC05.09 matches. Full compatible N_metadata_eligible unknown, not four or zero.
Later May8/13/28 PC compatibility is not assessed or substituted.
No POST pixels, AS-102+ scientific product, geometry, risk band, negative label or
recovery interpretation. `retained_required_post_slot=1`, `usable_post_observation=0`.
N_retained is null/NO_SUCCESSFULLY_SELECTED_COMPATIBLE_OBSERVATION; the provisional
metadata identity is not promoted to a retained usable scientific scene.

## Phase denominators — acquisition counts, explicit scope

PRE/EVENT inventory is accepted retained-cohort evidence, not a newly proven
full-calendar discovery survey; N_discovered/provider/full-compatibility counts
are null with reason. POST complete CDSE inventory is reused from M43; full PC
compatibility count remains null because only the earliest was assessed.
N_processing_attempted means new science in M44, not accepted-product reuse.
N_unavailable concerns required endpoint/slot, not every unselected inventory row.
PRE candidate/scoring NOT_APPLICABLE is not a measured zero/negative.

| Count | PRE | EVENT | POST |
|---|---|---|---|
| N_discovered | null (unknown/not selected) | null (unknown/not selected) | 26 |
| N_provider_records | null (unknown/not selected) | null (unknown/not selected) | 26 |
| N_metadata_eligible | null (unknown/not selected) | null (unknown/not selected) | null (unknown/not selected) |
| N_processing_attempted | 0 | 0 | 0 |
| N_evaluable | 5 | 2 | 0 |
| N_unavailable | 0 | 0 | 1 |
| N_candidate_geometry | NOT_APPLICABLE | 2 | 0 |
| N_scored | NOT_APPLICABLE | 1 | 0 |
| N_watch_or_higher | NOT_APPLICABLE | 1 | 0 |
| N_retained | 5 | 2 | null (unknown/not selected) |
| N_reused_accepted | 5 | 2 | 0 |

POST additional bookkeeping: CDSE-eligible-before-PC=4, one required POST slot,
zero usable POST observations, one reused metadata-selection record, zero reused
scientific observations. No May processing attempt occurred.

- PRE descriptive evaluability **5/5** retained records.
- EVENT evaluability **2/2**; positive candidate geometry **2/2** evaluable acquisitions.
- EVENT Watch-or-higher **1/1** accepted scored acquisition; **1/2** retained EVENT
  acquisitions with one unscored. The latter is availability-inclusive, not one Normal.
- POST evaluability **0/1 required slot**, not a biological negative. Candidate/scoring
  fractions **0/0 unavailable**, not a reported zero percentage; no usable retained scene.

Feature support, AS-105 P, AS-106 B/A and C/B, and AS-107 completeness/coverage
have separate denominators. None is event sensitivity, specificity or population accuracy.

## Frozen category decision trace

Integrity gate: accepted parent-aware validations PASS, IDs/fingerprints and
cross-artifact scalars agree; protected artifact hashes/modes verified. No production
parent reconstruction or scientific validation function was rerun.
Supplied verified documentary reference is provided (not newly retrieved).
All five PRE records evaluable; April3 and April28 geometry endpoints evaluable
and positive; POST endpoint not evaluable; inventory scope/missingness disclosed.
Required_context_complete = false, because POST lacks its geometry endpoint.

| Precedence | Predicate evaluated from evidence | Result |
|---|---|---|
| UNAVAILABLE | zero evaluable EVENT or documentary reference not provided | false |
| INCONCLUSIVE | at least one evaluable EVENT but none positive | false |
| PARTIALLY_CONSISTENT | positive EVENT evidence and incomplete required context | true — selected |
| CONSISTENT | both EVENT evaluable/positive and complete required context | false |

**PARTIALLY_CONSISTENT**: both retained event-month observations show accepted
candidate evidence, with April28 Watch, but missing POST limits the case to qualified
month/area observational correspondence. It is not biological truth or predictive
validation. The machine trace references each predicate's accepted evidence.

## PRD questions — bounded answers

- **Q1 — SUPPORTED**: Both retained EVENT acquisitions have accepted frozen-policy candidate anomaly evidence (April3 88/P794; April28 7/P802). This is not a statistical significance test or confirmed HAB.
- **Q2 — SUPPORTED**: Accepted temporal deviations and family evidence explain the selected candidates: April3 predominantly F2/F5, with one F1/F2 region; April28 F2/F4. Descriptive family evidence is not measured chlorophyll; red-edge and spectral components overlap.
- **Q3 — PARTIALLY_SUPPORTED**: Candidate presence exists in both retained April acquisitions, but accepted exact-grid recurrence is 0/7 with history coverage7/7 over25days+8seconds. Biological persistence, motion-tracked continuity and POST/recovery are not established.
- **Q4 — PARTIALLY_SUPPORTED**: April28 accepted Watch29.52380952380953 is supported. April3 has no accepted AS107 score or band; do not infer one.
- **Q5 — NOT_ESTIMABLE**: Exact onset-relative warning lead time is not estimable from month-level event timing. April3 is earliest evaluable candidate evidence among the two retained event-month observations, not a claim about all April acquisitions or days before onset.

Q1/Q2/Q3 reuse M33 AS-105 and M29/M34 evidence; Q4 reuses M39 immutable result;
Q5 uses M42 documentary precision. Detailed per-question sources are the corresponding
observation evidence references in JSON. No statistical-significance claim is made.

## Retrospective integrity and scientific limitations

April3/28 scientific outputs were known before Decision053. This case is not blind,
prospective or independently preregistered validation of those April outcomes.
Decision053 reporting categories were frozen before any new May metadata selection;
M43 retained the unavailable POST result without substitution. This supports process
integrity / anti-cherry-picking discipline, not predictive performance, independent
model validation or unbiased accuracy. No later outcome changed criteria, policy,
AOI, thresholds, dates, weights, bands, family definitions or recommendations.

Month-only timing and area-only location cannot establish exact onset, footprint,
lead time or biological pixel agreement. One retrospective event cannot yield
sensitivity/specificity/FPR/precision/recall/ROC-AUC/population accuracy. PRE is
not a negative-control group. Use unmatched_observational_anomaly unless independent
biological reference supports a false-positive label.

Conservative coastal/cloud masks and sparse five-history support remain; April28
P/water=802/7963 (roughly10%), April3=794/6096. Five shared historical observations
are not statistical sufficiency or independent confirmation. Small positive scales
can produce large robust-z magnitudes. BOA is not aquatic Rrs; correlated red-edge
features are not independent corroboration. Exact-pixel recurrence lacks motion
compensation, with sparse long gaps. Environmental context/intake exposure remain
unimplemented; only0.7/1.0 configured weight is available. Heuristic PoC weights
are uncalibrated; candidate-conditioned site maximum is an observational summary.
Al Raha is an analyst-defined validation AOI, not a confirmed desalination intake.

Forbidden: satellite HAB/species/toxin confirmation, measured chlorophyll, biological
probability/calibrated confidence, biological accuracy metrics, biological absence/
recovery, safe/unsafe water certification, shutdown advice or unknown-onset exact
lead time. Watch is a monitoring-priority result: Review on the next valid acquisition.
No same-pixel recurrence is not proof of no HAB or no biological persistence.

## Semantic digest and source accountability

Schema **as108-m44-case-study-v1**; SHA-256 **`ccc5f04f304a8b4bb8a367331069a5ca54776433e7c0fea0c67d662e68e0772a`**.


Hash only JSON `semantic_payload`, using sorted keys, compact comma/colon separators,
allow_nan=False, ensure_ascii=True, UTF-8 and one trailing LF. Arrays retain frozen
chronological order. Includes documentary semantics, phase windows, retained exact
identities/IDs/fingerprints, source evidence hashes, M43 digest/missingness, denominators,
question statuses, category/predicates and material limitations. Excludes creation/
publication time, the new Git commit SHA, display-only question prose and volatile
engineering environment metadata. Independent reconstruction/repeat is an engineering
gate; this digest is a report identity, not a new scientific product.

Every reused observation carries accepted source path/hash/locator. Scalar records
are copied, not rescored. April28 M29 external JSON was locally available and its
accepted hash verified; complete accepted scientific artifacts remain protected.
Unknown values remain null; JSON contains no NaN/Infinity or signed credentials.

## Preservation, engineering gate and network boundary

Engineering gates: **1285 full tests PASS (100.78s)**; six existing Rasterio
PendingDeprecationWarnings; Ruff PASS; diff/new-file whitespace PASS; strict finite
JSON, independent digest/repeat, predicate, credential and preservation checks PASS.
Engineering fixtures attempted no external network; no GitHub CI success claimed.

Decisions050–053 whole frozen sections, all source/tests/config/dependencies,
M39 accepted evidence, M42/M43 evidence and other upstream artifacts unchanged.
External preservation inventory:44 file hashes /57 modes; both known safety stashes
retained without apply/drop. No raster/cache scientific product created.
Documentary/CDSE/PC metadata/EO assets/EO raster bytes/real scientific compute:
**0/0/0/0/0/0**. Allowed Git operations are recorded separately in the task report;
no provider/signing endpoint was contacted. No GitHub CI success claimed.

## Presentation and forward handoff

**Documented event. Observable signal. Missing POST retained.**
Five descriptive PRE references → April3 candidate evidence → April28 Watch →
POST UNAVAILABLE → PARTIALLY_CONSISTENT retrospective case. Recommended visual:
a phase/evidence availability strip with POST explicitly missing; proposed, not captured.
Do not illustrate May recovery or call this HAB detection validated.

AS-108 P0 retrospective case-study reporting complete with POST unavailable,
prepared on `data/as-108-case-study`; publication does not claim merge/PR approval.
Owner review → separately authorized M44 PR/merge → separately authorized AS-201
Sentinel-1 retrieval/design execution. AS-201 NOT STARTED. Do not repair POST,
query later May matches, start future policy validation or P1 05.10 robustness here.
M44 PR NONE CREATED; M44 MERGE NONE PERFORMED; Decision054 ABSENT.
