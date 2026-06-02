from app.database.database import get_connection


def init_db():
    conn = get_connection()

    conn.execute("""
    CREATE TABLE IF NOT EXISTS events(
        event_id TEXT PRIMARY KEY,
        store_id TEXT,
        camera_id TEXT,
        visitor_id TEXT,
        event_type TEXT,
        timestamp TEXT,
        zone_id TEXT,
        dwell_ms INTEGER,
        is_staff INTEGER,
        confidence REAL,
        metadata TEXT
    )
    """)

    conn.commit()
    conn.close()