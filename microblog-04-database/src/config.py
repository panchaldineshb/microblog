import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    """Parent configuration class."""    
    DATABASE_FILE = os.path.join(basedir, 'app.db')
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + DATABASE_FILE
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    DEBUG = True
