from selenium import webdriver
from selenium.webdriver.common.by import By


# Start a new instance of the Chrome browser
driver = webdriver.Chrome()

# Navigate to the list page (assuming you've already logged in successfully)
driver.get("http://localhost:8080/list")

# add a new task 
add_button = driver.find_element(By.XPATH, "//button[contains(., 'Add New Item')]")
assert add_button is not None 

add_button.click() 
driver.implicitly_wait(5)  


task_input = driver.find_element(By.NAME, "todo")
add_new_task_button = driver.find_element("xpath", "//input[@value='Add']")

# Enter a new task and click the "Add" button
new_task = "New Task 1"
task_input.send_keys(new_task)
add_new_task_button.click()

driver.implicitly_wait(5)

# Check if the task was added successfully
radio_buttons = driver.find_elements(By.XPATH, "//input[@type='radio']")
assert len(radio_buttons) > 0

# # Go to the "Update Item" page for the added task

radio_button = driver.find_element(By.XPATH, "//input[@type='radio' and @name='todo_item' and @value='0']")
assert radio_button is not None

radio_button.click()

driver.implicitly_wait(5)

update_button = driver.find_element(By.XPATH, "//button[contains(., 'Update Item')]")
update_button.click()

driver.implicitly_wait(5)

task_input_update = driver.find_element(By.NAME, "todo")
update_task_button = driver.find_element("xpath", "//input[@value='Update']")

# update the task 
updated_task = "Updated Task 1"
task_input_update.clear()

driver.implicitly_wait(5)

task_input_update.send_keys(updated_task)
update_task_button.click()

driver.implicitly_wait(5)

updated_task_radio_button = driver.find_element(By.XPATH, "//input[@type='radio' and @name='todo_item' and @value='0' ]")
assert updated_task_radio_button is not None 

driver.implicitly_wait(5)

# delete the task 
updated_task_radio_button.click()
delete_button = driver.find_element(By.XPATH, "//button[contains(., 'Delete Item')]")

delete_button.click() 

driver.implicitly_wait(10)

driver.quit()

print("Selenium test passed!")