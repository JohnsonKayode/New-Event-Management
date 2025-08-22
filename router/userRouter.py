from database import user_db
from schema.userSchema import UserSchema, UpdateUserSchema
from fastapi import APIRouter, HTTPException
from uuid import UUID
from services.userServices import Service_user


user_router = APIRouter()

@user_router.get("/user")
def get_all_users():
    all_user = Service_user.get_all_users()
    return all

@user_router.get("/user/{id}")
def get_user_by_id(id: UUID):
    userId = Service_user.get_user_by_id(id)

    if id not in user_db:
        return f"This user does not exist"
    user_details = user_db[id]
    return user_details


@user_router.post("/user")
def createUser(user: UserSchema):
    userCreate = Service_user.create_user(user)

    if user.id in user_db:
        return f"This user exists in the Database"
    
    id = user.id = len(user_db) + 1
    details = user.model_dump()

    user_db.update({id: details})
    return {
        "message" : "Usser created successfully",
        "details" : details
    }


@user_router.put("/user/{id}/status")
def updateUser(id: UUID, user: UpdateUserSchema):
    userUpdate = Service_user.update_user(id, user)

    if id not in user_db:
        return f"This User does not exist"
    user_db[id].update(user.model_dump(exclude_unset=True))
    details = user_db[id]
    return {
        "message" : "User Updated successfully",
        "details" : details
    }
    
@user_router.delete("/user/{id}")
async def deleteUser(id: UUID):
    if id not in user_db:
        return f"This user does not exist"
    
    details = user_db.pop(id)
    return {
        "message" : "this user is not deleted",
        "details" : details
    }

