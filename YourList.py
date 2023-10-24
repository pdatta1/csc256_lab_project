# Do session request for users list.
# Button to add New item to list
# Button to update item on list (check boxes with button)
# Button to delete item (again check box with button)
import bottle
from bottle import route, get, post, request, run, redirect
from beaker.middleware import SessionMiddleware
import ItemUpdate
import Login

# Data is stored on the session in memory
@bottle.get('/list')
def your_list():
    session = bottle.request.environ.get('beaker.session')
    if 'todo_list' in session:
        todo_list = session['todo_list']
    else:
        todo_list = []
        session['todo_list'] = todo_list
    to_return = '''
        <form id="todo_form">
    '''
    # List is assembled in a loop to handle any number of items
    for x in range(len(todo_list)):
        to_return += f'''
            <input type="radio" name="todo_item" value="{x}"> {todo_list[x]} </br>
        '''

    # javascript function to process three different submit buttons
    to_return += '''
            <button type="button" onclick="processForm('add')">Add New Item</button>
            <button type="button" onclick="processForm('update')">Update Item</button>
            <button type="button" onclick="processForm('delete')">Delete Item</button>
        </form>

        <script type="text/javascript">
            function processForm(action) {
                var form = document.getElementById('todo_form');
                var selectedRadio = document.querySelector('input[name="todo_item"]:checked');
                var selectedValue = selectedRadio ? selectedRadio.value : null;


                if (action == 'add') {
                    form.action = '/newItems';
                } else if (action == 'update' && selectedValue != null) {
                    form.action = '/updateItems?todo_item=' + selectedValue;
                } else if (action == 'delete' && selectedValue != null) {
                    form.action = '/deleteItems?todo_item=' + selectedValue;
                }

                form.submit();
            }
        </script>
    '''
    return to_return