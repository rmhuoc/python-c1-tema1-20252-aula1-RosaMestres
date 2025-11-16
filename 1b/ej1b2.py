"""
Enunciado:
Manejo avanzado de errores HTTP con la biblioteca requests de Python.

En este ejercicio, aprenderás a:
1. Realizar peticiones a diferentes URLs que generarán distintos códigos de estado HTTP
2. Diferenciar entre varios tipos de errores HTTP (4xx, 5xx)
3. Manejar redirecciones (códigos 3xx)
4. Extraer información detallada de las respuestas de error
5. Procesar respuestas JSON con información específica sobre el estado

Tu tarea es completar la función request_with_error_handling para manejar adecuadamente
diferentes tipos de respuestas HTTP, incluyendo errores cliente (4xx), errores servidor (5xx)
y redirecciones (3xx).

Nota: El servidor httpstatuses.maor.io devuelve respuestas JSON con la siguiente estructura:

{
    "code": 404,
    "description": "Not Found"
}

Deberás comprobar que el código en el encabezado HTTP coincide con el campo "code"
en el cuerpo JSON y usar el campo "description" para proporcionar información detallada.
"""

import requests

def request_with_error_handling(url):
    """
    Realiza una petición GET a la URL proporcionada y maneja los diferentes tipos de
    respuestas HTTP que puedan ocurrir.

    Args:
        url (str): La URL a la que se realizará la petición

    Returns:
        dict: Un diccionario con la siguiente información:
            - success (bool): True si la petición fue exitosa (código 2xx), False en otro caso
            - status_code (int): El código de estado HTTP
            - is_redirect (bool): True si la respuesta es una redirección (código 3xx)
            - redirect_url (str, opcional): URL de redirección si is_redirect es True
            - error_type (str, opcional): "client_error" para 4xx, "server_error" para 5xx
            - message (str): Un mensaje descriptivo sobre el resultado de la petición
    """
    # Completa esta función para manejar diferentes tipos de respuestas HTTP
    # Debes gestionar al menos:
    # - Respuestas exitosas (códigos 2xx)
    # - Redirecciones (códigos 3xx)
    # - Errores del cliente (códigos 4xx)
    # - Errores del servidor (códigos 5xx)
    try:
        resp = requests.get(url, allow_redirects=False, timeout=10)
    except requests.RequestException as e:
        # Manejo de errores de conexión / tiempo de espera
        return {
            "success": False,
            "status_code": None,
            "is_redirect": False,
            "error_type": "connection_error",
            "message": f"connection_error: Error de conexión o tiempo de espera: {e}"
        }

        
    status = resp.status_code

    #Redirect
    is_redirect = 300 <= status < 400
    redirect_url = resp.headers.get("Location") if is_redirect else None

    body_code = None
    body_desc = None
    mismatch_note = ""
    try:
        data = resp.json()
        body_code = data.get("code")
        body_desc = data.get("description")
        if body_code is not None and body_code != status:
            mismatch_note = f" (Advertencia: JSON code={body_code} no coincide con HTTP {status})"
    except:
        #No json
        pass
    # Mensaje base usando la descripción del body o la razón del status
    base_desc = body_desc or resp.reason or "Sin descripción disponible"
    
    #Success response
    if 200 <= status <300:
        return {
            "success": True,
            "status_code": status,
            "is_redirect": False,
            "message": f"Peticion exitosa ({status}): {base_desc}{mismatch_note}"
        }
        
    if is_redirect:
        return {
            "success": False,
            "status_code": status,
            "is_redirect": True,
            "redirect_url": redirect_url,
            "message": (
                f"Respuesta de redireccion ({status}):{base_desc}. "
                f"Redirige a: {redirect_url}{mismatch_note}"
            )            

        }

     # Errores del cliente (4xx)
    if 400 <= status < 500:
        return {
            "success": False,
            "status_code": status,
            "is_redirect": False,
            "error_type": "client_error",
            "message": f"Error de cliente ({status}): {base_desc}{mismatch_note}"
        }

    # Errores del servidor (5xx)
    if 500 <= status < 600:
        return {
            "success": False,
            "status_code": status,
            "is_redirect": False,
            "error_type": "server_error",
            "message": f"Error de servidor ({status}): {base_desc}{mismatch_note}"
        }

    # Cualquier otro caso raro
    return {
        "success": False,
        "status_code": status,
        "is_redirect": is_redirect,
        "message": f"Respuesta no clasificada ({status}): {base_desc}{mismatch_note}"
    }
if __name__ == "__main__":
    # Puedes probar tu función con estas URLs:

    # Para probar un error 404 (Not Found)
    print("Probando URL con error 404:")
    result = request_with_error_handling("https://httpstatuses.maor.io/404")
    print(f"Resultado: {result}")

    # Para probar un error 500 (Server Error)
    print("\nProbando URL con error 500:")
    result = request_with_error_handling("https://httpstatuses.maor.io/500")
    print(f"Resultado: {result}")

    # Para probar una redirección 301 (Moved Permanently)
    print("\nProbando URL con redirección 301:")
    result = request_with_error_handling("https://httpstatuses.maor.io/301")
    print(f"Resultado: {result}")

    # Para probar una respuesta exitosa
    print("\nProbando URL con respuesta exitosa:")
    result = request_with_error_handling("https://httpstatuses.maor.io/200")
    print(f"Resultado: {result}")
