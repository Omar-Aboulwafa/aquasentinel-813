# Submission Packaging P0 — Release Audit

## Scope and audited baseline

This is a repository-content release audit for the reviewer-facing submission package. It is not organizer validation and does not override `docs/HACKATHON_SUBMISSION.md`.

Audited packaging content head before this audit record:

`be4bb2090727de9ac50cde856f870c55022a8f76`

Packaging branch:

`submission/p0-packaging`

Authoritative submission-contract ancestor:

`15d4204d3f269067b64146c4bc9e2d5592c5b30f`

The packaging branch was 16 commits ahead of that ancestor at the audited content head. The packaging diff contains only reviewer workflow/documentation/output files and does not modify scientific source, tests, configuration or frozen decisions.

## Repository file/content audit

Recursive Git tree inspection at audited head was complete (`truncated=false`).

### Raw/restricted Earth-observation imagery

Tracked-path checks:

- `.tif`: none
- `.tiff`: none
- `.jp2`: none
- `.SAFE`: none
- `data/raw`: none
- `data/cache`: none
- `.zip`: none
- committed presentation `.pdf`: none
- committed `.png`: none

**Result: PASS for repository packaging content.** No raw Sentinel scene, SAFE product, raster cache, full provider archive or presentation binary is added to Git.

The reviewer sample is the compact derived-evidence file:

`data/submission/hab_headline_input.json`

It retains accepted counts, source/product identifiers, grid metadata, frozen weights, historical-case status and scientific guardrails. It does not redistribute raw Earth-observation pixels.

## Credential and secret audit

The recursive tree contains no committed `.env` file. The only environment template is `.env.example`, and its external-service username/password fields are empty placeholders with an explicit instruction not to store real secrets.

Submission packaging intentionally commits no:

- API token,
- SAS token value,
- signed provider URL,
- Authorization header,
- password,
- private key,
- account credential.

References to SAS/signing in documentation describe the transport/security design; they are not credential values. Stable unsigned source/product identities are used for provenance.

**Result: PASS for newly packaged repository content.** This audit does not claim a forensic scan of every deleted object in all Git history; historical engineering evidence separately records repeated credential/security scans. Final form upload should still use only the verified PDF and repository URL.

## Data permission / licence boundary

The accepted Sentinel-2 discovery evidence records the STAC collection licence marker as `other`. AquaSentinel does not reinterpret that marker as a broad redistribution licence.

Release policy retained in README and notebook:

- no raw Sentinel-2 imagery is redistributed;
- no signed URLs or transient SAS material are persisted;
- exact public product IDs/providers are retained for traceability;
- reviewer reproduction uses compact accepted derived evidence by default;
- optional upstream retrieval remains with the original public providers and their applicable terms.

The project repository currently has no standalone open-source `LICENSE` file. Packaging therefore does not invent an MIT/Apache/other reuse grant. README states this limitation explicitly.

**Result: PASS for conservative submission packaging / attribution boundary.** This is not legal advice or a provider licence grant.

## Scientific-claim audit

Packaging preserves the accepted/frozen result without retuning:

- candidate pixels / policy-evaluable pixels: `7 / 802`
- candidate area: `2,800 m²`
- observational recurrence A/B/C: `7 / 7 / 0`
- provisional risk: `29.52380952380953 / Watch`
- evidence completeness: `0.70`
- historical classification: `PARTIALLY_CONSISTENT`
- POST: `UNAVAILABLE`
- lead time: `NOT_ESTIMABLE`

Packaging does not claim confirmed HAB, species, toxins, measured chlorophyll concentration, biological probability/calibrated confidence, safe/unsafe water, autonomous shutdown, exact warning lead time, completed Sentinel-1 oil science, or implemented environmental/intake-exposure evidence where unavailable.

**Result: PASS.**

## Presentation artifact audit

Verified external submission-form artifact:

`AquaSentinel_813_Submission.pdf`

Recorded properties:

- 9 pages
- 164,162 bytes
- SHA-256 `5525d6570cc42a6bd59cb38ea71affbcecb09df7043f28a27428e7b540056deb`
- PDF open/preflight/render review: PASS
- under 50 MB form limit: PASS
- form attachment: NOT YET VERIFIED / external owner action

The binary PDF is intentionally not committed to Git; `presentation/README.md` records its checksum and slide contract.

## Reproducibility audit status

Completed:

- reviewer notebook exists with committed visible outputs;
- deterministic replay completed successfully in the available runtime;
- every code cell parses under Python 3.11 grammar;
- expected output files are committed;
- root direct dependencies are pinned;
- a GitHub Actions Python 3.11 reproduction workflow is committed.

Still open:

- **fresh Python 3.11 install + notebook execution at the final submission commit is NOT YET PASS.** Local Python 3.11 acquisition was blocked by the execution environment's DNS, and connector-created pushes did not start a workflow run.

Do not upgrade this state to PASS until an independent Python 3.11 run succeeds.

## External release gates not covered by this audit

- final organizer-confirmed theme wording;
- team creator timezone / governing cutoff verification;
- formal final team/member eligibility;
- public or evaluator repository access, verified outside the owner session;
- live form title/summary/GitHub URL entry;
- PDF attachment;
- form confirmations;
- final submission and receipt.

## Audit conclusion

`REPOSITORY_PACKAGING_SECURITY_AND_DATA_AUDIT = PASS`

`CLEAN_PYTHON_311_REPRODUCIBILITY = OPEN`

`EXTERNAL_ADMINISTRATIVE_GATES = OPEN`

The package is ready for independent Python 3.11 validation and owner/organizer administrative completion. No AS-201/AS-202 scientific development was performed by this audit.
