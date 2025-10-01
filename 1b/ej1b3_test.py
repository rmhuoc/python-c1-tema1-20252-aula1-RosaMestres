import pytest
from flask import Flask
from flask.testing import FlaskClient
from ej1b3 import create_app

@pytest.fixture
def client() -> FlaskClient:
    app = create_app()
    app.testing = True
    with app.test_client() as client:
        yield client

def test_get_animals(client):
    """Test GET /animals - should return all animals"""
    response = client.get("/animals")
    assert response.status_code == 200
    assert len(response.json) == 3
    assert response.json[0]["name"] == "León"

def test_get_animal_exists(client):
    """Test GET /animals/1 - should return the animal with ID 1"""
    response = client.get("/animals/1")
    assert response.status_code == 200
    assert response.json["name"] == "León"
    assert response.json["species"] == "Panthera leo"

def test_get_animal_not_found(client):
    """Test GET /animals/999 - should return 404 error"""
    response = client.get("/animals/999")
    assert response.status_code == 404
    assert "error" in response.json

def test_add_animal(client):
    """Test POST /animals with valid data - should add a new animal"""
    response = client.post("/animals", json={"name": "Tigre", "species": "Panthera tigris"})
    assert response.status_code == 201
    assert response.json["name"] == "Tigre"
    assert response.json["id"] == 4

def test_add_animal_invalid(client):
    """Test POST /animals with invalid data - should return 400 error"""
    response = client.post("/animals", json={"name": "Tigre"})  # Missing species
    assert response.status_code == 400
    assert "error" in response.json

def test_delete_animal(client):
    """Test DELETE /animals/2 - should delete the animal with ID 2"""
    response = client.delete("/animals/2")
    assert response.status_code == 204

    # Verify animal was deleted
    response = client.get("/animals/2")
    assert response.status_code == 404

def test_delete_animal_not_found(client):
    """Test DELETE /animals/999 - should return 404 error"""
    response = client.delete("/animals/999")
    assert response.status_code == 404
    assert "error" in response.json

def test_method_not_allowed(client):
    """Test PUT /animals - should return 405 error"""
    response = client.put("/animals")
    assert response.status_code == 405
    assert "error" in response.json

def test_internal_server_error(client):
    """Test GET /test-error - should return 500 error"""
    response = client.get("/test-error")
    assert response.status_code == 500
    assert "error" in response.json
