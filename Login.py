# import bottle
from bottle import route, run, request, template, post, redirect, static_file, app, get 
from beaker.middleware import SessionMiddleware


# Load session before calling imports for the other pages
session_opts = {
    'session.type': 'memory',
    'session.auto': True,
}

# Once you wrap the bottle app in the SessionMiddleware app you'll have to reference bottle directly when you make a bottle call (like bottle.route())
app = SessionMiddleware(app(), session_opts)

# from YourList import your_list
import ItemUpdate
import YourList


@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./views/static')


@route('/')
def login():
    return template('login')


@post('/')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')

    if check_login(username, password):
        redirect('/list')
    else:
        return "<p>Login failed.</p>"


def check_login(username, password):
    if username == "User" and password == "password":
        return True
    else:
        return False
    

if __name__ == '__main__':
    run(host='localhost', port=8080, app=app, debug=True, reloader=True)