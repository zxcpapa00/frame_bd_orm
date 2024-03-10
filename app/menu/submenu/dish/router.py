from fastapi import APIRouter
from fastapi.exceptions import HTTPException

from app.menu.submenu.dish.dao import DishDAO
from app.menu.submenu.dish.schemas import CreateSDish, SDish

router = APIRouter(
    tags=['Блюдо'],
    prefix='/api/v1/menus'
)


@router.post('/{menu_id}/submenus/{submenu_id}/dishes', status_code=201)
async def create_dish(menu_id: str, submenu_id: str, data: CreateSDish) -> SDish:
    """Создание блюда"""
    dish = await DishDAO.add(
        submenu_id=submenu_id,
        title=data.title,
        description=data.description,
        price=data.price
    )

    return dish


@router.get('/{menu_id}/submenus/{submenu_id}/dishes', status_code=200)
async def get_dishes(menu_id: str, submenu_id: str) -> list[SDish]:
    """Получение всех блюд подменю"""
    dishes = await DishDAO.get_dishes(submenu_id)
    return dishes


@router.get('/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}', status_code=200)
async def get_dish_by_id(menu_id: str, submenu_id: str, dish_id: str) -> SDish:
    """Получение конкретного блюда"""
    dish = await DishDAO.find_by_id(dish_id)
    if not dish:
        raise HTTPException(status_code=404, detail='dish not found')
    return dish


@router.patch('/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}', status_code=200)
async def update_dish_by_id(menu_id: str, submenu_id: str, dish_id: str, data: CreateSDish) -> SDish:
    """Обновление блюда"""
    dish = await DishDAO.update_by_id(
        dish_id,
        title=data.title,
        description=data.description,
        price=data.price
    )
    return dish


@router.delete('/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}', status_code=200)
async def delete_dish_by_id(menu_id: str, submenu_id: str, dish_id: str):
    """Удаление блюда"""
    await DishDAO.delete_by_id(dish_id)
