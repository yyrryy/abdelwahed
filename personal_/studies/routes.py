from flask import (
    render_template,
    Blueprint,
    request
)
from flask.json import jsonify

from personal_.studies.funcs import tr





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
        print(word)
        mp, tran= tr(word)
        return jsonify({
            'tran':tran,
            'mp':mp
        })

@st.route('/stree', methods=['POST'])
def stress():
    if request.method == "POST":
        word=request.form['word']
        print(word)
        mp, tran= tr(word)
        return jsonify({
            'tran':tran,
            'mp':mp
        })