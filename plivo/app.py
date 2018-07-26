from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from plivo import TEMPLATE_DIR, STATIC_DIR
from plivo.config import AppConfig

app = Flask(
        'Plivo Application',
        template_folder=TEMPLATE_DIR,
        static_url_path='/static',
        static_folder=STATIC_DIR)
app.config.from_object(AppConfig)
app.debug = True

db = SQLAlchemy(app)
import plivo.models.
import plivo.models.settlements
import plivo.models.merchants
migrate = Migrate(app, db)
