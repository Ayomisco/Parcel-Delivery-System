from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Custom User model to add extra fields
    """
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)



    groups = models.ManyToManyField(
        to='auth.Group',
        related_name='parcel_users',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_query_name='parcel_user',
    )

    user_permissions = models.ManyToManyField(
        # Permission,
        'auth.Permission',
        related_name='parcel_users',
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='parcel_user',
    )

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['created_at']

    def __str__(self):
        return f"{self.phone}"


class DeliveryAgent(models.Model):
    """
    Model for Delivery Agent
    """
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    vehicle_type = models.CharField(max_length=50)
    vehicle_plate_number = models.CharField(max_length=20)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Delivery Agent'
        verbose_name_plural = 'Delivery Agents'
        ordering = ['id']


class Customer(models.Model):
    """
    Model for Customer
    """
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
        ordering = ['id']

    def __str__(self):
        return f"{self.name}"



class Parcel(models.Model):
    """
    Model for Parcel
    """
    STATUS_CHOICES = [
        ('CREATED', 'Created'),
        ('IN_TRANSIT', 'In Transit'),
        ('DELIVERED', 'Delivnameered'),
        ('CANCELLED', 'Cancelled'),
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    recipient_name = models.CharField(max_length=255)
    recipient_phone = models.CharField(max_length=20)
    pickup_address = models.CharField(max_length=255)
    delivery_address = models.CharField(max_length=255)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='CREATED')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='parcels_created')
    delivery_agent = models.ForeignKey(DeliveryAgent, on_delete=models.SET_NULL, null=True, blank=True, related_name='parcels_assigned')

    class Meta:
        verbose_name = 'Parcel'
        verbose_name_plural = 'Parcels'
        ordering = ['id']

    def __str__(self):
        return f"{self.name}"
