from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class ProductCategory(Base):
    __tablename__ = "product_categories"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_prod = Column(Integer, ForeignKey('products.id', ondelete='CASCADE'), nullable=True)
    id_cat = Column(Integer, ForeignKey("categories.id", ondelete='CASCADE'), nullable=True)

    category = relationship("Category", foreign_keys="ProductCategory.id_cat", lazy='joined')
    product = relationship("Product", foreign_keys="ProductCategory.id_prod", lazy='joined')
