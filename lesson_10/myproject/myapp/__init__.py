from flask import Flask
import os


app = Flask(__name__, static_folder='static')

import myapp.views

app.secret_key = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['UPLOAD_FOLDER'] = 'myapp/static/uploads'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True



