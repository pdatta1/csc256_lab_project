# features/list_view.feature

Feature: ToDo List Management

  Scenario: Remove an item from the to-do list
    Given the user has a to-do list with the following items:
      | Task 1       |
      | Task to keep |
      | Task to remove |
    When the user chooses to remove an item from the to-do list
    Then the to-do list should no longer contain the task "Task to remove"
    And the to-do list should still contain the task "Task to keep"

  Scenario: Open up list view to make sure to-do items are accurately reflected
    Given the user has a to-do list with the following items:
      | Task 1 |
    When the user opens the list view
    Then the list view should display the tasks in the following order:
      | Task 1 |
