import uuid

from pydantic import ConfigDict, BaseModel


class SSubMenu(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    title: str
    description: str
    dishes_count: int


class CreateSSubMenu(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    title: str
    description: str
