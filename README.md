# Tema 1. Servicios web y API

## 🗒️ Requisitos

Para realizar los ejercicios de este tema deberás tener configurado tu entorno de python.

### Librerias

Para instalar las librerías necesarias para este tema debes ejecutar el siguiente comando en el terminal:

```bash
pip install -r requirements.txt
```

> Nota: El archivo 'requirements.txt' no está dentro de ninguna carpeta.

## 📝 Enunciados

Los ejercicios los encontrarás organizados por carpetas según los apartados del tema. Cada ejercicio se presentará en un fichero python, que incluirá un comentario con el enunciado del ejercicio. 

Los apartados del tema junto con los ejercicios son los siguientes:

| Apartado | Ejercicios                                                     |
| -------- |----------------------------------------------------------------|
| a. Servidores y clientes HTTP | [ej1a1](1a/ej1a1.py) [ej1a2](1a/ej1a2.py) [ej1a3](1a/ej1a3.py) |
| b. Códigos de estado HTTP | [ej1b1](1b/ej1b1.py) [ej1b2](1b/ej1b2.py) [ej1b3](1b/ej1b3.py) |
| c. Cliente de una API | [ej1c1](1c/ej1c1.py) [ej1c2](1c/ej1c2.py) [ej1c3](1c/ej1c3.py) |
| d. Herramientas externas para APIs | [ej1d1](1d/ej1d1.py) |

Además, cada ejercicio irá acompañado de uno o varios tests para comprobar que tu solución es correcta. 

Cuando hayas propuesto una implementación para la función, ejecuta los tests para ver si tu solución es correcta. Si no pasa los tests, vuelve a intentarlo revisando los errores que te comentan los tests.

Una vez termines el ejercicio, deberás enviar tus cambios para que se registren en la plataforma y que puedan ser corregidos por tu profesor. 

Si tienes alguna duda sobre cómo ejecutar los tests o cómo enviar los cambios a GitHub, consulta el ejercicio del Tema 0. Si todavía tienes algun comentario o problema, puedes escribir tu consulta en la plataforma de Preguntas y Respuestas de la Escuela de Programación.

## 💻 Comandos
En la siguiente sección se presentan algunos comandos útiles para el desarrollo de la actividad. 

### Git

Con el fin de actualizar los repositorios locales con la última versión de código fuente, ejecute:

```bash
git pull
```

Para agregar los cambios realizados en los archivos, ejecute:

```bash
git add .
```

Para añadir un mensaje a los cambios realizados localmente, ejecute:

```bash
git commit -m "Mensaje"
```

Para sincronizar nuestras modificaciones con el repositorio remoto, ejecute:
```bash
git push
```

### Python

Para ejecutar las pruebas unitarias:
```bash
pytest 
```
En caso de tener algún problema, puedes probar ejecutar la función con la instrucción `python -m` delante, por ejemplo:

```bash
python -m pytest 
```
```bash
python -m pip install -r requirements.txt
```
Más información sobre cómo ejecutar las pruebas unitarias, consulte el ejercicio del tema 0.
