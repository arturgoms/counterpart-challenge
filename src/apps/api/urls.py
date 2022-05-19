from django.urls import path, include

app_name = "api"

urlpatterns = [
    path("settings/", include("apps.api.settings.urls")),
    path("", include("apps.api.results.urls")),
    path("", include("apps.api.city.urls")),
    path("", include("apps.api.healthcheck.urls")),
]
