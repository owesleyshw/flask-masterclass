from factory.alchemy import SQLAlchemyModelFactory
from app.model.user import User
from app.ext import db

from faker import Faker

fake = Faker()


class UserFactory(SQLAlchemyModelFactory):
    class Meta:
        model = User
        sqlalchemy_session = db.session

    name = fake.name()
