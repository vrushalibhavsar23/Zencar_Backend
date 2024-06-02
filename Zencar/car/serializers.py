from rest_framework import serializers
from .models import CarInventory, CarSales

class CarInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CarInventory
        fields = '__all__'

class CarSalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarSales
        fields = '__all__'