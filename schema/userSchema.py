from pydantic import BaseModel

from typing import Optional


class UserSchema(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True

class UpdateUserSchema(BaseModel):
    id: int
    name: Optional[str]
    email: Optional[str]
    is_active: Optional[bool]