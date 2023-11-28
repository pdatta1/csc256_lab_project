# import bottle
from typing import * 
from bottle import route, get, post, request, run, redirect, template
from beaker.middleware import SessionMiddleware

import YourList
import Login


# adding get_todo_list to make this more testable
def get_todo_list() -> List:
    session = request.environ.get('beaker.session')

    if session is None:
        session = {}
        request.environ['beaker.session'] = session

    if 'todo_list' in session:
        todo_list = session['todo_list']
    else:
        todo_list = []
        session['todo_list'] = todo_list

    return todo_list
    

# Data is stored on the session in memory
@route('/list')
def your_list():
    todo_list: List = get_todo_list()
    return template('list', todo_list=todo_list)



