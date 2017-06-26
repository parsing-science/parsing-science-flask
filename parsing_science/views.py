from flask import render_template

from parsing_science import app


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/projects/')
def projects():
    return render_template('projects.html')


@app.route('/talks/')
def talks():
    return render_template('talks.html')


@app.route('/contact/')
def contact():
    return render_template('contact.html')
