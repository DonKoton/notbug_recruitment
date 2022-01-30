from django.db import models
from django.urls import reverse

# Create your models here.


class Car(models.Model):
    brand = models.CharField(max_length=64)
    model = models.CharField(max_length=64)
    prod_year = models.IntegerField()
    owner = models.CharField(max_length=64)

    def get_absolute_url(self):
        return reverse('cars:car_detail', args=[str(self.pk)])


class Parts(models.Model):
    name = models.CharField(max_length=255)
    producer = models.CharField(max_length=128)
    part_number = models.IntegerField()
    price = models.FloatField()
    date_of_service = models.DateField()
    mileage = models.IntegerField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('cars:car_detail', args=[str(self.car.pk)])
