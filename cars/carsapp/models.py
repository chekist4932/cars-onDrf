from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Car(models.Model):
    make = models.CharField(max_length=20, blank=False, null=False)
    model = models.CharField(max_length=20, blank=False, null=False)
    # year = models.DateField()
    year = models.CharField(max_length=4, blank=False, null=False)
    description = models.CharField(max_length=100, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.make} {self.model} {self.year}'
