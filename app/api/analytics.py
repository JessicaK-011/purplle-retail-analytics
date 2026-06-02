from fastapi import APIRouter
from app.services.analytics_service import get_summary
from app.services.funnel_service import get_funnel
from app.services.heatmap_service import get_heatmap
from app.services.anomaly_service import get_anomalies

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)

@router.get("/summary")
def summary():
    return get_summary()


@router.get("/{store_id}/funnel")
def funnel(store_id: str):
    return get_funnel(store_id)

@router.get("/{store_id}/heatmap")
def heatmap(store_id: str):
    return get_heatmap(store_id)

@router.get("/{store_id}/anomalies")
def anomalies(store_id: str):
    return get_anomalies(store_id)