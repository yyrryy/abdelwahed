from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt



app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://hwxqgwisgorxov:ef788a743b9b4c0cd306bc335287f0d3f7c84c8d26b1fef2e6c842635911b735@ec2-54-145-224-156.compute-1.amazonaws.com:5432/d1kuss1n29ut3c'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY']='$2b$12$wUSYAe3hTC6QdaYe2JdrZO8yk/hM4BhXGAYhCZBetA0CKQAxQfNH2'

#mail configuration


db = SQLAlchemy(app)
bcrypt  = Bcrypt(app)

from personal_.admin.routes import admin
from personal_.main.routes import main
from personal_.blog.routes import log

app.register_blueprint(admin)
app.register_blueprint(main)
app.register_blueprint(log)

