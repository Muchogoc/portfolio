from portfolio.settings.base import *

import environ
import sentry_sdk

from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="https://7aa200acb2bf4f648cfd9d016710ddcd@sentry.io/1499111",
    integrations=[DjangoIntegration()]
)

env = environ.Env()
environ.Env.read_env(os.path.join(ROOT_DIR, '.env'))
SECRET_KEY = env('SECRET_KEY')

# DEBUG = env.bool('DEBUG')
DEBUG = True

# ALLOWED_HOSTS = [env.list('ALLOWED_HOSTS', cast=None)]
ALLOWED_HOSTS = ['*']

PROMETHEUS_EXPORT_MIGRATIONS = False


DATABASES = {
    'default': 
        env.db('DATABASE_URL')
    
}