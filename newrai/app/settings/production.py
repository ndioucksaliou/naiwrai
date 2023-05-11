import os
import sentry_sdk
from .base import *

DEBUG = False

sentry_sdk.init(
    dsn=os.environ["SENTRY_DSN"],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production,
    traces_sample_rate=0.1,
)

DOMAIN = os.environ.setdefault('DOMAIN', 'newrai.fr')

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = [DOMAIN]

CSRF_TRUSTED_ORIGINS = [f"https://{DOMAIN}"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.setdefault('POSTGRES_DB', 'postgres'),
        'USER': os.environ.setdefault('POSTGRES_USER', 'postgres'),
        'PASSWORD': os.environ.setdefault('POSTGRES_PASSWORD', 'postgres'),
        'HOST': os.environ.setdefault('POSTGRES_HOST', 'postgres'),
        'PORT': os.environ.setdefault('POSTGRES_PORT', '5432'),
    }
}

