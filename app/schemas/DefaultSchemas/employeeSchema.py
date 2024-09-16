import re
from pydantic import BaseModel, field_validator


class EmployeesBase(BaseModel):
    id_emp: int
    name: str
    cpf: str
    tel: str
    email: str
    address: str

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


class EmployeesCreate(EmployeesBase):
    id: int


class Employees(EmployeesBase):
    id: int

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True
