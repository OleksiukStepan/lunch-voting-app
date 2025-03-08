import pytest
from fastapi.testclient import TestClient
from backend.app.database.session import Base, get_db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from backend.app.main import app

TEST_DATABASE_URL = "postgresql://test_user:test_password@test_db:5432/test_db"
engine = create_engine(TEST_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="module")
def test_db():
    """Creates a fresh test database and cleans up after tests"""

    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    app.dependency_overrides[get_db] = lambda: db
    yield db
    db.close()
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="module")
def client(test_db):
    """Provides a test client using the test database."""
    return TestClient(app)


@pytest.fixture(scope="module")
def setup_test_data(client):
    """Seeds the database with test user, restaurant, and menu before voting."""

    # Create a test user
    user_response = client.post("/auth/register", json={
        "username": "testuser",
        "firstname": "Test",
        "lastname": "User",
        "password": "testpassword"
    })
    assert user_response.status_code == 200, user_response.text

    # Authenticate the user
    login_response = client.post("/auth/login", json={
        "username": "testuser",
        "password": "testpassword"
    })
    assert login_response.status_code == 200, login_response.text
    token = login_response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # Create a test restaurant
    restaurant_response = client.post("/restaurants/", json={"name": "Test Restaurant"}, headers=headers)
    assert restaurant_response.status_code == 200, restaurant_response.text
    restaurant_id = restaurant_response.json()["id"]

    # Create a test menu
    menu_response = client.post("/menus/", json={
        "dish": "Test Dish",
        "description": "A test dish description.",
        "price": 10.99,
        "date": "2025-03-07",
        "restaurant_id": restaurant_id
    }, headers=headers)
    assert menu_response.status_code == 200, menu_response.text
    menu_id = menu_response.json()["id"]

    return {
        "headers": headers,
        "menu_id": menu_id,
        "restaurant_id": restaurant_id,
        "user_id": 1
    }
