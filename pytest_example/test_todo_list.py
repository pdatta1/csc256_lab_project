from Login import *
from ItemUpdate import *
from YourList import *


def test_index():
    pass


def test_check_login():
    assert check_login('User', 'Pa55w0rd') == True
    assert check_login('User', 'password') == False
    assert check_login('user', 'Pa55w0rd') == False

def test_new_item():
    pass

def test_update_item():
    pass

def test_delete_item():
    pass


def test_your_list():
    pass