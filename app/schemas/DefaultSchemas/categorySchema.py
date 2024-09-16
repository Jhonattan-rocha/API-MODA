from pydantic import BaseModel
from typing import List, Optional
from app.schemas.DefaultSchemas.subCategorySchema import SubCategory


class CategoryBase(BaseModel):
    name: str


class CategoryCreate(CategoryBase):
    id: int


class Category(CategoryBase):
    id: int
    subcategories: List[Optional['SubCategory']]

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True
