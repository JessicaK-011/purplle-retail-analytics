from app.database.database import get_connection


def get_sales_summary():

    conn = get_connection()

    total_transactions = conn.execute("""
        SELECT COUNT(*)
        FROM sales
    """).fetchone()[0]

    total_revenue = conn.execute("""
        SELECT SUM(total_amount)
        FROM sales
    """).fetchone()[0]

    total_units = conn.execute("""
        SELECT SUM(qty)
        FROM sales
    """).fetchone()[0]

    conn.close()

    return {
        "total_transactions": total_transactions,
        "total_revenue": round(total_revenue or 0, 2),
        "total_units_sold": total_units
    }  


def get_top_brands():

    conn = get_connection()

    rows = conn.execute("""
        SELECT brand_name,
               ROUND(SUM(total_amount),2) as revenue
        FROM sales
        GROUP BY brand_name
        ORDER BY revenue DESC
        LIMIT 10
    """).fetchall()

    conn.close()

    return [
        {
            "brand": row[0],
            "revenue": row[1]
        }
        for row in rows
    ]
    
def get_top_products():

    conn = get_connection()

    rows = conn.execute("""
    SELECT product_name,
           SUM(total_amount) as revenue
    FROM sales
    GROUP BY product_name
    ORDER BY revenue DESC
    LIMIT 10
    """).fetchall()

    conn.close()

    return [
        {
            "product": row[0],
            "revenue": round(row[1], 2)
        }
        for row in rows
    ]
    
    
def get_top_salespeople():

    conn = get_connection()

    rows = conn.execute("""
        SELECT salesperson_name,
            SUM(total_amount) as revenue
        FROM sales
        GROUP BY salesperson_name
        ORDER BY revenue DESC
        LIMIT 10
    """).fetchall()

    conn.close()

    return [
        {
            "salesperson": row[0],
            "revenue": round(row[1], 2)
        }
        for row in rows
    ]
    
def get_basket_metrics():

    conn = get_connection()

    total_revenue = conn.execute("""
        SELECT SUM(total_amount)
        FROM sales
    """).fetchone()[0]

    total_transactions = conn.execute("""
        SELECT COUNT(*)
        FROM sales
    """).fetchone()[0]

    conn.close()

    avg_basket = 0

    if total_transactions:
        avg_basket = total_revenue / total_transactions

    return {
        "average_basket_value": round(avg_basket, 2)
    }