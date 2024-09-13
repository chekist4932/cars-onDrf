from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Car(models.Model):
    make = models.CharField(max_length=20, blank=False, null=False)
    model = models.CharField(max_length=20, blank=False, null=False)
    year = models.CharField(max_length=4, blank=True, null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.make} {self.model} {self.year}'


class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=False)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.content[:20]}... {self.author} {self.created_at}'