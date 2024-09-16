from sqlalchemy import Integer, Column, ForeignKey
from app.database import Base


class UserToCustomEntity(Base):
    __tablename__ = "user_to_custom_entity"

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    entity_id = Column(Integer, ForeignKey('dynamic_entities.id'), nullable=False)
