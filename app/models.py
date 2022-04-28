from datetime import date
from email.policy import default
from flask import current_app, url_for
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from . import db, login_manager


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    # confirmed = db.Column(db.Boolean, default=False)
    records = db.relationship('RecordView', backref='records', lazy='dynamic')

    def __str__(self):
        return '<User %r>' % self.username
    
    @property
    def password(self):
        raise AttributeError('Ошибка')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class RecordView(db.Model):
    __tablename__ = 'record'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), index=True,)
    text = db.Column(db.Text(), default=None)
    data_pub = db.Column(db.Date, default=None, index=True)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __str__(self):
        return self.title




