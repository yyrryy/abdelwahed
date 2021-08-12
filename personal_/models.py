from . import db
from datetime import datetime


class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    slogan = db.Column(db.String, nullable=False)
    content = db.Column(db.Text, nullable=False)
    lang = db.Column(db.String(2), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)


class Projects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    data = db.Column(db.String(50), nullable=False)
    cat = db.Column(db.String(50), nullable=False)
    link = db.Column(db.String(50), nullable=False)




class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    pswd = db.Column(db.String(120), nullable=False)
    
    
