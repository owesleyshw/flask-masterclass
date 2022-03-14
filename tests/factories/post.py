from factory.alchemy import SQLAlchemyModelFactory
from faker import Faker
from factory import SubFactory
from app.model.post import Post
from app.ext import db
from tests.factories.user import UserFactory

fake = Faker()


class PostFactory(SQLAlchemyModelFactory):
    class Meta:
        model = Post
        sqlalchemy_session = db.session
        sqlalchemy_session_persistence = "commit"

    title = fake.text(max_nb_chars=20)
    content = fake.text()
    published = True
    author = SubFactory(UserFactory)