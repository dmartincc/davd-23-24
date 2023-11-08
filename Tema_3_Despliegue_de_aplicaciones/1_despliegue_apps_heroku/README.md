# Como desplegar dash app en Heroku

Heroku es una plataforma de despliegue de aplicaciones web autogestionada.

Paso 1. Darse de alta en Heroku

Obtener usuario, password e instalar [Heroku cli](https://devcenter.heroku.com/articles/heroku-cli).

Paso 2.  Crear repositorio y entorno virtual

````
git init   
virtualenv venv
source venv/bin/activate
```

## Paso 3. Instalar dependencias

````
pip install -r requirements.txt
```

## Paso 4. Programa tu aplicación

Modifica __app.py__ y añade el código necesario para tu app.

## Paso 4. Desplegar aplicación

```
heroku create my-dash-app # change my-dash-app to a unique name
git add . # add all files to git
git commit -m 'Initial app boilerplate'
git push heroku master # deploy code to heroku
heroku ps:scale web=1  # run
```

En la siguiente url deberias tener acceso a tu aplicación. __https://my-dash-app.herokuapp.com__

Nota: Cambia __my-dash-app__ por el nombre tu aplicación.

## Paso 5. Actualizar aplicación

```
git status # view the changes
git add .  # add all the changes
git commit -m 'a description of the changes'
git push heroku master
```