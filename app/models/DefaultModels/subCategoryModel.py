from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.database import Base


class SubCategory(Base):
    __tablename__ = "subcategories"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True)
    id_cat = Column(Integer, ForeignKey('categories.id'), nullable=True)

    category = relationship("Category", back_populates="subcategories", foreign_keys="SubCategory.id_cat", lazy='joined')
