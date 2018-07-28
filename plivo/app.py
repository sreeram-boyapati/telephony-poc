import os

from flask import Flask
from flask_basicauth import BasicAuth
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from plivo.config import AppConfig
from plivo.config import DebugAppConfig

app = Flask('Plivo Application')

APP_MODE = os.environ.get('APP_MODE', 'dev')

basic_auth = BasicAuth(app)

if APP_MODE == 'dev':
    app.debug = True
    app.config.from_object(DebugAppConfig)
elif APP_MODE == 'prod':
    app.debug = False
    app.config.from_object(AppConfig)

db = SQLAlchemy(app)
import plivo.models.sms
migrate = Migrate(app, db)
