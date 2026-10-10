# AS-107 — HAB Risk and Evidence Completeness: Frozen Design

**Date:** 10 October 2026 (Asia/Dubai). **Decision 052: FINAL / FROZEN DESIGN — NOT IMPLEMENTED.**
M36 read-only feasibility/design audit COMPLETE. M37 design-freeze documentation only;
no real AS-107 score, scientific product, source/test/config edit or implementation.
Official design baseline: `6b22d32f078ef80158b2f2d7aac4f3dd07925038`, PR #21 merge.
AS-106 COMPLETE / CLOSED. Prepared on `docs/as-107-design-freeze`.

## Task, goal, inputs and outputs

Freeze owner-approved rules before inspecting any resulting real score. AS-107 v1
is an explainable, availability-aware, provisional observational HAB-like
screening-risk layer. It is not complete intake operational risk. Environmental
context and intake exposure are unavailable; current P0 output is always
qualified by `assessment_status = provisional_observational_screening`.
Every scored region and site summary preserves this qualification.

Future inputs: authoritative AS-105 target geometry, matching AS-106 persistence,
complete AS-105 integrity sequence, typed AS-104 witnesses and validated policy.
Future output: typed region results and a maximum-region AOI screening summary,
evidence completeness, drivers, recommendations and DerivedProductRecord.
No new dependency, raster output or disk cache is required. Existing NumPy,
standard-library dataclasses, math.fsum, canonical serialization and SHA-256 suffice.
The API performs no IO/network/retrieval/cache or registry mutation and no public
upstream extraction. Existing validator regeneration is integrity verification only.

## Canonical component order and weights

| Canonical component | Raw configured weight q_i | Current v1 meaning / availability |
| --- | ---: | --- |
| spectral_anomaly | 0.35 | Spectral family-evidence breadth; mandatory |
| chlorophyll_red_edge_signal | 0.20 | Red-edge family evidence breadth; mandatory |
| persistence | 0.15 | Observed same-pixel recurrence; available only when B_R > 0 |
| environmental_context | 0.15 | Unavailable / not_implemented |
| intake_exposure | 0.15 | Unavailable / not_implemented |

Preserve the existing names and config values. Weights are unvalidated PoC
hypotheses, not scientific constants. Require exactly these five names, finite
non-boolean numeric values, nonnegative weights, positive total, strictly positive
spectral/red-edge weights, and `abs(fsum(q_i) - 1.0) <= 1e-9`. Retain raw q_i and
canonical normalized w_i. Config coercion must not silently admit invalid inputs
at a future authorized policy boundary; M37 changes no loader or configuration.
No arbitrary provider context/exposure component is accepted by as107-v1.

## Frozen regional evidence definitions

For each unchanged authoritative AS-105 region R, membership is its component
label on the accepted grid. Define exact integer counts for every family j:

```text
a_j = count(R intersect family_available_j)
v_j = count(R intersect family_evidence_j)
```

Family order and membership remain frozen Decision 050:
F1 red_edge_b5_vs_red, F2 red_edge_line_height, F3 red_edge_b6_vs_red,
F4 visible_green_vs_red, F5 visible_green_vs_blue. F1's two features remain one
family vote. Availability and evidence counts come from regional masks, not
scene-wide diagnostics or a family voting anywhere being treated as uniform.

```text
S_R = 100 * sum(v_j for all five families) / sum(a_j for all five families)
E_R = 100 * (v1 + v2 + v3) / (a1 + a2 + a3)
```

Each component is available only with a positive denominator. S_R means spectral
family-evidence breadth over available family-pixel opportunities. E_R means
**red-edge family evidence breadth**, using F1–F3. The retained chlorophyll-named
config key does not estimate concentration or establish biological causation.
No raw z/rank/deviation magnitude, new anomaly threshold or spatial filter is used.

For the matching AS-106 target region:

```text
A_R = target candidate pixels
B_R = candidate pixels with valid prior history
C_R = recurrent candidate pixels
T_R = 100 * C_R / B_R, only when B_R > 0
```

B_R=0 means value None, availability unavailable and reason
`no_prior_valid_candidate_history`. Unsupported candidates are not nonrecurrent;
streak=1 is not proof of nonrecurrence. Streak/timing remain explanation evidence,
not another score, biological duration or a new calendar-gap cutoff.

**Overlap disclosure:** F1–F3 contribute to both spectral_anomaly and
chlorophyll_red_edge_signal. These are correlated/overlapping evidence, not
independent confirmation. Existing weights deliberately emphasize red-edge
signals. Preserve this in Decision 052, diagnostics, limitations and drivers.

## Missing components, score and coverage

Freeze availability-aware renormalization. Never replace missing evidence with
zero, a neutral value, inferred context or inferred exposure. Spectral and
red-edge components are mandatory: if either is unavailable, produce no score.
Persistence may be unavailable even though the validated persistence scene is
required. For unavailable drivers: value None, effective weight 0, contribution
None and explicit reason; context/exposure reason is `not_implemented`.

```text
W0 = math.fsum(all q_i in canonical order)
w_i = q_i / W0
I_R = available component set
K_R = math.fsum(w_i for available i in canonical order)
risk_R = 100 * math.fsum(w_i * (x_i / 100) for available i in canonical order) / K_R
```

Use Python float / binary64 arithmetic. No score for zero K_R. Validate component
values finite within [0,100]; reject invalid/out-of-range results rather than
clipping. No epsilon, snapping or multiplication by completeness.

Component coverage is available configured weight / all configured weight;
K_R is its canonical normalized evaluation. Current configuration implies maximum
possible P0 coverage 0.70, or 0.55 when only mandatory components are available.
These are policy consequences, not calculated real-scene outcomes. Removing a low
available component can raise the renormalized score; always expose coverage and
missing reasons. Adding future components changes the evidence basis, not
necessarily the environmental condition; future contracts require authorization.

## Evidence completeness and empty support

The primary scientific field is `evidence_completeness`, not probabilistic
confidence. For a nonempty region N_R=A_R:

```text
F_all = sum(a_j for all five families) / (5 * N_R)
F_red = (a1 + a2 + a3) / (3 * N_R)
H_R = B_R / A_R
evidence_completeness_R = min(component_coverage_R, F_all, F_red, H_R)
```

Output every factor and numerator/denominator, including configured weight
coverage and integer family/history denominators. This is evidence/support
completeness, not calibrated probability, biological confidence, statistical
sufficiency, accuracy or event likelihood. Do not add AS-104 history support as a
second multiplier: family availability already depends on eligible temporal support.

When B_R=0, persistence is unavailable, H_R=0 and completeness=0; a provisional
spectral/red-edge score may still exist. Zero describes missing historical support,
not zero anomaly/HAB likelihood, safe water or absence of HAB.

For zero target regions, fabricate none. Site `status = no_candidate_regions`;
score/band/completeness/selected_region are None. Preserve observation time and
policy/evaluability diagnostics. Use exactly: "No candidates under the frozen
policy in evaluable observations." Do not output zero/Normal/safe/absence of HAB.
Retain policy-support count so no candidates can be distinguished from an
unevaluable observation. Do not divide by zero or invent regional A=0 records.

## Continuous bands, interpretation and recommendations

Validate strictly increasing nonnegative integer maxima ending at 100; reject
booleans, equal/negative/malformed thresholds. General cut points are low_max+1,
watch_max+1 and elevated_max+1. Defaults mean:

| Band | Unrounded binary64 score | Monitoring recommendation |
| --- | --- | --- |
| Normal | 0 <= score < 25 | Continue scheduled observation |
| Watch | 25 <= score < 50 | Review on the next valid acquisition |
| Elevated | 50 <= score < 75 | Prioritize targeted review and field verification |
| High | 75 <= score <= 100 | High-priority field verification and increased monitoring |

Score, band, evidence completeness, component coverage, completeness factors,
interpretation flags and recommendation are separate. High with low completeness
remains numerically High; never multiply the score or silently downgrade its band.
Display rounding is non-authoritative; no band epsilon/snapping.

Freeze `limited_evidence_completeness_threshold = 0.50`, an uncalibrated
administrative interpretation/UI policy. Completeness <1 adds `incomplete_evidence`;
completeness <0.50 also adds `limited_evidence_completeness`. Neither means
probability or biological confidence. Qualify interpretation visibly, for example:
"High observational screening score with limited evidence completeness;
verification is required. Environmental context and intake exposure are unavailable."
Unscored cases request evidence review / additional valid observations. Never
recommend shutdown, unsafe-water certification or confirmed bloom/petroleum action.

## Regions, site selection and reconstructable drivers

Score every authoritative AS-105 region separately; retain ID/label/count/area,
family and persistence evidence. No geometry changes, merging, filtering or
single-pixel removal. Add `single_pixel_region` for a one-pixel region; no
biological spatial-coherence claim. Keep unscored regions and their reasons.

Site summary selects maximum scored regional raw score. Ties: descending evidence
completeness, then ascending AS-105 component label. Copy score/band/completeness/
coverage/drivers/recommendation/limitations together from that region. No region
average or HAB/oil combination. This is screening/monitoring priority, not a
validated whole-site estimator. Al Raha remains a validation AOI, not a confirmed intake.

RiskDriver fields: canonical_name, component_value float|None, configured_weight,
canonical_weight, effective_weight, contribution_points float|None, availability,
unavailable_reason, typed evidence counts/denominators, definition_id and
source_product_ids. Store all five in canonical component order. For available
components effective_weight=w_i/K_R and contribution_points=effective_weight*x_i.
Explanation ranking: descending available contribution, canonical-order ties,
then unavailable drivers in canonical order. Reconstruct raw risk from driver
values/weights using the canonical risk equation; separately rounded contribution
displays and floating-point operation order do not replace that equation.

## Typed API, witnesses, models and validation

Frozen future signature (not implemented):

```text
compute_hab_risk(
    geometry_scene: HABAnomalyGeometryScene,
    persistence_scene: HABPersistenceScene,
    *,
    geometry_scenes: Iterable[HABAnomalyGeometryScene],
    temporal_parents: Mapping[str, TemporalFeatureScene],
    policy: HABRiskPolicy,
) -> HABRiskScene
```

The explicit geometry must exactly match the target in the complete persistence
integrity sequence. Validate geometry.validate(temporal_parent) and
persistence.validate(geometry_scenes, temporal_parents=...). AS-104 scenes are
required typed integrity witnesses, not immediate numerical scoring parents.
Match target ID/time/grid/masks/labels, region IDs/counts and A/B/C/fractions;
retain original parent validators and frozen contracts. Future HABRiskScene.validate
regenerates scoring/explanations/identity from fully validated parents, rejects
rehash-consistent tampering and verifies provenance/parameters. Copy mutable data;
no parent changes, aliasing or registry mutation.

Frozen intended models: HABRiskPolicy, RiskDriver, EvidenceCompletenessFactors,
HABRegionRisk, HABSiteRiskSummary, HABRiskStatistics, HABRiskDiagnostics and
HABRiskScene. Frozen dataclasses, canonical tuples, defensive metadata copies.
Region results carry authoritative identity/measurements, all components, score/
band/completeness/factors, persistence explanation, assessment_status and recommendation.
Scene carries grid/target/time/parents, ordered regions, selected-region summary,
statistics/diagnostics, parameters, fingerprints, product ID and DerivedProductRecord.
No production modules are created by M37. Future paths only:
`src/aquasentinel/risk/{__init__,models,policy,scoring}.py` and focused `tests/risk/`.

## Provenance, identity and fingerprints

Immediate sources, exactly in order:
`(target_geometry_scene.product_id, persistence_scene.product_id)`.
Temporal witnesses do not become scoring sources; unavailable context/exposure
create no fictional source IDs. Actual PC → AS-102 → AS-103 → AS-104 → AS-105 →
AS-106 remains intact, with AS-107 consuming target AS-105 plus AS-106. Shared
ancestry can be deduplicated by the existing registry; no generic schema change.

Version as107-v1; type hab_risk; prefix hab_risk:. Canonical identity includes
immediate parent IDs/required versions, target acquisition/grid, consumed-input
fingerprint, raw/canonical weights, component definitions, missing/mandatory
rules, completeness definition, 0.50 flag, continuous bands, site/tie selection,
monitoring/qualification/assessment-status policies and relevant software versions.
Exclude created_at, display rounding and publication metadata.

`as107-input-v1`: framed SHA-256 segments following existing header-length/payload
conventions. Consume target policy/candidate masks, labels, family availability/
evidence on candidate support, authoritative region identities/consumed measurements,
AS-106 regional A/B/C and recurrence/history values, consumed timing/streak and
region-match evidence. Exclude unrelated reflectance/z/rank/deviation arrays and
complete AS-104 witness payloads. Parent IDs separately enter identity; consumed
bits change fingerprint even if a score is unchanged.

`as107-output-v1`: every region, five drivers, components, denominators, availability,
score/band/completeness/factors/coverage, interpretation/assessment, recommendations,
site selection, statistics/diagnostics/limitations. Exclude resulting AS-107 product
ID and creation time, preventing circularity.

Float64 arithmetic, Python float outputs, exact integer counts, math.fsum and fixed
component order; finite nonboolean values only. No NaN/infinity/clipping/score or
band epsilon. Zero denominator yields unavailable None. Sorted JSON keys, fixed
semantic list order, aware UTC timestamps, allow_nan=False, explicit exact binary64
fingerprint encoding (canonical hexadecimal policy floats acceptable), null for
unavailable values. Caller mapping order cannot affect identity.

## Future M38 synthetic and adversarial acceptance — NOT RUN

Require all three current components; B=0 and partial B/A; generic synthetic
future context/exposure/all-five arithmetic; unavailable mandatory spectral/red-edge;
zero/single/multiple regions; site maximum and site/driver ties; score 0/24/25/49/50/
74/75/100 and immediate float64 boundary neighbours; display-rounding independence;
invalid sums/names, bool/negative/NaN/infinite weights/values; malformed bands;
reordered maps/equivalent inputs; creation-time exclusion; incompatible targets;
missing witnesses; High with low completeness. Future-component tests exercise
arithmetic only: v1 rejects unvalidated arbitrary provider components. Score-zero
kernel tests must not fabricate zero-evidence candidates violating AS-105 policy.

Tamper family availability/evidence, candidate/labels/counts, persistence A/B/C/
fractions/timing/streak, target ID/time/grid, weights/bands, factors/drivers/effective
weights/contributions, site selection, recommendations/assessment/provenance.
Reject stale and recomputed attacker hashes/parameters. Test PC/AS104 provenance
shortcuts, hidden context/exposure, changed recommendation policy, signed URLs,
missing witnesses, parent mutation, defensive copies/no aliasing, no IO/network/
cache/registry effects. Verify existing parent validators run; do not weaken them.

## Future M39 real engineering acceptance — NOT RUN

Requires Decision 052 merged/frozen, separate implementation authorization and
passing synthetic/adversarial validation, then separate real-acceptance authorization.
Use unchanged accepted AS-105/106 typed parents and witnesses; verify sealed hashes/
modes; run offline, no EO retrieval/public upstream extraction. Freeze policy before
scoring. Independently reproduce integer denominators, components, weighted score,
band, completeness/factors, drivers/contributions and site selection. Repeat/permutate
caller/config order; verify identity/time exclusion/provenance/tamper rejection and
parent preservation. Accept any resulting band without tuning. No expected score
or band is declared; M37 calculates neither and inspects no result to predict one.

## Scientific limits, risks and AS-108 boundary

No confirmed HAB/species/toxins/chlorophyll concentration, biological certainty,
water-safety certification, shutdown advice, complete intake operational risk,
HAB probability, calibrated confidence, accuracy or warning-lead-time claim.
Correlated family/component evidence, candidate-conditioned regional summaries,
missing context/exposure, UNKNOWN history, exact-pixel motion limitations, long
observation gaps and shared sparse histories remain disclosed. Five histories are
not statistical sufficiency. Completeness does not measure biological certainty
or repair sparse upstream coverage. Renormalization changes with availability;
site maximum can emphasize single pixels. Future AS-105 policy validation NOT RUN;
P1 homogeneous 05.10 robustness NOT STARTED.

AS-107 demonstrates deterministic explainable heuristic engineering/reproducibility/
provenance only. Historical accuracy, sensitivity/specificity, false positives,
biological truth, chlorophyll accuracy, toxic bloom confirmation, optimal thresholds,
lead time, confidence calibration and intake-decision quality require separately
authorized AS-108 work. AS-108 NOT STARTED. No context/exposure implementation here.

## Milestones, M37 validation and next action

| Checkpoint | Scope / status |
| --- | --- |
| M36 / E36 / EV-040 | Prior read-only feasibility/design audit COMPLETE; recorded retrospectively here |
| M37 / E37 / EV-041 | Decision 052 FINAL / FROZEN DESIGN; documentation only, NOT IMPLEMENTED |
| M38 / E38 / EV-042 | Reserved future offline implementation + synthetic/adversarial validation; NOT STARTED |
| M39 / E39 / EV-043 | Reserved future frozen-policy real engineering acceptance; NOT STARTED |
| M40 / E40 / EV-044 | Reserved future publication / merge-effective closeout; NOT STARTED |

Numbering checked against existing maximum M35/E35/EV-039; reservations are not
execution evidence. M37 gates: existing full pytest, Ruff, diff/new-file whitespace,
credential/policy checks and preservation hashes/modes/stashes. Actual current
results are in [M37 evidence](evidence/AS_107_DESIGN_FREEZE.md), distinct from the
historical 993-test baseline. No AS-107 software is validated by those existing tests.
Owner review and separately authorized design PR/merge precede M38 authorization.
M37 may commit/push docs after gates; no PR/merge, implementation or real scoring.
