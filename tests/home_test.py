from ward import test
from tests.fixtures import browser_client


@test("Usuário visita página inicial com sucesso")
def _(browser=browser_client):
    browser.visit("/")

    assert browser.status_code == 200
    assert browser.is_text_present("Home Page")