import pytest
from flask.testing import FlaskClient
from ej1a3 import create_app

@pytest.fixture
def client() -> FlaskClient:
    app = create_app()
    app.testing = True
    with app.test_client() as client:
        yield client

def test_website_endpoint(client):
    """
    Prueba el endpoint /website para validar que devuelve una página web con estructura HTML mínima.
    """
    response = client.get("/website")
    assert response.status_code == 200, "El código de estado debe ser 200."
    html_content = response.data.decode("utf-8")
    assert "<!doctype html>" in html_content.lower(), "La respuesta debe contener la declaración <!doctype html>."
    assert "<html>" in html_content.lower(), "La respuesta debe contener la etiqueta <html>."
    assert "<body>" in html_content.lower(), "La respuesta debe contener la etiqueta <body>."
    assert "¡hola mundo!" in html_content.lower(), "La respuesta debe contener el mensaje '¡Hola mundo!' dentro del cuerpo."

