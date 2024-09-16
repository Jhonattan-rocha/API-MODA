from pydantic import BaseModel
from typing import List, Optional


class DynamicFieldToEntityValueBase(BaseModel):
    entity_id: int
    entity_id_instance: str
    field_id: int
    value: str


class DynamicFieldToEntityValueCreate(DynamicFieldToEntityValueBase):
    pass


class DynamicFieldToEntityValue(DynamicFieldToEntityValueBase):
    id: int

    class Config:
        orm_mode: True
        from_attributes: True
        arbitrary_types_allowed: True
