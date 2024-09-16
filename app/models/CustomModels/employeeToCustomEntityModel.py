from sqlalchemy import Integer, Column, ForeignKey
from app.database import Base


class EmployeeToCustomEntity(Base):
    __tablename__ = "employee_to_custom_entity"

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    employee_id = Column(Integer, ForeignKey('employees.id'), nullable=False)
    entity_id = Column(Integer, ForeignKey('dynamic_entities.id'), nullable=False)
