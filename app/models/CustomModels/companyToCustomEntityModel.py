from sqlalchemy import Integer, Column, ForeignKey
from app.database import Base


class CompanyToCustomEntity(Base):
    __tablename__ = "company_to_custom_entity"

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    company_id = Column(Integer, ForeignKey('companies.id'), nullable=False)
    entity_id = Column(Integer, ForeignKey('dynamic_entities.id'), nullable=False)
