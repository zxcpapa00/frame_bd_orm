import uuid

from pydantic import BaseModel, ConfigDict

from app.menu.submenu.dish.schemas import SDish


class SSubMenu(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    title: str
    description: str


class CreateSSubMenu(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    title: str
    description: str


class UpdateSSubMenu(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    title: str | None
    description: str | None


class SubmenuDetail(SSubMenu):
    dishes_count: int


class SubmenuWDishes(SSubMenu):
    dishes: list[SDish]
