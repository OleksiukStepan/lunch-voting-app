from datetime import date
from typing import Optional

from pydantic import BaseModel


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
