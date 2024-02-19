from sqlalchemy import select
from fastapi.exceptions import HTTPException

from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.menu.models import Menu
from app.menu.submenu.models import SubMenu


class MenuDAO(BaseDAO):
    model = Menu

    @classmethod
    async def get_menu_with_arg(cls, menu_id: str):
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns).filter_by(id=menu_id)
            res = await session.execute(query)
            menu = res.mappings().one_or_none()

            if not menu:
                raise HTTPException(status_code=404, detail="menu not found")

            query = select(SubMenu).filter(SubMenu.menu_id == menu_id)
            res = await session.execute(query)
            submenus = res.mappings().all()
            submenus_count = len(submenus)

            data = {
                'id': menu.id,
                'title': menu.title,
                'description': menu.description,
                'submenus_count': submenus_count
            }
            return data
