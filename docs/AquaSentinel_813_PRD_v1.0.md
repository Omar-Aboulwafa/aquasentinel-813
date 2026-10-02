# AquaSentinel 813 — Product Requirements & Delivery Plan v1.0

**Status:** FROZEN FOR PoC IMPLEMENTATION
**Challenge:** Arab Youth Space Hackathon 2026 — Track 03: Water Security & Marine Environments
**Working product name:** AquaSentinel 813
**PoC deadline:** 11 October 2026
**Primary user:** Desalination Plant Water Quality / Operations Manager
**Primary job-to-be-done:** Detect emerging marine hazards early enough to prioritize verification and monitoring before they threaten seawater intake operations.

---

# 1. Executive Product Definition

## 1.1 One-sentence proposition

> **AquaSentinel 813 watches the sea before a threat reaches the intake.**

## 1.2 Mentor-format statement

> **We help desalination plant operations teams use Earth-observation and environmental data to identify marine hazards approaching seawater intakes earlier, understand why the risk is elevated, and prioritize monitoring actions before water-quality conditions threaten plant performance.**

## 1.3 PoC thesis

Current intake monitoring is strongest at or near the plant. Earth observation adds spatial awareness offshore. AquaSentinel converts satellite and environmental observations into a simple operational question:

> **What is happening offshore, could it affect my monitored intake zone, and what should I verify first?**

The PoC will prove this for two hazard classes:

1. **Harmful-algal-bloom-related / biological water anomaly** — primary, full pipeline.
2. **Oil-slick / marine surface pollution** — secondary demonstrator.

Environmental context such as sea-surface temperature, currents and wind supports exposure assessment and explanation.

---

# 2. Frozen Scope

## 2.1 Must be complete for submission (P0)

### Hazard Module A — HAB / biological anomaly
- Sentinel-2 based water monitoring.
- Water/cloud/land masks.
- Chlorophyll-related and red-edge spectral features.
- Temporal anomaly against a local baseline.
- Persistence logic across observations.
- Explainable HAB-risk score.
- Historical event demonstration.
- Map layer + evidence panel + monitoring recommendation.

### Hazard Module B — Oil slick
- Sentinel-1 SAR based surface-slick candidate detection.
- Contextual filtering to reduce obvious look-alikes.
- Historical oil-spill demonstration.
- Exposure/proximity assessment to a user-defined intake/monitoring zone.
- Explainable oil-risk score.
- Map layer + evidence panel + monitoring recommendation.

### Cross-cutting
- AOI/date selection.
- Intake/monitoring-zone geometry.
- Data provenance.
- Risk severity bands.
- Confidence and limitations.
- Exportable event/risk record.
- Reproducible pipeline.
- Working demo.

## 2.2 Should be included if data/time allow (P1)

- EnMAP hyperspectral characterization for selected water anomalies.
- Copernicus Marine currents.
- Sea-surface temperature anomaly.
- ERA5 10 m wind.
- Simple short-horizon drift/exposure estimate.
- SHAP/model feature contribution where a fitted model is used.
- Historical time slider.
- Side-by-side multispectral vs hyperspectral evidence.

## 2.3 Explicitly out of scope for PoC

- Autonomous plant shutdown/control.
- Toxic-species or toxin confirmation from satellite alone.
- Full operational ocean forecast model.
- Digital twin of a desalination facility.
- Mobile app.
- Dedicated foundation model training.
- Real-time 24/7 production SLA.
- Proprietary plant telemetry integration.
- Jellyfish detection.
- Salinity hazard model.
- Full Gulf-wide deployment.
- Native Satellite 813 dependence.

---

# 3. Product Users

## 3.1 Primary persona

### Desalination Plant Water Quality / Operations Manager

Needs to know:
- Is there an abnormal marine condition offshore?
- Which hazard is most plausible?
- How strong is the evidence?
- Is the anomaly persistent?
- Is it near or moving toward the monitored intake zone?
- Where should field sampling/verification be prioritized?
- What changed compared with normal conditions?

Does **not** need:
- Raw band math.
- Black-box model output without explanation.
- Hundreds of raster layers.
- Autonomous operational commands.

## 3.2 Secondary users

- Environmental monitoring authority.
- Utility central operations team.
- Marine water-quality analyst.
- Coastal infrastructure operator.
- Emergency/environmental response planner.

---

# 4. Core User Journey

1. User opens AquaSentinel.
2. Selects a monitored site/AOI and date window.
3. System loads relevant Earth-observation observations.
4. System identifies usable water pixels and removes obvious cloud/land contamination.
5. Hazard modules independently evaluate:
   - HAB-like biological anomaly.
   - Oil-slick surface anomaly.
6. System calculates hazard-specific risk and confidence.
7. Exposure layer assesses proximity/persistence and, when available, current/wind context.
8. Map highlights priority zones.
9. User clicks a zone.
10. Evidence panel explains:
    - hazard type,
    - risk level,
    - confidence,
    - contributing signals,
    - timestamp,
    - data sources,
    - persistence,
    - monitored-zone proximity/exposure.
11. System recommends a **monitoring/verification priority**, never an autonomous plant action.
12. User can export the alert/risk record.

---

# 5. Product Language & Safety Guardrails

The product must say:

- **“HAB-like spectral anomaly”**
- **“elevated biological water-quality risk”**
- **“oil-slick candidate”**
- **“field verification recommended”**
- **“confidence”**
- **“observational risk”**

The product must not claim:

- “toxic algae confirmed”
- “oil spill confirmed” solely from a single remote-sensing signal
- “safe / unsafe water” as a definitive operational certification
- “shut down intake”
- species identification unless verified with appropriate evidence

Satellite analysis supports operational awareness; it does not replace laboratory or in-situ confirmation.

---

# 6. Hazard Model Design

## 6.1 HAB / Biological Anomaly Engine

### Inputs
- Sentinel-2 surface reflectance.
- Historical Sentinel-2 observations for local baseline.
- Optional EnMAP hyperspectral scene.
- Optional SST / SST anomaly.
- Optional currents.
- Optional wind.

### Core Sentinel-2 features
Candidate features should be tested rather than blindly fixed:

- Blue reflectance (B2)
- Green reflectance (B3)
- Red reflectance (B4)
- Red-edge bands (B5, B6, B7)
- NIR / narrow NIR (B8/B8A)
- NDCI-like chlorophyll proxy
- red-edge ratios
- water-colour change
- local temporal z-score / percentile anomaly
- spatial texture / connected anomaly area
- persistence across valid observations

### Baseline approach

**Phase 1 — explainable anomaly model**
- Build local climatological/recent baseline from clear observations.
- Calculate robust deviation per feature.
- Produce anomaly score.

**Phase 2 — fitted classifier only if labels support it**
- Random Forest or Gradient Boosting.
- Calibration where possible.
- Cross-validation by date/event, not random-pixel leakage.
- SHAP/feature contribution for explanation.

### Output
- `hab_risk_score` 0–100
- `confidence` 0–1
- `drivers[]`
- `persistence`
- `observed_at`
- `recommended_monitoring_priority`

---

## 6.2 Oil-Slick Engine

### Inputs
- Sentinel-1 SAR.
- Optional Sentinel-2 optical confirmation.
- Historical/reference SAR scene.
- Wind context where available.

### Core logic
- Radiometric calibration / normalized backscatter workflow.
- Speckle-aware smoothing.
- Water mask.
- Detect anomalously low-backscatter connected regions.
- Shape/size/context filters.
- Compare against previous/reference observation.
- Flag common look-alike risk conditions where possible.
- Optical cross-check if a cloud-free Sentinel-2 scene is temporally close.

### Output
- `oil_candidate_score` 0–100
- `confidence` 0–1
- `area_km2`
- `persistence`
- `drivers[]`
- `observed_at`
- `recommended_monitoring_priority`

### Critical wording
The module detects **surface-slick candidates**, not laboratory-confirmed petroleum.

---

# 7. Exposure & Intake-Risk Layer

Hazards remain separate. Do **not** mathematically combine “algae” and “oil” into one scientific phenomenon.

For each hazard, exposure is assessed independently using:

- distance to monitored intake/zone,
- hazard polygon size,
- persistence,
- direction of currents if available,
- wind context where relevant,
- simple advection estimate when justified.

## 7.1 Hazard-specific operational score

For PoC use an explainable, configurable heuristic first.

### HAB operational risk — initial tunable formulation

```
0.35 * spectral_anomaly
+ 0.20 * chlorophyll_red_edge_signal
+ 0.15 * persistence
+ 0.15 * environmental_context
+ 0.15 * intake_exposure
```

### Oil operational risk — initial tunable formulation

```
0.45 * sar_slick_likelihood
+ 0.15 * persistence
+ 0.20 * intake_exposure
+ 0.10 * drift_support
+ 0.10 * optical_or_context_confirmation
```

**Important:** These are PoC weighting hypotheses, not validated scientific constants. They must be configurable and disclosed.

## 7.2 Overall site status

Do not average unrelated hazard classes.

Use:

```
overall_site_alert = highest credible active hazard level
```

Dashboard still displays hazard-specific scores separately.

---

# 8. Risk Bands

| Score | Label | Meaning |
|---:|---|---|
| 0–24 | Normal | No material anomaly in current usable observations |
| 25–49 | Watch | Weak/early anomaly; continue observation |
| 50–74 | Elevated | Meaningful anomaly; prioritize review / targeted verification |
| 75–100 | High | Strong multi-signal anomaly; high-priority field verification |

If confidence is low, the UI must visibly downgrade the interpretation even if the raw risk score is high.

---

# 9. Data Architecture

```text
                   ┌──────────────────────────────────┐
                   │       Earth Observation          │
                   ├──────────────────────────────────┤
                   │ Sentinel-2  | Sentinel-1         │
                   │ Landsat     | EnMAP              │
                   └───────────────┬──────────────────┘
                                   │
                         STAC / API / COG / HDF5
                                   │
                                   ▼
                   ┌──────────────────────────────────┐
                   │       Ingestion & Catalog        │
                   │ AOI • Date • Provenance • Cache │
                   └───────────────┬──────────────────┘
                                   │
                                   ▼
                   ┌──────────────────────────────────┐
                   │          Pre-processing          │
                   │ Cloud • Land • Water • Align    │
                   │ SAR calibration • Reprojection  │
                   └───────────────┬──────────────────┘
                                   │
                    ┌──────────────┴──────────────┐
                    ▼                             ▼
       ┌────────────────────────┐     ┌────────────────────────┐
       │ HAB Feature Engine     │     │ Oil Feature Engine     │
       │ spectral • temporal    │     │ SAR • shape • change   │
       └───────────┬────────────┘     └───────────┬────────────┘
                   │                              │
                   ▼                              ▼
       ┌────────────────────────┐     ┌────────────────────────┐
       │ HAB Risk Model         │     │ Oil Risk Model         │
       └───────────┬────────────┘     └───────────┬────────────┘
                   └──────────────┬───────────────┘
                                  │
                                  ▼
                   ┌──────────────────────────────────┐
                   │    Environmental Context Layer   │
                   │ SST • currents • wind • history │
                   └───────────────┬──────────────────┘
                                   │
                                   ▼
                   ┌──────────────────────────────────┐
                   │      Intake Exposure Engine      │
                   │ proximity • persistence • drift │
                   └───────────────┬──────────────────┘
                                   │
                                   ▼
                   ┌──────────────────────────────────┐
                   │ Explainable Decision Layer       │
                   │ risk • confidence • drivers      │
                   │ monitoring priority              │
                   └───────────────┬──────────────────┘
                                   │
                                   ▼
                   ┌──────────────────────────────────┐
                   │         PoC Dashboard            │
                   │ map • timeline • alert • export  │
                   └──────────────────────────────────┘
```

---

# 10. Frozen Dataset Strategy

## 10.1 P0 — Required

| Dataset | Role |
|---|---|
| Sentinel-2 | HAB/water-colour surveillance and temporal anomaly |
| Sentinel-1 SAR | Oil-slick candidate detection |
| Historical event labels/reports | Validation |
| User-defined intake/AOI geometry | Exposure / product demo |

## 10.2 P1 — Strong enhancement

| Dataset | Role |
|---|---|
| EnMAP | Hyperspectral characterization / confidence enhancement |
| Copernicus Marine SST | Environmental context |
| Copernicus Marine currents | Exposure / advection estimate |
| ERA5 10 m wind | Surface transport/context |
| Landsat 8/9 | Historical / thermal cross-check |

## 10.3 P2 — Only if useful

| Dataset | Role |
|---|---|
| Planet / high-resolution imagery | visual/local detail |
| Other public water-quality products | corroboration |
| In-situ public observations | validation |

---

# 11. Validation Strategy

## 11.1 Biological anomaly validation

### Primary candidate
**Raha Beach, Abu Dhabi — April 2023**

Use official environmental reporting as event reference.

Analysis window:
- pre-event baseline,
- event window,
- post-event/recovery window.

Questions:
1. Did usable satellite observations show a significant anomaly?
2. Which features changed?
3. Did the anomaly persist spatially/temporally?
4. Would AquaSentinel have raised a Watch/Elevated status?
5. How early relative to the documented event could the signal be observed?

### Secondary candidate
**Fujairah — April 2026 bloom/discoloration event**

Use only if event timing/location and cloud-free EO observations support credible analysis.

## 11.2 Oil validation

### Primary candidate
**Kharg Island / Persian Gulf — May 2026**

Questions:
1. Can Sentinel-1 identify the slick-like surface anomaly?
2. Is it spatially coherent and temporally persistent?
3. Can optical/context data support interpretation?
4. Can the exposure engine demonstrate how a monitored coastal site would be assessed?

## 11.3 Validation rules

- Never validate and train on identical pixel samples without temporal/event separation.
- Report missing/cloud-contaminated observations.
- Report false positives encountered.
- Keep “event known from external report” separate from “satellite-derived evidence.”
- Capture screenshots/maps of before/during/after periods.

---

# 12. Hyperspectral Strategy

Hyperspectral data is an enhancement layer, not a dependency.

### Sentinel-2 role
**Where/when is an abnormal water signal visible?**

### EnMAP / future Satellite 813 role
**What additional spectral structure can characterize or strengthen the interpretation?**

PoC comparison:
- Multispectral feature view.
- Hyperspectral spectral curve / selected wavelengths.
- Show whether hyperspectral evidence materially changes confidence or characterization.

Avoid:
- feeding all bands into a black box only to claim “hyperspectral AI.”

---

# 13. UI Requirements

## 13.1 Dashboard layout

### Header
- Product name.
- Selected site.
- Current/latest observation timestamp.
- Data freshness status.

### Map
Layers:
- base map,
- intake/monitoring zone,
- HAB anomaly,
- oil-slick candidates,
- optional currents,
- optional SST anomaly.

### Site status panel
- highest active hazard,
- risk level,
- confidence,
- latest observation,
- recommended monitoring priority.

### Hazard detail panel
- evidence,
- main drivers,
- persistence,
- distance/exposure,
- uncertainty,
- source datasets.

### Timeline
- date selector,
- event markers,
- risk over time.

### Evidence view
- Sentinel-2 false/true-colour or selected product.
- SAR view for oil.
- hyperspectral chart when available.

### Export
- JSON or CSV alert record.
- GeoJSON hazard geometry if available.

## 13.2 PoC technology choice

**Recommended:** Python core package + Streamlit web app.

Reason:
- fastest path to an end-to-end demonstrator,
- strong geospatial/data-science ecosystem,
- easy deployment,
- keeps computation and UI connected,
- avoids spending submission week building product plumbing.

Optional FastAPI layer only after the core PoC is stable.

---

# 14. Suggested Repository Structure

```text
aquasentinel-813/
├── README.md
├── LICENSE
├── pyproject.toml
├── .env.example
├── app/
│   ├── streamlit_app.py
│   ├── pages/
│   └── components/
├── src/aquasentinel/
│   ├── config/
│   ├── catalog/
│   │   ├── stac.py
│   │   └── provenance.py
│   ├── ingestion/
│   │   ├── sentinel1.py
│   │   ├── sentinel2.py
│   │   ├── enmap.py
│   │   ├── copernicus_marine.py
│   │   └── era5.py
│   ├── preprocessing/
│   │   ├── optical.py
│   │   ├── sar.py
│   │   ├── masks.py
│   │   └── alignment.py
│   ├── features/
│   │   ├── water.py
│   │   ├── spectral.py
│   │   ├── temporal.py
│   │   └── sar.py
│   ├── hazards/
│   │   ├── hab.py
│   │   └── oil.py
│   ├── exposure/
│   │   ├── proximity.py
│   │   └── advection.py
│   ├── risk/
│   │   ├── scoring.py
│   │   ├── confidence.py
│   │   └── explain.py
│   ├── validation/
│   └── export/
├── notebooks/
│   ├── 01_hab_event_exploration.ipynb
│   ├── 02_oil_event_exploration.ipynb
│   ├── 03_hyperspectral_comparison.ipynb
│   └── 04_validation_summary.ipynb
├── data/
│   ├── aoi/
│   ├── reference/
│   └── cache/
├── tests/
├── docs/
│   ├── ARCHITECTURE.md
│   ├── DATA_SOURCES.md
│   ├── MODEL_CARD.md
│   ├── LIMITATIONS.md
│   └── VALIDATION.md
└── submission/
    ├── pitch/
    ├── demo/
    └── figures/
```

---

# 15. Technical Stack

## Core
- Python 3.11
- numpy
- pandas
- xarray
- rasterio / rioxarray
- geopandas
- shapely
- pyproj
- pystac-client
- stackstac where useful
- scikit-learn
- scipy
- matplotlib for analysis figures
- plotly for interactive dashboard plots
- Streamlit

## Optional
- LightGBM / XGBoost
- SHAP
- leafmap / folium / pydeck
- Copernicus Marine Toolbox
- cdsapi / earthkit
- dask for larger raster workloads

## Engineering rules
- Pin versions.
- Preserve CRS explicitly.
- Store dataset/product IDs.
- Cache derived results.
- Separate raw observations from derived products.
- Make risk weights configurable.
- Never hard-code secrets.
- Log every external/pretrained model and licence.

---

# 16. Alert Object Schema

Example internal object:

```json
{
  "site_id": "demo-site-01",
  "observed_at": "2026-05-08T10:00:00Z",
  "hazard": "oil_surface_slick_candidate",
  "risk_score": 78,
  "risk_band": "high",
  "confidence": 0.82,
  "persistence_observations": 2,
  "distance_to_monitoring_zone_km": 18.4,
  "drivers": [
    {"name": "sar_low_backscatter_anomaly", "contribution": "high"},
    {"name": "connected_area", "contribution": "moderate"},
    {"name": "temporal_persistence", "contribution": "moderate"}
  ],
  "recommended_action": "Prioritize field verification and increase monitoring frequency.",
  "sources": [
    {"platform": "Sentinel-1", "product_id": "..."}
  ],
  "limitations": [
    "Remote sensing cannot independently confirm petroleum composition."
  ]
}
```

---

# 17. Definition of Done — PoC

The PoC is submission-ready only when all are true:

- [ ] A user can select/open a demo site.
- [ ] At least one real historical HAB-related event is processed end-to-end.
- [ ] At least one real oil-slick event is processed end-to-end.
- [ ] Risk maps are derived from real EO data, not manually drawn.
- [ ] Every alert contains source provenance.
- [ ] Every alert contains confidence and limitations.
- [ ] Risk explanation lists the main evidence.
- [ ] Product recommends monitoring/verification, not automated shutdown.
- [ ] At least one before/during/after comparison is shown.
- [ ] HAB and oil hazards remain separately interpretable.
- [ ] The system can run reproducibly from a documented environment.
- [ ] README includes setup and demo steps.
- [ ] DATA_SOURCES.md records source/product/licence.
- [ ] MODEL_CARD.md records pretrained/fitted models.
- [ ] LIMITATIONS.md is explicit.
- [ ] Demo has a stable fallback dataset/cache in case live APIs fail.
- [ ] Screenshots/video of the working PoC exist before submission day.

---

# 18. Implementation Backlog

## EPIC 0 — Project foundation

### AS-001 Repository scaffold
**Priority:** P0
**Acceptance criteria:**
- repository structure created,
- Python environment reproducible,
- `.env.example`,
- basic CI/test command,
- README skeleton.

### AS-002 Configuration & AOI model
**Priority:** P0
**Acceptance criteria:**
- AOI stored as GeoJSON,
- monitored intake/zone configurable,
- date range configurable,
- risk weights configurable.

### AS-003 Provenance model
**Priority:** P0
**Acceptance criteria:**
- each raster/derived result can report source, product ID, acquisition timestamp and processing version.

---

## EPIC 1 — Sentinel-2 / HAB pipeline

### AS-101 STAC Sentinel-2 search
**Priority:** P0
Search by AOI/date/cloud metadata and return candidate scenes.

### AS-102 Optical preprocessing
**Priority:** P0
Cloud mask, land mask, water mask, reprojection/alignment.

### AS-103 Spectral feature extraction
**Priority:** P0
Generate chlorophyll-related/red-edge/water-colour candidate features.

### AS-104 Temporal baseline
**Priority:** P0
Calculate robust local baseline and anomaly per valid observation.

### AS-105 HAB anomaly geometry
**Priority:** P0
Create coherent candidate anomaly polygons/grid.

### AS-106 Persistence
**Priority:** P0
Track anomaly recurrence over consecutive valid observations.

### AS-107 HAB risk & confidence
**Priority:** P0
Output risk score, band, confidence and drivers.

### AS-108 HAB historical validation
**Priority:** P0
Raha Beach 2023 before/event/after analysis documented.

---

## EPIC 2 — Sentinel-1 / Oil pipeline

### AS-201 Sentinel-1 data retrieval
**Priority:** P0

### AS-202 SAR preprocessing
**Priority:** P0
Calibration/normalization and water-area preparation.

### AS-203 Low-backscatter candidate detection
**Priority:** P0

### AS-204 Candidate filtering
**Priority:** P0
Filter obvious small/noisy or implausible geometries.

### AS-205 Temporal/reference comparison
**Priority:** P0

### AS-206 Oil risk & confidence
**Priority:** P0

### AS-207 Kharg event validation
**Priority:** P0
Document before/during/after or multi-date observations.

---

## EPIC 3 — Environmental context

### AS-301 Copernicus Marine SST
**Priority:** P1

### AS-302 Copernicus Marine currents
**Priority:** P1

### AS-303 ERA5 wind
**Priority:** P1

### AS-304 Context normalization
**Priority:** P1
Convert context variables into interpretable anomaly/support features.

---

## EPIC 4 — Exposure engine

### AS-401 Intake proximity
**Priority:** P0
Calculate hazard distance to monitored zone.

### AS-402 Exposure scoring
**Priority:** P0
Add proximity and persistence to hazard operational score.

### AS-403 Simple advection estimate
**Priority:** P1
Only when current data quality supports it.

### AS-404 Exposure explanation
**Priority:** P0
Return human-readable reasons.

---

## EPIC 5 — Hyperspectral enhancement

### AS-501 EnMAP scene discovery
**Priority:** P1

### AS-502 EnMAP preprocessing
**Priority:** P1

### AS-503 Spectral extraction
**Priority:** P1
Extract selected water/anomaly spectra.

### AS-504 Multispectral vs hyperspectral comparison
**Priority:** P1
Show what extra information the hyperspectral observation contributes.

---

## EPIC 6 — Dashboard

### AS-601 Site overview
**Priority:** P0

### AS-602 Interactive map
**Priority:** P0

### AS-603 Hazard toggles
**Priority:** P0

### AS-604 Alert/evidence panel
**Priority:** P0

### AS-605 Timeline
**Priority:** P0

### AS-606 Evidence imagery
**Priority:** P0

### AS-607 Hyperspectral evidence view
**Priority:** P1

### AS-608 Export
**Priority:** P1

---

## EPIC 7 — Validation & scientific quality

### AS-701 Validation metrics
**Priority:** P0

### AS-702 False-positive review
**Priority:** P0

### AS-703 Uncertainty documentation
**Priority:** P0

### AS-704 Scientific claims review
**Priority:** P0

---

## EPIC 8 — Submission package

### AS-801 README final
**Priority:** P0

### AS-802 Architecture diagram
**Priority:** P0

### AS-803 Data/source/licence table
**Priority:** P0

### AS-804 Model card
**Priority:** P0

### AS-805 Limitations document
**Priority:** P0

### AS-806 Demo script
**Priority:** P0

### AS-807 Demo recording
**Priority:** P0

### AS-808 Pitch deck content
**Priority:** P0

### AS-809 Business case
**Priority:** P0

### AS-810 Submission-form mapping
**Priority:** P0
Complete as soon as exact required fields/formats are visible in the platform.

---

# 19. Delivery Sequence — 2 to 11 October

## 2 Oct — Freeze & scaffold
- PRD frozen.
- repository scaffold.
- AOIs/event list.
- data-access smoke tests.

## 3 Oct — HAB ingestion/preprocessing
- Sentinel-2 search.
- masks.
- event imagery.
- first derived water products.

## 4 Oct — HAB anomaly
- spectral features.
- temporal baseline.
- event map.
- first risk score.

## 5 Oct — Oil module
- Sentinel-1 ingestion.
- SAR anomaly detection.
- Kharg event map.

## 6 Oct — Risk/exposure
- proximity.
- persistence.
- confidence.
- evidence explanations.

## 7 Oct — Dashboard v0
- map.
- event selection.
- hazard panels.
- timeline.

## 8 Oct — Environmental context
- SST/current/wind where useful.
- simple exposure enhancement.

## 9 Oct — Hyperspectral
- EnMAP sample.
- comparison figure.
- integration if credible.

## 10 Oct — Submission hardening
- validation.
- limitations.
- demo recording.
- pitch/business case.
- offline cache/fallback.
- no major new features.

## 11 Oct — Final QA & submission
- reproduce demo from clean environment.
- verify links/files.
- submit early.
- retain local and cloud backups.

---

# 20. Kill Criteria / Time Protection

If a P1 item threatens a P0 requirement, drop it.

Drop or simplify:
1. drift simulation,
2. hyperspectral integration,
3. ML classifier,
4. exports,
5. advanced UI,

before dropping:
- real EO-derived HAB result,
- real EO-derived oil result,
- explainability,
- provenance,
- validation,
- working map/demo.

---

# 21. Risk Register

| Risk | Response |
|---|---|
| Cloud cover blocks optical event | use alternative dates/events; rely on SAR for oil; document missing data |
| EnMAP scene unavailable for exact event | use a representative scene to demonstrate hyperspectral method; do not pretend it validates the event |
| Too few HAB labels | use explainable anomaly model instead of overfit classifier |
| Oil false positives from low wind/natural films | context filters + confidence + “candidate” wording |
| Live API failure during demo | cache validated scenes and derived products |
| External dataset access/login delay | keep Sentinel-1/2 P0 independent from external context |
| Scope explosion | enforce P0/P1/P2 and kill criteria |
| Scientific overclaim | explicit terminology and limitations |
| Submission format changes | keep modular assets: repo, demo video, figures, short text, architecture, pitch |

---

# 22. Judging Narrative

## Problem
Desalination plants depend on seawater intakes exposed to offshore biological and pollution hazards.

## User
Water-quality / operations manager.

## Data
Use each sensor for what it is good at:
- Sentinel-2: water-colour / biological anomalies.
- Sentinel-1: surface slicks.
- EnMAP / 813: detailed spectral characterization.
- Marine/environmental data: exposure context.

## Decision
Where should monitoring and field verification be prioritized?

## Product
Explainable risk map + evidence + monitoring priority.

## Impact
Move awareness farther offshore and earlier in time than intake-only monitoring.

## Scalability
One intake → multiple plants → national coastline → Gulf / Red Sea coastal infrastructure.

---

# 23. Business Model Hypothesis

Initial B2B/B2G product options:

1. **Per-site annual monitoring subscription**
2. **Utility-wide multi-site licence**
3. **API / risk-feed subscription**
4. **Environmental authority monitoring licence**
5. **Enterprise integration / custom analytics**

Potential customer classes:
- desalination utilities,
- water authorities,
- environmental agencies,
- coastal industrial operators,
- ports,
- aquaculture operators.

The PoC does not need pricing validation. It must demonstrate a credible buyer and operational value chain.

---

# 24. Submission Asset Checklist

Prepare even before exact platform format is fully known:

- 1 working URL/demo.
- GitHub repository.
- README.
- 1 architecture figure.
- 1 problem/user/decision figure.
- 1 HAB validation figure.
- 1 oil validation figure.
- 1 hyperspectral comparison figure if available.
- 90–180 sec demo recording.
- concise methodology.
- data/source/licence table.
- limitations.
- business model summary.
- team roles.
- 5–7 slide pitch content.

---

# 25. Final Frozen Product Statement

> **AquaSentinel 813 is an explainable, multi-hazard marine-intake intelligence system that combines Earth observation and environmental context to detect biological and pollution anomalies offshore, assess their relevance to monitored desalination intake zones, and prioritize earlier field verification.**

**PoC core:** HAB + oil.
**Product vision:** multi-hazard seawater-intake protection intelligence.
**Scientific principle:** detect → explain → assess exposure → prioritize verification.
**Product principle:** real decision + right data + clear user.
