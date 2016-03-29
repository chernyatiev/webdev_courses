from flask.ext.wtf import Form, RecaptchaField
from wtforms import TextAreaField, TextField, StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, EqualTo, Email

class LoginForm(Form):
    email = TextField('Email address', [DataRequired(), Email()])
    password = PasswordField('Password', [DataRequired()])

class PostForm(Form):
    title = StringField('Title', [DataRequired()])
    body = TextAreaField('Body', [DataRequired()])

