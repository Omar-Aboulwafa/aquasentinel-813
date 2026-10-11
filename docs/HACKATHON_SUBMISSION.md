# AquaSentinel 813 — Hackathon Submission Source of Truth

This file is the authoritative repository source for current Arab Youth Space Hackathon 2026 submission rules, theme state, submission-readiness gates, and the submission consequence of current engineering evidence.

Engineering implementation/status belongs in `docs/PROJECT_STATE.md`. Scientific/design decisions belong in `docs/DECISIONS.md`. Historical engineering evidence remains under `docs/evidence/`.

## 1. Current authoritative administrative state

Current owner-confirmed organizer state:

```text
FINAL_SUBMISSION_THEME_LABEL = Marine & Water Security
THEME_ALIGNMENT_STATUS = CONFIRMED
REPOSITORY_VISIBILITY = PUBLIC
SUBMISSION_HEADLINE = Sentinel-2 HAB / Water-Quality Observational Intelligence
```

The previously documented mismatch between the old registered/cockpit label and the Marine/Water taxonomy is retained as historical context, but it is no longer an open submission blocker. The owner has confirmed the approved final theme as **Marine & Water Security**.

The repository is now public. Evaluator-access risk from private-repository permissions is therefore closed, subject only to the repository remaining public through evaluation.

## 2. Historical taxonomy conflict — resolved for final submission

Earlier project records captured three different labels:

- old live/cockpit label: **Urban Expansion, Land Use Change & Heat Risk**;
- current onboarding taxonomy: **Theme 03 — Marine & Water Security**;
- older starter-repository taxonomy: **Theme 6 — Water Quality & Inland/Coastal Water Intelligence**.

Do not erase that history from old evidence. For the final submission, however, the approved label is:

> **Marine & Water Security**

No submission artifact should continue to say “pending organizer confirmation”.

## 3. Official timeline

Current operational deadline:

- **11 October 2026, 23:59**
- governing interpretation: **local time of the team creator**
- commits pushed after the applicable cutoff do not count
- validation: **12–13 October 2026**
- pitching/judging: **14–16 October 2026**

The team creator’s timezone is still a stop-ship item until explicitly verified from the organizer platform/account. Do not infer it from the user’s location, AOI, repository timestamps, or development environment.

## 4. Submission form contract

Required submission fields/artifacts:

- project title;
- summary, maximum **2,000 characters**;
- GitHub repository URL;
- presentation slides as **PDF**, maximum **50 MB**;
- optional supporting ZIP, maximum **200 MB**.

Repository confirmations include:

- non-empty README;
- executable end-to-end Jupyter notebook;
- pinned root `requirements.txt`;
- example input/output;
- no credentials or restricted imagery;
- evaluator/organizer repository access.

**English is required** for the official submission package.

## 5. Blocking validation gates

The submission must satisfy all of the following:

1. submitted before the governing deadline;
2. eligible registered team/members;
3. accessible repository;
4. non-empty root README;
5. functioning executable `.ipynb`;
6. pinned dependency file;
7. sample input or exact reproducible retrieval;
8. committed example output;
9. README problem/business use case;
10. README installation/run instructions;
11. presentation PDF attached.

A recognizable code/data/results structure is useful but is not treated here as a separate elimination rule.

## 6. Reviewer reproducibility contract

A reviewer who has never spoken to the team should be able to clone the repository, follow the README, execute the reviewer notebook, and reproduce the headline result without contacting the team.

The submission package therefore uses:

- Python 3.11;
- root pinned `requirements.txt`;
- `notebooks/aquasentinel_hab_water_quality.ipynb`;
- compact committed input under `data/submission/`;
- committed reviewer output under `results/submission/`;
- no dependency on live provider uptime for the default replay;
- no committed raw full EO scenes, credentials, tokens, signed URLs, or restricted imagery.

## 7. README contract

The final README should present, in reviewer order:

1. title + one-line summary;
2. business use case;
3. problem;
4. data used;
5. technical approach;
6. installation;
7. how to run;
8. example input/output;
9. results/limitations;
10. team/licence/attribution.

## 8. Presentation contract

Recommended final flow:

1. title / team / **Marine & Water Security**;
2. problem and affected user;
3. business use case;
4. EO data;
5. technical approach;
6. actual outputs;
7. validation and limitations;
8. impact / business path;
9. incubation / next steps.

Actual accepted outputs must appear before roadmap claims. Future capability must be visibly separated from current proof.

## 9. Judging dimensions

Current judging preparation should optimize for:

- problem definition / real-world relevance;
- technical robustness / scalability;
- meaningful EO use;
- product / decision-support delivery;
- innovation;
- business viability;
- societal/environmental/economic impact and strategic alignment;
- presentation/communication.

Hyperspectral use is an optional advantage, not a P0 dependency.

## 10. Current EO/data-access boundary

Current Phase-2 submission must not depend on unguaranteed Phase-3 resources such as native Satellite 813 access, gIQ, commercial Planet imagery, or MBZ-SAT access.

The proven submission backbone is public Sentinel-2 EO evidence.

### Sentinel-1 AS-201 current boundary

M61 / PR #38 established:

```text
LIVE_READINESS = PROVED_AT_AS201_METADATA_ACCESS_BOUNDARY
SAR_SCIENTIFIC_READINESS = UNPROVED
OIL_DETECTION = NOT_STARTED
AS_202 = NOT_STARTED
```

Six exact frozen Sentinel-1 products passed the required live retrieval / asset / metadata-access validation chain. This proves the live engineering foundation only.

It does **not** prove:

- SAR raster-pixel access for the scientific workflow;
- calibration/noise-correction application;
- sigma0/gamma0/dB validity;
- speckle filtering/mosaicking;
- surface-slick or petroleum identification;
- oil-source attribution;
- water safety;
- shutdown advice.

## 11. Submission headline strategy

The final submission headline remains:

> **AquaSentinel 813 — Sentinel-2 HAB / Water-Quality Observational Intelligence**

Reason: the Sentinel-2 path contains the mature scientific/decision-support result, accepted retrospective evidence, reviewer notebook, committed outputs, and reproducible headline result.

Sentinel-1 is now stronger than a speculative roadmap item because the live access/metadata foundation is proven. Its correct submission role is:

> **Proven live Sentinel-1 access foundation; scientific SAR/surface-slick validation is the next incubation step.**

Do not call the current system an operational oil detector.

## 12. Frozen headline result

The reviewer-facing accepted result remains:

```text
candidate pixels / policy-evaluable pixels = 7 / 802
candidate area = 2,800 m²
observational recurrence A/B/C = 7 / 7 / 0
risk score = 29.52380952380953
risk band = Watch
evidence completeness = 0.70
recommendation = Review on the next valid acquisition
historical case = PARTIALLY_CONSISTENT
POST = UNAVAILABLE
lead time = NOT_ESTIMABLE
```

These values are not to be changed for presentation polish.

## 13. Scientific claim boundaries

The submission does not claim:

- confirmed HAB;
- species or toxins;
- measured chlorophyll concentration;
- biological probability or calibrated confidence;
- safe/unsafe water;
- automatic shutdown;
- validated warning lead time;
- completed Sentinel-1 oil science.

Field/laboratory verification remains necessary.

## 14. Current readiness state

Already closed/prepared on the packaging track:

- public repository access;
- final theme wording: **Marine & Water Security**;
- root reviewer README;
- root pinned requirements;
- executable English reviewer notebook with visible outputs;
- compact reviewer input;
- committed reviewer output;
- deterministic headline verification workflow;
- presentation package;
- project title and <=2,000-character summary.

Still external/stop-ship:

- verify creator timezone / governing cutoff;
- verify formal final team eligibility;
- merge/finalize the submission package on the intended `main` head;
- run final reproducibility/secret/restricted-data audit on that exact head;
- upload final V3 PDF;
- enter form title/summary/GitHub URL;
- verify all form confirmations;
- submit and retain receipt/confirmation.

## 15. Final release rule

No new science is required for eligibility. Sentinel-1 AS-202 must not become a dependency of submission readiness.

After the final repository head passes the release gates, prioritize successful submission and retained evidence over additional engineering.
