from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from app.database import Base
from sqlalchemy.orm import relationship


class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), index=True)
    social_reason = Column(String(100), index=True)
    cnpj = Column(String(20), index=True)
    tel = Column(String(20))
    email = Column(String(100), unique=True, index=True)
    address = Column(String(200))

    employees = relationship("Employees", back_populates="company")
