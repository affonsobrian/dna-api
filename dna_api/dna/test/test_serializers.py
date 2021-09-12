from django.contrib.auth.hashers import check_password
from django.forms.models import model_to_dict
from django.test import TestCase
from nose.tools import eq_, ok_

from ..models import Status
from ..serializers import DNASerializer, StatusSerializer


class TestDNASerializer(TestCase):
    def setUp(self):
        self.data = {
            "dna": [
                "AAGGTT",
                "AAGGTT",
                "AAGGTT",
            ],
        }

    def test_serializer_with_empty_data(self):
        serializer = DNASerializer(data={})
        assert serializer.is_valid() == False

    def test_serializer_with_valid_data(self):
        serializer = DNASerializer(data=self.data)
        assert serializer.is_valid() == True

        instance = serializer.save()

        assert instance.dna == self.data["dna"]
        assert instance.dna == self.data["dna"]


class TestStatusSerializer(TestCase):
    def setUp(self):
        self.data = {
            "count_human_dna": 2,
            "count_mutant_dna": 1,
        }
        self.status = Status.objects.create(**self.data)

    def test_serializer_with_empty_data(self):
        serializer = StatusSerializer(data={})
        assert serializer.is_valid() == True

    def test_serializer_with_valid_data(self):
        serializer = StatusSerializer(data=self.data)
        assert serializer.is_valid() == True

    def test_serializer_from_object(self):
        serializer = StatusSerializer(instance=self.status)
        data = serializer.data

        assert data["count_human_dna"] == self.status.count_human_dna
        assert data["count_mutant_dna"] == self.status.count_mutant_dna
