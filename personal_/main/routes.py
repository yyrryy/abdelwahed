from flask import (
    jsonify,
    render_template,
    Blueprint,
    request,
    send_file,
)
from personal_.models import Posts, Projects, Laptops
import os


main = Blueprint('main', __name__)


@main.route('/')
def index():
    # get 4 posts
    posts = Posts.query.order_by(Posts.votes.desc()).limit(4)

    projects = Projects.query.order_by(Projects.id.desc())

    return render_template('h2.html', 
    posts=posts,
    projects=projects)


@main.route('/project1')
def peoject1():
    return render_template('project1.html', title='Project1 - static website')


# @main.route('/projects')
# def projects():
#     projects = Projects.query.all()
#     return render_template('blog/blog.html', 
#     title='Projects',
#     projects=projects)


# @main.route('/cv1')
# def cv1():
#     path='static/thiscv.pdf'
#     return send_file(path, as_attachment=True)


@main.route('/cv')
def cv():
    path='static/cv_abdelouahed.pdf'
    return send_file(path, as_attachment=True)




@main.route('/ecom')
def ecom():
    return render_template('ecom.html')

@main.route('/calc', methods=['POST'])
def calculate():
    data=request.get_json()
    n=data['n']
    return jsonify({
        "n": 5
    })


@main.route('/laptops')
def laptops():
    return render_template('laptops.html', title="Laptops")

# route to create admin
@main.route('/test')
def test():
    return render_template('test.html', title="test")


# filtration system
@main.route('/filter/<usage>/<price>/<ram>/<storage>')
def filter(usage, price, ram, storage):
    # get all laptops
    laptops = Laptops.query.all()
    # filter by usage
    if usage != 'all':
        laptops = [laptop for laptop in laptops if laptop.usage == usage]
    # filter by price
    if price != 'all':
        laptops = [laptop for laptop in laptops if laptop.price == price]
    # filter by ram
    if ram != 'all':
        laptops = [laptop for laptop in laptops if laptop.ram == ram]
    # filter by storage
    if storage != 'all':
        laptops = [laptop for laptop in laptops if laptop.storage == storage]
    return render_template('laptops.html', title="Laptops", laptops=laptops)