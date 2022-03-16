from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()


def init_app(app):
    db.init_app(app)
    Migrate(app, db)
    login_manager.init_app(app)
