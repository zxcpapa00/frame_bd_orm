from httpx import AsyncClient


async def test_create_menu(ac: AsyncClient, menu_post: dict[str, str], saved_data: dict):
    response = await ac.post("/api/v1/menus", json=menu_post)

    assert response.status_code == 201
    saved_data['menu'] = response.json()


async def test_submenus_empty(ac: AsyncClient, saved_data: dict):
    menu = saved_data['menu']
    response = await ac.get("/api/v1/menus/{}/submenus".format(menu['id']))

    assert response.status_code == 200
    assert response.json() == []


async def test_submenu_create(ac: AsyncClient, saved_data: dict, submenu_post: dict):
    menu = saved_data['menu']
    submenu_post['menu_id'] = menu['id']
    response = await ac.post("/api/v1/menus/{}/submenus".format(menu['id']), json=submenu_post)

    assert response.status_code == 201
    saved_data['submenu'] = response.json()


async def test_submenus(ac: AsyncClient, saved_data: dict):
    menu = saved_data['menu']
    response = await ac.get("/api/v1/menus/{}/submenus".format(menu['id']))

    assert response.status_code == 200
    assert response.json() != []


async def test_get_submenu(ac: AsyncClient, saved_data: dict, submenu_post: dict):
    menu = saved_data['menu']
    submenu = saved_data['submenu']
    response = await ac.get("/api/v1/menus/{}/submenus/{}".format(menu['id'], submenu['id']))

    assert response.status_code == 200
    assert response.json()['id'] == submenu['id']
    assert response.json()['title'] == submenu['title']
    assert response.json()['description'] == submenu['description']
    assert response.json()['dishes_count'] == 0


async def test_patch_submenu(ac: AsyncClient, saved_data: dict, submenu_patch: dict):
    menu = saved_data['menu']
    submenu = saved_data['submenu']
    response = await ac.patch("/api/v1/menus/{}/submenus/{}".format(menu['id'], submenu['id']), json=submenu_patch)

    assert response.status_code == 200
    assert response.json()['id'] == submenu['id']
    assert response.json()['title'] == submenu_patch['title']
    assert response.json()['description'] == submenu_patch['description']


async def test_delete_submenu(ac: AsyncClient, saved_data: dict):
    menu = saved_data['menu']
    submenu = saved_data['submenu']
    response = await ac.delete("/api/v1/menus/{}/submenus/{}".format(menu['id'], submenu['id']))

    assert response.status_code == 200


async def test_submenus_empty_before_delete(ac: AsyncClient, saved_data: dict):
    menu = saved_data['menu']
    response = await ac.get("/api/v1/menus/{}/submenus".format(menu['id']))

    assert response.status_code == 200
    assert response.json() == []


async def test_get_submenu_before_delete(ac: AsyncClient, saved_data: dict, submenu_post: dict):
    menu = saved_data['menu']
    submenu = saved_data['submenu']
    response = await ac.get("/api/v1/menus/{}/submenus/{}".format(menu['id'], submenu['id']))

    assert response.status_code == 404


async def test_delete_menu(ac: AsyncClient, saved_data: dict):
    menu = saved_data['menu']
    response = await ac.delete("/api/v1/menus/{}".format(menu['id']))

    assert response.status_code == 200


async def test_get_menus(ac: AsyncClient):
    response = await ac.get("/api/v1/menus")

    assert response.status_code == 200
    assert response.json() == []
