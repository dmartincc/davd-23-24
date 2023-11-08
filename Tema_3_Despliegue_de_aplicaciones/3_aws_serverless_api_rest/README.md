# Despliegue de una Aplicación Flask con Serverless en AWS

Este repositorio contiene los pasos necesarios para desplegar una aplicación Flask en AWS utilizando una arquitectura serverless, específicamente AWS Lambda y API Gateway. Siga estos pasos para llevar a cabo el despliegue de su aplicación.

## Paso 1: Requisitos Previos

Asegúrese de tener instalado lo siguiente en su sistema:

- [AWS CLI](https://aws.amazon.com/cli/)
- [Python](https://www.python.org/downloads/)
- [Flask](https://flask.palletsprojects.com/en/2.1.x/)
- [Serverless Framework](https://www.serverless.com/)

## Paso 2: Configuración Inicial

Antes de comenzar con el despliegue, realice la configuración inicial:

```bash
serverless login
npm install
pip install -r requirements.txt
```

## Paso 3: Despliegue en AWS

Para desplegar su aplicación en AWS, ejecute el siguiente comando:

```bash
serverless deploy
```

Este comando desplegará su aplicación Flask en AWS Lambda y configurará la API Gateway.

Una vez completado el despliegue, obtendrá una URL para acceder a su aplicación Flask.

## Paso 4: Uso

Una vez completado el despliegue, Serverless Framework le proporcionará la URL de su API Gateway. Utilice esta URL para acceder a su aplicación Flask. Puede hacerlo con un comando `curl` similar al siguiente:

```bash
curl https://xxxxxxxx.execute-api.us-east-1.amazonaws.com/dev/
```

¡Su aplicación Flask se encuentra ahora desplegada en AWS con una arquitectura serverless!

## Personalización

Puede personalizar la configuración de despliegue en el archivo `serverless.yml` según sus necesidades, como configurar dominios personalizados, autorización, escalado y más.

## Acceso Local

Gracias a las capacidades de serverless-wsgi, también es posible ejecutar su aplicación localmente. Sin embargo, para hacerlo, deberá instalar primero la dependencia de werkzeug, así como todas las demás dependencias enumeradas en requirements.txt. Se recomienda utilizar un entorno virtual dedicado para este propósito. Puede instalar todas las dependencias necesarias con los siguientes comandos:

```bash
pip install werkzeug
pip install -r requirements.txt
```

En este punto, puede ejecutar su aplicación localmente con el siguiente comando:

```bash
serverless wsgi serve
```

Este paso le brinda capacidades adicionales de desarrollo local a través del complemento serverless-wsgi.