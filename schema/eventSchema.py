from pydantic import BaseModel
from typing import Optional, Union

class Event(BaseModel):
    id: int
    title: str
    location: str
    date: str
    is_open: bool = True


class UpdateEvent(BaseModel):
    id: Optional[str]
    title: Optional[str] = None
    location: Optional[str] = None
    date: Optional[str] = None
    is_open: Optional[bool] = None