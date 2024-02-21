from httpx import AsyncClient


class TestMenus:

    async def test_create_menu(self, ac: AsyncClient):
        menu = {"title": "My menu3", "description": "description 1"}
        response = await ac.post("/api/v1/menus", json=menu)
        assert response.status_code == 201

    async def test_get_menus(self, ac: AsyncClient):
        response = await ac.get("/api/v1/menus")
        assert response.status_code == 200
