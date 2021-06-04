from flask import render_template , request, Markup
from . import app, bcrypt, ext
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

@ext.register_generator
def index():
    # Not needed if you set SITEMAP_INCLUDE_RULES_WITHOUT_PARAMS=True
    yield 'index', {}

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


# @app.route('/contact', methods=['POST'])
# def contact():
#     if request.method == 'POST':
#         name = request.form['name']
#         email = request.form['email']
#         subject = request.form['subject']
#         message = request.form['message']
          
#         try:
#             msg = Message(subject=subject,
#                     recipients=['aitaliabdelwahed@gmail.ocm'],
#                     body=f'message from : {name} \n email : {email} \n\n\n {message}')
#             mail.send(msg)  
#         except Exception as e:
#             print(e)
#             return 'error'
