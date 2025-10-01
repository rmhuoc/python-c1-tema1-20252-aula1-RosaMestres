import pytest
from flask.testing import FlaskClient
from ej1a2 import create_app

@pytest.fixture
def client() -> FlaskClient:
    app = create_app()
    app.testing = True
    with app.test_client() as client:
        yield client

def test_hello_endpoint(client):
    """
    Prueba el endpoint /hello para validar que devuelve el mensaje correcto.
    """
    response = client.get("/hello")
    assert response.status_code == 200, "El código de estado debe ser 200."
    assert response.data.decode("utf-8") == "¡Hola mundo!", "El mensaje debe ser '¡Hola mundo!' en texto plano."

def test_goodbye_endpoint(client):
    """
    Prueba el endpoint /goodbye para validar que devuelve el mensaje correcto.
    """
    response = client.get("/goodbye")
    assert response.status_code == 200, "El código de estado debe ser 200."
    assert response.data.decode("utf-8") == "¡Adiós mundo!", "El mensaje debe ser '¡Adiós mundo!' en texto plano."

def test_greet_endpoint(client):
    """
    Prueba el endpoint /greet/<nombre> para validar que devuelve el mensaje personalizado correcto.
    """
    nombre = "Juan"
    response = client.get(f"/greet/{nombre}")
    assert response.status_code == 200, "El código de estado debe ser 200."
    assert response.data.decode("utf-8") == f"¡Hola, {nombre}!", "El mensaje debe ser personalizado con el nombre proporcionado."


