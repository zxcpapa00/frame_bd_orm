import asyncio
from typing import Any

import pytest
from app.database import Base, async_session_maker, engine
from httpx import AsyncClient

from app.main import app as fastapi_app
from app.menu.models import Menu
from app.menu.submenu.models import SubMenu
from app.menu.submenu.dish.models import Dish


@pytest.fixture(autouse=True, scope="module")
async def prepare_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


@pytest.fixture(scope='session')
def event_loop():
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
    yield loop
    loop.close()


@pytest.fixture()
async def ac():
    async with AsyncClient(app=fastapi_app, base_url="http://test") as ac:
        yield ac


@pytest.fixture(scope="function")
async def session():
    async with async_session_maker() as session:
        yield session


@pytest.fixture
def menu_post() -> dict[str, str]:
    return {'title': 'Menu 1', 'description': 'Menu 1 desc'}


@pytest.fixture(scope='module')
def saved_data() -> dict[str, Any]:
    return {}


@pytest.fixture
def menu_patch() -> dict[str, str]:
    return {'title': 'update Menu 1', 'description': 'update Menu 1 desc'}
