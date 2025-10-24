"""
Enunciado:
Introducción básica a la biblioteca requests de Python.
La biblioteca requests permite realizar peticiones HTTP de forma sencilla.

En este ejercicio, aprenderás a:
1. Realizar una petición GET a una API pública
2. Interpretar una respuesta en formato texto plano
3. Manejar errores en peticiones HTTP

Tu tarea es completar la función indicada para realizar una consulta básica
a la API de ipify.org, un servicio estable que proporciona la IP pública.
"""

import requests
from requests.exceptions import RequestException

def get_user_ip():
    """
    Realiza una petición GET a api.ipify.org para obtener la dirección IP pública
    en formato texto plano.

    Returns:
        str: La dirección IP si la petición es exitosa
        None: Si ocurre un error en la petición
    """
    # Completa esta función para:
    # 1. Realizar una petición GET a la URL https://api.ipify.org (sin parámetros)
    # 2. Verificar si la petición fue exitosa (código 200)
    # 3. Devolver el texto de la respuesta directamente (contiene la IP)
    # 4. Devolver None si hay algún error
    url = 'https://api.ipify.org'

    try:
        print(f"Realizando petición a: {url}")
        response = requests.get(url)
        response.raise_for_status()  # Lanza HTTPError para códigos 4xx/5xx
    except Exception as e:
        print(f"Error en la petición HTTP: {e}")
        return None
    
    # Asegurar que solo devolvemos la IP si la respuesta fue 200
    if response.status_code != 200:
        return None

    return (getattr(response, "text", "") or "").strip()

if __name__ == "__main__":
    # Ejemplo de uso de la función
    ip = get_user_ip()
    if ip:
        print(f"Tu dirección IP pública es: {ip}")
    else:
        print("No se pudo obtener la dirección IP")
