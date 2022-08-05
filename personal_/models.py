from email.policy import default
from turtle import title
from . import db
from datetime import datetime
from random import randint

class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    content = db.Column(db.Text, nullable=False)
    lang = db.Column(db.String(2), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    votes= db.Column(db.Integer, default=randint(1, 10))


class Projects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    data = db.Column(db.Text, nullable=False)
    cat = db.Column(db.String(50), nullable=False)
    link = db.Column(db.String(50), nullable=False)
    
class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    pswd = db.Column(db.String(120), nullable=False)
        
class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(20), nullable=False)
    score=db.Column(db.Integer, default=0)
    pswd = db.Column(db.String(500), nullable=False)
    group = db.Column(db.String(2))
    semister = db.Column(db.String(2))
    
class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(20), nullable=False)
    questions=db.Column(db.Text)
    options=db.Column(db.Text)
    answers=db.Column(db.Text)
    explanations=db.Column(db.Text)

class Votes(db.Model):
    # voting system model
    id = db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(20), nullable=False)
    description=db.Column(db.Text)
    votes = db.Column(db.Integer, default=0)    # number of votes

# table related to studies
