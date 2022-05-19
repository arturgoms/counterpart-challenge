from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.domain.models.results.managers import ResultsManager
from commons.models.base import Model


class Results(Model):

    start_date = models.DateField(_("Start date"), max_length=60)

    end_date = models.DateField(_("End date"), max_length=60)

    distance = models.FloatField(_("Distance"))

    city = models.ForeignKey(
        "domain.City",
        verbose_name=_("City"),
        related_name="city_results",
        on_delete=models.CASCADE,
    )

    date = models.DateField(_("Date"), max_length=60)

    earthquake = models.CharField(_("Earthquake Description"), max_length=100)

    objects = ResultsManager()

    class Meta:
        db_table = "result"
        verbose_name = _("Result")
        verbose_name_plural = _("Results")
        ordering = ["-created_at"]

    def __str__(self):
        return self.distance
