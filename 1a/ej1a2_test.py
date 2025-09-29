import pytest
from flask.testing import FlaskClient
from ej1a2 import create_app

@pytest.fixture
def client() -> FlaskClient:
    app = create_app()
    app.testing = True
    with app.test_client() as client:
        yield client

def test_greet_with_url_param(client):
    response = client.post("/greet?name=Juan")
    assert response.status_code == 200
    assert response.json == {"message": "¡Hola, Juan!"}

def test_greet_with_json_payload(client):
    response = client.post("/greet-json", json={"name": "Maria"})
    assert response.status_code == 200
    assert response.json == {"message": "¡Hola, Maria!"}
