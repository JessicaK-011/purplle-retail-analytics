from app.database.database import get_connection


def get_funnel(store_id):

    conn = get_connection()

    entered = conn.execute("""
        SELECT COUNT(DISTINCT visitor_id)
        FROM events
        WHERE store_id=? AND event_type='entered_store'
    """, (store_id,)).fetchone()[0]

    shelf = conn.execute("""
        SELECT COUNT(DISTINCT visitor_id)
        FROM events
        WHERE store_id=? AND event_type='visited_shelf'
    """, (store_id,)).fetchone()[0]

    billing = conn.execute("""
        SELECT COUNT(DISTINCT visitor_id)
        FROM events
        WHERE store_id=? AND event_type='visited_billing'
    """, (store_id,)).fetchone()[0]

    purchased = conn.execute("""
        SELECT COUNT(DISTINCT visitor_id)
        FROM events
        WHERE store_id=? AND event_type='purchased'
    """, (store_id,)).fetchone()[0]

    conn.close()

    return {
        "entered_store": entered,
        "visited_shelf": shelf,
        "visited_billing": billing,
        "purchased": purchased
    }