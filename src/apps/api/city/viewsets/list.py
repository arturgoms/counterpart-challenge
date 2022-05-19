import uuid
from apps.api.city.serializers.city import CitiesSerializer
from apps.domain import models
from commons.api import viewsets
from commons.djutils.api.mixins import FilterQuerysetMixin
from commons.djutils.models.filters import Search
from commons.models import filters


class CitiesListViewSet(FilterQuerysetMixin, viewsets.ListModelViewSet):
    queryset = models.City.objects.all()
    serializer_class = CitiesSerializer
    permission_classes = []

    filters = [
        filters.Filter("ids", lookup="pk", cast=uuid.UUID, many=True),
        Search(lookups=["name__icontains"]),
    ]

    def get_queryset(self):
        return super().get_queryset()
