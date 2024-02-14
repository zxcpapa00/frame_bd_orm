from typing import List

from fastapi import APIRouter

from app.menu.submenu.dao import SubMenuDAO
from app.menu.submenu.schemas import SchemaSubMenu

router = APIRouter(
    prefix="/api/v1/menus",
    tags=["Подменю"]
)


@router.get("/{menu_id}/submenus")
async def get_submenus(menu_id: str) -> List[SchemaSubMenu]:
    submenus = await SubMenuDAO.find_all_submenu_for_menu(menu_id)
    return submenus


@router.post("/{menu_id}/submenus")
async def create_submenu(menu_id: str, title: str, description: str):
    submenus = await SubMenuDAO.create_submenu_for_menu(menu_id, title=title, description=description)
