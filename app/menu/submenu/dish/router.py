from fastapi import APIRouter, status

from app.menu.submenu.dish.dao import DishDAO

router = APIRouter(
    tags=["Блюдо"]
)


@router.post("/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes")
async def create_dish(menu_id: str, submenu_id: str, title: str, description: str, price: float):
    dish = await DishDAO.create_dish(submenu_id, title=title, description=description, price=price)
    return status.HTTP_201_CREATED


@router.get("/api/v1/menus/{menu_id}/submenus/{submenu_id}/dishes")
async def get_dishes(menu_id: str, submenu_id: str):
    dishes = await DishDAO.get_dishes(submenu_id)
    return dishes
