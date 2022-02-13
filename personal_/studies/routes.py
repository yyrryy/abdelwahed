from flask import (
    flash,
    make_response,
    redirect,
    render_template,
    Blueprint,
    request,
    session,
    url_for
)
from flask.json import jsonify
from itsdangerous import json
from personal_.models import Quiz, Students

from personal_.studies.funcs import strss, tr, verb
from personal_ import bcrypt, db
from datetime import datetime, timedelta





st = Blueprint('studies', __name__, url_prefix='/studies')





@st.route('/')
def studies():
    return render_template('studies/t.html')




@st.route('/transcribe', methods=['POST'])
def transcribe():
    if request.method == "POST":
        word=request.form['word']
        mp, tran= tr(word)
        return jsonify({
            'tran':tran,
            'mp':mp
        })


@st.route('/stress', methods=['POST'])
def stress():
    if request.method == "POST":
        word=request.form['word']
        ns, press= strss(word)
        print(ns)
        return jsonify({
            'n':str(ns),
            'press':str(press)
        })

@st.route('/getverb', methods=['POST'])
def getverb():
    if request.method == "POST":
        word=request.form['word']
        data= verb(word)
        return jsonify({
            "data":data
        })


@st.route('/s1/grammar')
def grammar():
    return render_template('studies/lesson.html', titel='Grammar')
@st.route('/grammar/tenses')
def tenses():
    return render_template('studies/grammar/tenses.html', title='Tenses')
@st.route('/grammar/time')
def time():
    return render_template('studies/grammar/time.html', title='Time clauses')
@st.route('/grammar/modals')
def modals():
    return render_template('studies/grammar/modals.html', title='Time clauses')



# s1

@st.route('/s1/guided')
def guided():
    return render_template('studies/lesson.html', title='Guided reading')
@st.route('/guided/shorts')
def shorts():
    return render_template('studies/guided/shorts.html', title='Short stories')
@st.route('/guided/terms')
def terms():
    return render_template('studies/guided/terms.html', title='Literature terms')


@st.route('/s1/reading')
def reading():
    return render_template('studies/lesson.html', title='guided reading')


@st.route('/s1/spoken')
def spoken():
    return render_template('studies/lesson.html', title='Spoken english')

@st.route('/s1/writing')
def writing():
    return render_template('studies/lesson.html', title='Writing')


@st.route('/s1/lang1')
def language():
    return render_template('studies/lesson.html', title='Language et comm.')


@st.route('/s1/study')
def study():
    return render_template('studies/lesson.html', title='Study skills')


# s2
@st.route('/s2/reading2')
def reading2():
    return render_template('studies/lesson.html', title='Reading2')

@st.route('/s2/grammar2')
def grammar2():
    return render_template('studies/lesson.html', title='grammar2')

@st.route('/s2/culture')
def culture():
    return render_template('studies/lesson.html', title='culture')

@st.route('/s2/lang2')
def lang2():
    return render_template('studies/lesson.html', title='lang2')

@st.route('/s2/somp1')
def somp1():
    return render_template('studies/lesson.html', title='somp1')

@st.route('/s2/communication')
def communication():
    return render_template('studies/lesson.html', title='communication')

@st.route('/s2/business')
def business():
    return render_template('studies/lesson.html', title='business')






# quizes
@st.route('/quizes')
def quizes():
    quizes=Quiz.query.all()
    if 'userid' in session:
        rank=Students.query.order_by(Students.score.desc()).limit(10).all()
        user=Students.query.get(int(session['userid']))
        return render_template('studies/quizes.html', title='Quizes', user=user, quizes=quizes, len=len, json=json, rank=rank, enumerate=enumerate)
    flash('Holy crap! you need to login to take quizes.', 'warning')
    return render_template('studies/quizes.html', title='Quizes', user=False, quizes=quizes, json=json, len=len)
@st.route('/quiz/<id>')
def quiz(id):
    if 'userid' in session:
        user=Students.query.get(int(session['userid']))
        quiz=Quiz.query.get(id)
        options=json.loads(quiz.options)
        questions=json.loads(quiz.questions)
        return render_template('studies/quiz.html', 
        quiz=quiz, 
        options=options, 
        enumerate=enumerate,
        questions=questions,
        len=len(questions),
        user=user, 
        title=f'{quiz.title} Quiz',
        rank=Students.query.order_by(Students.score.desc()).limit(10).all(),
        )
    else: return '<h1>You are not logged in</h1>'
@st.route('/score/<id>', methods=['POST'])
def score(id):
    quiz=Quiz.query.get(id)
    answers=json.loads(quiz.answers)
    data=request.get_json()
    ans=data['ans']
    user=Students.query.get(int(data['userid']))
    print(user)
    correct=0
    coef=3 if quiz.id==1 or quiz.id==7 else 2
    for i in range(len(answers)):
        if ans[i]==answers[i]:
            correct+=1
    res= make_response(jsonify({
        'score': correct,
        "rate":correct*100/len(answers),
        "points": correct*coef
    }))
    user.score+=correct*coef
    db.session.commit()
    res.set_cookie(f'test{quiz.id}', 'Answered', expires= datetime.now() + timedelta(hours=24))
    return res


# auth
@st.route("/login", methods=["POST"])
def login():
    """
    Logs a user in (given the email and password are correct).
    """

    if request.method=='POST':
        username = request.form["username"]
        user = Students.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.pswd, request.form["pswd"]):
            session['userid'] = user.id
            flash("Logged in", 'success')
            return redirect(url_for("studies.quizes"))
        flash('Username or passsword not correct!', 'warning')
        return redirect(url_for("studies.quizes"))
    else:
        return render_template("studies/login.html")

@st.route("/signup", methods=["POST"])
def signup():
    data=request.get_json()
    username = data["username"]
    semister = data["semister"]
    group = data["group"]
    pswd = bcrypt.generate_password_hash(data["pswd"]).decode('utf-8')
    db.session.add(Students(username=username, semister=semister, group=group, pswd=pswd))
    db.session.commit()
    flash('Account successfully created', 'success')
    return redirect(url_for("studies.quizes"))

@st.route('/checkuser', methods=['POST'])
def checkuser():
    data=request.get_json()
    u=Students.query.filter_by(username=data['user']).first()

    return jsonify({
        'taken':True if u else False
    })
    


