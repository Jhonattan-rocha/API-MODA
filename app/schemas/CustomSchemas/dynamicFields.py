from pydantic import BaseModel


class DynamicFieldsBase(BaseModel):
    field_name: str
    type_value: str
    entity_id: int


class DynamicFieldsCreate(DynamicFieldsBase):
    pass


class DynamicFields(DynamicFieldsBase):
    id: int

    class Config:
        orm_mode: True
        from_attributes: True
        arbitrary_types_allowed: True
