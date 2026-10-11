# AquaSentinel 813 — Sentinel-2 HAB / Water-Quality Observational Intelligence

**One-line summary:** AquaSentinel 813 turns Sentinel-2 observations into explainable HAB-like water-quality anomaly screening, evidence-completeness diagnostics, and monitoring-priority guidance for desalination operations while preserving source provenance and scientific limitations.

> **Official submission theme label:** pending organizer confirmation. The repository intentionally does not invent or silently resolve the documented registration/taxonomy conflict. See `docs/HACKATHON_SUBMISSION.md`.

## 1. Title and one-line summary

AquaSentinel 813 is an explainable Earth-observation proof of concept for marine water-quality observational intelligence. The submission headline is the mature **Sentinel-2 HAB / water-quality** path. Sentinel-1 oil/surface-slick work is secondary and is not presented as completed oil science.

AquaSentinel's core principle is:

> Watch the sea before a threat reaches the intake.

The system supports a human monitoring decision; it does not autonomously declare water safe/unsafe or shut down a plant.

## 2. Business use case

**Primary user:** Desalination Plant Water Quality / Operations Manager.

**Primary decision:** Where and when should monitoring or field verification be prioritized?

The business value is earlier, explainable prioritization of scarce monitoring and sampling effort. Instead of treating a satellite anomaly as a laboratory diagnosis, AquaSentinel exposes the observation, contributing evidence, evidence completeness, provenance, and a conservative monitoring recommendation.

Current P0 output is **provisional observational screening**. Environmental context and intake-exposure components are not implemented in the accepted headline score, so the result must remain visibly incomplete.

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
- **Required Planetary Computer processing baseline for the accepted sequence:** `05.09`.
- **Reference observations:** 4, 9, 14, 24 and 29 March 2023.
- **Comparison observations:** 3 and 28 April 2023.
- **Historical-case POST attempt:** earliest frozen compatible May 2023 acquisition was metadata-selected but had no exact required Planetary Computer 05.09 match, so POST remains **UNAVAILABLE**; no later date was substituted.

The exact seven Sentinel-2 product IDs, AOI, grid, frozen counts, product lineage and expected accepted result are committed in `data/submission/hab_headline_input.json`.

### Processing level and radiometric boundary

AS-102 decodes the delivered Sentinel-2 L2A BOA product metadata and aligns native bands to the fixed analysis grid. BOA surface reflectance is **not** automatically aquatic remote-sensing reflectance (Rrs), and the repository does not claim otherwise.

### Licence and redistribution boundary

The recorded STAC collection licence marker in accepted project evidence is `other`; AquaSentinel does not infer a broader reuse permission from that marker. This repository therefore does **not** redistribute raw Sentinel-2 scenes, signed URLs, SAS tokens, or full provider products. Reviewer-facing inputs contain only compact derived/accepted evidence, source identifiers and provenance. Anyone re-running upstream retrieval must use the original public provider services and comply with the applicable provider/data terms.

## 5. Technical approach

The implemented headline path is:

1. **AS-101 — Sentinel-2 discovery:** configurable CDSE STAC search over the AOI/date/cloud contract; metadata provenance is retained.
2. **AS-102 — optical preprocessing:** strict match to the actual Planetary Computer product, bounded native-band access, XML-based BOA decoding, fixed 20 m grid and conservative water support.
3. **AS-103 — spectral features:** six deterministic candidate water-quality features from signed BOA reflectance; no event interpretation.
4. **AS-104 — temporal baseline:** strictly prior, per-pixel, per-feature comparison using five frozen March references for the accepted April targets; empirical rank is not probability.
5. **AS-105 — anomaly geometry:** predeclared family-aware candidate rule with no post-result threshold tuning; accepted 28 April result has 7 candidate pixels in 802 policy-evaluable pixels and one 2,800 m² region.
6. **AS-106 — recurrence:** exact same-grid, consecutive-valid observational recurrence; accepted A/B/C = 7/7/0. Zero recurrence does not prove biological absence.
7. **AS-107 — provisional risk:** availability-aware weighted explanation with explicit missing context/exposure and evidence completeness.
8. **AS-108 — historical case study:** retrospective observational-consistency assessment against documented April 2023 context; accepted classification is `PARTIALLY_CONSISTENT`, POST is unavailable, and exact lead time is not estimable.

Frozen scientific decisions are documented in `docs/DECISIONS.md`. The submission notebook does not retune thresholds, weights, dates, masks, evidence families, recurrence semantics or interpretation.

## 6. Installation

### Requirements

- Python **3.11** (`>=3.11,<3.12`)
- Git
- Internet access only if you choose to use the optional live metadata/upstream retrieval path. The default reviewer replay is offline after cloning.

### Clean environment

```bash
git clone https://github.com/Omar-Aboulwafa/aquasentinel-813.git
cd aquasentinel-813
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install -e .
```

On Windows PowerShell, activate with:

```powershell
.\.venv\Scripts\Activate.ps1
```

`requirements.txt` contains exact direct pins for the reviewer environment. No credential file is required for the deterministic submission replay.

## 7. How to run

### Recommended reviewer command — deterministic end-to-end submission replay

From the repository root:

```bash
python -m jupyter nbconvert \
  --to notebook \
  --execute notebooks/aquasentinel_hab_water_quality.ipynb \
  --output /tmp/aquasentinel_hab_water_quality.executed.ipynb \
  --ExecutePreprocessor.timeout=600
```

The notebook reads the committed sample input:

```text
data/submission/hab_headline_input.json
```

and regenerates the reviewer-facing outputs in:

```text
results/submission/
```

Expected headline values:

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

### Optional live metadata check

The final notebook contains `RUN_LIVE_METADATA_CHECK = False` by default so provider availability cannot break validation. Reviewers may set it to `True` to check whether the frozen product IDs remain discoverable through the configured CDSE metadata endpoint. This optional check is not required to reproduce the committed headline result.

## 8. Example input and output

### Example input

`data/submission/hab_headline_input.json` is the compact reviewer input. It contains only accepted derived evidence and provenance required to reproduce the submission result:

- the analyst-defined AOI and fixed grid,
- exact seven Sentinel-2 identities,
- AS-105 accepted candidate/evidence counts,
- AS-106 recurrence counts,
- AS-107 frozen weights and expected result,
- AS-108 historical-case status and limitations.

It contains no raw Earth-observation scene, secret, signed URL or restricted imagery.

### Example outputs

The notebook regenerates and the repository commits:

- `results/submission/hab_risk_summary.json`
- `results/submission/hab_risk_components.csv`
- `results/submission/historical_case_summary.csv`
- `results/submission/hab_risk_components.svg`
- `results/submission/hab_candidate_locator.svg`

The locator is explicitly a **bounding-box locator** for the accepted region inside the frozen analysis grid. It is not presented as an invented reconstruction of the exact accepted MultiPolygon.

## 9. Results and limitations

### Accepted headline result

For the accepted 28 April 2023 observation, the frozen AS-105 policy produced **7 candidate pixels** inside **802 policy-evaluable pixels**, one candidate region covering **2,800 m²**. AS-106 found **0/7 exact-pixel recurrence** among target candidates with valid prior observational history. Under frozen Decision 052 weights, the accepted AS-107 result is:

- **29.52380952380953 / Watch**
- **evidence completeness: 0.70**
- **component coverage: 0.70**
- **recommendation: Review on the next valid acquisition**
- spectral-anomaly contribution: **20.0 points**
- red-edge evidence contribution: **9.523809523809526 points**
- persistence contribution: **0.0 points**
- environmental context: **unavailable / not implemented**
- intake exposure: **unavailable / not implemented**

The historical case study is **PARTIALLY_CONSISTENT** with documented April 2023 area/month context. It is retrospective, the event timing is only month-level, spatial alignment is only area-level, required POST is unavailable, and exact warning lead time is **NOT ESTIMABLE**.

### Limitations that must remain visible

- HAB-like spectral anomaly is not confirmed HAB.
- No species, toxin or measured chlorophyll concentration is inferred by AquaSentinel.
- Five historical observations are not statistical sufficiency; empirical rank granularity is coarse.
- BOA surface reflectance is not aquatic Rrs.
- The current score is provisional because environmental context and intake exposure are unavailable.
- Exact-pixel recurrence cannot track moving water features and 0 recurrence is not biological absence.
- Al Raha is an analyst-defined validation AOI, not a confirmed desalination intake.
- The historical case is not blind/prospective biological accuracy validation.
- Sentinel-1 oil remains secondary; AS-202 preprocessing/oil science is not complete and is not claimed as a headline result.
- Hyperspectral data is an optional enhancement, not a P0 dependency.

Field and laboratory verification remain necessary.

## 10. Team, licence and attribution

- **Project:** AquaSentinel 813.
- **Hackathon:** Arab Youth Space Hackathon 2026.
- **Team state:** the organizer Cockpit is the authoritative source for the approved three-member roster; personal roster details are intentionally not duplicated in submission-readiness documentation.
- **Repository author metadata:** Omar Aboulwafa.
- **Official submission theme label:** pending organizer confirmation because the repository records a current registration/taxonomy conflict.
- **Earth-observation attribution:** Sentinel-2 source/product identities and providers are preserved in repository provenance; raw provider imagery is not redistributed here.
- **Project code licence:** no standalone open-source `LICENSE` file is currently declared in the repository, so this README does not invent a broad reuse grant. Submission materials are provided for hackathon review subject to repository access and applicable third-party data terms.

For the authoritative current submission contract, deadline interpretation, external theme/access blockers and readiness matrix, see `docs/HACKATHON_SUBMISSION.md`.
