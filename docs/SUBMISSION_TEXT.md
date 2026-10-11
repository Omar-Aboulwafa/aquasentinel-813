# AquaSentinel 813 — Final Submission Text

## Project title

**AquaSentinel 813 — Sentinel-2 HAB / Water-Quality Observational Intelligence**

Theme wording is intentionally omitted pending organizer confirmation, as required by `docs/HACKATHON_SUBMISSION.md`.

## Submission summary

Character count: **1,695 characters**, including paragraph breaks.

AquaSentinel 813 is an explainable Earth-observation decision-support PoC for desalination water-quality teams. It answers a practical operational question: where and when should monitoring or field verification be prioritized? Instead of turning a satellite anomaly into an unsupported diagnosis, AquaSentinel converts public Sentinel-2 observations into a traceable evidence packet: source provenance, spectral water-quality evidence, strictly-prior temporal comparison, family-aware candidate geometry, exact-pixel observational recurrence, evidence completeness, and a conservative next action.

For the accepted 28 April 2023 Al Raha validation observation, the frozen pipeline identified 7 candidate pixels within 802 policy-evaluable pixels, one 2,800 m² candidate region, and 0/7 exact-pixel recurrence among candidates with valid prior history. The availability-aware provisional score is 29.52380952380953 / Watch with evidence completeness 0.70, leading to the recommendation: Review on the next valid acquisition. A retrospective April 2023 case is PARTIALLY_CONSISTENT with documented month/area context; required POST evidence is unavailable and exact lead time is not estimable.

AquaSentinel does not claim confirmed HAB, species, toxins, measured chlorophyll, biological probability, water safety, or automatic shutdown. Human field/laboratory verification remains necessary. The submission includes a pinned Python 3.11 reviewer environment, executable notebook, compact reproducible input, actual outputs, deterministic verification, provenance, and explicit limitations. Sentinel-1 oil remains secondary/incomplete; hyperspectral is an optional enhancement, not a dependency.

## One-line summary

AquaSentinel 813 turns Sentinel-2 observations into explainable monitoring priorities for desalination water-quality teams, showing what evidence supports the decision, what evidence is missing, and what should be reviewed next.
