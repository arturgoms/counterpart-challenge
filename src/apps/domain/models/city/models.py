from django.db import models
from django.utils.translation import gettext_lazy as _
from commons.models.base import Model


class City(Model):

    name = models.CharField(_("Name"), max_length=60)

    country_code = models.CharField(_("Country Code"), max_length=10)

    latitude = models.FloatField(_("Latitude"))

    longitude = models.FloatField(_("Longitude"))

    class Meta:
        db_table = "city"
        verbose_name = _("City")
        verbose_name_plural = _("Cities")
        ordering = ["name"]

    def __str__(self):
        return self.name
