from .base import *

from core_lib.config_loader.utils import get_env


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

APP_SLUG = get_env("APP_SLUG")

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-!1anq!md%#l&42qlju7fgl^e4a9g0+=mzo-pun+j2-p2qj*-ts"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


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