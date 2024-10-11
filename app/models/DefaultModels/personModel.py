from sqlalchemy import Column, Integer, String
from app.database import Base
from sqlalchemy.orm import relationship


class Person(Base):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), index=True)
    cpf = Column(String(20), index=True)
    tel = Column(String(20))
    email = Column(String(100), unique=True, index=True)
