import uuid

from pydantic import ConfigDict, BaseModel


class SchemaSubMenu(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    title: str
    description: str
    dishes_count: int
