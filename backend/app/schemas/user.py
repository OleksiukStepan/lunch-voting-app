from typing import Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    username: str

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    password: str


class UserSchema(UserBase):
    id: int
    fullname: Optional[str] = None

    class Config:
        orm_mode = True
