from typing import List

from fastapi import APIRouter

from app.menu.submenu.dao import SubMenuDAO
from app.menu.submenu.schemas import SSubMenu, CreateSSubMenu

router = APIRouter(
    prefix="/api/v1/menus",
    tags=["Подменю"]
)


@router.get("/{menu_id}/submenus", status_code=200)
async def get_submenus(menu_id: str) -> List[SSubMenu]:
    submenus = await SubMenuDAO.find_all_submenu_for_menu(menu_id)
    return submenus


@router.post("/{menu_id}/submenus", status_code=201)
async def create_submenu(menu_id, data: CreateSSubMenu):
    submenu = await SubMenuDAO.create_submenu_for_menu(
        menu_id=menu_id,
        title=data.title,
        description=data.description
    )
    return submenu
