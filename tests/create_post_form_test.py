from black import assert_equivalent
from flask import url_for
from ward import test, skip

from tests.fixtures import browser_client
from tests.factories.user import UserFactory


@test("Usuário consegue ver o formulário")
def _(browser=browser_client):

    browser.visit(url_for("home.index"))
    browser.find_by_text("Criar novo post").click()

    assert browser.status_code.is_success
    assert browser.is_element_present_by_name("title")
    assert browser.is_element_present_by_name("content")
    assert browser.is_element_present_by_name("publish")
    assert browser.is_element_present_by_name("authors")
    assert browser.is_element_present_by_value("Salvar")


@test("Usuário consegue criar post")
def _(browser=browser_client):
    user = UserFactory.create()

    browser.visit(url_for("posts.new"))

    browser.fill("title", "Post 1")
    browser.fill("content", "Exemplo de conteúdo para o post 1")
    browser.select("authors", str(user.id))
    browser.check("publish")
    browser.find_by_value("Salvar").click()

    assert browser.is_text_present("Post 1")
    assert browser.is_text_present("Exemplo de conteúdo para o post 1")
    assert browser.is_text_present("Publicado")
    assert browser.is_text_present(user.name)
