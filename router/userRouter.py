from database import user_db
from schema.userSchema import UserSchema, UpdateUserSchema
from fastapi import APIRouter, status, HTTPException


user_router = APIRouter()

@user_router.get("/user")
def get_all_users():
    return user_db



