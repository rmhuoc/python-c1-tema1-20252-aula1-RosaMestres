import pytest
import threading
import requests
import json
import time
from ej1b3 import create_server

@pytest.fixture
def server():
    """
    Fixture para iniciar y detener el servidor HTTP durante las pruebas
    """
    # Crear el servidor en un puerto específico para pruebas
    server = create_server(host="localhost", port=8888)

    # Iniciar el servidor en un hilo separado
    thread = threading.Thread(target=server.serve_forever)
    thread.daemon = True
    thread.start()

    # Esperar un momento para que el servidor se inicie
    time.sleep(0.5)

    yield server

    # Detener el servidor después de las pruebas
    server.shutdown()
    server.server_close()
    thread.join(1)

def test_time_endpoint(server):
    """
    Prueba el endpoint /time para validar que devuelve la hora del sistema en formato JSON.
    """
    response = requests.get("http://localhost:8888/time")
    assert response.status_code == 200, "El código de estado debe ser 200."
    assert response.headers['Content-Type'] == 'application/json', "El tipo de contenido debe ser application/json."

    # Convertir la respuesta a JSON
    data = json.loads(response.text)

    # Verificar que la respuesta contiene los campos esperados
    assert 'timestamp' in data, "La respuesta debe contener el campo 'timestamp'."
    assert 'iso_format' in data, "La respuesta debe contener el campo 'iso_format'."
    assert 'readable' in data, "La respuesta debe contener el campo 'readable'."

    # Verificar que los tipos de datos son los correctos
    assert isinstance(data['timestamp'], (int, float)), "El timestamp debe ser un número."
    assert isinstance(data['iso_format'], str), "El formato ISO debe ser una cadena de texto."
    assert isinstance(data['readable'], str), "El formato legible debe ser una cadena de texto."

def test_custom_404_error(server):
    """
    Prueba que al acceder a una ruta no definida, se devuelve un error 404 personalizado en JSON.
    """
    # Usamos una ruta específica para poder verificar que se incluye en el mensaje de error
    test_path = "/ruta_no_existente"
    response = requests.get(f"http://localhost:8888{test_path}")

    assert response.status_code == 404, "El código de estado debe ser 404 para rutas inexistentes."
    assert response.headers['Content-Type'] == 'application/json', "El tipo de contenido del error debe ser application/json."

    # Convertir la respuesta a JSON
    data = json.loads(response.text)

    # Verificar que la respuesta de error tiene la estructura esperada con campos en el nivel superior
    # Permitimos algunas variaciones en los nombres de los campos

    # Verificar el código de error
    assert 'code' in data or 'status' in data, "La respuesta debe incluir un campo de código de error ('code' o 'status')."

    # Verificar el mensaje de error
    message_field_options = ['message', 'descripcion', 'detail']
    message_field = next((field for field in message_field_options if field in data), None)
    assert message_field is not None, f"La respuesta debe incluir un campo de mensaje de error ({', '.join(message_field_options)})."

    # Verificar que los valores son del tipo correcto
    code_field = 'code' if 'code' in data else 'status'
    assert isinstance(data[code_field], int), f"El campo '{code_field}' debe ser un número entero."
    assert isinstance(data[message_field], str), f"El campo '{message_field}' debe ser una cadena de texto."

    # Verificar que el mensaje de error incluye la ruta solicitada
    assert test_path in data[message_field], f"El mensaje de error debe incluir la ruta solicitada '{test_path}'."
