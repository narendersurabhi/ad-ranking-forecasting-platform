PYTHON=python
PIP=pip

install:
	$(PIP) install -e .[dev]

generate-data:
	$(PYTHON) scripts/generate_synthetic_data.py

features:
	$(PYTHON) scripts/run_feature_pipeline.py

train-ranking:
	$(PYTHON) scripts/train_ctr_model.py && $(PYTHON) scripts/train_cvr_model.py

train-forecast:
	$(PYTHON) scripts/train_inventory_forecast.py

evaluate-ranking:
	$(PYTHON) scripts/evaluate_ranking.py

evaluate-forecast:
	$(PYTHON) scripts/evaluate_forecast.py

serve:
	uvicorn api.main:app --host 0.0.0.0 --port 8000 --reload

test:
	pytest -q

lint:
	ruff check .

simulate-pacing:
	$(PYTHON) scripts/simulate_campaign_pacing.py

check-drift:
	$(PYTHON) scripts/run_drift_checks.py
