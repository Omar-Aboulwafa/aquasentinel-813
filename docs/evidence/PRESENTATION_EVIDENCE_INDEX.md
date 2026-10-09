# AquaSentinel 813 — Presentation Evidence Index

**Current platform-fix / cached acceptance checkpoint — 9 October 2026 (Asia/Dubai):**
The owner-authorized consistency predicate now compares `.casefold()` values only.
It does not strip punctuation/whitespace, map aliases, or rewrite stored platform
strings, source records, products, fingerprints or caches. Acquisition and all
other provenance/compatibility checks remain unchanged. Only
`temporal/baseline.py` and `tests/temporal/test_identity_lineage.py` changed in
source/tests: one predicate and 20 regression cases. The reverse-case unit case
isolates this predicate; the existing descriptor schema still requires lowercase
observation platforms. Full-API tests use the real lowercase-observation /
mixed-case-source pattern for both Sentinel-2A and Sentinel-2B.

M24/E24/EV-028 records the bug fix, with **132 temporal tests PASS** and the
pre-rerun combined **663 passed**, Ruff/diff PASS, six historical Rasterio warnings.
M25/E25/EV-029 records **real acceptance PASS**, reusing all six known-ID 05.09
AS-102 caches with no network or imagery reprocessing. Unchanged AS-103
reconstruction reproduced all six accepted IDs/content fingerprints. All 12
cache-file hashes remain identical. The exact five March acquisitions, April-28
target, March half-open window and minimum five were retained.

Cached rerun: **08:01:50.383608–08:01:51.327507 UTC** /
**12:01:50.383608–12:01:51.327507 +04:00 Asia/Dubai**. On the unchanged 20 m
EPSG:32640 310×228 grid, all features have 7,963 target-supported pixels.
Baseline/z/rank counts in approved feature order are
**792 / 802 / 801 / 801 / 801 / 797**; insufficient counts are
**7,171 / 7,161 / 7,162 / 7,162 / 7,162 / 7,166**. Zero MAD and both numerical
rejection counts are zero for every feature. Sparse history remains masked;
five scenes are not five valid observations at every pixel.

**18/18 independent scalar checks PASS**, synthetic later-scene addition/mutation
causal check PASS, deterministic repeat PASS, input immutability PASS.
Product: `temporal:e814b0574ab30d1841778ee3c5005ffcb313ab42473c41acc028f0a9f7804a8b`.
Immediate provenance parents are target AS-103 first, then R1–R5 chronologically;
each branch retains actual PC → AS-102 → AS-103 → AS-104 lineage. The future
control is synthetic and excluded, not evidence of future EO availability.
Full counts, summaries, fingerprints, parents and scalar records are in
[validation §§6–7](AS_104_TEMPORAL_BASELINE_VALIDATION.md).

M23/E23/EV-027 remains the earlier **BLOCKED** platform-casing attempt; its body
and all prior checkpoint/decision bodies remain preserved. No Decision 050.
Both retained stashes and old/new external recovery artifacts remain available.
AS-104 stays **UNCOMMITTED / READY FOR REVIEW**. Owner review is the next gate;
no commit/push/PR/merge, AS-105+, or P1 homogeneous-05.10 experiment. PASS is
engineering acceptance of temporal candidate BOA signals, not biological or
operational accuracy, risk, persistence, alert or warning-lead-time validation.
Earlier dated checkpoint statements below are historical; this update governs
current state. Final quality/security verification is recorded in validation §7.

**Created:** 6 October 2026 (Asia/Dubai).

**Historical PR #10 integration checkpoint — 9 October 2026 (Asia/Dubai):** Decision 048 is
merged through PR #10 at `39f2aee90c727fc151886efbdea44daec0e3f9b4` (fix commit
`c9a415b65a101319e9c9f2fef21ad0dcd44c9347`). The existing AS-104 branch was
fast-forwarded from `c6accab2c5753734466a6375d1b3ce1762e99bed`, then its retained
safety stash was applied. Genuine documentation conflicts were reconciled;
all ten restored AS-104 files matched the pre-integration SHA-256 inventory.
Temporal source/tests remain byte-for-byte unchanged. The combined offline gate
passed: **533 tests**, Ruff/diff checks, the same six Rasterio warnings.
The original Decision 047 → 048, M19 → M20, E18 → E19 → E20 and
EV-022 → EV-023 → EV-024 bodies/statuses are preserved in order. Their
cross-worktree/pending-merge wording describes the original dated checkpoints.
The frozen April 28 / exactly-five March / minimum-five / delivered-05.09 real
acceptance was resumed in three separately timestamped attempts. All stopped at
March 4 asset signing; a bounded diagnostic observed intermittent HTTP 504 and
successful responses for the same assets. The third attempt read SCL but
exhausted five attempts signing B02. **Real acceptance remains BLOCKED**: zero
completed reference scenes and no real temporal product. No scientific/mask/math/
grid contract was relaxed. Implementation remains uncommitted; see
[resumed evidence](AS_104_TEMPORAL_BASELINE_VALIDATION.md) / M21/E21/EV-025.
**P1 Processing Baseline Robustness Experiment — NOT STARTED**: homogeneous
05.09 versus homogeneous 05.10 requires separate authorization and is not
accuracy validation. AS-105+ is NOT authorized and NOT started. No commit,
push or PR in this integration task; retain the verified safety stash.

**Purpose:** Compact claim-to-evidence index for the [presentation journal](../PRESENTATION_JOURNAL.md). This pack preserves the CDSE investigation, the **historical Planetary Computer metadata-only checkpoint**, and the [later successful final raster gate](AS_102_PLANETARY_COMPUTER_RASTER_GATE.md). Historical records do not themselves certify perpetual external-service availability or authorize implementation. The separately authorized M15 update adds actual AS-102 implementation evidence EV-016/EV-017 and Decisions 039–045; AS-103 is COMPLETE AND MERGED through PR #8; EV-019/EV-020 preserve its earlier feature-branch acceptance stage, and EV-021 records the later final code-review/publication stage. AS-102 is COMPLETE AND MERGED through PR #6; EV-018 records the final reviewed/merged stage while EV-016/EV-017 preserve their historical acceptance checkpoint.

**Later evidence stage recorded:** 6 October 2026 (Asia/Dubai), FG-01. Original experiment timestamp not supplied; this is a later experiment than the preserved metadata-only checkpoint, not a new probe run by this documentation task.

**New implementation evidence:** EV-016/EV-017, fresh experiment started `2026-10-06T10:07:14.660936+00:00` UTC / `2026-10-06T14:07:14.660936+04:00` Asia/Dubai. Base `0867708ea62676dcbcd0f5f83577cc120d633f26`, branch `feature/as-102-optical-preprocessing`. This new experiment has exact timestamps, typed processing evidence and offline tests, unlike the original supplied historical reconstructions.

**Final review/merge update:** 8 October 2026 (Asia/Dubai), EV-018. Feature `fe3d27046c40600010753957ee8921d57071ec48`; [PR #6](https://github.com/Omar-Aboulwafa/aquasentinel-813/pull/6); merge `627b6ae8a509509dbb2d5d43bbdc6d74e0ce2aac` at `2026-10-08T07:06:46Z` / `2026-10-08T11:06:46+04:00`. Final reviewed baseline: 265 tests passed, Ruff/diff checks passed; six non-blocking Rasterio warnings. No configured/reported GitHub CI/workflow checks. At the AS-102 merge checkpoint AS-103 was NOT authorized and NOT started; the later AS-103 authorization/acceptance is recorded separately below.

**Historical AS-103 acceptance checkpoint:** 8 October 2026, EV-019/EV-020; explicitly authorized candidate-feature implementation, uncommitted/unpushed/unmerged. Six features, 7,963 valid pixels each; 348-test branch baseline. AS-104 NOT authorized and NOT started.

**Current AS-103 final review/merge update:** 8 October 2026 (Asia/Dubai), M18 / EV-021. AS-103 is **COMPLETE AND MERGED** through [PR #8](https://github.com/Omar-Aboulwafa/aquasentinel-813/pull/8). Implementation `5638bc8b4ab06f235f908642f714a7cc83b35709`; AS-103 implementation merge commit `b770d0561da9ac2b81ca2d4b8e784adff66ee231`, merged `2026-10-08T10:43:24Z` / `2026-10-08T14:43:24+04:00` Asia/Dubai. Final reviewed baseline: 348 tests passed, Ruff/diff checks passed; six existing non-blocking Rasterio PendingDeprecationWarnings only, no new AS-103 warnings. No GitHub Actions/workflow CI run was configured/reported; no GitHub CI success is claimed. AS-103 development is closed. AS-104 — Temporal Baseline is NEXT PLANNED only, NOT authorized and NOT started. No real-scene experiment was rerun during merge review or this documentation closeout.

**Historical AS-104 checkpoint — 8 October 2026 (Asia/Dubai):** Decision 047 explicitly
authorized implementation; M19 / E18–E19 / EV-022–EV-023 records an uncommitted
offline PASS and BLOCKED real multi-scene attempt. This supersedes older AS-104
status wording while preserving EV-001–EV-021 as historical records. No new merge,
GitHub CI, HAB/event or operational-performance claim. AS-105+ remains unstarted.

## Evidence standard and temporal boundary

**Historical PR #11 acceptance checkpoint — 9 October 2026 (Asia/Dubai):**
Decision 049 is merged through PR #11 at
`2006df7a70a4f48c66933aed96f4464d8d03084e` (fix commit
`9181e0da40898f5c729b8596367bb3e4719317d0`). The branch was fast-forwarded and
its NEW safety stash applied without dropping either stash. Four genuine
documentation conflicts were reconciled; all eight temporal source/test hashes
remain unchanged. Combined offline gate: **643 passed**, Ruff/diff PASS, six
existing Rasterio warnings. Decisions 046→047→048→049, milestones M18–M22,
engineering E17–E22 and detailed evidence EV-021–EV-026 coexist in order without
renumbering or duplicated bodies; earlier statuses remain historical.

The frozen 05.09 April-28 / exactly-five March / minimum-five real experiment ran
07:31:08.630215–07:31:57.353103 UTC / 11:31:08.630215–11:31:57.353103 Dubai.
**5/5 March AS-102 and AS-103 scenes completed** with normal production transport,
unchanged EPSG:32640 310×228 grid and masks. Valid-water counts:
8,674 / 2,092 / 7,350 / 3,834 / 6,156. Accepted April cache/feature IDs remain
unchanged; target supports 7,963 pixels per feature. March 4 has 52 denominator
exclusions in B04-denominator features; March 14 has 20 green/blue exclusions.

**AS-104 real acceptance is BLOCKED**, now at its target provenance guard:
`observation_match.platform` is `sentinel-2b`, but actual PC `SourceRecord.platform`
is `Sentinel-2B`. All three target acquisition timestamps agree. The unchanged
case-sensitive comparison at `temporal/baseline.py:105–110` rejects the target
before numerical reduction. March products have the corresponding same casing
mismatch. Transport succeeded; this is a representation/validation blocker, not
measured zero temporal support. No history distributions, temporal summaries,
AS-104 fingerprints/ID/lineage, scalar checks, future control or deterministic
repeat were produced/run. No code/test/cache-contract change or workaround.

M23/E23/EV-027 records this factual attempt, with full safe scene statistics,
IDs/fingerprints, support and diagnostic metadata in
[AS-104 validation](AS_104_TEMPORAL_BASELINE_VALIDATION.md#5-pr-11-integration-and-five-reference-0509-attempt--9-october-2026).
Owner review/authorization of a targeted platform-representation fix and realistic
metadata tests is the next gate; do not mutate source records or accepted caches
to bypass it. AS-104 remains uncommitted for review. No new Decision 050, commit,
push, PR or GitHub merge; only the required local ff-only integration occurred.
AS-105+ and P1 homogeneous-05.10 study NOT started. No hazard, science accuracy,
operational risk, persistence, alert or warning-lead-time claim.

**Historical upstream fix checkpoint — 8 October 2026:** Decision 048 / M20 / E20 /
EV-024 adds separately authorized source disambiguation, uncommitted for review.
AS-104 was explicitly authorized and remains uncommitted/preserved in its original
worktree; real acceptance is still BLOCKED pending upstream review/merge and a
separate rerun. Decision 047 and M19/E18–E19/EV-022–EV-023 remain there only, per
owner clarification; their numbers are reserved, not reused. Earlier AS-103
closeout authorization statements retain their historical checkpoint meaning.

**Historical Decision 049 fix checkpoint — 9 October 2026:** Decision 048 is merged via PR
#10 at `39f2aee90c727fc151886efbdea44daec0e3f9b4`. AS-104 resumed and then hit
intermittent per-asset SAS HTTP 504s. Decision 049/M22/E22/EV-026 now records a
separate, uncommitted reusable-token transport fix and fresh bounded smoke.
Decision 047/M19/E18–E19/EV-022–EV-023 and M21/E21/EV-025 stay only in the
preserved uncommitted AS-104 worktree; their bodies are not copied. Historical
EV-001–EV-024 rows remain unchanged. AS-104 acceptance is still BLOCKED pending
Decision 049 review/merge. AS-105+ and P1 homogeneous-05.10 study NOT started.

The historical probe reports and later raster-gate report transcribe the project owner's supplied factual reconstruction of completed investigations. “Directly observed” refers to those reported observations, not a new live probe performed when writing these documents. Original command logs, full STAC responses, exact experiment timestamps, and screenshots are not attached. Their absence is explicitly retained as a capture limitation.

Use these classifications: **directly observed evidence**, **provider/STAC-advertised metadata**, **inference**, **blocker**, **recommendation**, and **unverified claim**. An advertised format or grid does not prove a successful raster read. A provider recommendation is not an approved technical decision. A pending result must remain pending until a separately recorded experiment supports it.

EV-001–EV-008 index existing repository evidence. EV-009–EV-013 preserve the historical investigations. **EV-014 progresses from historical PENDING to later FG-01 PASS / READY**; both stages appear below, and the original PENDING row is preserved. EV-015 separates metadata-driven PC decoding from raster-access success. Record creation date, acquisition date, processing date, and experiment date must remain distinct.

EV-016/EV-017 retain the 6 October experiment and feature-branch status at that date. Their uncommitted/unmerged/review-pending wording is historical; **EV-018 supersedes that Git status** without changing the original experiment or its 213-test baseline.

EV-019/EV-020 and journal M17 retain the original AS-103 feature-branch acceptance state and experiment timestamp. Their uncommitted/not-merged statuses are intentional historical truth; **EV-021 / M18 supersedes that Git status** with a separately dated final review/merge checkpoint, preserving the 348-test baseline and all real-scene evidence.

## Claim index

| Evidence ID | Claim | Status | Metric/result | Source document | Suggested presentation use | Visual still needed? | Final validation needed? |
|---|---|---|---|---|---|---|---|
| EV-001 | Product thesis / Track 03 | Current approved product decisions | Water-quality/operations manager; monitoring/field-verification priority; two planned P0 hazards | [Decisions 001–015](../DECISIONS.md); [PRD §§1–5](../AquaSentinel_813_PRD_v1.0.md) | Problem/user/decision opening | Yes: operator-to-decision diagram | Yes for claimed operational impact; not for recorded thesis |
| EV-002 | AS-001 repository foundation | Completed engineering fact | Python 3.11, `src/` packaging, pytest/Ruff; `f878acc` | [Project State §6](../PROJECT_STATE.md); [pyproject](../../pyproject.toml) | Reproducible engineering foundation | Yes: package/setup capture | Fresh clean-environment reproduction before demo |
| EV-003 | AS-002 config/AOI | Completed engineering fact | TOML/GeoJSON validation and runtime context; `f606ac5`, `113ca44` | [Project State §7](../PROJECT_STATE.md); [runtime](../../src/aquasentinel/runtime.py) | Explicit geographic/scientific inputs | Yes: labelled Al Raha study map | Operational intake geometry remains separate/pending |
| EV-004 | AS-003 provenance | Completed engineering fact | Schema 1.0; historical 17-test project baseline; `e2baedc`, `db79260` | [Project State §§8–9](../PROJECT_STATE.md); [provenance](../../src/aquasentinel/provenance/) | Trace a future result to its source | Yes: labelled source/derived example | Real end-to-end derived hazard lineage remains future |
| EV-005 | Codex continuity | Completed recorded onboarding/handoff | AS-000C.1–8 completed; read-only audit at `779069d`; separate AS-101 authorization | [Project State §13](../PROJECT_STATE.md); [Handoff §§16–19](../HANDOFF.md) | Recoverable multi-machine/agent workflow | Yes: continuity sequence | Original full audit artifact not retained in tracked snapshot |
| EV-006 | AS-101 real Sentinel-2 search | Completed implementation and recorded experiment | AOI/date/cloud search, full pagination, deterministic candidates/provenance; PR #2 merge `1b83a73` | [AS-101 report](../AS_101_STAC_SEARCH.md) | Connect the use case to real catalog data | Yes: query-to-source diagram | Live services can change; raster usability not established |
| EV-007 | 44 candidate scenes | Directly observed catalog experiment | 44 unique products; 44/44 provenance conversions; 0.12–24.96% scene cloud; recorded 2 Oct 2026 | [AS-101 live result](../AS_101_STAC_SEARCH.md); [CDSE probe](AS_102_CDSE_ACCESS_PROBE.md) | First live-data evidence card | Yes: dated result card | Not a fixed future count; usable-water analysis pending |
| EV-008 | 97-test quality baseline | Recorded engineering validation | 97 tests passed, Ruff passed, diff check passed; 17 original tests retained | [AS-101 validation](../AS_101_STAC_SEARCH.md); [journal E09](../PRESENTATION_JOURNAL.md) | Quality/review evidence | Yes: dated test summary | Rerun before release; not scientific accuracy |
| EV-009 | CDSE reflectance offset discovery | Provider/STAC-advertised metadata; decoding inference | Scale `0.0001`, offset `-0.1`; valid DN decoding `DN * 0.0001 - 0.1` | [CDSE reflectance record](AS_102_CDSE_ACCESS_PROBE.md#reflectance-scaleoffset-discovery) | Explain why raw stored values need product semantics | Yes: sanitized metadata fields and formula | Yes: per-band metadata excerpts and decoded real sample |
| EV-010 | CDSE raster-access blocker | Observed environmental blocker; S3/OIDC route advertised | Proxy blocked live raster/header/window attempts; no full download; bounded access unverified | [CDSE access record](AS_102_CDSE_ACCESS_PROBE.md#access-route-and-blocker) | Catalog-versus-pixel-access distinction | Yes: access-boundary diagram | Yes: runtime transport and bounded read; do not infer universal provider denial |
| EV-011 | Planetary Computer STAC accessibility | Directly observed catalog evidence | Anonymous STAC READY / HTTP 200; corresponding item identified | [PC catalog result](AS_102_PLANETARY_COMPUTER_PROBE.md#directly-observed-catalog-result) | Evidence that an alternative catalog was reachable | Yes: sanitized catalog response | Raster signing/access still pending at this checkpoint |
| EV-012 | Same acquisition / different processed product | Metadata-supported inference; pixel equivalence unverified | Acquisition/platform/tile/orbit match; CDSE baseline 05.10/Aug 2024 versus PC 05.09/Apr 2023 | [Identity comparison](AS_102_PLANETARY_COMPUTER_PROBE.md#cross-provider-identity-finding) | Explain provenance during provider evaluation | Yes: comparison table | Metadata capture still needed; no pixel-equivalence claim |
| EV-013 | Planetary Computer COG delivery path | Provider/STAC-advertised metadata; viable-path inference | Nine proposed reflectance bands + SCL; B02 10 m, B05/SCL 20 m COG; host `sentinel2l2a01.blob.core.windows.net` | [PC assets/access](AS_102_PLANETARY_COMPUTER_PROBE.md#asset-inventory-and-advertised-delivery-path) | Potential route to bounded raster access | Yes: host-to-window diagram | Yes: allowlist/access, signing, header/window support, decoding |
| EV-014 | AS-102 bounded raster read | **PENDING — unverified at this evidence point** | No bounded read had yet been performed in the recorded PC stage; no DN/window result | [PC readiness](AS_102_PLANETARY_COMPUTER_PROBE.md#readiness-and-next-evidence) | Explicit remaining feasibility gate | Yes: actual tiny-window evidence after verification | **Yes; do not mark successful from catalog/COG metadata** |
| EV-014 · FG-01 | AS-102 bounded raster read — later final gate | **PASS / READY for tested PC product/path** | 3 successful bounded raster reads; 4 credential-free HTTP 200 signing operations; product XML read; metadata-driven B02/B05 decoding; **8/8 readiness gates passed** | [Later raster-gate record](AS_102_PLANETARY_COMPUTER_RASTER_GATE.md) | Show progression from catalog metadata to real bounded pixels | Yes: sanitized header/window/signing captures | Historical result reported; complete-band preprocessing, scientific suitability, and repeatability captures remain future |
| EV-015 | Metadata-driven PC reflectance decoding | Observed XML and DN samples; metadata-derived interpretation | XML 53,347 bytes; baseline 05.09; quantification 10000; offset -1000; B02 bandId 1/B05 bandId 4; `(DN - 1000) / 10000` | [XML and decoding evidence](AS_102_PLANETARY_COMPUTER_RASTER_GATE.md#product-xml-and-metadata-driven-interpretation) | Explain modern-baseline offsets with actual product metadata | Yes: XML field/band-map excerpt and sample table | Mechanics established for tested bands; aquatic suitability, quality masking, and pixel equivalence not established |
| EV-016 | Full-AOI AS-102 optical preprocessing | **PASS — implemented/validated on uncommitted feature branch** | 9 float32 bands + uint8 SCL/masks, (228,310), 20 m EPSG:32640; AOI 67,449; valid data 65,166; candidate water 10,211; valid water 7,963; AOI fraction 11.805957%, retention 77.984526%, excluded 2,248 | [Timestamped real validation](AS_102_OPTICAL_PREPROCESSING_VALIDATION.md); journal M15 | Real pixel/grid/mask evidence without hazard claims | Yes: AOI/candidate/retained/excluded map | Independent aquatic/HAB scientific validation remains future |
| EV-017 | Actual-PC lineage, verified AOI cache and quality gate | **PASS — implementation acceptance; not merged** | PC-only pixel lineage; CDSE discovery separate; SHA-256/canonical atomic cache; array/source/provenance-equivalent known-ID reload with catalog/signing/XML/raster calls blocked; 213 tests passed (97 retained), Ruff/diff check passed | [Cache/quality evidence](AS_102_OPTICAL_PREPROCESSING_VALIDATION.md); Decisions 039–045 | Reproducible, traceable inputs for future features | Yes: lineage/checksum/test card | Clean-machine/full-product demo and Git review remain pending |
| EV-018 | AS-102 final security/cache/provenance review and merge | **COMPLETE AND MERGED — 8 October 2026** | Final reviewed implementation `fe3d27046c40600010753957ee8921d57071ec48`; PR #6; merge `627b6ae8a509509dbb2d5d43bbdc6d74e0ce2aac`; 265 tests passed, Ruff/diff checks passed; canonical HTTPS/redirect protections, transient SAS containment, strict matching/asset rejection, bounded reads, conservative support and cache/provenance tamper checks; six non-blocking Rasterio warnings | [PR #6](https://github.com/Omar-Aboulwafa/aquasentinel-813/pull/6); [journal M16](../PRESENTATION_JOURNAL.md#m16--as-102-code-review-security-hardening-merge-and-closeout); committed source/tests | Reviewed/merged preprocessing and engineering reproducibility only; does NOT support HAB confirmation, chlorophyll concentration, toxin detection, water safety, desalination shutdown, warning lead time or operational risk accuracy | Yes: sanitized merge/commit/local-quality card | No configured/reported GitHub CI checks; independent science and full-product validation remain outstanding |
| EV-019 | Per-scene AS-103 candidate spectral features and numerical diagnostics | **PASS — authorized feature-branch acceptance, uncommitted** | 6 float32 arrays/masks (228,310); 7,963 valid pixels each; no denominator/nonfinite exclusions; two NDCI-like outputs below −1 retained; 491 negative-input pixels for B06 features | [Timestamped AS-103 evidence](AS_103_SPECTRAL_FEATURES_VALIDATION.md); journal M17 | Explain candidate signals and numerical support before temporal science | Yes: V18 sanitized maps | No HAB, chlorophyll concentration, toxins, species, safety, risk or lead-time claim; independent science remains future |
| EV-020 | AS-103 content identity, immediate-parent lineage and offline quality | **PASS — authorized feature-branch acceptance, not merged** | Versioned mask/five-band fingerprint; deterministic repeat; exact PC→AS-102→AS-103 registry chain; four scalar pixel checks; no access/write calls; 348 tests (265 retained +83 new), Ruff/diff pass, six existing Rasterio warnings | [AS-103 validation](AS_103_SPECTRAL_FEATURES_VALIDATION.md); [contract](../AS_103_SPECTRAL_FEATURES.md); Decision 046 | Reproducible candidate inputs for future AS-104 | Yes: V19 lineage/formula card | Code review/publication pending; no AS-104 authorization or GitHub CI/science claim |
| EV-021 | AS-103 final code review and merge | **COMPLETE AND MERGED — 8 October 2026** | Implementation `5638bc8b4ab06f235f908642f714a7cc83b35709`; PR #8; merge `b770d0561da9ac2b81ca2d4b8e784adff66ee231` at `2026-10-08T10:43:24Z` / `2026-10-08T14:43:24+04:00` Asia/Dubai; 348 tests passed, Ruff/diff checks passed; six existing non-blocking Rasterio warnings only, no new AS-103 warnings; typed model/arithmetic, inclusive denominator guards, NaN/support, consumed-content fingerprint/identity and immediate-parent lineage reviewed; real-scene evidence independently reviewed | [PR #8](https://github.com/Omar-Aboulwafa/aquasentinel-813/pull/8); [journal M18](../PRESENTATION_JOURNAL.md#m18--as-103-code-review-merge-and-closeout); committed source/tests and historical AS-103 acceptance evidence | Reviewed/merged spectral feature engineering, deterministic per-scene feature generation and reproducible lineage/identity only; does NOT support temporal anomaly, HAB confirmation, chlorophyll concentration, species/toxin identification, water safety, intake exposure, operational risk accuracy or warning lead time | Yes: V20 sanitized merge/local-quality card | No configured/reported GitHub Actions/workflow CI run or CI-success claim; independent science remains future; AS-104 NOT authorized and NOT started |
| EV-024 | Explicit PC processing-baseline source resolution and unchanged cache identity | **PASS — isolated fix offline/metadata gates; uncommitted, not merged** | 421 tests (348 retained +73 added), Ruff/diff pass, same six warnings; 5/5 frozen March references plus April target resolve at 05.09 with all eleven required assets and 0 forbidden signing/XML/raster/preprocessing/cache calls; accepted target cache retains identity/provenance/bytes and rejects 05.10 | [Timestamped fix validation](AS_102_REQUIRED_PC_BASELINE_FIX_VALIDATION.md); [plan/API](../AS_102_REQUIRED_PC_BASELINE_FIX.md); Decision 048; M20/E20 | Explain acquisition versus processing-product ambiguity and explicit failure-safe selection | Yes: sanitized ambiguity/constraint/quality card, pending | Upstream code review/merge and separate frozen AS-104 acceptance rerun; no March asset/decoding/support, temporal/HAB, operational accuracy or GitHub CI-success claim |
| EV-026 | Reusable transient PC account/container SAS transport | **PASS — offline/bounded transport smoke; UNCOMMITTED / READY FOR REVIEW** | 531 tests (421 main +110 net new), Ruff/diff PASS, six unchanged warnings; fresh March-4 05.09 all-eleven same-scope signs with 1 anonymous HTTP 200 token attempt, XML 1,024 bytes/B02 4,096 bytes via 206, zero additional acquisition for reuse; original worktree/cache hashes and stash preserved | [Timestamped validation](AS_102_REUSABLE_PC_SAS_TOKEN_FIX_VALIDATION.md); [plan](../AS_102_REUSABLE_PC_SAS_TOKEN_FIX.md); Decision 049; M22/E22 | Scoped credential reuse without changing scientific source identity | Yes: sanitized one-request/eleven-assets card; capture pending | No full processing, AS-104 acceptance, five usable histories, science/operational accuracy, availability guarantee or GitHub CI-success claim; review/merge remains next |
| EV-028 | AS-104 case-only platform consistency fix | **PASS — UNCOMMITTED / READY FOR REVIEW** | One equality predicate, 20 regression cases, 132 temporal and 663 full tests/Ruff/diff PASS; stored values/identities unchanged | [Validation §6](AS_104_TEMPORAL_BASELINE_VALIDATION.md#6-targeted-platform-case-representation-fix--9-october-2026); M24/E24 | Fix representation compatibility while preserving scientific identity | Yes: before/after predicate card; capture pending | No aliases, science change, Decision 050, publication or accuracy claim |
| EV-029 | AS-104 cached five-reference 05.09 acceptance rerun | **PASS — UNCOMMITTED / READY FOR REVIEW** | Six known-ID cache reloads/unchanged AS-103 IDs; 792–802 eligible pixels from 7,963 target support; 18 scalar checks, synthetic causal exclusion, repeat PASS; zero network | [Validation §7](AS_104_TEMPORAL_BASELINE_VALIDATION.md#7-cached-five-reference-0509-real-acceptance-rerun--9-october-2026); M25/E25 | Honest sparse temporal support and reproducible lineage | Yes: history-count/support card; capture pending | Five scenes are not statistical sufficiency; no HAB, concentration, safety, operational risk, persistence, alerts/lead time or CI-success claim |

### EV-021 final AS-103 review and merge

This later checkpoint records the owner-approved final implementation and real-scene
acceptance review, followed by verified publication/PR #8 merge. Review evidence:

- Typed model invariants (`models.py`) and feature arithmetic (`spectral.py`): PASS.
- Inclusive denominator epsilon guards and NaN/feature-support behavior: reviewed/tested PASS.
- Input fingerprint and consumed B02–B06 identity sensitivity: reviewed/tested PASS.
- Unconsumed B07/B08/B8A/B11 identity independence and timestamp-independent identity: reviewed/tested PASS.
- Exact PC→AS-102→AS-103 immediate-parent lineage and direct raw-source shortcut rejection: reviewed/tested PASS.
- M17 real-scene acceptance evidence, including independent scalar checks: review PASS.

M17's experiment began `2026-10-08T09:52:47.133486+00:00` UTC /
`2026-10-08T13:52:47.133486+04:00` Asia/Dubai. The later merge occurred at
`2026-10-08T10:43:24Z` / `2026-10-08T14:43:24+04:00` Asia/Dubai.
The scene was not rerun during merge review or this documentation closeout.
EV-019/EV-020 remain unchanged, including their historical statuses and 348-test baseline.
The preserved scene has six candidate features, 7,963 pixels each (100% parent water),
two below-−1 NDCI-like values retained/diagnosed and signed BOA preserved.

BOA is not aquatic Rrs; ndci_like is not calibrated chlorophyll; mci_like is an
analogue. Correlated NDCI-like/B05-red features are not independent biological
evidence. No event threshold, HAB/event classification, temporal baseline/anomaly,
species/toxins, safe/unsafe certification, autonomous plant action, intake exposure,
operational risk, persistence, warning lead-time accuracy or scientific accuracy is
established. AS-104 is NEXT PLANNED only, NOT authorized and NOT started.
No GitHub Actions/workflow CI run was configured/reported; local quality checks do
not imply GitHub CI success.

### EV-022 — AS-104 offline temporal engineering

**Status:** PASS — authorized implementation, uncommitted for review.
**Date:** 8 October 2026 (Asia/Dubai).
**Claim:** Causal target-ID selection, per-feature/pixel median/MAD/signed deviation,
positive-scale standardized anomaly, exact midrank, semantic target-support input
fingerprints, typed masks/counts/summaries, immediate-AS-103 multi-parent provenance
and blocked IO/immutability. 460 tests passed (348 +112), Ruff/diff PASS; six existing
Rasterio warnings. No dependency/config/cache-format/provenance-schema changes.
**Evidence:** [AS-104 plan/API](../AS_104_TEMPORAL_BASELINE.md), Decision 047,
[validation](AS_104_TEMPORAL_BASELINE_VALIDATION.md), journal M19 / E18.
**Limits:** Offline math/provenance evidence, not real multi-scene acceptance,
biological/event validation, risk, confidence/probability or warning lead time.
No commit/push/PR; AS-105+ unauthorized/unstarted.

### EV-023 — AS-104 fixed-window real acceptance blocked by provider ambiguity

**Status:** BLOCKED — real multi-scene acceptance NOT complete.
**Date:** 8 October 2026 (Asia/Dubai); actual attempt UTC
12:28:07.712335–12:28:29.564367 / Dubai 16:28:07.712335–16:28:29.564367.
**Claim:** Existing April 28 cache/AS-103 target reused (7,963 valid pixels/feature).
AS-101 returned 44 candidates; five March dates match tile 40RBN/orbit 20. The first
reference, March 4, has two PC products with the exact same acquisition/platform/
tile/orbit but baselines 05.09 and 05.10. Unchanged AS-102 exactly-one matching
raises ObservationMatchError; experiment stops before reference raster reads.
**Evidence:** [Timestamped AS-104 validation/blocker](AS_104_TEMPORAL_BASELINE_VALIDATION.md),
journal M19 / E19; stable product IDs, fixed bounds and metadata-only diagnosis.
**Limits:** Zero processed references; real support/summaries, temporal fingerprints/
ID/lineage, scalar checks and future-real-scene check NOT produced/run. No silent
selection workaround, window widening, minimum lowering, baseline mixing or mask
relaxation. Separately authorize any upstream selection-policy investigation.
No HAB/event, science accuracy or operational availability/lead-time claim.
**Visual:** V21 blocker/causal-contract card planned, no screenshot/anomaly map exists.

### EV-024 required-PC-baseline upstream fix

New metadata smoke: `2026-10-08T13:38:26.730440+00:00`–
`2026-10-08T13:38:48.970146+00:00` UTC, or
`2026-10-08T17:38:26.730440+04:00`–`2026-10-08T17:38:48.970146+04:00`
Asia/Dubai. The exact predeclared March products and accepted April product resolve
at 05.09 using the new optional constraint; no XML/rasters were accessed and no
cache was created. Separate offline loading of the accepted April cache verified
matching/contradicting constraints without altering its files or provenance.
This fixes ambiguity at metadata level only, not AS-104 real acceptance.
EV-022–EV-023 remain reserved in the untouched AS-104 worktree. All historical
EV-001–EV-021 rows remain unchanged, including EV-014 PENDING/later PASS progression.

### EV-025 — PR #10 integration and frozen AS-104 signing-access blocker

**Status:** Integration/preservation/offline PASS; real acceptance BLOCKED.
**Date:** 9 October 2026 (Asia/Dubai); exact three attempt times in validation §4.
**Claim:** Exact merged main `39f2aee90c727fc151886efbdea44daec0e3f9b4` integrated
ff-only; retained verified stash restored; four documentation conflicts reconciled;
Decision 047→048, M19→M20, E18–E20 and EV-022–EV-024 preserved without renumbering
or rewriting historical statuses. Eight temporal source/test files byte-identical;
533 tests, Ruff/diff PASS; six existing warnings. Frozen delivered-05.09 attempts
resolved March 4 product, read XML/SCL, then signing prevented completion;
last B02 signing exhausted five bounded attempts. Diagnostic observed intermittent
HTTP 504/200. Zero completed March references; accepted target 7,963 pixels/feature.
**Evidence:** [Timestamped resumed validation](AS_104_TEMPORAL_BASELINE_VALIDATION.md#4-decision-048-integration-and-resumed-frozen-acceptance--9-october-2026),
PR #10, journal M21 / E21, retained recovery/hash inventories and safety stash.
**Limits:** No real temporal support/counts/statistics/fingerprints/product/lineage,
scalar, future-scene or repeat result. Support is unknown, not measured zero;
not HAB, calibrated chlorophyll, biological/operational accuracy or GitHub CI.
**Next:** Retry identical 05.09 contract when signing is available; do not widen
bounds, reduce minimum, mix processing or relax masks. Keep changes uncommitted;
stash retained. P1 05.10 comparison and AS-105+ NOT STARTED.
**Visual:** V22 sanitized gate chronology/HTTP status card planned, no anomaly map.

### EV-026 reusable-token transport — later stage

Fresh transport experiment: `2026-10-09T06:44:49.076690+00:00`–
`2026-10-09T06:44:51.406274+00:00` UTC / 10:44:49–10:44:51 Asia/Dubai.
One token HTTP 200, eleven signs on the actual March-4 05.09 account/container,
two tiny HTTP 206 prefix/header reads, then zero extra acquisition requests for
three cache-reuse signs. Report contains safe counters/status/latency/bytes only.
No SAS credentials, product cache or full preprocessing created. EV-026 does not
supersede EV-024's historical metadata experiment; it records a new transport
stage after PR #10. EV-025 remains only in the preserved AS-104 worktree.

### EV-027 — PR #11 integration and real five-reference 05.09 acceptance attempt

**Status:** Integration/preservation/offline and AS-102/103 references PASS;
AS-104 real acceptance **BLOCKED**. Uncommitted for review.
**Date:** 9 October 2026; exact experiment UTC 07:31:08.630215–07:31:57.353103 /
Dubai 11:31:08.630215–11:31:57.353103 +04:00.
**Claim:** Exact ff-only PR #11 integration; second retained stash and external
recovery artifacts; eight temporal source/test hashes preserved. Combined suite
643 passed, Ruff/diff PASS, six existing warnings. Normal production transport
completed five predeclared actual 05.09 March AS-102/103 scenes, identical target
grid, and retained target cache identity/bytes. AS-104 target provenance guard
rejects lower-case observation `sentinel-2b` against source label `Sentinel-2B`.
Timestamps match; no temporal reduction occurred.
**Evidence:** [Validation §5](AS_104_TEMPORAL_BASELINE_VALIDATION.md#5-pr-11-integration-and-five-reference-0509-attempt--9-october-2026), M23/E23, PR #11 / 2006df7;
full safe per-scene IDs/fingerprints/statistics/support and diagnosis.
**Limits:** No real temporal distributions/arrays/masks/statistics, semantic
fingerprints/ID/lineage, scalar checks, causal future control or repeat result;
missing outputs are unmeasured, not zero. No new Decision 050, algorithm change,
cache rewrite, contract relaxation, hazard/accuracy/operational or GitHub CI claim.
**Visual:** Five-reference support table and sanitized platform-label guard card;
capture pending, no temporal anomaly screenshot.

### EV-014 evidence progression

| Stage / record date | Status | Evidence boundary |
|---|---|---|
| Historical checkpoint, recorded 6 Oct 2026 | **PENDING** | Anonymous catalog/advertised COGs only; [original report](AS_102_PLANETARY_COMPUTER_PROBE.md) remains unchanged |
| Later experiment FG-01, recorded 6 Oct 2026 | **PASS / READY** | GDAL 3.10.3 B02 64×64, B05 32×32, SCL 32×32 reads; signed XML and metadata-driven decoding; [new report](AS_102_PLANETARY_COMPUTER_RASTER_GATE.md) |

Original experiment timestamps were not supplied; report dates do not imply the experiments happened simultaneously. **At FG-01: AS-102 raster-access prerequisite READY; AS-102 NOT YET IMPLEMENTED; AS-103 NOT STARTED.** This historical state is preserved; the later EV-016/EV-017 record supports AS-102 feature-branch implementation acceptance, with AS-103 still not started at that checkpoint. EV-019/EV-020 records the subsequent separately authorized AS-103 acceptance. The SCL sample contains 353/1024 raw water-class pixels, not a final usable-water count. Exact transferred raster bytes were not measured.

No visual is claimed to exist merely because it is suggested here. A metadata inventory, 44 catalog products, and 97 passing software tests do not establish HAB detection, aquatic reflectance suitability, a safe/unsafe water decision, or operational warning lead time.

## Remaining evidence and presentation gaps

- Original probe task/command transcripts, dates/times, tool versions, sanitized STAC/asset metadata excerpts, and actual screenshots.
- CDSE raster transport/authentication and bounded range/window access; no provider-global access conclusion from the environment proxy blocker.
- The later FG-01 report now records credential-free signing, B02/B05/SCL headers/windows, and XML-based decoding. Original timestamps/commands/8-gate checklist, sanitized original XML/header/status captures still need evidence; EV-016 independently records later all-band preprocessing; do not relabel the earlier checkpoint as successful.
- Complete per-provider inventories and field provenance; no cross-provider pixel-equivalence result.
- Exact raster-transfer bytes were not measured; compressed blocks may exceed the requested pixel window. No byte-efficiency claim is supported.
- EV-016/EV-017 now records one real scene’s aligned optical arrays, mask/fraction statistics, actual-PC lineage and offline cache replay. Historical HAB/oil validation, false positives, operational demo site, full product/demo fallback and measured impact remain future evidence. EV-019/EV-020 adds candidate features only, not temporal/scientific interpretation.
- AS-102 contract/provider choice and implementation were separately authorized and recorded by Decisions 039–045 / M15. Final Git review/publication is recorded separately by EV-018 / M16 and PR #6. Presentation captures remain pending; the separate AS-103 authorization is recorded in Decision 046 / M17, not granted by this pack. EV-021 / M18 and PR #8 separately record AS-103 final review/merge. AS-104 remains NOT authorized and NOT started.

## Presentation capture rule

For every important experiment, future agents must record:

- Command/task purpose and the exact bounded method used.
- Experiment timestamp/date and timezone, separately from the report-creation date and product dates.
- Source/provider and stable catalog/collection references.
- Item/product identity, acquisition context, and processing baseline/version where relevant.
- Quantitative result, units/denominator, and whether it is observed, advertised, inferred, or unverified.
- Limitation, failure/blocker, remaining uncertainty, and authorization boundary.
- Screenshot/visual requirement, caption, capture status, and attribution/licence.
- Repository evidence file and relevant commit/PR reference when available.

Do **not** store credentials, SAS tokens, signed URLs, or secrets. Use sanitized unsigned references and metadata excerpts. Do not commit full EO scenes or runtime caches as presentation evidence.

After an evidence record exists, update the journal and affected EV entries. Preserve the old dated checkpoint when adding a later successful or failed gate; never rewrite a metadata-only stage as if it already contained pixel evidence. Scientific/provider decisions continue to be governed by the existing decision log and explicit authorization.

### EV-028 — Targeted platform case-representation consistency fix

**Status:** PASS — uncommitted for owner review. Date: 9 October 2026 (Asia/Dubai).
**Finding:** Only `_descriptor`'s platform equality changes to `.casefold()`.
No aliases, punctuation/space stripping, stored value normalization or identity
rewrite. Acquisition, lineage and every other compatibility rule are unchanged.
**Validation:** 20 added regressions; 132 temporal / 663 full tests, Ruff/diff PASS;
six historical Rasterio warnings. Reverse-case unit test isolates the predicate;
the existing lowercase observation descriptor schema remains unchanged.
**Evidence:** [Validation §6](AS_104_TEMPORAL_BASELINE_VALIDATION.md#6-targeted-platform-case-representation-fix--9-october-2026), M24/E24, source/test delta and external pre-fix patch/hash inventory.
**Limit:** Bug fix under Decision 047; no Decision 050 or new scientific result.

### EV-029 — Cached real five-reference 05.09 temporal acceptance rerun

**Status:** PASS — uncommitted for owner review. Date: 9 October 2026 (Asia/Dubai).
**Experiment:** 08:01:50.383608–08:01:51.327507 UTC /
12:01:50.383608–12:01:51.327507 +04:00. Exactly five fixed March references and
accepted April-28 target, March half-open window and minimum five. Six existing
known-ID 05.09 caches reused; unchanged AS-103 reconstruction reproduced exact
IDs; all 12 cache-file hashes preserved. Zero network attempts or raster writes.
**Result:** Six features each have target support 7,963. Baseline/z/rank counts
792/802/801/801/801/797; insufficient counts 7,171/7,161/7,162/7,162/7,162/7,166.
Zero MAD/numerical rejection counts zero. 18/18 independent scalar checks,
synthetic future addition/mutation exclusion, deterministic repeat and input
immutability PASS. Target-first/R1–R5 immediate parents and full upstream lineage.
**Product:** `temporal:e814b0574ab30d1841778ee3c5005ffcb313ab42473c41acc028f0a9f7804a8b`.
**Evidence:** [Validation §7](AS_104_TEMPORAL_BASELINE_VALIDATION.md#7-cached-five-reference-0509-real-acceptance-rerun--9-october-2026), M25/E25, complete safe JSON distributions/summaries/fingerprints/parents/scalar records.
**Limit:** Engineering acceptance only; rank is not probability/confidence/
severity and five observations are not statistical sufficiency. No aquatic Rrs,
HAB, concentration, species/toxins, safety, intake risk, persistence, alert,
warning lead-time or GitHub CI-success claim. Synthetic control is not a real
future observation. M23/E23/EV-027 remains historically BLOCKED; no publication,
AS-105+ or P1 homogeneous-05.10 experiment.
