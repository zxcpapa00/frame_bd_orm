from fastapi import APIRouter

from app.menu.submenu.dish.dao import DishDAO
from app.menu.submenu.dish.schemas import SDish, CreateSDish

router = APIRouter(
    tags=["Блюдо"],
    prefix="/api/v1/menus"
)


@router.post("/{menu_id}/submenus/{submenu_id}/dishes", status_code=201)
async def create_dish(menu_id: str, submenu_id: str, data: CreateSDish) -> SDish:

    dish = await DishDAO.add(
        submenu_id=submenu_id,
        title=data.title,
        description=data.description,
        price=data.price
    )

    return dish


@router.get("/{menu_id}/submenus/{submenu_id}/dishes")
async def get_dishes(menu_id: str, submenu_id: str):
    dishes = await DishDAO.get_dishes(submenu_id)
    return dishes
