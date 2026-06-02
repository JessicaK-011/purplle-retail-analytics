from app.database.database import get_connection


def get_anomalies(store_id):

    conn = get_connection()

    rows = conn.execute("""
        SELECT visitor_id,
               SUM(dwell_ms) as total_dwell
        FROM events
        WHERE store_id = ?
        GROUP BY visitor_id
        HAVING total_dwell > 300000
    """, (store_id,)).fetchall()

    conn.close()

    return [
        {
            "visitor_id": row[0],
            "total_dwell_ms": row[1]
        }
        for row in rows
    ]