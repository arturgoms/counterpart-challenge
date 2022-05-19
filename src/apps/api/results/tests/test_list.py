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


class ResultSchema(json_schema.JsonSchema):
    id = json_schema.UUIDProperty()
    start_date = json_schema.DateProperty()
    end_date = json_schema.DateProperty()
    distance = json_schema.NumberProperty()
    city = json_schema.ObjectProperty(schema=CitySchema)
    date = json_schema.DateProperty()
    earthquake = json_schema.StringProperty()


class ResultsListApiTestCase(AuthenticatedAPITestCase):
    def test_should_list(self):
        self.unauthenticated()

        self.mixer.cycle(10).blend(models.Results)

        response = self.client.get(reverse("api:results-list"))
        self.assertEqual(status.HTTP_200_OK, response.status_code)

        data = response.json()

        self.assertPaginatedSchema(ResultSchema, data)
