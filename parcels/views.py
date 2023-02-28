from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Parcel, Customer, DeliveryAgent
from .serializers import ParcelSerializer, CustomerSerializer, DeliveryAgentSerializer


# Create your views here.

class ParcelViewSet(viewsets.ModelViewSet):
    queryset = Parcel.objects.all()
    serializer_class = ParcelSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user.customer)

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]

class DeliveryAgentViewSet(viewsets.ModelViewSet):
    queryset = DeliveryAgent.objects.all()
    serializer_class = DeliveryAgentSerializer
    permission_classes = [IsAuthenticated]

