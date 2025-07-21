from fastapi import FastAPI, HTTPException
from fastapi import APIRouter
from router.userRouter import user_router


app = FastAPI()


include_router = APIRouter(user_router)

@app.get("/")
def mainHome():
    return {"message": "Welcome to the Event Management API"}

