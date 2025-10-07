"""
Tests para el ejercicio ej1b1.py
Este archivo contiene pruebas para verificar la correcta implementación
de la función get_nonexistent_resource manejando errores HTTP.
"""

import pytest
import requests
import responses
from unittest.mock import patch, Mock

from ej1b1 import get_nonexistent_resource

@pytest.fixture
def mock_responses():
    """
    Fixture para configurar respuestas simuladas para las peticiones HTTP
    """
    with responses.RequestsMock() as rsps:
        # Configurar respuesta para la petición a un recurso inexistente (404)
        rsps.add(
            responses.GET,
            "https://api.ipify.org/ip",
            body="Not Found",
            status=404
        )
        yield rsps

def test_get_nonexistent_resource(mock_responses):
    """
    Prueba la función get_nonexistent_resource cuando se produce un error 404.
    """
    result = get_nonexistent_resource()

    # Verificar que la función devuelve un diccionario
    assert isinstance(result, dict), "La función debe devolver un diccionario"

    # Verificar que el diccionario contiene las claves requeridas
    assert 'status_code' in result, "El diccionario debe contener la clave 'status_code'"
    assert 'requested_url' in result, "El diccionario debe contener la clave 'requested_url'"
    assert 'error_message' in result, "El diccionario debe contener la clave 'error_message'"

    # Verificar que los valores son correctos
    assert result['status_code'] == 404, "El código de estado debe ser 404"
    assert result['requested_url'] == "https://api.ipify.org/ip", "La URL debe ser la solicitada"

def test_get_nonexistent_resource_failure():
    """
    Prueba la función get_nonexistent_resource cuando la petición falla por un error de conexión.
    """
    with patch('requests.get') as mock_get:
        # Configurar el mock para simular un error de conexión
        mock_get.side_effect = Exception("Connection error")
        result = get_nonexistent_resource()

        # Verificar que la función maneja el error y devuelve la información apropiada
        assert isinstance(result, dict), "La función debe devolver un diccionario incluso en caso de error"
        assert 'status_code' in result, "El diccionario debe contener la clave 'status_code'"
        assert 'requested_url' in result, "El diccionario debe contener la clave 'requested_url'"
        assert 'error_message' in result, "El diccionario debe contener la clave 'error_message'"
        assert result['status_code'] is None or isinstance(result['status_code'], int), "El código de estado debe ser None o un número"
        assert result['requested_url'] == "https://api.ipify.org/ip", "La URL debe ser la solicitada"

@patch('requests.get')
def test_get_nonexistent_resource_specific_error(mock_get):
    """
    Prueba la función get_nonexistent_resource cuando la petición devuelve específicamente un código 404.
    """
    # Configurar la respuesta del mock con un código de error 404
    mock_response = Mock()
    mock_response.status_code = 404
    mock_response.raise_for_status.side_effect = requests.HTTPError("404 Client Error: Not Found for url: https://api.ipify.org/ip")
    mock_response.url = "https://api.ipify.org/ip"
    mock_get.return_value = mock_response

    result = get_nonexistent_resource()

    # Verificar que la función procesa correctamente el error HTTP
    assert isinstance(result, dict), "La función debe devolver un diccionario"
    assert result['status_code'] == 404, "El código de estado debe ser 404"
    assert result['requested_url'] == "https://api.ipify.org/ip", "La URL debe ser la solicitada"
    assert 'error_message' in result, "El diccionario debe contener la clave 'error_message'"
