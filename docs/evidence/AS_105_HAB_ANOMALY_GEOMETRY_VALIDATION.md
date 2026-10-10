# AS-105 M28 — Offline Geometry Implementation and Adversarial Validation

**Date:** 9 October 2026 (Asia/Dubai).
**Checkpoint:** M28 / E28 / EV-032, Decision 050.
**Status:** **PASS — SYNTHETIC OFFLINE IMPLEMENTATION / OWNER-RECONCILED / PUBLICATION AUTHORIZED**.
**Branch:** `feature/as-105-hab-anomaly-geometry`.
**Verified base:** `4e322df220f8cab2805fccf9a2b32dd825f29218`.
**Worktree:** `/workspace/aquasentinel-813-as105`.

## Evidence boundary

All geometry execution in this checkpoint uses synthetic temporal parents.
The fixtures reuse the existing upstream synthetic factory read-only, then
construct internally valid temporal snapshots and refresh their statistics,
output hash and provenance. Every fixture passes the existing AS-104 validator;
no production validation or upstream fixture is modified.

This validates implementation behavior, not HAB accuracy or biological causation.
Real candidate count/fraction/area/regions/fragmentation/vote distribution:
**UNKNOWN**. Real AS-105 acceptance: **NOT RUN**; its future checkpoint has not
been created. Future policy validation: required / **NOT RUN**.
AS-106+ and P1 homogeneous 05.10: **NOT STARTED**. Feature commit/push authorized
on 10 October 2026 after final gates; this evidence accompanies publication.
No PR creation/merge; exact Git/remote verification precedes PR review.

## Historical 9 October implementation quality gates

Existing environment: Python 3.11.16, NumPy 2.2.6, Rasterio 1.4.3 / GDAL 3.9.3.
No install, dependency, configuration or upstream algorithm change.

Commands executed from the isolated worktree with the existing environment's
Python (`/workspace/aquasentinel-813/.venv/bin/python`):

```text
python -m pytest tests/geometry -v
136 passed in 5.33s

python -m pytest -v
799 passed, 6 warnings in 22.62s

python -m ruff check .
All checks passed!

git diff --check
PASS
```

136 new collected test cases, all passing; 663 historical cases retained.
The six warnings are existing Rasterio `windows.py` PendingDeprecationWarnings
from three preprocessing tests at two source locations. No new geometry warnings.
Tracked and all new untracked paths additionally pass whitespace checking.
No GitHub CI-success claim: these are local offline quality gates.

## Synthetic controls A–E

| Control | Executed evidence | Result and scope |
|---|---|---|
| A — deterministic repeat | `test_deterministic_repeat_and_created_at_excluded` | PASS: identical scientific parameters, labels, regions, fingerprints and ID; later aware creation time is accepted without changing identity |
| B — irrelevant mutation | `test_irrelevant_valid_parent_mutation_keeps_identity`; `test_unconsumed_history_count_and_statistics_do_not_change_identity`; `test_unsupported_nan_payload_irrelevant` | PASS: valid parent centre/scale/z/anomaly/statistics/count/timing changes and unsupported NaN-bit changes do not alter consumed identity/output |
| C — consumed mutation | `test_one_consumed_bit_changes_identity_without_crossing_threshold`; `test_threshold_crossing_changes_evidence`; `test_support_mutation_changes_fingerprint_and_product`; `test_signed_zero_bits_preserved_in_consumed_identity` | PASS: one supported deviation/rank bit changes fingerprint/ID even without changing classification; predecessor crossing changes the expected pixel evidence; support and signed-zero bits remain explicit |
| D — connectivity | `test_diagonal_eight_connectivity`; `test_separated_single_pixels_row_major_and_no_filtering`; `test_exact_label_pixel_counts` | PASS: diagonal pixels form one eight-connected region; separated single pixels retain row-major labels, exact counts and no filtering |
| E — polygon | six `test_exact_roundtrip_no_added_pixels` fixtures; winding/order/hole tests | PASS: single cell, rectangle, hole, diagonal multipart, pinched and grid-border fixtures rasterize exactly; emission order/start/winding/hole order cannot change canonical output |

## Owner-review reconciliation — 10 October 2026 (Asia/Dubai)

This is part of M28/E28/EV-032 and Decision 050 before publication, not a new
milestone. Nominal 0.90 and the float32 rule remain unchanged. The frozen AS-104
rank is `(below + 0.5*exact_ties)/n`. For the accepted n=5 parent, no-tie ranks
are 0.0/0.2/0.4/0.6/0.8/1.0, with spacing 0.2; a passing no-tie pixel exceeds
all five histories. Exactly 0.90 requires four below plus one tie. This is a
predeclared empirical-rank upper-tail screen whose granularity depends on history
count, not a smooth population-percentile estimator, significance, probability,
confidence or severity. Five observations are not statistical sufficiency.

The geometry fixture invokes the existing AS-104 calculation on synthetic AS-103
inputs and validates the resulting parent, without duplicating its midrank math.
All cases also assert minimum five, five references, count five, positive
deviation, float32 ranks, eligible support and resulting feature/candidate masks.

| Exact case ID under `test_five_history_rank_granularity` | History / target | Expected rank | Screen |
|---|---|---|---|
| `four-below-no-ties` | 1,2,3,4,6 / 5 | float32(0.8) | fails |
| `five-below-no-ties` | 1,2,3,4,5 / 6 | float32(1.0) | passes |
| `four-below-one-tie` | 1,2,3,4,5 / 5 | float32(0.9) | passes |
| `three-below-two-ties` | 1,2,3,5,5 / 5 | float32(0.8) | fails |

No geometry source, temporal source/tests, frozen rule or real accepted parent
changes. No real AS-105 run; M29/E29/EV-033 are not created.

### Final owner-review publication gates — 10 October 2026

```text
python -m pytest tests/geometry -v
140 passed in 6.08s

python -m pytest -v
803 passed, 6 warnings in 22.83s

python -m ruff check .
All checks passed!

git diff --check
PASS
```

The four added cases pass; the earlier 136 geometry and 663 historical cases
remain passing. Same six historical Rasterio warnings, no new warnings.
Exact 18-path scope, reviewed geometry-source hashes, unchanged upstream files,
all twelve accepted cache hashes, read-only handoff, both stashes and recovery
artifacts are verified before publication. New untracked whitespace checks PASS.
Owner authorizes the single feature commit/push after these gates; this record
accompanies publication and requires final Git/remote equality and clean-worktree
verification. No PR/merge, real acceptance or future study is authorized here.

## Mandatory adversarial matrix — all 55 requirements covered

The numbers below correspond to the owner's mandatory case list, not the total
pytest count. The original implementation had 136 geometry cases; four
owner-review rank-granularity cases bring the latest total to 140.
Function names refer to the seven authorized files in `tests/geometry/`.

| Requirement | Test evidence | Result |
|---|---|---|
| 1–2 nominal float32 threshold / predecessor | `test_exact_float32_boundary` | PASS |
| 3–6 positive / +0 / -0 / negative direction | `test_strict_positive_direction` | PASS |
| 7 invalid rank cannot vote | `test_invalid_rank_cannot_vote_and_support_does_not_require_six_features`; `test_parent_rank_range_and_finiteness_enforced` | PASS |
| 8 rank can vote without z | `test_zero_mad_votes_without_z` | PASS |
| 9 huge z alone cannot vote | `test_huge_z_alone_cannot_vote` | PASS |
| 10 F1 duplicate members count once | `test_frozen_family_agreement` | PASS |
| 11 F1 + F4 candidate | `test_frozen_family_agreement` | PASS |
| 12 F4 + F5 fails red-edge requirement | `test_frozen_family_agreement` | PASS |
| 13 one red-edge family insufficient | `test_frozen_family_agreement` | PASS |
| 14 three qualifying families | `test_frozen_family_agreement` | PASS |
| 15 candidate containment and denominator | `test_candidate_and_family_masks_cannot_expand_water`; `test_denominator_uses_availability_not_votes` | PASS |
| 16 diagonal eight-connect | `test_diagonal_eight_connectivity` | PASS |
| 17 separated pixels | `test_separated_single_pixels_row_major_and_no_filtering` | PASS |
| 18 deterministic row-major labels | `test_separated_single_pixels_row_major_and_no_filtering` | PASS |
| 19 single-pixel retention | `test_separated_single_pixels_row_major_and_no_filtering` | PASS |
| 20 no implicit filtering | `test_separated_single_pixels_row_major_and_no_filtering` | PASS |
| 21 exact label counts | `test_exact_label_pixel_counts` | PASS |
| 22 multiple-resolution affine area | `test_area_is_affine_derived` at 10/20/30 m | PASS |
| 23 exact polygon round-trip | `test_exact_roundtrip_no_added_pixels` | PASS |
| 24 no added candidate pixels | `test_exact_roundtrip_no_added_pixels` | PASS |
| 25 deterministic parts/rings | `test_canonical_geometry_ignores_gdal_emission_ring_start_and_winding`; `test_holes_and_parts_are_sorted` | PASS |
| 26 unsupported CRS/grid rejection | `test_unsupported_crs_or_grid_fails` | PASS |
| 27 C/F layout invariant | `test_memory_layout_invariant` | PASS |
| 28 byte-order canonicalization | `test_endian_canonicalization_at_fingerprint_boundary` | PASS; whole-parent native-dtype contract remains intact |
| 29 unsupported values irrelevant | `test_unsupported_nan_payload_irrelevant` | PASS |
| 30 consumed-bit mutation | `test_one_consumed_bit_changes_identity_without_crossing_threshold` | PASS |
| 31 threshold crossing | `test_threshold_crossing_changes_evidence` | PASS |
| 32 rehashed family-policy change | `test_rehashed_altered_policy_is_not_valid_v1[mapping]` | PASS: identity changes and v1 rejects |
| 33 rehashed threshold-policy change | `test_rehashed_altered_policy_is_not_valid_v1[threshold]` | PASS: identity changes and v1 rejects |
| 34 rehashed connectivity change | `test_rehashed_altered_policy_is_not_valid_v1[connectivity]` | PASS: identity changes and v1 rejects |
| 35 parent buffers/metadata unchanged | `test_parent_buffers_metadata_unchanged_and_outputs_defensive` | PASS |
| 36 defensive output arrays | `test_parent_buffers_metadata_unchanged_and_outputs_defensive` | PASS |
| 37 immediate AS-104 provenance | `test_exact_recursive_lineage_and_registry_unchanged`; shortcut-rejection cases | PASS |
| 38 tampered evidence | `test_tampered_arrays_fail_parent_aware_validation` | PASS; rehashed output still rejected |
| 39 tampered candidates | `test_tampered_arrays_fail_parent_aware_validation` | PASS |
| 40 tampered labels | `test_tampered_arrays_fail_parent_aware_validation` | PASS |
| 41 tampered geometry | `test_tampered_region_geometry_and_measurements[geometry]` | PASS |
| 42 tampered region statistics | `test_tampered_region_geometry_and_measurements`; `test_tampered_scene_metadata` | PASS |
| 43 tampered identity/ID | `test_rehashed_altered_policy_is_not_valid_v1`; `test_tampered_scene_metadata[id]` | PASS |
| 44 tampered provenance | `test_provenance_shortcuts_or_tampering_rejected` | PASS |
| 45 empty support | `test_empty_policy_support` | PASS: null fraction/no regions/missing summaries |
| 46 eligible but zero candidates | `test_eligible_zero_candidates_and_all_candidates` | PASS: fraction 0.0 |
| 47 all-candidate raster | `test_eligible_zero_candidates_and_all_candidates` | PASS: fraction 1.0, exact count/votes |
| 48 grid-edge components | `test_exact_roundtrip_no_added_pixels[border]` | PASS |
| 49 holes | `test_exact_roundtrip_no_added_pixels[hole]`; winding/hole-order cases | PASS |
| 50 diagonal multipart | `test_diagonal_one_region_multipart_no_bridge` | PASS |
| 51 corner-touch/pinched fixtures | `test_exact_roundtrip_no_added_pixels[diagonal]`; `[pinched]` | PASS |
| 52 creation timestamp excluded | `test_deterministic_repeat_and_created_at_excluded` | PASS |
| 53 no network | `test_public_api_no_network_writes_or_upstream_calculation` | PASS: network functions replaced with failing sentinels |
| 54 no disk-cache write | same test | PASS: write-open/NumPy-save and cache paths guarded |
| 55 no upstream calculation | same test | PASS: optical/spectral/temporal public calculations replaced with failing sentinels |

Additional checks cover int32 label overflow, shape/dtype/key/order integrity,
parent version/type, rank range/finiteness, direct PC/optical/spectral provenance
shortcuts, mask/support mutation, signed-zero bits, family diagnostics, regional
missing-support summaries, output-hash noncircularity and a tuning-free API.

### Numerical robustness finding during offline review

A finite two-pixel regional deviation subset at +1e308 or -1e308 exposed an
overflow in NumPy's ordinary sum-based even median, despite the complete
synthetic AS-104 parent remaining valid. The new AS-105 summary now sorts and
uses the middle value or an overflow-safe even midpoint (half-sum for extreme
same-sign pairs). Two focused regression cases verify the finite exact median.
No input clipping/imputation, candidate-rule change or upstream modification.
This arithmetic rule is recorded in the frozen statistics-policy identity.

## Verified handoff prerequisite

The owner-authorized prerequisite reconstruction predates M28. These are
existing accepted parent facts, not a new real AS-105 run:

- Temporal product: `temporal:e814b0574ab30d1841778ee3c5005ffcb313ab42473c41acc028f0a9f7804a8b`.
- Accepted output fingerprint: `2a2902f946d49487f1416d0bd6ad73c7976910fe72060f03503540a49e2678dd`.
- 61/61 arrays previously verified; `allow_pickle=False` round-trip PASS;
  restored `scene.validate()` PASS; complete registry retained in manifest.
- External directory: `/workspace/aquasentinel-handoffs/as104/e814b0574ab30d1841778ee3c5005ffcb313ab42473c41acc028f0a9f7804a8b`.
- `arrays.npz`: 198,981 bytes; SHA-256 `14122d08baea3025d84127b7e6f55635a7fd12652319230c36ccf0d26df94902`.
- `manifest.json`: 176,608 bytes; SHA-256 `985ce7ca4df818b46fdb641afc08e65df621be0d91cad1c355b7a3017ff30433`.
- `SHA256SUMS.txt`: 157 bytes; SHA-256 `66fb164d8c86d55fb71fa43d4d2866fa531f75cf6ad522b081ba1ae1af518a21`.

M28 preservation is SHA/metadata-only: all three files remain byte-identical,
0444, in a 0555 directory. No handoff arrays were loaded into AS-105 or copied
into Git. All twelve accepted AS-102 cache-file hashes remain unchanged.
AS-102/103/104 source/tests/config/dependencies/provenance/cache format remain
byte-identical to the approved base; other worktrees retain their original
tracked bytes, HEADs and statuses. External recovery artifacts remain intact.
Both safety stashes remain untouched:
`f93950aab6fdfb40bb100158915ef12692aa1665` and
`d979a433a5ab8ae600282048f184eb5fd06a8f17`.

## Limitations and next authorized boundary

No real geometry metrics or scientific accuracy results are established.
Policy families are not independent; empirical rank is not probability,
confidence, significance or severity. No HAB/bloom confirmation, concentration,
species, toxins, water safety, intake risk, persistence, alert or lead-time claim.
Roughly 10% five-history support remains an upstream limitation; five references
are not statistical sufficiency. Large z from small positive scales remains
documented and z is excluded from this policy.

Future comparative validation must predeclare rank/direction, z/direction and
combined variants; 0.80/0.90/0.95 rank thresholds; 1/2/3-family minima; red-edge
required/optional; 4/8 connectivity; no-filter versus labelled filter sensitivity.
Add history-depth sensitivity where valid EO permits: predeclare around-five,
moderately deeper and substantially deeper histories; exact depths must be
selected from valid EO availability before the study. Assess coarse-rank
dependence without altering M29's accepted minimum-five parent. NOT RUN.
It has **NOT RUN**. April 28 cannot serve as both tuning data and sole superiority
evidence. Feature publication and then PR code review follow the passed owner-review clarification. Real AS-105 acceptance,
future policy study, AS-106+ and P1 05.10 require separate authorization.
