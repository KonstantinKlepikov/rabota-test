from fastapi import APIRouter, status, Depends, HTTPException, Request
from pymongo.client_session import ClientSession
from pydantic_core import ValidationError
from app.db.init_db import get_session
from app.schemas.scheme_vacancies import VacancyIn
from app.core.http_session import SessionMaker
from app.core.queries import VacanciesQuery
from app.crud.crud_vacancies import vacancies
from app.config import settings


router = APIRouter()


@router.get(
    "/vacancies_text_search",
    status_code=status.HTTP_200_OK,
    summary='Search vacancies with given text',
    response_description="",
    responses=settings.ERRORS
        )
async def vacancies_text_search(
    db: ClientSession = Depends(get_session),
        ) -> None:
    """
    """
    q = VacanciesQuery(session=SessionMaker, url=settings.VAC_SEQ)
    r = await q.query_vacancies()
    await vacancies.create_or_replace(db, obj_in=r[0])
