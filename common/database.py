from mongoengine import connect as mongo_engine_connect, disconnect_all

from common.config import settings


def connect() -> None:
    try:
        return mongo_engine_connect(
            settings.MONGODB_DATABASE,
            host=settings.MONGODB_HOST,
            port=settings.MONGODB_PORT,
        )
    except Exception as e:
        print("💥💥 Error connecting to mongodb: {}".format(e))


def disconnect() -> None:
    disconnect_all()
