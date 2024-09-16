from pydantic import BaseModel
from typing import List, Optional
from app.schemas.CustomSchemas.dynamicFields import DynamicFields


class DynamicEntityBase(BaseModel):
    entity_name: str


class DynamicEntityCreate(DynamicEntityBase):
    pass


class DynamicEntity(DynamicEntityBase):
    id: int
    fields: List[Optional["DynamicFields"]]

    class Config:
        orm_mode: True
        from_attributes: True
        arbitrary_types_allowed: True
