# Reviewer-facing submission outputs

These files are generated from `notebooks/aquasentinel_hab_water_quality.ipynb` using the committed small input `data/submission/hab_headline_input.json`.

- `hab_risk_summary.json` — accepted AS-107 headline result.
- `hab_risk_components.csv` — configured/effective weights, component values and contribution points.
- `hab_risk_components.svg` — actual accepted score-contribution figure.
- `hab_candidate_locator.svg` — accepted candidate-region **bounding-box** locator inside the frozen EPSG:32640 analysis grid; it is not an invented exact MultiPolygon.
- `historical_case_summary.csv` — PRE/EVENT/POST case-study summary, preserving POST as unavailable.

Scientific boundary: these are reviewer-facing visualizations of accepted observational evidence. They do not confirm HAB, toxins, species, chlorophyll concentration, water safety, or warning lead time.
