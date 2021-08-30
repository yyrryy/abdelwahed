from flask import (
    render_template,
    request,
    redirect,
    url_for,
    Blueprint)


cvbuilder = Blueprint('cvbuilder', __name__, url_prefix='/cvbuilder')


@cvbuilder.route('/')
def home():
    return '<h1>Comming soon!</h1>'