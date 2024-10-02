from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class DynamicFields(Base):
    __tablename__ = 'dynamic_fields'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True, unique=True)
    field_name = Column(String(255), index=True, nullable=False)
    type_value = Column(String(20), nullable=False)
    entity_id = Column(Integer, ForeignKey('dynamic_entities.id'), nullable=False)

    entity = relationship("DynamicEntity", back_populates="fields", foreign_keys="DynamicFields.entity_id")
 