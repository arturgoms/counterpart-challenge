from apps.domain.models.dynamic_config_parameter.models import DynamicConfigParameter
from apps.domain.models.panel_user.models import PanelUser
from apps.domain.models.city.models import City
from apps.domain.models.user_role.models import UserRole
from apps.domain.models.results.models import Results
from apps.domain.views import *  # noqa
from django.db.models import CharField
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from commons.djutils.db import Database

from commons.models.lookups import RemovePunctuation

CharField.register_lookup(RemovePunctuation)


@receiver(post_migrate)
def enable_unaccent_postgres_extension(sender, *args, **kwargs):
    """
    Unable unccent in database
    """
    db = Database()
    db.execute("CREATE EXTENSION IF NOT EXISTS unaccent;")
