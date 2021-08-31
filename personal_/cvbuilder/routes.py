from flask import (
    render_template,
    request,
    Blueprint)


cvbuilder = Blueprint('cvbuilder', __name__, url_prefix='/cvbuilder')


@cvbuilder.route('/')
def home():
    return render_template('cvbuilder/home.html')


@cvbuilder.route('/template', methods=['Post', 'Get'])
def template():
    template= request.form['template']
    return render_template('cvbuilder/template.html', title='Information')


@cvbuilder.route('/finalresul/<int:template>')
def finalresult(template):
    return 'final result'