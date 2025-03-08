
def test_create_restaurant(client):
    response = client.post("/restaurants/", json={"name": "Test Restaurant"})
    assert response.status_code == 200
    assert response.json()["name"] == "Test Restaurant"


def test_get_restaurants(client):
    response = client.get("/restaurants/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
