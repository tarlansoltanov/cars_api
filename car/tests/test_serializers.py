from django.test import TestCase
from django.db.models import Count
from rest_framework import serializers
from ..models import Car, Rate
from ..api.serializers import CarSerializer, RateSerializer

# Serializer tests

class CarSerializerTest(TestCase):
    """ Test module for Car Serializer """

    def setUp(self):
        self.model_data = Car.objects.create(make='Volkswagen', model='Passat')
        self.serialized_data = {'id': self.model_data.id, 'make': 'Volkswagen', 'model': 'Passat', 'avg_rating' : 0}
        self.serializer = CarSerializer(self.model_data)

    def test_contains_expected_fields(self):
        data = self.serializer.data

        self.assertEqual(list(data.keys()), ['id', 'make', 'model', 'avg_rating'])

    def test_make_field_content(self):
        data = self.serializer.data

        self.assertEqual(data['make'], self.model_data.make)

    def test_model_field_content(self):
        data = self.serializer.data

        self.assertEqual(data['model'], self.model_data.model)

    def test_avg_rating_field_content(self):
        data = self.serializer.data

        self.assertEqual(data['avg_rating'], self.model_data.avg_rate())

    def test_car(self):
        self.assertEqual(self.serializer.data, self.serialized_data)

    def test_popular(self):
        self.popular_serialized_data = {'id': self.model_data.id, 'make': 'Volkswagen', 'model': 'Passat', 'rates_number' : 0}
        self.popular_serializer = CarSerializer(self.model_data, context={'popular': True})

        self.assertEqual(self.serializer.data, self.serialized_data)

