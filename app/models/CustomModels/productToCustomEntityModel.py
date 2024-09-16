from sqlalchemy import Integer, Column, ForeignKey
from app.database import Base


class ProductToCustomEntity(Base):
    __tablename__ = "product_to_custom_entity"

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    entity_id = Column(Integer, ForeignKey('dynamic_entities.id'), nullable=False)
