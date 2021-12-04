# Django Cars API

Simple Cars API with Django and Django REST Framework.


## General Info

It is a simple API that you can add, delete and rate cars. 
You can see cars average rating and it's popularity by number of ratings.


## Technologies

* Python
* Django
* Django REST Framework
* PostgreSQL

## Setup

You can setup project in different environments:

* local
* development
* production

### Local

Prerequisites:

* Python

Firstly create virtual environment and install dependencies:

    $ python -m venv env
    $ source env/bin/activate
    $ pip install -r requirements.txt

Then create table migration, create database and run migrations:

    $ python manage.py makemigrations
    $ python manage.py migrate

Then simply run project:

    $ python manage.py runserver


### Development

Prerequisites:

* Docker

Copy Example Environment Variables file to project root directory:

    $ cp .env.example .env

You can also change evironment variables like database name, user, etc. in copied file.

Then build containers and run project:

    $ docker-compose up


### Production

Prerequisites:

* Docker

Copy Example Environment Variables file to project root directory:

    $ cp .env.example .env

Uncomment ENV_ROLE variable in copied file.

You can also change evironment variables like database name, user, etc. in copied file.

Then build containers and run project:

    $ docker-compose up