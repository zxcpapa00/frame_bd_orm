from httpx import AsyncClient


async def test_create_menu(ac: AsyncClient, menu_post: dict[str, str], saved_data: dict):
    response = await ac.post("/api/v1/menus", json=menu_post)

    assert response.status_code == 201
    saved_data['menu'] = response.json()


async def test_create_submenu(ac: AsyncClient, submenu_post: dict[str, str], saved_data: dict):
    menu = saved_data['menu']
    response = await ac.post("/api/v1/menus/{}/submenus".format(menu["id"]), json=submenu_post)

    assert response.status_code == 201
    assert 'id' in response.json()
    assert 'title' in response.json()
    assert 'description' in response.json()

    assert response.json()['title'] == submenu_post['title']
    assert response.json()['description'] == submenu_post['description']

    saved_data['submenu'] = response.json()


async def test_get_submenu_dishes_empty(ac: AsyncClient, saved_data: dict):
    menu = saved_data['menu']
    submenu = saved_data['submenu']
    response = await ac.get("/api/v1/menus/{}/submenus/{}/dishes".format(menu['id'], submenu['id']))

    assert response.status_code == 200
    assert response.json() == []


async def test_create_submenu_dish(ac: AsyncClient, dish_post: dict, saved_data: dict):
    menu = saved_data['menu']
    submenu = saved_data['submenu']
    response = await ac.post("/api/v1/menus/{}/submenus/{}/dishes".format(
        menu['id'],
        submenu['id']),
        json=dish_post)

    assert response.status_code == 201
    assert 'id' in response.json()
    assert 'title' in response.json()
    assert 'description' in response.json()
    assert 'price' in response.json()

    assert response.json()['title'] == dish_post['title']
    assert response.json()['description'] == dish_post['description']
    assert response.json()['price'] == '12.5'

    saved_data['dish'] = response.json()


async def test_get_submenu_dishes(ac: AsyncClient, saved_data: dict):
    menu = saved_data['menu']
    submenu = saved_data['submenu']
    response = await ac.get("/api/v1/menus/{}/submenus/{}/dishes".format(menu['id'], submenu['id']))

    assert response.status_code == 200
    assert response.json() != []


async def test_get_dish(ac: AsyncClient, saved_data: dict):
    menu = saved_data['menu']
    submenu = saved_data['submenu']
    dish = saved_data['dish']
    response = await ac.get("/api/v1/menus/{}/submenus/{}/dishes/{}".format(
        menu['id'],
        submenu['id'],
        dish['id']))

    assert response.status_code == 200
    assert 'id' in response.json()
    assert 'title' in response.json()
    assert 'description' in response.json()
    assert 'price' in response.json()

    assert response.json()['title'] == dish['title']
    assert response.json()['description'] == dish['description']
    assert response.json()['price'] == '12.5'


async def test_patch_dish(ac: AsyncClient, saved_data: dict, dish_patch: dict):
    menu = saved_data['menu']
    submenu = saved_data['submenu']
    dish = saved_data['dish']
    response = await ac.patch("/api/v1/menus/{}/submenus/{}/dishes/{}".format(
        menu['id'],
        submenu['id'],
        dish['id']),
        json=dish_patch)

    assert response.status_code == 200
    assert 'id' in response.json()
    assert 'title' in response.json()
    assert 'description' in response.json()
    assert 'price' in response.json()

    assert response.json()['title'] == dish_patch['title']
    assert response.json()['description'] == dish_patch['description']
    assert response.json()['price'] == '14.5'

    saved_data['dish'] = response.json()


async def test_get_updated_dish(ac: AsyncClient, saved_data: dict):
    menu = saved_data['menu']
    submenu = saved_data['submenu']
    dish = saved_data['dish']
    response = await ac.get("/api/v1/menus/{}/submenus/{}/dishes/{}".format(
        menu['id'],
        submenu['id'],
        dish['id']))

    assert response.status_code == 200
    assert 'id' in response.json()
    assert 'title' in response.json()
    assert 'description' in response.json()
    assert 'price' in response.json()

    assert response.json()['title'] == dish['title']
    assert response.json()['description'] == dish['description']
    assert response.json()['price'] == '14.5'


async def test_delete_dish(ac: AsyncClient, saved_data: dict):
    menu = saved_data['menu']
    submenu = saved_data['submenu']
    dish = saved_data['dish']
    response = await ac.delete("/api/v1/menus/{}/submenus/{}/dishes/{}".format(
        menu['id'],
        submenu['id'],
        dish['id']))

    assert response.status_code == 200


async def test_get_submenu_dishes_before_deleted(ac: AsyncClient, saved_data: dict):
    menu = saved_data['menu']
    submenu = saved_data['submenu']
    response = await ac.get("/api/v1/menus/{}/submenus/{}/dishes".format(menu['id'], submenu['id']))

    assert response.status_code == 200
    assert response.json() == []


async def test_get_deleted_dish(ac: AsyncClient, saved_data: dict):
    menu = saved_data['menu']
    submenu = saved_data['submenu']
    dish = saved_data['dish']
    response = await ac.get("/api/v1/menus/{}/submenus/{}/dishes/{}".format(
        menu['id'],
        submenu['id'],
        dish['id']))

    assert response.status_code == 404


async def test_delete_submenu(ac: AsyncClient, saved_data: dict):
    menu = saved_data['menu']
    submenu = saved_data['submenu']
    response = await ac.delete("/api/v1/menus/{}/submenus/{}".format(
        menu['id'],
        submenu['id']))

    assert response.status_code == 200


async def test_get_dishes(ac: AsyncClient, saved_data: dict):
    menu = saved_data['menu']
    response = await ac.get("/api/v1/menus/{}/submenus".format(
        menu['id']))

    assert response.status_code == 200
    assert response.json() == []


async def test_delete_menu(ac: AsyncClient, saved_data: dict):
    menu = saved_data['menu']
    response = await ac.delete("/api/v1/menus/{}".format(
        menu['id']))

    assert response.status_code == 200


async def get_menus(ac: AsyncClient):
    response = await ac.get("/api/v1/menus")

    assert response.status_code == 200
    assert response.json() == []
