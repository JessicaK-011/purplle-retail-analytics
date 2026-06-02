import json

from app.database.database import get_connection
from app.models.event import Event


def save_event(event: Event):

    conn = get_connection()

    conn.execute(
        """
        INSERT OR IGNORE INTO events
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            event.event_id,
            event.store_id,
            event.camera_id,
            event.visitor_id,
            event.event_type,
            event.timestamp.isoformat(),
            event.zone_id,
            event.dwell_ms,
            int(event.is_staff),
            event.confidence,
            json.dumps(event.metadata)
        )
    )

    conn.commit()
    conn.close()