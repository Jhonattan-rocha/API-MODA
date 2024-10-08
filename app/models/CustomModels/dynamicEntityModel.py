from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base
from sqlalchemy.orm import relationship


class DynamicEntity(Base):
    __tablename__ = 'dynamic_entities'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    entity_name = Column(String(255), index=True, unique=True, nullable=False)
    is_page = Column(Boolean, default=False, nullable=False)
    fields = relationship("DynamicFields", back_populates="entity")
