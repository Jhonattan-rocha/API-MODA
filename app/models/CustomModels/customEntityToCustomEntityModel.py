from sqlalchemy import Integer, Column, ForeignKey, String
from app.database import Base


class CustomEntityToEntity(Base):
    __tablename__ = "custom_entity_to_entity"

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    entity_id_1 = Column(Integer, ForeignKey('dynamic_entities.id', ondelete="CASCADE"), nullable=False)
    entity_id_2 = Column(String(255), default="user", nullable=False)
