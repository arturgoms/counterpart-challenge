import uuid

from django.urls import reverse
from rest_framework import status

from apps.api.tests import AuthenticatedAPITestCase
from apps.domain import models
from commons import json_schema


class ResultSchema(json_schema.JsonSchema):
    id = json_schema.UUIDProperty()
    start_date = json_schema.DateProperty()
    end_date = json_schema.DateProperty()
    distance = json_schema.NumberProperty()
    city = json_schema.UUIDProperty()
    date = json_schema.DateProperty()
    earthquake = json_schema.StringProperty()


class ResultCreateApiTestCase(AuthenticatedAPITestCase):
    def test_should_create(self):
        self.unauthenticated()

        city = self.mixer.blend(models.City)
        response = self.client.post(
            reverse("api:result-create"),
            data={
                "start_date": "2022-5-01",
                "end_date": "2022-6-01",
                "distance": 680,
                "city": city.id,
                "date": "2022-5-10",
                "earthquake": "M 5.4 - South Sandwich Islands region",
            },
        )

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)

        data = response.json()

        self.assertSchema(ResultSchema, data)
