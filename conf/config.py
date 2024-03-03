import os
from typing import Any

from pydantic import ConfigDict, field_validator, EmailStr
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_URL: str = "postgresql+psycopg2://koyeb-adm:OQl2Gbzrxh1m@ep-floral-darkness-a2gfw65c.eu-central-1.pg.koyeb.app:5432/db2"
    SECRET_KEY_JWT: str = "1234567890"
    ALGORITHM: str = "HS256"
    MAIL_USERNAME: EmailStr = "postgres@meail.com"
    MAIL_PASSWORD: str = "postgres"
    MAIL_FROM: str = "postgres"
    MAIL_PORT: int = 567234
    MAIL_SERVER: str = "postgres"
    REDIS_DOMAIN: str = 'localhost'
    REDIS_PORT: int = 11929
    REDIS_PASSWORD: str | None = None
    CLD_NAME: str = os.environ.get("CLD_NAME")
    CLD_API_KEY: int = os.environ.get("CLD_API_KEY")
    CLD_API_SECRET: str = os.environ.get("CLD_API_SECRET")

    @field_validator("ALGORITHM")
    @classmethod
    def validate_algorithm(cls, v: Any):
        if v not in ["HS256", "HS512"]:
            raise ValueError("algorithm must be HS256 or HS512")
        return v


    model_config = ConfigDict(extra='ignore', env_file=".env", env_file_encoding="utf-8")  # noqa


config = Settings()
