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
import functools
from personal_ import bcrypt, db, limiter
from personal_.models import Admin, Posts, Projects
import os
from PIL import Image

bp = Blueprint('admin', __name__, url_prefix='/admin')

def login_required(view):
    """
    Creates wrap that prevents unlogged in viewers from accessing admin-only routes.
    """
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if session.get('user_id') is None:
            return redirect(url_for('admin.login'))

        return view(**kwargs)

    return wrapped_view



@bp.route("/", methods=["GET"])
@login_required
def admin():
    """
    Renders the admin panel.
    """
    return redirect(url_for("admin.adminpanel"))

@bp.route('/admin')
@login_required
def adminpanel():
    """ admin panel """
    #get posts
    posts = Posts.query.order_by(Posts.id.desc())
    projects = Projects.query.order_by(Projects.id.desc())
    return render_template('admin/admin.html', 
    posts=posts,
    projects=projects,
    title='Admin panel')



@bp.route("/login", methods=["GET", "POST"])
@limiter.limit("2 per day")
def login():
    """
    Logs a user in (given the email and password are correct).
    """
    if request.method == "POST":
        username = request.form["username"]
        user = Admin.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.pswd, request.form["password"]):

            session.clear()
            session['user_id'] = user.username
            flash("What would you like to do today?")
            return redirect(url_for("admin.admin"))
        return render_template("admin/login.html", message="Username or password incorrect.")
    elif session.get('user_id') is not None:
        return redirect(url_for("admin.admin"))
    else:
        return render_template("admin/login.html")


#create project
@bp.route("/createproject", methods=["GET", "POST"])
@login_required
def createproject():
    project_id = Projects.query.order_by(Projects.id.desc()).first()
    if project_id:
        project_id = str(int(project_id.id) + 1)
    else:
        project_id = "1"
    if request.method == 'POST':
        title = request.form['title']
        cat = request.form['cat']
        link = request.form['link']
        project = Projects(title=title, cat=cat, link=link)
        
        img = request.files["img"]
        
        i = Image.open(img)
        size = (500, 500)
        i.thumbnail(size)
        
        #picture_path = os.path.join("personal_", "static", "images", "projects")
        
        with open(f'personal_/static/images/projects/{project_id}.jpg', 'w', encoding='utf-8') as file:
            i.save(file)
        db.session.add(project)
        db.session.commit()
        flash(f'project #{project_id} added')

        return redirect(url_for("admin.admin")) 
    return render_template("admin/createproject.html", 
        project_id = project_id,
        title=f'craete project #{project_id}')



#delete project
@bp.route("/deletepr/<id>", methods=["POST"])
@login_required
def deletepr(id):
    project = Projects.query.get(id)
    if request.method=='POST':
        db.session.delete(project)
        db.session.commit()
        flash(f'project #{id} deleted')
        return redirect(url_for("admin.admin"))
    


#create a post
@bp.route("/create", methods=["GET", "POST"])
@login_required
def create():
    """
    Get: renders the screen where the user can create a new post.
    Post: Adds the new post's information to the post and body images database.
    """
    update = False
    post_id = Posts.query.order_by(Posts.id.desc()).first()
    if post_id:
        post_id = str(int(post_id.id) + 1)
    else:
        post_id = "1"
    if request.method == "POST":
        title = request.form["title"]
        lang = request.form["lang"]
        Slogan = request.form["Slogan"]
        content = request.form["content"]
        if title and Slogan and content:
            data = Posts(title=title, Slogan=Slogan, content=content, lang=lang)
            db.session.add(data)
            db.session.commit()
            flash("Success, your post is live.")
            return redirect(url_for("admin.admin"))
        else:
            return redirect(url_for("admin.create"))
            

    else:
        return render_template("admin/create.html", 
        post_id=post_id, 
        update=update,
        title=f'craete post #{post_id}')











#Updating a post
@bp.route("/edit/<postid>", methods=["GET", "POST"])
@login_required
def edit(postid):
    update = True
    post = Posts.query.get(postid)
    if request.method == 'POST':
        post.title = request.form['title']
        post.Slogan = request.form['Slogan']
        post.content = request.form['content']
        db.session.commit()
        flash(f'post #{postid} updated')
        return redirect(url_for("admin.admin"))
    else:
        return render_template("admin/create.html", 
        posttitle=post.title,
        postid=postid,
        postslogan = post.Slogan,
        postcontent = post.content,
        post_id=postid,
        update=update,
        title=f'Update post #{postid}')
    


#delete a post
@bp.route("/delete/<postid>", methods=["POST"])
@login_required
def delete(postid):
    post = Posts.query.get(postid)
    if request.method=='POST':
        db.session.delete(post)
        db.session.commit()
        flash(f'post #{postid} deleted')
        return redirect(url_for("admin.admin"))
    
