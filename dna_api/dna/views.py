from rest_framework import mixins, viewsets

from dna_api.dna.models import DNA, Status
from dna_api.dna.serializers import DNASerializer, StatusSerializer


class DNAViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    queryset = DNA.objects.all().order_by("id")
    serializer_class = DNASerializer


class StatusViewSet(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    queryset = Status.objects.all().order_by("id")
    serializer_class = StatusSerializer
