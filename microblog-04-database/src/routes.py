from flask import render_template, flash, redirect, url_for

from src import app, db
from src.forms import LoginForm
from src.models import User, Post

@app.route('/')
@app.route('/index')
def index():
    user = User.query.all()
    posts = Post.query.all()
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/init_db')
def init_db():
    """For use on command line for setting up
    the database.
    """
    db.drop_all()
    db.create_all()
    return redirect(url_for('index'))



@app.route('/generate_fake')
def generate_fake():
    User.generate_fake(100)
    Post.generate_fake(100)
    return redirect(url_for('index'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
