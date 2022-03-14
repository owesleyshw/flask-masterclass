from faker import Faker
from flask import url_for
from ward import test

from tests.factories.post import PostFactory
from tests.fixtures import browser_client

fake = Faker()


@test("Usuário visita página inicial com sucesso")
def _(browser=browser_client):
    browser.visit(url_for("home.index"))

    assert browser.status_code == 200
    assert browser.is_text_present("Home Page")


@test("Usuário ver posts")
def _(browser=browser_client):
    posts = PostFactory.create_batch(2)

    browser.visit(url_for("home.index"))

    for post in posts:
        assert browser.is_text_present(post.title)


@test("Usuário ver posts ativos")
def _(browser=browser_client):
    posts = PostFactory.create_batch(2)

    browser.visit(url_for("home.index"))

    for post in posts:
        assert browser.is_text_present(post.title)
