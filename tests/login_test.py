import email
from flask import url_for
from ward import test

from tests.fixtures import browser_client
from tests.factories.user import UserFactory


@test("Usuário registra no sistema com sucesso")
def _(browser=browser_client):
    browser.visit(url_for("home.index"))
    browser.click_link_by_text("Registrar")
    browser.fill("name", "Wesley Júnior")
    browser.fill("email", "agarwesley19@gmail.com")
    browser.fill("password", "123456789")
    browser.find_by_value("Registrar").click()

    assert browser.is_text_present("Registro realizado com sucesso!")


@test("Usuário consegue se autenticar no sistema com sucesso")
def _(browser=browser_client):
    user = UserFactory.create(
        name="Wesley Júnior",
        email="agarwesley19@gmail.com",
        password="123456789",
    )

    browser.visit(url_for("home.index"))
    browser.click_link_by_text("Entrar")
    browser.fill("email", user.email)
    browser.fill("password", "123456789")
    browser.find_by_value("Entrar").click()

    assert browser.is_text_not_present("Registrar")
    assert browser.is_text_not_present("Entrar")
    assert browser.is_text_present("Wesley Júnior")
    assert browser.is_text_present("agarwesley19@gmail.com")
