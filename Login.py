# Basic framework for login request, single hardcoded user should be fine for
# initial sprint to KISS

from bottle import run, get, post, request, redirect
import YourList

@get('/') 
def login():
    return '''
        <form action="/" method="post">
            Username: <input name="username" type="text" /><br>
            Password: <input name="password" type="password" /><br>
            <input value="Login" type="submit" />
        </form>
    '''

@post('/')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        redirect("/list")
        #  return "<p>Your login information was correct.</p>"
    else:
        return "<p>Login failed.</p>"
    
def check_login(username, password):
    if username == "User" and password == "Pa55w0rd":
        return True
    else:
        return False
    
run(host='localhost', port=8080, debug=True)