from pydantic import BaseModel
from typing import List, Optional
from app.schemas.CustomSchemas.dynamicFields import DynamicFields

class DynamicFieldToEntityValueBase(BaseModel):
    entity_id: str
    entity_id_instance: str
    field_id: int
    value: str


class DynamicFieldToEntityValueCreate(DynamicFieldToEntityValueBase):
    pass


class DynamicFieldToEntityValue(DynamicFieldToEntityValueBase):
    id: int
    field: Optional["DynamicFields"]

    class Config:
        orm_mode: True
        from_attributes: True
        arbitrary_types_allowed: True
