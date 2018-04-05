from flask import Flask, request, render_template
import cgi
import os
import jinja2

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('forms.html')

@app.route("/", methods=['POST'])
def signup():

    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify-password']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''

    if username = '':
        username_error = 'That is not a valid username'
    elif len(username) < 3 or len(username) > 20:
        username_error = 'That is not a valid username'
    elif " " in username:
        username_error = 'Please do not include spaces'

    if password = '':
        password_error = 'That is not a valid password'
    elif len(password) < 3 or len(password) > 20:
        password_error = 'That is not a valid password'
    elif " " in password:
        password_error = "Please do not include spaces"

    if verify_password = '':
        verify_error = 'Please provide a matching password'
    elif verify_password != password:
        verify_error = 'Your passwords do not match'

    if email 

    if not username_error and not password_error and not verify_error and not email_error:
        return render_template('welcome.html', username=username)

    else:
        return render_template('forms.html', username=)

app.run()