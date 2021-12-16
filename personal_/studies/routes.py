from flask import (
    render_template,
    Blueprint,
    request
)
from flask.json import jsonify

from personal_.studies.funcs import strss, tr





st = Blueprint('studies', __name__, url_prefix='/studies')


@st.route('/')
def studies():
    return render_template('studies/home.html')


@st.route('/spoken')
def spoken():
    return render_template('studies/spoken.html')

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
        ns, s, press= strss(word)
        print(ns)
        return jsonify({
            'n':str(ns),
            's':str(s),
            'press':str(press)
        })


@st.route('/grammar')
def grammar():
    return render_template('studies/grammar.html')


@st.route('/guided')
def guided():
    return render_template('studies/guided.html', title='Terms')



@st.route('/guided/shorts')
def shorts():
    return render_template('studies/shorts.html', title='Short stories')
