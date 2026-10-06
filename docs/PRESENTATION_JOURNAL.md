# AquaSentinel 813 — Presentation Evidence Journal

**Created:** 6 October 2026

**Evidence-pack update:** 6 October 2026 (Asia/Dubai). The [claim index](evidence/PRESENTATION_EVIDENCE_INDEX.md) and [CDSE](evidence/AS_102_CDSE_ACCESS_PROBE.md) / [Planetary Computer](evidence/AS_102_PLANETARY_COMPUTER_PROBE.md) reports now preserve the owner's supplied reconstruction of earlier investigations. The PC record is the historical checkpoint before a bounded raster read, not a later final-gate result. Original experiment timestamps, raw transcripts, and screenshots remain capture gaps; no live probe was rerun for this update.

**Purpose:** Source of truth for the hackathon presentation narrative and its supporting evidence.

**Repository snapshot:** `cf1ed231348d60feae190cb79a5d94e9bf194c85`; locally available `origin/main`: `acbe2c113006922cfe3ffb9813165b16fa48c75f`. Their tracked file trees are identical.

**Scope:** Documentation reconstruction only; no new experiment, implementation, or technical decision.

This journal indexes repository evidence. It does not replace the [project state](PROJECT_STATE.md), [decision log](DECISIONS.md), [handoff](HANDOFF.md), or [PRD](AquaSentinel_813_PRD_v1.0.md). Those documents govern scope and authorization. Code/tests and Git history establish implementation history; a recorded live result establishes only the experiment it describes.

Status labels used throughout:

- **Completed fact:** supported by tracked implementation, documentation, or Git history.
- **Current decision:** an existing decision, cited by number; no new provider or scientific policy is adopted here.
- **Recorded experiment:** a documented observation, with its date and limits.
- **Provider/STAC-advertised metadata:** reported item/asset properties, distinguished from independently read raster headers/pixels.
- **Inference / recommendation / blocker / unverified claim:** conclusions, suggested next steps, obstacles, and missing verification are labelled separately in the probe records.
- **Evidence gap:** a requested story point without a supporting tracked report; outcome and date remain unverified from repository evidence.
- **Future plan:** intended work or proposed presentation material; neither implemented nor authorized by this journal.

Dates follow the source documents when they describe an event. Git dates retain their timezone when precision matters: AS-101 commits dated 2 October in UTC fall on 3 October in UAE time. The PRD delivery calendar is a plan, not a completion record. Lessons and presentation takeaways below are retrospective interpretations of the cited evidence, not claims of measured operational impact.

## 1. Executive project story

**Product thesis / current decisions:** AquaSentinel 813 competes in Track 03 — Water Security & Marine Environments. It targets the Desalination Plant Water Quality / Operations Manager and the question: **Where and when should monitoring or field verification be prioritized?** The intended value is offshore awareness before a threat reaches an intake, with evidence, confidence, exposure, and human verification. Sources: Decisions 001–004 and PRD sections 1–5 and 22.

The P0 product vision contains two separately interpretable hazards: Sentinel-2 HAB-like biological anomalies first, and Sentinel-1 oil-slick candidates second. Hyperspectral characterization, SST, currents, wind, and advanced drift are P1 enhancements. Transparent anomaly/risk logic precedes fitted ML; risk weights are hypotheses. These are design commitments, not delivered hazard capabilities. Sources: Decisions 005–015 and 034.

**Completed facts:** The repository first established reproducible packaging, validated configuration/AOI inputs, and provenance. Continuity documents and read-only Codex onboarding preceded explicit AS-101 authorization. AS-101 now discovers deterministic, fully paginated Sentinel-2 L2A candidates and converts them to provenance. It was merged through [PR #2](https://github.com/Omar-Aboulwafa/aquasentinel-813/pull/2) at `1b83a732155ee01c01b7d33cb50115725cfb08c3`; post-merge documentation was merged through [PR #3](https://github.com/Omar-Aboulwafa/aquasentinel-813/pull/3) at `acbe2c113006922cfe3ffb9813165b16fa48c75f`.

**Recorded experiment:** A 2 October CDSE metadata search returned 44 unique candidate scenes for the analyst-defined Al Raha validation polygon, 1 March–31 May 2023, with scene cloud cover <= 30%. Provenance conversion/serialization succeeded for 44/44. The recorded quality baseline is 97 tests, Ruff passed, and `git diff --check` passed. Source: [AS-101 report](AS_101_STAC_SEARCH.md).

**Current repository phase:** Foundation complete → continuity complete → Codex development handoff complete → AS-101 complete and merged → AS-102 Optical Preprocessing next planned, **not authorized and not started**. No active AS-102 development branch is recorded. No AS-103 implementation is present.

**Presentation boundary:** Catalog discovery proves metadata availability. It does not prove usable water pixels, successful reflectance decoding, a detected HAB, petroleum composition, water safety, earlier warning, or avoided plant disruption. The new evidence reports record advertised CDSE scale/offset, its environmental access blocker, PC catalog accessibility/advertised COGs, and the metadata-supported same-acquisition/different-product finding. At the PC checkpoint documented here, signing, decoding, and bounded raster reads remained unverified; EV-014 is PENDING. No provider or scientific decision is changed.

## 2. Chronological milestone timeline

### M01 — Track 03 selection and product thesis

- **Date:** Recorded in continuity documents committed 2 October 2026 (`5f67e5d`); original selection date is not recorded.
- **Task / milestone ID:** Product definition; Decisions 001–018.
- **Status:** Current decisions; product capabilities remain a PoC goal.
- **Problem / question:** How can EO support a concrete coastal water-security decision?
- **Why it mattered:** A defined operator and action give the project a defensible use case.
- **Options considered:** Generic marine monitoring, algae detection alone, oil mapping alone, and operational intake intelligence are contrasted in Decisions 002–004; no scored track comparison is recorded.
- **Decision:** Track 03; multi-hazard intake intelligence, HAB primary and oil secondary, with human verification.
- **Rationale:** UAE/Gulf relevance, suitable sensors, public-sector/utility users, and a clear operational value chain.
- **Implementation / experiment:** Frozen PRD and decision log; no customer or operational-impact experiment recorded.
- **Evidence:** [Decisions 001–018](DECISIONS.md); [PRD sections 1–5, 22–23](AquaSentinel_813_PRD_v1.0.md); commit `5f67e5d`.
- **Quantitative result:** Two P0 hazard classes planned; no measured warning lead time, avoided downtime, or buyer validation.
- **Limitation:** Al Raha is a validation study area, not a desalination intake; business models are hypotheses.
- **Lesson learned:** The user decision should determine the sensor and evidence design.
- **Impact on next step:** Prioritize Sentinel-2 discovery and scientific traceability before advanced models/UI.
- **Presentation takeaway:** “Watch offshore; explain the evidence; prioritize verification.”
- **Recommended visual:** Proposed operator → observation → evidence → monitoring-priority diagram; not yet captured.
- **Candidate slide title:** “A water-security decision, grounded in offshore evidence.”

### M02 — AS-001 repository foundation

- **Date:** 2 October 2026; initial commit at `14:14:18+04:00`.
- **Task / milestone ID:** AS-001 — Repository Scaffold.
- **Status:** Completed fact.
- **Problem / question:** How can development be reproducible and isolated from other office-machine projects?
- **Why it mattered:** The project must run across office, personal, and cloud environments without moving secrets.
- **Options considered:** Python 3.11 isolation versus newer machine Python versions; `src/` layout versus root imports; personal Git identity separate from company access. No benchmark comparison recorded.
- **Decision:** Python 3.11, `src/aquasentinel`, editable installation, pytest/Ruff, repository-local personal Git setup.
- **Rationale:** Scientific ecosystem compatibility and clean package/account isolation.
- **Implementation / experiment:** Packaging, README, ignore rules, environment example, initial package and smoke test.
- **Evidence:** `f878acc chore: scaffold AquaSentinel 813 project`; [Project State §6](PROJECT_STATE.md); [pyproject.toml](../pyproject.toml); [smoke test](../tests/test_smoke.py); Decisions 021–022 and 027–029.
- **Quantitative result:** Python major/minor pinned to 3.11; a separate initial passing-test count is not documented here.
- **Limitation:** Packaging proves infrastructure, not EO or hazard functionality.
- **Lesson learned:** Reproducibility begins with a small runnable package and an explicit quality gate.
- **Impact on next step:** AS-002 can add validated runtime inputs on a stable foundation.
- **Presentation takeaway:** The project started with repeatable engineering rather than a one-machine demonstration.
- **Recommended visual:** Proposed package tree plus setup/test commands; capture pending.
- **Candidate slide title:** “A foundation that another machine can reproduce.”

### M03 — AS-002 configuration and AOI model

- **Date:** 2 October 2026; feature `14:43:36+04:00`, merge `14:46:36+04:00`.
- **Task / milestone ID:** AS-002 — Configuration & AOI Model.
- **Status:** Completed fact; associated AOI decisions remain current.
- **Problem / question:** How can site, dates, thresholds, and risk assumptions vary without editing source code?
- **Why it mattered:** Invalid geometry or hidden assumptions can contaminate subsequent EO analysis.
- **Options considered:** Hard-coded settings versus TOML; transparent GeoJSON AOI versus an implied operational intake. Sources: Decisions 017–018 and 023–024.
- **Decision:** Validated TOML settings, GeoJSON features/roles, and a runtime context combining them.
- **Rationale:** Human-readable inputs, interoperability, explicit validation, and scientific honesty about the study area.
- **Implementation / experiment:** Date/cloud/risk validation; point/polygon/range/closure checks; duplicate feature-ID rejection; role lookup and runtime construction.
- **Evidence:** Feature `f606ac5`, merge `113ca44`; [configuration package](../src/aquasentinel/config/); [runtime](../src/aquasentinel/runtime.py); [AOI](../data/aoi/demo_site.geojson); [configuration tests](../tests/config/); Project State §7.
- **Quantitative result:** Configured analysis window 1 March–31 May 2023 and cloud threshold 30%; these are settings, not measured performance.
- **Limitation:** The analyst-defined Al Raha polygon and public reference point are neither an official boundary nor an intake; risk weights are unvalidated hypotheses.
- **Lesson learned:** Configuration must preserve the meaning of an AOI as well as its coordinates.
- **Impact on next step:** AS-101 receives validated search inputs; future operational-site selection remains separate.
- **Presentation takeaway:** “A study area is explicit, configurable, and honestly labelled.”
- **Recommended visual:** Proposed AOI map with “validation polygon” and “public reference point” labels; not yet captured.
- **Candidate slide title:** “Define the question geographically before searching.”

### M04 — AS-003 provenance before ingestion

- **Date:** 2 October 2026; feature `15:03:29+04:00`, merge `15:04:59+04:00`.
- **Task / milestone ID:** AS-003 — Provenance Model.
- **Status:** Completed fact; end-to-end hazard lineage is still future work.
- **Problem / question:** How will a future alert remain traceable to observations and processing versions?
- **Why it mattered:** Source identity lost during ingestion cannot be recovered reliably from a final risk map.
- **Options considered:** Ingest first and retrofit lineage versus build provenance first; Decision 019 explicitly adopts the latter.
- **Decision:** Typed source/derived records, validation, serialization, registry, recursive lineage, and JSON persistence.
- **Rationale:** Traceability must be available when the first real scenes arrive.
- **Implementation / experiment:** Reject duplicate IDs, missing upstream references, naive timestamps, and non-JSON processing parameters; restore multi-step dependencies from manifests.
- **Evidence:** Feature `e2baedc`, merge `db79260`; [provenance package](../src/aquasentinel/provenance/); [provenance tests](../tests/provenance/); Project State §§8–9; Decisions 019–020.
- **Quantitative result:** Provenance schema `1.0`; historical whole-project baseline **17 tests passed**, Ruff passed, as recorded at AS-003 completion.
- **Limitation:** A tested lineage registry is not evidence of a delivered feature → hazard → risk → alert pipeline.
- **Lesson learned:** Scientific explanations require traceable inputs, not just readable scores.
- **Impact on next step:** Every AS-101 candidate can be validated as an existing `SourceRecord` without replacing the provenance model.
- **Presentation takeaway:** “Every future result should answer: which source and which processing?”
- **Recommended visual:** Proposed source → feature → hazard → risk → alert diagram, distinguishing implemented registry from future products.
- **Candidate slide title:** “Build the evidence trail before the data flows.”

### M05 — AS-000C continuity and Codex onboarding

- **Date:** 2 October 2026; continuity merge `ccf38d3`, onboarding recorded at `779069d`, onboarding documentation `a01ae65` merged via PR #1 at `51f4ede`.
- **Task / milestone ID:** AS-000C.1–AS-000C.8.
- **Status:** Completed fact, including separate explicit AS-101 development authorization.
- **Problem / question:** Can a fresh developer/agent recover scope, scientific constraints, architecture, and next actions without chat memory?
- **Why it mattered:** Multiple machines and context loss make undocumented knowledge a delivery risk.
- **Options considered:** Conversation-dependent continuity versus repository documents; immediate coding versus first read-only onboarding.
- **Decision:** Repository as source of truth; startup checks and read-only audit before a separately authorized development handoff.
- **Rationale:** Validate understanding before allowing code changes, while preserving personal/company account separation.
- **Implementation / experiment:** AGENTS, state, decisions, PRD, handoff, and plan guidance; documented audit of config/AOI, provenance, tests, and architecture.
- **Evidence:** Commits `5f67e5d`, `160a2dd`, `ccf38d3`, `779069d`, `a01ae65`, `51f4ede`; [AGENTS](../AGENTS.md); [execution plans](../.agent/PLANS.md); Project State §13; Handoff §§16–19; Decisions 025–028 and 035–037.
- **Quantitative result:** Eight continuity/onboarding/handoff subtasks recorded complete; onboarding date 2 October. No onboarding performance metric recorded.
- **Limitation:** The full standalone onboarding audit is not a tracked artifact in this snapshot; completion is recorded by the continuity documents.
- **Lesson learned:** A reviewed read-only understanding check is distinct from implementation permission.
- **Impact on next step:** AS-101 becomes the first expressly authorized Codex development task; later milestones still require authorization.
- **Presentation takeaway:** “An agent handoff is reproducible project context, not conversation memory.”
- **Recommended visual:** Proposed continuity-file map and onboarding → authorization → development sequence.
- **Candidate slide title:** “Make the project recoverable before adding complexity.”

### M06 — AS-101 deterministic Sentinel-2 STAC discovery

- **Date:** Implemented/validated 2 October 2026 per AS-101 report; feature commit `2026-10-02T20:05:10Z`; merged 3 October at `00:24:55+04:00`.
- **Task / milestone ID:** AS-101 — Sentinel-2 STAC Search.
- **Status:** Completed fact; current provider decision is Decision 038.
- **Problem / question:** Which real L2A products intersect the validation AOI within the configured dates/cloud limit?
- **Why it mattered:** Downstream processing needs real, deterministic, provenance-bearing candidates before raster work.
- **Options considered:** Catalog-first versus full imagery work; STAC client versus maintaining a custom protocol; minimal dependency versus the PRD's broader future geospatial stack. No recorded provider benchmark.
- **Decision:** Configurable CDSE STAC (`https://stac.dataspace.copernicus.eu/v1/`, `sentinel-2-l2a`), using only new direct dependency `pystac-client==0.9.0`.
- **Rationale:** Owner-selected provider, STAC pagination support, bounded request waits, and scope protection.
- **Implementation / experiment:** Polygon `intersects`; inclusive UTC days; cloud query and local rechecks; complete GET/POST pagination; typed sorted candidates; duplicate/conflict rules; provider-qualified source IDs.
- **Evidence:** Feature `41a0b0b217cace909c906b7aedcb9cc6d0026f53`; documentation `b3f0e9f878375f5fbfccb35519eeac5cc8fa48af`; merge `1b83a732155ee01c01b7d33cb50115725cfb08c3`; [catalog](../src/aquasentinel/catalog/stac.py); [ingestion](../src/aquasentinel/ingestion/sentinel2.py); [AS-101 report](AS_101_STAC_SEARCH.md); Decisions 030–031 and 038.
- **Quantitative result:** Configurable 30-second per-request timeout; no result cap; initial historical quality gate 92 tests passed at `b3f0e9f`, later superseded by 97.
- **Limitation:** Per-request timeout is not a total search deadline. Asset references contain key/href/type/roles, not a reflectance-decoding or raster-alignment contract.
- **Lesson learned:** Complete pagination and explicit metadata failures protect against plausible-looking partial results.
- **Impact on next step:** AS-102 must establish actual asset access and pixel semantics; AS-101 does not establish either.
- **Presentation takeaway:** “Find real observations completely, and preserve their identity.”
- **Recommended visual:** Proposed query → pagination → sorted candidates → `SourceRecord` diagram; capture pending.
- **Candidate slide title:** “From an AOI question to traceable satellite candidates.”

### M07 — Real CDSE search: 44 candidates and 44 valid source records

- **Date:** 2 October 2026, as recorded in AS-101 documentation.
- **Task / milestone ID:** AS-101 real-data smoke test.
- **Status:** Recorded experiment; not a raster or event-validation experiment.
- **Problem / question:** Does the implemented search work against the real selected provider?
- **Why it mattered:** Offline protocol tests alone cannot demonstrate real catalog coverage.
- **Options considered:** Fixture-only acceptance versus a real metadata smoke test; execution plans require live evidence for external-data work.
- **Decision:** Query configured Al Raha polygon, 1 March–31 May 2023, cloud cover <= 30%, and validate every returned source record.
- **Rationale:** Exercise the actual integration while staying inside metadata-only scope.
- **Implementation / experiment:** Live credential-free HTTPS metadata search, followed by provenance conversion and serialization; reproduction command retained in the AS-101 report.
- **Evidence:** [AS-101 “Recorded real-data result” and reproduction](AS_101_STAC_SEARCH.md); Decision 038; commit `b3f0e9f`.
- **Quantitative result:** **44 unique candidate scenes; 44/44 provenance conversions/serializations**. Earliest `2023-03-04T06:47:51.024Z`; latest `2023-05-28T06:46:29.024Z`; scene cloud range **0.12–24.96%**; first candidate retained **47 asset references**.
- **Limitation:** Products can overlap tiles; 44 is not a count of independent dates. Scene cloud percentage is not AOI water-pixel quality. Catalog reprocessing may change future counts.
- **Lesson learned:** Live discovery and scientific usability are separate acceptance questions.
- **Impact on next step:** Investigate usable raster windows, scale/offset, masks, and alignment before deriving features.
- **Presentation takeaway:** “44 real candidate products, all traceable; water analysis still to be established.”
- **Recommended visual:** Proposed observed-count card and acquisition span with the query constraints printed beside it; do not invent a complete per-date plot from five example items.
- **Candidate slide title:** “The first live evidence: 44 candidate observations.”

### M08 — Review fix, 97-test baseline, and post-merge closeout

- **Date:** Review commits `2026-10-02T20:21:40Z` and `20:21:46Z`; PR #2 and closeout PR #3 merged 3 October 2026.
- **Task / milestone ID:** AS-101 final review and documentation closeout.
- **Status:** Completed fact; 97 is the recorded current quality baseline.
- **Problem / question:** Could a TOML boolean cloud threshold silently become numeric, and did documents accurately reflect committed/merged state?
- **Why it mattered:** `float(True)` would disguise invalid input and weaken the configured scientific filter.
- **Options considered:** Coercion versus rejecting booleans/non-numeric values before conversion. The implemented fix stays local to the cloud threshold.
- **Decision:** Preserve integer/float input; reject boolean/string input before any catalog request; update review and merge status without starting the next milestone.
- **Rationale:** Strict meaning at the configuration boundary and a trustworthy handoff.
- **Implementation / experiment:** Loader type check; parameterized valid thresholds `30`, `12.5`; invalid `true`, `false`, and `"30"` with zero catalog calls. Documentation preserved the 17-test historical baseline.
- **Evidence:** Fix `f57f6bf23e5a7d7eb97c190e5d0308e20d46ca37`; review docs `35caa900597773b4eecf9271ecee22d1b43ebe32`; closeout `cf1ed231348d60feae190cb79a5d94e9bf194c85`; [loader](../src/aquasentinel/config/loader.py); [focused tests](../tests/config/test_catalog.py); PR #2 merge `1b83a73`, PR #3 merge `acbe2c1`.
- **Quantitative result:** Five added parameterized cases; baseline **92 → 97 tests passed**, all 17 original tests retained; Ruff and diff check passed.
- **Limitation:** Test count measures executed cases, not algorithm accuracy, EO water suitability, or code coverage percentage.
- **Lesson learned:** Small type-coercion defects can alter scientific settings; documentation state requires review too.
- **Impact on next step:** AS-101 is closed out on main. AS-102 remains a separately authorized future task.
- **Presentation takeaway:** “The review hardened the meaning of the inputs, not just the happy path.”
- **Recommended visual:** Proposed valid/invalid threshold matrix and test-summary screenshot; capture pending.
- **Candidate slide title:** “A review gate that protects scientific inputs.”

### M09 — CDSE reflectance offset discovery

- **Date:** Report created 6 October 2026; original experiment timestamp not supplied. Acquisition is 28 April 2023, not the probe date.
- **Task / milestone ID:** AS-102 preparation — reflectance semantics investigation; EV-009.
- **Status:** Recorded provider/STAC-advertised metadata and decoding inference; no pixel verification.
- **Problem / question:** What provider/product metadata determines correct surface-reflectance decoding?
- **Why it mattered:** Stored values require product-specific scale/offset before scientific features can be interpreted.
- **Options considered:** DN/10000 alone versus applying the advertised additive offset; no comparative decoded-pixel experiment recorded.
- **Decision:** No scientific policy is changed; the report records the selected CDSE product's advertised semantics.
- **Rationale:** Preserve actual metadata instead of assuming a universal conversion.
- **Implementation / experiment:** Earlier item/raster metadata inspection, now transcribed from the owner's supplied record; no new probe or decoding implementation.
- **Evidence:** [CDSE reflectance record](evidence/AS_102_CDSE_ACCESS_PROBE.md#reflectance-scaleoffset-discovery); [EV-009](evidence/PRESENTATION_EVIDENCE_INDEX.md).
- **Quantitative result:** Advertised scale `0.0001`, offset `-0.1`, baseline `05.10`; inferred valid-value formula `DN * 0.0001 - 0.1`.
- **Limitation:** No read DN/decoded sample; raw per-band metadata excerpt still needed. L2A BOA reflectance is not automatically aquatic remote-sensing reflectance or HAB evidence.
- **Lesson learned:** Ignoring an advertised offset changes reflectance semantics; do not transfer it to another product without evidence.
- **Impact on next step:** Future handling must mask DN=0 before decoding and avoid automatic clamping of valid negatives; validate the actual product metadata/pixels before implementation.
- **Presentation takeaway:** “Reflectance decoding follows the product's metadata, including its offset.”
- **Recommended visual:** Sanitized scale/offset excerpt and metadata-based formula, labelled as advertised; capture pending.
- **Candidate slide title:** “What do the stored pixel values actually mean?”

### M10 — CDSE raster-access investigation and environmental blocker

- **Date:** Report created 6 October 2026; original probe timestamp not supplied.
- **Task / milestone ID:** AS-102 preparation — CDSE asset access; EV-010.
- **Status:** Recorded metadata investigation and proxy blocker; bounded raster access unverified.
- **Problem / question:** Can the catalog's referenced raster assets be read in the intended runtime?
- **Why it mattered:** Metadata availability does not imply authenticated or windowed pixel access.
- **Options considered:** CDSE's advertised S3/OIDC access route versus a possible alternative raster backend; no successful transport comparison recorded at this point.
- **Decision:** Decision 038 remains CDSE catalog discovery; no raster-provider decision adopted here.
- **Rationale:** Keep access feasibility distinct from AS-101's completed catalog scope.
- **Implementation / experiment:** Selected item metadata inspected; attempted raster/header/window access blocked by the environment proxy; no full raster/product download.
- **Evidence:** [CDSE access probe](evidence/AS_102_CDSE_ACCESS_PROBE.md); [EV-010 index](evidence/PRESENTATION_EVIDENCE_INDEX.md).
- **Quantitative result:** Selected item `S2B_MSIL2A_20230428T064629_N0510_R020_T40RBN_20240831T052931`; 47 assets; nine proposed bands plus SCL and `CLD_20m` available; JP2, EPSG:32640, 10/20 m advertised.
- **Limitation:** Headers, dimensions/dtype, actual authenticated transport, and window/range support unverified; proxy blocking is not a demonstrated provider-side denial.
- **Lesson learned:** Access must be demonstrated at the asset layer separately from the catalog layer.
- **Impact on next step:** Preserve a successful bounded access record before claiming readable pixels; retain original command/timestamp/metadata capture gaps.
- **Presentation takeaway:** “Discovery is one gate; reading pixels is another.”
- **Recommended visual:** Catalog-versus-asset access matrix with an explicit environment proxy boundary; capture pending.
- **Candidate slide title:** “A searchable catalog does not guarantee accessible pixels.”

### M11 — Planetary Computer catalog and advertised COG investigation

- **Date:** Report created 6 October 2026; original experiment timestamp not supplied. Historical checkpoint before asset-host allowlisting and raster reads.
- **Task / milestone ID:** AS-102 preparation — alternative raster backend; EV-011 and EV-013.
- **Status:** Recorded anonymous catalog success; advertised asset metadata; raster access/signing still unverified at this stage.
- **Problem / question:** Does Planetary Computer provide a practical raster-access alternative?
- **Why it mattered:** Public catalog accessibility and advertised COG delivery could reduce access friction, if pixel access is later verified.
- **Options considered:** Existing CDSE discovery/access route versus PC's catalog/COG path; no backend pivot approved.
- **Decision:** Existing CDSE AS-101 decision is unchanged; PC remains a viable investigation rather than an adopted dependency.
- **Rationale:** Handoff §20 and plan §6 distinguish provider evaluation from commitment.
- **Implementation / experiment:** Anonymous STAC/item inspection; identified matching observation and raster host; stopped before raster access because another allowlist update was required.
- **Evidence:** [PC probe](evidence/AS_102_PLANETARY_COMPUTER_PROBE.md); [EV-011/013 index](evidence/PRESENTATION_EVIDENCE_INDEX.md).
- **Quantitative result:** STAC READY / HTTP 200; item `S2B_MSIL2A_20230428T064629_R020_T40RBN_20230428T122311`; nine bands plus SCL; B02 10 m and B05/SCL 20 m COG advertised; host `sentinel2l2a01.blob.core.windows.net`.
- **Limitation:** No separate cloud-probability asset observed in this item; no explicit per-band raster scale/offset advertised. Signing, product-metadata decoding, native headers, and bounded reads unverified at this checkpoint.
- **Lesson learned:** Reachable STAC and a COG description still leave separate asset-access and decoding gates.
- **Impact on next step:** Verify the asset-host/signing path and read product metadata before a tiny-window probe; do not persist signed URLs/tokens.
- **Presentation takeaway:** “An alternative catalog was reachable; its pixel-access path still needed validation.”
- **Recommended visual:** Sanitized catalog-response and host-to-COG diagram labelled as a pre-read checkpoint; capture pending.
- **Candidate slide title:** “Test the path from public catalog to usable raster.”

### M12 — Same acquisition / different processing product

- **Date:** Comparison recorded 6 October 2026; original probe timestamp not supplied.
- **Task / milestone ID:** AS-102 preparation — cross-provider identity; EV-012.
- **Status:** Metadata-supported inference; pixel equivalence unverified.
- **Problem / question:** If two providers represent one observation, do they serve the same processing product?
- **Why it mattered:** A raster backend change must not silently substitute differently processed inputs under the original source identity.
- **Options considered:** Item ID equality versus acquisition/platform/tile/orbit identity; processed-product interchangeability is unsupported.
- **Decision:** Preserve existing provider-qualified source identity; no equivalence/substitution policy adopted here.
- **Rationale:** Decisions 019–020 require the actual raster input's provenance.
- **Implementation / experiment:** Compared the reported CDSE and PC identity/processing fields, without a raster equality test.
- **Evidence:** [Cross-provider table](evidence/AS_102_PLANETARY_COMPUTER_PROBE.md#cross-provider-identity-finding); [CDSE identity](evidence/AS_102_CDSE_ACCESS_PROBE.md#providerstac-advertised-identity); EV-012.
- **Quantitative result:** Both acquire `2023-04-28T06:46:29.024Z`, Sentinel-2B, tile 40RBN, orbit 20. CDSE baseline 05.10/reprocessed Aug 2024; PC baseline 05.09/generated `2023-04-28T12:23:11.362052Z`; different product IDs.
- **Limitation:** Same underlying acquisition does not establish identical processed pixels. No cross-provider pixel comparison or equivalence metric.
- **Lesson learned:** Preserve product provenance as well as observation context.
- **Impact on next step:** If PC later supplies pixels, use a provider-qualified source record for that actual PC product and retain discovery/matching context separately.
- **Presentation takeaway:** “One acquisition, different processing baselines and product identities.”
- **Recommended visual:** Side-by-side identity table from the evidence report, with pixel equivalence explicitly unverified; capture pending.
- **Candidate slide title:** “One observation can have more than one processed product.”

### M13 — AS-102 access-gate status at the documented checkpoint

- **Date:** Repository implementation state documented 3 October 2026; historical probe checkpoint recorded 6 October 2026; exact experiment date not supplied.
- **Task / milestone ID:** AS-102 — Optical Preprocessing readiness boundary; EV-014.
- **Status:** PC catalog READY; raster implementation NOT READY at this evidence point; bounded read PENDING. This is not a later final-gate result.
- **Problem / question:** Is there enough reproducible asset and decoding evidence to begin optical preprocessing?
- **Why it mattered:** Cloud/land/water masks and alignment require readable pixels with defined semantics.
- **Options considered:** CDSE advertised S3/OIDC/JP2 and PC advertised COG path; no final backend, grid, or masking decision recorded.
- **Decision:** AS-102 remains not authorized and not started according to Project State/Handoff; no active development branch.
- **Rationale:** Catalog/metadata feasibility neither proves raster readiness nor authorizes implementation.
- **Implementation / experiment:** Historical metadata/access investigations now documented; no bounded PC read at that stage and no preprocessing package implemented by this task.
- **Evidence:** [PC readiness](evidence/AS_102_PLANETARY_COMPUTER_PROBE.md#readiness-and-next-evidence); [EV-014](evidence/PRESENTATION_EVIDENCE_INDEX.md); Project State §§1, 14–15 and 21–22; Handoff §§3 and 15.
- **Quantitative result:** HTTP 200 catalog result and advertised B02/B05/SCL path; no measured window/DN result, valid-water fraction, or aligned product in this checkpoint.
- **Limitation:** Asset allowlisting/signing, PC scale/offset decoding, bounded reads, and any later final-gate report remain evidence gaps here; do not claim latest external readiness from this historical stage.
- **Lesson learned:** Keep feasibility, authorization, implementation, and scientific validation as separate states.
- **Impact on next step:** Record any later gate as a separately dated experiment, then seek explicit AS-102 implementation authorization; do not start AS-103.
- **Presentation takeaway:** “Catalog access worked; a bounded pixel read remained the next evidence gate.”
- **Recommended visual:** Checkpoint readiness matrix with raster reads/decoding marked pending; capture pending.
- **Candidate slide title:** “What was proved before the first bounded raster read?”

## 3. Decision timeline

The decision log is authoritative. Except Decision 038's explicit 2 October selection date, original per-decision dates are not recorded. Decisions 001–037 were documented with continuity setup on 2 October; do not imply that numerical order supplies precise event times.

| Recorded period | Decisions | Choice / alternative | Rationale and consequence | Evidence / status |
|---|---|---|---|---|
| 2 Oct continuity record | 001–006 | Track 03 and a defined operator; multi-hazard product with HAB first, oil second | Operational decision drives scope, rather than a generic map or detector | Decision log; current product commitments |
| 2 Oct continuity record | 007–010 | S2 optical, S1 SAR; hyperspectral P1, no native-813 requirement | Sensor suitability and a P0 path independent of enhancement availability | Decision log; future hazard capabilities |
| 2 Oct continuity record | 011–015 | Explainable baseline before complex ML; independent hazards; human verification | Weak labels and scientific uncertainty preclude confirmatory or autonomous claims | Decision log; current guardrails |
| 2 Oct continuity record | 016–018 | Historical validation; study AOI distinct from operational intake | External event reports and EO findings must remain separate | Decision log; planned validation |
| 2 Oct engineering / continuity record | 019–024 | Provenance first; Python 3.11; `src/`, TOML, GeoJSON | Traceable outputs and reproducible validated inputs | AS-001/002/003 commits; implemented foundations |
| 2 Oct continuity record | 025–029, 035–037 | Repository continuity, multi-machine workflow, isolated accounts, branches, read-only onboarding | Recoverable state and reviewed authorization before development | AS-000C history; completed setup |
| 2 Oct continuity record | 030–034 | Minimal dependencies; catalog before imagery; preferred future Streamlit; cache fallback; protect P0 | Delivery reliability and evidence precede sophistication | Decision log; UI/cache remain plans |
| Explicitly 2 Oct | 038 | Configurable CDSE catalog; `pystac-client==0.9.0` only new direct dependency | Owner selection and tested real discovery without raster scope | AS-101 report and commits; implemented |
| 3 Oct merge record | No new technical decision | Close AS-101 status after PR #2; preserve AS-102 authorization boundary | Documents must match merged engineering state | `cf1ed23`, PR #3 / `acbe2c1`; completed docs |
| Investigations recorded 6 Oct; original probe timestamps missing | None adopted | CDSE scale/offset/access blocker, PC catalog/advertised COGs, cross-provider product distinction | Metadata and access findings are documented; backend/processing decisions remain pending | M09–M13; [evidence index](evidence/PRESENTATION_EVIDENCE_INDEX.md); no technical decision changed |

Pending decisions remain pending: task-required geospatial dependencies, final operational demo site, usable hyperspectral event/site, and fitted ML selection. The PRD's broad stack is a suggested future stack, not the installed dependency inventory.

## 4. Engineering evidence index

| ID | Evidence location | What it supports | What it does not support |
|---|---|---|---|
| E01 | [pyproject.toml](../pyproject.toml), [README](../README.md), `f878acc` | Python range `>=3.11,<3.12`, package/test/lint foundation | Fully locked environment or an implemented application UI |
| E02 | [config](../src/aquasentinel/config/), [runtime](../src/aquasentinel/runtime.py), [tests](../tests/config/), `f606ac5` / `113ca44` | Validated config/AOI and runtime inputs | A real intake geometry or validated risk weights |
| E03 | [provenance](../src/aquasentinel/provenance/), [tests](../tests/provenance/), `e2baedc` / `db79260` | Schema 1.0, validation, serialization, registry, lineage persistence | Real derived hazard/risk/alert products |
| E04 | [AGENTS](../AGENTS.md), state/handoff/decisions, [plans](../.agent/PLANS.md), AS-000C commits | Recoverable project context and recorded onboarding completion | A tracked copy of the original full audit report |
| E05 | [catalog/stac.py](../src/aquasentinel/catalog/stac.py), [catalog tests](../tests/catalog/test_stac.py) | Real client logic with offline HTTP fixtures; complete pagination and explicit errors | A raster data-access implementation |
| E06 | [ingestion/sentinel2.py](../src/aquasentinel/ingestion/sentinel2.py), [tests](../tests/ingestion/test_sentinel2.py) | Candidate normalization, sorting, duplicates, filters, source mapping | Pixel scale/offset, native grid, mask policy |
| E07 | [AS-101 report](AS_101_STAC_SEARCH.md), Decision 038 | Dated live CDSE query and reproduction instructions | Permanent catalog count or asset-read success |
| E08 | [loader](../src/aquasentinel/config/loader.py), [test_catalog.py](../tests/config/test_catalog.py), `f57f6bf` | Strict TOML cloud typing before network requests | A general refactor of all config coercions |
| E09 | AS-101 report; history `b3f0e9f` → `35caa90` → `cf1ed23` | Historical 92 and current 97 passing-test baselines; preserved 17 original tests | Detection accuracy, coverage percentage, or service SLA |
| E10 | PR #2 / `1b83a73`; PR #3 / `acbe2c1` | Implementation merge and post-merge closeout on main | AS-102 authorization or completion |
| E11 | [.gitignore](../.gitignore), config cache path, Decision 033 | Large EO/cache/secret exclusions and demo-fallback requirement | A completed cached raster demo |
| E12 | [CDSE report](evidence/AS_102_CDSE_ACCESS_PROBE.md), [PC report](evidence/AS_102_PLANETARY_COMPUTER_PROBE.md), [EV-009–EV-014](evidence/PRESENTATION_EVIDENCE_INDEX.md) | Owner-supplied record of metadata/blocked access/catalog success and product-identity comparison | Successful raster reads/signing/decoding at the documented pre-read checkpoint; later final-gate result |

Reproduce the engineering quality gate with `git diff --check`, `python -m pytest -v`, and `python -m ruff check .` in the Python 3.11 environment. Record fresh results separately from historical results. Do not rerun a live probe and silently rewrite the original 44-scene observation.

Journal-task validation on 6 October 2026: the existing `.venv` used Python 3.11.16; `python -m pytest -v` reported **97 passed in 0.20s**, and `python -m ruff check .` reported **All checks passed!** No live catalog or raster experiment was rerun. Whitespace validation also checks the new untracked file with `git diff --no-index --check /dev/null docs/PRESENTATION_JOURNAL.md`, because plain `git diff --check` does not include untracked files.

## 5. Scientific evidence index

| ID | Evidence | Scientific meaning / permitted claim | Boundary |
|---|---|---|---|
| S01 | Decisions 014–015; PRD §5 | Intended outputs support awareness and field verification | No toxin/species/petroleum confirmation, definitive safe/unsafe certification, or automatic shutdown |
| S02 | [AOI GeoJSON](../data/aoi/demo_site.geojson); Decisions 017–018 | Explicit analyst-defined Al Raha study area | Not an official boundary or operational intake |
| S03 | AS-101 live-result record | Candidate L2A metadata is available in the chosen AOI/window | Cloud metadata is scene-wide; usable water pixels not demonstrated |
| S04 | Provenance schema/tests and AS-101 conversion record | Observations retain source/product/time/catalog identity | Traceability does not itself validate reflectance or a hazard |
| S05 | Decision 016; PRD §11 | Al Raha April 2023 and Kharg May 2026 are historical validation candidates | No completed event analysis, labelled dataset, or laboratory confirmation in tracked evidence |
| S06 | Decisions 011–013; configured weights | Explainable, separately interpretable hazards and tunable PoC hypotheses | No fitted classifier, validated weights, or measured risk calibration |
| S07 | Decision 008 | SAR roughness anomalies can motivate slick-candidate analysis | Low-wind and natural-film look-alikes must be reviewed; no implemented oil result yet |
| S08 | [CDSE reflectance metadata](evidence/AS_102_CDSE_ACCESS_PROBE.md#reflectance-scaleoffset-discovery); M09 | Advertised scale 0.0001/offset -0.1 imply `DN * 0.0001 - 0.1`; mask DN=0 first, do not automatically clamp valid negatives | No decoded pixel verification; L2A BOA reflectance is not automatically aquatic remote-sensing reflectance |
| S09 | [PC identity comparison](evidence/AS_102_PLANETARY_COMPUTER_PROBE.md#cross-provider-identity-finding); M12 | Metadata supports same acquisition but different baseline/product identity | No pixel equivalence; actual raster product needs its own provenance |
| S10 | [CDSE quality assets](evidence/AS_102_CDSE_ACCESS_PROBE.md#advertised-assets-format-and-grid); [PC inventory](evidence/AS_102_PLANETARY_COMPUTER_PROBE.md#asset-inventory-and-advertised-delivery-path) | SCL available in both; `CLD_20m` observed in CDSE; no separate cloud-probability asset observed in the inspected PC item | No quality-mask performance, usable-water fraction, or collection-wide absence claim |

No measured HAB accuracy, false-positive rate, temporal lead time, intake exposure, or avoided loss is available in the repository. The presentation must distinguish motivation, planned method, measured engineering evidence, and future scientific validation.

## 6. Failures / blockers / pivots

| Topic | Classification | Repository-supported observation | Response / lesson | Presentation restriction |
|---|---|---|---|---|
| TOML boolean becomes `1.0` through coercion | Fixed review defect | `f57f6bf` changes the loader and adds numeric/invalid-input tests | Reject invalid types before converting or requesting the catalog | May show the actual before/after diff; not a measured environmental failure |
| Pagination cycles, malformed pages, conflicting duplicates | Tested failure modes | AS-101 code/tests explicitly reject these cases | Explicit failure is safer than silently returning partial evidence | Do not claim the live provider exhibited all fixture failure modes |
| Raster access after catalog search | Recorded environmental blocker | [CDSE report](evidence/AS_102_CDSE_ACCESS_PROBE.md): proxy blocked raster/header/window attempts; S3/OIDC route advertised | Separate catalog success, runtime blocking, and provider access requirements | No successful bounded CDSE read or universal provider-denial claim |
| Reflectance offset discovery | Advertised metadata finding; pixel verification pending | CDSE scale 0.0001/offset -0.1 recorded for selected baseline-05.10 product | Use product-specific metadata; capture sanitized per-band excerpts | Formula is metadata-derived, not an observed decoded-pixel result |
| Planetary Computer / allowlist / signing | Recorded catalog success and historical asset-host blocker | [PC report](evidence/AS_102_PLANETARY_COMPUTER_PROBE.md): HTTP 200; additional blob-host allowlist needed | Advertised COG path remains viable; signing/decoding/read still pending at this stage | No provider pivot, successful signing, or successful raster read claimed |
| Same observation, different processing product | Metadata-supported finding | Acquisition/platform/tile/orbit match; CDSE 05.10/Aug 2024 versus PC 05.09/Apr 2023 | Preserve actual product identity if provider supplies pixels | Same acquisition does not imply pixel equivalence |
| Live services, cloud, labels, SAR look-alikes | Anticipated risks, not necessarily observed failures | PRD risk register and Project State §18 | Cached fallback, conservative claims, transparent baselines, false-positive review | Keep planned mitigations distinct from completed work |
| PRD calendar versus current delivery | Schedule plan versus actual state | Planned 3 Oct preprocessing does not override recorded AS-102 not-started status | Use commits and state docs for the completed timeline | Do not present the entire planned calendar as achieved |

No provider-to-provider architecture pivot is adopted. The new reports preserve the historical access/metadata findings, while bounded reads, PC decoding, and later final-gate evidence remain outside the documented checkpoint. Missing raw transcripts/timestamps/screenshots are capture gaps, not claims that the investigations never occurred.

## 7. Metrics and quantitative results

| Metric | Recorded value | Date / source | Interpretation |
|---|---|---|---|
| AS-003 quality baseline | 17 tests passed; Ruff passed | 2 Oct; Project State §9 | Historical whole-project baseline; preserve as history |
| Initial AS-101 quality baseline | 92 tests passed; Ruff/diff check passed | 2 Oct documentation at `b3f0e9f` | Superseded by review fixes; not current baseline |
| AS-101 reviewed baseline | 97 tests passed; Ruff/diff check passed | Review docs `35caa90`; current AS-101 report | Engineering validation, not scientific accuracy |
| Added cloud-type cases | 5: 2 accepted numeric, 3 rejected literals | `f57f6bf`; config tests | Explains 92 → 97; invalid cases make zero catalog calls |
| Live catalog result | 44 unique candidate products | 2 Oct; AS-101 report | Not 44 independent dates, water-valid scenes, or detections |
| Provenance conversion/serialization | 44/44 successful | Same recorded live experiment | Valid source records for all candidates |
| Acquisition span | 4 Mar 06:47:51.024Z – 28 May 06:46:29.024Z, 2023 | AS-101 report | Returned temporal coverage only |
| Observed scene cloud cover | 0.12–24.96% | AS-101 report | Not AOI-specific clear-water fraction |
| Query settings | 1 Mar–31 May 2023; <= 30% scene cloud | Config/report | Input constraints, not performance results |
| First candidate asset references | 47 | AS-101 report | Inventory count; no raster access implied |
| Metadata request timeout | 30 seconds default | Config/Decision 038 | Per request; not total duration or measured latency |
| New direct AS-101 dependency | 1: `pystac-client==0.9.0` | pyproject / Decision 038 | No raster-processing stack adopted |
| Provenance schema | 1.0 | Provenance serialization / Project State | Schema version, not product maturity score |
| Selected CDSE item's assets | 47 | [CDSE probe record](evidence/AS_102_CDSE_ACCESS_PROBE.md) | Separate from the first March candidate's 47 references |
| CDSE advertised raster conversion | Scale 0.0001; offset -0.1 | CDSE probe metadata record; original probe date not supplied | Metadata-derived formula; no read DN/decoded sample |
| PC anonymous STAC | READY / HTTP 200 | [PC historical checkpoint](evidence/AS_102_PLANETARY_COMPUTER_PROBE.md) | Catalog access, not successful raster access |
| PC advertised probe assets | B02 10 m; B05 and SCL 20 m COG; nine reflectance bands available | PC item-inspection record | No native header or bounded read verified at this point |
| Cross-provider processing versions | CDSE 05.10/Aug 2024; PC 05.09/Apr 2023 | PC identity comparison | Same acquisition/platform/tile/orbit; different processed product |
| Bounded PC raster read | PENDING | EV-014; pre-read evidence point | No window/DN result; any later gate requires a separate dated record |
| PoC deadline | 11 October 2026 | PRD | Delivery target, not evidence of readiness |

Unavailable metrics: successful bounded raster reads, transfer bytes, reflectance sample checks, valid-water counts/fractions, preprocessing runtime, accuracy/false positives, warning lead time, buyer validation, or avoided operating cost. Do not fabricate these to fill slides.

## 8. Presentation visual / screenshot inventory

No presentation screenshot/image assets are tracked in the inspected repository. The PRD contains a text architecture diagram; source documents, tests, and Git history are available to capture. The following are **recommended future visuals**, not existing screenshots or generated artifacts.

| Visual ID | Proposed visual | Evidence basis | Capture status / constraint |
|---|---|---|---|
| V01 | Operator, offshore concern, verification decision | PRD §§1–5; Decisions 001–004 | Planned diagram; label product value as intended, not measured |
| V02 | Implemented versus planned architecture | PRD §9; tracked source tree | Text diagram exists; slide rendering pending; mark preprocessing/hazards/UI as future |
| V03 | Foundation/continuity/AS-101 timeline | Git history; M02–M08 | Capture pending; distinguish source dates and timezones |
| V04 | Al Raha study polygon and public reference point | GeoJSON; Decisions 017–018 | Map pending; explicitly “analyst-defined validation AOI,” not intake |
| V05 | Source/derived lineage example | Provenance tests/models; Decisions 019–020 | Capture pending; use a labelled fixture, not an invented real alert |
| V06 | Search constraints and 44/44 evidence card | AS-101 recorded result | Layout pending; state observation date and scene-count caveats |
| V07 | Tiny candidate metadata table | Five real example rows in AS-101 report | Capture pending; retain exact IDs/cloud values; no complete timeline inference |
| V08 | Cloud-type review diff and 97-test summary | `f57f6bf`; tests; quality record | Capture pending; show actual run result and interpreter when captured |
| V09 | CDSE reflectance metadata and formula | M09; [CDSE report](evidence/AS_102_CDSE_ACCESS_PROBE.md) | Report available; sanitized original metadata capture pending; label as advertised, not pixel-verified |
| V10 | CDSE/PC access and product-identity comparison | M10–M12; [PC report](evidence/AS_102_PLANETARY_COMPUTER_PROBE.md) | Comparison table available; rendered visual/original response capture pending; raster read still pending at this checkpoint; never show SAS URLs/tokens |
| V11 | Before/event/after water evidence and mask map | PRD §§11, 17; AS-108 plan | Future scientific validation; no actual result available |
| V12 | Separate HAB/oil evidence and monitoring-priority panels | PRD §§13, 17 | Future dashboard/demo; do not present mockups as implemented software |

For every captured visual, record its path, date, evidence IDs, source/product identity where relevant, caption, licence/attribution, and limitations. Large rasters and runtime caches remain excluded from Git; screenshots must contain no credentials or private operational information.

## 9. Lessons learned

These are interpretations supported by the reconstructed evidence, not new technical decisions.

1. **Define the operational question first.** Decisions 001–004 link sensors to monitoring priority for a specific user; no demonstrated commercial impact yet.
2. **Separate validation geometry from deployment claims.** Decisions 017–018 prevent an accessible study polygon from becoming a falsely implied intake.
3. **Build traceability before live ingestion.** AS-003 enabled AS-101 to validate every candidate as a source record without changing provenance.
4. **Make handoffs recoverable.** AS-000C records context and authorization in Git; the new M09–M13 reports preserve prior investigations while exposing remaining timestamp/transcript/capture gaps.
5. **Catalog completeness is a correctness concern.** AS-101 consumes pagination and rejects malformed/incomplete results rather than returning quiet partial success.
6. **Validate input meaning before conversion.** The cloud boolean fix preserves the user's configured threshold and adds explicit pre-network evidence.
7. **Software evidence and scientific evidence answer different questions.** 97 passing tests and 44 catalog candidates do not establish water-pixel usability or hazard performance.
8. **Minimal dependencies protect scope.** AS-101 adds a STAC client only; the broader PRD tool list is not a mandate to install everything.
9. **A presentation needs an evidence trail too.** Probe records now preserve product identity and reported findings; original commands/timestamps, pixel verification, and visuals remain explicit gaps. Advertised COGs and a matching acquisition do not prove readable or identical pixels.
10. **Plans are not completion records.** AS-101's merge is evidenced; planned optical, feature, hazard, risk, and UI milestones remain future work.

## 10. Final-presentation slide candidates

This is a proposed 7-slide spine, consistent with the PRD's 5–7-slide target. It is not a final deck or a claim that the full PoC is submission-ready. Detailed milestone titles above can become appendix material.

| Slide | Candidate title / story | Evidence / visual | Readiness |
|---|---|---|---|
| 1 | “Watch the sea before a threat reaches the intake” — user, problem, verification decision | M01, S01; V01 | Thesis supported; operational benefit remains intended |
| 2 | “The right sensor for each hazard” — S2 biology, S1 slick candidates, optional hyperspectral | Decisions 005–015; V02 | Scope supported; hazard results not built |
| 3 | “Build the evidence trail first” — config/AOI, provenance, recoverable handoffs | M02–M05; V03–V05 | Engineering supported; visuals pending |
| 4 | “44 real candidates, every source traceable” — real CDSE query and its limits | M06–M07; E05–E07; V06–V07 | Live metadata evidence supported |
| 5 | “Public data access must work at the pixel level” — proxy blocker, advertised offset/COGs, same acquisition but different product | M09–M13; EV-009–EV-014; V09–V10 | Historical metadata/access story supported by reports; captures pending; no successful bounded read at this evidence point |
| 6 | “From usable water pixels to a defensible anomaly” — masks, before/event/after, false positives, exposure | PRD §§6, 11, 17; V11–V12 | Future work; no AS-102/103 or event result claim |
| 7 | “Monitoring priority with evidence and limits” — intended workflow, 97-test baseline, reproducibility, next steps | M08; S01–S08; V08 | Engineering supported; end-to-end demo and impact evidence outstanding |

For a presentation made from this evidence pack, slide 5 must label provider-advertised versus observed/inferred findings and preserve EV-014's PENDING state at the historical checkpoint. Slide 6 must describe future work or be omitted. Never replace missing real scientific evidence with an unlabelled simulation. Business subscriptions/licences in PRD §23 are hypotheses, not validated pricing or revenue.

## 11. Outstanding evidence still needed

| Priority / category | Missing evidence | Required record before a presentation claim |
|---|---|---|
| Immediate capture | CDSE reflectance metadata verification | Formula/baseline now in [CDSE report](evidence/AS_102_CDSE_ACCESS_PROBE.md); still need original per-band metadata excerpt, timestamp, and actual decoded sample verification |
| Access verification / capture | CDSE raster investigation follow-up | Proxy blocker and advertised route recorded; still need original commands/hosts/tool context and bounded transport/header/window result |
| Access verification / capture | Planetary Computer follow-up | HTTP 200 and advertised assets recorded; still need original timestamp/metadata capture, signing evidence, product-metadata decoding, and bounded read |
| Identity capture | Same acquisition / different processing product | Comparison now in [PC report](evidence/AS_102_PLANETARY_COMPUTER_PROBE.md#cross-provider-identity-finding); original metadata excerpts/rendered comparison pending; pixel equivalence unverified |
| Access verification | Later AS-102 final access gate | EV-014 remains PENDING at the recorded pre-read point; any later result needs separately dated methods/results, without rewriting the earlier checkpoint |
| P0 implementation evidence | AS-102 optical preprocessing | Separate explicit authorization, approved contract, tests, real-data acceptance, masks/alignment/valid-water result, derived provenance; not started here |
| P0 scientific evidence | HAB and oil historical validation | Cited event references, usable observations, before/during/after, false-positive review, uncertainty, temporally separated evaluation |
| P0 product evidence | Operational site and decision demo | Defensible public site/intake source; clearly separated validation AOI; working hazard-specific evidence/priority workflow |
| P0 reproducibility | Cached fallback and clean-environment demo | Reproducible small demo assets/manifests and documented fallback; no raw scenes or secrets in Git |
| P0 presentation | Captured visuals, demo recording, attribution | Real screenshots/figures linked to evidence IDs, metadata/licences, limitations, dated 90–180-second recording |
| Scientific/impact claim | Lead time, accuracy, operational benefit | Measurement method, reference labels/timing, limitations; omit claims until supported |
| P1 only | Hyperspectral/environmental enhancement | Demonstrated usable data and measurable contribution; must not block core P0 |

The new probe records were created before this journal update and transcribe the owner's supplied evidence. They resolve earlier blanket “no report” gaps only for the findings actually supplied. Remaining capture/verification gaps do not assert that later experiments failed or never happened. No source/test/configuration or decision-log change is made by this documentation task.

## 12. Reusable milestone-entry template

Copy the following for each meaningful milestone, major review, data probe, failure, or decision. Write “not recorded,” “not measured,” or “pending” when evidence is missing.

```markdown
### Mxx — Milestone name

- **Date:** Event date/timezone; separately record report/commit date if different.
- **Task / milestone ID:** Existing task ID or clearly labelled investigation.
- **Status:** Completed fact / current decision / recorded experiment / blocker / evidence gap / future plan.
- **Problem / question:** What uncertainty or user need was addressed?
- **Why it mattered:** Product, engineering, scientific, or delivery consequence.
- **Options considered:** Only recorded alternatives; say if none are recorded.
- **Decision:** Existing approved decision ID, or pending; this entry alone is not approval.
- **Rationale:** Evidence supporting the choice and its tradeoffs.
- **Implementation / experiment:** Exact bounded work performed, environment/tools, inputs.
- **Evidence:** Relative repository paths, section/evidence IDs, full commit SHA/PR,
  sanitized provider records and reproduction method where relevant.
- **Quantitative result:** Values, units, denominator, observation date, and uncertainty;
  distinguish measured results from settings and planned targets.
- **Limitation:** What the evidence cannot establish; missing ground truth or access.
- **Lesson learned:** Interpretation supported by the evidence, not invented impact.
- **Impact on next step:** Prerequisites, remaining gaps, and authorization boundary.
- **Presentation takeaway:** A defensible sentence with an appropriate status label.
- **Recommended visual:** Existing artifact path or planned capture; caption/attribution.
- **Candidate slide title:** A title that does not overclaim the result.
```

For external data, also record provider, collection, item/product ID, observation identity, processing version, stable unsigned source references, metadata origin, licence, and lineage impact. If a result changes, preserve the old dated result and add the new one with its cause; do not silently replace history. Never store credentials, SAS tokens, private keys, full raw scenes, or runtime caches as evidence.

## Presentation Update Rule

Future agents must update this journal after every meaningful milestone or major decision, within the authorized documentation scope. Add a dated milestone entry with all template fields and repository evidence; update the timeline, evidence indexes, metrics, blocker state, visual inventory, and slide candidates affected by it.

Record successful and failed experiments, options considered, reasons, quantitative outcomes, limitations, and lessons while the evidence is available. Preserve historical baselines and prior decision rationale. Label proposed work and missing evidence explicitly; never promote chat memory, intended work, synthetic examples, or an access probe into completed implementation or scientific validation.

Cross-check new entries against Project State, Handoff, Decisions, the PRD, tests/code, and Git history. An approved technical change belongs in the decision log through a separately authorized task; this journal only records and explains it. Keep feasibility, authorization, implementation, merge status, and validation distinct. Do not mark AS-102 implemented or start AS-103 through a presentation update. Capture sanitized visual references and exact reproduction evidence without secrets or large EO files.
