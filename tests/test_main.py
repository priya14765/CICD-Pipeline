from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root_serves_homepage() -> None:
    response = client.get("/")

    assert response.status_code == 200
    assert response.headers["content-type"].startswith("text/html")
    assert "Your service is" in response.text


def test_api_returns_service_message() -> None:
    response = client.get("/api")

    assert response.status_code == 200
    assert response.json() == {"message": "CodeNova service is running"}


def test_health_check_returns_ok() -> None:
    response = client.get("/healthz")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
