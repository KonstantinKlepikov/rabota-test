from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.api.api_v1.api import api_router
from app.db.init_db import create_collections
from app.core.http_session import SessionMaker


async def aio_on_start_up() -> None:
    SessionMaker.get_aiohttp_client()


async def aio_on_shutdown() -> None:
    await SessionMaker.close_aiohttp_client()


app = FastAPI(
    title=settings.title,
    openapi_url=f"{settings.API_V1}/openapi.json",
    description=settings.descriprion,
    version=settings.version,
    openapi_tags=settings.openapi_tags,
    swagger_ui_parameters={"defaultModelsExpandDepth": -1},
    on_startup=[aio_on_start_up, create_collections],
    on_shutdown=[aio_on_shutdown],
        )


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(api_router, prefix=settings.API_V1)
