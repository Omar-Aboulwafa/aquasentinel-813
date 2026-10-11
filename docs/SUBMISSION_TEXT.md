# AquaSentinel 813 — Final Submission Text

## Project title

**AquaSentinel 813 — Sentinel-2 HAB / Water-Quality Observational Intelligence**

Theme wording is intentionally omitted pending organizer confirmation, as required by `docs/HACKATHON_SUBMISSION.md`.

## Submission summary

Character count: **1,504 characters**, including paragraph breaks.

AquaSentinel 813 is an explainable Sentinel-2 marine water-quality observational-intelligence PoC for desalination monitoring. It uses public Earth-observation data, conservative coastal-water preprocessing, spectral water-quality features, causal temporal comparison, family-aware anomaly geometry, exact-pixel observational recurrence, and an availability-aware risk layer that exposes missing evidence rather than hiding it.

For the accepted 28 April 2023 Al Raha validation observation, the frozen pipeline produced 7 candidate pixels within 802 policy-evaluable pixels (2,800 m²), 0/7 exact-pixel recurrence among candidates with prior valid history, and a provisional observational risk score of 29.52380952380953 / Watch with evidence completeness 0.70. The recommended action is to review the next valid acquisition. A retrospective April 2023 case study is PARTIALLY_CONSISTENT with documented month/area context; required POST evidence is unavailable and exact lead time is not estimable.

AquaSentinel does not claim confirmed HAB, species, toxins, chlorophyll concentration, biological probability, water safety, or automatic plant shutdown. Field/laboratory verification remains necessary. The repository includes a pinned Python 3.11 reviewer environment, an executable notebook, compact reproducible input, actual outputs, provenance, and documented limitations. Sentinel-1 oil remains a secondary incomplete capability; hyperspectral data is optional rather than a submission dependency.

## One-line summary

AquaSentinel 813 turns Sentinel-2 observations into explainable HAB-like water-quality anomaly screening, evidence-completeness diagnostics, and monitoring-priority guidance for desalination operations while preserving source provenance and scientific limitations.
