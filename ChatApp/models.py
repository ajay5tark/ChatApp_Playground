from flask_login import UserMixin
from app import db
import datetime

class User(UserMixin, db.Model):
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True} 
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))
    messages = db.relationship('Message', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}: {}>'.format(self.id, self.name)

class Message(db.Model):
    __tablename__ = 'msgs'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(2000))
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    date = db.Column(db.DateTime(timezone=True), default=datetime.datetime.now)
    msg_type = db.Column(db.Integer)

    def __init__(self, c, sid, t):
        self.content = c
        self.sender_id = sid
        self.msg_type = t
    
    def __repr__(self):
        return '<Message {}: {}>'.format(self.id, self.content)
    
