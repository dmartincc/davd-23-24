# Ejercicio git y dash

## Pull repositorio

```
git pull git@github.com:dmartincc/davd-23-24.git
```
Ahora que hemos bajado el repositorio a proceder a:

## Ir al folder donde tenemos el servidor de dash.

```
cd Tema_2_app_visualizaciones/ 
```

## Instalar entorno virtual y sus dependencias.

Instalar y configurar virtualenvwrapper para crear entorno virtuales.

````
pip install virtualenvwrapper
export WORKON_HOME=~/Envs
mkdir -p $WORKON_HOME
source /usr/local/bin/virtualenvwrapper.sh
mkvirtualenv dash
````
Instalar dependecias a partir del fichero requirements.txt

```
pip install -r requirements.txt
```

Ahora con nuestro entorno virtual con todas las dependencias necesarias podemos arrancar el servidor.

## Arrancar el servidor de dash.

```
python 3.\ Introduccion\ a\ Dash.py
```

Carga en el navegador la url: http://127.0.0.1:8050/

Revisa el código del script de python que hemos arrancado y estudia los componentes.

Ahora, procedemos a arrancar el servidor con callbacks.

```
python 4.\ Callbacks\ y\ componentes\ core.py
```





