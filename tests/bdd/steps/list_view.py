
from behave import given, when, then
from YourList import get_todo_list

@given('the user has a to-do list with the following items')
def step_given_user_has_todo_list(context):
    context.session = get_todo_list()
    for row in context.table:
        context.session.append(row[0])

@when('the user chooses to remove an item from the to-do list')
def step_when_user_removes_item(context):
    context.removed_task = 'Task to remove'
    context.session = [task for task in context.session if task != context.removed_task]

@then('the to-do list should no longer contain the task "{task}"')
def step_then_list_should_not_contain_task(context, task):
    assert task not in context.session

@then('the to-do list should still contain the task "{task}"')
def step_then_list_should_contain_task(context, task):
    assert task in context.session


@when('the user opens the list view')
def step_when_user_opens_list_view(context):
    context.todo_list = get_todo_list()

@then('the list view should display the tasks in the following order')
def step_then_list_view_should_display_in_order(context):
    expected_order = [row for row in context.session]
    context.todo_list = get_todo_list()
    print(f'context todo list {context.todo_list}')
    print('expected order: ', expected_order)
    assert context.todo_list == expected_order
