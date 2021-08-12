from flask import render_template , request, Markup
from . import app, bcrypt
from personal_.models import Posts, Projects
import os
@app.route('/')
def index():
    # get 4 posts
    posts = Posts.query.order_by(Posts.id.desc()).limit(4)
    projects = Projects.query.order_by(Projects.id.desc()).limit(4)

    return render_template('home.html', 
    posts=posts,
    projects=projects)


@app.route('/blog')
def blog():
    # get posts from db
    return render_template('blog.html', title='blog')


@app.route('/post/<postid>')
def post(postid):

    #get the post maches the id in the db
    post = Posts.query.get(postid)





    content = Markup(post.content)

    

    try:
        prev = Posts.query.get(int(postid)-1)
        nxt = Posts.query.get(int(postid)+1)
    except:
        pass
    
    return render_template('post.html', 
    post=post, 
    content=content, 
    next=nxt, 
    previous=prev,
    title=f'read post #{postid}')

