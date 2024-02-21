from typing import Any

from httpx import AsyncClient


async def test_get_menus_empty(ac: AsyncClient):
    response = await ac.get("/api/v1/menus")
    assert response.status_code == 200
    assert response.json() == []


async def test_create_menu(ac: AsyncClient, menu_post: dict[str, str], saved_data: dict[str, Any]):
    response = await ac.post("/api/v1/menus", json=menu_post)
    assert response.status_code == 201
    saved_data['menu'] = response.json()


async def test_get_menu_by_id(ac: AsyncClient, saved_data: dict[str, Any]):
    menu = saved_data['menu']
    response = await ac.get("/api/v1/menus/{}".format(menu['id']))

    assert 'id' in response.json()
    assert 'title' in response.json()
    assert 'description' in response.json()
    assert 'submenus_count' in response.json()
    assert 'dishes_count' in response.json()


async def test_get_menus(ac: AsyncClient):
    response = await ac.get("/api/v1/menus")
    assert response.status_code == 200
    assert response.json() != []


async def test_patch_menu(ac: AsyncClient, saved_data: dict[str, Any], menu_patch: dict[str, str]):
    menu = saved_data['menu']
    response = await ac.patch("/api/v1/menus/{}".format(menu['id']), json=menu_patch)

    assert response.status_code == 200
    assert 'id' in response.json()
    assert 'title' in response.json()
    assert 'description' in response.json()

    assert response.json()['title'] == menu_patch['title']
    assert response.json()['description'] == menu_patch['description']

    saved_data['menu'] = response.json()


async def test_patched_menu(ac: AsyncClient, saved_data: dict[str, Any]):
    menu = saved_data['menu']
    response = await ac.get("/api/v1/menus/{}".format(menu['id']))

    assert response.status_code == 200
    assert response.json()['id'] == menu['id']
    assert response.json()['title'] == menu['title']
    assert response.json()['description'] == menu['description']


async def test_delete_menu(ac: AsyncClient, saved_data: dict[str, Any]):
    menu = saved_data['menu']
    response = await ac.delete("/api/v1/menus/{}".format(menu['id']))

    assert response.status_code == 200


async def test_get_deleted_menu(ac: AsyncClient, saved_data: dict[str, Any]):
    menu = saved_data['menu']
    response = await ac.get("/api/v1/menus/{}".format(menu['id']))

    assert response.status_code == 404
