
def test_vote_for_menu(client, setup_test_data):
    headers = setup_test_data["headers"]
    menu_id = setup_test_data["menu_id"]
    user_id = setup_test_data["user_id"]

    vote_response = client.post("/votes/", json={
        "user_id": user_id,
        "menu_id": menu_id
    }, headers=headers)

    assert vote_response.status_code == 200, vote_response.text


def test_get_today_votes(client, setup_test_data):
    headers = setup_test_data["headers"]

    response = client.get("/votes/", headers=headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)



def test_get_voting_results(client, setup_test_data):
    headers = setup_test_data["headers"]

    response = client.get("/votes/results/", headers=headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
