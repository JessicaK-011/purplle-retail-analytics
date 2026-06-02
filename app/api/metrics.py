from fastapi import APIRouter
from app.services.metrics_service import get_store_metrics

router = APIRouter(
    prefix="/stores",
    tags=["Metrics"]
)

@router.get("/{store_id}/metrics")
def metrics(store_id: str):
    return get_store_metrics(store_id)