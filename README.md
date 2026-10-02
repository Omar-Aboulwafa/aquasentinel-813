# AquaSentinel 813

AquaSentinel 813 is an explainable multi-hazard marine-intake intelligence system for the Arab Youth Space Hackathon 2026.

## Mission

AquaSentinel watches the sea before a threat reaches the intake.

The PoC combines Earth-observation and environmental data to detect offshore marine anomalies, assess their relevance to monitored desalination intake zones, and prioritize earlier field verification.

## PoC Scope

### Primary hazard
- HAB-like / biological water-quality anomalies
- Sentinel-2 based monitoring
- Temporal and spectral anomaly detection
- Explainable risk scoring

### Secondary hazard
- Oil-slick surface candidates
- Sentinel-1 SAR based monitoring
- Exposure and proximity assessment

### Enhancement layers
- EnMAP hyperspectral data
- Sea-surface temperature
- Ocean currents
- Wind context

## Primary User

Desalination Plant Water Quality / Operations Manager.

## Core Decision

Where and when should monitoring or field verification be prioritized?

## Scientific Guardrails

AquaSentinel provides observational risk intelligence.

It does not independently confirm:
- toxic algae species,
- algal toxins,
- petroleum composition,
- operational plant shutdown decisions.

Field and laboratory verification remain necessary.

## Development Environment

- Python 3.11
- Conda environment: `aquasentinel813`
- Source layout: `src/aquasentinel`

## Project Status

PoC development for submission on 11 October 2026.
