from ad_ranking_forecasting_platform.paths import ARTIFACTS
from ad_ranking_forecasting_platform.registry.model_registry import LocalModelRegistry


def main():
    reg = LocalModelRegistry(ARTIFACTS / "model_registry.json")
    reg.register("ctr_model", "v1", "production", str(ARTIFACTS / "ctr_model.joblib"), {"auc": 0.7}, {"owner": "ml"})
    reg.register("forecast_model", "v1", "production", str(ARTIFACTS / "forecast_model.joblib"), {"mae": 100}, {"owner": "ml"})


if __name__ == "__main__":
    main()
