# ad-ranking-forecasting-platform

Production-style Python repository that simulates an ad decisioning platform for streaming media inventory. It demonstrates candidate retrieval, ML ranking, budget and pacing logic, inventory forecasting, model registry patterns, API serving, and local deployment.

## What this project demonstrates
- Ad candidate retrieval and targeting logic
- ML-based ad ranking with CTR and CVR models
- Budget and pacing-aware business rules
- Inventory forecasting for ad supply planning
- Local model registry patterns
- Real-time inference API
- Observability and fallback mechanisms
- Containerized deployment and testability

## Architecture overview
- Data generation creates realistic synthetic users, content, campaigns, creatives, impression opportunities, and engagement events.
- Feature pipeline produces user, campaign, context, and pacing features.
- Retrieval applies targeting, budget, and frequency cap checks.
- Ranking scores candidates and applies business rules.
- Forecasting predicts impression inventory by placement and context buckets.
- Registry records model version, stage, metrics, and metadata.
- FastAPI serves ranking and forecast endpoints with in-memory metrics.

See `docs/architecture.md` and `docs/system_design.md` for system-level details.

## Local setup
```bash
python -m venv .venv && source .venv/bin/activate
pip install -e .[dev]
```

## End-to-end run
```bash
make generate-data
make features
make train-ranking
make train-forecast
make evaluate-ranking
make evaluate-forecast
make serve
```

## API
- `GET /health`
- `POST /rank-ads`
- `POST /forecast-inventory`
- `GET /metrics`

## Testing and linting
```bash
make lint
make test
```

## Assumptions
- Synthetic patterns approximate ad-tech behavior and are not production-calibrated.
- Real campaign pacing state is simulated from generated budget signals.
- Serving loads local artifacts and local CSV tables.

## Future improvements
- Calibration report for CTR probabilities
- Rich pacing simulator and budget burn-down dashboard
- Persistent metrics backend with Prometheus exporter
- Feature drift checks integrated into CI

## Interview narrative
- Retrieval and ranking are separate to reduce latency and improve control.
- CTR and CVR estimate engagement and conversion intent, then business rules enforce delivery constraints.
- Budget and pacing must run after scoring to satisfy contractual obligations.
- Forecasting informs supply planning and campaign allocation ahead of serving windows.
- Observability tracks quality, fallbacks, and latency-sensitive serving health.

## Resume bullets
- Built a production-style ad decisioning platform in Python with synthetic large-scale data, deterministic targeting, and ML ranking APIs for real-time ad serving simulations.
- Implemented CTR and CVR ranking pipelines with business-rule reranking for budget, pacing, and diversity constraints, plus reason-code explainability for top-K outputs.
- Developed inventory forecasting, local model registry workflows, CI, tests, and containerized deployment manifests to demonstrate end-to-end MLOps and platform engineering practices.
