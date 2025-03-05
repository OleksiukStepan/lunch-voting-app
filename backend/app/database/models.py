from sqlalchemy import Column, Integer, String, Numeric, ForeignKey, Date

from backend.app.database.session import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    firstname = Column(String(255), nullable=False)
    lastname = Column(String(255), nullable=False)
    username = Column(String(255), unique=True, nullable=False)
    password = Column(String, nullable=False)

    @property
    def fullname(self):
        if self.firstname and self.lastname:
            return f"{self.firstname} {self.lastname}"

        return None


class Restaurant(Base):
    __tablename__ = "restaurants"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False, unique=True)


class Menu(Base):
    __tablename__ = "menus"

    id = Column(Integer, primary_key=True, autoincrement=True)
    dish = Column(String(255), unique=True, nullable=False)
    description = Column(String)
    price = Column(Numeric(10, 2), nullable=False)
    date = Column(Date)

    restaurant_id = Column(Integer, ForeignKey("restaurants.id"), nullable=False)


class Vote(Base):
    __tablename__ = "votes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    menu_id = Column(Integer, ForeignKey("menu.id"), nullable=False)
