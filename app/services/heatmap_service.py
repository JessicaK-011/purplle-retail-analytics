from app.database.database import get_connection


def get_heatmap(store_id):

    conn = get_connection()

    rows = conn.execute("""
        SELECT zone_id, COUNT(*) as visits
        FROM events
        WHERE store_id = ?
        GROUP BY zone_id
    """, (store_id,)).fetchall()

    conn.close()

    return [
        {
            "zone": row[0],
            "visits": row[1]
        }
        for row in rows
    ]