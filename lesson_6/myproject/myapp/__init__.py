from flask import Flask
app = Flask(__name__)

import myapp.views
app.secret_key = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

