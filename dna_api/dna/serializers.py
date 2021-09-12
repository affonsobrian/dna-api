from rest_framework import serializers

from .models import DNA, Status


class DNASerializer(serializers.ModelSerializer):
    class Meta:
        model = DNA
        fields = (
            "id",
            "dna",
            "is_mutant",
        )
        read_only_fields = ("id", "is_mutant")


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ("id", "count_mutant_dna", "count_human_dna", "ratio")
        read_only_fields = ("id", "count_mutant_dna", "count_human_dna", "ratio")
