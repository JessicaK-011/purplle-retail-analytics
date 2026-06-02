from fastapi import FastAPI

from app.database.init_db import init_db
from app.api.events import router as event_router
from app.api.analytics import router as analytics_router
from app.api.metrics import router as metrics_router

app = FastAPI()

app.include_router(event_router)
app.include_router(analytics_router)
app.include_router(metrics_router)

@app.on_event("startup")
def startup():
    init_db()

@app.get("/")
def home():
    return {"message": "Retail Analytics System"}

@app.get("/health")
def health():
    return {"status": "healthy"}