from behave import *
from selenium import webdriver


@given(u'I click localhost link')
def clickLink(context):
    context.driver = webdriver.Chrome()


@when(u'I see todo list homepage')
def typeInfo(context):
    context.driver.get("http://localhost:8080")


@when(u'Enter username "{User}" and password "{password}"')
def verifyCred(context, user, password):
    context.driver.find_element_by_name("username").send_keys(user)
    context.driver.find_element_by_name("password").send_keys(password)


@when(u'Click on login button')
def clickLogin(context):
    context.driver.find_element_by_class("button is-success").click()


@then(u'User will successfully be logged into todo list')
def clickLogin(context):
    try:
        text = context.driver.find_element_by_class("side-bar button is-primary is-light is-hovered")
    except:
        context.driver.close()
        assert False, "Test Failed"
    if text == "Add New Item":
        context.driver.close()
        assert True, "Test Passed"
