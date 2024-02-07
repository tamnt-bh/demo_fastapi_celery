from mongoengine import connect as mongo_engine_connect, disconnect_all

from common.config import settings


def connect() -> None:
    if settings.ENVIRONMENT == "testing":
        return mongo_engine_connect(
            settings.MONGODB_DATABASE,
            host=settings.MONGODB_HOST,
            port=settings.MONGODB_PORT,
        )
    else:
        return mongo_engine_connect(
            settings.MONGODB_DATABASE,
            host=settings.MONGODB_HOST,
            port=settings.MONGODB_PORT,
            username=settings.MONGODB_USERNAME,
            password=settings.MONGODB_PASSWORD,
            alias="default",
        )


def disconnect() -> None:
    disconnect_all()
