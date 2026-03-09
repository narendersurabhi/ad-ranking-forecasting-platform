from fastapi import APIRouter, Depends

from api.dependencies import get_metrics

router = APIRouter()


@router.get("/metrics")
def metrics_endpoint(metrics=Depends(get_metrics)):
    return metrics.snapshot()
