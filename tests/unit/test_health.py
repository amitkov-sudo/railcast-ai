from fastapi.testclient import TestClient

from services.api.main import app


def test_api_health() -> None:
    client = TestClient(app)
    response = client.get("/v1/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
