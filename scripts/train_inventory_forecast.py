import pandas as pd

from ad_ranking_forecasting_platform.forecasting.dataset import build_forecast_dataset
from ad_ranking_forecasting_platform.forecasting.train import save_forecast_model, train_forecast_model
from ad_ranking_forecasting_platform.paths import ARTIFACTS, DATA_RAW


def main():
    ARTIFACTS.mkdir(parents=True, exist_ok=True)
    impressions = pd.read_csv(DATA_RAW / "impressions.csv")
    ds = build_forecast_dataset(impressions)
    model = train_forecast_model(ds)
    save_forecast_model(model, ARTIFACTS / "forecast_model.joblib")


if __name__ == "__main__":
    main()
