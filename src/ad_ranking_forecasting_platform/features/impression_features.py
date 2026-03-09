import pandas as pd


def build_impression_features(impressions: pd.DataFrame) -> pd.DataFrame:
    out = impressions.copy()
    out["hour_bucket"] = pd.to_datetime(out["timestamp"]).dt.hour
    out["day_bucket"] = pd.to_datetime(out["timestamp"]).dt.dayofweek
    return out
