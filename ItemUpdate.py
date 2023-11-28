from bottle import route, request, template, redirect, static_file, response
from json import dumps

import YourList
import Login

# Creates form allowing user to enter a new task
# GET and POST are combined GET is a simple form, POST accessess the session adds the item to a list then readds the list item to the session
@route('/newItems', method=['GET', 'POST'])
def new_item():
    if request.method == 'GET':
        return template('add_item')
        # return '''
        #         <form action="/newItems" method="post">
        #             Task: <input name = "todo" type="text" />
        #             <input value="Add" type="submit" />
        #         </form>
        #     '''
    elif request.method == 'POST':
        session = request.environ.get('beaker.session')
        if 'todo_list' in session:
            todo_list = session['todo_list']
            taskToAdd = request.forms.get('todo')
            todo_list.append(taskToAdd)
            session['todo_list'] = todo_list
        else:
            todo_list = []
            session['todo_list'] = todo_list
        redirect('/list')

# Create form allowing user to update existing task
# Same as newItems just with form preloaded, POST sets existing item instead of append
@route('/updateItems', method=['GET', 'POST'])
def update_item():
    todo_item = int(request.query.get('todo_item'))
    # todo_item = request.query.get('todo_item')
    if request.method == 'GET':
        session = request.environ.get('beaker.session')
        if 'todo_list' in session:
            todo_list = session['todo_list']
        else:
            todo_list = []
        return template('update_item', todo_list=todo_list, todo_item=todo_item)
        # f'''
        #     <form action="/updateItems?todo_item={todo_item}" method="post">
        #         Task: <input name = "todo" value = "{todo_list[todo_item]}" type="text" />
        #         <input value="Update" type="submit" />
        #     </form>
        # '''
    elif request.method == 'POST':
        session = request.environ.get('beaker.session')
        if 'todo_list' in session:
            todo_list = session['todo_list']
            taskToAdd = request.forms.get('todo')
            todo_list[todo_item] = (taskToAdd)
            session['todo_list'] = todo_list
        else:
            todo_list = []
            session['todo_list'] = todo_list
        redirect('/list')

# deleteItems only has one method since it doesn't have a display, pops indicated item from list pulled from session before readding it to the session
@route('/deleteItems', method=['GET'])
def delete_item():
    session = request.environ.get('beaker.session')
    todo_item = int(request.query.get('todo_item'))
    if 'todo_list' in session:
        todo_list = session['todo_list']
        todo_list.pop(todo_item)
        session['todo_list'] = todo_list
    else:
        todo_list = []
        session['todo_list'] = todo_list
    redirect('/list')    

# sortItems only has one method since it doesn't have a display, sorts items from list pulled from session before readding it to the session
@route('/sortItems', method=['GET'])
def sort_item():
    session = request.environ.get('beaker.session')
    # todo_item = int(request.query.get('todo_item'))
    if 'todo_list' in session:
        todo_list = session['todo_list']
        todo_list.sort()
        session['todo_list'] = todo_list
    else:
        todo_list = []
        session['todo_list'] = todo_list
    redirect('/list')

@route('/getJson', method=['GET'])
def get_json():
    session = request.environ.get('beaker.session')
    if 'todo_list' in session:
        todo_list = session['todo_list']
        response.content_type = 'application/json'
        return dumps(todo_list)
    else:
        redirect('/list')