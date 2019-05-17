from flask import Blueprint, render_template, redirect, url_for, request
import models
from flask_login import login_required


chat = Blueprint('chat', __name__)

@chat.route('/lobby', methods=['GET'])
@login_required
def lobby():
    Messages = models.Message.query.all()
    return render_template('chat.html', Messages=Messages)   
