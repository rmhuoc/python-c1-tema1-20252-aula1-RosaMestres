"""
Tests para el ejercicio ej1d1.py
Este archivo contiene pruebas para verificar la correcta implementación
de las funciones que utilizan la biblioteca pybikes para acceder a 
información de sistemas de bicicletas compartidas.

Nota: Estas pruebas requieren conexión a internet para acceder a la API.
"""

import pytest
import pandas as pd
import matplotlib.pyplot as plt
from unittest.mock import patch, MagicMock

# Importar el módulo a probar
import sys
import os

from ej1d1 import (
    listar_sistemas_disponibles, 
    buscar_sistema_por_ciudad, 
    obtener_info_sistema,
    obtener_estaciones,
    crear_dataframe_estaciones,
    visualizar_estaciones
)

# Fixture para simular una estación
@pytest.fixture
def mock_stations():
    """Proporciona una lista de estaciones simuladas para pruebas."""
    stations = []
    # Crear 5 estaciones simuladas
    for i in range(1, 6):
        station = MagicMock()
        station.name = f"Station {i}"
        station.latitude = 41.3 + (i / 100)
        station.longitude = 2.1 + (i / 100)
        station.bikes = i * 5  # 5, 10, 15, 20, 25
        station.free = 30 - (i * 5)  # 25, 20, 15, 10, 5
        stations.append(station)
    return stations

def test_listar_sistemas_disponibles():
    """
    Prueba la función listar_sistemas_disponibles.
    Debe devolver una lista no vacía de sistemas.
    """
    sistemas = listar_sistemas_disponibles()
    assert isinstance(sistemas, list), "La función debe devolver una lista"
    assert len(sistemas) > 0, "La lista de sistemas no debe estar vacía"
    assert all(isinstance(s, str) for s in sistemas), "Todos los elementos deben ser strings"

def test_buscar_sistema_por_ciudad():
    """
    Prueba la función buscar_sistema_por_ciudad.
    Debe encontrar al menos un sistema para Barcelona.
    """
    sistemas = buscar_sistema_por_ciudad("Barcelona")
    assert isinstance(sistemas, list), "La función debe devolver una lista"
    assert len(sistemas) > 0, "Debería haber al menos un sistema para Barcelona"
    assert "bicing" in sistemas, "El sistema 'bicing' debe estar entre los resultados"

def test_obtener_info_sistema():
    """
    Prueba la función obtener_info_sistema.
    Debe devolver un diccionario con metadatos del sistema.
    """
    info = obtener_info_sistema("bicing")
    assert isinstance(info, dict), "La función debe devolver un diccionario"
    assert "name" in info, "Los metadatos deben incluir el nombre del sistema"
    assert "city" in info, "Los metadatos deben incluir la ciudad del sistema"
    assert "country" in info, "Los metadatos deben incluir el país del sistema"

@patch('pybikes.get')
def test_obtener_estaciones_error(mock_get):
    """
    Prueba la función obtener_estaciones cuando hay un error.
    """
    # Configurar el mock para lanzar una excepción
    mock_get.side_effect = Exception("Error de prueba")
    
    # La función debe manejar el error y devolver None
    estaciones = obtener_estaciones("sistema_inexistente")
    assert estaciones is None, "Debe devolver None cuando hay un error"

def test_crear_dataframe_estaciones(mock_stations):
    """
    Prueba la función crear_dataframe_estaciones.
    """
    df = crear_dataframe_estaciones(mock_stations)
    
    # Verificar que es un DataFrame
    assert isinstance(df, pd.DataFrame), "Debe devolver un DataFrame"
    
    # Verificar que tiene las columnas esperadas
    expected_columns = ['name', 'latitude', 'longitude', 'bikes', 'free']
    for col in expected_columns:
        assert col in df.columns, f"El DataFrame debe tener la columna '{col}'"
    
    # Verificar el número de filas
    assert len(df) == 5, "El DataFrame debe tener 5 filas"
    
    # Verificar el contenido
    assert df.iloc[0]['name'] == "Station 1", "El nombre de la primera estación debe ser 'Station 1'"
    assert df.iloc[0]['bikes'] == 5, "La primera estación debe tener 5 bicicletas"

@patch('matplotlib.pyplot.show')
@patch('matplotlib.pyplot.savefig')
def test_visualizar_estaciones(mock_savefig, mock_show, mock_stations):
    """
    Prueba la función visualizar_estaciones.
    """
    # Crear un DataFrame para la prueba
    df = pd.DataFrame({
        'name': [station.name for station in mock_stations],
        'bikes': [station.bikes for station in mock_stations],
        'free': [station.free for station in mock_stations],
        'latitude': [station.latitude for station in mock_stations],
        'longitude': [station.longitude for station in mock_stations]
    })
    
    # Llamar a la función
    visualizar_estaciones(df)
    
    # Verificar que se llamó a la función show() para mostrar el gráfico
    # (o alternativamente, que se guardó el gráfico)
    assert mock_show.called or mock_savefig.called, "Debe mostrar o guardar una visualización"

# Pruebas adicionales para verificar comportamiento con valores borde

def test_buscar_sistema_por_ciudad_no_existente():
    """
    Prueba buscar_sistema_por_ciudad con una ciudad que no existe.
    """
    sistemas = buscar_sistema_por_ciudad("CiudadImaginaria123456")
    assert isinstance(sistemas, list), "La función debe devolver una lista"
    assert len(sistemas) == 0, "La lista debe estar vacía para una ciudad inexistente"

def test_obtener_info_sistema_no_existente():
    """
    Prueba obtener_info_sistema con un sistema que no existe.
    """
    info = obtener_info_sistema("sistema_inexistente_123456")
    assert info is None, "Debe devolver None para un sistema inexistente"

def test_crear_dataframe_estaciones_lista_vacia():
    """
    Prueba crear_dataframe_estaciones con una lista vacía.
    """
    df = crear_dataframe_estaciones([])
    assert isinstance(df, pd.DataFrame), "Debe devolver un DataFrame vacío"
    assert len(df) == 0, "El DataFrame debe estar vacío"
