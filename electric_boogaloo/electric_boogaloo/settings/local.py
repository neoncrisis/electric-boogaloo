from __future__ import absolute_import

from .base import *

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'electric_boogaloo',
        'USER': 'django',
        'PASSWORD': os.getenv('DATABASE_PASSWORD', 'YsPIj03h7hjK14aufQJZpCpyed3mwu'),
        'HOST': os.getenv('DATABASE_HOST', 'localhost'),
        'PORT': '5432',
    }
}