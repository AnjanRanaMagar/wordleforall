
from . import db
from flask_login import UserMixin
from datetime import datetime

class User(UserMixin,db.Model):
    __table__name='user'
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(255),unique=True)
    password = db.Column(db.String(255))
    name = db.Column(db.String(1000))

class Score(db.Model):
    '''Helps to ceate a score board for our users.
    score: based on attempts, e.g if scored in 1st try will get (100 points = 5words*20points each)
    attempts: how many attempts was needed for correct guess.
    user_id: is a foreign key linking each score to a specific user in the User table.
    user: establishes a relationship between the Score and User models, allowing for easy 
            access between the two (e.g., accessing all scores of a user.'''
    __tablename__='Score'
    id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.Integer, nullable=False)
    attempts = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    time_taken = db.Column(db.Float, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('scores', lazy=True))