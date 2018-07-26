from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from plivo import TEMPLATE_DIR, STATIC_DIR
from plivo.config import AppConfig

app = Flask('Plivo Application')

app.config.from_object(AppConfig)
app.debug = True

db = SQLAlchemy(app)
import plivo.models.sms
migrate = Migrate(app, db)
