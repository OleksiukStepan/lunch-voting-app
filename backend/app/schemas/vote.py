from datetime import date

from pydantic import BaseModel


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
