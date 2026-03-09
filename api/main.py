from fastapi import FastAPI

from api.routes.forecast_inventory import router as forecast_router
from api.routes.health import router as health_router
from api.routes.metrics import router as metrics_router
from api.routes.rank_ads import router as rank_router

app = FastAPI(title="Ad Ranking Forecasting Platform")
app.include_router(health_router)
app.include_router(rank_router)
app.include_router(forecast_router)
app.include_router(metrics_router)
