from fastapi import FastAPI, HTTPException
from fastapi import APIRouter
from router.eventRouter import event_router
from router.userRouter import user_router


app = FastAPI()


app.include_router(user_router)
app.include_router(event_router)

@app.get("/")
def mainHome():
    return {"message": "Welcome to the Event Management API"}

