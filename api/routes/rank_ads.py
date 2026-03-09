import pandas as pd
from fastapi import APIRouter, Depends

from ad_ranking_forecasting_platform.inference.rank_service import rank_ads
from ad_ranking_forecasting_platform.schemas.requests import RankAdsRequest
from ad_ranking_forecasting_platform.schemas.responses import RankAdsResponse
from api.dependencies import get_assets, get_metrics, get_models

router = APIRouter()


@router.post("/rank-ads", response_model=RankAdsResponse)
def rank_ads_endpoint(
    request: RankAdsRequest,
    assets=Depends(get_assets),
    models=Depends(get_models),
    metrics=Depends(get_metrics),
):
    exposure_counts = pd.DataFrame(columns=["campaign_id", "exposure_count"])
    result = rank_ads(request.model_dump(), assets, models["ctr"], models["cvr"], exposure_counts)
    metrics.inc("rank_requests")
    return {
        "request_id": request.request_id,
        "ranked_ads": result["ranked_ads"],
        "latency_ms": result["latency_ms"],
        "model_versions": {"ctr_model": "v1", "cvr_model": "v1"},
    }
