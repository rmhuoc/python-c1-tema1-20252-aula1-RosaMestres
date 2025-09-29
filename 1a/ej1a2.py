"""
Enunciado:
Desarrolla una aplicación web básica con Flask que responda a peticiones POST.
La aplicación debe tener dos endpoints:

1. `POST /greet?name=<nombre>`: Devuelve un saludo personalizado en formato JSON con la estructura {"message": "¡Hola, <nombre>!"}.
2. `POST /greet-json`: Recibe un JSON con el campo "name" y devuelve un saludo personalizado en formato JSON con la estructura {"message": "¡Hola, <nombre>!"}.

Esta es una introducción simple a Flask para entender cómo manejar datos enviados al servidor mediante parámetros en la URL y mediante un cuerpo JSON.

Tu tarea es completar la implementación de la función create_app() y de los endpoints solicitados.
"""

from flask import Flask, jsonify, request

def create_app():
    """
    Crea y configura la aplicación Flask
    """
    app = Flask(__name__)

    @app.route('/greet', methods=['POST'])
    def greet():
        """
        Devuelve un saludo personalizado utilizando un parámetro en la URL
        """
        # Implementa este endpoint para devolver el saludo personalizado
        pass

    @app.route('/greet-json', methods=['POST'])
    def greet_json():
        """
        Devuelve un saludo personalizado utilizando un JSON en el cuerpo de la solicitud
        """
        # Implementa este endpoint para devolver el saludo personalizado
        pass

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
