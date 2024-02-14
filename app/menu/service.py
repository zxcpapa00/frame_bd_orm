from app.menu.dao import MenuDAO


class Service:

    async def get_menu(self, menu_id):
        menu = await MenuDAO.find_by_id(menu_id)
        return {
            "id": menu.id,
            "title": menu.title,
            "description": menu.description
        }
