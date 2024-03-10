from typing import List

from fastapi import APIRouter, HTTPException, status
from fastapi_cache.decorator import cache
from pydantic import EmailStr
from pydantic.v1 import parse_obj_as

from app.menu.dao import MenuDAO
from app.menu.schemas import (SMenu, SMenuAll, SMenuCreate, SMenuDetail,
                              SMenuUpdate)
from app.tasks.tasks import send_email

router = APIRouter(
    prefix='/api/v1/menus',
    tags=['Меню']
)


@router.get('', status_code=200)
async def get_all_menu() -> list[SMenu]:
    menus = await MenuDAO.find_all()
    return menus


@router.get('/all')
@cache(expire=30)
async def get_menus() -> list[SMenuAll]:
    menus = await MenuDAO.get_menus_with_submenus_and_dishes()
    return menus


@router.get('/menus_on_email/{menu_id}')
async def get_menus_on_email(menu_id: str, email: EmailStr):
    menu = await MenuDAO.find_by_id(menu_id)
    menu_dict = dict(menu)
    send_email.delay(menu_dict, email)
    return f"Меню был отправлено на вашу почту: {email}"


@router.post('', status_code=201)
async def create_menu(menu_data: SMenuCreate) -> SMenu:
    menu = await MenuDAO.add(title=menu_data.title, description=menu_data.description)
    return menu


@router.get('/{menu_id}', status_code=200)
async def get_menu_by_id(menu_id: str) -> SMenuDetail:
    menu = await MenuDAO.get_menu_with_arg(menu_id)
    return menu


@router.delete('/{menu_id}', status_code=200)
async def delete_menu_by_id(menu_id: str):
    await MenuDAO.delete_by_id(menu_id)


@router.patch('/{menu_id}')
async def update_menu_by_id(menu_id: str, data: SMenuUpdate) -> SMenu:
    menu = await MenuDAO.update_by_id(menu_id, title=data.title, description=data.description)
    if not menu:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='menu not found')
    return menu
