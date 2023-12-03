# Charne Robinson
# December 1st, 2023
# API Testing - Scenario 1


import requests

ENDPOINT = "http://localhost:8080/"


def test_get_todo_list():
    response = requests.get(ENDPOINT + "/getjson")
    assert response.status_code == 200

    data = response.json()
    print(data)



