from rest_framework import serializers
from ..models import Car, Rate
import requests

class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = ('id', 'make', 'model') 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.context.get('popular') == True:
            self.fields['rates_number'] = serializers.SerializerMethodField()
        else:
            self.fields['avg_rating'] = serializers.SerializerMethodField()

    def validate(self, data):
        """
        Check that if the car exists in government database.
        """
        response = requests.get(f"https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/{ data['make'].lower() }?format=json")
        results = response.json()['Results']

        if len(results) == 0:
            raise serializers.ValidationError("Car not found")

        for item in results:
            if item['Make_Name'].lower() == data['make'].lower() and item['Model_Name'].lower() == data['model'].lower():
                return data
        
        raise serializers.ValidationError("Car not found")

    def get_avg_rating(self, car):
        return car.avg_rate()

    def get_rates_number(self, car):
        return car.rates.count()

class RateSerializer(serializers.ModelSerializer):
    
    car_id = serializers.IntegerField(write_only=True)
    rating = serializers.IntegerField(write_only=True)

    class Meta:
        model = Rate
        fields = ('id', 'car_id', 'rating')

    def validate_car_id(self, value):
        """ Check that car exists """
        car = Car.objects.filter(id=value)
        if not car.exists():
            raise serializers.ValidationError("Car not found")
        return value

    def validate_rating(self, value):
        """ Check that rating is between 1 and 5 """
        if value > 5 or value < 0:
            raise serializers.ValidationError("Rating must be between 0 and 5")
        return value

    def create(self, validated_data):
        """
        Create a new rate for a car.
        """
        car_id = validated_data.get('car_id')
        rating = validated_data.get('rating')

        car = Car.objects.get(id=car_id)
        rate = Rate.objects.create(car=car, rate=rating)
        return rate
