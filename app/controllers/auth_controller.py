from app.ext import db
from app.form import AuthLoginForm, AuthRegisterForm
from app.model.user import User
from flask import redirect, url_for, flash
from werkzeug.security import check_password_hash
from flask_login import login_user


class AuthController:
    def login(self, view, request):
        return view("auth/login.html", form=AuthLoginForm())

    def logged(self, view, request):
        form = AuthLoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()

            if not user or not check_password_hash(user.password, form.password.data):
                flash("E-mail ou senha inválidos")
                return redirect(url_for("auth.login"))

            login_user(user)
            return redirect(url_for("home.index"))

    def register(self, view, request):
        return view("auth/register.html", form=AuthRegisterForm())

    def registered(self, view, request):
        form = AuthRegisterForm()
        if form.validate_on_submit():
            user = User(
                name=form.name.data,
                email=form.email.data,
                password=form.password.data,
            )
            db.session.add(user)
            db.session.commit()
            flash("Registro realizado com sucesso!")
            return redirect(url_for("auth.register"))
