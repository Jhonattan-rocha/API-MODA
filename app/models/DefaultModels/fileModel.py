from sqlalchemy import Column, Integer, String, Text
from app.database import Base

class File(Base):
    __tablename__ = "files"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, index=True)
    content_type = Column(String)
    description = Column(Text, nullable=True)
    file_path = Column(String)
