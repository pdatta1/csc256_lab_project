from typing import List, Optional

import requests

def get_todo_list() -> Optional[List[str]]:
    url = 'http://localhost:8080/list'
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve to-do list. Status Code: {response.status_code}")
        return None

def print_and_validate_todo_list(todo_list: Optional[List[str]]) -> None:
    if todo_list is not None:
        print("To-Do List:", todo_list)
        # Add further validation logic as needed

def delete_item(index: int) -> None:
    delete_url = f'http://localhost:8080/deleteItems?todo_item={index}'
    response = requests.get(delete_url)

    if response.status_code == 302:
        print(f"Item at index {index} deleted successfully.")
    else:
        print(f"Failed to delete item. Status Code: {response.status_code}")

# Scenario 3: Bring up entered to-do list and verify accuracy
todo_list = get_todo_list()
print_and_validate_todo_list(todo_list)

# Scenario 4: After verifying the to-do list accuracy, delete an item and review the list again to ensure it is not there
delete_index: int = 1 # Replace <index> with the index of the item to delete
delete_item(delete_index)

# Retrieve the updated to-do list
updated_todo_list = get_todo_list()
print_and_validate_todo_list(updated_todo_list)
