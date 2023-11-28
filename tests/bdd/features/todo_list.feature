Feature: todo_list login
  Scenario Outline: Logging into todo list with valid credentials
    Given I click localhost link
    When I see todo list homepage
    And Enter username <User> and password <password>
    And Click on login button
    Then User will successfully be logged into todo list


  Examples:
    |username| | password |
    |User    | | password |
    |password| | User     |
    |uSer    | | Password |
    |USER    | | paSSword |