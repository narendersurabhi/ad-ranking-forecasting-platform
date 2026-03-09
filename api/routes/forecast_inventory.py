from fastapi import APIRouter, Depends

from ad_ranking_forecasting_platform.inference.forecast_service import forecast_inventory
from ad_ranking_forecasting_platform.schemas.requests import ForecastInventoryRequest
from ad_ranking_forecasting_platform.schemas.responses import ForecastInventoryResponse
from api.dependencies import get_metrics, get_models

router = APIRouter()


@router.post("/forecast-inventory", response_model=ForecastInventoryResponse)
def forecast_endpoint(request: ForecastInventoryRequest, models=Depends(get_models), metrics=Depends(get_metrics)):
    out = forecast_inventory(request.model_dump(), models["forecast"])
    metrics.inc("forecast_requests")
    return {
        "placement_id": request.placement_id,
        "forecast": out["forecast"],
        "latency_ms": out["latency_ms"],
        "model_version": "forecast_v1",
    }
