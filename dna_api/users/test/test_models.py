import factory
from django.test import TestCase
from rest_framework.authtoken.models import Token

from dna_api.users.test.factories import UserFactory

from ..models import User, create_auth_token


class TestUserModel(TestCase):
    def setUp(self):
        self.data = {
            "username": "username",
            "password": "password",
            "email": "email@email.com",
            "first_name": "first",
            "last_name": "last",
        }

    def test_instanciate_object(self):
        instance = User.objects.create(**self.data)
        assert instance.username == self.data["username"]


class TestTokenModel(TestCase):
    def setUp(self):
        self.user_data = factory.build(dict, FACTORY_CLASS=UserFactory)
        self.user = User.objects.create(**self.user_data)
        Token.objects.all().delete()

    def test_instanciate_object(self):
        assert Token.objects.count() == 0

        create_auth_token(User, self.user, created=True)

        assert Token.objects.count() == 1
