import asyncio
import pytest
from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, DeclarativeBase

from app.config import Settings, settings
from fastapi.testclient import TestClient
from httpx import AsyncClient

from app.main import app as fastapi_app
from app.menu.models import Menu
from app.menu.submenu.models import SubMenu
from app.menu.submenu.dish.models import Dish

DATABASE_URL = (
    f"postgresql+asyncpg://{settings.TEST_DB_USER}:{settings.TEST_DB_PASS}@{settings.TEST_DB_HOST}:"
    f"{settings.TEST_DB_PORT}/{settings.TEST_DB_NAME}")

test_engine = create_async_engine(DATABASE_URL, poolclass=NullPool)

test_async_session_maker = sessionmaker(bind=test_engine, class_=AsyncSession, expire_on_commit=False)


class TestBase(DeclarativeBase):
    pass


@pytest.fixture(autouse=True, scope="module")
async def prepare_database():
    async with test_engine.begin() as conn:
        await conn.run_sync(Menu.metadata.drop_all)
        await conn.run_sync(Menu.metadata.create_all)


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
    async with test_async_session_maker() as session:
        yield session
