from flask import Blueprint, render_template

#from . import app

mod = Blueprint('core', __name__)

@mod.route('/')
def index():
    return render_template('core/index.html')


@mod.route('/about/')
def about():
    return render_template('core/about.html')


@mod.route('/projects/')
def projects():
    return render_template('core/projects.html')


@mod.route('/talks/')
def talks():
    return render_template('core/talks.html')


@mod.route('/contact/')
def contact():
    return render_template('core/contact.html')
