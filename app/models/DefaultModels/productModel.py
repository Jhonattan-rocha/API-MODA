from sqlalchemy import Column, Integer, String, Float, Boolean
from sqlalchemy.orm import relationship
from app.database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, default="")
    description = Column(String, default="")
    price = Column(Float, nullable=False, default=0)

#    product_categories = relationship("ProductCategory", back_populates="product", foreign_keys="ProductCategory.id_prod")
