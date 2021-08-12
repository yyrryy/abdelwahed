from flask import (
    flash,
    render_template,
    request,
    redirect,
    url_for,
    Markup,
    Blueprint,
    abort,
    session
)
from personal_.models import Posts, Projects

main = Blueprint('main', __name__)


@main.route('/')
def index():
    # get 4 posts
    posts = Posts.query.order_by(Posts.id.desc()).limit(4)
    projects = Projects.query.order_by(Projects.id.desc()).limit(4)

    return render_template('main/home.html', 
    posts=posts,
    projects=projects)

