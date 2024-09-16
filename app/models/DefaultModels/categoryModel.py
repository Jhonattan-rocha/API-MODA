from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base
from sqlalchemy.orm import relationship


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True)
#    categories_products = relationship("ProductCategory", back_populates="category", foreign_keys="ProductCategory.id_cat")
    subcategories = relationship("SubCategory", back_populates="category", lazy='joined')
