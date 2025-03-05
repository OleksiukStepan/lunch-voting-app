from datetime import date

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.app.database.models import Menu
from backend.app.database.session import get_db
from backend.app.schemas.menu import MenuCreate, MenuSchema

router = APIRouter()


@router.post("/", response_model=MenuCreate)
def create_menu(menu: MenuCreate, db: Session = Depends(get_db)):
    new_menu = Menu(**menu.model_dump())
    db.add(new_menu)
    db.commit()
    db.refresh(new_menu)
    return new_menu


@router.get("/", response_model=MenuSchema)
def get_all_menus(db: Session = Depends(get_db)):
    return db.query(Menu).all()


@router.get("/today/", response_model=MenuSchema)
def get_today_menu(db: Session = Depends(get_db)):
    menu = db.query(Menu).filter(Menu.date == date.today())

    if not menu:
        raise HTTPException(
            status_code=400,
            detail="No menu available for today"
        )

    return menu
