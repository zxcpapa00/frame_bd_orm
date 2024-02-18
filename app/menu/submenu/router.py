from typing import List

from fastapi import APIRouter
from fastapi.exceptions import HTTPException

from app.menu.submenu.dao import SubMenuDAO
from app.menu.submenu.schemas import SSubMenu, CreateSSubMenu, UpdateSSubMenu

router = APIRouter(
    prefix="/api/v1/menus",
    tags=["Подменю"]
)


@router.get("/{menu_id}/submenus", status_code=200)
async def get_submenus(menu_id: str) -> List[SSubMenu]:
    submenus = await SubMenuDAO.find_all_submenu_for_menu(menu_id)
    return submenus


@router.post("/{menu_id}/submenus", status_code=201, response_model=SSubMenu)
async def create_submenu(menu_id, data: CreateSSubMenu):
    submenu = await SubMenuDAO.create_submenu_for_menu(
        menu_id=menu_id,
        title=data.title,
        description=data.description
    )
    return submenu


@router.get("/{menu_id}/submenus/{submenu_id}", status_code=200, response_model=SSubMenu)
async def get_submenu_by_id(menu_id: str, submenu_id: str):
    submenu = await SubMenuDAO.get_submenu(menu_id, submenu_id)
    if not submenu:
        raise HTTPException(status_code=404, detail="submenu not found")
    return submenu


@router.patch("/{menu_id}/submenus/{submenu_id}", status_code=200, response_model=SSubMenu)
async def update_submenu_by_id(menu_id: str, submenu_id: str, data: UpdateSSubMenu):
    submenu = await SubMenuDAO.update_by_id(
        submenu_id,
        title=data.title,
        description=data.description
    )
    return submenu
