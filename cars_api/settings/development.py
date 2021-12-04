# Docker development environment settings

from .base import *

SECRET_KEY = 'Z!i^^6Q@89%vnM4!une*6&9!68VP8*b43@&zbD2^nt548'

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

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