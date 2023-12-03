# csc256_lab_project
CSC 256 Lab project 2023

Modules needed to run this web app:
-----------------------------
pip install bottle
pip install beaker




- Testing Selenium
    - pip install selenium
    - Run the server first
        - python Login.py
    - python tests/selenium/selenium_test.py


- Testing BDD
    - make sure these are installed with pip
        - pip install behave
        - RUN 'behave' in the root directory of the projectLogging into todo list with valid credentials 

- Testing TDD
    - pip install pytest
    - pytest

- Performance Testing
    - pip install locust
    - pip install bs4
    - locust -f tests/performance_testing/perform_test.py
    - navigate to http://localhost:8089/ 
        - enter amount of users, spawn rate and host, then click button
        - your will be linked to a dashboard and you can view the performance stats

- API TESTING
    - pip install pytest
    - pytest tests/api/test_api.py