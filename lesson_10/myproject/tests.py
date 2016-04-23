import os
import unittest
from werkzeug import  generate_password_hash
from myapp import app
from myapp.models import db,User

class TestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test2.db'
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


    def test_homepage(self):
        rv = self.app.get('/')
        assert 'Hello World' in rv.data

    def test_add_user(self):
        user = User(email = 'admin@example.com', username = 'admin', password = generate_password_hash('123456'))
        db.session.add(user)
        db.session.commit()
	user2 = User.query.filter_by(username = 'admin').first()
        assert user ==  user2

    
    def login(self, email, password):
        return self.app.post('/login', data=dict(email=email, password=password), follow_redirects=True)

    def test_login(self):
        rv = self.login('admin@example.com', password = generate_password_hash('123456'))
        assert 'admin@example.com' in rv.data


if __name__ == '__main__':
    unittest.main()
