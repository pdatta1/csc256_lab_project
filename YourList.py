# import bottle
from bottle import route, get, post, request, run, redirect, template
from beaker.middleware import SessionMiddleware

import YourList
import Login


# Data is stored on the session in memory
@route('/list')
def your_list():
    session = request.environ.get('beaker.session')
    if 'todo_list' in session:
        todo_list = session['todo_list']
    else:
        todo_list = []
        session['todo_list'] = todo_list
    return template('list', todo_list=todo_list)