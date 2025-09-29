import pytest
from flask.testing import FlaskClient
from ej1a4 import create_app
from scipy import misc
import io

@pytest.fixture
def client() -> FlaskClient:
    app = create_app()
    app.testing = True
    with app.test_client() as client:
        yield client

def test_post_text(client):
    response = client.post("/text", data="Este es un texto de prueba", content_type="text/plain")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Este es un texto de prueba"
    assert response.content_type == "text/plain"

def test_post_html(client):
    response = client.post("/html", data="<h1>Prueba HTML</h1>", content_type="text/html")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "<h1>Prueba HTML</h1>"
    assert response.content_type == "text/html"

def test_post_json(client):
    response = client.post("/json", json={"key": "value"})
    assert response.status_code == 200
    assert response.json == {"key": "value"}
    assert response.content_type == "application/json"

def test_post_xml(client):
    xml_data = "<root><key>value</key></root>"
    response = client.post("/xml", data=xml_data, content_type="application/xml")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == xml_data
    assert response.content_type == "application/xml"

def test_post_image(client):
    # Use an example image from scipy.misc
    image = misc.face()
    image_bytes = io.BytesIO()
    misc.imsave(image_bytes, image, format="png")
    image_bytes.seek(0)

    data = {
        "file": (image_bytes, "test_image.png")
    }
    response = client.post("/image", data=data, content_type="multipart/form-data")
    assert response.status_code == 200
    assert response.json["message"] == "Imagen guardada"
    assert response.json["filename"] == "test_image.png"
