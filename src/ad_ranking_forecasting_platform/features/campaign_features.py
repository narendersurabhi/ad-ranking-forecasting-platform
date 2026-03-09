import pandas as pd


def build_campaign_features(campaigns: pd.DataFrame) -> pd.DataFrame:
    out = campaigns.copy()
    out["pacing_ratio"] = out["remaining_budget"] / out["budget"].clip(lower=1)
    out["campaign_historical_ctr"] = 0.02 + (out["bid"] / out["bid"].max()) * 0.03
    out["campaign_historical_cvr"] = out["campaign_historical_ctr"] * 0.2
    return out
