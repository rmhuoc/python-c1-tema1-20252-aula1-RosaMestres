"""
Enunciado:
Desarrolla una aplicación web básica con Flask que maneje diferentes tipos de metadatos enviados en las solicitudes HTTP y explore el uso de diferentes tipos MIME (tipos de contenido).
La aplicación debe tener los siguientes endpoints:

1. `GET /text`: Devuelve un texto plano con el tipo MIME `text/plain`.
2. `GET /html`: Devuelve un fragmento HTML con el tipo MIME `text/html`.
3. `GET /json`: Devuelve un objeto JSON con el tipo MIME `application/json`.
4. `GET /xml`: Devuelve un documento XML con el tipo MIME `application/xml`.
5. `GET /image`: Devuelve una imagen con el tipo MIME `image/png` (usa una imagen estática para este ejemplo).

Tu tarea es completar la implementación de la función create_app() y de los endpoints solicitados.
"""

from flask import Flask, jsonify, Response, send_file

def create_app():
    """
    Crea y configura la aplicación Flask
    """
    app = Flask(__name__)

    @app.route('/text', methods=['GET'])
    def get_text():
        """
        Devuelve un texto plano con el tipo MIME `text/plain`
        """
        # Implementa este endpoint para devolver el contenido solicitado
        pass  

    @app.route('/html', methods=['GET'])
    def get_html():
        """
        Devuelve un fragmento HTML con el tipo MIME `text/html`
        """
        # Implementa este endpoint para devolver el contenido solicitado
        pass  

    @app.route('/json', methods=['GET'])
    def get_json():
        """
        Devuelve un objeto JSON con el tipo MIME `application/json`
        """
        # Implementa este endpoint para devolver el contenido solicitado
        pass  

    @app.route('/xml', methods=['GET'])
    def get_xml():
        """
        Devuelve un documento XML con el tipo MIME `application/xml`
        """
        # Implementa este endpoint para devolver el contenido solicitado
        pass  

    @app.route('/image', methods=['GET'])
    def get_image():
        """
        Devuelve una imagen con el tipo MIME `image/png`
        """
        # Implementa este endpoint para devolver el contenido solicitado
        pass  

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
