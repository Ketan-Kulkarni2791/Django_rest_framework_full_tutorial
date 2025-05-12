from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User


def alphanumeric(value):
    if not str(value).isalnum():
        raise ValidationError('Chassis number should contain alphanumeric characters only.')
    return value


class ShowroomList(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    website = models.URLField()

    def __str__(self):
        return self.name

class CarList(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    active = models.BooleanField(default=False)
    chassisnumber = models.CharField(max_length=17, unique=True, blank=True, null=True, validators=[alphanumeric])
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    showroom = models.ForeignKey(ShowroomList, on_delete=models.CASCADE, related_name='showrooms', null=True, blank=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    apiuser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='apiuser', null=True, blank=True)
    rating = models.IntegerField(validators=[MinValueValidator, MaxValueValidator])
    comments = models.CharField(max_length=200, null=True)
    car = models.ForeignKey(CarList, on_delete=models.CASCADE, related_name='reviews', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.car.name} - {self.rating}'

    