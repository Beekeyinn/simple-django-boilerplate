from decouple import config

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": config("DATABASE_NAME"),
        "USER": config("DATABASE_USER"),
        "PASSWORD": config("DATABASE_PASSWORD"),
        "HOST": config("DATABASE_HOST"),
        "PORT": config("DATABASE_PORT"),
    }
}


CHANNEL = config("CHANNEL")
REDIS_URL = f'{config("REDIS_URL")}/{CHANNEL}'

CELERY_BROKER_URL = REDIS_URL
