# AquaSentinel 813 — Hackathon Submission Source of Truth

This file is the single authoritative repository source for Arab Youth Space Hackathon 2026 submission requirements, registration/theme state, judging criteria, official program data ecosystem, and submission-readiness rules.

- Engineering implementation/status → [PROJECT_STATE.md](PROJECT_STATE.md).
- Scientific/design decisions → [DECISIONS.md](DECISIONS.md).
- Agent execution rules → [AGENTS.md](../AGENTS.md) and [.agent/PLANS.md](../.agent/PLANS.md).
- Do not duplicate hackathon/submission facts into those files; link to this document instead.

## 1. Authority and source provenance

Organizer rules and guide/starter facts below are supplied in the project owner's documentation authorizations. The current update adds the official Onboarding Guide, organizer-linked starter repository, current PoC Submission Guide, owner-supplied Cockpit/form state and the read-only Submission Gap Audit. This task does not claim independent inspection of authenticated platform pages or organizer guide/notebook content.

| Source | Reference | Provenance / role |
|---|---|---|
| Current live platform / team Cockpit | https://spaceacademy-hackathons.space.gov.ae/ | OWNER_SUPPLIED_COCKPIT_SNAPSHOT: registered challenge, approved team with three listed members, edit restrictions; no personal member details stored |
| Current PoC Submission form | https://spaceacademy-hackathons.space.gov.ae/poc-submission | OWNER_SUPPLIED_FORM_SNAPSHOT: fields, limits and current empty/unchecked upload/form state; not independently authenticated inspection |
| Current official Space Academy Onboarding Guide | Organizer guide; no distinct direct guide URL supplied in this update | Current theme taxonomy, PoC access phases and notebook/topic mapping supplied by the owner |
| Current PoC Submission Guide - Arab Youth Space Hackathon | https://spaceacademy-hackathons.space.gov.ae/guides/poc-submission-guide.html | Current deadline, validation/submission requirements, English requirement, reproducibility and presentation guidance supplied by the owner |
| Organizer-linked 813-hyperspectral-hackathon repository | https://github.com/Tnecniv-Teikram/813-hyperspectral-hackathon | Training/starter/Tanager examples; earlier taxonomy and timeline remain visible but do not control current rules |
| Older organizer orientation / introductory webinar materials | Organizer-supplied materials; no distinct recording URL supplied | Historical worked example, theme context and judging guidance |
| Organizer data/training materials | https://spaceacademy-hackathons.space.gov.ae/data | Broader program ecosystem; listing alone does not establish current PoC entitlement |
| Read-only Submission Gap Audit | Official main e137795686d8f97bbd8ba6bc0465616783586ae0; repository files referenced in §13 | Artifact readiness, not new science or organizer validation |

The repository's PRIVATE visibility was confirmed by read-only GitHub repository metadata in this update. Evaluator access was not verified. Organizer source-access timestamps are not established by this task; do not invent them. Later changes must retain their provenance and source conflicts.

No personal email, phone number, account identifier, browser state, saved page or screenshot is stored here. Public source and repository URLs are references, not evidence of evaluator access.

## Source precedence when organizer materials conflict

1. **Current live submission form / team Cockpit** governs actual current team registration, displayed registered challenge/theme, current submission fields, upload limits and platform state. The recorded snapshots are owner-supplied; they do not imply Codex authenticated inspection.
2. **Current official Space Academy Onboarding Guide and PoC Submission Guide** govern current program rules, theme taxonomy, PoC access phase, validation/submission requirements and judging guidance.
3. **Organizer-linked GitHub starter repository** governs training material, starter notebooks, technical examples and Tanager STAC examples. It does **not** govern current theme numbering, deadline or data-access entitlement where it conflicts with the current platform/guides.
4. **Older webinar/orientation material** remains historical organizer context; it must not silently override newer live/current sources.

**Never erase a conflict. Record it and identify which source governs the current operational decision.** This precedence is administrative source governance, not a change to scientific policies.

## 2. Registration and versioned theme taxonomy

### A. Current team registration — owner-supplied Cockpit state

The actual currently displayed administrative challenge label is **Urban Expansion, Land Use Change & Heat Risk**. The supplied Cockpit state indicates an approved team with **three listed members**; formal final validation eligibility remains unverified. No personal roster data is stored.

The platform indicates that direct team-information edits are locked after approval; organizers should be contacted for updates. No registration change is established.

### B. Current official Onboarding taxonomy — organizer rules

| Current theme | Current Onboarding label |
|---|---|
| Theme 01 | Climate Resilience & Disaster Recovery |
| Theme 02 | Precision Agriculture & Crop Intelligence |
| Theme 03 | Marine & Water Security |
| Theme 04 | Blue Carbon & Mangrove Health |
| Theme 05 | Sustainable Urban Planning & Smart Cities |
| Theme 06 | Air Quality & Environmental Intelligence |

Theme 03 asks about unusual water-colour/turbidity patterns and possible bloom-related signals. It recommends starting with Sentinel-2 and adding open hyperspectral data for detailed spectral investigation.

### C. Organizer-linked GitHub starter taxonomy — earlier training version

The starter repository uses an earlier/different taxonomy, including:

- **Theme 2 — Urban Expansion, Land Use Change & Heat Risk**.
- **Theme 6 — Water Quality & Inland/Coastal Water Intelligence**.

Retain this training taxonomy unchanged. The starter's Theme 6 number is not the current Onboarding/platform theme number. The current Onboarding Guide governs current taxonomy; the live Cockpit governs the team's actual displayed registration. Neither establishes that the mismatch has been resolved.

### D. AquaSentinel substantive alignment — project interpretation

AquaSentinel aligns with the **marine/water problem family**: HAB-like / biological water-quality screening, coastal anomaly monitoring, desalination-intake monitoring priority and surface-slick observational evidence. This is substantive alignment, not proof of changed registration or implemented exposure assessment. Actual engineering state belongs in PROJECT_STATE.md.

Older orientation examples explicitly include harmful algal blooms / Red Tides, salinity, protecting desalination intakes, spectral water-quality indicators and early bloom detection in the Gulf for a desalination operator. They remain context, not a substitute for current taxonomy.

### Administrative state

```text
THEME_TAXONOMY_STATUS = VERSION_CONFLICT_DOCUMENTED
REGISTERED_THEME_LABEL = Urban Expansion, Land Use Change & Heat Risk
AQUASENTINEL_SUBSTANTIVE_ALIGNMENT = MARINE_WATER
CURRENT_ONBOARDING_THEME = Theme 03 — Marine & Water Security
STARTER_REPO_WATER_THEME = Theme 6 — Water Quality & Inland/Coastal Water Intelligence
FINAL_SUBMISSION_THEME_LABEL = PENDING_ORGANIZER_CONFIRMATION
THEME_ALIGNMENT_STATUS = EXTERNAL_ACTION_REQUIRED
```

Organizer confirmation/correction is required so the submission form, README and title slide use one consistent official theme. Historical product/theme choices in DECISIONS.md do not establish current platform registration.

## 3. Official timeline

| Milestone | Organizer date / rule |
|---|---|
| Submissions opened | 25 September 2026 |
| Final PoC deadline | 11 October 2026, 23:59 |
| Deadline interpretation | Local time of the team creator |
| Commit cutoff | Commits pushed after the deadline are not part of the submission |
| Validation | 12–13 October 2026 |
| Pitching & judging | 14–16 October 2026 |

### Timeline-source conflict

The organizer-linked GitHub starter repository contains older timeline material, including a **later PoC submission date**. The exact older date is not supplied in this update and is not invented here. Preserve the conflict; that training timeline does not replace the current operational deadline.

```text
SUBMISSION_DEADLINE_SOURCE = CURRENT_POC_SUBMISSION_GUIDE_AND_PLATFORM
OLDER_STARTER_REPO_TIMELINE = HISTORICAL_NON_CONTROLLING
```

Current operational deadline remains **11 October 2026, 23:59, local time of the team creator**. Commits pushed after the applicable current deadline are not part of the submission.

**The team creator's timezone has not been explicitly verified.** Do not infer it from the AOI, country, development environment, historical engineering timestamps or this repository. Confirm it from the platform/account before interpreting the cutoff in UTC or another timezone.

## 4. Current PoC Submission form contract

| Visible field | Contract |
|---|---|
| Project title | Required project-title field; final title is not drafted here |
| One-line summary / what the PoC does | Maximum 2,000 characters; final summary is not drafted here |
| GitHub repository URL | Public repository or private repository with evaluator access |
| Presentation slides | PDF only; maximum 50 MB |
| Supporting archive | Optional ZIP; maximum 200 MB |

Visible confirmations concern a repository containing:

- README.
- A Jupyter notebook that runs end to end.
- Pinned requirements.txt.
- Example input and output.
- No credentials or restricted imagery.
- Access for organizers/the evaluation account.

### Current form snapshot — separate from organizer requirements

Provenance: **OWNER_SUPPLIED_FORM_SNAPSHOT**, not independently authenticated platform inspection. The supplied snapshot showed:

- No presentation PDF selected.
- Project title empty.
- Summary empty.
- GitHub URL empty.
- Confirmation checkboxes unchecked: **UNSATISFIED_IN_OWNER_SNAPSHOT**.

The known repository URL is https://github.com/Omar-Aboulwafa/aquasentinel-813 ; that does not mean the form field was populated. No submission receipt is verified.

**English is REQUIRED** under the current official submission requirements supplied in this update. English README/documentation alone does not satisfy readiness for notebook narration and slides that do not yet exist.

Recording the form contract does not mean its confirmations have been satisfied or submitted.

## 5. Automated validation and eligibility

These are **BLOCKING** requirements:

1. Submission before the deadline.
2. Eligible registered team and members.
3. Accessible repository.
4. Non-empty root README.md.
5. At least one functioning executable .ipynb.
6. requirements.txt / dependency file as required by the guide, with pinned versions.
7. Sample input committed OR an exact reproducible retrieval script.
8. Committed example output.
9. README describing the problem and business use case.
10. README installation/run instructions.
11. Presentation PDF attached.

The current form explicitly confirms pinned requirements.txt. No root requirements.txt exists on audited main, and README does not direct the reviewer to an accepted alternate dependency path. pyproject.toml does not satisfy the current submission requirement; this remains MISSING.

A recognizable repository structure with code/data/results separated is **FLAGGED**, rather than a blocking elimination criterion.

**VALIDATION_PASS != JUDGING_SCORE**

Passing automated validation only makes the project eligible for judging; it does not establish a judging score, scientific accuracy or award outcome.

## 6. Reproducibility contract

The organizer's core objective, paraphrased: a reviewer who has never spoken to the team should be able to clone the repository, follow the README, and reproduce the headline result without contacting the team.

Organizer guidance:

- A clean reproducible notebook is preferable to a half-finished application.
- Use relative paths.
- Restart the kernel and run all cells with no errors.
- Commit visible notebook outputs.
- Keep the repository small.
- Do not commit full scenes, restricted imagery, credentials or tokens.

Engineering test success and historical evidence files alone do not establish a runnable reviewer workflow.

## 7. README contract

The official guide's required/recommended content areas, in order:

1. **Title and one-line summary.**
2. **Business use case.**
3. **Problem.**
4. **Data used:** product, provider, dates, processing level and licence.
5. **Technical approach:** workflow, indices/models/parameters in execution order.
6. **Installation:** exact commands and Python version.
7. **How to run:** notebook, inputs, runtime and expected output.
8. **Example input and output.**
9. **Results and limitations.**
10. **Team, licence and attribution.**

This contract is recorded here; README.md is not rewritten by this task.

## 8. Presentation contract

Slides are submitted as PDF; presentation quality matters in judging. Official recommended flow:

1. Title — project/team/theme/country.
2. Problem and affected user.
3. Business use case / end user.
4. Data — including whether/how hyperspectral is used.
5. Approach/workflow.
6. Actual example outputs.
7. Validation and limitations.
8. Impact.
9. Incubation/next steps.

**Actual result screenshots should be prioritized over stock imagery or diagrams of systems not built.** Do not claim a visual exists unless it exists, or present a proposed capability as implemented.

## 9. Judging criteria

Organizer judging dimensions:

- Problem definition / real-world relevance.
- Technical soundness / robustness / scalability.
- Meaningful EO-data use.
- Product and delivery model / decision support.
- Innovation.
- Business viability.
- Societal/environmental/economic impact and strategic alignment.
- Presentation/communication.

Appropriate hyperspectral use receives bonus / extra credit. Hyperspectral, including Satellite 813, is an advantage and not a mandatory P0 dependency. Bonus guidance does not require forcing hyperspectral data into an unsuitable workflow. No numerical judging weights are supplied here.

## 10. Official program data ecosystem

### Organizer-listed EO/data ecosystem

These are program-listed sensors, products and resources; listing does not establish AquaSentinel use, current access entitlement or a universal reuse licence.

| Listed resource | Organizer context supplied |
|---|---|
| Satellite 813 | Separately organizer-supplied: hyperspectral; approximately 205 bands, approximately 20 m; water quality / vegetation chemistry / materials; native access not guaranteed in Phase 2 |
| Sentinel-1 SAR | GRD, on-demand |
| Sentinel-2 / Copernicus | Program EO resource |
| Landsat 8/9 | Program EO resource |
| PlanetScope | Program EO resource |
| MBZ-SAT | Program EO resource |
| EnMAP hyperspectral | Program hyperspectral resource |
| Tanager-1 hyperspectral | Planet; approximately 426 bands, approximately 30 m, approximately 380–2500 nm; organizer-linked GitHub training description |
| ESA WorldCover | Program data resource |
| WorldPop | Program data resource |
| OpenStreetMap extracts | Program data resource |
| Planet / Planet Developers / Planet open data | Program data/access resources |
| USGS EarthExplorer | Program data/access resource |
| Microsoft Planetary Computer / STAC | Program data/access resource |

### Organizer water-quality starter notebook

**ORGANIZER TRAINING / STARTER REFERENCE — NOT AQUASENTINEL VALIDATION EVIDENCE**

Organizer-linked notebook: **06_ecosystem_health_water_qualityy.ipynb**.
Its documented purpose covers water quality, turbidity, chlorophyll/algal-bloom screening and hyperspectral water analysis. Relevant organizer-linked Tanager collection: **tanager-core-imagery/coastal-water-bodies**.

The current Onboarding Guide maps this notebook to the current Marine & Water topic despite its filename retaining **06**. Do not rename or reinterpret the historical training filename as current theme numbering. The notebook and collection are references, not proof that AquaSentinel used them or accessed their pixels.

### Keep hyperspectral sensors separate

The organizer-linked GitHub repository describes **Tanager-1**, provider **Planet**, with approximately **426 bands**, approximately **30 m** resolution and approximately **380–2500 nm** spectral range. Separately supplied Satellite 813 specifications remain separately attributed above. **Tanager is not Satellite 813.** Planet's Tanager archive does not establish availability of native Satellite 813 imagery.

### Workspace/tooling and current gIQ availability

**gIQ** belongs to the broader Space42/program tooling ecosystem. The current official Onboarding Guide states **no gIQ access during Phase 2 PoC**; it may be provided during Phase 3/incubation. Do not design current reproducibility around gIQ. Python, Jupyter, Google Colab, QGIS, GitHub and AI/ML frameworks remain available workflow options. Cloud-native / small-AOI access is encouraged.

Earlier orientation/program descriptions positioned gIQ as the primary workspace. Retain that broader/historical context, but the current Onboarding Guide governs actual Phase-2 entitlement.

### Current Onboarding access model

| Phase | Confirmed/current scope or conditional future scope |
|---|---|
| Phase 1 — Preparatory & open exploration | Open multispectral data, open hyperspectral data, public starter datasets, GitHub notebooks, local Python/Jupyter/Colab/QGIS |
| Phase 2 — Proof of Concept development | Open multispectral data, open hyperspectral data, and Planet Tanager **open-archive data only** according to organizer examples |
| Phase 3 — Incubation for selected teams | May provide commercial Planet data, gIQ access, Satellite 813 upon availability, MBZ-SAT upon availability, and other project-specific resources only when organizers confirm them |

For current Phase 2: **no commercial Planet data; no gIQ access; no guaranteed Satellite 813 data; no guaranteed MBZ-SAT data**. These are not current PoC dependencies.

**Access-source conflict:** the earlier recorded Phase-2 description of sponsored high-resolution/commercial access aligned with theme/AOI is outdated and does not govern current access. The current Onboarding Guide above governs Phase 2; Phase 3 resources remain conditional, not automatic entitlements.

**P0 must not depend on Phase-3-only or unguaranteed resources.**

The current platform FAQ permits open external public datasets. Pretrained models are allowed when disclosed and licences are respected.

### AquaSentinel implementation providers — separate project fact

The inspected official-main implementation uses CDSE discovery and Planetary Computer source/asset access for Sentinel-2, and the frozen Sentinel-1 retrieval contract also distinguishes CDSE discovery from Planetary Computer access. See PROJECT_STATE.md, DECISIONS.md and the AS-101/AS-102/AS-201 contracts for exact engineering state and source provenance. Organizer listing does not prove successful live access, licensing approval or scientific validity for any particular source.

## 11. Official Marine & Water Security worked example

**ORGANIZER WORKED EXAMPLE — NOT AQUASENTINEL VALIDATION EVIDENCE**

1. Use Sentinel-2 for broad/frequent coastal coverage.
2. Add hyperspectral EnMAP / Satellite 813 over the bloom area.
3. Compute water indices/chlorophyll proxies and classify pixels.
4. Use hyperspectral information to help distinguish bloom signatures from turbidity.
5. Compare dates for spread/change.
6. Map hotspots near the intake.
7. Deliver a dashboard or alert to the desalination operator.

This is organizer context, not a claim that AquaSentinel has implemented each step, confirmed a bloom, measured chlorophyll, identified species/toxins or validated an intake.

## 12. AquaSentinel submission interpretation

**PROJECT INTERPRETATIONS — NOT ORGANIZER RULES**

- AquaSentinel's existing P0 architecture is strongly aligned with the Marine & Water Security problem statement.
- Sentinel-2 HAB monitoring is the strongest direct match to the organizer worked example; actual evidence retains the project's observational scientific boundaries.
- Sentinel-1 oil/surface-slick work is complementary multi-hazard EO capability, not proof of implemented oil detection.
- Satellite 813 / EnMAP hyperspectral can strengthen spectral characterization and judging alignment where scientifically appropriate.
- P0 must remain functional without native Satellite 813 availability.
- Do not sacrifice reproducibility/headline output to force optional hyperspectral integration.

### Submission headline strategy — PROJECT INTERPRETATION — NOT ORGANIZER RULE

The strongest current submission headline candidate is the mature **Sentinel-2 HAB / water-quality pipeline**, rather than making eligibility depend on unfinished Sentinel-1 oil science. The HAB path already contains accepted real EO-derived results and historical case-study evidence. AS-201 is still undergoing engineering interoperability validation; AS-202 and downstream oil science have not started. Organizer validation prioritizes a functioning reproducible notebook and an actual example result.

```text
SUBMISSION_HEADLINE_CANDIDATE = SENTINEL2_HAB_WATER_QUALITY
SENTINEL1_OIL_ROLE = SECONDARY_MULTI_HAZARD_CAPABILITY_UNTIL_COMPLETED
```

This does not freeze final pitch wording or remove the oil roadmap. Refer to PROJECT_STATE.md for engineering detail; this document records only the submission consequence.

### Hyperspectral strategy — PROJECT INTERPRETATION — NOT ORGANIZER RULE

**HYPERSPECTRAL = OPTIONAL_JUDGING_ENHANCEMENT**

Preferred safe strategy: **Sentinel-2 HAB baseline → optional Tanager/EnMAP detailed spectral investigation**. Do not make submission eligibility depend on native Satellite 813 access or force hyperspectral analysis merely for bonus points. Any later Tanager/EnMAP result requires its own reproducible data, provenance and licence handling.

These interpretations neither resolve the registration mismatch nor change scientific/product decisions or authorize further implementation.

## 13. Submission readiness matrix

Read-only Submission Gap Audit baseline: official main **e137795686d8f97bbd8ba6bc0465616783586ae0**, PR #32. **M51 is unmerged and is not part of this repository-readiness snapshot.** Other unmerged engineering/evidence branches are likewise excluded. This update changes only this existing document; the AGENTS.md pointer remains unchanged.

Statuses are **PRESENT_VERIFIED**, **MISSING**, **PARTIAL**, **NOT_YET_VERIFIED**, and **EXTERNAL_ACTION_REQUIRED**. Artifact presence is checked against audited main; owner-supplied platform/form facts are separately labelled. No independent authenticated form/roster inspection, submission receipt or creator timezone is claimed. PRESENT_VERIFIED does not mean organizer validation passed.

The repository is **PRIVATE**, confirmed by read-only GitHub repository metadata. Owner/Codex fetch access is not evaluator access. Either make the repository public or explicitly grant the evaluation account access, then verify in a logged-out/evaluator context.

**Internal accepted scientific evidence is not the submission example output.** AS-107/AS-108 accepted evidence is available, but the required reviewer-facing map, figure, table or exported layer must be produced by the reproducible notebook and shown from the submission workflow. Current evidence JSON/Markdown does not satisfy that final deliverable.

| Requirement | Official status | AquaSentinel status | Evidence/location | Next action |
|---|---|---|---|---|
| Correct official/final submission theme | Registration/submission alignment required | EXTERNAL_ACTION_REQUIRED | Registered challenge differs from substantive alignment; taxonomy versions conflict; §2 | Obtain organizer confirmation |
| Final submission before deadline / receipt | BLOCKING | NOT_YET_VERIFIED | No verified receipt; current deadline governs, §3 | Confirm creator timezone and submit before cutoff; retain receipt |
| Formal team/member validation eligibility | BLOCKING | NOT_YET_VERIFIED | OWNER_SUPPLIED_COCKPIT_SNAPSHOT: approved team with three listed members; final eligibility not verified | Confirm final eligibility without storing personal roster data |
| Evaluator repository access | BLOCKING | EXTERNAL_ACTION_REQUIRED | Repository PRIVATE; evaluator grant not verified; development fetch is insufficient | Make public or grant evaluator access, then verify logged-out/evaluator access |
| Non-empty root README.md | BLOCKING | PRESENT_VERIFIED | Root README inspected and non-empty | Complete remaining contract sections |
| Full README contract | Guide's required/recommended content areas | PARTIAL | Basic project/user/decision text exists; data, install/run and results contract incomplete | Complete §7 contract later |
| README business use case | BLOCKING | PRESENT_VERIFIED | Primary user and operational decision already exist | Retain and expand delivery detail if needed |
| README full problem statement | BLOCKING | PARTIAL | Mission/scope exists, but full problem/event/data explanation is incomplete | Add clear problem statement |
| README installation/run instructions | BLOCKING | MISSING | Python version alone is not install/run commands; README has neither | Add exact installation and headline-result run commands |
| Functioning end-to-end .ipynb | BLOCKING | MISSING | No tracked .ipynb on audited main | Create and verify restart/run-all later |
| Root pinned requirements.txt | BLOCKING; explicit current form confirmation | MISSING | No root requirements.txt; pyproject.toml is not an accepted reviewer dependency path in README | Supply pinned requirements.txt and verify installation |
| Reviewer-ready sample input / exact retrieval workflow | BLOCKING | MISSING | AOI GeoJSON alone is not sufficient EO sample input; no clean submission-level retrieval workflow/script | Supply permitted sample input or an exact reproducible reviewer workflow |
| Reviewer-facing committed example output | BLOCKING | MISSING | No notebook-produced map/figure/table/exported layer in submission workflow; evidence JSON/Markdown is insufficient | Produce and commit an actual notebook example result |
| Accepted internal scientific result available | Internal preparation evidence, not submission-output compliance | PRESENT_VERIFIED | AS_107_REAL_ACCEPTANCE MD/JSON and AS_108_HISTORICAL_CASE_STUDY MD/JSON exist | Reuse accepted evidence as source for later submission output |
| Reviewer-facing results/ artifact | Readiness/structure; directory name is not a separate blocking rule | MISSING | No dedicated reviewer-facing results/ artifact on audited main | Add clear output location later |
| README data/provider/date/processing-level/licence section | README guide area; licence compliance required | MISSING | Detailed provenance elsewhere; consolidated required README section absent | Add verified data/licence/attribution section |
| README results/limitations contract | README guide area | PARTIAL | Scientific guardrails exist; actual results/example presentation incomplete | Add accepted results and limitations without overclaiming |
| English-language submission | REQUIRED | PARTIAL | README/inspected docs English; final notebook narration/slides do not exist | Provide English notebook narration and slides |
| Presentation PDF | BLOCKING; PDF only, ≤50 MB | MISSING | OWNER_SUPPLIED_FORM_SNAPSHOT: no presentation file selected; no tracked PDF | Prepare actual-result PDF and attach within limit |
| Form project title | Current form field | MISSING | OWNER_SUPPLIED_FORM_SNAPSHOT: empty | Draft/confirm later after theme resolution |
| Form summary ≤2,000 characters | Current form limit | MISSING | OWNER_SUPPLIED_FORM_SNAPSHOT: empty | Draft later and verify character count |
| Form GitHub URL | Current form field | MISSING | OWNER_SUPPLIED_FORM_SNAPSHOT: empty; known repo URL does not prove entry | Enter repository URL and verify evaluator access |
| Form confirmation checkboxes | Visible submission confirmations | NOT_YET_VERIFIED | UNSATISFIED_IN_OWNER_SNAPSHOT: unchecked | Satisfy each prerequisite and verify current confirmations |
| Repository code/data/results structure | FLAGGED, not blocking elimination | PARTIAL | src/, tests/, data/, docs/ exist; notebooks/ and reviewer-facing results/ missing | Make reviewer input/code/output locations clear |
| No credentials/restricted imagery | Visible form confirmation | PARTIAL | Existing engineering scans and .gitignore positive; final history/licence review not certified | Complete submission-history and data-permission review |
| Notebook visible outputs and restart/run-all | Reproducibility guidance | MISSING | No notebook | Verify all cells and commit permitted visible outputs |
| Supporting ZIP if used | OPTIONAL; ≤200 MB | NOT_YET_VERIFIED | No optional archive/upload verified | Omit if unnecessary; otherwise verify content/permissions/size |

The matrix is a readiness snapshot, not authorization to repair missing deliverables here. No final title/summary, notebook, README rewrite, presentation output or scientific result is created by this update. The submission is not declared ready, accepted or validated.

## Current submission blockers

**14 current known submission blockers/gaps** are retained below. They include blocking organizer deliverables and unresolved administrative/readiness actions; they are not fourteen separate automated elimination rules.

1. Functioning end-to-end notebook missing.
2. Pinned requirements.txt missing.
3. Reviewer-ready sample input/exact retrieval workflow missing.
4. Reviewer-facing example output missing.
5. README installation/run instructions missing.
6. README full data/licence/results contract incomplete.
7. Presentation PDF missing.
8. Evaluator repository access unresolved because the repository is private.
9. Final submission theme label unresolved.
10. Form project title empty in the owner-supplied snapshot.
11. Form summary empty in the owner-supplied snapshot.
12. Form GitHub URL empty in the owner-supplied snapshot.
13. Form confirmations incomplete in the owner-supplied snapshot.
14. Final submission/receipt not yet verified.

Items 8–9 require external administrative resolution; form state in items 7 and 10–13 is owner-supplied, not independently authenticated inspection. Directory naming/structure is FLAGGED, not a separate blocking criterion by name. English completion is part of the missing notebook/slides readiness. **Unfinished Sentinel-1 oil science is not an automated-submission blocker.** Do not confuse an engineering roadmap gap with organizer eligibility requirements.

## 14. Submission-readiness rules and boundaries

- Resolve theme registration and creator-timezone interpretation externally before final submission.
- Verify each blocking requirement independently; do not replace missing reviewer artifacts with engineering test counts.
- Use the matrix's explicit missing/partial/unverified states until evidence supports an update.
- Keep organizer facts, project interpretation, artifact presence, scientific acceptance and evaluator access distinct.
- Keep scientific claims within existing decisions/evidence; presentation polish does not authorize changing accepted outcomes.
- No provider access, SAR pixel reads, EO processing, live scientific compute or AS-201 correction is performed by this documentation task. Normal offline engineering tests are permitted by AGENTS.md.
- No AS-202 work, new scientific decision, PR creation or merge is authorized here.

## Authority / anti-duplication rule

- Hackathon/submission facts are maintained here only.
- PROJECT_STATE.md must not become a second copy of submission requirements.
- DECISIONS.md must not be used for administrative submission rules.
- Future agents should update this file when organizer requirements change.
- Historical engineering evidence remains in its existing evidence files.
