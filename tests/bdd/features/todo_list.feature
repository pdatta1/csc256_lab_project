# Charne Robinson
# November 25th, 2023
# BDD Testing - Scenario 1

# features/todo_list.feature

Feature: todo_list login

  Scenario: Logging into todo list with valid credentials
    Given I click localhost link
    When I see todo list homepage
    And Enter username "User" and password "password"
    And Click on login button
    Then User will successfully be logged into todo list


