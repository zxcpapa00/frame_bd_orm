from pydantic import BaseModel, ConfigDict
import uuid


class SMenu(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    title: str
    description: str


