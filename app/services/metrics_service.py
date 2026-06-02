from app.database.database import get_connection


def get_store_metrics(store_id):

    conn = get_connection()

    total_events = conn.execute(
        """
        SELECT COUNT(*)
        FROM events
        WHERE store_id = ?
        """,
        (store_id,)
    ).fetchone()[0]

    unique_visitors = conn.execute(
        """
        SELECT COUNT(DISTINCT visitor_id)
        FROM events
        WHERE store_id = ?
        """,
        (store_id,)
    ).fetchone()[0]

    avg_confidence = conn.execute(
        """
        SELECT AVG(confidence)
        FROM events
        WHERE store_id = ?
        """,
        (store_id,)
    ).fetchone()[0]

    conn.close()

    return {
        "store_id": store_id,
        "total_events": total_events,
        "unique_visitors": unique_visitors,
        "average_confidence": round(avg_confidence or 0, 2)
    }