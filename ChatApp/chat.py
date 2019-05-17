from flask import Blueprint, render_template, redirect, url_for, request
from app import db
from flask_login import login_required


chat = Blueprint('chat', __name__)

@chat.route('/lobby', methods=['GET'])
@login_required
def lobby():
    return render_template('chat.html')   