import uuid

from pydantic import BaseModel, ConfigDict, condecimal


class CreateSDish(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    title: str
    description: str
    price: condecimal(ge=0, decimal_places=2)


class SDish(CreateSDish):

    id: uuid.UUID
