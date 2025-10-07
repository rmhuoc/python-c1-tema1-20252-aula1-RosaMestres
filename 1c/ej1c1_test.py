"""
Tests para el ejercicio ej1c1.py
Este archivo contiene pruebas para verificar la correcta implementación
de las funciones para consultar la API GBFS del sistema de bicicletas compartidas de Barcelona.
"""

import pytest
import requests
import json
import io
import sys
from unittest.mock import patch, MagicMock

from ej1c1 import get_gbfs_feeds, extract_feeds_info, print_feeds_summary

@pytest.fixture
def sample_gbfs_response():
    """
    Fixture para proporcionar una respuesta de ejemplo de la API GBFS
    """
    return {
        "last_updated": 1759834448,
        "ttl": 0,
        "data": {
            "en": {
                "feeds": [
                    {"name": "geofencing_zones", "url": "https://barcelona.publicbikesystem.net/customer/gbfs/v2/en/geofencing_zones"},
                    {"name": "gbfs_versions", "url": "https://barcelona.publicbikesystem.net/customer/gbfs/v2/gbfs_versions"},
                    {"name": "vehicle_types", "url": "https://barcelona.publicbikesystem.net/customer/gbfs/v2/en/vehicle_types"},
                    {"name": "station_information", "url": "https://barcelona.publicbikesystem.net/customer/gbfs/v2/en/station_information"},
                    {"name": "station_status", "url": "https://barcelona.publicbikesystem.net/customer/gbfs/v2/en/station_status"},
                    {"name": "system_regions", "url": "https://barcelona.publicbikesystem.net/customer/gbfs/v2/en/system_regions"},
                    {"name": "system_information", "url": "https://barcelona.publicbikesystem.net/customer/gbfs/v2/en/system_information"},
                    {"name": "system_pricing_plans", "url": "https://barcelona.publicbikesystem.net/customer/gbfs/v2/en/system_pricing_plans"}
                ]
            }
        },
        "version": "2.3"
    }

@patch('ej1c1.requests.get')
def test_get_gbfs_feeds_success(mock_get, sample_gbfs_response):
    """
    Prueba la función get_gbfs_feeds cuando la petición es exitosa
    """
    # Configurar el mock para retornar una respuesta exitosa
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = sample_gbfs_response
    mock_get.return_value = mock_response

    # Ejecutar la función
    result = get_gbfs_feeds()

    # Verificar que se llamó a requests.get con la URL correcta
    mock_get.assert_called_once_with("https://barcelona-sp.publicbikesystem.net/customer/gbfs/v2/gbfs.json")

    # Verificar que el resultado es el esperado
    assert result == sample_gbfs_response, "La función debe devolver los datos JSON de la respuesta"

@patch('ej1c1.requests.get')
def test_get_gbfs_feeds_error_status(mock_get):
    """
    Prueba la función get_gbfs_feeds cuando la petición devuelve un código de error
    """
    # Configurar el mock para retornar un código de error
    mock_response = MagicMock()
    mock_response.status_code = 404
    mock_get.return_value = mock_response

    # Ejecutar la función
    result = get_gbfs_feeds()

    # Verificar que el resultado es None cuando hay un error
    assert result is None, "La función debe devolver None cuando hay un error de estado HTTP"

@patch('ej1c1.requests.get')
def test_get_gbfs_feeds_connection_error(mock_get):
    """
    Prueba la función get_gbfs_feeds cuando ocurre un error de conexión
    """
    # Configurar el mock para simular un error de conexión
    mock_get.side_effect = requests.exceptions.ConnectionError("Connection refused")

    # Ejecutar la función
    result = get_gbfs_feeds()

    # Verificar que el resultado es None cuando hay un error de conexión
    assert result is None, "La función debe devolver None cuando hay un error de conexión"

def test_extract_feeds_info_success(sample_gbfs_response):
    """
    Prueba la función extract_feeds_info cuando se proporciona una respuesta válida
    """
    # Ejecutar la función
    result = extract_feeds_info(sample_gbfs_response)

    # Verificar que el resultado es una lista
    assert isinstance(result, list), "La función debe devolver una lista"

    # Verificar que la lista contiene 8 elementos (feeds)
    assert len(result) == 8, "La función debe extraer todos los feeds disponibles"

    # Verificar la estructura de los elementos
    for feed in result:
        assert "name" in feed, "Cada feed debe contener el campo 'name'"
        assert "url" in feed, "Cada feed debe contener el campo 'url'"

    # Verificar el contenido del primer feed
    assert result[0]["name"] == "geofencing_zones", "El nombre del primer feed debe ser correcto"
    assert result[0]["url"] == "https://barcelona.publicbikesystem.net/customer/gbfs/v2/en/geofencing_zones", "La URL del primer feed debe ser correcta"

def test_extract_feeds_info_none_input():
    """
    Prueba la función extract_feeds_info cuando se proporciona None como entrada
    """
    # Ejecutar la función con None como entrada
    result = extract_feeds_info(None)

    # Verificar que el resultado es None
    assert result is None, "La función debe devolver None cuando la entrada es None"

def test_extract_feeds_info_invalid_format():
    """
    Prueba la función extract_feeds_info cuando el formato de los datos es inválido
    """
    # Datos con formato inválido (sin campo 'data')
    invalid_data = {"last_updated": 1759834448, "ttl": 0, "version": "2.3"}

    # Ejecutar la función
    result = extract_feeds_info(invalid_data)

    # Verificar que el resultado es None
    assert result is None, "La función debe devolver None cuando el formato de datos es inválido"

def test_print_feeds_summary(sample_gbfs_response, capsys):
    """
    Prueba la función print_feeds_summary cuando se proporcionan feeds válidos
    """
    # Extraer los feeds de ejemplo
    feeds_info = extract_feeds_info(sample_gbfs_response)

    # Ejecutar la función
    print_feeds_summary(feeds_info)

    # Capturar la salida estándar
    captured = capsys.readouterr()

    # Verificar que la salida contiene la información esperada
    assert "Barcelona Bike-Sharing System" in captured.out, "La salida debe contener el título del sistema"
    assert f"Available Feeds: {len(feeds_info)}" in captured.out, "La salida debe indicar el número de feeds disponibles"
    assert "geofencing_zones" in captured.out, "La salida debe contener el nombre del primer feed"
    assert "https://barcelona.publicbikesystem.net/customer/gbfs/v2/en/geofencing_zones" in captured.out, "La salida debe contener la URL del primer feed"

def test_print_feeds_summary_none(capsys):
    """
    Prueba la función print_feeds_summary cuando se proporciona None como entrada
    """
    # Ejecutar la función con None
    print_feeds_summary(None)

    # Capturar la salida estándar
    captured = capsys.readouterr()

    # Verificar que la salida contiene un mensaje de error
    assert "Error" in captured.out, "La salida debe contener un mensaje de error"
