from faker import Faker
from flask import url_for
from ward import test

from tests.factories.post import PostFactory
from tests.fixtures import browser_client

fake = Faker()


@test("Usuário ver detalhes sobre o post")
def _(browser=browser_client):
    post = PostFactory.create()

    browser.visit(url_for("home.index"))
    browser.find_by_id(f"post-{post.id}").click()

    assert browser.is_text_present(post.title)
    assert browser.is_text_present(post.content)
    assert browser.is_text_present("Publicado")


@test("Usuário acessa página do post diretamente")
def _(browser=browser_client):
    post = PostFactory.create()

    browser.visit(url_for("posts.show", id=post.id))

    assert browser.is_text_present(post.title)
    assert browser.is_text_present(post.content)
    assert browser.is_text_present("Publicado")
    assert browser.is_text_present(post.author.name)


@test("Usuário deleta um post")
def _(browser=browser_client):
    post = PostFactory.create()

    browser.visit(url_for("posts.show", id=post.id))
    browser.find_by_value("Excluir").click()

    assert browser.url == "http://localhost/"
    assert browser.is_text_present("Home Page")
    assert browser.is_text_not_present(post.title)
