from pydantic import BaseModel


class UserSchema(Basemodel):
    id: int
    name: str
    email: str
    is_active: bool = True

class UpdateUserSchema(BaseModel):
    name: str | None = None
    email: str | None = None
    is_active: bool | None = None