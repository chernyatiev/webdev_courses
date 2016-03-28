import flask
import flask.ext.login as flask_login
from flask.ext.wtf import Form
from wtforms import TextField, BooleanField
from wtforms.validators import DataRequired
from flask import Flask, redirect, url_for, request, render_template


app = flask.Flask(__name__)
app.secret_key = 'super secret string'  # Change this!


login_manager = flask_login.LoginManager()
login_manager.init_app(app)


users = {'chernyatiev@gmail.com': {'password': 'secret'}}


class LoginForm(Form):
    email = TextField('email', validators = [DataRequired()])
    password=TextField('password', validators = [DataRequired()])


class User(flask_login.UserMixin):
    pass

@login_manager.user_loader
def user_loader(email):
    if email not in users:
        return

    user = User()
    user.id = email
    return user


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if flask.request.method == 'GET':
        return render_template("login.html", form=form)

    email = flask.request.form['email']
    if flask.request.form['password'] == users[email]['password']:
        user = User()
        user.id = email
        flask_login.login_user(user)
        return flask.redirect(flask.url_for('protected'))

    return 'Bad login'


@app.route('/protected')
@flask_login.login_required
def protected():
    return 'Logged in as: ' + flask_login.current_user.id


@app.route('/logout')
def logout():
    flask_login.logout_user()
    return 'Logged out'



@login_manager.unauthorized_handler
def unauthorized_handler():
    return redirect(url_for('login'))


if __name__ == "__main__":
    app.debug = True
    app.run()
