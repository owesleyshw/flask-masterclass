from ward import fixture
from splinter import Browser

from app import create_app
from app.ext import db

@fixture
def browser_client():
    app = create_app()
    app.testing = True
    app_context = app.test_request_context()
    app_context.push()

    with app.test_client():
        db.create_all()
        yield Browser("flask", app=app)
    
    db.session.remove()
    db.drop_all()