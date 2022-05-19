from apps.api.results.serializers.result import ResultsCreateSerializer
from commons.api import viewsets, mixins
from rest_framework import status
from apps.domain import models
from rest_framework.response import Response


class CreateResultViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = ResultsCreateSerializer
    permission_classes = []

    def create(self, request, *args, **kwargs):
        serializer = ResultsCreateSerializer(
            data=request.data, context=self.get_serializer_context()
        )
        serializer.is_valid(raise_exception=True)

        instance = models.Results.objects.create(
            start_date=serializer.validated_data["start_date"],
            end_date=serializer.validated_data["end_date"],
            distance=serializer.validated_data["distance"],
            city=serializer.validated_data["city"],
            date=serializer.validated_data["date"],
            earthquake=serializer.validated_data["earthquake"],
        )

        serializer = self.get_serializer(
            instance=instance, context=self.get_serializer_context()
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)
