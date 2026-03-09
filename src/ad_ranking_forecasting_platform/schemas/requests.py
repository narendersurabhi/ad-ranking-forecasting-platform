from pydantic import BaseModel


class RankAdsRequest(BaseModel):
    request_id: str
    user_id: str
    content_id: str
    placement_id: str
    device_type: str
    region: str
    time_of_day: str
    top_k: int = 3


class ForecastInventoryRequest(BaseModel):
    placement_id: str
    region: str
    device_type: str
    content_type: str
    horizon: str = "24h"
