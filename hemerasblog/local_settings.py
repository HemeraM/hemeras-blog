import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'hemerabg',
        'USER': 'hemera',
        'PASSWORD': 'hemera1',
        'HOST': 'localhost',
        'PORT': '5433',
    }
}

DEBUG = True
