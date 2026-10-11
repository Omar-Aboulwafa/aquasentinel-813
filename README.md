# AquaSentinel 813 — Sentinel-2 HAB / Water-Quality Observational Intelligence

**Theme:** Marine & Water Security

**One-line summary:** AquaSentinel 813 turns Sentinel-2 observations into explainable HAB-like water-quality anomaly screening, evidence-completeness diagnostics, and monitoring-priority guidance for desalination operations while preserving source provenance and scientific limitations.

## 1. Title and one-line summary

AquaSentinel 813 is an explainable Earth-observation proof of concept for marine water-quality observational intelligence. The submission headline is the mature **Sentinel-2 HAB / water-quality** path.

AquaSentinel's core principle is:

> Watch the sea before a threat reaches the intake.

The system supports a human monitoring decision; it does not autonomously declare water safe/unsafe or shut down a plant.

Sentinel-1 is a secondary multi-hazard expansion path. Its **live retrieval and metadata/access foundation is proven**, but scientific SAR pixel processing and oil/surface-slick interpretation have not started and are not claimed as completed capability.

## 2. Business use case

**Primary user:** Desalination Plant Water Quality / Operations Manager.

**Primary decision:** Where and when should monitoring or field verification be prioritized?

The business value is earlier, explainable prioritization of scarce monitoring and sampling effort. Instead of treating a satellite anomaly as a laboratory diagnosis, AquaSentinel exposes the observation, contributing evidence, evidence completeness, provenance, and a conservative monitoring recommendation.

Current headline output is **provisional observational screening**. Environmental context and intake-exposure components are not implemented in the accepted headline score, so the result remains visibly incomplete.

## 3. Problem

Coastal desalination operators can be affected by changing marine conditions, but satellite observations are indirect and can be sparse, cloudy, or scientifically ambiguous. A useful PoC therefore needs to do more than display imagery: it must preserve source identity, compare observations consistently through time, explain why a candidate area was flagged, distinguish available from unavailable evidence, and keep a human verification step in the decision chain.

AquaSentinel addresses that problem with an explainable chain:

```text
Observation
→ spectral features
→ causal temporal comparison
→ candidate anomaly geometry
→ observational recurrence
→ provisional risk + evidence completeness
→ monitoring priority
→ human field/laboratory verification
```

Scientific boundary: the current pipeline does **not** independently confirm a HAB, toxic species, toxins, chlorophyll concentration, biological probability, water safety, or an automatic operational shutdown decision.

## 4. Data used

### Headline Sentinel-2 sequence

- **Product:** Sentinel-2 Level-2A surface reflectance.
- **Discovery provider:** Copernicus Data Space Ecosystem (CDSE) STAC.
- **Pixel/asset provider:** Microsoft Planetary Computer.
- **AOI:** analyst-defined Al Raha Bay validation AOI in Abu Dhabi; it is **not** a confirmed desalination intake.
- **Analysis grid:** EPSG:32640, 20 m, 310 × 228 pixels.
- **Required Planetary Computer processing baseline:** `05.09`.
- **Reference observations:** 4, 9, 14, 24 and 29 March 2023.
- **Comparison observations:** 3 and 28 April 2023.
- **Historical-case POST:** unavailable because the frozen compatible May attempt had no exact required Planetary Computer 05.09 match; no later date was substituted.

The exact seven Sentinel-2 product identities, AOI, grid, frozen counts, lineage and expected result are committed in `data/submission/hab_headline_input.json`.

### Sentinel-1 secondary foundation

M61 / PR #38 proved the live AS-201 retrieval and metadata/access boundary for six exact frozen real Sentinel-1 products. This is an engineering foundation, not oil science. The project has not started AS-202 SAR pixel/backscatter/surface-slick scientific processing.

### Data sources and licences

- **Copernicus Sentinel-1 and Sentinel-2 data:** Sentinel data are made available on a **free, full and open** basis under the European Commission's **Legal Notice on the use of Copernicus Sentinel Data and Service Information**. Lawful use includes reproduction, distribution, communication, adaptation, modification and combination with other data. Public redistribution/communication requires source attribution. Official legal notice: https://sentinels.copernicus.eu/documents/247904/690755/Sentinel_Data_Legal_Notice
- **Copernicus Data Space Ecosystem (CDSE):** used for discovery, source identity and metadata access. Use of the CDSE service is subject to its Terms and Conditions: https://dataspace.copernicus.eu/terms-and-conditions
- **Microsoft Planetary Computer:** used as an access/asset-delivery service for the exact Sentinel products selected by the pipeline. Planetary Computer service/token use is subject to Microsoft's Terms of Use: https://planetarycomputer.microsoft.com/terms . The underlying Sentinel data remain subject to the Copernicus Sentinel legal notice above.
- **Attribution used by AquaSentinel:** reviewer-facing derived outputs based on the 2023 Sentinel-2 sequence should be read as **Contains modified Copernicus Sentinel data 2023**. Sentinel-1 AS-201 engineering evidence based on the frozen 2026 products should be read as **Contains modified Copernicus Sentinel data 2026**.

AquaSentinel does not redistribute raw Sentinel scenes or provider products. It commits compact derived evidence, source/product identifiers, provenance and reviewer outputs only. Short-lived signed URLs/tokens are never committed.

### Processing and redistribution boundary

Sentinel-2 L2A BOA surface reflectance is **not** automatically aquatic remote-sensing reflectance (Rrs), and the repository does not claim otherwise.

The repository does not redistribute raw Sentinel scenes, signed URLs, SAS tokens, credentials, or full provider products. Reviewer-facing inputs contain compact accepted evidence, source identifiers and provenance.

## 5. Technical approach

The implemented headline path is:

1. **AS-101 — Sentinel-2 discovery:** configurable CDSE STAC search with provenance.
2. **AS-102 — optical preprocessing:** strict product match, bounded asset access, XML-based BOA decoding, fixed 20 m grid and conservative water support.
3. **AS-103 — spectral features:** deterministic water-quality features from signed BOA reflectance; no event diagnosis.
4. **AS-104 — temporal baseline:** strictly-prior per-pixel comparison using frozen March references; empirical rank is not probability.
5. **AS-105 — anomaly geometry:** predeclared family-aware candidate rule with no post-result threshold tuning.
6. **AS-106 — recurrence:** exact same-grid observational recurrence; accepted A/B/C = 7/7/0. Zero recurrence does not prove biological absence.
7. **AS-107 — provisional risk:** availability-aware explanation with explicit missing context/exposure and evidence completeness.
8. **AS-108 — historical case:** retrospective observational-consistency assessment; `PARTIALLY_CONSISTENT`, POST unavailable, exact lead time not estimable.

Frozen scientific decisions are documented in `docs/DECISIONS.md`.

## 6. Installation

Requirements:

- Python **3.11** (`>=3.11,<3.12`)
- Git

```bash
git clone https://github.com/Omar-Aboulwafa/aquasentinel-813.git
cd aquasentinel-813
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install -e .
```

Windows PowerShell activation:

```powershell
.\.venv\Scripts\Activate.ps1
```

No credential file is required for the deterministic reviewer replay.

## 7. How to run

From the repository root:

```bash
python -m jupyter nbconvert \
  --to notebook \
  --execute notebooks/aquasentinel_hab_water_quality.ipynb \
  --output /tmp/aquasentinel_hab_water_quality.executed.ipynb \
  --ExecutePreprocessor.timeout=600
```

The notebook reads:

```text
data/submission/hab_headline_input.json
```

and regenerates reviewer-facing outputs under:

```text
results/submission/
```

Expected headline:

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

The notebook’s live metadata check remains optional so provider availability cannot break the default reviewer replay.

## 8. Example input and output

Example input:

- `data/submission/hab_headline_input.json`

Committed reviewer outputs:

- `results/submission/hab_risk_summary.json`
- `results/submission/hab_risk_components.csv`
- `results/submission/historical_case_summary.csv`
- `results/submission/hab_risk_components.svg`
- `results/submission/hab_candidate_locator.svg`

The locator is a bounding-box locator for the accepted region inside the frozen grid; it is not an invented reconstruction of the exact accepted MultiPolygon.

## 9. Results and limitations

Accepted 28 April 2023 headline:

- **7 candidate pixels / 802 policy-evaluable pixels**
- **one 2,800 m² candidate region**
- **0/7 exact-pixel recurrence**
- **29.52380952380953 / Watch**
- **evidence completeness: 0.70**
- **recommendation: Review on the next valid acquisition**
- spectral contribution: **20.0**
- red-edge evidence contribution: **9.523809523809526**
- persistence contribution: **0.0**
- environmental context: **unavailable / not implemented**
- intake exposure: **unavailable / not implemented**

Historical case: **PARTIALLY_CONSISTENT**. It is retrospective, event timing is month-level, alignment is area-level, POST is unavailable, and exact warning lead time is **NOT ESTIMABLE**.

Limitations:

- HAB-like spectral anomaly is not confirmed HAB.
- No species, toxin or measured chlorophyll concentration is inferred.
- Five historical observations are not statistical sufficiency.
- BOA surface reflectance is not aquatic Rrs.
- Exact-pixel recurrence cannot track moving water features.
- Al Raha is an analyst-defined validation AOI, not a confirmed desalination intake.
- The historical case is not blind/prospective biological accuracy validation.
- Sentinel-1 AS-201 live access is proven, but AS-202 SAR science/oil detection is not started.
- Hyperspectral is an optional incubation enhancement, not a P0 dependency.

Field and laboratory verification remain necessary.

## 10. Team, licence and attribution

- **Project:** AquaSentinel 813
- **Hackathon:** Arab Youth Space Hackathon 2026
- **Theme:** **Marine & Water Security**
- **Team state:** organizer platform remains authoritative for the approved roster.
- **Repository author metadata:** Omar Aboulwafa
- **EO attribution:** product/source identities and providers are retained in repository provenance; raw provider imagery is not redistributed. Data-source licensing and service terms are stated explicitly in Section 4 above.
- **Project code licence:** no standalone open-source `LICENSE` file is declared, so this README does not invent a broad reuse grant.

For engineering status and scientific evidence, see `docs/PROJECT_STATE.md`, `docs/DECISIONS.md`, and `docs/evidence/`.
