from flask.ext.wtf import Form, RecaptchaField
from wtforms import TextAreaField, TextField, StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, EqualTo, Email

class LoginForm(Form):
    email = TextField('Email address', [DataRequired(), Email()])
    password = PasswordField('Password', [DataRequired()])


class RegisterForm(Form):

    email = TextField('Email address', [DataRequired(), Email()])
    username = TextField('Username', [DataRequired()])
    password = PasswordField('Password', [DataRequired()])


class UserForm(Form):

    email = TextField('Email address', [DataRequired(), Email()])
    username = TextField('Username', [DataRequired()])
    address = TextField('Address')



class PostForm(Form):
    title = StringField('Title', [DataRequired()])
    body = TextAreaField('Body', [DataRequired()])



