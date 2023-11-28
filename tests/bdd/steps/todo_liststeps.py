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
        print(f"Exception at User will blahhhhh {e}")
        context.driver.close()
        assert False, "Test Failed"
