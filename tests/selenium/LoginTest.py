from selenium import webdriver
from selenium.webdriver.common.by import By

# Start a new instance of the Chrome browser
driver = webdriver.Chrome()

# Navigate to the login page
driver.get("http://localhost:8080")


# Find the username and password input fields and the login button
username_input = driver.find_element("name", "username")
password_input = driver.find_element("name", "password")
login_button = driver.find_element("xpath", "//input[@value='Login']")

# Enter the username and password
username_input.send_keys("User")
password_input.send_keys("Pa55w0rd")

# Click the login button
login_button.click()

# Wait for the redirect to the list page
driver.implicitly_wait(10)  


# Find the buttons by their visible text
add_button = driver.find_element(By.XPATH, "//button[contains(., 'Add New Item')]")
update_button = driver.find_element(By.XPATH, "//button[contains(., 'Update Item')]")
delete_button = driver.find_element(By.XPATH, "//button[contains(., 'Delete Item')]")


# Assert the presence of these buttons
assert add_button is not None
assert update_button is not None
assert delete_button is not None

# Close the browser
driver.quit()

print("Login test passed!")
