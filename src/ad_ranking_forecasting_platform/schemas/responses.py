from pydantic import BaseModel


class RankedAd(BaseModel):
    campaign_id: str
    creative_id: str
    score: float
    ctr_score: float
    cvr_score: float
    reason_codes: list[str]


class RankAdsResponse(BaseModel):
    request_id: str
    ranked_ads: list[RankedAd]
    latency_ms: int
    model_versions: dict[str, str]


class ForecastBucket(BaseModel):
    bucket_start: str
    predicted_impressions: int


class ForecastInventoryResponse(BaseModel):
    placement_id: str
    forecast: list[ForecastBucket]
    latency_ms: int
    model_version: str
