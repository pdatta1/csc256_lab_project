# Basic framework for login request, single hardcoded user should be fine for
# initial sprint to KISS

import bottle
from bottle import Bottle, route, run, get, post, request, redirect
from beaker.middleware import SessionMiddleware

# Load session before calling imports for the other pages
session_opts = {
    'session.type': 'memory',
    'session.auto': True,
}
# Once you wrap the bottle app in the SessionMiddleware app you'll have to reference bottle directly when you make a bottle call (like bottle.route())
app  = SessionMiddleware(bottle.app(), session_opts)

import YourList
import ItemUpdate

# Simple login function, use f string as best practice for dynamic strings
@bottle.get('/') 
def login():
    return f'''
        <form action="/" method="post">
            Username: <input name="username" type="text" /><br>
            Password: <input name="password" type="password" /><br>
            <input value="Login" type="submit" />
        </form>
    '''

# Successful login causes a redirect, failure displays fail message
@bottle.post('/')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        redirect('/list')
        #  return "<p>Your login information was correct.</p>"
    else:
        return "<p>Login failed.</p>"
    
# Login info is hard coded at this point
def check_login(username, password):
    # Login detail are currently hardcoded for this sprint
    if username == "User" and password == "Pa55w0rd":
        return True
    else:
        return False

# command that causes the bottle server to run app=app causes the function to see the SessionManager app as a bottle app
if __name__ == '__main__':
    bottle.run(host='localhost', port=8080, app=app, debug=True)