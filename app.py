from flask import Flask, request
from flask_socketio import SocketIO
import os
from Util.login_methods import *

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

# Alot of the code below has been taken from the official documentation of flask
# Feel free to go ahead and learn from the website. Documentations are a brilliant way to do so.
# But please do mention where you take some code from. No Plagiarism will be tollerated if, it comes in notice

@app.route('/')
def hello():
    return "Hello World"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        attempt_login()
    else:
        show_login_form()

@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username


