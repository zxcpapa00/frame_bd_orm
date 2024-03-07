from typing import List

from fastapi import APIRouter, HTTPException, status

from app.menu.dao import MenuDAO
from app.menu.schemas import SMenu, SMenuCreate, SMenuUpdate, SMenuDetail, SMenuAll

router = APIRouter(
    prefix="/api/v1/menus",
    tags=["Меню"]
)


@router.get("", status_code=200)
async def get_all_menu() -> List[SMenu]:
    menus = await MenuDAO.find_all()
    return menus


@router.get("/all")
async def get_menus() -> List[SMenuAll]:
    menus = await MenuDAO.get_menus_with_submenus_and_dishes()
    return menus


@router.post("", status_code=201)
async def create_menu(menu_data: SMenuCreate) -> SMenu:
    menu = await MenuDAO.add(title=menu_data.title, description=menu_data.description)
    return menu


@router.get("/{menu_id}", status_code=200)
async def get_menu_by_id(menu_id: str) -> SMenuDetail:
    menu = await MenuDAO.get_menu_with_arg(menu_id)
    return menu


@router.delete("/{menu_id}", status_code=200)
async def delete_menu_by_id(menu_id: str):
    await MenuDAO.delete_by_id(menu_id)


@router.patch("/{menu_id}")
async def update_menu_by_id(menu_id: str, data: SMenuUpdate) -> SMenu:
    menu = await MenuDAO.update_by_id(menu_id, title=data.title, description=data.description)
    if not menu:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="menu not found")
    return menu
