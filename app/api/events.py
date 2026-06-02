from fastapi import APIRouter

from app.models.event import Event
from app.services.event_service import save_event

router = APIRouter()


@router.post("/events/ingest")
def ingest_event(event: Event):

    save_event(event)

    return {
        "status": "success"
    }