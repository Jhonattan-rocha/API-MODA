from sqlalchemy.orm import relationship
from sqlalchemy import String, Integer, Float, Column, ForeignKey, Boolean
from app.database import Base


class Employees(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    id_emp = Column(Integer, ForeignKey('companies.id'), nullable=True)
    name = Column(String(150), index=True)
    cpf = Column(String(20), index=True)
    tel = Column(String(20))
    email = Column(String(100), unique=True, index=True)
    address = Column(String(200))

    company = relationship("Company", back_populates="employees")
