import pytest
from fastapi.testclient import TestClient
from backend.app.main import app
from backend.app.database.session import get_db, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

TEST_DATABASE_URL = "postgresql://test_user:test_password@postgres_fastapi:5432/test_db"
engine = create_engine(TEST_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="module")
def test_db():
    """Creates a fresh test database and cleans up after tests."""
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    yield db
    db.close()
    Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="module")
def client(test_db):
    """Provides a test client using the test database."""
    app.dependency_overrides[get_db] = lambda: test_db
    return TestClient(app)
