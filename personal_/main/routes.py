from flask import (
    jsonify,
    render_template,
    Blueprint,
    request,
    send_file,
)
from personal_.models import Posts, Projects
import os


main = Blueprint('main', __name__)


@main.route('/')
def index():
    # get 4 posts
    posts = Posts.query.order_by(Posts.votes.desc()).limit(4)

    projects = Projects.query.order_by(Projects.id.desc())

    return render_template('h2.html', 
    posts=posts,
    projects=projects)


@main.route('/project1')
def peoject1():
    return render_template('project1.html', title='Project1 - static website')


# @main.route('/projects')
# def projects():
#     projects = Projects.query.all()
#     return render_template('blog/blog.html', 
#     title='Projects',
#     projects=projects)


# @main.route('/cv1')
# def cv1():
#     path='static/thiscv.pdf'
#     return send_file(path, as_attachment=True)


@main.route('/cv')
def cv():
    path='static/cv_abdelouahed.pdf'
    return send_file(path, as_attachment=True)




@main.route('/ecom')
def ecom():
    return render_template('ecom.html')

@main.route('/calc', methods=['POST'])
def calculate():
    data=request.get_json()
    n=data['n']
    return jsonify({
        "n": 5
    })
