from pydantic import BaseModel


class RestaurantBase(BaseModel):
    name: str


class RestaurantCreate(RestaurantBase):
    pass


class RestaurantSchema(RestaurantBase):
    id: int

    class Config:
        orm_mode = True
