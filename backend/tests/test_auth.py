
def test_register_user(client):
    response = client.post("/auth/register", json={
        "username": "testuser",
        "firstname": "Test",
        "lastname": "User",
        "password": "testpassword"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()


def test_login_user(client):
    response = client.post("/auth/login", json={
        "username": "testuser",
        "password": "testpassword"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()
    return response.json()["access_token"]
