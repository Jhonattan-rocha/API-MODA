from sqlalchemy import Integer, Column, ForeignKey
from app.database import Base


class SubCategoryToCustomEntity(Base):
    __tablename__ = "subcategory_to_custom_entity"

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    subcategory_id = Column(Integer, ForeignKey('subcategories.id'), nullable=False)
    entity_id = Column(Integer, ForeignKey('dynamic_entities.id'), nullable=False)
