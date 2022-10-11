# DjangoRest
Creación de una base de datos utilizando Django Rest framework y Heroku con su respectivo deploy


Configuración de variables de entorno

En la carpeta del proyecto DjangoRest agregar un archivo .env con la siguiente estructura, reemplazar los interrogantes por los datos según corresponda:
DEBUG=True SECRET_KEY=??? DB_DRIVER=django.db.backends.postgresql_psycopg2 DB_HOST=??? DB_PORT=5432 DB_NAME=??? DB_USER=??? DB_PASSWORD=???

Notas
Crea un entorno virtual

python -m venv env

Activa entorno virtual

env\Scripts\activate // para windows source env/bin/activate //para linux

Instala paquete django

pip install django

Crea el proyecto

django-admin startproject nombre_del_proyecto

Crea una aplicación

django-admin startapp nombre_de_la_aplicacion

Inicia la aplicación

python manage.py runserver

Instala paquete djangorestframework para crear una api rest

pip install djangorestframework

Instala paquete djangorestframework-simplejwt para autenticación con JWT

pip install djangorestframework-simplejwt

Instala paquete psycopg2 para conectar a base de datos postgresql

pip install psycopg2

Instala paquete python-decouple para separar la configuración y claves secretas de la aplicación en un archivo .env no rastreado por Git.

pib install python-decouple
