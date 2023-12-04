from typing import Annotated
from fastapi import APIRouter, status, Depends, Query, HTTPException
from pymongo.client_session import ClientSession
from pydantic_core import ValidationError
from app.db.init_db import get_session
from app.schemas.scheme_vacancies import VacancyInOut, VacancyQuery
from app.core.http_session import SessionMaker
from app.core.queries import VacanciesQuery
from app.crud.crud_vacancies import vacancies
from app.config import settings


router = APIRouter()


# TODO: test me
@router.get(
    "/vacancies_text_search",
    status_code=status.HTTP_200_OK,
    summary='Search vacancies with given text',
    response_description="",
    responses=settings.ERRORS
        )
async def vacancies_text_search(
    searchstring: Annotated[list[str], Query()],
    db: ClientSession = Depends(get_session),
        ) -> None:
    """
    """
    # get external api response and update bd
    v = VacanciesQuery(session=SessionMaker, url=settings.VAC_SEQ)
    await v.get_and_create(db)

    # query to db
    q = VacancyQuery(searchstring=searchstring)
    result = await vacancies.text_search(db, q)
    r = [r.model_dump(exclude=['id', ]) for r in result]
    print(r)
    return [r.model_dump(exclude=['_id', ]) for r in result]

# TODO: test me
@router.post(
    "/vacancies_text_search",
    status_code=status.HTTP_200_OK,
    summary='Search vacancies with given ids and text',
    response_description="",
    responses=settings.ERRORS
        )
async def vacancies_parametrized_text_search(
    q: VacancyQuery,
    db: ClientSession = Depends(get_session),
        ) -> None:
    """
    """
    # get external api response and update bd
    v = VacanciesQuery(session=SessionMaker, url=settings.VAC_SEQ)
    await v.get_and_create(db)

    # query to db
    result = await vacancies.text_search(db, q)
    return [r.model_dump(exclude=['id', ]) for r in result]
