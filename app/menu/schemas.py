import uuid

from pydantic import BaseModel, ConfigDict

from app.menu.submenu.schemas import SubmenuWDishes


class SMenu(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    title: str
    description: str


class SMenuCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    title: str
    description: str


class SMenuUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    title: str | None
    description: str | None


class SMenuDetail(SMenu):
    submenus_count: int
    dishes_count: int


class SMenuAll(SMenu):
    id: uuid.UUID | str | None
    submenus: list[SubmenuWDishes]
