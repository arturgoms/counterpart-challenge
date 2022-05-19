from apps.domain import models
from commons.api.serializers import PartialModelSerializer


class CitiesSerializer(PartialModelSerializer):
    class Meta:
        model = models.City
        fields = ["id", "name", "country_code", "latitude", "longitude"]


class ResultsSerializer(PartialModelSerializer):
    city = CitiesSerializer(many=False)

    class Meta:
        model = models.Results
        fields = [
            "id",
            "start_date",
            "end_date",
            "distance",
            "city",
            "date",
            "earthquake",
        ]


class ResultsCreateSerializer(PartialModelSerializer):
    class Meta:
        model = models.Results
        fields = [
            "id",
            "start_date",
            "end_date",
            "distance",
            "city",
            "date",
            "earthquake",
        ]
