from flask import url_for
from ward import test

from tests.fixtures import browser_client


@test("Usuário registra no sistema com sucesso")
def _(browser=browser_client):
    browser.visit(url_for("home.index"))
    browser.click_link_by_text("Registrar")
    browser.fill("name", "Wesley Júnior")
    browser.fill("email", "agarwesley19@gmail.com")
    browser.fill("password", "123456789")
    browser.find_by_value("Registrar").click()

    assert browser.is_text_present("Registro realizado com sucesso!")
