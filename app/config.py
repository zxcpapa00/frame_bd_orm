from typing import Literal

from pydantic.v1 import ConfigDict
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    model_config = ConfigDict(env_file=".env")
    MODE: Literal["DEV", "TEST", "PROD"]

    # database
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    # test
    TEST_DB_USER: str
    TEST_DB_PASS: str
    TEST_DB_HOST: str
    TEST_DB_PORT: int
    TEST_DB_NAME: str

    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str

    # smtp
    SMTP_HOST: str
    SMTP_USER: str
    SMTP_PORT: int
    SMTP_PASS: str

    # redis
    REDIS_HOST: str
    REDIS_PORT: int


settings = Settings()
