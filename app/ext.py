from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = "auth.login"
login_manager.login_message = (
    "Você precisa se autenticar para acessar a página!"
)


def init_app(app: Flask):
    db.init_app(app)
    Migrate(app, db)
    login_manager.init_app(app)

    @app.shell_context_processor
    def shell_context_processor():
        from app.model.user import User
        from app.model.post import Post

        return dict(app=app, db=db, User=User, Post=Post)
