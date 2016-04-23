from flask.ext.wtf import Form, RecaptchaField
from wtforms import TextAreaField, TextField, StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, EqualTo, Email
from myapp.models import User, Post

from wtforms.ext.appengine.db import model_form
from wtforms import validators



class LoginForm(Form):
    email = TextField('Email address', [DataRequired(), Email()])
    password = PasswordField('Password', [DataRequired()])


class RegisterForm(Form):

    email = TextField('Email address', [DataRequired(), Email()])
    username = TextField('Username', [DataRequired()])
    password = PasswordField('Password', [DataRequired()])


    def __init__(self, original_username, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.original_username = original_username

    def validate(self):
        if not Form.validate(self):
            return False
        if self.username.data == self.original_username:
            return True
        user = User.query.filter_by(username = self.username.data).first()
        if user != None:
            self.username.errors.append('This nickname is already in use. Please choose another one.')
            return False
        
        return True


class UserForm(Form):

    email = TextField('Email address', [DataRequired(), Email()])
    username = TextField('Username', [DataRequired()])
    address = TextField('Address')

   
    def __init__(self, original_nickname, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.original_username = original_username

    def validate(self):
        if not Form.validate(self):
            return False
        if self.username.data == self.original_username:
            return True
        user = User.query.filter_by(username = self.username.data).first()
        if user != None:
            self.username.errors.append('This nickname is already in use. Please choose another one.')
            return False
        return True



class PostForm(Form):
    title = StringField('Title', [DataRequired()])
    body = TextAreaField('Body', [DataRequired()])



