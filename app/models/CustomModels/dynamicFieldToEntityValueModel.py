from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base
from sqlalchemy.orm import relationship


class DynamicFieldToEntityValue(Base):
    __tablename__ = 'dynamic_field_to_entity_value'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    entity_id = Column(String, ForeignKey('dynamic_entities.id', ondelete='CASCADE'), nullable=False)
    entity_id_instance = Column(String, nullable=False)
    field_id = Column(Integer, ForeignKey('dynamic_fields.id', ondelete='CASCADE'), nullable=False)
    value = Column(String(255), nullable=True)
    
    # Relacionamento reverso com DynamicFields
    field = relationship("DynamicFields", back_populates="values")
