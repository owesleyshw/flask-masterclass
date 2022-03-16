from email.policy import default
from app.model.user import User
from flask_wtf import FlaskForm
from wtforms.fields import (
    StringField,
    TextAreaField,
    BooleanField,
    SelectField,
    SubmitField,
    EmailField,
    PasswordField
)


class PostForm(FlaskForm):
    title = StringField("Título")
    content = TextAreaField("Conteúdo")
    publish = BooleanField("Publicar", default=False)
    authors = SelectField("Autores", coerce=int)
    submit = SubmitField("Salvar")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.authors.choices = [
            (user.id, user.name) for user in User.query.all()
        ]

class AuthRegisterForm(FlaskForm):
    name = StringField("Nome")
    email = EmailField("E-mail")
    password = PasswordField("Senha")
    submit = SubmitField("Registrar")