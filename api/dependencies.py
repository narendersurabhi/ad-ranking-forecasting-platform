from functools import lru_cache

import joblib
import pandas as pd

from ad_ranking_forecasting_platform.monitoring.metrics import InMemoryMetrics
from ad_ranking_forecasting_platform.paths import ARTIFACTS, DATA_RAW


@lru_cache(maxsize=1)
def get_assets():
    return {
        "campaigns": pd.read_csv(DATA_RAW / "campaigns.csv"),
        "creatives": pd.read_csv(DATA_RAW / "creatives.csv"),
        "content": pd.read_csv(DATA_RAW / "content.csv"),
    }


@lru_cache(maxsize=1)
def get_models():
    return {
        "ctr": joblib.load(ARTIFACTS / "ctr_model.joblib"),
        "cvr": joblib.load(ARTIFACTS / "cvr_model.joblib"),
        "forecast": joblib.load(ARTIFACTS / "forecast_model.joblib"),
    }


@lru_cache(maxsize=1)
def get_metrics():
    return InMemoryMetrics()
