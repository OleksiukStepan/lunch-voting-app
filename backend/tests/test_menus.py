
def test_create_menu(client, setup_test_data):
    restaurant_id = setup_test_data["restaurant_id"]

    response = client.post("/menus/", json={
        "dish": "Test Unique Dish",
        "description": "A test dish description.",
        "price": 10.99,
        "date": "2025-03-07",
        "restaurant_id": restaurant_id
    })
    assert response.status_code == 200
    assert response.json()["dish"] == "Test Unique Dish"


def test_get_menus(client):
    response = client.get("/menus/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_today_menu(client):
    response = client.get("/menus/today/")
    assert response.status_code in [200, 400]
