from flask import (
    render_template,
    request,
    redirect,
    url_for,
    Blueprint,
)
from personal_.models import Posts



log = Blueprint('blog', __name__, url_prefix='/blog')


@log.route('/')
def blog():
    return render_template('blog/blog.html', 
    posts=Posts.query.all())


@log.route('/post/<id>')
def post(id):
    p=Posts.query.get(id)
    
    return render_template('blog/post.html', 
    title=p.title, 
    post=p,
    next=Posts.query.get(p.id+1),
    previous=Posts.query.get(p.id-1))