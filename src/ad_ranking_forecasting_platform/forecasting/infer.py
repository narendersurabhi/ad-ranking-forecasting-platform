from datetime import datetime, timedelta

import pandas as pd

from ad_ranking_forecasting_platform.forecasting.train import FEATURES


def forecast_horizon(model, context: dict, hours: int = 24) -> list[dict]:
    now = datetime(2026, 3, 10, 18)
    rows = []
    for i in range(hours):
        ts = now + timedelta(hours=i)
        row = {
            "placement_id": context["placement_id"],
            "region": context["region"],
            "device_type": context["device_type"],
            "hour": ts.hour,
            "day": ts.weekday(),
            "lag_1": context.get("lag_1", 1000),
            "rolling_3": context.get("rolling_3", 1100),
        }
        pred = float(model.predict(pd.DataFrame([row])[FEATURES])[0])
        rows.append({"bucket_start": ts.isoformat(), "predicted_impressions": max(0, int(pred))})
    return rows
