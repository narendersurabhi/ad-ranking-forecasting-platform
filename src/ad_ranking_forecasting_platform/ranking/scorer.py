from __future__ import annotations

import pandas as pd

from ad_ranking_forecasting_platform.config import ScoringWeights
from ad_ranking_forecasting_platform.features.pacing_features import pacing_adjustment
from ad_ranking_forecasting_platform.ranking.business_rules import apply_business_rules


def score_candidates(candidates: pd.DataFrame, ctr_model, cvr_model, weights: ScoringWeights) -> pd.DataFrame:
    df = candidates.copy()
    pred_cols = ["device_type", "region", "placement_id", "bid", "quality_score", "pacing_ratio"]
    df["ctr_score"] = ctr_model.predict_proba(df[pred_cols])[:, 1]
    df["cvr_score"] = cvr_model.predict_proba(df[pred_cols])[:, 1]
    df["bid_adjustment"] = df["bid"] / df["bid"].max()
    df["pacing_adjustment"] = df["pacing_status"].map(pacing_adjustment)
    df["final_score"] = (
        weights.alpha * df["ctr_score"]
        + weights.beta * df["cvr_score"]
        + weights.gamma * df["bid_adjustment"]
        + weights.delta * df["pacing_adjustment"]
    )
    return apply_business_rules(df).sort_values("final_score", ascending=False)
