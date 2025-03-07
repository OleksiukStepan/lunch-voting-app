from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.app.database.models import Restaurant
from backend.app.database.session import get_db
from backend.app.schemas.restaurant import (
    RestaurantCreate,
    RestaurantBase,
    RestaurantSchema,
)

router = APIRouter()


@router.post("/", response_model=RestaurantSchema)
def create_restaurant(restaurant: RestaurantCreate, db: Session = Depends(get_db)):
    """Creates a new restaurant with the given name"""

    new_restaurant = Restaurant(name=restaurant.name)
    db.add(new_restaurant)
    db.commit()
    db.refresh(new_restaurant)

    return new_restaurant


@router.get("/", response_model=list[RestaurantBase])
def get_all_restaurants(db: Session = Depends(get_db)):
    """Retrieves a list of all registered restaurants"""

    return db.query(Restaurant).all()
