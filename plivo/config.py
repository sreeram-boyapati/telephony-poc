import os

from os.path import join
from plivo import ROOT_DIR


class AppConfig(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY')
    WTF_CSRF_ENABLED = False
    BASIC_AUTH_USERNAME = os.environ.get('BASIC_AUTH_USERNAME')
    BASIC_AUTH_PASSWORD = os.environ.get('BASIC_AUTH_PASSWORD')
    SERVER_NAME = 'telephony-poc.herokuapp.com'


class DebugAppConfig(object):
    SQLALCHEMY_DATABASE_URI = "sqlite:////" + join(ROOT_DIR, 'sqlite.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'thisismylife'
    WTF_CSRF_ENABLED = False
    BASIC_AUTH_USERNAME = 'test'
    BASIC_AUTH_PASSWORD = 'test'

