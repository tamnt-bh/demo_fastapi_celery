from datetime import timedelta, datetime
from typing import Optional

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext

from app.entity.auth import TokenData
from app.models.user import UserModel
from app.services.user_service import UserService
from app.utils.error_exception import credentials_exception
from common.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def verify_token(token: str) -> Optional[TokenData]:
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        email: str = payload.get("email")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email, id=payload.get("id"))
        return token_data
    except JWTError:
        raise credentials_exception


def get_password_hash(password):
    return pwd_context.hash(password)


def get_current_user(
        token: str = Depends(oauth2_scheme),
        user_service: UserService = Depends(UserService),
) -> UserModel:
    token_data = verify_token(token=token)
    user: UserModel = user_service.get_by_email(email=token_data.email)
    if user is None:
        raise credentials_exception
    return user


def create_access_token(data: TokenData, expires_delta: timedelta = None) -> str:
    to_encode = data.model_dump()

    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(days=settings.ACCESS_TOKEN_EXPIRE)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

    if isinstance(encoded_jwt, str):
        return encoded_jwt
    else:
        return encoded_jwt.decode("utf-8")
