from database import user_db, event_db
from schema.eventSchema import Event, UpdateEvent
from fastapi import APIRouter, HTTPException


event_router = APIRouter()


@event_router.get("/event")
async def getEvents():
    return event_db

@event_router.post("/event")
async def createEvent(event: Event):
    if event.id in event_db:
        return f"This event Already exists in the Database"
    
    event.id = len(event_db) + 1
    details = event.model_dump()

    event_db.update({event.id : details})
    return {
        "messsage" : "Event successfully created",
        "details" : details
    }

@event_router.delete("/event/{id}")
async def deleteEvent(id: int):
    if id not in event_db:
        return f"This event does not exist"
    
    details = event_db.pop(id)
    return {
        "message" : "this event no longer exists",
        "details" : details
    }
    