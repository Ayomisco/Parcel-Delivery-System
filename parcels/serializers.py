from rest_framework import serializers
from .models import Parcel, Customer, DeliveryAgent


class ParcelSerializer(serializers.ModelSerializer):
    customer = serializers.StringRelatedField()
    delivery_agent = serializers.StringRelatedField()

    class Meta:
        model = Parcel
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class DeliveryAgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryAgent
        fields = '__all__'
