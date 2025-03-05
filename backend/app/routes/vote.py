from datetime import date

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.app.database.models import Vote, Menu
from backend.app.database.session import get_db
from backend.app.schemas.vote import VoteSchema

router = APIRouter()


@router.get("/votes/", response_model=VoteSchema)
def get_today_votes(db: Session = Depends(get_db)):
    votes = (
        db.query(Menu, Vote).join(Vote, Vote.menu_id == Menu.id)
        .filter(Menu.date == date.today()).all()
    )
    return votes


@router.post("/vote")
def vote_for_menu(user_id: int, menu_id: int, db: Session = Depends(get_db)):
    existing_vote = db.query(Vote).filter(
        Vote.user_id == user_id, Vote.menu_id == menu_id
    ).first()

    if existing_vote:
        raise HTTPException(status_code=400, detail="User has already voted")

    vote = Vote(user_id=user_id, menu_id=menu_id)
    db.add(vote)
    db.commit()
    return vote
