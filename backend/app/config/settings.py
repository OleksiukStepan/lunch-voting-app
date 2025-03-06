from pathlib import Path

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ROOT_DIR: Path = Path(__file__).resolve().parents[3]
    BASE_DIR: Path = Path(__file__).parent.parent
    PATH_TO_DB: str = str(BASE_DIR / "database" / "lunch.db")
