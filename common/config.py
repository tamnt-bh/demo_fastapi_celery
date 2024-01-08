from typing import Optional

from pydantic import ConfigDict
from pydantic_settings import BaseSettings


class _Settings(BaseSettings):
    model_config = ConfigDict(env_file=".env")

    # mongodb
    MONGODB_HOST: str
    MONGODB_PORT: int
    MONGODB_DATABASE: str

    PROJECT_NAME: str = "Demo Celery + FastAPI"

    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE: int = 1
    SECRET_KEY: str

    ENVIRONMENT: str

    RABBITMQ_URL: str = "amqp://guest:guest@localhost:5672"

    SENDGRID_API_KEY: str
    EMAIL_FROM: str
    NAME_EMAIL_FROM: str


settings = _Settings()
