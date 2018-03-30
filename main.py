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

    if username = '':
        username_error = 'That is not a valid username'
    else:
        

app.run()