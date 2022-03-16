from app.ext import db
from app.form import AuthRegisterForm
from app.model.user import User
from flask import redirect, url_for, flash


class AuthController:
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
