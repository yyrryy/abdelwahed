from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://hwxqgwisgorxov:ef788a743b9b4c0cd306bc335287f0d3f7c84c8d26b1fef2e6c842635911b735@ec2-54-145-224-156.compute-1.amazonaws.com:5432/d1kuss1n29ut3c'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY']='$2b$12$wUSYAe3hTC6QdaYe2JdrZO8yk/hM4BhXGAYhCZBetA0CKQAxQfNH2'

#mail configuration


db = SQLAlchemy(app)
bcrypt  = Bcrypt(app)
limiter = Limiter(app, key_func=get_remote_address)



from personal_ import routes, admin

app.register_blueprint(admin.bp)

