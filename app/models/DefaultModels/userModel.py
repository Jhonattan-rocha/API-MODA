from sqlalchemy import Column, Integer, String, ForeignKey,Boolean
from sqlalchemy.orm import relationship
from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), default="")
    email = Column(String(255), default="")
    lang = Column(String(10), default="pt")
    password = Column(String(255), nullable=False, default=0)
    salt = Column(String(255), default="")
    auth_token = Column(String(255), default="")
    profile_id = Column(Integer, ForeignKey("user_profile.id"), nullable=True)

    profile = relationship("UserProfile")
