from sqlalchemy import Integer, Column, ForeignKey
from app.database import Base


class CustomEntityToCustomEntity(Base):
    __tablename__ = "custom_entity_to_custom_entity"

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    entity_id_1 = Column(Integer, ForeignKey('dynamic_entities.id'), nullable=False)
    entity_id_2 = Column(Integer, ForeignKey('dynamic_entities.id'), nullable=False)
