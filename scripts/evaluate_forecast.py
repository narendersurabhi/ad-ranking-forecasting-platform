import json

import joblib
import pandas as pd

from ad_ranking_forecasting_platform.forecasting.dataset import build_forecast_dataset
from ad_ranking_forecasting_platform.forecasting.metrics import regression_metrics
from ad_ranking_forecasting_platform.forecasting.train import FEATURES
from ad_ranking_forecasting_platform.paths import ARTIFACTS, DATA_RAW


def main():
    model = joblib.load(ARTIFACTS / "forecast_model.joblib")
    ds = build_forecast_dataset(pd.read_csv(DATA_RAW / "impressions.csv"))
    y_pred = model.predict(ds[FEATURES])
    m = regression_metrics(ds["impressions"].values, y_pred)
    (ARTIFACTS / "forecast_eval.json").write_text(json.dumps(m, indent=2))
    print(m)


if __name__ == "__main__":
    main()
