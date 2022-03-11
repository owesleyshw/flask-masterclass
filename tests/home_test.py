from flask import url_for
from ward import test
from faker import Faker

from tests.fixtures import browser_client
from app.model.post import Post
from app.ext import db

fake = Faker()

@test("Usuário visita página inicial com sucesso")
def _(browser=browser_client):
    browser.visit(url_for("home.index"))

    assert browser.status_code == 200
    assert browser.is_text_present("Home Page")

@test("Usuário ver posts")
def _(browser=browser_client):
    p1 = Post(title="Post 1", content="Conteúdo de exemplo do post 1", published=True)
    p2 = Post(title="Post 2", content="Conteúdo de exemplo do post 2", published=True)
    
    db.session.add(p1)
    db.session.add(p2)
    db.session.commit()
    
    browser.visit(url_for("home.index"))

    assert browser.is_text_present("Post 1")
    assert browser.is_text_present("Post 2")

@test("Usuário ver posts ativos")
def _(browser=browser_client):
    p1 = Post(title="Post 1", content="Conteúdo de exemplo do post 1", published=True)
    p2 = Post(title="Post 2", content="Conteúdo de exemplo do post 2", published=False)
    
    db.session.add(p1)
    db.session.add(p2)
    db.session.commit()
    
    browser.visit(url_for("home.index"))

    assert browser.is_text_present("Post 1")
    assert browser.is_text_not_present("Post 2")

@test("Usuário ver detalhes sobre o post")
def _(browser=browser_client):
    p = Post(title=fake.name(), content=fake.text(), published=True)
    db.session.add(p)
    db.session.commit()
    
    browser.visit(url_for("home.index"))
    post = browser.find_by_id(f'post-{p.id}')
    post.click()

    assert browser.is_text_present(p.title)
    assert browser.is_text_present(p.content)
    assert browser.is_text_present('Publicado')
