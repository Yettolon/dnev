import unittest
from flask import url_for

from app.models import User
from app import create_app, db


class UserModelTest(unittest.TestCase):
    def setUp(self):    
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client(use_cookies=True)


    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()


    def test_password_setter(self):
        u = User(password='cat')
        self.assertFalse(u.password_hash is None)

    def test_no_password_getter(self):
        u = User(password = 'cat')
        with self.assertRaises(AttributeError):
            u.password
        
    def test_password_verification(self):
        u = User(password = 'cat')
        self.assertTrue(u.verify_password('cat'))
        self.assertFalse(u.verify_password('dog'))



    def test_password_salt_are_random(self):
        u = User(password = 'cat')
        u2 = User(password = 'cat')
        self.assertTrue(u.password_hash != u2.password_hash)

    def test_register_and_login(self):
            response = self.client.post(url_for('auth.register'), data={
                'email':'asdsd@asdsa.dsa',
                'username': 'john',
                'password':'cat',
                'password2':'cat',
            })
            self.assertTrue(response.status_code == 302)

