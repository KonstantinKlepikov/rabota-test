import pytest
from typing import Callable
from fastapi import HTTPException
from app.core.queries import VacanciesQuery
from app.core.http_session import SessionMaker
from app.schemas.scheme_vacancies import VacancyIn
from tests.core.conftest import vacancies_raw


@pytest.fixture
def queries(session: SessionMaker) -> VacanciesQuery:
    """Make queries class
    """
    q = VacanciesQuery(
        session,
        "http://gsr-rabota.ru/api/v2/Vacancies/All/List",
            )
    return q


class TestVacanciesQuery:
    """Test VacanciesQuery
    """

    @pytest.fixture(scope="function")
    async def mock_response(
        self,
        session: SessionMaker,
        monkeypatch,
            ) -> Callable:
        async def mock_return(*args, **kwargs) -> Callable:
            return vacancies_raw()
        monkeypatch.setattr(session, "get_query", mock_return)

    @pytest.mark.skip("FIXME: error with aiohttp client")
    async def test_query_vacancie(
        self,
        queries: VacanciesQuery,
            ) -> None:
        """Test make_simple_entry
        """
        data = vacancies_raw()
        result = await queries.query_vacancies()
        assert len[result] == len(data)
        assert isinstance(result, list)
        assert isinstance(result[0], VacancyIn)
