from flask import (
    render_template,
    Blueprint,
    request
)
from flask.json import jsonify

from personal_.studies.funcs import strss, tr, verb





st = Blueprint('studies', __name__, url_prefix='/studies')


@st.route('/')
def studies():
    return render_template('studies/home.html')




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
    return render_template('studies/grammar/grhome.html')
@st.route('/s1/grammar/tenses')
def tenses():
    return render_template('studies/grammar/tenses.html', title='Tenses')
@st.route('/s1/grammar/time')
def time():
    return render_template('studies/grammar/time.html', title='Time clauses')
@st.route('/s1/grammar/modals')
def modals():
    return render_template('studies/grammar/modals.html', title='Time clauses')







@st.route('/s1/guided')
def guided():
    return render_template('studies/guided/home.html')
@st.route('/s1/guided/shorts')
def shorts():
    return render_template('studies/guided/shorts.html', title='Short stories')
@st.route('/s1/guided/terms')
def terms():
    return render_template('studies/guided/terms.html', title='Literature terms')


@st.route('/s1/reading')
def reading():
    return render_template('studies/reading/home.html')


@st.route('/s1/spoken')
def spoken():
    return render_template('studies/spoken/home.html')

@st.route('/s1/writing')
def writing():
    return render_template('studies/writing/home.html', m='Writing')


@st.route('/s1/language')
def language():
    return render_template('studies/language/home.html', m='Language et comm.')


@st.route('/s1/study')
def study():
    return render_template('studies/study/home.html', m='Study skills')


