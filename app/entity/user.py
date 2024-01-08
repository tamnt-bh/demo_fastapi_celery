from typing import Optional

from pydantic import EmailStr, ConfigDict, field_validator, BaseModel

from app.entity.base import BaseEntity, PyObjectId


def transform_email(email: str) -> str:
    return email.lower()


class UserBase(BaseEntity):
    email: EmailStr
    fullname: str
    _extract_email = field_validator("email", mode="before")(transform_email)


class UserInDB(UserBase):
    model_config = ConfigDict(from_attributes=True)
    password: Optional[str]
    id: Optional[PyObjectId] = None


class UserInCreate(UserBase):
    password: str

    @field_validator("password")
    def validate_min_length(cls, value):
        if len(value) < 8:
            raise ValueError(f"Password must be at least 8 characters")
        return value


class UserInUpdate(BaseModel):
    email: Optional[EmailStr] = None
    fullname: Optional[str] = None


class User(UserBase):
    id: str
