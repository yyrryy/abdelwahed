from flask import (
    render_template,
    request,
    Blueprint)
from PIL import Image
cvbuilder = Blueprint('cvbuilder', __name__, url_prefix='/cvbuilder')


@cvbuilder.route('/')
def home():
    return render_template('cvbuilder/home.html')


@cvbuilder.route('/template', methods=['Post', 'Get'])
def template():
    id= request.form['template']
    return render_template('cvbuilder/temp.html', 
    title='Information',
    id=id)


@cvbuilder.route('/result/<int:id>')
def result(id):
    img= Image.open(request.form['img'])
    return render_template('cvbuilder/res'+str(id)+'.html',
    title="result")