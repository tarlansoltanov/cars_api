from rest_framework import serializers
from ..models import Car, Rate
import requests

class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = ('id', 'make', 'model') 

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