# Charne Robinson
# December 1st, 2023
# API Testing - Scenario 1


import requests
import pytest 

ENDPOINT = "http://localhost:8080/"

"""
Scenario 1: Logging in with valid credentials 

Scenario 2: Add item to out to-do list 
"""

def test_user_can_login_with_valid_credential(): 
    login_payload = { 
        'username': 'User',
        'password': 'password'
    }
    response = requests.post(ENDPOINT, json=login_payload)
    assert response.status_code == 200

def test_user_can_add_item():
   task_index = 0 
   response = requests.post(f"{ENDPOINT}/newItems?todo_item={task_index}")

   assert response.status_code == 200



def test_get_todo_list():
    """
        issue -> /getJson is redirecting to /list
                - developers needs to remove the else statemen to
                - redirect in order to get the json.
                - make sure the todo list array is populated
    """
    response = requests.get(ENDPOINT + "getJson")
    assert response.status_code == 200

    data = response.json()
    print(data)



