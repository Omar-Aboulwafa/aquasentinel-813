# AquaSentinel 813 — Final Submission Checklist

> Operational release checklist. Organizer rules and deadline/theme authority remain in `docs/HACKATHON_SUBMISSION.md`.

## A. Stop-ship gates — all must be resolved before final submit

- [ ] **Theme confirmation:** organizer has confirmed/corrected the official challenge/theme wording. Do not silently substitute Marine & Water Security for the live registered label without confirmation.
- [ ] **Creator timezone verified:** confirm the team creator’s timezone from the organizer platform/account and interpret the 11 Oct 2026 23:59 cutoff accordingly.
- [ ] **Formal eligibility verified:** live platform shows the team is eligible for PoC judging and all required members are registered.
- [ ] **Evaluator repository access verified:** repository is public or the exact organizer/evaluator account can open it.
- [ ] **Submission made before the governing cutoff with safety margin.**
- [ ] **Submission receipt / confirmation retained.**

## B. Repository release gate

- [ ] Final submission branch/head is known and recorded.
- [ ] Root `README.md` is non-empty and follows the required ten-section structure.
- [ ] `requirements.txt` is present at repository root with exact direct pins.
- [ ] `notebooks/aquasentinel_hab_water_quality.ipynb` exists and contains visible outputs.
- [ ] `data/submission/hab_headline_input.json` exists.
- [ ] `results/submission/` contains the committed reviewer outputs.
- [ ] No raw full EO scenes, `.SAFE`, JP2/TIFF scene payloads, restricted imagery, signed URLs, SAS tokens, credentials or real `.env` secrets are tracked.
- [ ] `.env.example` contains placeholders only.
- [ ] README install/run commands match the final repository state.
- [ ] Optional live metadata check remains optional; headline reproduction does not depend on provider uptime.
- [ ] Sentinel-1 remains clearly secondary/incomplete.
- [ ] Hyperspectral remains optional and is not falsely claimed as implemented.

## C. Final reproducibility gate

At the exact final submission head:

- [ ] GitHub Actions `Submission reproducibility` completes successfully.
- [ ] Clean Python 3.11 setup passes.
- [ ] Reviewer requirements install passes.
- [ ] Repository tests and Ruff pass.
- [ ] Reviewer notebook executes end to end.
- [ ] Headline result verification passes.
- [ ] Deterministic reviewer-output verification passes.

Expected frozen headline:

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

Any change to these accepted values is a stop-ship event requiring owner/scientific review; presentation polish must not change the frozen result.

## D. Presentation gate

- [ ] Final PDF has exactly the intended slides and opens successfully.
- [ ] PDF is under 50 MB.
- [ ] PDF is visually preflighted: no clipping, overflow, broken glyphs or hidden text.
- [ ] Deck leads with the operator/water-security problem rather than implementation detail.
- [ ] Actual accepted output appears before roadmap/future work.
- [ ] `29.52 / Watch` is explicitly described as provisional monitoring-priority output, not probability/confidence.
- [ ] Evidence completeness `0.70` is visible.
- [ ] Environmental context and intake exposure are visibly unavailable/not implemented.
- [ ] Historical case remains `PARTIALLY_CONSISTENT`; POST unavailable; lead time not estimable.
- [ ] Al Raha remains labelled analyst-defined validation AOI, not a confirmed intake.
- [ ] Business slide labels buyer/revenue/value statements as hypotheses or incubation validation where appropriate.
- [ ] No invented customers, pricing, savings, ROI, deployments or prevented shutdowns.
- [ ] Official theme wording is inserted only after organizer confirmation.

## E. Live submission form gate

Use the exact current form contract from `docs/HACKATHON_SUBMISSION.md`.

- [ ] Project title entered exactly as approved.
- [ ] Summary entered and character count remains <= 2,000.
- [ ] GitHub URL entered correctly.
- [ ] Final presentation PDF selected and upload completed.
- [ ] Supporting ZIP is omitted unless specifically useful and verified <200 MB.
- [ ] README confirmation checked only after verification.
- [ ] Executable notebook confirmation checked only after verification.
- [ ] Pinned requirements confirmation checked only after verification.
- [ ] Example input/output confirmation checked only after verification.
- [ ] No credentials/restricted imagery confirmation checked only after final audit.
- [ ] Organizer/evaluator repository access confirmation checked only after access test.
- [ ] All required project/team sections complete.
- [ ] Participation in judging / non-withdrawal state verified if the platform exposes it.
- [ ] Final review screenshot or equivalent evidence captured before pressing Submit.
- [ ] Submit action completed.
- [ ] Confirmation page/email/receipt saved.

## F. Five-minute judge defense gate

Every presenter should be able to answer without improvising:

- [ ] What is the single user decision AquaSentinel supports?
- [ ] Why is this not a confirmed HAB detector?
- [ ] What do 7/802, 2,800 m², 29.52/Watch and 0.70 mean?
- [ ] Why is 0/7 recurrence not biological absence?
- [ ] Why are environmental context and intake exposure missing?
- [ ] Why is Al Raha not claimed as an intake?
- [ ] What exactly was reproduced in CI?
- [ ] Why was no later POST acquisition substituted?
- [ ] What is innovative compared with a single index map or unsupported black-box classifier?
- [ ] Who is the buyer/user and what is the business-model hypothesis?
- [ ] What would be validated during incubation?
- [ ] Where do hyperspectral and Sentinel-1 fit without overstating current capability?

Use `docs/PITCH_AND_JUDGE_QA.md` as the answer contract.

## Final release rule

**No new science, feature or visual improvement is allowed to endanger a passing validation artifact on submission day.** After all stop-ship gates are green, prioritize successful submission and retained evidence over additional engineering.
