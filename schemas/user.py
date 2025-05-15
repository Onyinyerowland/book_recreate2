from pydantic import BaseModel, EmailStr
from uuid import UUID
from typing import Optional, Any


class UserBase(BaseModel):
    name: str
    email: EmailStr
    age: int


class UserCreate(UserBase):
    pass


class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    age: Optional[int] = None


class User(UserBase):
    id: UUID


class Response(BaseModel):
    message: str
    data: Optional[Any] = None
