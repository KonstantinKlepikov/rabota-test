import pytest
from aiohttp.test_utils import TestClient
from fastapi import HTTPException
from app.core.http_session import SessionMaker


class TestAiohttpClient:
    """Test aiohttp session cleint
    """

    async def test_aiohttp_client(
        self,
        session: SessionMaker,
            ) -> None:
        """Test get_aiohttp_client
        """
        assert isinstance(session.aiohttp_client, TestClient), 'wrong client'
        await session.close_aiohttp_client()
        assert session.aiohttp_client is None, 'not closed'

    async def test_client(
        self,
        session: SessionMaker,
        urls: dict[str, str]
            ) -> None:
        """Test testclient
        """
        resp = await session.aiohttp_client.get(urls['vacancies'])
        assert resp.status == 200
        text = await resp.text()
        assert '1020000000001' in text, 'wrong result'

    @pytest.mark.parametrize(
        "route,status",
        [("err400", "400"), ("err404", "404"), ("err429", "429")]
            )
    async def test_client_errors(
        self,
        route: str,
        status: int,
        session: SessionMaker,
        urls: dict[str, str]
            ) -> None:
        """Test testclient raise response errors
        """
        with pytest.raises(HTTPException):
            await session._get(session.aiohttp_client, urls[route])
