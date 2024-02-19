import uuid
from typing import Optional

from pydantic import ConfigDict, BaseModel


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

    title: Optional[str]
    description: Optional[str]


class SubmenuDetail(SSubMenu):
    dishes_count: int
