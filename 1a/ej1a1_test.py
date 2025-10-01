import pytest
from flask.testing import FlaskClient
from ej1a1 import create_app

@pytest.fixture
def client() -> FlaskClient:
    app = create_app()
    app.testing = True
    with app.test_client() as client:
        yield client

def test_root_endpoint(client):
    """
    Prueba el endpoint / para validar que devuelve el mensaje correcto.
    Si deseas cambiar el idioma del ejercicio, edita este archivo.
    """
    response = client.get("/")
    assert response.status_code == 200, "El código de estado debe ser 200."
    assert response.data.decode("utf-8") == "¡Hola mundo!", "El mensaje debe ser '¡Hola mundo!' en texto plano."
