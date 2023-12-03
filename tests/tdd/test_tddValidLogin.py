# Charne Robinson
# December 1st, 2023
# TDD Testing - Scenario 1

from selenium import webdriver


def clickLink(context):
    context.driver = webdriver.Chrome()


def login(context, user, password):
    context.get("http://localhost:8080")
    context.driver.find_element("name", "username").send_keys(user)
    context.driver.find_element("name", "password").send_keys(password)


def test_login_is_valid(context, username, password):
    try:
        button = context.driver.find_element("xpath", "//button[contains(., 'Add New Item')]")

        if button == "Add New Item":
            context.driver.close()
            assert True, "Test Passed"
    except Exception as e:
        print(f"Exception at User {e}")
        context.driver.close()
        assert False, "Test Failed"
