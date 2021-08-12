from flask import (
    render_template,
    request,
    redirect,
    url_for,
    Blueprint,
    Markup
)
from personal_.models import Posts



log = Blueprint('blog', __name__, url_prefix='/blog')


@log.route('/')
def blog():
    return render_template('blog/blog.html', 
    posts=Posts.query.all())


@log.route('/post/<int:id>/<name>')
def post(id, name):
    p=Posts.query.get(id)
    
    return render_template('blog/post.html', 
    content=Markup(p.content),
    title=p.title, 
    post=p,
    next=Posts.query.get(p.id+1),
    previous=Posts.query.get(p.id-1))