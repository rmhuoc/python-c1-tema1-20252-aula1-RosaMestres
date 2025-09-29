import pytest
from flask import Flask
from flask.testing import FlaskClient
from ej1b2 import create_app

@pytest.fixture
def client() -> FlaskClient:
    app = create_app()
    app.testing = True
    with app.test_client() as client:
        yield client

def test_get_tasks_empty(client):
    response = client.get("/tasks")
    assert response.status_code == 200
    assert response.json == []

def test_add_task(client):
    response = client.post("/tasks", json={"name": "Comprar leche"})
    assert response.status_code == 201
    assert response.json == {"id": 1, "name": "Comprar leche"}

    response = client.get("/tasks")
    assert response.status_code == 200
    assert response.json == [{"id": 1, "name": "Comprar leche"}]

def test_delete_task(client):
    client.post("/tasks", json={"name": "Comprar leche"})
    response = client.delete("/tasks/1")
    assert response.status_code == 200
    assert response.json == {"message": "Task deleted"}

    response = client.get("/tasks")
    assert response.status_code == 200
    assert response.json == []

def test_delete_nonexistent_task(client):
    response = client.delete("/tasks/999")
    assert response.status_code == 404
    assert response.json == {"error": "Task not found"}