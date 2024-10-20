import re

from pydantic import BaseModel, field_validator


class PersonBase(BaseModel):
    name: str
    cpf: str
    tel: str
    email: str

    @field_validator('cpf')
    def cpf_cnpj_check(cls, v):
        if not (11 <= len(v) <= 14):
            raise ValueError('CPF must be between 11 and 14 characters')
        if not re.match(r'^\d{11}$', v):
            raise ValueError('CPF must only consist of numbers')
        return v

    @field_validator('tel')
    def tel_check(cls, v):
        if not re.match(r'^\d+$', v):
            raise ValueError('Telephone must only be made up of numbers')
        return v


class PersonCreate(PersonBase):
    id: int


class Person(PersonBase):
    id: int

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True
