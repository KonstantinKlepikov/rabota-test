from typing import TypeVar, Generic, Type
from pydantic import BaseModel
from app.config import settings


SchemaDbType = TypeVar("SchemaDbType", bound=BaseModel)
SchemaReturnType = TypeVar("SchemaReturnType", bound=BaseModel)


class CRUDBase(Generic[SchemaDbType]):
    def __init__(
        self,
        schema: Type[SchemaReturnType],
        col_name: str,
        db_name: str = settings.DB_NAME
            ):
        """
        CRUD object with default methods to Create,
        Read, Update, Delete (CRUD).
        """
        self.schema = schema
        self.col_name = col_name
        self.db_name = db_name
