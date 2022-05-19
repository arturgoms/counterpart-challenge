from django.urls import include, path

from rest_framework import routers

from apps.api.results.viewsets.list import ResultsListViewSet
from apps.api.results.viewsets.create import CreateResultViewSet

router = routers.DefaultRouter()
router.register("", ResultsListViewSet, basename="results")


urlpatterns = [
    path(
        "result/",
        CreateResultViewSet.as_view(actions={"post": "create"}),
        name="result-create",
    ),
    path("results/", include(router.urls)),
]
