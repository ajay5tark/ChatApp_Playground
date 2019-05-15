from flask import Blueprint, render_template, redirect, url_for, request
from . import db
from flask_login import login_required

chat = Blueprint('chat', __name__)

@chat.route('/chat', methods=['GET'])
@login_required
def chat():
    return "Chat"   