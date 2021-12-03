# Local development environment settings

from .base import *

SECRET_KEY = 'django-insecure-xm6#byq!q73*@4u*ms6!%!321t4n7ociqdjmz$rz9$1m7b$kny'

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}