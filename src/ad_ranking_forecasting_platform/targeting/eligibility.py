import pandas as pd


def enforce_frequency_cap(candidates: pd.DataFrame, exposure_counts: pd.DataFrame) -> pd.DataFrame:
    merged = candidates.merge(exposure_counts, on="campaign_id", how="left").fillna({"exposure_count": 0})
    return merged[merged["exposure_count"] < merged["frequency_cap"]]
