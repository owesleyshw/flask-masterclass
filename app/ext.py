from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import 

db = SQLAlchemy()


def init_app(app):
    db.init_app(app)
    Migrate(app, db)
