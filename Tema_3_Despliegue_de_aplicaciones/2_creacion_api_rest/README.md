# API de Análisis de Sentimiento con Flask

Este repositorio contiene una API sencilla creada con Flask para realizar análisis de sentimiento en opiniones de usuarios utilizando la biblioteca Hugging Face Transformers.

## Requisitos

Antes de comenzar, asegúrate de tener instalados los siguientes requisitos en tu sistema:

- [Python](https://www.python.org/downloads/)
- [Flask](https://flask.palletsprojects.com/en/2.1.x/)
- [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/)
- [Hugging Face Transformers](https://huggingface.co/transformers/)

## Comenzar

1. Instala las bibliotecas de Python requeridas:

    ```bash
    virtualenv venv
    source venv/bin/activate
    pip install transformers
    pip install Flask
    pip install Flask-RESTful
    ```

2. Ejecuta la aplicación Flask:

    ```bash
    python app.py
    ```

## Puntos finales de la API

La API expone los siguientes puntos finales:

- `GET /sentiment/<int:review_id>`: Recupera el análisis de sentimiento para una revisión específica proporcionando su `review_id`. Si no se proporciona `review_id`, se devuelven todas las revisiones.

- `PUT /sentiment/<int:review_id>`: Agrega una nueva revisión con el `review_id` especificado y se realizará automáticamente un análisis de sentimiento. Debes proporcionar el `name`, `review` y un `rating` opcional.

- `DELETE /sentiment/<int:review_id>`: Elimina una revisión por su `review_id`.

## Solicitud de Ejemplo

Para analizar una revisión, puedes realizar una solicitud PUT a `/sentiment/<int:review_id>`. Por ejemplo:

```bash
curl -X PUT http://127.0.0.1:5000/sentiment/1 -d "name=Juan" -d "review=Este es un gran producto" -d "rating=5"
```

## Respuesta de Ejemplo

La respuesta para una solicitud de análisis de sentimiento incluirá la predicción de sentimiento y la probabilidad:

```json
{
    "name": "Juan",
    "review": "Este es un gran producto",
    "rating": 5,
    "prediction": "POSITIVO",
    "probability": 0.984531044960022,
    "timestamp": "2023-10-27 14:52:03.123456"
}
```

## Personalización

Puedes personalizar el modelo de análisis de sentimiento cambiando el parámetro `model` en la llamada a `transformers.pipeline` para utilizar un modelo diferente de Hugging Face. Ajusta el nombre y los parámetros del modelo según sea necesario.
