from sqlalchemy.orm import relationship
from datetime import datetime
from sqlalchemy import String, Integer, Float, Column, DateTime, ForeignKey
from app.database import Base


class InputOutputStock(Base):
    __tablename__ = "input_output_stock"

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    type = Column(String(1), index=True, nullable=False)
    qtd = Column(Float, nullable=False)
    date = Column(DateTime, nullable=False, default=datetime.now())
