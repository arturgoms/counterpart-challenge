from django.urls import reverse
from rest_framework import status

from apps.api.tests import AuthenticatedAPITestCase
from apps.domain import models
from commons import json_schema


class CitySchema(json_schema.JsonSchema):
    id = json_schema.UUIDProperty()
    name = json_schema.StringProperty()
    country_code = json_schema.StringProperty()
    latitude = json_schema.NumberProperty()
    longitude = json_schema.NumberProperty()


class CityListApiTestCase(AuthenticatedAPITestCase):
    def test_should_list(self):
        self.unauthenticated()

        self.mixer.cycle(10).blend(models.City)

        response = self.client.get(reverse("api:cities-list"))
        self.assertEqual(status.HTTP_200_OK, response.status_code)

        data = response.json()

        self.assertPaginatedSchema(CitySchema, data)
