import re
from typing import List, Optional

from app.schemas.DefaultSchemas.employeeSchema import Employees
from pydantic import BaseModel, field_validator


class CompanyBase(BaseModel):
    name: str
    social_reason: str
    cnpj: str
    tel: str
    email: str
    address: str

    @field_validator('cnpj')
    def cpf_cnpj_check(cls, v):
        if not (11 <= len(v) <= 14):
            raise ValueError('CNPJ must be between 14 and 17 characters')
        if not re.match(r'^\d{14}$', v):
            raise ValueError('CNPJ must only consist of numbers')
        return v

    @field_validator('tel')
    def tel_check(cls, v):
        if not re.match(r'^\d+$', v):
            raise ValueError('Telephone must only be made up of numbers')
        return v


class CompanyCreate(CompanyBase):
    id: int


class Company(CompanyBase):
    id: int
    employees: List[Optional[Employees]]

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True
