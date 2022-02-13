from flask import (
    flash,
    render_template,
    request,
    redirect,
    url_for,
    Blueprint,
    session,
    jsonify,
    send_file
    
)
import functools
import json
from personal_ import bcrypt, db
from personal_.admin.funcs import convertor, refactor
from personal_.models import Admin, Posts, Projects, Quiz
from random import randint, choice


admin = Blueprint('admin', __name__, url_prefix='/admin')


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





@admin.route('/')
@login_required
def adminpanel():
    print(session)
    """ admin panel """
    #get posts
    posts = Posts.query.order_by(Posts.id.desc())
    projects = Projects.query.order_by(Projects.id.desc())
    quizes = Quiz.query.order_by(Quiz.id.desc())
    return render_template('admin/admin.html', 
    posts=posts,
    projects=projects,
    quizes=quizes,
    title='Admin panel')



@admin.route("/login", methods=["GET", "POST"])
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
            return redirect(url_for("admin.adminpanel"))
        
        return render_template("admin/login.html")
    elif session.get('user_id') is not None:
        return redirect(url_for("admin.adminpanel"))
    else:
        return render_template("admin/login.html")


#create project
@admin.route("/createproject", methods=["GET", "POST"])
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
        data = request.form['data']
        link = request.form['link']
        project = Projects(title=title, cat=cat, data=data, link=link)
 
        db.session.add(project)
        db.session.commit()
        flash(f'project #{project_id} added', 'success')
        return redirect(url_for('admin.createproject'))
    return render_template("admin/createproject.html", 
        project_id = project_id,
        title=f'craete project #{project_id}')
 

@admin.route('/updatepr/<id>', methods=['GET', 'POST'])
@login_required
def updatepr(id):
    p= Projects.query.get(id)
    if request.method=='POST':
        p.title = request.form['title']
        p.data = request.form['data']
        p.link = request.form['link']
        p.cat = request.form['cat']
        db.session.commit()
        flash(f'project #{id} updated', 'success')
        return redirect(url_for('admin.adminpanel'))
    return render_template('admin/createproject.html', update=True, p=p)

#delete project
@admin.route("/deletepr/<id>", methods=["POST"])
@login_required
def deletepr(id):
    project = Projects.query.get(id)
    db.session.delete(project)
    db.session.commit()
    flash(f'project #{id} deleted', 'danger')
    return redirect(url_for("admin.adminpanel"))
    


#create a post
@admin.route("/createpost", methods=["GET", "POST"])
@login_required
def create():
    
    post_id = Posts.query.order_by(Posts.id.desc()).first()
    if post_id:
        post_id = str(int(post_id.id) + 1)
    else:
        post_id = "1"
    if request.method == "POST":
        title = request.form["title"]
        lang = request.form["lang"]
        content = request.form["content"].strip()
        c=convertor(content)
        data = Posts(title=title, votes=randint(0, 20), content=c, lang=lang)
        db.session.add(data)
        db.session.commit()
        flash("Success, your post is live.", 'success')
        return redirect(url_for("admin.create"))
            

    else:
        return render_template("admin/create.html", 
        post_id=post_id, 
        update=False,
        title=f'craete post #{post_id}')



@admin.route('/upvote/<int:id>', methods=['POST'])
def upvote(id):
    p=Posts.query.get(id)
    p.votes+=1
    db.session.commit()
    return jsonify({
        'st': 'OK'
    })








#Updating a post
@admin.route("/edit/<postid>", methods=["GET", "POST"])
@login_required
def edit(postid):
    post = Posts.query.get(postid)
    if request.method == 'POST':
        post.title = request.form['title']
        post.content = convertor(request.form['content'].strip())
        db.session.commit()
        flash(f'post #{postid} updated', 'success')
        return redirect(url_for("admin.adminpanel"))
    else:
        return render_template("admin/create.html", 
        p=post,
        content=refactor(post.content),
        update=True,
        title=f'Update post #{postid}')
    


#delete a post
@admin.route("/deletepost/<postid>", methods=["POST"])
@login_required
def delete(postid):
    post = Posts.query.get(postid)
    print('=====>', post)
    db.session.delete(post)
    db.session.commit()
    flash(f'post #{postid} deleted', 'danger')
    return redirect(url_for("admin.adminpanel"))
    
@admin.route('/docs')
def docs():
    return render_template('admin/docs.html')

@admin.route('/inscription')
def inscription():
    path='static/grgdh4x65f4hwerg.pdf'
    return send_file(path, as_attachment=True)


#quizz
@admin.route('/createquiz', methods=['GET', 'POST'])
def createquiz():
    if request.method=='POST':
        title=request.form['title']
        questions=json.dumps(request.form.getlist('questions'))
        options=request.form.getlist('options')
        answers=json.dumps([int(i) for i in (request.form.getlist('answers'))])
        o=[]
        for i in options:
            l=[a.strip() for a in i.split(',')]
            o.append(l)
        db.session.add(Quiz(title=title, questions=questions, answers=answers, options=json.dumps(o)))
        db.session.commit()
        flash(f'Quiz for {title} created', 'success')
        return redirect(url_for('admin.createquiz'))
    return render_template('admin/createquiz.html')
    
@admin.route('/editquiz/<id>', methods=['GET', 'POST'])
def editquiz(id):
    quiz=Quiz.query.get(id)

    if request.method=='POST':
        quiz.title=request.form['title']
        quiz.questions=json.dumps(request.form.getlist('questions'))
        quiz.answers=json.dumps([int(i) for i in (request.form.getlist('answers'))])
        options=request.form.getlist('options')
        o=[]
        for i in options:
            l=[a.strip() for a in i.split(',')]
            o.append(l)
        quiz.options=json.dumps(o)

        db.session.commit()
        # flash(f'quiz {quiz.title} edited', 'success')
        return redirect(url_for('admin.editquiz', id=id))

    questions=json.loads(quiz.questions)
    options=json.loads(quiz.options)
    answers=json.loads(quiz.answers)
    t=quiz.title
    return render_template('admin/createquiz.html', update=True, questions=questions, id=id,options=options, answers=answers, title=f'Edit {t} quiz', t=t)





