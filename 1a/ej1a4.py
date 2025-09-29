"""
Enunciado:
Desarrolla una aplicación web básica con Flask que maneje diferentes tipos de metadatos enviados en las solicitudes HTTP y explore el uso de diferentes tipos MIME (tipos de contenido).
La aplicación debe tener los siguientes endpoints:

1. `POST /text`: Recibe un texto plano con el tipo MIME `text/plain` y lo devuelve en la respuesta.
2. `POST /html`: Recibe un fragmento HTML con el tipo MIME `text/html` y lo devuelve en la respuesta.
3. `POST /json`: Recibe un objeto JSON con el tipo MIME `application/json` y lo devuelve en la respuesta.
4. `POST /xml`: Recibe un documento XML con el tipo MIME `application/xml` y lo devuelve en la respuesta.
5. `POST /image`: Recibe una imagen con el tipo MIME `image/png` y la guarda en el servidor.

Tu tarea es completar la implementación de la función create_app() y de los endpoints solicitados.
"""

from flask import Flask, jsonify, request, Response

def create_app():
    """
    Crea y configura la aplicación Flask
    """
    app = Flask(__name__)

    @app.route('/text', methods=['POST'])
    def post_text():
        """
        Recibe un texto plano con el tipo MIME `text/plain` y lo devuelve en la respuesta.
        """
        # Implementa este endpoint para devolver el saludo personalizado
        pass  

    @app.route('/html', methods=['POST'])
    def post_html():
        """
        Recibe un fragmento HTML con el tipo MIME `text/html` y lo devuelve en la respuesta.
        """
        # Implementa este endpoint para devolver el saludo personalizado
        pass  

    @app.route('/json', methods=['POST'])
    def post_json():
        """
        Recibe un objeto JSON con el tipo MIME `application/json` y lo devuelve en la respuesta.
        """
        # Implementa este endpoint para devolver el saludo personalizado
        pass  

    @app.route('/xml', methods=['POST'])
    def post_xml():
        """
        Recibe un documento XML con el tipo MIME `application/xml` y lo devuelve en la respuesta.
        """
        # Implementa este endpoint para devolver el saludo personalizado
        pass  

    @app.route('/image', methods=['POST'])
    def post_image():
        """
        Recibe una imagen con el tipo MIME `image/png` y la guarda en el servidor.
        """
        # Implementa este endpoint para devolver el saludo personalizado
        pass  

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
