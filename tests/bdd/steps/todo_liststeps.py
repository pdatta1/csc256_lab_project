# Charne Robinson
# November 25h, 2023
# BDD Testing - Scenario 1

from behave import *
from selenium import webdriver


@given(u'I click localhost link')
def clickLink(context):
    context.driver = webdriver.Chrome()


@when(u'I see todo list homepage')
def typeInfo(context):
    context.driver.get("http://localhost:8080")


@when(u'Enter username "{user}" and password "{password}"')
def verifyCred(context, user, password):
    context.driver.find_element("name", "username").send_keys(user)
    context.driver.find_element("name", "password").send_keys(password)


@when(u'Click on login button')
def clickLogin(context):
    button = context.driver.find_element("xpath", "//button[contains(., 'Login')]")
    button.click() 


@then(u'User will successfully be logged into todo list')
def clickLogin(context):
    try:
        button = context.driver.find_element("xpath", "//button[contains(., 'Add New Item')]")
   
        if button == "Add New Item":
            context.driver.close()
            assert True, "Test Passed"
    except Exception as e:
        print(f"Exception at User {e}")
        context.driver.close()
        assert False, "Test Failed"

@given('the login page is open')
def step_given_user_on_login_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get("http://localhost:8080")

@when('the user enters invalid credentials')
def step_when_user_enters_invalid_credentials(context):
    username_input = context.driver.find_element("name", "username")
    password_input = context.driver.find_element("name", "password")
    username_input.send_keys("InvalidUser")
    password_input.send_keys("InvalidPassword")


@when('clicks the login button')
def step_when_clicks_login_button(context):
    login_button = context.driver.find_element("xpath", "//input[@value='Login']")
    login_button.click()

@then('the user should see an error message indicating invalid credentials')
def step_then_see_login_failed_message(context):
    login_failed_message = context.driver.find_element(By.XPATH, "//p[text()='Login failed.']")
    assert login_failed_message is not None

@then('the user should remain on the login page')
def step_then_remain_on_login_page(context):
    assert context.driver.current_url == "http://localhost:8080/"
