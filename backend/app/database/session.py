from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

DATABASE_URL = "postgresql://stepan:stepan_password@lunch_db:5432/lunch"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
