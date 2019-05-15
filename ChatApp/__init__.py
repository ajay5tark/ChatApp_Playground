from flask import Flask, request, render_template
import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.urandom(24)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost:5432/chatapp'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    # Alot of the code below has been taken from the official documentation of flask
    # Feel free to go ahead and learn from the website. Documentations are a brilliant way to do so.
    # But please do mention where you take some code from. No Plagiarism will be tollerated if, it comes in notice
    
    from .auth import auth as auth_blueprint
    from .main import main as main_blueprint
    
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)

    return app
