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

    class Meta:
        model = Rate
        fields = ('id', 'car_id', 'rate')

