from fastapi import APIRouter, Body, Depends

from app.controller.auth import AuthController
from app.entity.auth import AuthInfoInResponse, SignupRequest, LoginRequest

router = APIRouter()


@router.post("/register", response_model=AuthInfoInResponse)
def register(payload: SignupRequest = Body(...), auth_controller: AuthController = Depends(AuthController)):
    response = auth_controller.register(payload=payload)
    return response


@router.post("/login", response_model=AuthInfoInResponse)
def login(payload: LoginRequest = Body(...), auth_controller: AuthController = Depends(AuthController)):
    response = auth_controller.login(payload=payload)
    return response
