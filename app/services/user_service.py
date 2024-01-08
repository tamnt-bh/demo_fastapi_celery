from typing import Optional

from mongoengine import QuerySet, DoesNotExist

from app.entity.user import UserInCreate
from app.models.user import UserModel


class UserService:
    def __init__(self):
        pass

    def create(self, user: UserInCreate) -> UserModel:
        new_user = UserModel(**user.model_dump())
        new_user.save()
        return new_user

    def get_by_email(self, email: str) -> Optional[UserModel]:
        qs: QuerySet = UserModel.objects(email=email)
        try:
            user: UserModel = qs.get()
            return user
        except DoesNotExist:
            return None
