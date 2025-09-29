"""
Enunciado:
Desarrolla una aplicación web básica con Flask que responda a una petición GET.
La aplicación debe tener un único endpoint:

1. `GET /hello`: Devuelve un mensaje de saludo en formato JSON con la estructura {"message": "¡Hola, mundo!"}.

Esta es una introducción simple a Flask para entender cómo crear una aplicación web básica y responder
a solicitudes HTTP.

Tu tarea es completar la implementación de la función create_app() y del endpoint solicitado.
"""

from flask import Flask, jsonify

def create_app():
    """
    Crea y configura la aplicación Flask
    """
    app = Flask(__name__)

    @app.route('/hello', methods=['GET'])
    def hello():
        """
        Devuelve un mensaje de saludo en formato JSON
        """
        # Implementa este endpoint para devolver el mensaje de saludo
        pass

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)