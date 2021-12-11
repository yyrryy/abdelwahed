from flask import (
    render_template,
    Blueprint,
)
from personal_.models import Posts, Projects
import os


main = Blueprint('main', __name__)


@main.route('/')
def index():
    # get 4 posts
    posts = Posts.query.order_by(Posts.votes.desc()).limit(4)
    projects = Projects.query.order_by(Projects.id.desc()).limit(4)

    return render_template('home.html', 
    posts=posts,
    projects=projects)

@main.route('/projects')
def projects():
    projects = Projects.query.all()
    return render_template('blog/blog.html', 
    title='Projects',
    projects=projects)


# @main.route('/resume')
# def resume():
#     path='static/thiscv.pdf'
#     return send_file(path, as_attachment=True)