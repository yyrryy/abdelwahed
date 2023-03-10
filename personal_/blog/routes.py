from flask import (
    jsonify,
    render_template,
    request,
    Blueprint,
    Markup,
    session
)
from personal_.models import Posts
from urllib.parse import urlparse
from personal_ import db


log = Blueprint('blog', __name__, url_prefix='/blog')


@log.route('/')
def blog():
    return render_template('blog/blog.html', 
    posts=Posts.query.order_by(Posts.votes.desc()).all(),
    title='My blog')


@log.route('/<int:id>/<string:name>')
def post(id, name):
    p=Posts.query.get(id)
    next=Posts.query.get(p.id+1)
    isadmin=session.get('isadmin'),
    
    if isadmin[0]:
        print('rr')
    previous=Posts.query.get(p.id-1)
    return render_template('blog/post.html', 
    content=Markup(p.content),
    title=p.title, 
    post=p,
    next=next,
    previous=previous,
    isadmin=isadmin[0],
    root = urlparse(request.host_url)
    )

@log.route('/upvote/<int:id>', methods=['POST'])
def upvote(id):
    p=Posts.query.get(id)
    v=p.votes
    p.votes+=1
    db.session.commit()
    return jsonify({
        'votes':v+1
    })