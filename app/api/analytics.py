from fastapi import APIRouter
from app.services.analytics_service import get_summary
from app.services.funnel_service import get_funnel
from app.services.heatmap_service import get_heatmap
from app.services.anomaly_service import get_anomalies
from app.services.sales_service import get_sales_summary
from app.services.sales_service import get_top_products
from app.services.sales_service import get_top_salespeople
from app.services.sales_service import get_basket_metrics
from app.services.cctv_service import get_cctv_summary
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

@router.get("/sales-summary")
def sales_summary():
    return get_sales_summary()

from app.services.sales_service import (
    get_sales_summary,
    get_top_brands
)

@router.get("/top-brands")
def top_brands():
    return get_top_brands()

@router.get("/top-products")
def top_products():
    return get_top_products()

@router.get("/top-salespeople")
def top_salespeople():
    return get_top_salespeople()

@router.get("/basket-metrics")
def basket_metrics():
    return get_basket_metrics()

@router.get("/cctv-summary")
def cctv_summary():
    return get_cctv_summary()