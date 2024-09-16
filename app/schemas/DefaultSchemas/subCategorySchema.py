from pydantic import BaseModel


class SubCategoryBase(BaseModel):
    name: str
    id_cat: int


class SubCategoryCreate(SubCategoryBase):
    id: int


class SubCategory(SubCategoryBase):
    id: int

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True
