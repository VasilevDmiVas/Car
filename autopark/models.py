from django.db import models

# Create your models here.

class CarType(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ['name']

class CarBrand(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']

class Car(models.Model):
    car_number = models.CharField(max_length=10)
    car_type = models.ForeignKey(CarType, on_delete=models.SET_NULL, null=True)
    car_brand = models.ForeignKey(CarBrand, on_delete=models.SET_NULL, null=True)
    is_electric = models.BooleanField(default=False)
    year = models.pozitiveIntegerField()


class ParkingSlot(models.Model):
   is_free = models.BooleanField(default=True)
   number = models.IntegerField()
   car = models.OneToOneField(Car, on_delete=models.SET_NULL, null=True)

class Meta:
    ordering = ['number']

class Parking(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    description = models.TextField(null=True)
    parking_slots = models.ForeignKey(ParkingSlot, on_delete=models.SET_NULL, null=True)



