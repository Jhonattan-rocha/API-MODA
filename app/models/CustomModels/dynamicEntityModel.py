from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class DynamicEntity(Base):
    __tablename__ = 'dynamic_entities'

    id = Column(String, primary_key=True, index=True)
    entity_name = Column(String(255), index=True, unique=True, nullable=False)
    
    fields = relationship(
        "DynamicFields", 
        back_populates="entity", 
        cascade='all, delete-orphan',
        passive_deletes=True
    )

