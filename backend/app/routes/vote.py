from datetime import date

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import func
from sqlalchemy.orm import Session

from backend.app.database.models import Vote, Menu, User
from backend.app.database.session import get_db
from backend.app.schemas.vote import VoteSchema, VoteCreate
from backend.app.utils.dependencies import get_current_user

router = APIRouter()


@router.get("/", response_model=list[VoteSchema])
def get_today_votes(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    votes = db.query(Vote).filter(Vote.created_at == date.today()).all()

    for vote in votes:
        vote.menu = db.query(Menu).filter(Menu.id == vote.menu_id).first()

    return votes


@router.post("/", response_model=VoteCreate)
def vote_for_menu(vote_data: VoteCreate, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    vote = db.query(Vote).filter(
        Vote.user_id == vote_data.user_id, Vote.menu_id == vote_data.menu_id
    ).first()

    if vote:
        raise HTTPException(status_code=400, detail="User has already voted")

    vote = Vote(user_id=vote_data.user_id, menu_id=vote_data.menu_id)
    db.add(vote)
    db.commit()
    db.refresh(vote)

    return vote


@router.get("/results/", response_model=list[list])
def get_voting_results(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    results = (
        db.query(Menu.dish, func.count(Vote.id))
        .join(Vote, Menu.id == Vote.menu_id)
        .filter(Vote.created_at == date.today())
        .group_by(Menu.dish)
        .all()
    )

    return results
