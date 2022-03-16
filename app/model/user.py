from app.ext import db, login_manager
from flask_login import UserMixin
from sqlalchemy import event
from werkzeug.security import generate_password_hash


@login_manager.user_loader
def get_current_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(84), nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    posts = db.relationship("Post", backref="author")  # one to many


@event.listens_for(User, "before_insert")
def encrypt_user_password(mapper, connect, target):
    target.password = generate_password_hash(target.password)
