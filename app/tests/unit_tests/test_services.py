from httpx import AsyncClient


async def test_create_menu(ac: AsyncClient, saved_data: dict, menu_post: dict):
    response = await ac.post('api/v1/menus', json=menu_post)

    assert response.status_code == 201
    saved_data['menu'] = response.json()


async def test_create_submenu(ac: AsyncClient, saved_data: dict, submenu_post: dict):
    menu = saved_data['menu']
    response = await ac.post('api/v1/menus/{}/submenus'.format(menu['id']), json=submenu_post)

    assert response.status_code == 201
    saved_data['submenu'] = response.json()


async def test_create_dish_one(ac: AsyncClient, saved_data: dict, dish_post: dict):
    menu = saved_data['menu']
    submenu = saved_data['submenu']
    response = await ac.post('api/v1/menus/{}/submenus/{}/dishes'.format(
        menu['id'],
        submenu['id']),
        json=dish_post)

    assert response.status_code == 201
    saved_data['dish_one'] = response.json()


async def test_create_dish_second(ac: AsyncClient, saved_data: dict, dish_post_second: dict):
    menu = saved_data['menu']
    submenu = saved_data['submenu']
    response = await ac.post('api/v1/menus/{}/submenus/{}/dishes'.format(
        menu['id'],
        submenu['id']),
        json=dish_post_second)

    assert response.status_code == 201
    saved_data['dish_second'] = response.json()


async def test_get_menu(ac: AsyncClient, saved_data: dict):
    menu = saved_data['menu']
    response = await ac.get('api/v1/menus/{}'.format(menu['id']))

    assert response.status_code == 200
    assert 'id' in response.json()
    assert 'title' in response.json()
    assert 'description' in response.json()
    assert 'submenus_count' in response.json()
    assert 'dishes_count' in response.json()

    assert response.json()['submenus_count'] == 1
    assert response.json()['dishes_count'] == 2


async def test_get_submenu(ac: AsyncClient, saved_data: dict):
    menu = saved_data['menu']
    submenu = saved_data['submenu']
    response = await ac.get('api/v1/menus/{}/submenus/{}'.format(
        menu['id'],
        submenu['id']))

    assert response.status_code == 200
    assert 'id' in response.json()
    assert 'title' in response.json()
    assert 'description' in response.json()
    assert 'dishes_count' in response.json()

    assert response.json()['dishes_count'] == 2


async def test_delete_submenu(ac: AsyncClient, saved_data: dict):
    menu = saved_data['menu']
    submenu = saved_data['submenu']
    response = await ac.delete('api/v1/menus/{}/submenus/{}'.format(
        menu['id'],
        submenu['id']))

    assert response.status_code == 200


async def test_get_submenus(ac: AsyncClient, saved_data: dict):
    menu = saved_data['menu']
    response = await ac.get('api/v1/menus/{}/submenus'.format(
        menu['id']))

    assert response.status_code == 200
    assert response.json() == []


async def test_get_dishes(ac: AsyncClient, saved_data: dict):
    menu = saved_data['menu']
    submenu = saved_data['submenu']
    response = await ac.get('api/v1/menus/{}/submenus/{}/dishes'.format(
        menu['id'],
        submenu['id']))

    assert response.status_code == 200
    assert response.json() == []


async def test_get_menu_before_delete(ac: AsyncClient, saved_data: dict):
    menu = saved_data['menu']
    response = await ac.get('api/v1/menus/{}'.format(menu['id']))

    assert response.status_code == 200
    assert 'id' in response.json()
    assert 'title' in response.json()
    assert 'description' in response.json()
    assert 'submenus_count' in response.json()
    assert 'dishes_count' in response.json()

    assert response.json()['submenus_count'] == 0
    assert response.json()['dishes_count'] == 0


async def test_delete_menu(ac: AsyncClient, saved_data: dict):
    menu = saved_data['menu']
    response = await ac.delete('api/v1/menus/{}'.format(menu['id']))

    assert response.status_code == 200


async def test_get_menus(ac: AsyncClient, saved_data: dict):
    response = await ac.get('api/v1/menus')

    assert response.status_code == 200
    assert response.json() == []
