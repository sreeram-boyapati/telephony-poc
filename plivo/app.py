import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from plivo.config import AppConfig

app = Flask('Plivo Application')

app.config.from_object(AppConfig)
APP_MODE = os.environ.get('APP_MODE', 'dev')


if APP_MODE == 'dev':
    app.debug = True
elif APP_MODE == 'prod':
    app.debug = False


db = SQLAlchemy(app)
import plivo.models.sms
migrate = Migrate(app, db)
