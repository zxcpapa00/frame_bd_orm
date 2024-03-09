from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis

from app.database import async_session_maker
from app.menu.router import router as menu_router
from app.menu.submenu.router import router as submenu_router
from app.menu.submenu.dish.router import router as dish_router

from app.menu.models import Menu

app = FastAPI(
    title="Restaurant menu"
)
app.include_router(menu_router)
app.include_router(submenu_router)
app.include_router(dish_router)


# @app.on_event("startup")
# async def clear_database():
#     async with async_session_maker() as session:
#         await session.execute(Menu.__table__.delete())
#         await session.commit()


@app.on_event("startup")
def startup():
    redis = aioredis.from_url("redis://localhost:6379", encoding="utf-8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="cache")
