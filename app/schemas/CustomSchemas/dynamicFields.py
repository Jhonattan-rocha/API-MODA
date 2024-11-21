from pydantic import BaseModel


class DynamicFieldsBase(BaseModel):
    field_name: str
    type_value: str
    entity_id: str
    entity_rel: str
    field_entity_rel: str
    rules: str = ""
    required: bool = False
    readOnly: bool = False
    disabled: bool = False


class DynamicFieldsCreate(DynamicFieldsBase):
    pass


class DynamicFields(DynamicFieldsBase):
    id: int

    class Config:
        orm_mode: True
        from_attributes: True
        arbitrary_types_allowed: True
