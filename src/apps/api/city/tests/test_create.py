import uuid

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


class CityCreateApiTestCase(AuthenticatedAPITestCase):
    def test_should_create(self):
        self.unauthenticated()

        response = self.client.post(
            reverse("api:city-create"),
            data={
                "name": self.faker.name(),
                "country_code": "BR",
                "latitude": 100,
                "longitude": 200,
            },
        )

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)

        data = response.json()

        self.assertSchema(CitySchema, data)
