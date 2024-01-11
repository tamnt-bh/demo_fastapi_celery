from typing import Any

from app.entity.user import User, UserInDB
from app.models.user import UserModel


def chunk_list(lst: list, chunk_size: int):
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]


def convert_type_user(users: list[UserModel]) -> list[dict[str, Any]]:
    return [User(**UserInDB.model_validate(user).model_dump()).model_dump() for user in users]
