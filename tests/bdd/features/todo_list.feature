# features/todo_list.feature

Feature: todo_list login

  Scenario: Logging into todo list with valid credentials
    Given I click localhost link
    When I see todo list homepage
    And Enter username "User" and password "password"
    And Click on login button
    Then User will successfully be logged into todo list

  Scenario: Logging in witht invalid credentials 
    Given the login page is open
    When the user enters invalid credentials
    And clicks the login button
    Then the user should see a login failed message
  
  Scenario: User can add an item
    Given the user is on the list page
    When the user adds a new item with name "Test Item" and quantity "3"
    Then the item "Test Item" should be added to the list


