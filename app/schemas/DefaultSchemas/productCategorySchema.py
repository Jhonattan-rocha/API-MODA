from typing import Optional
from pydantic import BaseModel
from app.schemas.DefaultSchemas.productSchema import Product
from app.schemas.DefaultSchemas.categorySchema import Category


class ProductCategoryBase(BaseModel):
    id_prod: int
    id_cat: int


class ProductCategoryCreate(ProductCategoryBase):
    id: int


class ProductCategory(ProductCategoryBase):
    id: int
    product: Optional[Product]
    category: Optional[Category]

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True
