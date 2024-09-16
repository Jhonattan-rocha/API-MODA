from pydantic import BaseModel, Field
from typing import Optional, Annotated
from app.schemas.DefaultSchemas.userProfileSchema import UserProfile


class UserBase(BaseModel):
    lang: str
    name: str
    email: str
    password: Optional[str] = ""
    salt: Optional[str] = ""
    auth_token: Optional[str] = ""
    profile_id: Optional[int] = None


class UserCreate(UserBase):
    id: int


class User(UserBase):
    id: int
    password: Optional[str] = Field(exclude=True)
    salt: Optional[str] = Field(exclude=True)
    auth_token: Optional[str] = Field(exclude=True)
    profile: Optional["UserProfile"]

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True
