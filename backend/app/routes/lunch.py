from datetime import date

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.app.database.models import Restaurant, Menu, User, Vote
from backend.app.database.session import get_db
from backend.app.schemas.lunch import (
    RestaurantCreate,
    RestaurantBase,
    MenuCreate,
    MenuSchema,
    UserCreate,
    VoteSchema,
)

router = APIRouter()


@router.post("/restaurants/", response_model=RestaurantCreate)
def create_restaurant(restaurant: RestaurantCreate, db: Session = Depends(get_db)):
    new_restaurant = Restaurant(name=restaurant.name)
    db.add(new_restaurant)
    db.commit()
    db.refresh(new_restaurant)
    return new_restaurant


@router.get("/restaurants/", response_model=RestaurantBase)
def get_all_restaurants(db: Session = Depends(get_db)):
    return db.query(Restaurant).all()

@router.post("/menus/", response_model=MenuCreate)
def create_menu(menu: MenuCreate, db: Session = Depends(get_db)):
    new_menu = Menu(**menu.model_dump())
    db.add(new_menu)
    db.commit()
    db.refresh(new_menu)
    return new_menu


@router.get("/menus/", response_model=MenuSchema)
def get_all_menus(db: Session = Depends(get_db)):
    return db.query(Menu).all()


@router.post("/users/", response_model=UserCreate)
def create_employee(employee: UserCreate, db: Session = Depends(get_db)):
    new_user = User(**employee.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/menus/today/", response_model=MenuSchema)
def get_today_menu(db: Session = Depends(get_db)):
    menu = db.query(Menu).filter(Menu.date == date.today())

    if not menu:
        raise HTTPException(
            status_code=400,
            detail="No menu available for today"
        )


@router.get("/votes/", response_model=VoteSchema)
def get_today_votes(db: Session = Depends(get_db)):
    votes = (
        db.query(Menu, Vote).join(Vote, Vote.menu_id == Menu.id)
        .filter(Menu.date == date.today()).all()
    )
    return votes
