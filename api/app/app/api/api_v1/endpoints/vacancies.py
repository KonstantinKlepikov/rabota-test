from typing import Annotated
from fastapi import APIRouter, status, Depends, Query
from pymongo.client_session import ClientSession
from app.db.init_db import get_session
from app.schemas.scheme_vacancies import (
    VacancyInOut,
    VacancyTextSearch,
    VacancySearchFields,
        )
from app.core.http_session import SessionMaker
from app.core.queries import VacanciesQuery
from app.crud.crud_vacancies import vacancies
from app.config import settings


router = APIRouter()


# TODO: test me
@router.post(
    "/vacancies_text_search",
    status_code=status.HTTP_200_OK,
    summary='Search vacancies with given ids and text',
    response_description="""
    Filtered by fields values and given words vacancies
    """,
    responses=settings.ERRORS,
    response_model=list[VacancyInOut],
        )
async def vacancies_parametrized_text_search(
    q: VacancySearchFields,
    searchstring: Annotated[list[str], Query()],
    db: ClientSession = Depends(get_session),
        ) -> None:
    """Text search with filtering by fields value.

    Search pattern: AND for all given words. Use a group
    of single words, not phrases for search query.
    """
    # get external api response and update bd
    v = VacanciesQuery(session=SessionMaker, url=settings.VAC_SEQ)
    await v.get_and_create(db)

    # query to db
    q = VacancyTextSearch(**q.model_dump(), searchstring=searchstring)
    return await vacancies.text_search(db, q)
