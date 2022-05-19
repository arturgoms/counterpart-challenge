import uuid
from apps.api.results.serializers.result import ResultsSerializer
from apps.domain import models
from commons.api import viewsets
from commons.djutils.api.mixins import FilterQuerysetMixin
from commons.djutils.models.filters import Search
from commons.models import filters


class ResultsListViewSet(FilterQuerysetMixin, viewsets.ListModelViewSet):
    queryset = models.Results.objects.all()
    serializer_class = ResultsSerializer
    permission_classes = []

    filters = [
        filters.Filter("ids", lookup="pk", cast=uuid.UUID, many=True),
        Search(lookups=["city_name__icontains"]),
    ]

    def get_queryset(self):
        return super().get_queryset()
