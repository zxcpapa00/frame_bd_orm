from sqlalchemy import select, insert, func

from fastapi.exceptions import HTTPException
from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.menu.submenu.dish.models import Dish
from app.menu.submenu.models import SubMenu


class SubMenuDAO(BaseDAO):
    model = SubMenu

    @classmethod
    async def find_all_submenu_for_menu(cls, menu_id: str):
        async with (async_session_maker() as session):
            query = select(
                cls.model.__table__.columns,
                func.count(Dish.__table__.columns.id).label('dishes_count')
            ).filter_by(menu_id=menu_id).outerjoin(
                Dish, Dish.submenu_id == cls.model.__table__.columns.id
            ).group_by(cls.model.__table__.columns.id)
            result = await session.execute(query)
            return result.mappings().all()

    @classmethod
    async def create_submenu_for_menu(cls, menu_id: str, **data):
        async with async_session_maker() as session:
            query = insert(cls.model).values(menu_id=menu_id, **data)
            await session.execute(query)
            await session.commit()

            query = select(cls.model).filter_by(**data)
            result = await session.execute(query)
            added_object = result.scalar()
            return added_object

    @classmethod
    async def get_submenu(cls, menu_id: str, submenu_id: str):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(id=submenu_id, menu_id=menu_id)
            result = await session.execute(query)
            submenu = result.scalars().one_or_none()
            if not submenu:
                raise HTTPException(status_code=404, detail="submenu not found")

            data = {
                'id': submenu.id,
                'title': submenu.title,
                'description': submenu.description,
                'dishes_count': len(submenu.dishes)
            }

            print(len(submenu.dishes))
            return data
