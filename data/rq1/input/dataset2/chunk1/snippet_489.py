#Source: https://stackoverflow.com/questions/64236572/fastapi-typeerror-object-of-type-modelmetaclass-is-not-json-serializable
from typing import List, Optional
from pydantic import BaseModel


# Todo model
class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None

class TodoCreation(TodoBase):
    pass


class Todo(TodoBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True
        
# User model
class UserBase(BaseModel):
    username: str
    email: str

class UserCreation(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    todo: List[Todo] = []

    class Config:
        orm_mode = True