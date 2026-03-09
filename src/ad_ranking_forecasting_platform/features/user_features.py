import pandas as pd


def build_user_history(users: pd.DataFrame, events: pd.DataFrame) -> pd.DataFrame:
    agg = events.groupby("user_id").agg(click_rate=("click", "mean"), conversion_rate=("conversion", "mean"))
    out = users.merge(agg, on="user_id", how="left").fillna({"click_rate": 0.01, "conversion_rate": 0.001})
    out["ad_fatigue_score"] = 1 - out["prior_engagement_rate"]
    return out
