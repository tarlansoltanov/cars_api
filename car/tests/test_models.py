from django.test import TestCase
from django.db.models import Count
from ..models import Car, Rate

# Model tests

class CarTest(TestCase):
    """ Test module for Car model """

    def setUp(self):
        Car.objects.create(make='Volkswagen', model ='Passat')
        Car.objects.create(make='Volkswagen', model ='Golf')

    def test_car(self):
        volkswagen = Car.objects.filter(make='Volkswagen').all()
        passat = Car.objects.filter(model='Passat').get()
        
        self.assertEqual(volkswagen.count(), 2)
        self.assertEqual(passat.make, "Volkswagen")

    def test_car_str(self):
        passat = Car.objects.filter(model='Passat').get()
        golf = Car.objects.filter(model='Golf').get()
        
        self.assertEqual(str(passat), "Volkswagen Passat")
        self.assertEqual(str(golf), "Volkswagen Golf")


class RateTest(TestCase):
    """ Test module for Rate model """

    def setUp(self):
        test1 = Car.objects.create(make='Volkswagen', model ='Passat')
        test2 = Car.objects.create(make='Volkswagen', model ='Golf')
        test3 = Car.objects.create(make='Volkswagen', model ='Jetta')

        Rate.objects.create(car=test1, rate=5)
        Rate.objects.create(car=test2, rate=4)
        Rate.objects.create(car=test1, rate=3)

        test1.add_rate(5)

    def test_rate(self):
        passat = Car.objects.filter(model='Passat').get()
        golf = Car.objects.filter(model='Golf').get()
        jetta = Car.objects.filter(model='Jetta').get()
        
        self.assertEqual(passat.rates.count(), 3)
        self.assertEqual(golf.rates.count(), 1)
        self.assertEqual(jetta.rates.count(), 0)

    def test_avg_rate(self):
        passat = Car.objects.filter(model='Passat').get()
        golf = Car.objects.filter(model='Golf').get()
        jetta = Car.objects.filter(model='Jetta').get()
        
        self.assertEqual(passat.avg_rate(), 13/3)
        self.assertEqual(golf.avg_rate(), 4.0)
        self.assertEqual(jetta.avg_rate(), 0)
