from django.test import TestCase

from ..models import DNA, Status


class TestDNAModel(TestCase):
    def setUp(self):
        self.data = {
            "dna": [
                "AAAATT",
                "AAAATT",
                "AAGGTT",
            ],
        }

    def test_instanciate_object(self):
        instance = DNA.objects.create(**self.data)
        assert instance.dna == self.data["dna"]


class TestStatusModel(TestCase):
    def setUp(self):
        self.data = {
            "count_human_dna": 2,
            "count_mutant_dna": 1,
        }
        self.dna_data = {
            "dna": [
                "AAGGTT",
                "AAGGTT",
                "AAGGTT",
            ],
        }
        self.dna = DNA.objects.create(**self.dna_data)

    def test_instanciate_object(self):
        instance = Status.objects.create(**self.data)
        assert instance.count_human_dna == self.data["count_human_dna"]
        assert instance.count_mutant_dna == self.data["count_mutant_dna"]

    def test_update_status(self):
        instance = Status.objects.first()

        assert instance.count_human_dna == 1

        Status.update_status(DNA, self.dna)

        instance = Status.objects.first()
        assert instance.count_human_dna == 2
