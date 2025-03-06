from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.app.database.models import User
from backend.app.database.session import get_db
from backend.app.schemas.user import UserCreate, UserSchema

router = APIRouter()


@router.post("/", response_model=UserCreate)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.get("/", response_model=list[UserSchema])
def get_all_users(db: Session = Depends(get_db)):
    return db.query(User).all()
