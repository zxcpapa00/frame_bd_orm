from typing import Optional

from pydantic import BaseModel, ConfigDict
import uuid


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

    title: Optional[str]
    description: Optional[str]


class SMenuDetail(SMenu):

    submenus_count: int
    dishes_count: int
