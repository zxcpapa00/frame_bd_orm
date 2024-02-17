import uuid
from typing import Optional, List

from fastapi import APIRouter, HTTPException, status

from app.menu.dao import MenuDAO
from app.menu.schemas import SMenu, SMenuCreate, SMenuUpdate

router = APIRouter(
    prefix="/api/v1/menus",
    tags=["Меню"]
)


@router.get("/")
async def get_all_menu() -> List[SMenu]:
    menus = await MenuDAO.find_all()
    return menus


@router.post("/", status_code=201)
async def create_menu(menu_data: SMenuCreate) -> SMenu:
    menu = await MenuDAO.add(title=menu_data.title, description=menu_data.description)
    return menu


@router.get("/{menu_id}", status_code=200)
async def get_menu_by_id(menu_id: str):
    menu = await MenuDAO.find_by_id(menu_id)
    if not menu:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="menu not found")
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
