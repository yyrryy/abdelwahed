from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_sitemap import Sitemap



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY']='$2b$12$wUSYAe3hTC6QdaYe2JdrZO8yk/hM4BhXGAYhCZBetA0CKQAxQfNH2'

#mail configuration


db = SQLAlchemy(app)
bcrypt  = Bcrypt(app)
limiter = Limiter(app, key_func=get_remote_address)
ext = Sitemap(app)


from personal_ import routes, admin

app.register_blueprint(admin.bp)

