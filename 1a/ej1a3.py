"""
Enunciado:
Desarrolla una aplicación web básica con Flask que responda a una petición GET y devuelva una pequeña página web.
La aplicación debe tener el siguiente endpoint:

1. `GET /website`: Devuelve una página web con una estructura HTML mínima que incluya un mensaje "¡Hola mundo!".

Tu tarea es completar la implementación de la función create_app() y del endpoint solicitado.

Nota: Asegúrate de incluir una estructura HTML válida en la respuesta.
"""

from flask import Flask

def create_app():
    """
    Crea y configura la aplicación Flask
    """
    app = Flask(__name__)

    @app.route('/website', methods=['GET'])
    def get_website():
        """
        Devuelve una página web con una estructura HTML mínima
        """
        # Implementa este endpoint para devolver el contenido solicitado
        pass

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
