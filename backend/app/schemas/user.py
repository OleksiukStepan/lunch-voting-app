from typing import Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    username: str

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    firstname: str
    lastname: str
    password: str


class UserSchema(UserBase):
    id: int
    fullname: Optional[str] = None

    class Config:
        orm_mode = True


class UserLogin(UserBase):
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str
