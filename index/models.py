from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from django.contrib.auth.models import User

class Author(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media')
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    gender = models.CharField(max_length=10, choices=GENDER)

    def __str__(self):
        return self.user

class computer(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media')
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    gender = models.CharField(max_length=10, choices=GENDER)

    def __str__(self):
        return self.name


