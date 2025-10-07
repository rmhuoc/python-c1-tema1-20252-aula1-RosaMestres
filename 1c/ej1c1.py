"""
Enunciado:
Desarrolla un cliente HTTP básico utilizando la biblioteca requests de Python.
El cliente debe realizar peticiones a la API pública de Wikipedia.

Tareas:
1. Realizar una petición GET a la API de Wikipedia para obtener información sobre un artículo
2. Procesar la respuesta JSON para extraer información relevante
3. Manejar posibles errores en las peticiones

Esta es una introducción a las peticiones HTTP en Python utilizando la biblioteca requests
para entender cómo interactuar con APIs web.

Tu tarea es completar la implementación de las funciones indicadas.

Nota: La API de Wikipedia es estable y ampliamente utilizada, perfecta para aprender
cómo funcionan las peticiones HTTP.
"""

import requests

def get_wikipedia_article(article_title):
    """
    Realiza una petición GET a la API de Wikipedia para obtener información
    sobre el artículo especificado.
    
    Args:
        article_title (str): El título del artículo de Wikipedia a buscar
        
    Returns:
        dict: Datos del artículo si se encuentra
        None: Si ocurre un error o no se encuentra el artículo
    """
    # La URL base de la API de Wikipedia en español
    base_url = "https://es.wikipedia.org/api/rest_v1/page/summary/"
    
    # Implementa aquí la lógica para:
    # 1. Construir la URL completa utilizando el título del artículo
    # 2. Realizar una petición GET usando requests
    # 3. Verificar el código de estado de la respuesta
    # 4. Si es exitosa (código 200), devolver el contenido JSON
    # 5. Si hay un error, manejar la excepción y devolver None
    pass


def extract_article_info(article_data):
    """
    Extrae información relevante del artículo a partir de los datos recibidos.
    
    Args:
        article_data (dict): Datos del artículo obtenidos de la API
        
    Returns:
        dict: Diccionario con los campos 'title', 'description' y 'extract'
        None: Si los datos de entrada son None o no tienen el formato esperado
    """
    # Implementa aquí la lógica para:
    # 1. Verificar que article_data no es None
    # 2. Extraer el título, la descripción y el extracto del artículo
    # 3. Devolver un diccionario con esos tres campos
    # 4. Manejar posibles errores si algún campo no existe
    pass


def print_article_summary(article_info):
    """
    Imprime un resumen formateado del artículo.
    
    Args:
        article_info (dict): Información del artículo con los campos 'title',
                            'description' y 'extract'
    """
    # Implementa aquí la lógica para:
    # 1. Verificar que article_info no es None
    # 2. Imprimir el título, la descripción y el extracto con formato
    # 3. Si article_info es None, imprimir un mensaje de error
    pass


if __name__ == '__main__':
    # Título del artículo a buscar
    article = "Python_(programming_language)"
    
    # Obtener los datos del artículo
    article_data = get_wikipedia_article(article)
    
    # Extraer la información relevante
    article_info = extract_article_info(article_data)
    
    # Imprimir el resumen
    print_article_summary(article_info)
