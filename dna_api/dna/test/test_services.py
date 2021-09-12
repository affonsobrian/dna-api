from django.contrib.auth.hashers import check_password
from django.forms.models import model_to_dict
from django.test import TestCase
from nose.tools import eq_, ok_

from ..services import DNAService


class TestDNAService(TestCase):
    def setUp(self):
        self.mutant_dna = [
            "ATGCGA",
            "CAGTGC",
            "TTATGT",
            "AGAAGG",
            "CCCCTA",
            "TCACTG",
        ]
        self.vertical_mutant_dna = [
            "AAACGC",
            "ACCGCC",
            "ACATGT",
            "ACAAGG",
            "CCCCTA",
            "TCACTG",
        ]
        self.regular_dna = [
            "ATGCGA",
            "CAGTGC",
            "TTATTT",
            "AGACGG",
            "GCGTCA",
            "TCACTG",
        ]

    def test_service_with_mutant(self):
        is_mutant = DNAService.is_mutant(self.mutant_dna)
        assert is_mutant == True

    def test_service_with_vertical_mutant(self):
        is_mutant = DNAService.is_mutant(self.vertical_mutant_dna)
        assert is_mutant == True

    def test_service_with_regular_dna(self):
        is_mutant = DNAService.is_mutant(self.regular_dna)
        assert is_mutant == False

    def test_service_dna_iteration_counter(self):
        count, mutant_count, last_letter = DNAService._dna_iteration_counter(
            0, 0, self.mutant_dna, 0, 0, None, 4
        )
        assert count == 1
        assert mutant_count == 0
        assert last_letter == self.mutant_dna[0][0]
