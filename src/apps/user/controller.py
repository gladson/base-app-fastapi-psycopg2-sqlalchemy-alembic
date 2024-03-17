from typing import List

from fastapi import APIRouter, Body, HTTPException

from apps.user.model import User as UserModel
from apps.user.repository import UserRepository
from apps.user.service import UserService
from core.utils.logger import Logger

router = APIRouter()
user_repository = UserRepository()
user_service = UserService(user_repository)


@router.get("/{user_id}", response_model=UserModel)
async def get_user(user_id: int):
    user = user_service.get_user(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/", response_model=UserModel)
async def create_user(user: UserModel = Body(...)):
    if user.username is None or user.email is None or user.password is None:
        raise HTTPException(
            status_code=400,
            detail="Name and email and password are required",
        )
    return user_service.create_user(
        user.username,
        user.email,
        user.password,
    )


@router.put("/{user_id}", response_model=UserModel)
async def update_user(user_id: int, user: UserModel = Body(...)):
    existing_user = user_service.get_user(user_id)
    if existing_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user_service.update_user(
        user_id,
        user.username,
        user.email,
        user.password if user.password is not None else None,
    )


@router.delete("/{user_id}", response_model=UserModel)
async def delete_user(user_id: int):
    user = user_service.delete_user(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.get("/", response_model=List[UserModel])
async def get_all_users():
    Logger("User").info("Get all users")
    return user_service.get_all_users()
