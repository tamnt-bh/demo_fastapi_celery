from fastapi import Depends, HTTPException, status
from mongoengine import NotUniqueError

from app.controller.security import get_password_hash, create_access_token, verify_password
from app.entity.auth import TokenData, AuthInfoInResponse, LoginRequest
from app.entity.user import UserInCreate, User, UserInDB
from app.models.user import UserModel
from app.services.user_service import UserService
from app.utils.error_exception import system_exception
from celery_worker.tasks import send_email_register_success


class AuthController:
    def __init__(
            self,
            user_service: UserService = Depends(UserService),
    ):
        self.user_service = user_service

    def register(self, payload: UserInCreate):
        obj_in: UserInCreate = UserInCreate(**payload.model_dump(exclude=({"password"})),
                                            password=get_password_hash(payload.password))

        try:
            user: UserModel = self.user_service.create(user=obj_in)

            send_email_register_success.delay(to_email=user.email, fullname=user.fullname)

            access_token = create_access_token(
                data=TokenData(email=user.email, id=str(user.id))
            )
            return AuthInfoInResponse(access_token=access_token,
                                      user=User(**UserInDB.model_validate(user).model_dump()))
        except NotUniqueError:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="This email existed already",
            )
        except Exception as e:
            print("Error>>>", e)
            raise system_exception

    def login(self, payload: LoginRequest):
        user: UserModel = self.user_service.get_by_email(payload.email)

        checker = False
        if user:
            checker = verify_password(payload.password, user.password)

        if not user or not checker:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password",
                headers={"WWW-Authenticate": "Bearer"},
            )

        access_token = create_access_token(
            data=TokenData(email=user.email, id=str(user.id))
        )
        return AuthInfoInResponse(access_token=access_token,
                                  user=User(**UserInDB.model_validate(user).model_dump()))
