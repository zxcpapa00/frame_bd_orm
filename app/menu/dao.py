from sqlalchemy import select, text
from fastapi.exceptions import HTTPException

from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.menu.models import Menu


class MenuDAO(BaseDAO):
    model = Menu

    @classmethod
    async def get_menus_with_submenus_and_dishes(cls):
        async with async_session_maker() as session:
            query = select(cls.model)
            res = await session.execute(query)
            return res.scalars().all()

    @classmethod
    async def get_menu_with_arg(cls, menu_id: str):
        async with async_session_maker() as session:
            """SQL QUERY 
            SELECT m.id, m.title, m.description, COUNT(s.id) as submenus_count, d.dishes_count FROM menu as m
            LEFT JOIN submenu as s ON m.id = s.menu_id
            LEFT JOIN (SELECT s.id, COUNT(d.submenu_id) as dishes_count FROM submenu as s
            JOIN dish as d ON d.submenu_id = s.id
            GROUP BY 1) as d ON d.id = s.id
            GROUP BY 1, 5"""

            query = text("""SELECT m.id, m.title, m.description, COUNT(s.id) as submenus_count, d.dishes_count FROM menu as m
            LEFT JOIN submenu as s ON m.id = s.menu_id
            LEFT JOIN (SELECT s.id, COUNT(d.submenu_id) as dishes_count FROM submenu as s
            JOIN dish as d ON d.submenu_id = s.id
            GROUP BY 1) as d ON d.id = s.id
            WHERE m.id = '{}'
            GROUP BY 1, 5""".format(menu_id))

            res = await session.execute(query)
            menu = res.mappings().one_or_none()

            if not menu:
                raise HTTPException(status_code=404, detail="menu not found")

            return menu

            # query = select(cls.model.__table__.columns).filter_by(id=menu_id)
            # res = await session.execute(query)
            # menu = res.mappings().one_or_none()
            #
            # if not menu:
            #     raise HTTPException(status_code=404, detail="menu not found")
            #
            # query = select(SubMenu).filter(SubMenu.menu_id == menu_id)
            # res = await session.execute(query)
            # submenus = res.scalars().all()
            # submenus_count = len(submenus)
            #
            # dishes_count = sum([len(submenu.dishes) for submenu in submenus])
            #
            # data = {
            #     'id': menu.id,
            #     'title': menu.title,
            #     'description': menu.description,
            #     'submenus_count': submenus_count,
            #     'dishes_count': dishes_count
            # }
            # return data
