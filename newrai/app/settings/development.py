from .base import *
import sentry_sdk
from core_lib.config_loader.utils import get_env


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

APP_SLUG = get_env("APP_SLUG")

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-!1anq!md%#l&42qlju7fgl^e4a9g0+=mzo-pun+j2-p2qj*-ts"

DOMAIN = "newrai.development.neonumy.dev"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = [DOMAIN]

CSRF_TRUSTED_ORIGINS = [f"https://{DOMAIN}"]

EMAIL_BACKEND = "django_ses.SESBackend"


sentry_sdk.init(
    dsn=get_env("SENTRY_DSN"),
    environment="development",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production,
    traces_sample_rate=0.1,
)

# try:
#     from .local import *
# except ImportError:
#     pass

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": f"{APP_SLUG}_db",
        "USER": f"{APP_SLUG}_user",
        "PASSWORD": get_env("DATABASE_POSTGRES_PASSWORD", ""),
        "HOST": get_env("DATABASE_POSTGRES_HOST", ""),
        "PORT": get_env("DATABASE_POSTGRES_PORT", ""),
        # required for pgBouncer
        "DISABLE_SERVER_SIDE_CURSORS": True,
    }
}

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_STORAGE_BUCKET_NAME = "neonumy-uploads-development"
AWS_S3_ACCESS_KEY_ID = get_env('AWS_ACCESS_KEY_ID')
AWS_S3_SECRET_ACCESS_KEY = get_env('AWS_SECRET_ACCESS_KEY')
AWS_LOCATION = "newrai"
AWS_QUERYSTRING_AUTH = False
AWS_DEFAULT_ACL = "public-read"

AWS_S3_FILE_OVERWRITE = False

AWS_SES_REGION_NAME = 'eu-central-1'
AWS_SES_REGION_ENDPOINT = 'email.eu-central-1.amazonaws.com'