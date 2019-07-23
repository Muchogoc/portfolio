from .base import *

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="https://7aa200acb2bf4f648cfd9d016710ddcd@sentry.io/1499111",
    integrations=[DjangoIntegration()]
)


DEBUG = DEBUG = os.environ.get('DEBUG', default=False)

SECRET_KEY = os.environ.get('SECRET_KEY')

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '35.194.45.36', '18.219.55.177']

INSTALLED_APPS = INSTALLED_APPS + ('django_prometheus',)

MIDDLEWARE = (
        ('django_prometheus.middleware.PrometheusBeforeMiddleware',) +
        MIDDLEWARE +
        ('django_prometheus.middleware.PrometheusAfterMiddleware',)
    )

PROMETHEUS_EXPORT_MIGRATIONS = False

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('SQL_ENGINE'),
        'NAME': os.environ.get('SQL_DATABASE'),
        'USER': os.environ.get('SQL_USER'),
        'PASSWORD': os.environ.get('SQL_PASSWORD'),
        'HOST': os.environ.get('SQL_HOST'),
        'PORT': os.environ.get('SQL_PORT'),

    }
}