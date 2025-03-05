from datetime import date
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



class RestaurantBase(BaseModel):
    name: str


class RestaurantCreate(RestaurantBase):
    pass


class RestaurantSchema(RestaurantBase):
    id: int

    class Config:
        orm_mode = True


class MenuBase(BaseModel):
    dish: str
    description: Optional[str] = None
    price: float
    date: date


class MenuCreate(MenuBase):
    restaurant_id: int


class MenuSchema(MenuBase):
    id: int
    restaurant_id: int

    class Config:
        orm_mode = True


class VoteBase(BaseModel):
    user_id: int
    menu_id: int
    created_at: date


class VoteCreate(VoteBase):
    pass


class VoteSchema(VoteBase):
    id: int

    class Config:
        orm_mode = True
