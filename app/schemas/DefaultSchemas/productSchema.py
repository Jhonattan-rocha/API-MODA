from typing import List, Optional
from pydantic import BaseModel, field_validator


class ProductBase(BaseModel):
    name: str
    description: str
    price: float

    @field_validator('price')
    def price_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError('Price must be positive')
        return v

    @field_validator('name')
    def name_must_not_be_empty(cls, v):
        if not v.strip():
            raise ValueError('Name must not be empty')
        return v


class ProductCreate(ProductBase):
    id: int


class Product(ProductBase):
    id: int

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True
