import pytest
import json
from functools import lru_cache
from typing import Any
from aiohttp import web
from aiohttp.test_utils import TestClient
from yarl import URL
from app.core.http_session import SessionMaker


@lru_cache
def vacancies_raw() -> list[dict[str: Any]]:
    """Mock vacancies data raw
    """
    with open('./tests/core/vacancies.json', 'r') as f:
        return json.loads(f.read())


def vacancies(request: web.Request) -> web.Response:
    """Mock vacancies response
    """
    return web.Response(
        text=json.dumps(vacancies_raw(), ensure_ascii=False),
        content_type='application/json'
            )


async def err400(request: web.Request) -> web.Response:
    """Mock hhru vacancy response errors
    """
    return web.Response(status=400, content_type='application/json')


async def err404(request: web.Request) -> web.Response:
    """Mock hhru vacancy response errors
    """
    return web.Response(status=404, content_type='application/json')


async def err429(request: web.Request) -> web.Response:
    """Mock hhru vacancy response errors
    """
    return web.Response(status=429, content_type='application/json')


@pytest.fixture
def urls() -> dict[str, str]:
    """Urls for request

    Returns:
        dict[str, str]: dict with urls
    """
    return {
        'vacancies': str(URL.build(path='/api/v2/Vacancies/All/List')),
        'err400': str(URL.build(path='/err400')),
        'err404': str(URL.build(path='/err404')),
        'err429': str(URL.build(path='/err429')),
            }


@pytest.fixture
def client(loop, aiohttp_client) -> TestClient:
    """Make a test client
    """
    app = web.Application()
    app.router.add_routes([
        web.get('/api/v2/Vacancies/All/List', vacancies),
        web.get('/err400', err400),
        web.get('/err404', err404),
        web.get('/err429', err429),
            ])
    client = loop.run_until_complete(aiohttp_client(app))
    return client


@pytest.fixture
def session(client: TestClient) -> SessionMaker:
    """Make test session
    """
    SessionMaker.aiohttp_client = client
    session = SessionMaker()
    return session
