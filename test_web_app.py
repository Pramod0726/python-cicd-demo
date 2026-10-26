
from fastapi.testclient import TestClient

from web_app import api

client = TestClient(api)


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_calculate_divide():
    response = client.post(
        "/calculate",
        json={"a": 10, "b": 2, "operation": "divide"},
    )

    assert response.status_code == 200
    assert response.json() == {"operation": "divide", "result": 5}


def test_divide_by_zero():
    response = client.post(
        "/calculate",
        json={"a": 10, "b": 0, "operation": "divide"},
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Cannot divide by zero"
def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Python CI/CD Demo API is running - CD test successful",
        "docs"   : "/docs",
        "health" : "/health",
    }