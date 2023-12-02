import toml
from pydantic import SecretStr
from pydantic_settings import BaseSettings
from typing import Type
from app.schemas.scheme_error import (
    HttpErrorMessage,
    HttpError400,
    HttpError404,
    HttpError409,
        )


ErrorType = dict[int, dict[str, Type[HttpErrorMessage]]]
poetry_data = toml.load('pyproject.toml')['tool']['poetry']


class Settings(BaseSettings):
    # api vars
    API_V1: str = "/api/v1"

    # db settings
    MONGODB_URL: SecretStr
    DB_NAME: str

    # aiohttp session parameters
    SIZE_POOL_HTTP: int = 100
    TIMEOUT_AIOHTTP: int = 2
    QUERY_SLEEP: float = 0.05

    # open-api settings
    title: str = poetry_data['name']
    descriprion: str = poetry_data['description']
    version: str = poetry_data['version']
    openapi_tags: list = [
        {
            "name": "vacancies",
            "description": "Search vacancies",
        },
    ]
    ERRORS: ErrorType = {
        400: {'model': HttpError400},
        404: {'model': HttpError404},
        409: {'model': HttpError409},
            }


settings = Settings()
