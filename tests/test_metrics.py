from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_metrics():

    response = client.get(
        "/stores/brigade_bangalore/metrics"
    )

    assert response.status_code == 200

    data = response.json()

    assert "store_id" in data

    assert "unique_visitors" in data