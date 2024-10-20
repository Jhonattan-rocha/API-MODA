from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class DynamicFields(Base):
    __tablename__ = 'dynamic_fields'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True, unique=True)
    field_name = Column(String(255), index=True, nullable=False)
    type_value = Column(String(20), nullable=False)
    entity_rel = Column(String, nullable=True, default="")
    field_entity_rel = Column(String, nullable=True, default="")
    rules = Column(String(255), nullable=True, default="")
    entity_id = Column(String, ForeignKey('dynamic_entities.id', ondelete='CASCADE'), nullable=False)
    
    entity = relationship("DynamicEntity", back_populates="fields")
    
    values = relationship(
        "DynamicFieldToEntityValue",
        back_populates="field",
        cascade='all, delete-orphan',
        passive_deletes=True
    )
