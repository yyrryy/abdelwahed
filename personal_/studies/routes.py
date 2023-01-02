from flask import (
    flash,
    make_response,
    redirect,
    render_template,
    Blueprint,
    request,
    session,
    url_for,
    Markup
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
    return render_template('studies/home.html', title='Flash Ait Melloul')




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





@st.route('/grammar1')
def grammar():
    return render_template('studies/grammar/grhome.html')
@st.route('/grammar/tenses')





@st.route('/guided')
def guided():
    return render_template('studies/guided/home.html', title='Guided reading')
@st.route('/guided/shorts')
def shorts():
    return render_template('studies/guided/shorts.html', title='Short stories')
@st.route('/guided/terms')
def terms():
    return render_template('studies/guided/terms.html', title='Literature terms')


@st.route('/reading')


@st.route('/')
def s1():
    return render_template('studies/semisters/s1.html')


@st.route('/reading1')
def reading():
    course='<h1>this is a course</h1>'
    return render_template('studies/lesson.html',
    course=Markup(course),
    title='Reading comp. precis 1')


@st.route('/spoken')
def spoken():
    return render_template('studies/lesson.html', title='Spoken english')

@st.route('/writing')
def writing():
    return render_template('studies/lesson.html', title='Writing')



@st.route('/language')

@st.route('/lang1')
def language():
    return render_template('studies/lesson.html', title='Language et comm.')


@st.route('/study')
def study():
    return render_template('studies/lesson.html', title='Study skills')






@st.route('/reading2')
def reading2():
    return render_template('studies/lesson.html', title='Reading2')

@st.route('/grammar2')
def grammar2():
    return render_template('studies/grammar2/home.html', title='grammar2')

@st.route('/culture')
def culture():
    return render_template('studies/lesson.html', title='culture')

@st.route('/lang2')
def lang2():
    return render_template('studies/lesson.html', title='lang2')

@st.route('/comp1')
def somp1():
    return render_template('studies/lesson.html', title='somp1')

@st.route('/communication')
def communication():
    return render_template('studies/lesson.html', title='communication')

@st.route('/business')
def business():
    return render_template('studies/lesson.html', title='business')






# quizes
@st.route('/quizes')
def quizes():
    quizes=Quiz.query.all()
    user=''
    if 'userid' in session:
        user=Students.query.get(int(session['userid']))
    else: user=Students.query.get(0)
    print(user)
    if user:
        rank=Students.query.order_by(Students.score.desc()).limit(10).all()
        return render_template('studies/quizes.html', title='Quizzes', user=user, quizes=quizes, len=len, json=json, rank=rank, enumerate=enumerate)
    return render_template('studies/quizes.html', title='Quizzes', user=False, quizes=quizes, json=json, len=len)
@st.route('/quiz/<id>')
def quiz(id):
    user=''
    if 'userid' in session:
        user=Students.query.get(int(session['userid']))
    else: user=Students.query.get(0)
    print(user)
    if user:
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
    else: return '<h1>Nothing to see here, you need to log in a jmmi</h1>'
@st.route('/score/<id>', methods=['POST'])
def score(id):
    quiz=Quiz.query.get(id)
    answers=json.loads(quiz.answers)
    data=request.get_json()
    ans=data['ans']
    user=Students.query.get(int(data['userid']))
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
    res.set_cookie(f'test{quiz.id}', 'Answered', expires= datetime.now() + timedelta(hours=2))
    return res


# auth
@st.route("/login", methods=["POST"])
def login():
    data=request.get_json()
    print('data', data)
    username=data['username']
    user=Students.query.filter_by(username=username).first()
    print('user;',user)
    if user and bcrypt.check_password_hash(user.pswd, data['password']):
        session['userid'] = user.id
        session['_remember'] = 'set'
        # return a json response
        return redirect(url_for('studies.quizes'))
    else:
        return jsonify({
            'message':'Invalid cridentials',
        })


@st.route("/signup", methods=["POST"])
def signup():
    data=request.get_json()
    username = data["username"]
    semister = data["semister"]
    group = data["group"]
    pswd = bcrypt.generate_password_hash(data["pswd"]).decode('utf-8')
    db.session.add(Students(username=username, semister=semister, group=group, pswd=pswd))
    db.session.commit()
    return jsonify({
        'valid':True,
    })

@st.route('/checkuser', methods=['POST'])
def checkuser():
    data=request.get_json()
    u=Students.query.filter_by(username=data['user']).first()

    return jsonify({
        'taken':True if u else False
    })

@st.route('/logout')
def logout():
    session.pop('userid', None)
    print(session)
    return redirect(url_for('studies.quizes'))
    


