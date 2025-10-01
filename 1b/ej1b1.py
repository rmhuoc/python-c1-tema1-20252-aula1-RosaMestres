"""
Enunciado:
Desarrolla una API REST básica utilizando Flask con un endpoint que devuelve información sobre productos.

Tu tarea es implementar el siguiente endpoint:

`GET /product/<id>`: Devuelve información sobre un producto específico por su ID.
- Si el producto existe, devuelve los datos del producto con código 200 (OK).
- Si el producto no existe, devuelve un mensaje de error con código 404 (Not Found).

Requisitos:
- Utiliza la lista de productos proporcionada.
- Devuelve las respuestas en formato JSON utilizando la función jsonify() de Flask.
- Asegúrate de utilizar los códigos de estado HTTP apropiados.

Ejemplo:
1. Una solicitud `GET /product/1` debe devolver los datos del producto con ID 1 y código 200.
2. Una solicitud `GET /product/999` debe devolver un mensaje de error con código 404.
"""

from flask import Flask, jsonify

# Lista de productos predefinida
products = [
    {"id": 1, "name": "Laptop", "price": 999.99},
    {"id": 2, "name": "Smartphone", "price": 699.99},
    {"id": 3, "name": "Tablet", "price": 349.99}
]

def create_app():
    """
    Crea y configura la aplicación Flask
    """
    app = Flask(__name__)

    @app.route('/product/<int:product_id>', methods=['GET'])
    def get_product(product_id):
        """
        Devuelve información sobre un producto específico por su ID
        - Si existe: devuelve el producto con código 200 (OK)
        - Si no existe: devuelve un error con código 404 (Not Found)
        """
        # Implementa este endpoint
        pass


    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)