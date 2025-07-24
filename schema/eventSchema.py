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
    title: Optional[str]
    location: Optional[str]
    date: Optional[str]
    is_open: Optional[bool] = True