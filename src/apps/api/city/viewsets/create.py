from apps.api.city.serializers.city import CitiesSerializer
from commons.api import viewsets, mixins
from rest_framework import status
from apps.domain import models
from rest_framework.response import Response


class CreateCityViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = CitiesSerializer
    permission_classes = []

    def create(self, request, *args, **kwargs):
        serializer = CitiesSerializer(
            data=request.data, context=self.get_serializer_context()
        )
        serializer.is_valid(raise_exception=True)

        instance = models.City.objects.create(
            name=serializer.validated_data["name"],
            country_code=serializer.validated_data["country_code"],
            latitude=serializer.validated_data["latitude"],
            longitude=serializer.validated_data["longitude"],
        )

        serializer = self.get_serializer(
            instance=instance, context=self.get_serializer_context()
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)
