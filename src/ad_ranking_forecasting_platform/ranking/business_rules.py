import pandas as pd


def apply_business_rules(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out = out[out["remaining_budget"] > 5]
    out["diversity_penalty"] = out.groupby("advertiser_vertical").cumcount() * 0.01
    out["final_score"] = out["final_score"] - out["diversity_penalty"]
    return out
