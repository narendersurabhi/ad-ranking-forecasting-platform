# AGENTS change log and repository status

## Purpose
Track repository changes and provide working context for future agents.

## Current status
- Initialized production-style Python project structure for ad ranking and inventory forecasting.
- Added synthetic data generator for users, campaigns, creatives, content, impressions, and events.
- Added feature, retrieval, targeting, ranking, forecasting, inference, registry, monitoring, and API modules.
- Added training, evaluation, and model registration scripts.
- Added tests, CI workflow, docs, Dockerfiles, docker-compose, and Kubernetes manifests.
- Added Makefile targets for local end-to-end workflows.
- Added CTR calibration reliability analysis (`ctr_reliability_report.csv`) with ECE/MCE and Brier score in ranking evaluation.
- Added richer campaign pacing simulation with 14-day budget burn-down and summary reporting artifacts.
- Added persistent observability storage using SQLite and feature drift checks with PSI-based CI gate.

## Notes for future agents
- Run `make generate-data` before training scripts.
- Run `make features` before ranking model training scripts.
- API depends on local artifacts in `data/artifacts` and raw CSVs in `data/raw`.
- Use `make simulate-pacing` to generate campaign operations pacing outputs.
- Use `make check-drift` to run and persist drift checks.
- Keep this file updated whenever changes are made.

## Latest change log
- Implemented `src/ad_ranking_forecasting_platform/ranking/calibration.py` and integrated calibration outputs into `scripts/evaluate_ranking.py`.
- Implemented `src/ad_ranking_forecasting_platform/forecasting/pacing.py` and new `scripts/simulate_campaign_pacing.py`.
- Implemented `src/ad_ranking_forecasting_platform/monitoring/backend.py` and full drift logic in `src/ad_ranking_forecasting_platform/monitoring/drift.py`.
- Added `scripts/run_drift_checks.py` and CI workflow drift gate in `.github/workflows/ci.yml`.
- Added tests for calibration, pacing simulation, and drift monitoring.
