# AquaSentinel 813 — Pitch and Judge Q&A Defense

> Presentation/pitch support only. Scientific claims remain governed by `docs/DECISIONS.md`; hackathon rules/theme/admin state remain governed by `docs/HACKATHON_SUBMISSION.md`.

## 90-second core pitch

**AquaSentinel 813 helps desalination water-quality teams answer one operational question: where should we look first, and what evidence supports that decision?**

Marine Earth-observation data can reveal unusual water conditions, but a satellite anomaly is not a laboratory diagnosis. In a high-consequence setting, a useful product must show not only what was flagged, but why, how complete the evidence is, where it came from, and what a human should do next.

AquaSentinel turns public Sentinel-2 observations into an explainable evidence chain: spectral water-quality features, strictly-prior temporal comparison, family-aware candidate geometry, exact-grid observational recurrence, evidence completeness, and a conservative monitoring-priority action.

For our accepted 28 April 2023 validation observation, the frozen pipeline identified **7 candidate pixels out of 802 policy-evaluable pixels**, one **2,800 square metre** candidate region, and **0 of 7 exact-pixel recurrence** among candidates with valid prior history. The provisional score is **29.52 - Watch**, with **0.70 evidence completeness**. The action is simple: **review on the next valid acquisition**.

We intentionally do not call that a confirmed HAB. We do not infer species, toxins, measured chlorophyll, biological probability, water safety, or an automatic plant shutdown. Missing environmental context and intake exposure remain visibly missing rather than being hidden inside a confident score.

The result is independently reproducible from a clean Python 3.11 environment, with the notebook, pinned dependencies, sample input, actual outputs, provenance and deterministic checks committed for review.

**Our incubation goal is to bind this trusted baseline to real operator-approved intake geometry, add environmental and exposure evidence, run a prospective pilot, and validate the workflow with desalination operators. AquaSentinel is designed to become operational without pretending to know more than the evidence can support.**

## 30-second version

AquaSentinel 813 is explainable EO decision support for desalination water-quality monitoring. Instead of turning a satellite anomaly into an unsupported “HAB detected” label, it tells an operator **where to review, why it was flagged, how complete the evidence is, and what to do next**. Our accepted Sentinel-2 result narrowed 802 policy-evaluable pixels to 7 candidates, produced a provisional **29.52 / Watch** with **0.70 evidence completeness**, and recommends reviewing the next valid acquisition. The workflow is reproducible, provenance-preserving, and explicitly keeps field/laboratory verification in the loop.

## Opening sentence

**“We are not trying to replace the laboratory. We are trying to make the next laboratory or monitoring decision more targeted, explainable and reproducible.”**

## Closing sentence

**“Select AquaSentinel for incubation, and we will move from a reviewer-ready observational PoC to an operator-validated marine water-security product without weakening the scientific guardrails that make it trustworthy.”**

## Hostile judge Q&A

### Q1. Is AquaSentinel actually detecting harmful algal blooms?

**Answer:** Not yet, and we deliberately do not claim that. The current PoC performs HAB-like water-quality **observational screening** from Sentinel-2. It prioritizes areas for human review using spectral, temporal and recurrence evidence. Confirmation of a HAB, species, toxin or measured chlorophyll requires field or laboratory evidence.

### Q2. Then why call it HAB / water-quality intelligence?

**Answer:** Because HAB-like spectral behaviour is one of the water-quality risk patterns the system screens for, but the output is explicitly a monitoring priority rather than a biological diagnosis. The product language and score semantics preserve that boundary.

### Q3. What exactly does the score 29.52 mean?

**Answer:** It is an availability-aware **provisional monitoring-priority score** under frozen weights. It is not probability, confidence or severity. The score exposes the contributing spectral and red-edge evidence, persistence contribution, and the evidence components that are unavailable. The corresponding band is Watch and the recommended action is to review the next valid acquisition.

### Q4. Why is evidence completeness only 0.70?

**Answer:** Environmental context and intake exposure are not implemented in the accepted headline result. Rather than pretending those inputs are zero, AquaSentinel marks them unavailable and reports the completeness explicitly. That is intentional evidence governance.

### Q5. How can the result help a real desalination plant if the AOI is not an intake?

**Answer:** The present Al Raha AOI is an analyst-defined validation AOI, not a claimed plant intake. The PoC proves the observational and reproducibility chain. The first incubation step is to bind that chain to operator-approved intake geometries and implement the intake-exposure component using real operational context.

### Q6. Why did you not use an AI classifier?

**Answer:** A classifier is only as defensible as its labels and validation. We do not have sufficient biological ground truth to justify a calibrated HAB classifier. A black-box probability would create more apparent certainty than the evidence supports. The architecture can later incorporate validated models while preserving provenance and evidence-completeness semantics.

### Q7. Why not just compute a common water index and show a map?

**Answer:** A useful operational decision requires more than a single pixel index. AquaSentinel adds a strictly-prior temporal baseline, family-aware candidate policy, observational recurrence, explicit missing-evidence handling, exact product lineage, and a conservative human action. The innovation is the end-to-end evidence-to-decision contract.

### Q8. Does 0/7 recurrence mean the anomaly disappeared?

**Answer:** No. The implemented recurrence is exact same-grid observational recurrence. Water features can move and valid support can change. Zero exact-pixel recurrence is therefore evidence about this observation sequence, not proof of biological disappearance.

### Q9. How was the system validated?

**Answer:** We have two different forms of validation and keep them separate. First, the reviewer workflow is independently reproducible in a clean Python 3.11 CI run, including quality gates, notebook execution, headline verification and deterministic outputs. Second, the historical April 2023 case is only **PARTIALLY_CONSISTENT** with documented area/month context; it is retrospective, POST evidence is unavailable, and exact lead time is not estimable. We do not present that as prospective biological accuracy validation.

### Q10. If POST is unavailable, why not use a later acquisition?

**Answer:** Because the accepted historical-case contract froze compatibility requirements before interpreting the result. Substituting a later scene simply to improve the story would weaken scientific credibility. AquaSentinel preserves the missing POST evidence and says lead time is not estimable.

### Q11. How is this scalable?

**Answer:** The core workflow is configuration-driven around AOI, observation sequence, product lineage and analysis grid. Scaling operationally would mean onboarding approved sites/intakes, automating scheduled retrieval and monitoring, and validating site-specific environmental/exposure components. We do not claim production-scale deployment yet; the PoC demonstrates the reproducible technical foundation.

### Q12. What is your commercial model?

**Answer:** Our current **business hypothesis** is B2B decision support for desalination utilities and coastal water-monitoring organizations, delivered as a site-configured monitoring workspace with API/reporting integration. A plausible revenue model is an annual site or enterprise subscription plus integration/service work. We have not fabricated pricing or traction; incubation should validate user workflow, procurement fit, measurable value and pricing.

### Q13. What economic value can you prove today?

**Answer:** We do not claim quantified savings today. The value hypothesis is measurable: reduce the analyst search space, prioritize field sampling, improve provenance/traceability and eventually measure alert burden and warning lead time in a prospective pilot. Those are the metrics we would validate with an operator.

### Q14. Why is this strategically relevant to the UAE?

**Answer:** Desalination is central to UAE water security, and Environment Agency - Abu Dhabi documents that harmful algal blooms can disrupt desalination operations by clogging seawater filtration systems. AquaSentinel targets the monitoring-decision layer around that real operational risk. These national facts provide context; they are not presented as validation of our specific accepted AOI.

### Q15. Where is hyperspectral data?

**Answer:** Hyperspectral evidence is an optional scientific enhancement, not a dependency we force into the PoC merely for bonus points. The accepted Sentinel-2 baseline is reproducible and scientifically bounded. In incubation we would test open hyperspectral data where it can add defensible spectral discrimination, while keeping sensor-specific evidence and validation separate.

### Q16. What about Sentinel-1 oil detection?

**Answer:** It is a secondary expansion path and is not claimed as completed oil science. We deliberately keep the submission headline on the mature Sentinel-2 water-quality path. Sentinel-1 should only become a product capability after the live chain and the oil-science interpretation are validated.

### Q17. What stops false alarms?

**Answer:** Several design choices reduce unsupported escalation: strictly-prior comparison, family-aware candidate rules, recurrence as a separate evidence layer, availability-aware scoring, explicit evidence completeness and a conservative human verification step. That said, the PoC has not yet measured operational false-alert rate; prospective operator validation is required.

### Q18. Why should we choose you over a more visually impressive dashboard?

**Answer:** A dashboard can be built after the evidence contract is trustworthy. AquaSentinel already proves the difficult foundation: real EO lineage, reproducibility, transparent evidence, explicit limitations and a defined operational decision. Incubation can add the user interface and operational integrations without rebuilding the science from scratch.

### Q19. Are you saying satellite monitoring can prevent desalination shutdowns?

**Answer:** No. We are saying EO can help prioritize monitoring and field verification. The current PoC does not demonstrate prevention of a shutdown, operational savings or a guaranteed warning lead time.

### Q20. What would you accomplish during incubation?

**Answer:** Five concrete steps: use operator-approved intake geometry; implement environmental context and exposure; run prospective multi-date monitoring; conduct operator/user validation including alert and sampling workflow; and validate the commercial/procurement model. Only then would we promote additional sensor layers such as hyperspectral or Sentinel-1 where the evidence supports them.

## Phrases to avoid

- “We detect HABs.”
- “This is 70% confidence.”
- “The anomaly persisted / disappeared biologically.”
- “This protects the intake” as a demonstrated current outcome.
- “We validated early warning lead time.”
- “Our AI predicts algae.”
- “Our oil detector works.”
- “We used Satellite 813 data.”
- Any claim of customer traction, revenue, savings, ROI or deployment not supported by evidence.

## Preferred phrases

- “HAB-like water-quality observational screening.”
- “Monitoring-priority decision support.”
- “Evidence completeness 0.70.”
- “Exact-pixel observational recurrence.”
- “Review on the next valid acquisition.”
- “Analyst-defined validation AOI.”
- “Retrospective case: PARTIALLY_CONSISTENT.”
- “POST unavailable; exact lead time not estimable.”
- “Hyperspectral is an optional evidence layer for incubation.”
- “Sentinel-1 remains a secondary incomplete expansion path.”
