from flask import flash, request, jsonify, render_template, session, redirect, url_for, send_from_directory
from myapp import app
from forms import  LoginForm, PostForm, RegisterForm, UserForm
from models import User, Post, db
from werkzeug import check_password_hash, generate_password_hash, secure_filename
import flask.ext.login as flask_login
import os

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


@app.route('/calc')
def calc():
    return render_template('calc.html')

@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)



@flask_login.login_required
@app.route('/home')
def home():
    user = flask_login.current_user
    return render_template('home.html', user=user)


@flask_login.login_required
@app.route('/edit_profile', methods=['GET', 'POST'])
def edit_profile():
    user = flask_login.current_user
    form = UserForm()
    if form.validate_on_submit():
        user.email = form.email.data
        user.username = form.username.data
        user.address = form.address.data
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit_profile.html", form=form, user=user)

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
            flash('You are successfully logged')
            return redirect(url_for('home'))
    elif flask_login.current_user.is_authenticated:
        return redirect(url_for('home'))
    return render_template("login.html", form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data, password = generate_password_hash(form.password.data))
        db.session.add(user)
        db.session.commit()
        flask_login.login_user(user)
        flash('You are successfully register')    
        return redirect(url_for('home'))
    return render_template("register.html", form = form) 

@flask_login.login_required
@app.route("/logout")
def logout():
    flask_login.logout_user()
    return redirect(url_for('index'))


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join( app.config['UPLOAD_FOLDER'],filename))
            return "File was susessfully uploaded"
    return render_template("upload.html")


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


