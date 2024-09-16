from sqlalchemy import Integer, Column, ForeignKey
from app.database import Base


class CategoryToCustomEntity(Base):
    __tablename__ = "category_to_custom_entity"

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    entity_id = Column(Integer, ForeignKey('dynamic_entities.id'), nullable=False)
