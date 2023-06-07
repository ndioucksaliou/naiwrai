import os
import sentry_sdk
from .base import *

DEBUG = False

SECRET_KEY = os.environ["SECRET_KEY"]

sentry_sdk.init(
    dsn=os.environ["SENTRY_DSN"],
    environment="production",
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

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_STORAGE_BUCKET_NAME = "neonumy-uploads-production"
AWS_S3_ACCESS_KEY_ID = os.environ['AWS_S3_ACCESS_KEY_ID']
AWS_S3_SECRET_ACCESS_KEY = os.environ['AWS_S3_SECRET_ACCESS_KEY']
AWS_LOCATION = "newrai"
AWS_QUERYSTRING_AUTH = False
AWS_DEFAULT_ACL = "public-read"

AWS_S3_FILE_OVERWRITE = False