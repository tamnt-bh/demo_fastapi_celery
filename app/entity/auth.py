from typing import Optional

from pydantic import BaseModel, EmailStr

from app.entity.base import BaseEntity
from app.entity.user import User, UserInCreate


class Token(BaseModel):
    access_token: Optional[str] = None


class TokenData(BaseModel):
    email: str
    id: str = None


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class SignupRequest(UserInCreate):
    pass


class AuthInfoInResponse(BaseEntity, Token):
    user: User
