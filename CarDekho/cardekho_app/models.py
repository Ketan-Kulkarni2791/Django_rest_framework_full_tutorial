from django.db import models
from django.core.exceptions import ValidationError


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

    def __str__(self):
        return self.name