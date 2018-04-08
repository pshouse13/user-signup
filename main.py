from flask import Flask, request, render_template
import cgi
import os
import jinja2
import re

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('forms.html')

@app.route("/signup", methods=['POST'])
def signup():

    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']
    
    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''
#username validation
    if username == '':
        username_error = 'That is not a valid username'
    elif len(username) < 3 or len(username) > 20:
        username_error = 'That is not a valid username'
    elif " " in username:
        username_error = 'Please do not include spaces'
#password validation
    if password == '':
        password_error = 'That is not a valid password'
    elif len(password) < 3 or len(password) > 20:
        password_error = 'That is not a valid password'
    elif " " in password:
        password_error = 'Please do not include spaces'
#verify password
    if verify_password == '':
        verify_error = 'Please provide a matching password'
    elif verify_password != password:
        verify_error = 'Your passwords do not match'
#email validation using new regex method
    if email != "": 
        if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
            email_error = "This is not a valid email"

    if not username_error and not password_error and not verify_error and not email_error:
        return render_template('welcome.html', username = username)

    else:
        return render_template('forms.html', username = username, username_error = username_error, 
        password_error = password_error, verify_error = verify_error, email = email, email_error = email_error)

app.run()