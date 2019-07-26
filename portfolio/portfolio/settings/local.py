from .base import *

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = os.environ.get('DEBUG', default=True)

ALLOWED_HOSTS = ['localhost', '127.0.0.1']
