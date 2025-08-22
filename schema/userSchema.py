from pydantic import BaseModel
from uuid import UUID
from typing import Optional


class UserSchema(BaseModel):
    id: UUID
    name: str
    email: str
    is_active: bool = True

class UpdateUserSchema(BaseModel):
    id: UUID 
    name: Optional[str] = None
    email: Optional[str] = None
    is_active: Optional[bool] = None