from apps.domain import models
from commons.api.serializers import PartialModelSerializer


class CitiesSerializer(PartialModelSerializer):
    class Meta:
        model = models.City
        fields = ["id", "name", "country_code", "latitude", "longitude"]
