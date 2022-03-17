from flask import url_for
from ward import test

from tests.fixtures import browser_client
from tests.factories.user import UserFactory


@test("Usuário sem autenticação não conseguem criar posts")
def _(browser=browser_client):
    browser.visit(url_for("home.index"))

    assert browser.is_text_not_present("Criar novo post")


@test("Usuário sem autenticação não conseguem acessar a página de criar posts")
def _(browser=browser_client):
    browser.visit(url_for("posts.new"))

    assert browser.is_text_present(
        "Você precisa se autenticar para acessar a página!"
    )


@test("Usuário consegue criar post")
def _(browser=browser_client):
    user = UserFactory.create(
        name="Wesley Júnior",
        email="agarwesley19@gmail.com",
        password="123456789",
    )

    browser.visit(url_for("auth.login"))
    browser.fill("email", user.email)
    browser.fill("password", user.password)
    browser.find_by_value("Entrar").click()

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
