from datetime import date

from pydantic import BaseModel

from backend.app.schemas.menu import MenuSchema


class VoteBase(BaseModel):
    user_id: int
    menu_id: int


class VoteCreate(VoteBase):
    pass


class VoteSchema(VoteBase):
    id: int
    created_at: date
    menu: MenuSchema

    class Config:
        orm_mode = True
