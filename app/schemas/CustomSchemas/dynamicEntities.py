from pydantic import BaseModel, Field
from typing import List, Optional
from app.schemas.CustomSchemas.dynamicFields import DynamicFields
import uuid

def get_uuid():
    return str(uuid.uuid4())

class DynamicEntityBase(BaseModel):
    id: str = Field(default_factory=get_uuid)
    entity_name: str
    is_page: bool


class DynamicEntityCreate(DynamicEntityBase):
    pass


class DynamicEntity(DynamicEntityBase):
    fields: List[Optional["DynamicFields"]]

    class Config:
        orm_mode: True
        from_attributes: True
        arbitrary_types_allowed: True
