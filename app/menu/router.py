import uuid
from typing import Optional, List

from fastapi import APIRouter

from app.menu.dao import MenuDAO
from app.menu.schemas import SMenu

router = APIRouter(
    prefix="/api/v1/menus",
    tags=["Меню"]
)


@router.get("/")
async def get_all_menu() -> List[SMenu]:
    menus = await MenuDAO.find_all()
    return menus


@router.post("/", status_code=201)
async def create_menu(title: str, description: str) -> SMenu:
    asd = await MenuDAO.add(title=title, description=description)
    return asd


@router.get("/{menu_id}")
async def get_menu_by_id(menu_id: str):
    menu = await MenuDAO.find_by_id(menu_id)
    return menu


@router.delete("/{menu_id}", status_code=200)
async def delete_menu_by_id(menu_id: uuid.UUID):
    await MenuDAO.delete_by_id(menu_id)


@router.put("/{menu_id}")
async def update_menu_by_id(menu_id: uuid.UUID, title: Optional[str], description: Optional[str]):
    return await MenuDAO.update_by_id(menu_id, title=title, description=description)
