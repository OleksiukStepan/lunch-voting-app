from sqlalchemy import (
    Column,
    Integer,
    String,
    Numeric,
    ForeignKey,
    Date,
    func,
)
from sqlalchemy.orm import relationship

from backend.app.database.session import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    firstname = Column(String(255), nullable=False)
    lastname = Column(String(255), nullable=False)
    username = Column(String(255), unique=True, nullable=False)
    password = Column(String, nullable=False)

    votes = relationship("Vote", back_populates="users")

    @property
    def fullname(self):
        if self.firstname and self.lastname:
            return f"{self.firstname} {self.lastname}"

        return None


class Restaurant(Base):
    __tablename__ = "restaurants"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False, unique=True)

    menus = relationship("Menu", back_populates="restaurants")


class Menu(Base):
    __tablename__ = "menus"

    id = Column(Integer, primary_key=True, autoincrement=True)
    dish = Column(String(255), unique=True, nullable=False)
    description = Column(String)
    price = Column(Numeric(10, 2), nullable=False)
    date = Column(Date, default=func.current_date())
    restaurant_id = Column(Integer, ForeignKey("restaurants.id"), nullable=False)

    restaurants = relationship("Restaurant", back_populates="menus")
    votes = relationship("Vote", back_populates="menus")


class Vote(Base):
    __tablename__ = "votes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    menu_id = Column(Integer, ForeignKey("menus.id"), nullable=False)
    created_at = Column(Date, default=func.current_date())

    users = relationship("User", back_populates="votes")
    menus = relationship("Menu", back_populates="votes")
