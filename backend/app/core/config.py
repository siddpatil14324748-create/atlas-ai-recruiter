from functools import lru_cache
from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=False,
    )

    app_name: str = Field(default="atlas-ai-recruiter")
    app_env: Literal["development", "testing", "production"] = Field(default="development")
    debug: bool = Field(default=False)
    logging_level: str = Field(default="INFO")

    postgres_host: str = Field(default="localhost")
    postgres_port: int = Field(default=5432)
    postgres_user: str = Field(default="atlas")
    postgres_password: str = Field(default="atlas")
    postgres_db: str = Field(default="atlas")

    redis_host: str = Field(default="localhost")
    redis_port: int = Field(default=6379)
    redis_db: int = Field(default=0)

    database_url: str | None = Field(default=None)
    redis_url: str | None = Field(default=None)


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
