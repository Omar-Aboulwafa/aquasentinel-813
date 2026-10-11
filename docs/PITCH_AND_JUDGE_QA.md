# AquaSentinel 813 — Pitch and Judge Q&A Defense

> Presentation/pitch support only. Scientific claims remain governed by `docs/DECISIONS.md`; current hackathon/theme/admin state remains governed by `docs/HACKATHON_SUBMISSION.md`.

## 90-second core pitch

**AquaSentinel 813 helps desalination water-quality teams answer one operational question: where should we look first, and what evidence supports that decision?**

Marine Earth-observation data can reveal unusual water conditions, but a satellite anomaly is not a laboratory diagnosis. In a high-consequence setting, a useful product must show not only what was flagged, but why, how complete the evidence is, where it came from, and what a human should do next.

Our proven submission capability is the Sentinel-2 water-quality path. It converts public observations into an explainable evidence chain: spectral water-quality features, strictly-prior temporal comparison, family-aware candidate geometry, exact-grid observational recurrence, evidence completeness, and a conservative monitoring-priority action.

For the accepted 28 April 2023 validation observation, the frozen pipeline identified **7 candidate pixels out of 802 policy-evaluable pixels**, one **2,800 square metre** candidate region, and **0 of 7 exact-pixel recurrence** among candidates with valid prior history. The provisional monitoring-priority score is **29.52 / Watch**, with **0.70 evidence completeness**. The action is: **Review on the next valid acquisition**.

We deliberately do not call that a confirmed HAB. Missing environmental context and intake exposure stay visibly missing rather than being hidden inside a confident score.

AquaSentinel is also designed as a multi-hazard architecture. Sentinel-1 AS-201 now has a **proven live retrieval and metadata/access foundation against six frozen real products**. We deliberately stop the claim there: calibrated SAR pixels, backscatter science and surface-slick/oil interpretation have not started.

**Incubation is therefore not needed to invent the project. It is needed to validate the next operational layer: real intake geometry, environmental exposure, prospective field evidence, calibrated SAR/surface-slick science, and an operator pilot.**

## 30-second version

AquaSentinel 813 is explainable EO decision support for desalination water-quality monitoring under **Marine & Water Security**. Our accepted Sentinel-2 result narrowed 802 policy-evaluable pixels to 7 candidates and produced a provisional **29.52 / Watch** with **0.70 evidence completeness**. The workflow is reproducible and keeps field/laboratory verification in the loop. Sentinel-1 live retrieval/metadata access is already proven; the scientific SAR/oil layer is the next validation step, not a current claim.

## Opening sentence

**“We are not trying to replace the laboratory. We are trying to make the next monitoring or verification decision more targeted, explainable and reproducible.”**

## Closing sentence

**“We know what is proven, what is still unproven, and exactly what incubation would allow us to validate next.”**

## Hostile judge Q&A

### Q1. Are you actually detecting harmful algal blooms?

**Answer:** Not as a confirmed biological diagnosis. The current PoC performs HAB-like water-quality **observational screening** from Sentinel-2 and prioritizes areas for human review. Confirmation of species, toxins or biological state requires field/laboratory evidence.

### Q2. What exactly does 29.52 mean?

**Answer:** It is an availability-aware **provisional monitoring-priority score** under frozen weights. It is not probability, confidence or severity. The corresponding band is Watch and the recommended action is to review the next valid acquisition.

### Q3. Why is evidence completeness only 0.70?

**Answer:** Environmental context and intake exposure are not implemented in the accepted headline result. AquaSentinel marks them unavailable rather than silently scoring them as zero.

### Q4. Does 0/7 recurrence mean the anomaly disappeared?

**Answer:** No. The implemented recurrence is exact same-grid observational recurrence. Water features can move and valid support can change. Zero exact-pixel recurrence is not proof of biological disappearance.

### Q5. How was the Sentinel-2 result validated?

**Answer:** The reviewer workflow is reproducible in a clean Python 3.11 CI environment, including tests, Ruff, notebook execution, headline verification and deterministic outputs. The historical April 2023 case is only **PARTIALLY_CONSISTENT** with documented area/month context; POST is unavailable and exact lead time is not estimable. We do not present it as prospective biological accuracy validation.

### Q6. Why not use a black-box AI classifier?

**Answer:** We do not have sufficient biological ground truth to justify a calibrated HAB classifier. A black-box probability would create more certainty than the evidence supports. The architecture can later incorporate validated models while preserving provenance and evidence-completeness semantics.

### Q7. Why not just show a spectral index map?

**Answer:** Operational decision support requires more than a single index. AquaSentinel adds strictly-prior temporal comparison, family-aware candidate policy, recurrence, explicit missing-evidence handling, exact product lineage and a conservative human action.

### Q8. Is Sentinel-1 just a roadmap idea?

**Answer:** No. M61 / PR #38 proved the **live retrieval and metadata/access foundation** against six exact frozen real Sentinel-1 products. All required AS-201 access/metadata stages passed live. That means the engineering access foundation is real, not conceptual.

### Q9. So does your oil detector work?

**Answer:** We do **not** have an oil detector yet. M61 explicitly did not read SAR science pixels, apply calibration/noise correction, compute calibrated backscatter, or detect surface slicks. AS-202 has not started. We are separating a proven live access foundation from unproven SAR science.

### Q10. Why stop Sentinel-1 now?

**Answer:** Because starting AS-202 opens a new scientific validation track. The submission already has a mature, reproducible Sentinel-2 headline. Freezing Sentinel-1 at a proven engineering boundary protects submission reliability and creates a precise incubation objective.

### Q11. How can this help a real desalination plant if Al Raha is not an intake?

**Answer:** Al Raha is explicitly an analyst-defined validation AOI, not a claimed plant intake. The first operator step is to bind the proven chain to operator-approved intake geometry and implement the exposure component using real operational context.

### Q12. What is the business model?

**Answer:** The current **business hypothesis** is B2B decision support for desalination utilities and coastal water-monitoring organizations, delivered as a site-configured monitoring workspace with API/reporting integration. A plausible revenue model is an annual site/enterprise subscription plus integration. Pricing and procurement fit must be validated during incubation.

### Q13. What economic value can you prove today?

**Answer:** We do not claim quantified savings today. The value hypothesis is measurable: reduce analyst search space, prioritize field sampling, improve provenance/traceability, measure alert latency, and ultimately quantify operational value during a prospective pilot.

### Q14. Why is this relevant now?

**Answer:** Marine risk around Gulf shipping and coastal infrastructure is operationally important, and historical UAE oil spills have disrupted desalination operations. Our claim is not that AquaSentinel would have prevented those incidents. The relevance is that water-quality anomalies and potential surface pollution belong in the same intake-focused monitoring architecture.

### Q15. What would incubation unlock?

**Answer:** Five concrete steps: bind to operator-approved intake geometry; add environmental context and exposure; run prospective multi-date monitoring; validate Sentinel-1 calibrated SAR/surface-slick science on the already proven live access foundation; and run operator/user plus commercial-procurement validation.

## Phrases to avoid

- “We detect HABs.”
- “This is 70% confidence.”
- “The anomaly disappeared biologically.”
- “We protect the intake” as a demonstrated current outcome.
- “We validated warning lead time.”
- “Our oil detector works.”
- “We used Satellite 813 data.”
- “Sentinel-1 science is validated.”
- Any unsupported customer traction, revenue, savings, ROI, prevented shutdowns or lives-saved claim.

## Preferred phrases

- “HAB-like water-quality observational screening.”
- “Monitoring-priority decision support.”
- “Evidence completeness 0.70.”
- “Exact-pixel observational recurrence.”
- “Review on the next valid acquisition.”
- “Retrospective case: PARTIALLY_CONSISTENT.”
- “POST unavailable; exact lead time not estimable.”
- “Sentinel-1 AS-201 live retrieval/metadata access is proven.”
- “AS-202 SAR science and oil/surface-slick interpretation have not started.”
- “A proven live access foundation with a clearly bounded incubation validation path.”
