from uuid import UUID
import pytest
from fastapi import APIRouter, HTTPException, Response
from services.user import user_service
from schemas.user import Response, UserCreate, UserUpdate

user_router = APIRouter()

@user_router.get("")
def get_users():
    return user_service.get_all_users()

@user_router.get("/{id}")
def get_user_by_id(id: UUID):
    user = user_service.get_user_by_id(id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")
    return user

@user_router.post("")
def add_user(user_in: UserCreate):
    user = user_service.create_user(user_in)
    return Response(message="User created successfully", data=user)

@user_router.put("/{id}")
def update_user(id: UUID, user_in: UserUpdate):
    user = user_service.update_user(id, user_in)
    if not user:
        raise HTTPException(status_code=404, detail="User not found.")
    return Response(message="User updated successfully", data=user)

@user_router.delete("/{id}")
def delete_user(id: UUID):
    deleted = user_service.delete_user(id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found.")
    return Response(message="User deleted successfully")










