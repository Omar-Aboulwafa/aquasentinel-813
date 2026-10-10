# AquaSentinel 813 — Hackathon Submission Source of Truth

This file is the single authoritative repository source for Arab Youth Space Hackathon 2026 submission requirements, registration/theme state, judging criteria, official program data ecosystem, and submission-readiness rules.

- Engineering implementation/status → [PROJECT_STATE.md](PROJECT_STATE.md).
- Scientific/design decisions → [DECISIONS.md](DECISIONS.md).
- Agent execution rules → [AGENTS.md](../AGENTS.md) and [.agent/PLANS.md](../.agent/PLANS.md).
- Do not duplicate hackathon/submission facts into those files; link to this document instead.

## 1. Authority and source provenance

The current facts below are derived from organizer-provided/current materials supplied in the project owner's authorization for this documentation task. This task records those supplied facts; it does not claim an independent inspection of authenticated platform pages, accounts, saved HTML, screenshots or webinar recordings.

| Organizer source | Reference | What it establishes here |
|---|---|---|
| Arab Youth Space Hackathon platform / team cockpit | https://spaceacademy-hackathons.space.gov.ae/ | Current registered theme, edit restrictions, timeline and FAQ facts supplied by the owner |
| Current PoC Submission form | https://spaceacademy-hackathons.space.gov.ae/poc-submission | Visible fields, upload limits and confirmations |
| PoC Submission Guide - Arab Youth Space Hackathon | https://spaceacademy-hackathons.space.gov.ae/guides/poc-submission-guide.html | Automated validation, reproducibility, README and presentation guidance |
| Organizer orientation / introductory webinar materials | Organizer-supplied materials; no distinct recording URL supplied | Theme 03, worked example and judging guidance |
| Organizer data/training materials | https://spaceacademy-hackathons.space.gov.ae/data and https://github.com/Tnecniv-Teikram/813-hyperspectral-hackathon | Program data ecosystem, workspace and access phases |

Source access timestamps are not established by this task. Do not invent them. Later organizer changes must be checked against the current form/guide and recorded here with their provenance.

No personal email, phone number, account identifier, browser state, saved page or screenshot is stored here. Public source and repository URLs are references, not account-access evidence.

## 2. Registration and theme alignment

### Organizer/platform facts supplied for this task

**Current registered platform theme shown in the team cockpit:**

**Urban Expansion, Land Use Change & Heat Risk**

**Organizer orientation theme 03:**

**Marine & Water Security**

The Marine & Water Security examples explicitly include harmful algal blooms / Red Tides, salinity, protecting desalination intakes, spectral water-quality indicators, and early bloom detection in the Gulf for a desalination operator.

The platform indicates that direct team-information edits are locked after approval; organizers should be contacted for updates.

### AquaSentinel substantive alignment — project interpretation

AquaSentinel is a marine-intake decision-support PoC focused on HAB-like / biological water-quality anomalies, surface-slick candidates, and desalination-intake exposure/monitoring priority. This is substantive alignment with Marine & Water Security, not proof of registration under that theme or of implemented exposure assessment. Actual implementation remains documented in PROJECT_STATE.md.

### Administrative state

**THEME_ALIGNMENT_STATUS = UNRESOLVED_REGISTRATION_MISMATCH**

No platform theme change is established. Organizer confirmation/correction is required before final submission so the submission form, README and title slide use one consistent official theme. Historical product/theme choices in DECISIONS.md do not establish the current platform registration.

## 3. Official timeline

| Milestone | Organizer date / rule |
|---|---|
| Submissions opened | 25 September 2026 |
| Final PoC deadline | 11 October 2026, 23:59 |
| Deadline interpretation | Local time of the team creator |
| Commit cutoff | Commits pushed after the deadline are not part of the submission |
| Validation | 12–13 October 2026 |
| Pitching & judging | 14–16 October 2026 |

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

Recording these confirmations does not mean they have been satisfied or submitted.

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

The current form explicitly asks for pinned requirements.txt. Do not assume that pyproject.toml alone satisfies that confirmation without organizer/guide confirmation.

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
| Satellite 813 | Hyperspectral; approximately 205 bands, approximately 20 m; water quality / vegetation chemistry / materials |
| Sentinel-1 SAR | GRD, on-demand |
| Sentinel-2 / Copernicus | Program EO resource |
| Landsat 8/9 | Program EO resource |
| PlanetScope | Program EO resource |
| MBZ-SAT | Program EO resource |
| EnMAP hyperspectral | Program hyperspectral resource |
| Tanager-1 hyperspectral | Program hyperspectral resource |
| ESA WorldCover | Program data resource |
| WorldPop | Program data resource |
| OpenStreetMap extracts | Program data resource |
| Planet / Planet Developers / Planet open data | Program data/access resources |
| USGS EarthExplorer | Program data/access resource |
| Microsoft Planetary Computer / STAC | Program data/access resource |

### Workspace/tooling

GIQ is presented as the program's primary geospatial workspace, operated by Space42. Teams may also use Python, Google Colab, QGIS, GitHub and AI/ML frameworks. Cloud-native / small-AOI access is encouraged.

### Access model

1. **Phase 1:** open-access exploration, including Sentinel-2, Landsat, Planet open data and sample hyperspectral scenes.
2. **Phase 2:** sponsored high-resolution/commercial and selected hyperspectral access aligned with theme/AOI.
3. **Phase 3:** premium/tailored AOI-specific data/model-ready inputs for finalist/incubation work.

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

These interpretations neither resolve the registration mismatch nor change scientific/product decisions or authorize further implementation.

## 13. Submission readiness matrix

Read-only repository audit baseline: official main **e137795686d8f97bbd8ba6bc0465616783586ae0**, PR #32. Unmerged engineering/evidence branches are not included in this readiness snapshot. The only changes made by this governance task are this document and the AGENTS.md pointer/minimal theme de-duplication.

Allowed AquaSentinel status values are **PRESENT_VERIFIED**, **MISSING**, **PARTIAL**, **NOT_YET_VERIFIED**, and **EXTERNAL_ACTION_REQUIRED**. PRESENT_VERIFIED means the stated artifact/fact was inspected, not that the submission passed organizer validation. Repository access by the development environment does not prove evaluator access. No platform form, roster, submission receipt or timezone was inspected.

| Requirement | Official status | AquaSentinel status | Evidence/location | Next action |
|---|---|---|---|---|
| Correct official theme | Registration/submission alignment required | EXTERNAL_ACTION_REQUIRED | Supplied cockpit theme differs from substantive Marine & Water Security alignment; §2 | Obtain organizer confirmation/correction, then align form/README/title slide |
| Submission before deadline | BLOCKING | NOT_YET_VERIFIED | No submission receipt inspected; cutoff in §3 | Verify creator timezone and submit before the cutoff |
| Eligible registered team and members | BLOCKING | NOT_YET_VERIFIED | No approved roster/eligibility record inspected | Confirm eligibility and registration with platform/organizers |
| Accessible repository | BLOCKING | PARTIAL | Git fetch succeeds for Omar-Aboulwafa/aquasentinel-813 | Verify public access or private evaluator permissions |
| Non-empty root README.md | BLOCKING | PRESENT_VERIFIED | Root README.md inspected; project description and user/decision present | Complete remaining guide sections without removing the existing purpose |
| Functioning executable .ipynb | BLOCKING | MISSING | No tracked .ipynb in the audited tree | Create a clean end-to-end notebook and verify restart/run-all later |
| Pinned requirements/dependency file | BLOCKING; form explicitly confirms requirements.txt | PARTIAL | No requirements.txt; pyproject.toml pins four runtime dependencies, but build/dev requirements are not all exact pins | Provide the required pinned submission dependency file and verify installation later |
| Sample input OR exact retrieval script | BLOCKING | PARTIAL | data/aoi/demo_site.geojson is an AOI input; config/default.toml exists; no tracked reviewer retrieval script | Provide sufficient permitted sample inputs or exact retrieval instructions/script for the headline workflow |
| Committed example output | BLOCKING | PRESENT_VERIFIED | docs/evidence/AS_107_REAL_ACCEPTANCE.json contains accepted Watch output; AS_108_HISTORICAL_CASE_STUDY MD/JSON also committed | Expose the chosen example clearly in the future notebook/README |
| README problem description | BLOCKING | PARTIAL | Mission/scope describes marine threats; no dedicated problem statement or event/data explanation | Add a clear problem/data statement later |
| README business use case | BLOCKING | PRESENT_VERIFIED | README Primary User / Core Decision identifies operator and monitoring-priority question | Expand delivery/use-case detail where needed |
| README installation/run instructions | BLOCKING | PARTIAL | README lists Python 3.11 but no install/run commands; docs/HANDOFF.md has development setup/test commands only | Add exact reviewer installation and headline-result run commands |
| Presentation PDF attached | BLOCKING | NOT_YET_VERIFIED | No platform attachment inspected; no tracked PDF | Prepare the final PDF and verify form upload, PDF format and 50 MB limit |
| Presentation PDF artifact in audited tree | Required submission deliverable; repository storage not specified | MISSING | No tracked PDF | Prepare actual-result slides in a separately authorized task |
| Code/data/results structure | FLAGGED; not blocking elimination | PARTIAL | src/, data/, docs/evidence/, tests/ exist; no dedicated results/ directory | Make code, input and output locations clear; avoid unnecessary restructuring |
| English-language requirement | NOT ESTABLISHED in supplied facts | NOT_YET_VERIFIED | Inspected README/docs are English; this does not establish the organizer language rule | Confirm required language from the current guide/organizers; record it here |
| Data/licence documentation | README guide area; licence compliance required | PARTIAL | AS-101/AS-102/AS-201 contracts and accepted provenance record sources/levels/licence metadata; README lacks consolidated data/licence section | Verify actual reuse terms and add submission data/licence/attribution details |
| No credentials or restricted imagery | Visible form confirmation | PARTIAL | .gitignore excludes secrets/full scenes; tracked tree has no full-scene raster; release/licence review is not certified by those facts | Complete credential/history and data-permission review before confirming |
| Notebook visible outputs and restart/run-all | Reproducibility guidance | MISSING | No notebook | Verify all cells run and commit permitted outputs later |
| Form project title | Current form field | NOT_YET_VERIFIED | Platform field not inspected; no final title drafted here | Draft/confirm later after theme resolution |
| Form summary ≤2,000 characters | Current form limit | NOT_YET_VERIFIED | Platform field not inspected; no final summary drafted here | Draft later and count characters before submission |
| GitHub repository URL | Current form field | PRESENT_VERIFIED | https://github.com/Omar-Aboulwafa/aquasentinel-813 ; repository identity/fetch verified | Enter this URL and verify evaluator access; form entry itself remains unverified |
| Organizer/evaluation-account access | Visible form confirmation | NOT_YET_VERIFIED | Development Git access alone is insufficient | Confirm evaluator access externally |
| Supporting ZIP if used | OPTIONAL; maximum 200 MB | NOT_YET_VERIFIED | No archive prepared or upload inspected | Omit if unnecessary; otherwise verify content, permissions and size |

The readiness matrix is a snapshot, not authorization to repair missing deliverables in this task. In particular, the submission is not declared ready, accepted or validated. No final title/summary, notebook, README rewrite or slide deck is produced here.

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
