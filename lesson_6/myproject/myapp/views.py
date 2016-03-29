from flask import request, render_template, session, redirect, url_for
from myapp import app
from forms import  LoginForm, PostForm
from models import User, Post, db
from werkzeug import check_password_hash, generate_password_hash
import flask.ext.login as flask_login


login_manager = flask_login.LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def user_loader(id):
    try:
        user = User.query.filter_by(id=id).first()
        return user
    except:
        return None
    


@app.route('/')
def index():
    return 'Hello World!'


@flask_login.login_required
@app.route('/home')
def home():
    user = flask_login.current_user
    return 'hello ' + user.email

@flask_login.login_required
@app.route('/create_post', methods=['GET', 'POST'])
def create_post():
    form = PostForm(request.form)
    if form.validate_on_submit():
        post = Post(title=form.title.data, body = form.body.data, author = flask_login.current_user)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('posts'))
    return render_template("create_post.html", form = form)


@app.route('/posts')
def posts():
    posts = Post.query.all()
    return render_template("posts.html", posts=posts) 


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            flask_login.login_user(user)
            return redirect(url_for('home'))
    return render_template("login.html", form=form)
