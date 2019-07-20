from .base import *

import environ
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="https://7aa200acb2bf4f648cfd9d016710ddcd@sentry.io/1499111",
    integrations=[DjangoIntegration()]
)

env = environ.Env()

env.read_env(os.path.join(ROOT_DIR, '.env'))

DEBUG = False

SECRET_KEY = env('SECRET_KEY')

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
        'ENGINE': env('SQL_ENGINE'),
        'NAME': env('SQL_DATABASE'),
        'USER': env('SQL_USER'),
        'PASSWORD': env('SQL_PASSWORD'),
        'HOST': env('SQL_HOST'),
        'PORT': env('SQL_PORT'),

    }
}