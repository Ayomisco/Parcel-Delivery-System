from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ParcelViewSet, CustomerViewSet, DeliveryAgentViewSet


router = DefaultRouter()
router.register(r'parcels', ParcelViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'deliveryagents', DeliveryAgentViewSet)


urlpatterns = [
    path('', include(router.urls)),
]