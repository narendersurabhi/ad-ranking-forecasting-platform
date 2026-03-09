import time

from ad_ranking_forecasting_platform.forecasting.infer import forecast_horizon
from ad_ranking_forecasting_platform.inference.fallback import sparse_forecast_baseline


def forecast_inventory(request: dict, model):
    start = time.time()
    if request.get("placement_id") is None:
        return {"forecast": sparse_forecast_baseline(), "latency_ms": int((time.time() - start) * 1000)}
    horizon = 24 if request.get("horizon", "24h") == "24h" else 24 * 7
    return {"forecast": forecast_horizon(model, request, hours=horizon), "latency_ms": int((time.time() - start) * 1000)}
