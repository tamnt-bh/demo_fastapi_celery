from typing import Optional

from pydantic import ConfigDict
from pydantic_settings import BaseSettings


class _Settings(BaseSettings):
    model_config = ConfigDict(env_file=".env", extra="ignore")

    MONGODB_HOST: str
    MONGODB_PORT: int
    MONGODB_DATABASE: str
    MONGODB_EXPOSE_PORT: Optional[str] = None
    MONGODB_USERNAME: str
    MONGODB_PASSWORD: str

    API_PORT: Optional[str] = None

    PROJECT_NAME: str = "Demo Celery + FastAPI"

    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE: int = 1
    SECRET_KEY: str

    ENVIRONMENT: str

    RABBITMQ_USER: str
    RABBITMQ_PASS: str
    RABBITMQ_HOST: str

    SENDGRID_API_KEY: str
    EMAIL_FROM: str
    NAME_EMAIL_FROM: str

    TIMEZONE: str


settings = _Settings()
