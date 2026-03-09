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

## Notes for future agents
- Run `make generate-data` before training scripts.
- Run `make features` before ranking model training scripts.
- API depends on local artifacts in `data/artifacts` and raw CSVs in `data/raw`.
- Keep this file updated whenever changes are made.
