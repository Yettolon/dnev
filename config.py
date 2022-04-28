import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or "\x12\xb6}\xaaugh\x1cwH\xd9\xc6\xe5\xdf\xb1k\xed'O\xd5\xf5\x8cp\xf5"
    FLASKY_POSTS_PER_PAGE = 30
    
    @staticmethod
    def init_app(app):
        pass

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://admin:admin@localhost/black_db'
    WTF_CSRF_ENABLED = False

class Develo(Config):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'postgresql://admin:admin@localhost/black_db'

config = {
    'development': Develo,
    'default': Develo,
    'testing': TestingConfig,
}