from django.urls import include, path

from rest_framework import routers

from apps.api.city.viewsets.list import CitiesListViewSet
from apps.api.city.viewsets.create import CreateCityViewSet

router = routers.DefaultRouter()
router.register("", CitiesListViewSet, basename="cities")


urlpatterns = [
    path(
        "city/",
        CreateCityViewSet.as_view(actions={"post": "create"}),
        name="city-create",
    ),
    path("cities/", include(router.urls)),
]
