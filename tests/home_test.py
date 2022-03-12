from app.ext import db
from app.model.post import Post
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


@test("Usuário ver detalhes sobre o post")
def _(browser=browser_client):
    post = PostFactory.create()

    browser.visit(url_for("home.index"))
    browser.find_by_id(f"post-{post.id}").click()

    assert browser.is_text_present(post.title)
    assert browser.is_text_present(post.content)
    assert browser.is_text_present("Publicado")
