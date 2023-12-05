from typing import Generator
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.client_session import ClientSession
from pymongo.errors import CollectionInvalid
from app.config import settings
from app.schemas.constraint import Collections


def get_client(mongodb_url: str) -> AsyncIOMotorClient:
    """Get mongo db

    Args:
        mongodb_url (str): url to mongo

    Returns:
        AsyncIOMotorClient: client exemplar
    """
    return AsyncIOMotorClient(mongodb_url)


client = get_client(settings.MONGODB_URL.get_secret_value())


async def create_collections() -> None:
    """Create collections
    """
    for collection in Collections.get_values():

        # create collection if not exist
        try:
            await client[settings.DB_NAME].create_collection(collection)
        except CollectionInvalid:
            continue

        # create indexes
        if collection == Collections.VACANCIES.value:

            await client[settings.DB_NAME][collection].create_index(
                {"$**": "text"}, name='search_index'
                    )


async def get_session() -> Generator[ClientSession, None, None]:
    """Get mongo session
    """
    try:
        session = await client.start_session()
        yield session
    finally:
        await session.end_session()
