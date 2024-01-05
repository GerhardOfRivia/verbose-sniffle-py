from typing import Optional, Union

from pydantic import BaseModel


class UserBase(BaseModel):
    email: str


class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True


class TaskBase(BaseModel):
    user: int
    subject: str
    complete: bool = False


class Task(TaskBase):
    id: int
    created: int
    modified: Optional[int]

    class Config:
        orm_mode = True

