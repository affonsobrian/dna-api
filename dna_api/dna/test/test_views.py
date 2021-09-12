from django.contrib.auth.hashers import check_password
from django.urls import reverse
from faker import Faker
from rest_framework import status
from rest_framework.test import APITestCase

from dna_api.dna.models import DNA, Status
from dna_api.users.models import Token

from .factories import UserFactory

fake = Faker()


class TestDNAListTestCase(APITestCase):
    def setUp(self):
        self.url = reverse("dna-list")
        self.user = UserFactory()
        self.data = {
            "dna": [
                "AACCTT",
                "AACCTT",
                "AACCTT",
                "AACCTT",
            ]
        }
        self.dna = DNA.objects.create(dna=self.data["dna"])
        self.token = f"Token {Token.objects.filter(user=self.user).first().key}"
        self.client.credentials(HTTP_AUTHORIZATION=self.token)

    def test_post_request_with_no_data_fails(self):
        response = self.client.post(self.url, {})
        assert response.status_code, status.HTTP_400_BAD_REQUEST

    def test_post_request_with_valid_data_succeeds(self):
        response = self.client.post(self.url, self.data)
        assert response.status_code == status.HTTP_201_CREATED

        dna = DNA.objects.get(pk=response.data.get("id"))
        assert dna.dna == self.data.get("dna")

    def test_list_request(self):
        response = self.client.get(self.url)

        assert response.status_code == status.HTTP_200_OK

        assert response.data["results"][0]["dna"] == self.data["dna"]


class TestUserDetailTestCase(APITestCase):
    def setUp(self):
        self.user = UserFactory()
        self.data = {
            "dna": [
                "AACCTT",
                "AACCTT",
                "AACCTT",
                "AACCTT",
            ]
        }
        self.dna = DNA.objects.create(dna=self.data["dna"])
        self.url = reverse("dna-detail", kwargs={"pk": self.dna.pk})
        self.token = f"Token {Token.objects.filter(user=self.user).first().key}"
        self.client.credentials(HTTP_AUTHORIZATION=self.token)

    def test_get_request_returns_a_given_dna(self):
        response = self.client.get(self.url)
        assert response.status_code == status.HTTP_200_OK


class TestStatusListTestCase(APITestCase):
    def setUp(self):
        self.url = "/api/v1/stats/"
        self.user = UserFactory()
        self.data = {
            "count_mutant_dna": 1,
            "count_human_dna": 2,
        }
        self.status = Status.objects.create(**self.data)
        self.token = f"Token {Token.objects.filter(user=self.user).first().key}"
        self.client.credentials(HTTP_AUTHORIZATION=self.token)

    def test_get_list_stats(self):
        response = self.client.get(self.url)

        assert response.status_code, status.HTTP_400_BAD_REQUEST
        data = dict(response.data["results"][0])

        assert data["count_mutant_dna"] == self.data["count_mutant_dna"]
        assert data["count_human_dna"] == self.data["count_human_dna"]


class TestStatusDetailTestCase(APITestCase):
    def setUp(self):
        self.user = UserFactory()
        self.data = {
            "count_mutant_dna": 1,
            "count_human_dna": 2,
        }
        self.status = Status.objects.create(**self.data)
        self.url = f"/api/v1/stats/{self.status.pk}/"
        self.token = f"Token {Token.objects.filter(user=self.user).first().key}"
        self.client.credentials(HTTP_AUTHORIZATION=self.token)

    def test_retrieve_stats(self):
        response = self.client.get(self.url)
        data = dict(response.data)

        assert response.status_code, status.HTTP_400_BAD_REQUEST

        assert data["count_mutant_dna"] == self.data["count_mutant_dna"]
        assert data["count_human_dna"] == self.data["count_human_dna"]
