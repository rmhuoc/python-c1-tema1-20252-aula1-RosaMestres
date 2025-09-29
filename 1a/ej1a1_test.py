import pytest
from flask.testing import FlaskClient
from ej1a1 import create_app

@pytest.fixture
def client() -> FlaskClient:
    app = create_app()
    app.testing = True
    with app.test_client() as client:
        yield client

def test_hello_endpoint(client):
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json == {"message": "¡Hola, mundo!"}
