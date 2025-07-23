from database import user_db
from schema.userSchema import UserSchema, UpdateUserSchema
from fastapi import APIRouter, HTTPException
from uuid import UUID


user_router = APIRouter()

@user_router.get("/user")
def get_all_users():
    return user_db

@user_router.post("/user")
def createUser(user: UserSchema):
    if user.id in user_db:
        return f"This user Exists in the Database"
    
    id = user.id = len(user_db) + 1
    details = user.model_dump()

    user_db.update({id: details})
    return {
        "message" : "Usser created successfully",
        "details" : details
    }


@user_router.patch("/user/{id}/status")
def updateUser(id: int, user: UpdateUserSchema):
    if user.id not in user_db:
        return f"This User doess not exist"
    
    details = user_db[id] = user.model_dump()
    user_db.update({id: details})
    return {
        "message" : "User Updated successfully",
        "details" : details
    }
    

