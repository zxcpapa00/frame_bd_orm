from sqlalchemy import insert, select

from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.menu.submenu.dish.models import Dish


class DishDAO(BaseDAO):
    model = Dish

    @classmethod
    async def get_dishes(cls, submenu_id: str):
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns).filter_by(submenu_id=submenu_id)
            result = await session.execute(query)
            return result.mappings().all()
