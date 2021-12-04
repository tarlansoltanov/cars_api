from django.test import TestCase
from django.db.models import Count
from ..models import Car, Rate
from ..api.serializers import CarSerializer

import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse

# Initialize the APIClient app
client = Client()

# View tests
class CarsViewsetTest(TestCase):
    """ Test module for GET all cars API """

    def setUp(self):
        test1 = Car.objects.create(make='Volkswagen', model ='Passat')
        test2 = Car.objects.create(make='Volkswagen', model ='Golf')

        test1.add_rate(5)
        test2.add_rate(4)
        test1.add_rate(3)

    def test_get_all_cars(self):
        # Get API response
        response = client.get(reverse('car-list'))

        # Get data from DB
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_popular_cars(self):
        # Get API response
        response = client.get(reverse('car-popular'))

        # Get data from DB
        cars = Car.objects.all().annotate(rate_num=Count('rates')).order_by('-rate_num')
        serializer = CarSerializer(cars, many=True, context={'popular': True})

        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_car(self):
        # Get API response
        response = client.delete(reverse('car-detail', kwargs={'pk': 1}))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.assertEqual(Car.objects.filter(id=1).exists(), False)

        # Get API response
        response = client.delete(reverse('car-detail', kwargs={'pk': 10}))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_car(self):
        # Get API response
        response = client.post(reverse('car-list'), {'make': 'Volkswagen', 'model': 'Jetta'}, format='json')

        # Get data from DB
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
    
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = client.get(reverse('car-list'))
        self.assertEqual(response.data, serializer.data)

        # Get API response
        response = client.post(reverse('car-list'), {'make': 'WrongCar', 'model': 'WrongCar'}, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    
    def test_rate_car(self):
        # Get data from DB
        car = Car.objects.get(id=2)

        rates_number = car.rates.count()

        # Get API response
        response = client.post(reverse('rate-car'), {'car_id': 2, 'rating': 2}, format='json')
    
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(car.rates.count(), rates_number + 1)

        # Get API response
        response = client.post(reverse('rate-car'), {'car_id': 9, 'rating': 2}, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Get API response
        response = client.post(reverse('rate-car'), {'car_id': 2, 'rating': 7}, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)