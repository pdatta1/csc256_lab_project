import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def wait_and_find_element(driver, by, element, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((by, element))
    )

def login(driver, username, password):
    driver.get("http://localhost:8080")
    username_input = wait_and_find_element(driver, By.NAME, "username")
    password_input = wait_and_find_element(driver, By.NAME, "password")
    login_button = wait_and_find_element(driver, By.XPATH, "//button[contains(., 'Login')]")

    assert username_input is not None
    assert password_input is not None
    assert login_button is not None

    username_input.send_keys(username)
    password_input.send_keys(password)
    login_button.click()

    # Check for the presence of the "Add New Item" button after successful login
    add_new_item_button = wait_and_find_element(driver, By.XPATH, "//button[contains(., 'Add New Item')]")
    assert add_new_item_button is not None

def test_scenario_1(driver):
    # Log in with valid credentials
    login(driver, "User", "password")

    # Verify successful login by checking the presence of the "Add New Item" button
    add_new_item_button = wait_and_find_element(driver, By.XPATH, "//button[contains(., 'Add New Item')]")
    assert add_new_item_button is not None

def test_scenario_2(driver):
    # Log in with valid credentials
    login(driver, "User", "password")

    # Add a new task
    add_new_task(driver, "New Task 1")

    # Verify the task is added successfully by checking the presence of the task in the list
    todo_list_items = driver.find_elements(By.XPATH, "//input[@type='radio' and @name='todo_item']")
    assert len(todo_list_items) > 0  # Assuming there is at least one item

def test_scenario_3(driver):
    # Log in with valid credentials
    login(driver, "User", "password")

    # Add a new task
    add_new_task(driver, "New Task 1")

    # Navigate to the list view by changing the URL
    driver.get("http://localhost:8080/list")

    # Verify the accuracy of the to-do list
    todo_list_items = driver.find_elements(By.XPATH, "//input[@type='radio' and @name='todo_item']")
    assert len(todo_list_items) > 0  # Assuming there is at least one item

def test_scenario_4(driver):
    # Log in with valid credentials
    login(driver, "User", "password")

    # Add a new task
    add_new_task(driver, "Task to Delete")

    # Navigate to the list view by changing the URL
    driver.get("http://localhost:8080/list")

    # Verify the accuracy of the to-do list before deletion
    todo_list_items_before_deletion = driver.find_elements(By.XPATH, "//input[@type='radio' and @name='todo_item']")
    assert len(todo_list_items_before_deletion) > 0  # Assuming there is at least one item

    # Delete the task
    delete_task(driver, 0)

    # Verify the accuracy of the to-do list after deletion by changing the URL
    driver.get("http://localhost:8080/list")

    # Verify the list is now empty
    todo_list_items_after_deletion = driver.find_elements(By.XPATH, "//input[@type='radio' and @name='todo_item']")
    assert len(todo_list_items_after_deletion) == 0  # The item should be deleted

def add_new_task(driver, task):
    # Add a new task to the To-Do list.
    add_button = wait_and_find_element(driver, By.XPATH, "//button[contains(., 'Add New Item')]")
    add_button.click()

    task_input = wait_and_find_element(driver, By.NAME, "todo")
    add_task_button = wait_and_find_element(driver, By.XPATH, "//button[contains(., 'Add Task')]")

    task_input.send_keys(task)
    add_task_button.click()

def delete_task(driver, task_index):
    # Delete a task and verify it's removed from the list.
    radio_button_xpath = f"//input[@type='radio' and @name='todo_item' and @value='{task_index}']"
    item_to_delete_radio_button = wait_and_find_element(driver, By.XPATH, radio_button_xpath)
    item_to_delete_radio_button.click()

    delete_button = wait_and_find_element(driver, By.XPATH, "//button[contains(., 'Delete Item')]")
    delete_button.click()
