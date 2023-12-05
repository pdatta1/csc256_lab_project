
from selenium import webdriver


def clickLink(context):
    context.driver = webdriver.Chrome()


def login(context, user, password):
    context.get("http://localhost:8080")
    context.driver.find_element("name", "username").send_keys(user)
    context.driver.find_element("name", "password").send_keys(password)


#Carine Rotich

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
        
def test_invalid_login(context, username, password):
    try:
        login(context, username, password)
        error_message = context.driver.find_element("id", "error-message").text
        assert "Invalid credentials" in error_message, "Test Passed"
    except Exception as e:
        print(f"Exception: {e}")
        assert False, "Test Failed"


def test_remove_item_from_todo_list(context, item_text):
    try:
        remove_item_from_todo_list(context, item_text)
        assert not context.driver.find_elements("xpath", f"//li[contains(., '{item_text}')]")
    except Exception as e:
        print(f"Exception: {e}")
        assert False, "Test Failed"


