import pandas as pd


def build_forecast_dataset(impressions: pd.DataFrame) -> pd.DataFrame:
    df = impressions.copy()
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df["bucket_start"] = df["timestamp"].dt.floor("h")
    agg = (
        df.groupby(["bucket_start", "placement_id", "region", "device_type"]).size().rename("impressions").reset_index()
    )
    agg["hour"] = agg["bucket_start"].dt.hour
    agg["day"] = agg["bucket_start"].dt.dayofweek
    agg["lag_1"] = agg.groupby(["placement_id", "region", "device_type"])["impressions"].shift(1)
    agg["rolling_3"] = (
        agg.groupby(["placement_id", "region", "device_type"])["impressions"].transform(lambda x: x.rolling(3, min_periods=1).mean())
    )
    return agg.fillna(agg["impressions"].median())
