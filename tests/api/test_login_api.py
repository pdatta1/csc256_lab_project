# Charne Robinson
# December 1st, 2023
# API Testing - Scenario 1


import requests

ENDPOINT = "http://localhost:8080/"


def test_can_call_endpoint():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200


def test_validLogin():
    login = {
        "content": "login test content",
        "user_id": "User",
        "password": "password",
        "is_done": False,
    }
    response = requests.post(ENDPOINT + "/getjson", json=login)
    assert response.status_code == 200

    data = response.json()
    print(data)

    # this part forward I got from the video I watched. IDK how to apply what he did to ours

    task_id = data["task"]["task_id"]
    get_task_response = requests.get(ENDPOINT + f"/getjson/{task_id}")

    assert get_task_response.status_code == 200
    get_task_data = get_task_response.json()
    assert get_task_data["content"] == login["content"]
    assert get_task_data["user_id"] == login["user_id"]
    print(get_task_data)
