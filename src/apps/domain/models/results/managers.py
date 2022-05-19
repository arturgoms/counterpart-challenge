from django.db import models


class ResultsQuerySet(models.QuerySet):
    pass


class ResultsManager(models.Manager.from_queryset(ResultsQuerySet)):
    pass
