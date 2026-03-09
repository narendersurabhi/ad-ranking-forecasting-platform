from __future__ import annotations

import time

import pandas as pd

from ad_ranking_forecasting_platform.config import AppConfig
from ad_ranking_forecasting_platform.inference.fallback import cold_start_campaigns
from ad_ranking_forecasting_platform.ranking.explainability import reason_codes
from ad_ranking_forecasting_platform.ranking.scorer import score_candidates
from ad_ranking_forecasting_platform.retrieval.candidate_generation import generate_candidates


def rank_ads(request: dict, assets: dict, ctr_model, cvr_model, exposure_counts: pd.DataFrame):
    start = time.time()
    candidates = generate_candidates(assets["campaigns"], assets["creatives"], request, exposure_counts)
    if candidates.empty:
        return {"ranked_ads": cold_start_campaigns(), "latency_ms": int((time.time() - start) * 1000)}
    scored = score_candidates(candidates, ctr_model, cvr_model, AppConfig().scoring)
    top = scored.head(request.get("top_k", 3))
    ranked = []
    for _, row in top.iterrows():
        ranked.append(
            {
                "campaign_id": row["campaign_id"],
                "creative_id": row["creative_id"],
                "score": float(row["final_score"]),
                "ctr_score": float(row["ctr_score"]),
                "cvr_score": float(row["cvr_score"]),
                "reason_codes": reason_codes(row.to_dict()),
            }
        )
    return {"ranked_ads": ranked, "latency_ms": int((time.time() - start) * 1000)}
