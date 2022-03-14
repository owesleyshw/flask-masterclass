from flask import url_for
from ward import test
from .fixtures import browser_client


@test("Usuário consegue criar post")
def _(browser=browser_client):
    browser.visit(url_for('home.index'))