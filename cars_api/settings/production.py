from .base import *

SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = True if os.environ['DEBUG'].capitalize() == 'True' else False

ALLOWED_HOSTS = [os.environ['DOMAIN']]

# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['DB_DATABASE'],
        'USER': os.environ['DB_USERNAME'],
        'PASSWORD': os.environ['DB_PASSWORD'],
        'HOST': os.environ['DB_HOST'],
        'PORT': os.environ['DB_PORT'],
    }
}