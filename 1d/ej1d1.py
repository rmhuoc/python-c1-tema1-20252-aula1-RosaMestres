"""
Enunciado:
Este ejercicio introduce el uso de bibliotecas especializadas para acceder a APIs de forma
sencilla y estructurada. En concreto, utilizaremos la biblioteca pybikes que proporciona
wrappers para múltiples sistemas de bicicletas compartidas en todo el mundo.

En lugar de construir nuestro propio cliente HTTP y procesar manualmente los datos JSON,
aprenderemos a utilizar herramientas existentes que hacen este trabajo por nosotros.

Tareas:
1. Explorar los sistemas de bicicletas disponibles
2. Obtener información sobre el sistema de Barcelona (Bicing)
3. Analizar los datos de las estaciones

Esta práctica ilustra cómo las bibliotecas especializadas simplifican el acceso a APIs
y permiten concentrarse en el análisis de datos en lugar de en los detalles técnicos
de la comunicación con la API.
"""

import pybikes
import pandas as pd
import time
from typing import List, Dict, Any, Optional
import matplotlib.pyplot as plt
import sys
import os
import json



def _cargar_instancias() -> List[Dict[str, Any]]:
    """
    Lee todos los ficheros JSON de pybikes/data y devuelve
    una lista de instancias con tag y meta.
    """
    instancias: List[Dict[str, Any]] = []

    base_dir = os.path.dirname(pybikes.__file__)
    data_dir = os.path.join(base_dir, "data")

    if not os.path.exists(data_dir):
        return instancias

    for filename in os.listdir(data_dir):
        if not filename.endswith(".json"):
            continue

        path = os.path.join(data_dir, filename)
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception:
            continue

        for inst in data.get("instances", []):
            tag = inst.get("tag")
            meta = inst.get("meta", {})
            if tag:
                instancias.append({"tag": tag, "meta": meta})

    return instancias






def listar_sistemas_disponibles() -> List[str]:
    """
    Obtiene una lista de todos los sistemas de bicicletas disponibles en pybikes.

    Returns:
        List[str]: Lista de identificadores de sistemas disponibles
    """
    # Implementa aquí la lógica para obtener y devolver la lista
    # de sistemas disponibles en pybikes
    instancias = _cargar_instancias()
    # nos quedamos solo con los tags
    tags = sorted({inst["tag"] for inst in instancias})
    return tags


def buscar_sistema_por_ciudad(ciudad: str) -> List[str]:
    """
    Busca sistemas de bicicletas que contengan el nombre de la ciudad especificada.

    Args:
        ciudad (str): Nombre de la ciudad a buscar

    Returns:
        List[str]: Lista de sistemas que coinciden con la búsqueda
    """
    # Implementa aquí la lógica para buscar y devolver sistemas
    # que coincidan con la ciudad especificada
    ciudad = ciudad.lower()
    instancias = _cargar_instancias()
    encontrados: List[str] = []

    for inst in instancias:
        meta = inst.get("meta", {}) or {}
        city = str(meta.get("city", "")).lower()
        name = str(meta.get("name", "")).lower()

        if ciudad in city or ciudad in name:
            encontrados.append(inst["tag"])

    # quitar duplicados manteniendo orden
    vistos = set()
    resultado = []
    for tag in encontrados:
        if tag not in vistos:
            vistos.add(tag)
            resultado.append(tag)

    return resultado


def obtener_info_sistema(tag: str) -> Dict[str, Any]:
    """
    Obtiene la información del sistema especificado.

    Args:
        tag (str): Identificador del sistema (por ejemplo, 'bicing')

    Returns:
        Dict[str, Any]: Metadatos del sistema o None si no existe
    """
    # Implementa aquí la lógica para obtener y devolver
    # los metadatos del sistema especificado
    try:
        system = pybikes.get(tag)
    except Exception as e:
        print(f"No se ha podido obtener el sistema '{tag}': {e}", file=sys.stderr)
        return None

    # meta es un diccionario con name, city, country, etc.
    return getattr(system, "meta", {}) or {}



def obtener_estaciones(tag: str) -> Optional[List]:
    """
    Obtiene la lista de estaciones del sistema especificado.

    Args:
        tag (str): Identificador del sistema (por ejemplo, 'bicing')

    Returns:
        Optional[List]: Lista de objetos estación o None si hay error
    """
    # Implementa aquí la lógica para obtener y devolver
    # la lista de estaciones del sistema especificado
    try:
        system = pybikes.get(tag)
    except Exception as e:
        print(f"No se ha podido obtener el sistema '{tag}': {e}", file=sys.stderr)
        return None

    try:
        system.update()  # hace la llamada HTTP y rellena .stations
        estaciones = getattr(system, "stations", None)
        return estaciones
    except Exception as e:
        print(f"Error al actualizar el sistema '{tag}': {e}", file=sys.stderr)
        return None


def crear_dataframe_estaciones(estaciones: List) -> pd.DataFrame:
    """
    Convierte la lista de estaciones en un DataFrame de pandas.

    Args:
        estaciones (List): Lista de objetos estación

    Returns:
        pd.DataFrame: DataFrame con la información de las estaciones
    """
    # Implementa aquí la lógica para convertir la lista de estaciones
    # en un DataFrame de pandas con al menos las columnas:
    # nombre, latitud, longitud, bicicletas disponibles, espacios libres
    filas = []
    for st in estaciones:
        filas.append({
            "name": getattr(st, "name", None),
            "latitude": getattr(st, "latitude", None),
            "longitude": getattr(st, "longitude", None),
            "bikes": getattr(st, "bikes", None),
            "free": getattr(st, "free", None),
        })

    df = pd.DataFrame(filas)
    return df

def visualizar_estaciones(df: pd.DataFrame) -> None:
    """
    Genera una visualización simple de la disponibilidad de bicicletas.

    Args:
        df (pd.DataFrame): DataFrame con la información de las estaciones
    """
    # Implementa aquí la lógica para crear un gráfico de barras que muestre
    # las 10 estaciones con más bicicletas disponibles
    if "bikes" not in df.columns or "name" not in df.columns:
        print("El DataFrame no tiene las columnas necesarias ('name', 'bikes').")
        return

    top = df.sort_values("bikes", ascending=False).head(10)

    plt.figure()
    top.plot(kind="bar", x="name", y="bikes", legend=False)
    plt.title("Top 10 estaciones con más bicicletas disponibles")
    plt.ylabel("Bicicletas disponibles")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    # Guarda a archivo
    plt.savefig("top10_bicing.png")
    # Y luego intenta mostrarlo
    plt.show()


if __name__ == "__main__":
    # Listar sistemas disponibles
    print("\nSistemas de bicicletas disponibles:")
    sistemas = listar_sistemas_disponibles()
    print(f"Total: {len(sistemas)} sistemas")
    print(f"Algunos ejemplos: {sistemas[:5]}")

    # Buscar sistemas en Barcelona
    print("\nBuscando sistemas en Barcelona:")
    sistemas_barcelona = buscar_sistema_por_ciudad("Barcelona")
    print(f"Encontrados: {len(sistemas_barcelona)}")
    for sistema in sistemas_barcelona:
        print(f"- {sistema}")

    # Si se encuentra el sistema de Barcelona (Bicing), obtener información
    if "bicing" in sistemas:
        print("\nInformación del sistema Bicing de Barcelona:")
        info = obtener_info_sistema("bicing")
        for key, value in info.items():
            print(f"{key}: {value}")

        # Obtener estaciones
        print("\nObteniendo estaciones...")
        estaciones = obtener_estaciones("bicing")
        if estaciones:
            print(f"Obtenidas {len(estaciones)} estaciones")

            # Convertir a DataFrame
            print("\nConvirtiendo a DataFrame...")
            df = crear_dataframe_estaciones(estaciones)
            print(df.head())

            # Estadísticas básicas
            print("\nEstadísticas de bicicletas disponibles:")
            print(df['bikes'].describe())

            # Visualización
            print("\nVisualizando estaciones con más bicicletas disponibles...")
            visualizar_estaciones(df)
        else:
            print("No se pudieron obtener las estaciones.")
    else:
        print("El sistema 'bicing' no está disponible en pybikes.")

