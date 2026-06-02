from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_sales_summary():

    response = client.get(
        "/analytics/sales-summary"
    )

    assert response.status_code == 200

    data = response.json()

    assert "total_transactions" in data

    assert "total_revenue" in data


def test_top_brands():

    response = client.get(
        "/analytics/top-brands"
    )

    assert response.status_code == 200