from flask import Flask, request, render_template
import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user
from flask_socketio import SocketIO, disconnect
import config
import functools
app = Flask(__name__)
app.config.from_object(config.DevelopmentConfig)
db = SQLAlchemy(app)

socketio = SocketIO(app)

import models

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

def authenticated_only(f):
    @functools.wraps(f)
    def wrapped(*args, **kwargs):
        if not current_user.is_authenticated:
            disconnect()
        else:
            return f(*args, **kwargs)
    return wrapped

@socketio.on('sendMessage')
@authenticated_only
def handle_message(message):
    new_msg = models.Message(message['data'],current_user.id,1)
    db.session.add(new_msg)
    db.session.commit()
    print(new_msg)

@socketio.on('my event')
def handle_event(json):
    print("recieved json: " + str(json))

@login_manager.user_loader
def load_user(user_id):
    return models.User.query.get(int(user_id))
# Alot of the code below has been taken from the official documentation of flask
# Feel free to go ahead and learn from the website. Documentations are a brilliant way to do so.
# But please do mention where you take some code from. No Plagiarism will be tollerated if, it comes in notice

from auth import auth as auth_blueprint
from main import main as main_blueprint
from chat import chat as chat_blueprint

app.register_blueprint(auth_blueprint)
app.register_blueprint(main_blueprint)
app.register_blueprint(chat_blueprint)

if __name__ == '__main__':
    socketio.run(app)
