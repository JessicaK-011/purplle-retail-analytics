from app.database.database import get_connection


def get_summary():

    conn = get_connection()

    total_events = conn.execute(
        "SELECT COUNT(*) FROM events"
    ).fetchone()[0]

    unique_visitors = conn.execute(
        "SELECT COUNT(DISTINCT visitor_id) FROM events"
    ).fetchone()[0]

    entries = conn.execute(
        """
        SELECT COUNT(*)
        FROM events
        WHERE event_type='entered_store'
        """
    ).fetchone()[0]

    exits = conn.execute(
        """
        SELECT COUNT(*)
        FROM events
        WHERE event_type='exited_store'
        """
    ).fetchone()[0]

    staff_count = conn.execute(
        """
        SELECT COUNT(DISTINCT visitor_id)
        FROM events
        WHERE is_staff=1
        """
    ).fetchone()[0]

    conn.close()

    return {
        "total_events": total_events,
        "unique_visitors": unique_visitors,
        "entries": entries,
        "exits": exits,
        "staff_count": staff_count
    }