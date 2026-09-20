from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_get_all_tasks():
    response = client.get("/tasks")

    assert response.status_code == 200
    assert len(response.json()) == 3


def test_get_task():
    response = client.get("/tasks/1")

    assert response.status_code == 200
    assert response.json()["title"] == "Learn Python"


def test_get_nonexistent_task():
    response = client.get("/tasks/999")

    assert response.status_code == 404
    assert response.json() == {"detail": "Task not found"}


def test_create_task():
    response = client.post(
        "/tasks",
        json={
            "title": "Learn GitHub Actions",
            "completed": False,
        },
    )

    assert response.status_code == 200
    assert response.json()["title"] == "Learn GitHub Actions"
    assert response.json()["completed"] is False