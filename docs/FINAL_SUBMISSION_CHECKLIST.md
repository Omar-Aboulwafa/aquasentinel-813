# AquaSentinel 813 — Final Submission Checklist

> Operational release checklist. Organizer rules and current theme authority remain in `docs/HACKATHON_SUBMISSION.md`.

## A. Stop-ship gates

- [x] **Theme confirmed:** Marine & Water Security.
- [x] **Repository accessible:** repository is public.
- [ ] **Creator timezone verified:** confirm the team creator’s timezone from the organizer platform/account and interpret the 11 Oct 2026 23:59 cutoff accordingly.
- [ ] **Formal eligibility verified:** live platform confirms the team/members are eligible for PoC judging.
- [ ] **Submission completed before the governing cutoff with safety margin.**
- [ ] **Submission receipt / confirmation retained.**

## B. Repository release gate

- [ ] Final submission `main` head is known and recorded.
- [ ] Submission PR/package merged into the intended final `main`.
- [ ] Root `README.md` follows the reviewer-facing ten-section structure.
- [ ] Root pinned `requirements.txt` is present.
- [ ] `notebooks/aquasentinel_hab_water_quality.ipynb` exists with visible outputs.
- [ ] `data/submission/hab_headline_input.json` exists.
- [ ] `results/submission/` contains committed reviewer outputs.
- [ ] No raw full EO scenes, `.SAFE`, JP2/TIFF scene payloads, restricted imagery, signed URLs, SAS tokens, credentials or real `.env` secrets are tracked.
- [ ] `.env.example` contains placeholders only.
- [ ] README install/run commands match final repository state.
- [ ] Default headline reproduction does not depend on provider uptime.
- [ ] Sentinel-1 wording is exact: **AS-201 live retrieval/metadata access proven; AS-202 SAR science/oil detection not started.**
- [ ] Hyperspectral remains optional and is not falsely claimed as implemented.

## C. Final reproducibility gate

At the exact final submission head:

- [ ] GitHub Actions `Submission reproducibility` succeeds.
- [ ] Clean Python 3.11 setup passes.
- [ ] Reviewer requirements install passes.
- [ ] Repository tests and Ruff pass.
- [ ] Reviewer notebook executes end to end.
- [ ] Headline result verification passes.
- [ ] Deterministic reviewer-output verification passes.

Frozen headline:

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

Any change to these accepted values is a stop-ship event.

## D. Presentation V3 gate

- [ ] Theme shown exactly as **Marine & Water Security**.
- [ ] PDF opens and is <50 MB.
- [ ] No clipping, overflow, broken glyphs or hidden text.
- [ ] Actual accepted Sentinel-2 output appears before future-work claims.
- [ ] `29.52 / Watch` is described as a provisional monitoring-priority output, not probability/confidence.
- [ ] Evidence completeness `0.70` is visible.
- [ ] Environmental context and intake exposure remain unavailable/not implemented.
- [ ] Historical case remains `PARTIALLY_CONSISTENT`; POST unavailable; lead time not estimable.
- [ ] Al Raha remains an analyst-defined validation AOI, not a confirmed intake.
- [ ] Sentinel-1 live access foundation is presented as proven, while SAR science/oil detection remains future validation.
- [ ] Incubation slide separates **proven today**, **proven engineering foundation**, and **validate next**.
- [ ] No invented customers, pricing, savings, ROI, prevented shutdowns or lives saved.

## E. Live submission form gate

- [ ] Project title entered exactly as approved.
- [ ] Summary entered and <=2,000 characters.
- [ ] GitHub URL entered correctly.
- [ ] Final V3 presentation PDF uploaded.
- [ ] Supporting ZIP omitted unless specifically useful and verified <200 MB.
- [ ] README confirmation checked after verification.
- [ ] Executable notebook confirmation checked after verification.
- [ ] Pinned requirements confirmation checked after verification.
- [ ] Example input/output confirmation checked after verification.
- [ ] No credentials/restricted imagery confirmation checked after final audit.
- [ ] Public repository access rechecked from logged-out context if practical.
- [ ] All required project/team sections complete.
- [ ] Final review screenshot/evidence captured before Submit.
- [ ] Submit action completed.
- [ ] Confirmation page/email/receipt saved.

## F. Judge defense gate

Presenter can answer without improvising:

- What single decision does AquaSentinel support?
- Why is this not a confirmed HAB detector?
- What do 7/802, 2,800 m², 29.52/Watch and 0.70 mean?
- Why is 0/7 recurrence not biological absence?
- Why are environmental context and intake exposure missing?
- Why is Al Raha not claimed as an intake?
- What exactly is reproducible?
- What did M61 prove for Sentinel-1?
- What did M61 explicitly **not** prove?
- Why does AS-202 belong in incubation rather than the submission critical path?
- Who is the buyer/user and what is the business-model hypothesis?
- What exactly would incubation unlock?

## Final release rule

**No new science or feature is allowed to endanger a passing validation artifact on submission day.** Freeze Sentinel-1 at the proven AS-201 boundary until submission packaging is closed.
