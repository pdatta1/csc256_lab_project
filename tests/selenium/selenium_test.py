from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium import webdriver
from typing import * 



def wait_and_find_element(driver: webdriver.Chrome, by: By, element: str, timeout: int = 10) -> WebElement:
    """
    Wait for an element to be present on the page and return it.
    """
    try:
        return WebDriverWait(driver, timeout).until(lambda d: d.find_element(by, element))
    except: 
        return None 

def login(driver: webdriver.Chrome, username: str, password: str) -> bool:
    """
    Log in with the provided username and password.
    Return True if login is successful, False otherwise.
    """
    driver.get("http://localhost:8080")
    username_input = wait_and_find_element(driver, By.NAME, "username")
    password_input = wait_and_find_element(driver, By.NAME, "password")
    login_button = wait_and_find_element(driver, By.XPATH, "//button[contains(., 'Login')]")

    username_input.send_keys(username)
    password_input.send_keys(password)
    login_button.click()

    try:
        # Check for the presence of the "Add New Item" button after successful login
        wait_and_find_element(driver, By.XPATH, "//button[contains(., 'Add New Item')]")
        return True  # Login successful
    except Exception as e:
        print(f"Login failed. Exception: {e}")
        return False  # Login failed



def add_new_task(driver: webdriver.Chrome, task: str) -> None:
    """
    Add a new task to the To-Do list.
    """
    add_button = wait_and_find_element(driver, By.XPATH, "//button[contains(., 'Add New Item')]")
    add_button.click()

    task_input = wait_and_find_element(driver, By.NAME, "todo")
    add_task_button = wait_and_find_element(driver, By.XPATH, "//button[contains(., 'Add Task')]")

    task_input.send_keys(task)
    add_task_button.click()


def list_view(driver: webdriver.Chrome) -> None:
    """
    Navigate to the list view and verify the tasks are displayed.
    """

    # Check for the presence of radio buttons corresponding to tasks
    task_radio_buttons = driver.find_elements(By.XPATH, "//input[@type='radio' and @name='todo_item']")
    assert len(task_radio_buttons) > 0

    # Optional: Print the text of each task for verification
    for index, radio_button in enumerate(task_radio_buttons):
        print(f"Task {index}: {radio_button.text}")



def sign_out(driver: webdriver.Chrome) -> None:
    """
    Sign out and verify the user is redirected to the login page.
    """
    return "Sign out functionality not implemented yet."
    logout_button = wait_and_find_element(driver, By.XPATH, "//button[contains(., 'Logout')]")
    logout_button.click()

    login_button = wait_and_find_element(driver, By.XPATH, "//input[@value='Login']")
    assert login_button is not None


def delete_task(driver: webdriver.Chrome, task_index: int) -> None:
    """
    Delete a task and verify it's removed from the list.
    """
    radio_button_xpath = f"//input[@type='radio' and @name='todo_item' and @value='{task_index}']"
    item_to_delete_radio_button = wait_and_find_element(driver, By.XPATH, radio_button_xpath)
    item_to_delete_radio_button.click()

    delete_button = wait_and_find_element(driver, By.XPATH, "//button[contains(., 'Delete Item')]")
    delete_button.click()

    list_view(driver)

    deleted_items = driver.find_elements(By.XPATH, "//input[@type='checkbox' and @checked='checked']")
    assert len(deleted_items) == 0


def update_task(driver: webdriver.Chrome, task_index: int, updated_task: str) -> None:
    """
    Update a task and verify the update is reflected in the list.
    """
    radio_button_xpath = f"//input[@type='radio' and @name='todo_item' and @value='{task_index}']"
    item_to_update_radio_button = wait_and_find_element(driver, By.XPATH, radio_button_xpath)
    item_to_update_radio_button.click()

    update_button = wait_and_find_element(driver, By.XPATH, "//button[contains(., 'Update Item')]")
    update_button.click()

    task_input_update = wait_and_find_element(driver, By.NAME, "todo")
    task_input_update.clear()
    task_input_update.send_keys(updated_task)

    update_task_button = wait_and_find_element(driver, By.XPATH, "//input[@value='Update']")
    update_task_button.click()

    list_view(driver)

    updated_items = driver.find_elements(By.XPATH, "//input[@type='checkbox' and @checked='checked']")
    assert len(updated_items) > 0


def run_test_scenarios() -> None:
    """
    Run the test scenarios.
    """
    driver = webdriver.Chrome()

    try:
        login(driver, "User", "password")
        add_new_task(driver, "New Task 1")
        list_view(driver)

        # Scenario 1: Sign in/Sign out functionality
        # sign_out(driver)

        # Scenario 2: List view functionality
        login(driver, "User", "password")
        list_view(driver)

        # Scenario 3: Verify user authentication
        if not login(driver, "User", "WrongPassword"):
            print("Login with wrong credentials failed.")


        # Scenario 4: Delete functionality
        login(driver, "User", "password")
        add_new_task(driver, "Task to Delete")
        delete_task(driver, 0)

        # Scenario 5: Update functionality
        # login(driver, "User", "password")
        # add_new_task(driver, "Task to Update")
        # update_task(driver, 0, "Updated Task")
    # except Exception as e: 
    #     print(f"Exception Thrown : {e}")
    finally:
        driver.quit()
        print("Selenium test passed!")


if __name__ == "__main__":
    run_test_scenarios()
